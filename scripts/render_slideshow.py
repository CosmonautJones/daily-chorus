import argparse
import json
import subprocess
import os
from pathlib import Path


def run(args):
    subprocess.run(args, check=True)


def ass_time(seconds):
    cs = round(seconds * 100)
    return f"{cs // 360000}:{cs // 6000 % 60:02}:{cs // 100 % 60:02}.{cs % 100:02}"


def captions(path, size, title, duration, scenes, lyrics):
    width, height = size
    vertical = height > width
    font_size = 48 if vertical else 46
    margin = 220 if vertical else 85
    header = f"""[Script Info]
ScriptType: v4.00+
PlayResX: {width}
PlayResY: {height}
WrapStyle: 0

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Lyric,Arial,{font_size},&H00FFFFFF,&H00FFFFFF,&H00100B06,&H900D0804,1,0,0,0,100,100,0,0,3,10,0,2,75,75,{margin},1
Style: Brand,Arial,28,&H00A1C9FF,&H00FFFFFF,&H00100B06,&H900D0804,1,0,0,0,100,100,1,0,3,7,0,7,65,65,65,1
Style: Topic,Arial,{font_size},&H00A1C9FF,&H00FFFFFF,&H00100B06,&H900D0804,1,0,0,0,100,100,0,0,3,10,0,8,75,75,{120 if vertical else 75},1
Style: Disclosure,Arial,22,&H00FFFFFF,&H00FFFFFF,&H00100B06,&H900D0804,0,0,0,0,100,100,0,0,3,5,0,1,65,65,{135 if vertical else 35},1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
    events = []
    def event(start, end, style, text):
        text = text.replace("\n", r"\N").replace("{", "").replace("}", "")
        events.append(f"Dialogue: 0,{ass_time(start)},{ass_time(end)},{style},,0,0,0,,{text}")
    event(0, duration, "Brand", "DAILY CHORUS / " + title)
    event(0, duration, "Disclosure", "AI music + original AI illustrations / REVIEW PREVIEW")
    for scene in scenes:
        event(scene["start"] + 0.5, min(scene["end"], scene["start"] + 5.5), "Topic", scene["label"])
    for lyric in lyrics:
        event(lyric["start"], lyric["end"], "Lyric", lyric["text"])
    path.write_text(header + "\n".join(events) + "\n", encoding="utf-8")


parser = argparse.ArgumentParser(description="Render a local illustrated song and a vertical chorus preview. Does not upload.")
parser.add_argument("timeline", type=Path)
args = parser.parse_args()
spec = json.loads(args.timeline.read_text(encoding="utf-8-sig"))
root = args.timeline.resolve().parent
output = root / "renders"
output.mkdir(exist_ok=True)
duration = float(json.loads(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "json", str(root / spec["audio"])]))["format"]["duration"])
scenes = spec["scenes"]
if not scenes or scenes[0]["start"] != 0 or abs(scenes[-1]["end"] - duration) > 0.05:
    raise ValueError("Scenes must cover the complete audio")
for previous, current in zip(scenes, scenes[1:]):
    if abs(previous["end"] - current["start"]) > 0.001:
        raise ValueError("Scenes must be contiguous")
clip = spec["clip"]
if not 20 <= clip["end"] - clip["start"] <= 30 or not 0 <= clip["start"] < clip["end"] <= duration:
    raise ValueError("Clip must be 20–30 seconds within the audio")
for scene in scenes:
    if not (root / scene["image"]).is_file() or scene["end"] <= scene["start"]:
        raise ValueError("Each scene needs an image and positive duration")

parts = []
for i, scene in enumerate(scenes):
    length = scene["end"] - scene["start"]
    frames = round(length * 24)
    part = output / f"scene-{i:02}.mp4"
    vf = f"scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,setsar=1,fade=t=in:st=0:d=0.35,fade=t=out:st={length-0.35}:d=0.35"
    run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-loop", "1", "-framerate", "24", "-i", str(root / scene["image"]), "-vf", vf, "-frames:v", str(frames), "-c:v", "libx264", "-preset", "veryfast", "-crf", "21", "-pix_fmt", "yuv420p", "-an", str(part)])
    parts.append(part.name)
    print(f"Scene {i+1}/{len(scenes)} rendered", flush=True)
(output / "concat.txt").write_text("\n".join(f"file '{name}'" for name in parts), encoding="utf-8")
full_ass = output / "full.ass"
captions(full_ass, (1920, 1080), spec["title"], duration, scenes, spec.get("lyrics", []))
full = output / "make-room-full.mp4"
os.chdir(output)
run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", "concat.txt", "-i", str(root / spec["audio"]), "-map", "0:v:0", "-map", "1:a:0", "-vf", "subtitles=full.ass", "-t", str(duration), "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", full.name],)
clip_length = clip["end"] - clip["start"]
clip_lyrics = [{"start": max(0, line["start"] - clip["start"]), "end": min(clip_length, line["end"] - clip["start"]), "text": line["text"]} for line in spec.get("lyrics", []) if line["end"] > clip["start"] and line["start"] < clip["end"]]
captions(output / "vertical.ass", (1080, 1920), spec["title"], clip_length, [{"start": 0, "end": clip_length, "label": "MAKE ROOM FOR TOMORROW"}], clip_lyrics)
run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-loop", "1", "-framerate", "24", "-i", str(root / clip["image"]), "-ss", str(clip["start"]), "-i", str(root / spec["audio"]), "-vf", "scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,setsar=1,subtitles=vertical.ass,fade=t=in:st=0:d=0.3", "-t", str(clip_length), "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k", "-af", "afade=t=in:st=0:d=0.15,afade=t=out:st="+str(clip_length-0.4)+":d=0.4", "-movflags", "+faststart", "make-room-vertical.mp4"])
print("Full and vertical previews ready", flush=True)

