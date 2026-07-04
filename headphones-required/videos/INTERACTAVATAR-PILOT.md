# InteractAvatar — Pilot Plan
*Evaluate a next-gen talking-avatar model as an upgrade to the current avatar pipeline · Status: proposed, not started*

## Why this, why now
Our video scripts don't just talk — Glenn **demonstrates**: "I'll do it on screen right now," pointing at a spectrum analyzer, holding up a track. Lip-sync-only avatars (Wav2Lip / SadTalker tier) can't act or handle objects, so the "show, don't tell" credibility of the book gets flattened into a talking head.

[InteractAvatar](https://github.com/angzong/InteractAvatar) (angzong, Jan 2026) generates **talking + acting + object interaction** from a single reference image, text-guided, with high-fidelity lipsync. It's Apache-2.0 (commercial use is fine) and beats current SOTA (HuMo, VACE, Wan-S2V) on its own benchmark. If it holds up on *our* footage, it's a generation ahead of what we run.

**This is a pilot, not a migration.** Chatterbox voice stays exactly as-is. We're testing one thing: does the avatar look good enough to ship.

## What we're actually testing (the one question)
> On a real 20–30s slice of a V-script, with Glenn's reference image + our Chatterbox narration, does InteractAvatar produce a *shippable* clip — believable lipsync, a natural gesture/interaction, no uncanny artifacts — at a render cost we can live with?

Everything below serves that yes/no.

## Constraints & unknowns (read before spending GPU hours)
- **Backbone: Wan2.2-5B.** A 5B video DiT is heavy — expect **≥24 GB VRAM** (A100/4090-class) and **minutes per clip**, not seconds. Confirm the pod GPU tier before starting.
- **Research-grade code.** Fresh Jan 2026 release: thin docs, likely rough setup, possible dependency pinning pain. Budget setup time, not just render time.
- **Input triad:** reference image + audio + text/motion prompt → video. Our Chatterbox WAV is the audio; we need a good still of Glenn and a written interaction prompt per shot.

## Steps
1. **Provision** — spin up the RunPod pod on a ≥24 GB GPU (A100 40GB ideal). Note hourly cost up front; this is the main spend.
2. **Install** — clone the repo, follow its setup, pull the Wan2.2-5B weights. Log every deviation from the README in a `SETUP-NOTES.md` (research repos rarely install clean).
3. **Assets** — pick ONE 20–30s beat from an existing V-script (V02's "there's no 10 Hz tone" demo is a good stress test — it implies pointing at a screen). Prepare: a clean front-facing still of Glenn, the Chatterbox narration WAV for that beat, and a one-line interaction prompt (e.g. *"gestures toward a monitor showing a spectrum analyzer"*).
4. **Generate** — render the clip. Capture: wall-clock render time, peak VRAM, and $ cost.
5. **A/B** — put it next to the same beat from the current pipeline. Judge on the criteria below.
6. **Decide** — apply the decision gate. Write the verdict at the bottom of this file.

## Success criteria (all must pass to proceed)
- [ ] **Lipsync** tracks the Chatterbox audio with no obvious drift or mouth artifacts.
- [ ] **The interaction reads as intentional** — a gesture/object handling that looks directed, not random flailing.
- [ ] **No uncanny tells** — eyes, hands, and face hold up at 1080p on a phone screen (our muted-autoplay audience will still pause and look).
- [ ] **Identity holds** — it still looks like Glenn across the whole clip, no morphing.
- [ ] **Cost is sane** — render time × pod rate is affordable across ~10 videos of many shots each. Note the actual number.

## Decision gate
- **All 5 pass →** greenlight a second pilot on a full 60–90s scene, then plan integration into the heyg pipeline.
- **Lipsync/identity pass but interaction is weak →** still potentially useful as a better *talking head*; reassess vs. current pipeline on quality alone.
- **Uncanny or cost-prohibitive →** shelve it, revisit when the model matures or a lighter variant ships. Chatterbox + current avatar carries the launch.

## Explicitly out of scope
- Voice. Chatterbox stays; narration params are settled in [../voice/chatterbox_narration.py](../voice/chatterbox_narration.py).
- Any production integration into heyg — not until a pilot passes the gate.
- Replacing the current avatar pipeline wholesale — this is additive evaluation.

## Verdict
*(fill in after the pilot — render time, peak VRAM, $/clip, pass/fail per criterion, go/no-go)*
