# Scene Recognition And Failures

Use this when the cue may sound like a generic mood rather than a specific game scene. The goal is that a listener can infer place, action, and game function without seeing the filename.

## Recognition Contract

Every BGM cue must provide evidence for:

- Place: where the player is.
- Action: what the player is doing.
- Stakes: safe, curious, threatened, triumphant, lost, hunted, or pressured.
- Scale: intimate, room-sized, field-sized, vast, cosmic, claustrophobic.
- Game function: explore, fight, flee, solve, rest, shop, menu, cutscene, transition.

A cue that only says "spooky", "hot", "cold", "pretty", "sad", or "epic" is under-specified.

## Blind Listening Test

Before presenting a cue, run this test:

1. Hide the title and prompt.
2. Write the top 3 likely scene guesses.
3. List the audible evidence for the intended scene.
4. List the strongest wrong interpretation.
5. Change the design if the intended scene is not the strongest guess.

Score 0-3:

- 0: abstract mood only.
- 1: broad emotion is clear, scene is not.
- 2: scene family is clear but specific place/action is ambiguous.
- 3: place, action, and game function are strongly implied.

Do not deliver a production-facing cue with a recognition score below 2.

## Evidence Types

Use several evidence types, not one token sound:

- Rhythm evidence: walking, ritual, chase, hesitation, battle collision, sailing sway, machinery, dance, or stillness.
- Register evidence: vast low pressure, intimate midrange, fragile high points, distant calls, close foreground.
- Harmonic evidence: modal travel, unresolved haunted suspension, heroic cadence, infernal chromatic pressure, frozen open fifths.
- Timbre evidence: wood, stone, metal, glass, organ-like, choir-like, reed-like, pluck-like, water-like, machinery-like.
- Surface evidence: room tail, outdoor openness, tight dry action, underwater blur, snow hush without static, heat pressure without hiss.
- Motif evidence: hero, place, threat, memory, machine, ritual, monster, settlement, loss.
- Event evidence: doors, floorboards, waves, impacts, bells, machinery, but only when integrated musically.

## Common Failure Patterns

### Generic Mood

- Symptom: listener hears "mysterious" or "tense" but no place.
- Fix: add place-specific rhythm, register, surface, and motif evidence.

### Token Instrument

- Symptom: one instrument or effect is expected to carry the whole concept.
- Fix: make rhythm, harmony, and phrase behavior also express the scene.

### Same Under The Hood

- Symptom: several cues share the same pulse, noise bed, chord pace, and note density with different patches.
- Fix: change meter/pulse grammar, harmonic plan, phrase form, and surface behavior before changing timbre.

### Abstract Horror

- Symptom: haunted mansion, cave, cursed forest, dungeon, and title screen all sound interchangeable.
- Fix: decide whether the cue is indoor or outdoor, moving or waiting, ancient or domestic, safe exploration or active threat.

### Location Without Gameplay

- Symptom: place is clear, but it feels like a still image rather than game music.
- Fix: add player motion, loop form, state changes, pickups, or a low/mid rhythmic surface.

### Sound Design Instead Of Composition

- Symptom: the cue is identifiable only by sound effects, noise, reverb, impacts, or novelty timbre.
- Fix: write motif, bass function, harmonic plan, and phrase form with simple tones first.

## Contrast Cards

### Forest Shrine vs Forest Abandoned Mansion

- Forest shrine: sacred suspension, gentle ritual pulse, brighter upper partials, less domestic wood, more stillness and reverence.
- Forest abandoned mansion: room-sized resonance, old wood/floor events, broken domestic motif, hesitant rhythm, indoor/outdoor boundary.

### Abandoned Mansion vs Cave

- Abandoned mansion: wood, glass, old melody, room tail, floorboard rhythm, human past.
- Cave: stone resonance, dripping or low hollow space, less tonal memory, more geological echo.

### Abandoned Mansion vs Demon Castle

- Abandoned mansion: intimate, decayed domesticity, fragile memory, uncertain safety.
- Demon castle: scale, authority, organ/choir/low brass-like pressure, antagonist identity, ritual or military gravity.

### Hellfire Field vs Hot Desert Field

- Hellfire field: oppressive low pressure, distorted gravity, chromatic/infernal cells, geological impacts, survival.
- Hot desert field: travel groove, heat shimmer, open horizon, pluck/reed motion, lighter percussion.

### Snowfield vs Sad Piano Scene

- Snowfield: horizon scale, open fifths, cold register spacing, slow travel, sparse warmth.
- Sad piano scene: intimate foreground, human phrasing, closer room, clearer emotional cadence.

## Delivery Rule

When a prompt names a specific scene, include in the brief:

- Intended blind-listening guess.
- Top 4 audible evidence items.
- Top 2 wrong-scene risks.
- One design choice that prevents each wrong-scene risk.
