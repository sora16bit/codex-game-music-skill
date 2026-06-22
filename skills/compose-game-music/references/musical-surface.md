# Musical Surface

Use this when the user says the music is not a "surface", "plane", or "面", or when a cue has layers but still feels like disconnected events. In this skill, surface means the total musical behavior of the cue: attack, sustain, release, note length, overlap, phrasing, dynamics, register, harmony, room, mix depth, and how layers breathe together.

## Surface Is Not Just A Pad

A long pad can help, but it is not enough. A convincing surface usually comes from several dimensions working together:

- Articulation: legato, detached, accented, brushed, tremolo-like, rolled, strummed, bowed-like, breathy, or struck.
- Note length: short points, medium gestures, held tones, tied notes, and phrase tails.
- Overlap: one line starts before another ends, held tones bridge phrases, releases smear into the next attack.
- Dynamics: small swells, accents, phrase arcs, call-response intensity, and thinning.
- Register: low foundation, low-mid warmth, mid body, high detail, and avoided ranges.
- Harmony: voice leading, suspensions, pedals, contrary motion, passing tones, and cadence behavior.
- Rhythm field: not only drums; repeated bowing, tremolo, arpeggios, bass motion, hand percussion, or harmonic pulses.
- Room and mix: dry foreground, shared room, reverb tails, delay, panning, and front/back depth.

If every layer has the same envelope, the same grid, and the same dry placement, the result will feel like points even when many notes are present.

## Surface Design Pass

Before rendering, write these decisions:

1. Foreground surface: what carries attention, how it attacks, how it releases, and how it breathes.
2. Middle surface: what keeps continuity between foreground events.
3. Background surface: what makes the place feel continuous without stealing focus.
4. Motion surface: what creates travel, danger, calm, or ritual pressure without relying only on drums.
5. Tail surface: what remains after notes end: silence, room, delay, heat, wind, tremolo, or harmonic resonance.

For each layer, define:

- `attack`: immediate, soft, bowed-like, plucked, struck, breathy, or swelling.
- `body`: sustained, decaying, tremolo, pulsing, noisy, vowel-like, or filtered.
- `release`: dry stop, short tail, room tail, delay, reverb, or overlap into next phrase.
- `phrase role`: pickup, statement, answer, suspension, cadence, interruption, or glue.

## Voice And Phrase Continuity

Use these techniques to turn points into music:

- Tie at least one note across a barline in every important 2-4 bar phrase.
- Let a counterline begin before the lead phrase ends.
- Change harmony under a held note.
- Use anticipations and pickups into strong beats.
- Vary note lengths inside the same motif; avoid every note being the same duration.
- Let bass and inner voices move when the melody holds.
- Use rests deliberately; silence should feel like phrase punctuation, not missing data.
- Keep a shared room or tail for related layers so they feel like one world.

## Block-Chord Punching Failure

When feedback says the cue feels like "points", "not connected", "just a chord progression", "打ち込んだだけ", or "音が繋がってない", assume the main failure is not layer count. It is usually that every voice attacks and releases together, so the harmony behaves like rectangular blocks instead of a performed surface.

Before adding instruments, rewrite the phrase so at least three of these are true:

- One foreground or inner note is held across a chord change.
- One common tone remains while the bass or harmony moves beneath it.
- One suspension resolves after the new harmony arrives.
- One line enters before the previous line fully releases.
- One bass pickup or anticipation points into the next bar.
- One phrase tail rings into the next attack instead of stopping dry.
- The melody contains a long note while inner voices continue moving.

For piano-like, organ-like, string-like, choir-like, or pad-like parts, explicitly plan sustain time and release time. A note ending exactly when the next chord starts is often too clean; let selected notes overlap, smear, or resolve late. For plucked parts, use ringing tails, broken chords, anticipations, and pedal tones instead of only detached attacks.

The quick test: reduce the cue to piano. If it feels like someone pressing block chords every bar with no pedal, no legato, no suspensions, and no melodic breath, rewrite note lengths and voice leading before changing timbre.

## Procedural Rendering Rules

Raw oscillators make surface problems worse because they do not naturally contain instrumental noise, body resonance, or performance imperfections. When rendering procedurally:

- Do not use the same envelope shape for every layer.
- Do not quantize every note to the same start/end grid. Schedule some notes to cross the grid, sustain over harmony changes, or release after the next attack.
- Give leads a mixture of note lengths and connected releases.
- Add subtle pitch drift, vibrato, or brightness movement only where musically motivated.
- Use a common early-reflection or short room for ensemble glue.
- Avoid full wet reverb on everything; distant layers can be wetter, foreground layers should stay readable.
- Make sustained layers evolve in filter, voicing, rhythm, or dynamics; static drones become ambience.
- Add low-mid body where appropriate; high sparkle alone sounds like UI.
- Avoid using broadband noise as a universal surface. Noise should be event-shaped, filtered narrowly, intermittent, or tied to a concrete source; a constant "shhh" layer quickly reads as cheap static rather than place.
- Prefer fewer, better-behaved layers over many unrelated points.

## Surface Failure Diagnoses

### "Interesting But Not The Requested Music"

- Likely causes: timbral novelty is stronger than scene function, or the cue's surface suggests a different genre/world than the prompt.
- Fixes: restate the gameplay job, simplify novelty layers, and rebuild the surface around movement, scale, and player emotion.

### "Layered But Still Not Musical"

- Likely causes: layers share identical attacks/releases, no voice leading, no overlap, no dynamic arcs, and no shared room.
- Fixes: redesign envelopes, add phrase overlaps, write inner motion, and create a shared room/tail.

### "Pad Plus Dots"

- Likely causes: background plane exists but foreground and middle surfaces do not connect to it.
- Fixes: add a middle layer with medium note values, make lead notes overlap into the pad, and let harmony move under held tones.

### "Unnatural Performance"

- Likely causes: exact grid timing, equal velocities, identical note lengths, no breath or bow logic, and no phrase contour.
- Fixes: use phrase-level velocity arcs, human-scale rests, varied note values, grace notes only where idiomatic, and articulation-specific envelopes.

### "Constant Static / Zaa Noise"

- Likely causes: broadband noise used as a default ambience bed, too many noise-based layers at once, high-frequency noise left continuous, or the same filtered-noise gesture reused across scenes.
- Fixes: remove the constant noise bed, keep only sparse concrete events, replace air with pitched room resonance or low-frequency movement, and use silence/tails for space.

## Rebuild Rule

When surface fails, do not first add more instruments. First rewrite:

- note lengths,
- envelopes,
- overlaps,
- phrase handoffs,
- voice leading,
- dynamic arcs,
- room/tail placement.

Only add instruments after the surface behavior works with two or three layers.
