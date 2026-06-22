# Composition Design Gates

Use these gates before composing or revising BGM. The purpose is to prevent prompt words from becoming a pile of musical symbols. A cue should prove the concept through rhythm, phrase behavior, texture, form, and sound source choice.

## Gate 1: Concept Translation

Convert the scene into musical jobs before naming instruments.

Answer these:

- Scene role: field, battle, boss, town, dungeon, menu, event, or transition.
- Player motion: walking, sailing, climbing, sneaking, fleeing, fighting, reading, waiting, or recovering.
- Camera scale: intimate, room-sized, area-wide, horizon-wide, cosmic, or claustrophobic.
- Emotional action: move forward, relax, brace, investigate, celebrate, grieve, or survive.
- Place identity: climate, culture, architecture, material, landscape, technology, and magic level.
- Loop fatigue target: how many minutes the loop should tolerate before it becomes tiring.

Reject shallow translations:

- "Hot" does not automatically mean high noise or bright filter.
- "Snow" does not automatically mean bells.
- "Fantasy" does not automatically mean harp.
- "Tension" does not automatically mean snare, chugging ostinato, or constant low pulses.
- "Epic" does not automatically mean choir and brass.

## Gate 2: Music Design

Write a compact design card:

- BPM and meter.
- Key/scale and the specific color tones that matter.
- Loop length in bars and seconds.
- Phrase form: A, A', B, bridge, breakdown, fill, or stinger positions.
- Motif: 3-8 notes or one rhythm cell.
- Harmonic rhythm: static pedal, 1 chord per bar, 2 chords per bar, modal vamp, or cadence cycle.
- Density curve: what changes every 4, 8, 16, and 32 bars.
- Point/line/plane roles.
- Negative space: what the cue deliberately avoids.

The design must state what is audible in the first 5 seconds. If the concept is not clear by then, the cue needs a stronger opening gesture.

## Gate 3: Idiom And Instrumentation

Choose musical language, not only instruments.

For each instrument-like layer, define:

- Role: theme, counterline, harmonic plane, rhythmic plane, bass foundation, texture, impact, or stinger.
- Register: low, low-mid, mid, high-mid, high, or full-range.
- Articulation: legato, staccato, tremolo, marcato, pizzicato-like, plucked, rolled, breathy, bowed-like, struck, scraped, or sustained.
- Phrase behavior: call, answer, drone, ostinato, cadence glue, pickup, interruption, or echo.
- Variation rule: ornament, displacement, inversion, octave shift, reharmonization, thinning, or rest.

For genre or place identity, specify at least two of these:

- Rhythm grammar: straight, swung, uneven groups such as 3+3+2, 6/8 lilt, dotted march, reel-like drive, hand-drum cycle, or pulse-free ambient.
- Ornament style: grace notes, slides, turns, mordents, trills, bends, ghost notes, rolls, or cuts.
- Cadence behavior: unresolved modal loop, bright cadence, deceptive cadence, suspended cadence, or pedal-based gravity.
- Texture grammar: wide open fifths, close dissonance, tremolo plane, arpeggiated shimmer, antiphonal response, or sparse pointillism.

## Gate 4: Deliverable And Sound Source

Pick the output route based on the failure mode and quality target.

Use procedural Web Audio when:

- The goal is a prototype, small interactive sketch, or tightly code-controlled SFX.
- The user accepts synthesized approximations.
- The cue can survive with simple timbres.

Use MIDI-like data or MIDI when:

- The user needs editable composition.
- The cue needs real phrase design before final rendering.
- The local environment has or can later attach a synth, SoundFont, or DAW.

Use rendered loops or stems when:

- The user wants game-ready perceived quality.
- Instrument realism, ensemble feel, mix, or loop polish matters.
- Adaptive intensity can be handled by vertical layers.

Use hybrid delivery when:

- BGM needs rendered quality but SFX need procedural responsiveness.
- A small build needs one loop plus lightweight stingers.

Always state whether the result is procedural approximation, MIDI-rendered, sample-based, or recorded. Do not describe oscillator layers as real instruments.

## Gate 5: Self-Review And Rebuild

Before final delivery, score these 0-3:

- Concept fit: does the cue sound like the requested scene without the title?
- Function: does it support the player's action?
- Motif: is there a memorable identity within 10-20 seconds?
- Form: is there phrase-level development beyond a static loop?
- Thickness: are point, line, and plane all represented when the scene needs them?
- Idiom: do rhythm, ornament, cadence, and texture match the world?
- Sound source: is the chosen render route good enough for the requested quality?
- Loopability: can it repeat without obvious fatigue?

Rebuild triggers:

- Score 0 in concept fit, function, or sound source.
- Score 1 or lower in three or more categories.
- The cue only communicates the scene through one token instrument or one token effect.
- Muting percussion removes almost all identity.
- Muting texture leaves only disconnected points.
- The first 5 seconds do not communicate the scene role.

When a rebuild triggers, change the design card first. Do not only raise volume, add more notes, or swap patches.

## Quick Design Cards

### Hot, Upbeat Desert Field

- Jobs: forward travel, heat shimmer, open horizon, playful danger, long-loop walkability.
- Possible grammar: 100-124 BPM, 4/4 or 6/8, uneven 3+3+2 accents, modal vamp, ornamented reed/pluck-like theme, hand-drum cycle or bass-carried groove.
- Point/line/plane: shimmer/noise plane, plucked or bass rhythmic line, lead/counterline, sparse metal or clap-like points.
- Avoid: only Phrygian scale plus shaker; too much mystery with no walking pulse; constant high hiss.

### Frozen Snowfield

- Jobs: horizon scale, cold air, isolation, slow movement, fragile warmth at landmarks.
- Possible grammar: 60-88 BPM, wide open fifths, suspended harmony, slow harmonic rhythm, long plane with subtle motion, sparse bell-like points, low warm line entering rarely.
- Point/line/plane: wind/noise plane, pad/string-like plane, slow bass line, fragile motif, distant sparkle points.
- Avoid: constant bells; UI-like sparkle; no low-mid warmth; empty ambient with no travel identity.

### High-Stakes Final Battle

- Jobs: immediate confrontation, world-scale stakes, active player motion, antagonist pressure, phase escalation.
- Possible grammar: 132-176 BPM or half-time, short motif collision within 1-2 bars, faster harmonic rhythm, register extremes, role-rotating propulsion.
- Point/line/plane: tremolo/choir/organ-like plane, heroic line, antagonist counterline, moving bass, sparse decisive impacts.
- Avoid: castle ambience, static organ drone, default snare/backbeat, percussion as the only source of tension.

### Hellfire / Infernal Field

- Jobs: oppressive heat, underworld scale, forward travel under threat, heroic endurance, long-loop pressure.
- Possible grammar: 78-112 BPM, half-time or 12/8 mass, Phrygian dominant / harmonic minor / chromatic cells, low pedal with upper-voice instability.
- Surface: sub pressure, distorted low line, cluster swells, tremolo heat, ash/noise room, sparse stone/metal impacts, one restrained heroic motif.
- Point/line/plane: low-end plane and harmonic pressure first; bass/inner line as motion; impacts as terrain events; lead as survival, not cheer.
- Avoid: light desert groove, bright shaker tokenism, pretty pluck-first writing, or ambience with no walking gravity.
