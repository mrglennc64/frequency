# Appendix A — The Verified Session Standard
*Target: 3 pp · Write in Week 6 (Aug 10–16) · Status: not started · SEEDS FREQUENCYFORGE — keep in exact sync with `../../../frequencyforge-mvp-spec.md` §2.4*

## Purpose & role
The construction-certificate specification, published openly. Strategic double duty: (1) gives the book's evaluation framework (Ch. 11, 14) a concrete standard, (2) seeds the market for FrequencyForge, whose certificates implement this exact spec. Publishing the standard openly — anyone may adopt it — is what makes it a *standard* rather than a marketing gimmick; Forge then competes on being the easiest way to comply.

## Contents
- **What a Verified Session certificate must document** (mirror Forge spec §2.4 field-for-field):
  - Left and right carrier frequencies; computed beat frequency; band classification
  - Ramp profile graph (frequency over time: ramp-in / plateau / ramp-out)
  - Subliminal/voice layer offset in dB relative to bed (if any layer is used) + published affirmation script (the Ch. 9 transparency rule)
  - Final master LUFS and sample rate
  - Unique verification ID — resolvable by anyone to confirm the session's construction
- **Pass criteria** (from Ch. 8 / the audit's "What Correct Looks Like"): two clean carriers at the stated difference; 60–120 s entrainment ramps; stable plateau; layer offsets consistent within −18 to −24 dB; LUFS appropriate to intent (sleep −20, focus −16); headphone requirement stated at point of delivery
- **What the certificate does NOT claim** — no outcome promises; it verifies construction, not results (Ch. 12 discipline applies to the standard itself)
- A filled-in sample certificate for one of the €97 tier's demonstration sessions (design pass produces this)

## Reuse
Forge spec §2.4 is the master; this appendix is its public prose form. Any drift between the two damages both — check at the Week 6 fact-check gate.

## CTA
One line: sessions and tools that implement this standard, including FrequencyForge (waitlist), listed at [site].
