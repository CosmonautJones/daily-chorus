# Render the illustrated slideshow

The first renderer uses Python's standard library and installed FFmpeg/ffprobe. It takes local audio, original illustrations, and an explicitly reviewed timeline. It does not search, generate music/art, upload, or post.

Run from any directory:

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
