# Render a directed music video

Use the [video-director skill](../skills/daily-chorus-video-director/SKILL.md) to plan the recurring story and shot changes. The directed renderer needs Python with Pillow, FFmpeg/ffprobe, local audio and original art. Run it from the repository root:

```powershell
python scripts/render_music_video.py C:\path\to\private-packet\timeline.json stills
python scripts/render_music_video.py C:\path\to\private-packet\timeline.json
```

The first command creates a shot contact sheet; inspect it before the full render. A timeline uses this shape (replace sample timings with the actual audio duration):

```json
{
  "audio": "selected.mp3",
  "output": "music-video.mp4",
  "reporting_date": "2026-10-14",
  "genre": "TECHNO",
  "encoder": "h264_nvenc",
  "shots": [
    {"start": 0, "end": 120, "image": "assets/scene.png", "zoom": [1.02, 1.10], "center": [0.5, 0.5], "transition": "cut", "purpose": "Establish the story"}
  ],
  "lyrics": [],
  "cards": [{"start": 3, "end": 8, "text": "DATED NEWS CONTEXT"}],
  "titles": []
}
```

Shots must cover the complete audio contiguously. Relative paths resolve beside the timeline. Optional shot fields: `weather` (`rain`, `dust`, `confetti`), `sprite` (transparent PNG), `sprite_x` (fraction of frame width), `sprite_y` and `sprite_height` (pixels). Supported transitions include `cut`, `paper`, `iris`, `whip`, and `shutter`; non-cut transitions reveal the incoming shot over the preceding final frame for 0.3 seconds. Caption entries use start/end seconds and text. Use real cues or omit karaoke when timing is uncertain.

The output is 1920×1080/30fps H.264 with stereo AAC. Omit `encoder` to use CPU `libx264`; select `h264_nvenc` only after verifying it works on the local machine. The renderer saves progress, a contact sheet and full-decode/duration verification. It does not generate art, transcribe, upload or establish listening approval. It replaces outputs in its private working folder on rerun; preserve approved revisions separately.

## Simple slideshow fallback

The first renderer uses Python's standard library and installed FFmpeg/ffprobe. It takes local audio, original illustrations, and an explicitly reviewed timeline. It does not search, generate music/art, upload, or post.

Run from the repository root; the private packet can be elsewhere:

```powershell
python scripts/render_slideshow.py C:\path\to\private-packet\timeline.json
```

A timeline names a local audio file, a title, contiguous scenes covering the audio, optional timed lyrics, and a 20–30 second clip. Paths to media are relative to the timeline file. Each scene includes start/end seconds, image, and a short topic label. Clip fields are start/end seconds and image.

Example shape:

```json
{
  "title": "SONG TITLE",
  "audio": "selected.mp3",
  "scenes": [
    {"start": 0, "end": 120, "image": "visuals/cover.png", "label": "TODAY'S MEDLEY"}
  ],
  "lyrics": [],
  "clip": {"start": 30, "end": 55, "image": "visuals/cover.png"}
}
```

Replace example timings with actual audio cues. The renderer checks scene coverage, gaps, image availability, and clip bounds. It writes 1920×1080 full and 1080×1920 vertical MP4s under the packet's `renders` folder. Both use 24 fps H.264 video, AAC audio, readable labels, and gentle fades. Optional captions use the supplied times; the renderer does not infer or verify lyrics.

Re-running replaces renderer outputs in that private folder; keep approved exports separately before revising. These files stay outside the public repository. Complete decode and dimensions/duration checks establish technical integrity; they do not replace listening and editorial approval.
