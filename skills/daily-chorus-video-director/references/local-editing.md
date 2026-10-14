# Local editing: verified lessons

## October 14, 2026 — story pilot accepted

V1 held a large title and one illustration. Travis requested multiple edits, transitions and story progression. The accepted revision used thirteen shots over 25 seconds: kitchen receipt → coin/medal match → economic research → disputed diesel split → receipt bridge → warehouse release → story triptych → closing title. His response was “perfection”; this is feedback on the pilot, not evidence of retention or calibrated quality.

Four new generated assets (kitchen, city, warehouse, transparent heroine) plus two existing editorial images supplied the cut. Full-bleed art and small branding gave the story room. Reframing yielded useful detail inserts without more image calls. A recurring character/object made cuts legible. “Bills down” stayed a wish; news was dated October 12. Brief topic cards contextualized the chorus; the full informative verses were outside this excerpt.

Pillow composed camera and cutout transforms, rain, light, paper and coins. FFmpeg encoded; Kinocut 1.16.1's Python client muxed audio and read media information. Measured RMS windows were dBFS loudness, not frequencies or verified beats. Output: 1920×1080, 30fps, 25 seconds, 750 frames, stereo AAC/H.264. Complete decode and browser playback passed. Human listening QA remained pending.

Private example on Travis's workstation: outputs/daily-chorus/2026-10-12/animation-pilot-v2 contains shot plan, exact prompts/hashes, renderer, actual Kinocut calls, encoded transition checks and playback evidence. It is an example, not a required path or portable dependency.

The render took 243 seconds for 25 seconds. Profile before scaling to full songs: cache gradients/overlays, avoid repeated resampling and use FFmpeg filters where suitable. Do not lower quality silently. Verify complete coverage and transitions after optimization.

## Tool boundaries observed

- Kinocut's kino.exe launcher failed with a uv trampoline path error; its isolated Python client worked. Locate the live environment before use; do not assume the wrapper is repaired.
- PAIR routes inference requests, not image animation. This pilot did not use NVIDIA inference, Hyperframes or a generated-video model.
- motion-craft is scoped to native Higgsedit. It does not govern ordinary local Python animation.
- A transparent cutout can translate, rotate and bounce. Fluid walking, lip sync and articulated dancing need a different animation method.
- Native Suno downloads can include timed lyric subtitles. Inspect actual streams. If cues are missing, use verified alignment or retain uncertainty; never guess then claim exact synchronization.

## Production checks

Keep sources immutable and revisions separate. Distinguish reporting, creation and upload dates. Check daily state before Create; reconcile uncertain submissions. Another video revision of an existing take does not require music regeneration.

Review early, verse, chorus, transition and final encoded frames at full size. Check long proper names. Decode the entire file and verify player playback. Save output hash and actual tool results.

After authorized publication, reconcile channel contents before any uncertain retry, compare complete saved description with the prepared file, and inspect expanded public source addresses and final lyric. Never truncate URLs or lyrics with ellipses.

## October 14, 2026 — full alternate take

The alternate “Bass Up, Bills Down” take ran 217.12 seconds. Thirty-four shots extended the receipt journey through the research and disputed fuel-policy chapters, then returned home. Seven scene illustrations and one transparent character layer supplied varied framing, environmental overlays and audio-responsive cutout motion. Two scenes were newly generated; the others were reused from the pilot. This is layered illustration animation, not articulated character acting.

The maintained `scripts/render_music_video.py` uses native FFmpeg filters and verified NVIDIA H.264 encoding. The full export took 218.5 seconds, including complete decode, at 1920×1080/30fps with 6,514 frames and stereo AAC. The earlier Pillow pilot took 243 seconds for 25 seconds. These are observed runs on this workstation, not a portable speed guarantee. The full export had no decode errors and differed from the audio duration by 0.013 seconds. Inspect encoded frames and player playback as well as the metrics.

FFmpeg xfade inputs needed matching `settb=1/30`; mismatched input time bases failed the initial five-second check. Runtime overlay x/y commands were supported by the installed FFmpeg. Native graphic particle atlases and measured RMS drove extra motion without model calls per frame.

Suno format buttons were multi-select: choosing M4A did not deselect MP3. The alternate MP3 was identified by its embedded song ID and duration; an older M4A with the same title belonged to the other take. The alternate timed M4A stalled. Free local base.en transcription supplied approximate section boundaries but missed phrases. Accordingly, the full video used topic cards rather than a guessed karaoke track; the entire canonical lyric sheet stayed in the description. Human listening/alignment QA remains a separate check. Reconcile files after uncertain downloads and never unlock repeatedly to resolve a stalled export.

## October 14, 2026 — animation feedback and next test

Travis found the cutting effective but the animation itself lacking. The accepted pilot and technical success of the full render did not establish satisfactory character animation. Use generated scene footage when a character must act; retain local typography, transitions and occasional graphic inserts around it.

A useful first test starts from the existing kitchen illustration: the heroine lifts her head, studies the long receipt, puts down her coin and gathers the paper with a determined expression. One continuous shot with a nearly still camera separates actual acting from camera-only motion. Preserve the art style and props, request no dialogue/music, and keep Suno as the final soundtrack. Check finger/prop contact, paper continuity, face drift and whether the requested action actually happens before scaling.

Gemini's live workspace labeled its video generator Gemini Omni. One reference-image submission returned a ten-second result after an eight-second request. The user supplied its normal download: 1280×720/24fps H.264, stereo AAC, 10.005 seconds, complete decode passed. Sampled frames showed real body/facial movement but an invented second foreground table around six seconds and an unwanted harsh expression. Reject the whole take for continuity; successful movement is not sufficient quality evidence.

The first prompt combined head movement, coin placement, receipt handling and leaning forward in a crowded low-angle scene. A cleaned medium keyframe removed competing props, established one table and placed both hands on the continuous receipt from the beginning. Its shorter revised prompt asks for reading, a breath and a calm upward look with a locked camera, seated posture and unchanged grip. This still passed visual inspection; the revised animation remains untested. Grok's workspace exposed six-second, 720p, 16:9 silent video settings, but its separate upload permission gate blocked the reference even after chat approval. No Grok generation was submitted, so no provider ranking is supported.

Private test prompts/state stay in the dated packet; recheck current provider controls and included limits on future runs. Preserve native provenance marks. Clean stills before animating and inspect temporal artifacts afterward; a clean keyframe cannot guarantee a clean clip. Reject or regenerate damaged footage rather than hiding geometry failures behind rapid cuts. Teach the verified story in the verses and exact local typography, then release tension through the hook.
