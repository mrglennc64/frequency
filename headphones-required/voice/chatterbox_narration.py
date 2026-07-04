"""
chatterbox_narration.py — narration-tuned Chatterbox wrapper for Glenn's voice.

WHY THIS EXISTS
    Raw Chatterbox defaults are tuned for short, expressive clips. On long-form
    narration that comes out "hammy + robotic": an over-dramatic delivery contour
    applied uniformly to every sentence. Two things fix it:

      1. Lower the two delivery knobs (exaggeration + cfg_weight) and temperature.
      2. Generate PER SENTENCE with a FIXED seed, then concatenate — so the voice
         character stops drifting between sentences (the "inconsistent" failure).

    Diagnosis + rationale live in ./VOICE-GUIDE.md. These are STARTING values;
    tune exaggeration in the 0.25–0.40 band by ear on one paragraph first.

DEPLOY
    This file is the source of truth (version-controlled in FREQUENCY). Copy it
    onto the RunPod pod (voice-cloning branch) and import it instead of calling
    model.generate(...) directly. See "DEPLOY TO POD" at the bottom.
"""

import re
import torch

# --- Narration defaults --------------------------------------------------------
# Chatterbox ships these at 0.5 / 0.5 / 0.8. Those are the hammy-robotic values
# for narration. The values below are the calm-credible-narrator settings.
NARRATION_DEFAULTS = {
    "exaggeration": 0.30,   # was 0.5 — kills the ham; lower = more measured
    "cfg_weight":   0.30,   # was 0.5 — slows/steadies pacing, stops sing-song
    "temperature":  0.65,   # was 0.8 — steadier prosody, less robotic swing
}

# Fixed seed = the same voice character on every sentence and every re-render.
# Change it only if you want to roll a *different* take of the whole read.
NARRATION_SEED = 1234

# Silence inserted between sentences when stitching (seconds). A touch of space
# reads as natural breath; too much drags. 0.25–0.35 is the audiobook pocket.
SENTENCE_GAP_S = 0.30


def _split_sentences(text: str):
    """Split into sentence-sized chunks, keeping terminal punctuation.

    Punctuation drives Chatterbox's pacing, so we preserve . ! ? and let each
    sentence be its own generation unit (short units = stable delivery)."""
    text = " ".join(text.split())  # collapse whitespace/newlines
    parts = re.split(r"(?<=[.!?])\s+", text)
    return [p.strip() for p in parts if p.strip()]


def generate_narration(model, text, audio_prompt_path, seed=NARRATION_SEED, **overrides):
    """Render `text` in the cloned voice with narration-tuned, drift-free settings.

    Args:
        model:              a loaded ChatterboxTTS instance
        text:               the SPOKEN-ADAPTED script (see VOICE-GUIDE Stage 2 —
                            do NOT feed page prose; strip [SCREEN:]/[pause] cues)
        audio_prompt_path:  path to Glenn's clean reference sample (mono, denoised)
        seed:               fixed for consistency; keep constant across re-renders
        **overrides:        e.g. exaggeration=0.35 to nudge a single render

    Returns:
        (wav_tensor, sample_rate) — ready to save with torchaudio.save(...)
    """
    params = {**NARRATION_DEFAULTS, **overrides}
    sr = model.sr

    gap = torch.zeros(1, int(sr * SENTENCE_GAP_S))
    chunks = []
    for sentence in _split_sentences(text):
        torch.manual_seed(seed)            # <-- same seed every sentence = no drift
        wav = model.generate(
            sentence,
            audio_prompt_path=audio_prompt_path,
            **params,
        )
        if wav.dim() == 1:
            wav = wav.unsqueeze(0)
        chunks.append(wav)
        chunks.append(gap)

    if not chunks:
        return torch.zeros(1, 1), sr
    return torch.cat(chunks[:-1], dim=1), sr   # drop trailing gap


# --- Example usage -------------------------------------------------------------
if __name__ == "__main__":
    import torchaudio
    from chatterbox.tts import ChatterboxTTS

    model = ChatterboxTTS.from_pretrained(device="cuda")

    script = (
        "Here's something that sounds impossible. A ten-hertz binaural track? "
        "There's no ten-hertz tone in it. None. Open it up in any analyzer and "
        "search the whole file. Nothing in there is oscillating at ten hertz. "
        "And that's not a defect. That's the entire trick."
    )

    wav, sr = generate_narration(
        model,
        script,
        audio_prompt_path="glenn_reference.wav",   # <-- your clean sample
    )
    torchaudio.save("v02_narration.wav", wav, sr)
    print(f"wrote v02_narration.wav @ {sr} Hz")

# --- DEPLOY TO POD -------------------------------------------------------------
# 1. Copy this file to the pod:
#      scp headphones-required/voice/chatterbox_narration.py <pod>:/workspace/
# 2. In your inference script, replace the raw model.generate(...) call with:
#      from chatterbox_narration import generate_narration
#      wav, sr = generate_narration(model, script, audio_prompt_path=REF_WAV)
# 3. MASTER the output before shipping (raw TTS is never broadcast-ready). ACX-ish:
#      ffmpeg -i v02_narration.wav -af \
#        "highpass=f=80, loudnorm=I=-20:TP=-3:LRA=11, deesser" v02_master.wav
#    Target: -18..-23 dB RMS, peak <= -3 dB, noise floor < -60 dB.
