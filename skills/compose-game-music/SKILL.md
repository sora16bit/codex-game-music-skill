---
name: compose-game-music
description: Create, critique, revise, and integrate scene-fit game music and SFX for games and interactive scenes. Use when Codex needs to infer an audio brief, compose BGM, improve weak/thin/generic music, design gameplay/UI SFX, choose Web Audio/Tone.js/MIDI/rendered loop/stem/Unity/Godot deliverables, implement audio in a repo, study legal game-score references, or judge whether music fits gameplay, scene, loop, and production quality.
---

# Compose Game Music

## Status

Treat this skill as experimental for production-quality rendering, but strong for composition direction, symbolic music, adaptive music design, procedural Web Audio prototypes, SFX design, critique, and implementation. For realistic ensemble performance, polished soundtrack assets, or "real game music" quality, move toward MIDI plus a credible synth/SoundFont, rendered loops, synchronized stems, or an external production brief instead of endlessly polishing oscillator-only output.

## Operating Modes

Pick exactly one primary mode before acting, then load only the references needed for that mode.

- **Critique mode**: use when asked to find problems, review, judge fit, or explain why music is weak. Output verdict, top issues, fix plan, and verification. Read [references/review-checklist.md](references/review-checklist.md).
- **Compose spec mode**: use when no repo edit or renderer is required. Output a complete cue design card, motif/rhythm/harmony/bass layers, loop plan, and optional MIDI-like JSON. Read [references/composition-design-gates.md](references/composition-design-gates.md) and, for BGM, [references/composition-theory-core.md](references/composition-theory-core.md).
- **Implementation mode**: use when editing a game/app repo. Inspect existing audio/runtime first, match its style, and implement the smallest usable audio system change. Read [references/web-audio-patterns.md](references/web-audio-patterns.md) for raw browser audio, or [references/deliverable-formats.md](references/deliverable-formats.md) for engines/assets.
- **Production handoff mode**: use when quality exceeds procedural synthesis or the user asks for real/proper/game-quality output. Provide MIDI-like data, MIDI/rendering plan, stem plan, rendered-loop brief, or engine handoff metadata. Read [references/deliverable-formats.md](references/deliverable-formats.md) and [references/output-contracts.md](references/output-contracts.md).

If a request contains both BGM and SFX, keep music and SFX separable in buses, files, data structures, and explanation.

## Core Workflow

Do not turn prompt adjectives directly into instruments or effects. Always pass these gates before generating notes or code:

1. **Concept translation**: name the scene in one phrase; infer scene role, player motion, threat/safety, place identity, camera scale, gameplay function, and loop fatigue target.
2. **Composition design**: decide BPM, meter, tonal center/mode, loop length, phrase form, motif, harmonic rhythm, bass function, counterline/inner motion, density curve, adaptive layers, and negative space.
3. **Surface design**: define point/line/plane roles, register, articulation, note length, overlap, dynamics, distance, room/tail behavior, and which notes sustain or bridge phrase/chord boundaries.
4. **Deliverable choice**: choose Web Audio, Tone.js, MIDI-like JSON, MIDI, MusicXML/ABC, rendered loop, stems, Unity/Godot plan, or hybrid. State whether the result is procedural approximation, MIDI-rendered, sample-based, or recorded.
5. **Self-review**: score concept fit, function, motif, form, thickness, idiom, sound-source honesty, loopability, SFX space, and implementation safety. Rebuild the design card if concept fit, function, or sound source fails.

Before full rendering, prove the cue with a music-only sketch: motif plus bass or harmony, optional counterline, phrase form, and loop return. If it fails with plain tones, effects will not fix it.

## Minimum Output Contracts

Use [references/output-contracts.md](references/output-contracts.md) whenever the response must be structured. At minimum:

