import array
import hashlib
import json
import math
import subprocess
import sys
import time
import wave
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont, ImageOps

timeline = Path(sys.argv[1]).resolve()
root = timeline.parent
data = json.loads(timeline.read_text(encoding='utf-8-sig'))
work = root/'video-work'
work.mkdir(exist_ok=True)
W, H, FPS = 1920, 1080, 30
shots = data['shots']
audio = (root/data['audio']).resolve()
duration = float(json.loads(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','json',str(audio)]))['format']['duration'])
assert abs(shots[0]['start']) < .001 and abs(shots[-1]['end']-duration) < .05
for i, shot in enumerate(shots):
    assert (root/shot['image']).is_file() and shot['end'] > shot['start']
    if i:
        assert abs(shot['start']-shots[i-1]['end']) < .001
for cue in data.get('lyrics', []):
    assert 0 <= cue['start'] < cue['end'] <= duration+.05


def run(args, name):
    command = ['ffmpeg','-nostdin','-hide_banner','-v','error','-y']+args
    with (work/(name+'.log')).open('wb') as log:
        result = subprocess.run(command, cwd=root, stdout=log, stderr=log)
    if result.returncode:
        raise RuntimeError((work/(name+'.log')).read_text(errors='replace'))


encoder = ['-c:v',data.get('encoder','libx264'),'-pix_fmt','yuv420p']
if data.get('encoder') == 'h264_nvenc':
    encoder += ['-preset','p4','-cq','20','-b:v','0']
else:
    encoder += ['-threads','2','-preset','veryfast','-crf','19']

sheet = Image.new('RGB',(1280, math.ceil(len(shots)/4)*202),'#081b2c')
small_font = ImageFont.truetype('C:/Windows/Fonts/arial.ttf',13)
for i, shot in enumerate(shots):
    art = Image.open(root/shot['image']).convert('RGB')
    zoom = sum(shot.get('zoom',[1.02,1.08]))/2
    cw = art.width/zoom
    ch = cw*H/W
    cx, cy = shot.get('center',[.5,.5])
    x = max(0,min(art.width-cw,cx*art.width-cw/2))
    y = max(0,min(art.height-ch,cy*art.height-ch/2))
    thumb = art.resize((320,180),Image.Resampling.LANCZOS,box=(x,y,x+cw,y+ch))
    sheet.paste(thumb,(i%4*320,i//4*202))
    ImageDraw.Draw(sheet).text((i%4*320+6,i//4*202+182),f'{i+1:02} / {shot["start"]:.1f}s / {shot.get("purpose","")[:27]}',font=small_font,fill='#fff2d6')
sheet.save(root/'shot-plan.jpg',quality=92)
if sys.argv[2:] == ['stills']:
    print(f'{len(shots)} shot compositions ready',flush=True)
    sys.exit(0)

started = time.perf_counter()
run(['-i',str(audio),'-vn','-ac','1','-ar','8000','-c:a','pcm_s16le',str(work/'rms.wav')],'rms')
with wave.open(str(work/'rms.wav')) as wav:
    samples = array.array('h',wav.readframes(wav.getnframes()))
levels=[]
for i in range(round(duration*FPS)+1):
    a,b=round(i*8000/FPS),round((i+1)*8000/FPS)
    window=samples[a:b]
    rms=math.sqrt(sum(x*x for x in window)/max(1,len(window)))/32768
    levels.append(20*math.log10(max(rms,1e-8)))
active=sorted(x for x in levels if x>-50)
lo,hi=active[len(active)//10],active[len(active)*9//10]
energy=[max(0,min(1,(x-lo)/max(1,hi-lo)))**.7 for x in levels]
(root/'audio-energy.json').write_text(json.dumps({'source':'measured mono RMS, dBFS, not beat detection','fps':FPS,'levels':levels}),encoding='utf-8')

# These are native graphic overlays, not substituted editorial illustrations.
for kind in ['rain','dust','confetti']:
    im=Image.new('RGBA',(W,H*2))
    d=ImageDraw.Draw(im)
    for i in range(130):
        x,y=(i*137)%W,(i*281)%(H*2)
        if kind=='rain':
            d.line((x,y,x-10,y+32),fill=(125,220,224,55),width=2)
        elif kind=='dust':
            d.ellipse((x,y,x+3,y+3),fill=(255,203,110,75))
        else:
            d.polygon([(x,y),(x+9,y+3),(x+7,y+17),(x-3,y+13)],fill=(255,194,78,120) if i%3 else (80,223,213,120))
    im.save(work/(kind+'.png'))

clips=[]
metrics=[]
for i,shot in enumerate(shots):
    tick=time.perf_counter()
    frames=round(shot['end']*FPS)-round(shot['start']*FPS)
    length=frames/FPS
    raw=work/f'shot-{i:03}-raw.mp4'
    final=work/f'shot-{i:03}.mp4'
    z0,z1=shot.get('zoom',[1.02,1.08])
    cx,cy=shot.get('center',[.5,.5])
    pan=f"zoompan=z='{z0}+({z1}-{z0})*on/{max(1,frames-1)}':x='max(0,min(iw-iw/zoom,iw*{cx}-iw/zoom/2))':y='max(0,min(ih-ih/zoom,ih*{cy}-ih/zoom/2))':d=1:s={W}x{H}:fps={FPS},setsar=1"
    args=['-loop','1','-framerate',str(FPS),'-i',str(root/shot['image'])]
    filters=[f'[0:v]{pan}[base]']
    current='base'
    input_index=1
    if shot.get('weather'):
        kind=shot['weather']
        args+=['-loop','1','-framerate',str(FPS),'-i',str(work/(kind+'.png'))]
        speed=340 if kind=='rain' else 45
        filters.append(f"[{current}][{input_index}:v]overlay=x=0:y='-{H}+mod((t+{shot['start']})*{speed},{H})':shortest=1[weather]")
        current='weather'
        input_index+=1
    if shot.get('sprite'):
        args+=['-loop','1','-framerate',str(FPS),'-i',str(root/shot['sprite'])]
        hero_x=shot.get('sprite_x',.55)*W
        hero_y=shot.get('sprite_y',135)
        commands=work/f'shot-{i:03}.cmd'
        commands.write_text('\n'.join(f'{n/FPS:.5f} overlay@hero y {hero_y-22*energy[min(len(energy)-1,round(shot["start"]*FPS)+n)]:.3f};' for n in range(frames)),encoding='utf-8')
        filters.append(f"[{current}]sendcmd=f='video-work/{commands.name}'[timed]")
        filters.append(f"[{input_index}:v]scale=-1:{shot.get('sprite_height',770)},rotate='0.025*sin(3*t)':c=none:ow=iw:oh=ih[hero]")
        filters.append(f"[timed][hero]overlay@hero=x='{hero_x}-w/2+15*sin(t*2.8)':y={hero_y}:shortest=1[character]")
        current='character'
    filters.append(f'[{current}]format=yuv420p[v]')
    args+=['-filter_complex_threads','1','-filter_complex',';'.join(filters),'-map','[v]','-frames:v',str(frames),'-an']+encoder+[str(raw)]
    run(args,f'shot-{i:03}-render')
    transition=shot.get('transition','cut')
    if i and transition!='cut':
        previous=work/f'shot-{i-1:03}-last.jpg'
        effect={'paper':'diagtl','iris':'circleopen','whip':'slideleft','shutter':'wipeleft'}.get(transition,transition)
        run(['-loop','1','-framerate',str(FPS),'-i',str(previous),'-i',str(raw),'-filter_complex_threads','1','-filter_complex',
             f'[0:v]trim=duration=0.3,settb=1/30,setpts=PTS-STARTPTS,format=yuv444p[a];[1:v]settb=1/30,setpts=PTS-STARTPTS,format=yuv444p[b];[a][b]xfade=transition={effect}:duration=0.3:offset=0,format=yuv420p[v]',
             '-map','[v]','-frames:v',str(frames),'-an']+encoder+[str(final)],f'shot-{i:03}-transition')
    else:
        raw.replace(final)
    run(['-ss',str(max(0,length-1/FPS)),'-i',str(final),'-frames:v','1',str(work/f'shot-{i:03}-last.jpg')],f'shot-{i:03}-last')
    clips.append(final)
    metrics.append({'shot':i+1,'frames':frames,'seconds':time.perf_counter()-tick,'transition':transition})
    (root/'render-progress.json').write_text(json.dumps({'completed':i+1,'total':len(shots),'shots':metrics},indent=2),encoding='utf-8')
    print(f'Shot {i+1}/{len(shots)}: {frames} frames in {time.perf_counter()-tick:.1f}s',flush=True)

def ass_time(seconds):
    n=round(seconds*100)
    return f'{n//360000}:{n//6000%60:02}:{n//100%60:02}.{n%100:02}'


def ass_text(value):
    return value.replace('\\','\\\\').replace('{','\\{').replace('}','\\}').replace('\n','\\N')


ass='''[Script Info]
ScriptType: v4.00+
PlayResX: 1920
PlayResY: 1080
WrapStyle: 0
[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Lyric,Arial,48,&H00E6F4FF,&H00E6F4FF,&H00100B07,&H80100B07,-1,0,0,0,100,100,0,0,3,4,0,2,100,100,60,1
Style: Brand,Arial,24,&H00D6F2FF,&H00D6F2FF,&H80100B07,&H80100B07,-1,0,0,0,100,100,1,0,1,2,0,7,72,72,38,1
Style: Date,Arial,22,&H00D6F2FF,&H00D6F2FF,&H80100B07,&H80100B07,0,0,0,0,100,100,0,0,1,2,0,9,72,72,38,1
Style: Topic,Arial,32,&H00DCE458,&H00DCE458,&H90100B07,&H90100B07,-1,0,0,0,100,100,0,0,3,9,0,7,72,72,106,1
Style: Title,Impact,120,&H0057BDFF,&H0057BDFF,&H90100B07,&H90100B07,0,0,0,0,100,100,0,0,1,3,0,7,85,85,365,1
[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
'''
events=[(0,duration,'Brand','DAILY CHORUS'),(0,duration,'Date',data['reporting_date']+' / '+data['genre'])]
events += [(c['start'],c['end'],'Lyric',c['text']) for c in data.get('lyrics',[])]
events += [(c['start'],c['end'],'Topic',c['text']) for c in data.get('cards',[])]
events += [(c['start'],c['end'],'Title',c['text']) for c in data.get('titles',[])]
for start,end,style,text in events:
    ass+=f'Dialogue: 1,{ass_time(start)},{ass_time(end)},{style},,0,0,0,,{ass_text(text)}\n'
(work/'captions.ass').write_text(ass,encoding='utf-8-sig')
(work/'concat.txt').write_text('\n'.join("file '"+p.as_posix().replace("'","'\\''")+"'" for p in clips),encoding='utf-8')
output=root/data.get('output','music-video.mp4')
run(['-f','concat','-safe','0','-i',str(work/'concat.txt'),'-i',str(audio),'-vf',"ass='video-work/captions.ass'",
     '-map','0:v:0','-map','1:a:0','-t',str(duration)]+encoder+['-c:a','aac','-b:a','192k','-ac','2','-movflags','+faststart',str(output)],'final')
probe=json.loads(subprocess.check_output(['ffprobe','-v','error','-show_streams','-show_format','-of','json',str(output)]))
v=next(s for s in probe['streams'] if s['codec_type']=='video')
a=next(s for s in probe['streams'] if s['codec_type']=='audio')
assert (v['width'],v['height'],v['r_frame_rate'],a['channels'])==(W,H,'30/1',2)
assert abs(float(probe['format']['duration'])-duration)<.06
decoded=subprocess.run(['ffmpeg','-nostdin','-v','error','-i',str(output),'-f','null','-'],capture_output=True)
assert decoded.returncode==0 and not decoded.stderr,decoded.stderr.decode(errors='replace')
proof={'output':str(output),'sha256':hashlib.sha256(output.read_bytes()).hexdigest(),'bytes':output.stat().st_size,
       'duration':float(probe['format']['duration']),'source_audio_duration':duration,'frames':v.get('nb_frames'),
       'width':W,'height':H,'fps':FPS,'audio_channels':a['channels'],'full_decode_exit':0,'decode_errors':'',
       'render_seconds':time.perf_counter()-started,'shots':len(shots),'model_calls_per_frame':0,
       'encoder':data.get('encoder','libx264'),'human_listening_qa':'pending','timing_source':data.get('timing_source','provided cues')}
(root/'verification.json').write_text(json.dumps(proof,indent=2),encoding='utf-8')
print(json.dumps(proof,indent=2),flush=True)
