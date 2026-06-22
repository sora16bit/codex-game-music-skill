# Industry Concepts

Use these concepts when game music needs to feel closer to shipped game audio.

## Adaptive Music

Adaptive music changes in response to player actions or game state. Common changed parameters include volume, arrangement, tempo, density, and transitions.

## Vertical Orchestration / Layering

Keep multiple layers or stems aligned to the same musical timeline, then add/remove layers based on intensity. Typical layers:

- Sub or low pulse
- Bass
- Percussion
- Harmony/pad/chord stabs
- Lead motif
- Texture/noise/danger layer
- Reward/victory color

In code-only prototypes, functions can stand in for stems, but they still need separate density and gain control.

## Horizontal Re-sequencing

Switch between different musical sections at phrase boundaries:

- A section: baseline traversal or exploration
- B section: higher pressure or active puzzle
- Breakdown: planning/safe state
- Bridge/fill: transition into danger or success
- Stinger: short event cue for unlock, death, victory, fail, warning

Avoid random immediate switches unless the game intentionally needs shock.

## Phrase and Bar Awareness

Important transitions should generally wait for a beat, bar, or phrase boundary. This makes changes feel composed instead of arbitrary.

Common scheduling choices:

- Immediate: damage, death, critical warning, pause.
- Next beat: UI confirm, pickup, small reward.
- Next bar: danger layer, combat layer, exploration detail.
- Next phrase: section change, boss phase music, victory transition when not urgent.

## SFX Integration

Game SFX can be tied to the score:

- Share motif notes or scale tones with the BGM.
- Quantize non-critical UI sounds to subdivisions.
- Use contrasting envelopes for different tool classes.
- Keep critical gameplay SFX readable above the music.

## Practical Threshold

If oscillator-only music still feels cheap after layering, form, and mix fixes, recommend rendered loops/stems, MIDI plus a real synth/soundfont, or DAW-produced assets. Raw oscillators are useful for prototypes, but they are not a substitute for production sound design.

## Intensity Model

Treat intensity as a musical control signal, not only a volume value.

- 0.00-0.20: ambience, pulse, sparse motif, no busy percussion.
- 0.20-0.45: baseline play; bass, light drums, simple harmony.
- 0.45-0.70: active challenge; denser percussion, more bass, motif variation.
- 0.70-0.90: danger or late-stage; high pulse, fills, brighter filters, tension layer.
- 0.90-1.00: climax; use briefly unless the game is constantly extreme.

Map variables such as speed, health, threat, combo, timer, area depth, and boss phase to intensity with smoothing. Avoid frame-by-frame jitter; use thresholds, hysteresis, or phrase-bound updates.

## Leitmotif System

Build one small identity cell and reuse it with transformations:

- Victory: same motif with brighter mode or upward resolution.
- Failure: inverted, slowed, or downward version.
- Danger: compressed rhythm, dissonant interval, higher register.
- UI: first two or three notes as short confirm/unlock cues.
- Boss/player relationship: boss motif can interrupt or distort player motif.

## Arrangement Roles

Each layer should have a job:

- Pulse: time and motion.
- Bass: weight and threat.
- Harmony: color and area identity.
- Lead: memorable motif.
- Texture: danger, place, or magic.
- Percussion: energy and readability.
- Stinger: event meaning.

If two layers do the same job in the same register, remove or simplify one before adding more notes.

## Avoiding Formulaic Tension

Do not rely on a constant repeated "chug" as the default signifier for battle, chase, or boss music. A pulse can exist, but it should have a compositional reason and should change jobs over time.

Useful alternatives:

- Rhythmic displacement: move the motif one subdivision early or late in the answer phrase.
- Uneven accent groups: use 3+3+2, 2+2+3, 5+3, or phrase-specific accents instead of identical beats.
- Negative space: drop percussion or bass for a bar so the next impact means more.
- Role rotation: let bass carry the pulse in one section, percussion in another, harmony in another, and melody in the climax.
- Reharmonization: keep the motif but change the chord beneath it.
- Interruption: let the boss/danger motif cut across the player motif rather than merely adding another layer.
- Register drama: move the same idea between low, mid, and high registers to imply struggle.

When revising a formulaic cue, remove one habitual layer before adding anything new.

## Percussion Palette Choice

Choose percussion deliberately. A snare/backbeat can be correct for some action music, but it should never be the automatic answer to intensity.

Before adding a snare-like layer, ask:

- Does the setting imply military, rock, marching, or arcade language?
- Would low impacts, silence, organ pedal, choir rhythm, frame drum, hand percussion, metallic hits, or bass motion communicate the scene better?
- Is the rhythm expressing the character/world, or only filling space?

For final battles, tension can come from harmonic gravity, unresolved suspensions, register extremes, antiphonal motifs, sudden rests, and boss-theme interruptions before percussion density.

## TPO: Active Battle vs Location Atmosphere

Separate "this place is ominous" from "the player is fighting now."

Active final battle cues need:

- Immediate foreground event in the first 5 seconds.
- Shorter attacks and clearer rhythmic or melodic propulsion.
- Motifs that answer, interrupt, or collide within 1-2 bars.
- Harmonic rhythm that changes often enough to imply danger.
- Low-end motion or impact that supports action, not only scale.

Location/castle ambience can use:

- Long drones and slow pads.
- Sparse motif fragments.
- Distant reverb and low motion.
- Longer silences with little consequence.

If a final battle cue feels chill, reduce ambience before adding more layers.
