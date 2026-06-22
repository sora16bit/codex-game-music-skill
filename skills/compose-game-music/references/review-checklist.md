# Review Checklist

Use this when critiquing game music or audio direction.

## Core Questions

- Fit: Does the music match the scene, mechanics, pacing, and art direction?
- Function: Does it help the player understand threat, safety, progress, or reward?
- Motif: Is there a recognizable musical identity within 10-20 seconds?
- Presence: Is the music loud and present enough for the game without masking SFX?
- Form: Does it have phrase-level change, such as A/B sections, fills, breakdowns, or escalation?
- Thickness: Does it use enough layers across low, mid, high, transient, and texture roles?
- Loopability: Can it repeat for minutes without obvious fatigue?
- Space: Are important SFX still readable?
- Adaptation: Do state changes alter the music in a meaningful way?
- Transitions: Are unlocks, death, danger, and victory supported by stingers or layer changes?
- SFX Fit: Do slash, impact, UI, tool, failure, and victory sounds match the action and mix?
- Implementation: Are audio nodes cleaned up, autoplay handled, and timers deterministic?
- Platform: Is the output format actually usable in the target game?
- Source honesty: Does the response accurately describe whether sounds are procedural approximations, MIDI-rendered instruments, sample-based, or recorded?

## Scoring

Use a 0-3 score for each area when a clear critique is requested:

- 0: absent or actively harmful
- 1: present but weak
- 2: functional with fixable gaps
- 3: strong for the current project stage

Report the top 3 fixes first. Avoid giving equal weight to minor mix issues and structural problems.

## Diagnosis Map

### "Thin" or "Cheap"

- Likely causes: single oscillator line, no low/mid/high role split, weak envelopes, no percussion/noise layer, no room/tail.
- Fixes: add sub or bass role, chord/pad/stab role, short noise percussion, lead doubling, phrase fills, and better gain staging.

### "Fake Instrumentation"

- Likely causes: raw oscillators are described as real instruments, all patches share the same envelope/timbre, or the requested quality exceeds procedural synthesis.
- Fixes: be explicit that the sound is an approximation; switch to MIDI + SoundFont/synth, rendered stems, or external production if realistic ensemble quality matters.

### "Too Quiet"

- Likely causes: low master/music gain, timid envelopes, no midrange presence, SFX masking, long attacks.
- Fixes: increase bus gain moderately, add stronger transient/mid layer, shorten attacks, spread registers, and preserve SFX headroom.

### "Repetitive"

- Likely causes: no A/B section, no phrase fills, identical rhythm every bar, no intensity curve.
- Fixes: add 8/16/32-step form, pickups, fills, lead variations, breakdowns, or state-bound layers.

### "Formulaic" or "Same Under The Hood"

- Likely causes: tension is carried by the same constant backbeat/ostinato in every cue, only timbre changes, accompaniment never yields to melody/harmony, no rests or phrase-level argument.
- Fixes: remove the default chugging layer for at least one section, rotate the pulse between bass/percussion/harmony, use uneven accent groups, add call-response, reharmonize the motif, interrupt the loop with silence or held notes, and make the next section answer the previous one.
- Check: mute the drums. If the cue loses almost all identity, the composition is underdeveloped.

### "Everything Uses Snare"

- Likely causes: combat intensity is always translated into backbeat/snare-like transients, regardless of setting, culture, monster scale, or scene mood.
- Fixes: ban snare-like layers for the revision pass, then rebuild tension from harmony, register, phrase interruption, low impacts, non-Western/cultural percussion, texture, or silence. Reintroduce snare only if it has a specific dramatic reason.
- Check: if replacing the snare with silence improves the cue's identity, it was a crutch.

### "Annoying"

- Likely causes: constant high loop, piercing resonance, unchanging drone, too frequent alert, clashing SFX.
- Fixes: lower/soften high content, add rests, threshold danger sounds, shorten tails, or move elements to lower register.

### "Doesn't Feel Like Game Music"

- Likely causes: not tied to mechanics, no loop design, no stingers, no adaptive response, no clear function.
- Fixes: define gameplay function, map state to layers, add event cues, validate loop fatigue, and reuse a motif across BGM/SFX.

### "Good Track, Bad Fit"

- Likely causes: genre mismatch, wrong energy curve, masks gameplay cues, too much emotional specificity.
- Fixes: simplify arrangement, adjust tempo/density, shift instrumentation, and reserve dramatic sections for events.

### "Too Chill / Castle Ambience Instead Of Battle"

- Likely causes: long pads and drones carry the cue, attacks are too soft, percussion/low motion is too sparse, motif answers are too slow, harmonic rhythm is slow, reverb creates distance instead of urgency.
- Fixes: move active material into the first 5 seconds, shorten envelopes, increase foreground motif exchange, accelerate harmonic rhythm, use bass motion or culturally fit impacts for propulsion, reduce ambient beds, and make the boss/player motifs collide.
- Check: the cue should still feel like a fight if the listener imagines no environment visuals.

## Response Pattern

When reviewing, answer in this order:

1. Verdict: usable as-is, usable with changes, or needs rebuild.
2. Top issues: list concrete problems by impact.
3. Fix plan: specific musical, mix, and implementation changes.
4. Verification: what to test in-game, such as loop fatigue, SFX readability, state changes, and browser autoplay.

Do not use the composition-spec response shape for critique-only requests. If the user asks to find problems in a skill, codebase, cue, or audio direction, lead with findings and avoid inventing notes/chords unless a fix sketch is requested.

## Rebuild Threshold

Call for a rebuild, not a parameter tweak, when any of these are true:

- Concept fit, gameplay function, or sound-source suitability scores 0.
- Three or more core areas score 1 or lower.
- The cue only works because of one token instrument, one token effect, or one constant rhythm layer.
- Muting percussion, noise, or ambience removes almost all identity.
- The first 5 seconds do not communicate player action or scene role.
- The requested quality exceeds the chosen sound source.
