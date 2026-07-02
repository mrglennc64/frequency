# Appendix B — Free Analysis Tools and How to Use Them
*Target: 4 pp · Status: DRAFTED (Jul 2, 2026) — ⚠ QA gate: every procedure below must be re-verified click-by-click against current tool versions before launch (menu names drift; broken steps kill credibility); screenshots = design-pass assets*

---

This appendix is a manual, not an essay. It holds the exact steps for every measurement in this book, so the chapters can carry the judgment while this page carries the clicks. Everything here is free, runs on Windows/Mac/Linux, and requires no accounts. Chapter references: mono-sum and inversion (Ch. 2, Check 1), spectrum measurement (Ch. 5, Check 2), spectrogram/ramp reading (Ch. 8, Check 3), layer isolation (Ch. 9, Check 4).

## B.1 — Audacity (the workhorse)

Free audio editor: audacityteam.org. Used for four of the five audit checks. Work on the *delivered file* — your purchased download.

**Mono-sum test (Ch. 2 / Check 1)**
1. *File → Open* your track. You'll see two stacked waveforms (left/right). *(If you see only one, the file is already mono — for a "binaural" product, the audit just ended.)*
2. Play ~1 minute on headphones. Note the character — the smooth pulse, if real.
3. Select all (Ctrl/Cmd-A) → *Tracks → Mix → Mix Stereo Down to Mono*.
4. Play the same passage. Character changed (rough acoustic beating appeared / smooth pulse gone) → real two-carrier build. Identical → no binaural construction. Undo (Ctrl/Cmd-Z) restores stereo.

**Inversion / cancellation check (Checks 1 & 4)**
1. Open the track → click the track-name dropdown → *Split Stereo to Mono* (two independent tracks).
2. Select the lower track only → *Effect → Invert*.
3. Play both together (they auto-mix). **Silence** = the channels were identical — fake stereo, proven. **Residual sound** = the channels differ; what you're hearing is *only* the difference content — for a real binaural pair, the carriers; for a "subliminal" product, this is where a buried voice layer becomes audible (see B.1 layer measurement below).
4. To measure a exposed layer's level: select the residual → *Effect → Amplify* shows its current peak dB in the "Amplification" field default (read, then Cancel); compare against the bed measured the same way on the un-inverted mix. Offset = bed level − layer level. Honest range: −18 to −24 dB. Theater: −52.

**Carrier measurement (Ch. 5 / Check 2)**
1. *Split Stereo to Mono* as above. Solo the top (left) track.
2. Select ~30 s from the *middle* of the session (past the ramp-in — you want the plateau).
3. *Analyze → Plot Spectrum*. Set Size to 65536 for fine resolution. The tall spike is your carrier; hover to read its frequency (e.g., 200.0 Hz).
4. Repeat for the right track (e.g., 211.2 Hz). Subtract: 211.2 − 200.0 = **11.2 Hz beat** → check against the claimed band (Ch. 5 table). This is the arithmetic that catches "6 Hz theta" tracks running at alpha.

## B.2 — Spek (whole-file spectrogram)

Free spectrogram viewer: spek.cc. One job, done instantly: drag the file in and see **frequency over time** for the entire session at a glance — this is Check 3.

*How to read it:* time runs left-to-right, frequency bottom-to-top, brightness = energy. The carriers appear as thin horizontal lines low in the image. What you're grading (Ch. 8): do the lines **converge at the start** (ramp-in) and glide apart to a stable plateau? Do they **hold steady** — no drift, no stair-steps? Is there a **gentle convergence at the end** (ramp-out)? A session that's one unbroken flat stripe from second zero told you no entrainment design exists. Panning "8D" tracks betray themselves here too: instead of stable lines, energy sloshes between channels. *(Audacity's own spectrogram view — track dropdown → Spectrogram — does the same job if you'd rather stay in one tool.)*

## B.3 — Loudness (LUFS) measurement

For checking session loudness against intent (Ch. 8: sleep ≈ −20 LUFS, focus ≈ −16; sleep sessions never above conversational level). Free options, either works:

- **youlean.co Loudness Meter (free tier)** — runs as a plugin (in Audacity: *Effect* menu after install) or standalone; play the file through it and read **Integrated LUFS** when done.
- **ffmpeg** (command line, all platforms): `ffmpeg -i track.wav -af loudnorm=print_format=summary -f null -` — read "Input Integrated" from the output. One line, no GUI.

Measure *several tracks from the same catalog*: the number itself matters less than the **spread**. A catalog ranging −19 to −8 LUFS (the audit's finding) failed loudness discipline regardless of any single track's value.

## B.4 — No-install versions

- **The phone mono test (Ch. 2 quick version):** play the track through a single phone speaker vs. headphones. One speaker = physical mono sum. Essentially identical both ways → no binaural content. Two minutes, zero software, surprisingly final.
- **A reference beat, so you know what you're testing for:** any free online binaural generator (search "binaural beat generator"; several run in-browser) — set 200 Hz carrier / 10 Hz beat, listen on headphones, then sum to mono or pull one earbud. Now you've *heard* the real percept appear and die. Calibrate your ears once and every audit afterward is easier.
- **Streaming-only products:** you can still run the phone test and Check 5 (listening guidance), but carrier-precise measurement wants the delivered file — which is why Ch. 14's demand list includes "a measurable file." A seller who only streams has opted out of being verified; weigh accordingly.

## B.5 — Capability summary

| Tool | Tells you | Can't tell you |
|---|---|---|
| Audacity | Mono-sum, inversion, carrier frequencies, layer offsets | Whole-session shape at a glance |
| Spek | Ramp/plateau design, drift, panning disease | Precise carrier values, levels |
| LUFS meter / ffmpeg | Loudness vs. intent, catalog spread | Anything about construction |
| Phone test | Binaural yes/no, roughly | Everything else |

Twenty minutes, one evening, any track you own. The chapters told you what the numbers mean; this page makes sure you can always get them.

---
---

## Working brief (archived — draft above supersedes)

**Purpose:** Tool-by-tool manual; chapters carry judgment, appendix carries clicks; future-proofs the book (tool steps updatable in one place). **Structure (as drafted):** B.1 Audacity (mono-sum; inversion/cancellation incl. layer-level measurement via Amplify readout; Plot Spectrum carrier measurement at 65536 with mid-session selection note); B.2 Spek spectrogram reading (ramp/plateau/drift/8D slosh + Audacity fallback); B.3 LUFS (Youlean free / ffmpeg loudnorm one-liner; spread > single value); B.4 no-install (phone test; browser generator as ear-calibration reference; streaming-only caveat → Ch. 14 demand 4); B.5 capability table. **Master-copy rule:** Ch. 2's steps summarize; THIS file is canonical for procedures. **⚠ QA gate:** re-verify every step against current versions + capture screenshots in Week 6; mono-sum section was to be written W3 with lead magnet — now drafted here first, lead magnet PDF pulls from this.
