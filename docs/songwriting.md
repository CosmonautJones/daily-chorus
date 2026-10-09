# Write the hook first

Use the [Daily Chorus Lyricist skill](../skills/daily-chorus-lyricist/SKILL.md) for every new medley. It defines the writer and independent lyric-editor roles, genre-specific phrasing, factual boundaries, and the text quality gate. Its user-level invocation is `$daily-chorus-lyricist`; the repository copy is the maintained source.

## The lean daily pass

1. Read dated state first. Completed or uncertain Suno submissions go to reconciliation, not lyric-driven regeneration.
2. Give the writer compact verified story briefs, genre/tempo, emotional thread, and recent titles/hooks. Draft two hooks and one complete song using the skill. Each verse explains who/where, the key development, and supported significance with at least two event-specific facts; map those facts to the sung lines.
3. Run one independent editor agent with the skill, briefs, hooks, lyrics, and style only. Use a fresh context; assign review responsibility and no file or browser mutations. No research dump, full chat history, extra browsing, or review panel.
4. The editor writes one factual takeaway per story from the lyrics alone, then compares it with the brief. Require a listener to understand what happened and why it matters without reading the description. Incorporate necessary edits once, then check facts and pronunciation. Save `lyric-review.md`: reviewer type, takeaways and comprehension gaps, five scores with concrete reasons, applied edits, blockers, and readiness. The local text gate requires every story to pass comprehension, 8/10 or better, no zero, and no factual/originality/respect blocker or unresolved verification question. If unresolved, preserve `needs_lyrics` before spending credits. Explicitly label a parent self-review if an independent agent is unavailable.
5. Save readable canonical lyrics, optional verified pronunciation spelling, and a concise style prompt separately. Submit only through the operational workflow's one normal Create request.

Written quality review cannot establish melody, delivery, intelligibility, or actual sound. Listening review of generated audio remains pending until performed. A critique of an existing generated song may create a separate revision proposal; it must not replace the lyric sheet belonging to that audio.

Rendering still uses local code and one original image per story with gentle fades. No model call per frame is needed. Longer community skills remain optional for a specific unresolved issue; they are not loaded every day.
