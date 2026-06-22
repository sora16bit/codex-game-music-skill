# SFX Recipes

Use these as starting points for procedural sounds, asset briefs, or revision notes. Keep critical SFX more readable than BGM. Tie non-critical UI and reward sounds to the track scale or motif when possible.

## Core Parameters

- Attack: transient clarity. Short attacks read as clicks, cuts, impacts, or UI taps.
- Body: identity and mass. Use pitch, waveform, noise color, filter, and duration.
- Tail: space and feedback. Use decay, delay, reverb, or filtered release sparingly.
- Pitch motion: upward for activation/reward, downward for failure/impact, wobble for magic/instability.
- Register: low for weight, mid for gameplay readability, high for urgency and UI sparkle.

## Recipes

### UI Confirm

- Shape: short bright attack, 80-160 ms body, slight upward pitch.
- Notes: use tonic, fifth, or motif note; keep quieter than reward stingers.
- Avoid: long tails that stack during menu navigation.

### UI Cancel / Back

- Shape: soft click plus downward minor third or fourth, 100-180 ms.
- Timbre: triangle/sine with low-pass, or muted pluck.
- Avoid: harsh error tone unless the action truly failed.

### Item Pickup

- Shape: bright transient, quick arpeggio or two-note lift, 200-450 ms.
- Pitch: scale degree 1-3-5, 5-6-8, or motif fragment.
- Variant: rare item adds octave sparkle and longer tail.

### Unlock / Ability Gained

- Shape: 1-2 bar stinger, motif stated clearly, low support hit plus high lift.
- Harmony: brighten mode, add major sixth/ninth or suspended resolution.
- Mix: briefly duck dense BGM if needed.

### Slash / Cut

- Shape: 5-20 ms bright transient, 60-140 ms filtered noise slice, 80-220 ms low/mid body when hitting.
- Motion: fast downward or upward pitch sweep depending on weapon weight.
- Variants: air slash lacks low impact; heavy slash adds low thump and longer tail.

### Hit / Impact

- Shape: click or crack transient, 70-180 ms body, short low decay.
- Timbre: noise burst plus sine/triangle low thump; add distortion for heavy damage.
- Gameplay: damage impacts should cut through music but not mask follow-up actions.

### Jump

- Shape: short upward sweep, 80-180 ms, light body.
- Timbre: sine/triangle or filtered noise puff.
- Avoid: making every jump sound like a reward.

### Land

- Shape: low-mid thud, 60-160 ms; add grit for heavy surfaces.
- Variant: small landing is mostly transient; hard landing adds low body and dust/noise.
- Gameplay: communicate weight without over-triggering fatigue.

### Dash / Boost

- Shape: quick whoosh with sharp start, 120-300 ms, optional Doppler pitch movement.
- Timbre: filtered noise plus tonal accent.
- Sync: can quantize to 8th/16th subdivision if dash is rhythmic.

### Danger Warning

- Shape: repeating high-mid pulse or short alarm motif.
- Pitch: use tritone, minor second, or unresolved dominant color.
- Rule: become more frequent or brighter with danger; do not drone constantly.

### Failure / Death

- Shape: immediate low hit, downward gesture, short silence or tail.
- Harmony: invert or darken main motif.
- Mix: clearly interrupts but should not be painfully loud.

### Victory / Clear

- Shape: bright motif resolution, 1-4 bars for small win, 4-8 bars for major clear.
- Harmony: major third/sixth lift or brighter mode.
- Integration: reuse level motif so success feels earned.

### Magic / Spell

- Shape: charge, cast transient, tail. Charge rises; cast defines element; tail sells space.
- Timbre: modulated sine/triangle for clean magic, noise/filter movement for dark magic.
- Gameplay: charge loops should have variation and a clear release.

### Mechanical Tool

- Shape: tactile click, motor/gear body, short mechanical tail.
- Timbre: square/pulse, filtered noise, metallic ticks.
- Differentiate tools by rhythm and pitch range, not just volume.

### Sci-Fi Tool

- Shape: activation chirp, energy body, deactivation tail.
- Timbre: FM-like tones, filter sweeps, narrow-band noise.
- Avoid: constant high whine that competes with warnings.

## Revision Diagnostics

- Too cheap: add attack/body/tail structure, pitch motion, and a second layer.
- Too quiet: improve transient and register before only raising gain.
- Too harsh: soften attack, shorten high-frequency tail, or lower resonance.
- Too samey: vary envelope, pitch contour, noise color, and motif interval by action class.
- Masks BGM: shorten tail, move register, or duck a music layer at trigger time.
