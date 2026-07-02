# Voice Guide — Part II (and the whole book)
*How we make the writing read like Glenn, then make the narration sound like Glenn · Status: process doc, awaiting a voice sample to calibrate*

The current Part II drafts (Ch. 4–7) are written in a strong forensic-engineer voice — but it's *my* rendering of that persona, not calibrated to how Glenn actually writes and talks. This guide is the two-stage process to fix that. Stage 1 (written) feeds Stage 2 (spoken): we get the words sounding like you, then narrate those words.

---

## Stage 1 — Written voice (make it read like you)

### The one thing that unblocks everything: a voice sample
I can't reverse-engineer your voice from the polished project docs (`f1.pdf`, the audit sample) because those are already house-style, possibly co-written — they'll teach me the *brand* voice, not the *raw you*. What calibrates fastest, in order of value:

1. **10–15 minutes of you talking into your phone** about binaural beats / the sludge market / a client story — unscripted, how you'd explain it to a smart friend. Transcribed, this is gold: it captures your real rhythm, asides, and the metaphors you actually reach for.
2. **Raw writing you didn't polish** — a long email, a forum rant, a DM where you got heated about fake tracks.
3. Anything with your unedited opinions in it.

Drop any of those in this `voice/` folder (or paste them to me) and Stage 1 starts for real.

### Voice profile (fill from samples — template)
Once I have samples I complete this, and every voice pass checks against it:
- **Sentence rhythm:** _(short & punchy? long, winding, clause-heavy? a mix — and where?)_
- **Register:** _(do you swear? how formal? jargon-dense or plain?)_
- **Signature moves:** _(metaphors you reach for; how you open a point; how you land one)_
- **Address:** _(how much you talk directly to "you"; how much "I")_
- **Tells to keep:** _(phrases that are unmistakably you)_
- **Anti-tells — things to cut:** _(constructions that read as generic/AI and that you'd never write — e.g. "it's not X, it's Y", tidy tricolons, "Here's the thing")_

### The pass, then the read-aloud test
1. I do a voice pass on Ch. 4 first (it's the load-bearing chapter and the V2 script), rewriting to the profile.
2. **You read it out loud.** Anywhere you stumble, wince, or think "I'd never say that" — mark it. That reaction is the highest-signal edit in the whole process; the ear catches what the eye approves.
3. I fold your marks back into the profile, then run the calibrated pass across Ch. 5–7 and eventually the whole book.

**Why this matters for this product specifically:** the book's entire thesis is *distrust the polished, trust the real craftsman.* If the prose reads as slick-generic, it quietly contradicts the argument. Your actual voice — 30 years, a little impatient with nonsense — is a credibility asset, not a style preference.

---

## Stage 2 — Spoken voice (natural narration for videos + audiobook)

### Script for the ear, not the page
Page prose and spoken prose are different animals. We do **not** narrate the chapters verbatim — we adapt them: shorter sentences, more signposting, no "[DIAGRAM 8.2]" or "as the table shows," contractions everywhere, one idea per breath. The natural unit is the **video script** (V2–V5 map to Ch. 4–7), which already has the hook → claim → demo → takeaway → CTA shape in `../videos/`. An audiobook edition comes later off the same adapted scripts.

### Whose voice — and the recommendation
1. **Your real voice, recorded.** Most authentic; ideal for a whistleblower-with-receipts product. Cost: your time, retakes, consistency across 10 videos.
2. **A clone of your voice (recommended for scale).** Record a clean sample once; a voice model then narrates every script in your voice, consistently, and re-renders instantly when a script changes. Pairs directly with your avatar pipeline. This is the sweet spot: it *is* your voice, just scalable.
3. **A stock/synthetic voice — not recommended.** For a product whose whole pitch is "the real thing sounds like this," a generic narrator undercuts you. Skip it.

**Recommendation:** clone your own voice (option 2). It keeps the authenticity of option 1 with the throughput you need for 10 videos + an audiobook.

### Tooling & what it needs
- **Voice-clone/TTS:** ElevenLabs. **Voice ID: `tXoAX6rzg9vkoUfJKy0k`** — this is the narration voice for the whole series; every script header references it. It needs a few minutes of **clean, consistent** audio to build/refine the model — quiet room, one mic, no music, natural pace. The *same* recording session that gives me your Stage-1 talking sample can double as the clone's training data — record it well and it serves both stages.
  - *TTS prep:* the script files under `../videos/scripts/` are spoken-adapted. Before pasting into ElevenLabs, strip the `[SCREEN: …]` and `[pause]` direction lines — those are for the editor/avatar, not the voice. Spoken paragraphs are the TTS input.
- **Pipeline fit:** cloned VO → your avatar/visual pipeline → captions (muted-autoplay audience) → the audit design system for lower-thirds and diagrams, per `../videos/script-template.md`.
- **This session's limit:** I can't generate or clone audio here (no audio tool is connected). What I do is produce the *scripts* — the calibrated, spoken-adapted words the voice reads. You (or a later session with the right tool) run the actual cloning/render.

---

## Demonstration — Ch. 4 opening: page prose → spoken adaptation
Same content, retuned for the ear. This is *my* uncalibrated pass; once I have your sample it gets your fingerprints. Reacting to this is itself Stage-1 calibration — tell me what's you and what isn't.

**Page version (as drafted):**
> There is no 10 Hz tone in a 10 Hz binaural track. Open the file in any spectrum analyzer you like. Search every second of it. You will not find anything oscillating at 10 Hz, because nothing in the file does.

**Spoken adaptation (for V2 narration):**
> Here's something that sounds impossible. A ten-hertz binaural track? There's no ten-hertz tone in it. None. Open it up in any analyzer — I'll do it on screen right now — and search the whole file. Nothing in there is oscillating at ten hertz. Nothing. [SCREEN: spectrum, no 10 Hz peak] And that's not a defect. That's the entire trick, and once you see it, nobody sells you a fake one again.

What changed, and why: contractions; the claim broken into breath-sized pieces; a spoken demo cue built in; direct "I'll do it right now" presence; the payoff moved up front. That's the template for adapting all of Part II.

---

## What I need from you to start for real
**One recording** — 10–15 minutes, quiet room, you talking about this stuff unscripted. It calibrates the written voice *and* trains the narration clone in a single take. Drop it here and I'll (1) build your voice profile, (2) do the calibrated pass on Ch. 4, and (3) hand you a V2 narration script ready for the clone.
