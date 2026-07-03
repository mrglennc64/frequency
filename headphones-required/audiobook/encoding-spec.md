# Audiobook Encoding Spec — Headphones Required (binaural edition)
### Glenn Carter · Frequency Engineering · Jul 3, 2026

The audiobook that teaches honest frequency audio must itself be a **Verified Session** — correct construction, headphone-honest, state-claim only. This spec is what to build against, and it ships with the construction certificate at the bottom.

---

## 1. The choice: alpha, 10 Hz

| Parameter | Value | Why |
|---|---|---|
| **Beat frequency** | **10 Hz (alpha)** | The listener's job is *comprehension* — an alert task. Delta/theta (0.5–7 Hz) push toward drowsiness and fight understanding. Alpha = relaxed alertness: calm, receptive, focused without dulling attention. 10 Hz is the center. |
| **Band alt** | 8 Hz (calmer) or 12 Hz (slightly more alert) | Stay in alpha; only move if 10 feels off after listening. |
| **Do NOT use** | 40 Hz "gamma focus" | Above the ~30 Hz binaural ceiling — the brain stops fusing the tones into a beat (Ch. 4 / App. C). "40 Hz binaural" doesn't work. If you ever want 40 Hz, it must be isochronic/monaural. |
| **Carriers** | **L 100.0 Hz / R 110.0 Hz** (= 10 Hz beat) | Low carriers sit mostly *below* the 300 Hz–4 kHz speech-intelligibility band, so they don't muddy the words. Clean pure sines, exact values. |
| **Carrier caveat** | tune after hearing the narration | A deep male narrator's fundamental is ~100–150 Hz. If the carriers sit right on his voice, shift the pair down (90/100) or up (150/160) — keep the 10 Hz difference — and pick by ear. |

## 2. Construction (per Ch. 8)
- **Ramp-in:** 60–120 s at the start of each file (or the whole book) — the bed *emerges* instead of clicking on.
- **Plateau:** steady 10 Hz for the body of the read. No drift, no per-chapter band switching — one intent throughout.
- **Ramp-out:** gentle return at the end.
- **Level:** the tone bed sits **~15–25 dB below the narration** — present, never attention-grabbing. Narration is always the priority signal.
- **Master:** spoken-word loudness, ~**−18 to −20 LUFS** integrated, true-peak ≤ −3 dB. Consistent across every chapter file.

## 3. Format & delivery decision (the honest part)
Binaural = **headphones only.** A lot of audiobook listening happens on car/phone speakers, where the binaural beat is physically void (Ch. 4). Pick one, on purpose:
- **(A) Headphone edition** — embed the binaural bed, state **"Headphones required"** loud and clear (it's the title). Speaker listeners get plain narration.
- **(B) Speaker-safe edition** — use an alpha **monaural or isochronic** bed instead, which survives speakers, so everyone gets the effect.
- **(C) Ship both** — a plain edition and a headphone binaural edition. Most honest, best positioning. *(Recommended.)*

Distribution note: a constant background tone can trip Audible/ACX mastering & noise-floor checks — sell the binaural edition **direct** (own site / Gumroad), not Audible.

## 4. Claim discipline (per Ch. 12)
Call it: *"a subtle alpha bed for calm, focused listening."* A **state** claim — defensible.
Never: "learn faster," "absorb into your subconscious," "manifest." There's no good evidence a beat improves *comprehension*; sell it as a nicer listening state, not a learning hack. The restraint is the brand.

## 5. How to generate the carriers — do NOT download pre-made "binaural" files
You can't verify a downloaded file's carriers, and it won't be matched to your narrator. Generate clean tones yourself:

- **Audacity** (free · https://www.audacityteam.org) — the manual route: two mono tracks, pan one hard-left and generate a 100.0 Hz sine, pan the other hard-right and generate 110.0 Hz. Fade-in the first ~90 s (ramp), fade-out the end. Export, then mix under the narration at −15 to −25 dB. (Same tool as Appendix B.)
- **Gnaural** (free, open-source · https://gnaural.sourceforge.net/ — project: https://sourceforge.net/projects/gnaural/) — a purpose-built binaural generator (implements the 1973 Oster paper you cite in App. C). Set carrier + beat, add ramps, export a WAV bed.
- **SBaGen** (free, GPL · https://uazu.net/sbagen/) — scriptable, renders a WAV of a timed sequence; ideal if you want precise, repeatable ramps across a long file.

For a 30-year engineer: generating the pair in your DAW (two oscillators, exact Hz, hard-panned, low level, ramped) gives you the cleanest, most controllable result and full documentation for the certificate.

---

## 6. Construction Certificate (ships with the binaural edition)

> **VERIFIED SESSION — Headphones Required (audiobook, binaural edition)**
> - Left carrier: **100.0 Hz** · Right carrier: **110.0 Hz**
> - Computed beat: **10.0 Hz** · Band: **alpha**
> - Ramp: 90 s ramp-in / steady plateau / ramp-out per file
> - Bed level: −__ dB relative to narration · Master: −__ LUFS integrated, true-peak −__ dBTP
> - Delivery: **Headphones required** (binaural void on speakers)
> - Claim: subtle alpha bed for calm, focused listening. **No therapeutic or learning claim.**
> - Verification ID: __________
>
> *This certifies construction, not results (Appendix A). Educational audio-engineering — not medical or therapeutic advice.*

*(Fill the blanks with your final measured values after encoding.)*
