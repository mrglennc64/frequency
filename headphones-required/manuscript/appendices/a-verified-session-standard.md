# Appendix A — The Verified Session Standard
*Target: 3 pp · Status: DRAFTED (Jul 2, 2026) — keep field list in exact sync with `frequencyforge-mvp-spec.md` §2.4; sample certificate = design-pass asset · SEEDS FREQUENCYFORGE*

---

This appendix is a specification, published openly. Anyone — creator, tool-builder, competitor — may adopt it, implement it, and print certificates against it, with no license and no permission from me. That's deliberate: a standard only I can use is a marketing gimmick; a standard anyone can comply with is a market force. What follows defines what a **Verified Session** certificate must contain, what qualifies a session to carry one, and what a certificate is forbidden to claim.

## A.1 — What the certificate documents

One page, shipped with the session file, stating:

| Field | Contents |
|---|---|
| **Carriers** | Left and right carrier frequencies, in Hz, to one decimal (e.g., L 100.0 / R 102.5). For monaural/isochronic constructions: the tone frequency and modulation rate, format named. |
| **Beat** | The computed beat frequency (R − L) and its **band classification** (delta/theta/alpha/beta/gamma per the Ch. 5 ranges). |
| **Ramp profile** | A frequency-over-time graph of the full session: ramp-in duration, plateau value(s), ramp-out duration; multi-stage journeys shown stage by stage. |
| **Voice/subliminal layer** | If present: the offset in dB relative to the masking bed (constant, within −18 to −24 dB), *and a link to the full published script* (Ch. 9 transparency rule). If absent: stated as absent. |
| **Master** | Integrated loudness (LUFS), sample rate, and format of the delivered file. |
| **Delivery requirement** | "Headphones required" for binaural constructions, stated on the certificate itself. |
| **Verification ID** | A unique identifier resolvable by anyone (URL/QR) to confirm the certificate matches a registered session — so a certificate can't be forged onto a different file after the fact. |

Every field is a measurement, not a description. Each one is independently checkable with the Chapter 11 methods and Appendix B tools — that's the design criterion: **nothing goes on the certificate that the customer can't verify from the file.**

## A.2 — Pass criteria

A session qualifies as Verified when (numbers per Ch. 8 / the audit's "What Correct Looks Like"):

- Two clean carriers at the stated frequencies, with the stated difference — measured, not asserted; stereo separation stable across the session (no panning of carriers);
- Entrainment ramps present: 60–120 s ramp-in, gentle ramp-out, stable plateau(s) with no abrupt jumps;
- Any voice layer at a *consistent* −18 to −24 dB offset beneath the bed, with the script published;
- Master loudness appropriate to intent (sleep ≈ −20 LUFS, focus ≈ −16 LUFS) and consistent across a catalog;
- The headphone requirement (for binaural) stated at every point of delivery, certificate included.

A session may be honest and still not qualify — an unramped tone honestly labeled "raw tone, no entrainment design" is truthful but not Verified. The standard certifies *craft*, above the floor of mere honesty.

## A.3 — What the certificate must never claim

The standard's teeth face both directions. A Verified Session certificate documents **construction, not results**. It makes no outcome promises: no healing, no health effects, no manifestation, no financial or life outcomes — nothing an eardrum cannot mechanically deliver (Ch. 12's boundary, made structural).

**A certificate bearing a therapeutic or outcome claim is invalid on its face**, whatever its measurements say. This is not a legal disclaimer; it's the standard's core logic. The moment a certificate could say "cures," certificates would become the *next* costume for the fraud this book exists to end — engineering-grade paper wrapped around a Chapter 7 myth. The refusal is what keeps the artifact trustworthy.

## A.4 — Build-to-spec sessions

The refusal in A.3 is also what makes one honest product category possible: **build-to-spec**. A customer who wants specific frequencies — a Rife-list value, a chakra set, a Solfeggio tone, a number of personal significance — can have exactly those numbers, engineered to full A.2 craft, certified under A.1. The certificate reads, in substance: *"You requested [frequency]. Here it is, built correctly, documented below. This certifies the construction; it makes no therapeutic claim."*

This is the audit's passing chakra suite, formalized: the meaning stays yours; the engineering becomes checkable; the invoice for miracles disappears. (Chapter 7 explains why this is the only honest version of the "special frequencies" market.)

## A.5 — Adopting the standard

For creators: publish certificates with every session — a template following A.1 is sufficient; a registry-backed verification ID is better, and tools that automate both (including FrequencyForge, the one I'm building) are listed at the back-matter resource page. For listeners: a seller's reaction to being asked for an A.1 certificate is itself a complete audit result. For everyone: the standard is versioned; the current text and sample certificates live at the resource page.

*(Design pass: include a filled-in sample certificate here — the 45-min sleep session built in Ch. 8: L 100.0 / R 102.5, 2.5 Hz delta, 90 s ramp-in, 5-min ramp-out, no voice layer, −20 LUFS, 44.1 kHz, headphones required, verification ID. One of the €97 tier's three demonstration sessions ships against this exact page.)*

---
---

## Working brief (archived — draft above supersedes)

**Purpose:** The certificate spec, published openly; seeds FrequencyForge; gives Ch. 11/14 a concrete standard. **Structure (as drafted):** A.1 field table (mirrors Forge §2.4 field-for-field + delivery requirement; design criterion = customer-verifiable from file); A.2 pass criteria (Ch. 8 numbers; honest ≠ Verified distinction); A.3 no-outcome rule (health claim = invalid on its face; keeps the artifact trustworthy); A.4 build-to-spec (Jul 2 Rife decision formalized; chakra-suite precedent); A.5 adoption (open, versioned, Forge mentioned once; asking-for-a-certificate-is-an-audit line). **Sync obligation:** any drift vs. frequencyforge-mvp-spec.md §2.4 caught at Week 6 gate. **CTA:** one line, resource page.