- A **critique** must include a verdict, top 3 issues by impact, concrete fixes, and in-game verification.
- A **BGM spec** must include cue metadata, 4/8/16-bar form, motif, harmonic plan, bass role, layers, loop return, and self-review scores.
- A **MIDI-like output** must include `bpm`, `meter`, `scale`, `loopBars`, `tracks`, note `bar/beat/dur/note/vel`, and layer intent.
- A **stem/render brief** must include exact bars/seconds, BPM, sample rate target if known, file names, loop boundaries, gain ranges, transition rules, and SFX priority.
- An **implementation summary** must include music brief, implemented files, adaptation model, cleanup/autoplay handling, and verification.

## Bundled Scripts

Use [scripts/render_demo_mids.py](scripts/render_demo_mids.py) as a deterministic, dependency-free Standard MIDI writer for the bundled demos and for quick validation of MIDI-first output. It writes field/exploration examples plus active battle and final boss tests using only Python's standard library.

Prefer adapting this script when the user asks for a quick playable `.mid` prototype and no project-specific renderer exists. For production audio, still prefer DAW/SoundFont/rendered stems when quality matters.

## Revision Rules For Weak Music

When the user says music is weak, thin, too quiet, generic, repetitive, monotonous, not like real game music, or missing drama, treat it as a required rebuild brief. Diagnose structure, arrangement density, mix level, state changes, motif strength, and sound source before changing volume.

Rebuild against these targets:

1. Presence: stronger envelopes, midrange, register spread, layering, and bus gain while preserving SFX readability.
2. Form: A/B sections, fills, pickups, breakdowns, stingers, 8/16/32-bar phrase changes, and loop return.
3. Thickness: intentional low, mid, high, transient, line, plane, and event roles.
4. Motion: variation in rhythm, octave, chord voicing, density, contour, and phrase answer.
5. Identity: a motif that recurs in BGM, UI/tool SFX, unlock, fail, and victory where appropriate.
6. Gameplay sync: intensity tied to stage, threat, health/resource, timer, speed, boss phase, player state, or unlocks.
7. Sound design discipline: remove constant drones, hums, hiss, static, and white-noise beds unless they have a specific scene job.
8. Source realism: if fake instrumentation is the failure, switch to MIDI + credible synth/SoundFont, rendered stems, or production handoff.

For runners, chases, speed games, and battles, do not start inert. Use a nonzero baseline intensity around 0.20-0.30 for procedural Web Audio, with audible pulse/bass/core harmony and room for escalation.

## Adaptive Music Standards

Use established interactive-music techniques:

- Vertical layering: fade percussion, bass, harmony, lead, danger, reward, and texture layers by game state without restarting the phrase.
- Horizontal re-sequencing: move between A/B/C, calm, danger, battle, bridge, victory, failure, and menu sections at beat/bar/phrase boundaries.
- Phrase awareness: schedule important changes on musical boundaries unless gameplay urgency demands immediate response.
- Leitmotif reuse: keep a small motif stable enough to survive changes of tempo, harmony, register, timbre, and scene meaning.
- Music/SFX sync: quantize UI/tool SFX to musical subdivisions when it improves feel; do not delay urgent danger/failure cues.
- Intensity model: map game variables to density, register, harmonic pressure, rhythm, and layer gain, not only volume.

## Composition Rules

- Prefer one strong small motif over many unrelated notes.
- Prove motif, harmonic logic, bass function, phrase form, voice continuity, and at least one development device before arranging.
- Use 4, 8, 16, or 32-bar game forms; 8/16/32-step patterns are useful for procedural loops.
- Make phrases answer each other. For 4 bars use statement/answer/variation/return; for 8 bars use A/A'/B/return or antecedent/consequent plus fill.
- Treat chord labels as horizontal voices. Use common tones, suspensions, anticipations, delayed releases, contrary motion, and inner motion so harmony does not become block triggers.
- Make bass do a job: pedal, walk, ostinato with variation, threat pulse, contrary answer, ground, or deliberate absence.
- Use nonchord tones with behavior: passing, neighbor, suspension, appoggiatura, anticipation, pedal, or prepared color. Random dissonance is not depth.
- Leave space for SFX. Music should not occupy every frequency range all the time.
- Avoid using constant backbeat, repeated ostinato, chugging, snare, or broadband noise as the default tension solution.
- Distinguish active combat from location ambience. Active final battles need foreground motion in the first 5 seconds through motif exchange, bass movement, harmonic acceleration, rhythmic propulsion, or event-like impacts.
- Be honest about sound sources. Oscillator layers are "string-like", "choir-like", "organ-like", "fiddle-like", or "brass-like" approximations unless actual samples, SoundFonts, MIDI instruments, or recorded/rendered assets are used.
- Avoid copying named artists, songs, soundtracks, melodies, basslines, chord voicings, or arrangements. Use broad style and mechanism descriptors.

