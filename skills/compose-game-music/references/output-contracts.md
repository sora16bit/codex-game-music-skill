# Output Contracts

Use these contracts when the task needs reliable structure. Keep them concise in the final answer unless the user asks for full detail.

## Critique Contract

1. Verdict: usable as-is, usable with changes, or needs rebuild.
2. Top issues: list the top 3 by musical/gameplay impact, not by ease of fixing.
3. Evidence: tie each issue to motif, form, rhythm, harmony, bass, texture, sound source, mix, SFX space, adaptation, or implementation.
4. Fix plan: state concrete changes to notes, phrase form, layer roles, mix, transitions, or code.
5. Verification: state what to test in-game.

Use 0-3 scores when helpful:

| Area | Score | Question |
| --- | --- | --- |
| Concept fit |  | Would a listener guess the scene without the title? |
| Function |  | Does it support player action and pacing? |
| Motif |  | Is there memorable identity within 10-20 seconds? |
| Form |  | Is there phrase-level development? |
| Thickness |  | Are low/mid/high, point/line/plane, and transient roles covered when needed? |
| Source |  | Is the sound-source route honest and good enough? |
| Loopability |  | Can it repeat without obvious fatigue? |
| SFX space |  | Are gameplay sounds still readable? |

## BGM Spec Contract

```text
Cue:
Scene role:
Gameplay function:
Deliverable:
Sound source honesty:

Design card:
- BPM / meter:
- Key or tonal center / mode:
- Loop length:
- First 5 seconds:
- Phrase form:
- Motif:
- Harmonic rhythm:
- Bass function:
- Counterline / inner motion:
- Point / line / plane roles:
- Density curve:
- Negative space:
- Loop return:

Layers:
- base:
- bass:
- harmony:
- lead:
- counterline:
- texture:
- percussion / impacts:
- stingers:

Self-review:
- fit/function/motif/form/thickness/source/loopability/SFX:
```

## Note Pattern Contract

When giving notes, include enough timing to implement without guessing.

```text
Bars 1-4:
- Lead: scale degrees or notes with rhythm.
- Bass: role plus note/rhythm.
- Harmony: chord/function and voice-leading note.
- Event: fill, impact, or rest.
Bars 5-8:
- State what repeats, answers, varies, contrasts, and returns.
```

Prefer scale degrees for legal safety when discussing references. Use exact notes only for original output, public-domain material, or user-provided material.

## MIDI-like JSON Contract

```json
{
  "title": "cue_name",
  "sourceType": "original MIDI-like composition",
  "bpm": 132,
  "meter": "4/4",
  "scale": "D Dorian",
  "loopBars": 8,
  "swing": 0,
  "layers": [
    { "name": "base", "role": "pulse", "gain": [0.15, 0.35], "state": "always" }
  ],
  "tracks": [
    {
      "name": "bass",
      "instrument": "synth bass or rendered bass patch",
      "role": "moving pressure",
      "notes": [
        { "bar": 1, "beat": 1, "dur": 0.5, "note": "D2", "vel": 0.78 }
      ]
    }
  ],
  "transitions": [
    { "from": "base", "to": "danger", "boundary": "bar", "rule": "fade in when threat > 0.55" }
  ],
  "sfxPriority": "duck music 2-4 dB for critical warning and fail SFX"
}
```

## Stem Plan Contract

```text
Cue name:
BPM / meter / key:
Loop: bars and exact seconds:
Files:
- cue_base.wav/ogg:
- cue_bass.wav/ogg:
- cue_harmony.wav/ogg:
- cue_lead.wav/ogg:
- cue_danger.wav/ogg:
- cue_reward.wav/ogg:
All stems:
- same start sample, length, sample rate, and loop boundary
- render with headroom for SFX
Gain rules:
- base:
- bass:
- harmony:
- lead:
- danger:
- reward:
Transitions:
- vertical fade:
- horizontal section:
- stinger:
Validation:
- seamless loop
- no click at boundary
- SFX readable
- early intensity not inert
```

## Implementation Contract

Before editing:

- Inspect existing audio libraries, asset loading, update loop, state model, and cleanup lifecycle.
- Avoid new dependencies unless already present or approved.
- Decide whether to add procedural audio, asset playback, or metadata only.

After editing, summarize:

- Music brief
- Files changed
- What was implemented
- How it adapts to game state
- Cleanup/autoplay/SFX bus handling
- Verification performed and any gaps
