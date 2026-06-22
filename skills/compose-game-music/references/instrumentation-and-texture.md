# Instrumentation And Texture

Use this when the music feels like isolated points instead of a continuous musical surface. Do not solve texture by adding random notes. Build roles, performance techniques, and phrase connections.

## Honesty About Sound Sources

Do not overclaim instrumentation. If the implementation uses raw oscillators, filtered noise, or simple procedural synthesis, describe the result as an approximation:

- "string-like tremolo plane", not "strings"
- "choir-like sustained pad", not "choir"
- "organ-like additive tone", not "pipe organ"
- "fiddle-like counterline", not "fiddle performance"

Use real instrument names without qualification only when the deliverable uses actual samples, SoundFonts, MIDI instruments with credible patches, recorded assets, or a renderer/synth designed for that instrument family.

If the user asks for realistic ensemble quality, prefer MIDI + SoundFont/synth, rendered stems, or external audio assets over oscillator-only generation.

## Point, Line, Plane

- Point: isolated hit, pluck, stab, short note, UI-like event.
- Line: melody, bass line, counterline, ostinato, arpeggio.
- Plane: sustained harmony, tremolo bed, choir vowel, drone with motion, string divisi, organ registration, layered rhythm field.

Good game music usually uses all three. A cue made only of points feels like scattered events. A cue made only of planes feels ambient. A cue made only of lines can feel thin or MIDI-like.

Do not reduce "plane" to a long pad or extra layer count. A musical surface is also created by note lengths, articulation, overlap, release tails, voice leading, dynamics, register balance, panning, room sound, and how one phrase hands motion to the next. A cue can contain many layers and still feel pointillistic if every part attacks and releases in the same detached way.

## Ensemble Roles

Assign every layer a role:

- Primary theme: the thing the listener can remember.
- Counterline: argues with or supports the theme.
- Harmonic plane: gives emotional world and continuity.
- Rhythmic plane: gives motion without necessarily being drums.
- Bass foundation: defines weight and harmonic gravity.
- Threat identity: antagonist color, interval, register, rhythm, or timbre.
- Impact layer: meaningful events, not constant filler.
- Air/noise layer: space and pressure, always subordinate.

If a layer has no role, remove it or merge it with another role.

Noise is not a free ambience layer. Before adding wind, hiss, ash, breath, static, or filtered white noise, define its concrete source and time behavior. If the source is vague, use pitch, resonance, reverb tail, low movement, or silence instead.

## Performance Techniques

Specify how an instrument plays, not just its name.

### Strings

- Tremolo: continuous threat, panic, supernatural pressure.
- Spiccato / short bow: active motion, but avoid constant chugging.
- Marcato: decisive attacks, battle statements.
- Sustained divisi: harmonic plane and scale.
- Glissando / slide: horror, collapse, monster movement.
- Pizzicato: stealth, pluck motion, light fantasy.

### Fiddle

- Reel-like bowing: forward drive.
- Double stops: raw folk aggression.
- Grace notes/cuts: Celtic articulation.
- Drones/open-string support: cultural grounding.
- Counter-melody: answer the pipe/whistle; do not only double it.

### Pipes / Whistle / Reed Lead

- Grace-note attacks and cuts: phrase identity.
- Sustained high note: alarm or heroic pressure.
- Quick neighbor turns: Celtic motion.
- Call phrases: good for hero/world identity.
- Avoid endless detached beeps; connect notes with phrase logic.

### Brass / Horns

- Marcato calls: phase changes, final battle scale.
- Sustained low horns: doom and gravity.
- Rising swells: escalation.
- Short answer phrases: antagonist or army response.
- Avoid generic epic blasts without motif.

### Choir

- Sustained vowel plane: mythic stakes.
- Rhythmic syllable-like pulses: ritual pressure.
- Antiphonal response: world vs demon, hero vs fate.
- Avoid constant ahh pad if the cue must be active.

### Pipe Organ

- Pedal: villain gravity, doom.
- Full chord stab: phase impact.
- Inner moving line: intelligent antagonist pressure.
- High reed stop-like line: demonic alarm.
- Avoid long organ drone as the main final-battle material; it reads as castle ambience.

