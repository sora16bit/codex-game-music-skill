# Deliverable Formats

Choose the simplest format that can satisfy the requested quality, interactivity, and target runtime.

## Selection Protocol

Before choosing a format, answer:

- Is the task prototype, production handoff, or direct repo implementation?
- Does the requested quality require real samples, a synth/SoundFont, or rendered audio?
- Does the game need note-level responsiveness, vertical layering, horizontal section changes, or only a loop?
- Can the current repo already load audio assets or run a synth dependency?
- Is the user asking for editable composition data, playable audio, or code integration?

If procedural oscillator output has already been criticized as cheap, fake, thin, or not like real game music, do not make another oscillator-only pass unless the user explicitly wants procedural audio.

## Decision Table

| Request / Constraint | Prefer | Notes |
| --- | --- | --- |
| Fast browser prototype | Web Audio | Best for procedural BGM/SFX without assets. Sound quality depends on synthesis care. |
| Existing project already uses Tone.js | Tone.js | Use declarative patterns and Tone.Transport only when dependency exists or is approved. |
| User wants "real", "less cheap", or "game-quality" | Rendered loops or stems | Better tone and mix; needs asset loading and loop validation. |
| User critiques fake instruments or performance | MIDI + credible synth/SoundFont or rendered stems | Do not over-polish oscillator approximations when the failure is instrumental realism. |
| Adaptive music with good mix | Stems | Use synchronized base/drums/bass/harmony/lead/danger/reward layers. |
| User needs editable composition data | MIDI-like JSON or MIDI | Good for iteration; needs synth/soundfont for final sound. |
| Sheet-like exchange format | MusicXML or ABC | Good for notation and theme handoff, not final in-game audio. |
| Unity/Godot integration | Loop/stem plan plus engine bus rules | Include asset names, BPM, bar length, loop points, transitions, and bus routing. |
| Tiny game jam build | Hybrid | Render BGM loop, synth lightweight SFX procedurally. |

## Required Metadata

For any loop or stem plan, include:

- Title or cue name
- Scene role
- BPM, meter, key/scale
- Loop length in bars and seconds
- Intro/loop/outro split if any
- Layer names and intended gain range
- Transition rules: immediate, beat, bar, phrase, or event stinger
- SFX priority notes
- Sound-source status: procedural approximation, MIDI-rendered, sample-based, recorded, or production brief only
- Validation plan: loop boundary, click test, loudness relative to SFX, state transition test

Use [output-contracts.md](output-contracts.md) for full templates.

## MIDI-like JSON

Use when no renderer exists but a structured composition is useful.

```json
{
  "bpm": 132,
  "meter": "4/4",
  "scale": "D Dorian",
  "loopBars": 8,
  "tracks": [
    {
      "name": "bass",
      "instrument": "synth bass",
      "notes": [
        { "bar": 1, "beat": 1, "dur": 0.5, "note": "D2", "vel": 0.78 }
      ]
    }
  ]
}
```

Required track fields:

- `name`: layer name used by code or handoff.
- `instrument`: honest target such as `synth bass`, `string-like pad`, `SoundFont strings`, or `sampled taiko`.
- `role`: bass foundation, motif, counterline, harmony, texture, impact, or stinger.
- `notes`: each with `bar`, `beat`, `dur`, `note`, and `vel`.

Preferred optional fields:

- `swing`, `humanizeMs`, `gain`, `pan`, `stateRule`, `articulation`, `release`.

## Stem Plan

Use separate synchronized loops when the game needs adaptive density.

- `base`: always-on pulse, quiet enough for early play.
- `drums`: rhythmic energy; fade in by intensity or combat state.
- `bass`: weight and danger; can simplify during dialogue or menus.
- `harmony`: pads/stabs; adds color without masking SFX.
- `lead`: motif; enter after player understands the scene.
- `danger`: alarms, risers, high pulses; thresholded by threat.
- `reward`: bright color; short layer or stinger after success.

Render all stems at the same BPM, length, sample rate, and loop boundaries. Start stems together and automate gain rather than restarting them unless horizontal re-sequencing is intended.

## Rendered Loop Brief

When asking a renderer, DAW, or external asset process to create audio, specify:

- Exact duration and loop bars
- Seamless loop requirement
- File format: `wav` for source, `ogg` or compressed format for game build
- Target loudness relative to SFX, not a broadcast loudness target
- Leave headroom for SFX and avoid full-spectrum constant density
- Provide 1-2 alternate mixes if time allows: normal and low-intensity
- Document whether the asset is procedural approximation, MIDI-rendered, sample-based, or recorded.

Renderer discovery when working locally:

- Check the project first for existing audio tooling, packages, export scripts, DAW stems, or asset folders.
- If no renderer exists, output MIDI-like JSON plus a rendering brief instead of pretending audio was rendered.
- If a renderer exists, generate or update the asset, then verify that the file exists and the loop duration matches the metadata.
- If dependency installation, network access, or external software is required, ask/escalate according to the active environment rules.

## Unity

- Use AudioMixer groups: `Music`, `SFX`, `UI`, optionally `Ambience`.
- Loop BGM clips with sample-accurate loop points when possible.
- For stems, start all AudioSources on the same DSP time and automate mixer volume.
- Trigger stingers on event, beat, or bar boundary depending on gameplay urgency.

## Godot

- Use audio buses: `Music`, `SFX`, `UI`, optionally `Ambience`.
- Use `AudioStreamPlayer` or multiple players for stems.
- Keep loop assets trimmed and test import loop flags.
- For adaptive layers, adjust bus/player volume rather than recreating streams each frame.

## Web Delivery Notes

- Respect browser autoplay: initialize/resume audio only after user gesture.
- For rendered assets, preload or lazy-load without blocking first input.
- For procedural audio, use a master bus plus separate music and SFX gain.
- Stop/dispose sources and scheduled loops on reset, scene change, or unmount.
