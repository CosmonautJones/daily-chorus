# The Daily Chorus loop

One daily medley, two or three verified headlines, a changing genre, and human review before release.

## 1. Scan a varied news slate

Use the actual date in America/New_York. Consider four to six current candidates spanning good, bad, scary, and funny news, and both world and national coverage. The initial national lens is the U.S. Mood and geographic scope are independent tags.

Read the last seven available packets to identify recent topics and sounds. Prefer developments from the previous 24 hours; up to 48 hours is acceptable for an ongoing development when labeled. Choose two or three stories with a coherent emotional connection. Aim for both world and national coverage and a hopeful or lighter item when the verified slate supports it. Explain omissions rather than forcing categories into the song.

Verify each included story through at least two independent newsrooms. Syndicated copies of one wire report count as one source. Supplement with primary records where useful. For each story record the article URL, publisher, wire attribution, publication/update date, event date when known, three supported facts, and uncertainty. Search snippets alone are insufficient.

If fewer than two current stories can be verified, preserve the research and stop before using generation credits.

## 2. Compare evidence and framing

For each story, separate common supported facts, disputed or attributed claims, and differences in emphasis. A comparison should say what the actual articles show; do not infer an outlet's position from its name.

When freely accessible, Ground News or another published rating provider can supply outlet bias/factuality context. Link the rating and record the provider and date checked. Mark missing ratings as unknown. Keep those outlet-level assessments distinct from the evidence supporting an individual claim. Do not invent coverage percentages or apply a U.S. left/right label to every country's politics.

Use neutral factual language. Claims receive weight according to their evidence, rather than equal space by default. Original reporting remains the factual source; aggregation and ratings help compare coverage.

## 3. Choose the sound

A closed, verified listener poll targeting today's song takes priority. Record its URL, totals, and selected genre. Explain a tie-breaking choice. An unavailable poll or zero votes triggers an editorial choice.

Otherwise rotate from rap (including crunk), country, techno, pop, K-pop inspired pop, pop-punk, rock, metal, house, drum and bass, hyperpop, Afrobeats, Latin pop, soul, R&B, funk, disco, reggae, jazz, or acoustic. Explore other genres when they fit. Avoid the previous day's primary genre when the mood permits. Check recent credible music reporting or charts before calling a sound current or trending; record the supporting link and date. The genre pool remains usable when trend evidence is unavailable.

Give crunk rap and country early turns in the upcoming rotation, per the creator's October 7 request, unless a verified poll or the story's mood calls for something else. Crunk prompts should emphasize a head-bouncing groove, heavy bass, punchy drums, chantable hooks, and clear rhythmic vocals. Country prompts should emphasize a strong storytelling hook, acoustic guitar, steel or fiddle accents, and a warm vocal. Keep one coherent primary sound per song.

Record the genre, its relationship to the day's mood, and whether the choice came from listeners, rotation, or a verified trend. Describe musical qualities in the Suno prompt, including rhythm, instrumentation, energy, and vocal delivery. English is the starting language. Avoid artist or voice impersonation.

## 4. Write one song

Each of the two or three headlines gets its own verse or short section. Use a chorus connecting their shared mood, with one memorable hook that works in a short clip. Aim for roughly two to three minutes. Preserve factual distinctions between stories, and keep fictional narrators or imagery separate from reporting.

Humor can fit an absurd event or a fictional illustration. Treat victims, grief, and serious human suffering respectfully. Avoid fabricated quotes, unsupported accusations, partisan campaigning, or copied article prose and lyrics.

Prepare a dated private packet using the [template](packet-template.md): title, story slate, source comparison, genre decision, original lyrics, style prompt, Behind the song notes, release copy, and [visual storyboard](visuals.md). Use the [compact songwriting guide](songwriting.md) and [Daily Chorus Lyricist skill](../skills/daily-chorus-lyricist/SKILL.md) for one writer pass and one independent editor pass before Create. Save the concrete lyric review and stop as `needs_lyrics` if its text gate or factual checks remain unresolved. Record the chosen stories and tags in the daily state so subsequent runs can track variety.

## 5. Generate drafts once

Use the authorized Suno account through supported tools. Check account access, plan entitlement, and credits before creation. Append the date to the draft title for reconciliation.

Save state before submission. Make at most one normal Create request per Eastern date and keep the versions returned. If the submission outcome is uncertain, reconcile matching tracks before any retry. Do not automatically extend, remix, regenerate, purchase, or download paid assets.

Completion requires actual song-page links, a completed status, duration when shown, and enabled playback controls. A lyrics file alone is a prepared packet. Do not claim a listening or quality review that has not happened.

## 6. Illustrate after selection

Default to the second completed version from each normal Suno request, per the creator's October 7 preference. Save both links and record the selected song ID. This selection preference does not authorize future publication.

Prepare scene concepts with the packet. After a song version is selected and its download entitlement confirmed, obtain the authorized audio and produce original artwork or use images with confirmed reuse rights. Time scenes and lyric captions to the actual audio; a written storyboard is not a rendered video.

Prepare a 1920×1080 full YouTube video and a 1080×1920, 20–30 second chorus cut for Shorts/X when those releases are requested. See [visuals.md](visuals.md) for composition, attribution, and disclosure rules.

## 7. Review, release, and listen

The creator approves the specific song, finished video, caption, and destination. Include story-specific context, article links where supported, image credits, and AI-use disclosure. YouTube and X profiles link to each other for listeners to find the wider conversation.

Full-song YouTube descriptions include every supporting article's complete URL with newsroom/wire attribution and story labels, followed by the entire original lyric sheet, including repeated sections. Copy from the canonical packet files, not shortened browser labels or pronunciation spellings. Do not replace sources or lyrics with ellipses. Check the actual description limit and shorten the introduction first; flag a limit before publication if complete content cannot fit. Reopen the saved Studio description and compare the full text, source URLs, and final lyric line with the prepared file. Also verify lyrics in the expanded public description. YouTube may shorten displayed link labels while retaining complete URLs; clickable external links can require channel verification.

Propose four next-day poll choices from the genre pool, rotating options instead of repeating a fixed ballot. A published poll targets an 8 AM Eastern close before the 9 AM draft run. Topic suggestions can shape the slate, but every selected headline still needs verification. Posts, polls, uploads, and distribution remain separate approved actions.

Notify on new completed drafts, a new failure, or required user action. Keep repeated unchanged review/blocker checks quiet.

## Current execution

The pilot's current scheduler is a Codex heartbeat on the creator's computer, scheduled daily at 9 AM Eastern. It reads a local operational workflow and uses the signed-in browser. A [local slideshow renderer](rendering.md) is implemented for selected audio and saved cue times. A standalone service, direct Suno API integration, and automatic publishing are not implemented in this repository.

## Methodology reference

[Ground News methodology](https://ground.news/rating-system), checked October 7, 2026: bias and factuality ratings concern news publications; an outlet rating does not evaluate the truth of each article. Our source comparison is an editorial process inspired by that distinction.