### Harp / Dulcimer / Pluck

- Broken-chord shimmer: fantasy color.
- Fast repeated figure: nervous motion.
- Cadential flourish: phrase glue.
- Avoid making it too pretty during high-stakes combat unless contrasted by threat.

### Percussion / Impacts

- Low frame drum/body hit: cultural pulse.
- Timpani-like roll: approach to phase hit.
- Metallic hit: ritual, magic, boss attack.
- Hand percussion: folk motion.
- Silence before impact: increases force.
- Avoid using percussion as the only source of motion.

## Building A Musical Surface

Use these combinations:

### Active Final Battle Surface

- Foreground: short heroic theme in pipe/whistle or brass.
- Counterline: fiddle or high strings answering every 1-2 bars.
- Plane: string tremolo or choir rhythm, not long static pad.
- Bass: moving pedal with modal/chromatic pressure.
- Threat: organ inner line or low brass interruption.
- Impacts: sparse but decisive phase hits.

### Celtic High-Stakes Surface

- Pipe/whistle carries theme with grace-note attacks.
- Fiddle answers with double-stop-like or reel-like fragments.
- Low strings carry 6/8 or 12/8 motion.
- Frame drum/bodhran is optional; bass/pluck can carry pulse.
- Organ appears as corruption or final-boss color, not general ambience.
- Harp/dulcimer glues phrase endings, not constant sparkle.

### Dense But Readable Surface

- Keep one clear foreground motif.
- Put motion in mid or low register while theme occupies high register.
- Use sustained plane underneath, but modulate it with phrase changes.
- Let impacts mark form, not every beat.
- Use register separation so density does not become mud.

## Phrase Connection

Avoid isolated note events by connecting phrases:

- Use pickup notes into the next bar.
- Let a held note overlap into the answer phrase.
- Use a counterline that begins before the main phrase ends.
- Change harmony under a sustained note.
- Repeat the motif in another register before it disappears.
- Use call-response within 1-2 bars.
- For harmony instruments, avoid all voices attacking and releasing together every bar. Hold common tones, let one voice resolve late, keep pedal notes through changes, or roll/break chords so the harmony has a body instead of a switch-like on/off shape.

## Diagnostics

### "Pointillistic / Dots Not Music"

- Likely causes: too many isolated short notes, no sustained plane, no counterline, no legato/pickup/overlap, no role continuity.
- Fixes: add a harmonic or tremolo plane, connect phrases with pickups/holds, vary articulation and note length, design release tails, assign counterline and bass roles, reduce random impacts, and write performance techniques for each instrument.

### "Chord Blocks / Not Connected"

- Likely causes: harmony is entered as simultaneous chord events, all voices share the same start/end points, no sustain pedal behavior, no common tones, no suspensions, no delayed releases, and melody does not breathe over the harmony.
- Fixes: rewrite durations before changing sounds. Hold one or two notes across the chord change, move an inner voice while the top note sustains, add a bass pickup into the next harmony, delay one resolution, and let tails overlap the next phrase.

### "Same Instrument Wearing Different Hats"

- Likely causes: all instruments use the same synth envelope, register, articulation, and role.
- Fixes: differentiate attack, sustain, vibrato, brightness, register, phrase length, and role. Use fewer instruments with clearer technique.

### "Dense But Still Weak"

- Likely causes: density is all points; no plane, no hierarchy, no bass/harmony argument.
- Fixes: create one foreground theme, one motion layer, one harmonic plane, and one threat layer. Mute everything else.

### "Ambient Instead Of Battle"

- Likely causes: planes are static and foreground is too sparse.
- Fixes: keep plane moving through tremolo, harmonic rhythm, register shifts, rhythmic choir, or inner organ line.

## Revision Protocol

When texture fails:

1. Name the missing dimension: point, line, or plane.
2. Pick 4-6 ensemble roles before adding notes.
3. Define a performance technique for each role.
4. Write the plane first if the cue feels like dots.
5. Write the theme and counterline next.
6. Add impacts last.
7. Check by muting impacts; the music should still flow.
8. Check by muting the plane; the cue should still have theme and motion.