## Source Study Rules

When asked to learn from real game music, scores, sheet music, MIDI, MusicXML, ABC, public analyses, or soundtrack examples, read [references/score-study-workflow.md](references/score-study-workflow.md) and [references/game-score-study-patterns.md](references/game-score-study-patterns.md).

Use legal sources only: public-domain music, user-provided/licensed scores, official licensed books the user owns, self-authored examples, or short analytical excerpts. If using web summaries or fan transcriptions, extract only abstract mechanisms and do not reproduce exact notes. Convert references into contour, rhythm grammar, form, harmonic function, bass role, texture, loop return, and gameplay function before composing.

Practical lessons to preserve from real game music and theory:

- Game cues must fit action, controls, SFX, and loop fatigue, not only mood.
- Memorable loops rely on repetition with hierarchy: motif to phrase to section, not random novelty.
- Player motion is often rhythmic before it is instrumental.
- A short motif is valuable only if it can be repeated, answered, varied, and reused across states.
- Adaptive music needs both arrangement changes and phrase-boundary logic.

## SFX Rules

Treat gameplay SFX as part of musical readability.

- Slash/cut sounds need attack, body, and tail.
- Impacts need mass, material, and gameplay importance.
- UI/tool sounds should share motif notes, scale tones, rhythm cells, or timbral family with the BGM when useful.
- Failure/death must cut through without painful loudness.
- Victory/reward needs a concise cadence or color change, not only a louder sound.
- Bridge, stasis, cut, gravity/pin, magic, mechanical, and warning sounds should be distinguishable.
- If SFX feels wrong, revise envelope, pitch movement, noise color, transient/body/tail, and timing before replacing the whole audio system.

Read [references/sfx-recipes.md](references/sfx-recipes.md) for concrete SFX patterns.

## Reference Loading

Read only what is relevant:

- Common scene styles: [references/scene-recipes.md](references/scene-recipes.md)
- Concept gates and quick design cards: [references/composition-design-gates.md](references/composition-design-gates.md)
- Stronger composition theory: [references/composition-theory-core.md](references/composition-theory-core.md)
- Legal score/reference study: [references/score-study-workflow.md](references/score-study-workflow.md)
- Game-score mechanisms: [references/game-score-study-patterns.md](references/game-score-study-patterns.md)
- Scene recognizability failures: [references/scene-recognition-and-failures.md](references/scene-recognition-and-failures.md)
- Battle/boss/chase/final battle: [references/battle-music-design.md](references/battle-music-design.md)
- Instrumentation and ensemble texture: [references/instrumentation-and-texture.md](references/instrumentation-and-texture.md)
- Musical surface and continuity: [references/musical-surface.md](references/musical-surface.md)
- Browser implementation: [references/web-audio-patterns.md](references/web-audio-patterns.md)
- Deliverable choice and engine handoff: [references/deliverable-formats.md](references/deliverable-formats.md)
- Critique/review: [references/review-checklist.md](references/review-checklist.md)
- Industry interactive-music concepts: [references/industry-concepts.md](references/industry-concepts.md)
- Structured response templates: [references/output-contracts.md](references/output-contracts.md)

## Final Response Shape

Match the chosen mode. Do not force note/chord/integration sections into a pure critique.

- Critique: verdict, top issues, fix plan, verification.
- Compose spec: music brief, deliverable format, design card, notes/patterns/chords, loop/adaptation, self-review.
- Code edit: music brief, what changed, how it adapts, how verified.
- Production handoff: cue metadata, asset/stem/MIDI plan, transition rules, integration instructions, validation checklist.
