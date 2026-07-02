# FrequencyForge — MVP Specification
### Glenn Carter · Frequency Engineering
*Working title. Alternatives: TrueTone Studio, CarrierLab, VerifiedBinaural.*

---

## 1. Positioning

Every competitor sells finished audio. FrequencyForge sells the **engineering layer**: a web app that lets coaches, influencers, and wellness creators build *technically correct* binaural/frequency sessions — with a verifiable construction certificate attached to every export.

One-line pitch: **"Anyone can generate a tone. FrequencyForge generates proof."**

The certificate is the moat. It converts a commodity (a tone generator) into a credibility product (verified engineering), the same way a CIP scan report converts a website check into a procurement document.

---

## 2. Core MVP Features (Phase 1 — 6–8 weeks solo build)

### 2.1 Session Builder
- Intent presets: Focus (beta 14–18 Hz), Meditation (alpha 8–12 Hz), Manifestation/Deep work (theta 4–7 Hz), Sleep (delta 0.5–3 Hz), plus custom.
- User selects: target beat frequency, carrier base (100–400 Hz range with sensible defaults), session length (10–90 min).
- **Entrainment ramp engine** — the differentiator novices don't know exists:
  - Ramp-in: 60–120 s glide from near-zero beat to target
  - Plateau: stable target band
  - Ramp-out: gentle return (critical for sleep sessions)
  - Optional multi-stage journeys (alpha → theta → delta descent)

### 2.2 Layer Engine
- Background bed upload (rain, ocean, pads) or built-in generative pads
- Voice/affirmation upload with automatic subliminal mixing:
  - Consistent −18 to −24 dB offset under the masking bed (user-adjustable within safe bounds)
  - Auto stereo placement and gentle band-limiting
  - Loudness normalization of the final master (target LUFS per use case: sleep −20, focus −16)

### 2.3 Headphone Gate
- Every exported session opens with an optional 5-second stereo verification sweep ("left… right…") — the built-in headphone check no one else ships
- Player embed (Phase 2) refuses binaural playback claims on detected mono output

### 2.4 The Certificate (the moat)
Every export generates a PDF + shareable web page documenting:
- Left/right carrier frequencies, computed beat frequency, band classification
- Ramp profile graph (frequency over time)
- Subliminal layer offset (if used), LUFS, sample rate
- Unique verification ID + QR — anyone can check the session's construction
- Creator branding on white-label tier

### 2.5 Export
- WAV + 320 kbps MP3, embedded metadata, certificate attached

---

## 3. Architecture

- **Audio engine:** Web Audio API (OscillatorNode pairs, GainNode automation for ramps) rendered via OfflineAudioContext → WAV. All client-side = near-zero server cost for generation.
- **Backend:** lightweight API (Node or Python/FastAPI) for accounts, certificate registry (verification IDs must resolve server-side to be trustworthy), Stripe billing, file storage (S3/R2) for uploaded beds/voice.
- **Frontend:** React. Session builder = timeline UI + live preview.
- **Certificate registry:** the only part that must be server-authoritative. Simple: session hash + parameters stored at export; public verify page renders them.

Solo-buildable: you shipped the entire NSS suite in a year; this MVP is a fraction of that surface.

---

## 4. Pricing

| Tier | Price | Includes |
|---|---|---|
| Creator | €29/mo | 10 exports/mo, certificates, standard presets |
| Pro | €79/mo | Unlimited exports, subliminal engine, custom ramps, journeys |
| White-Label | €199/mo | Creator branding on certificates & player, client sub-accounts |

Annual = 2 months free. Free tier: 1 watermarked export (the funnel).

---

## 5. Phases

1. **Phase 1 (wk 1–8):** Builder + ramps + WAV export + certificate PDF + Stripe. Launch to the Headphones Required audience.
2. **Phase 2 (wk 9–16):** Subliminal layer engine, verify pages with QR, embeddable player with headphone gate.
3. **Phase 3:** White-label, journey presets marketplace (creators sell ramp profiles — you take 20%).

---

## 6. Strategic notes

- Keep 100% of this IP in a new entity (or personal) — **not** NSS. It must survive/ignore the acqui-hire.
- The Frequency Audit service feeds this: every audited channel is a warm lead ("your catalog failed; here's the tool that would have prevented it").
- Certificates create network effects: every shared certificate is an ad with your engine's name on it.
