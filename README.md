# Codex Game Music Skill

A Codex skill for composing editable game BGM as multi-track MIDI.

Ask in natural language. Codex translates game-scene prompts like `desert field`, `snowfield`, `tropical coast`, `town`, `dungeon`, or `boss battle` into composition briefs, loop plans, and playable `.mid` files for Midiano, MuseScore, LMMS, DAWs, and game-audio pipelines.

This is an experimental v0.1 release focused on MIDI-first game music prototyping.

## Demo

Add the demo video here after uploading it to GitHub releases, GitHub user attachments, YouTube, or X.

```md
https://github.com/user-attachments/assets/your-demo-video-id
```

The v0.1 demo was generated from three short Japanese prompts:

| Prompt | MIDI | Scene | Notes |
| --- | --- | --- | --- |
| `砂漠` | `examples/midi/mirage_caravan_short.mid` | Mirage Caravan | Desert field loop with a reed-like motif, 3+3+2 walking pulse, warm pedal bass, and sparse heat shimmer. |
| `雪国` | `examples/midi/white_horizon_snowfield.mid` | White Horizon Snowfield | Snowfield loop with a wide bell motif, distant strings, slow bass, and cold open space. |
| `南国` | `examples/midi/palm_lantern_coast_tropical.mid` | Palm Lantern Coast | Tropical coast loop with flute lead, marimba motion, offbeat guitar, island percussion, and warm bass. |

## What Makes It Different

This is not just a folder of prompts.

`compose-game-music` is a Codex-first music workflow. The agent translates a game scene into musical jobs, chooses a deliverable format, designs motif/form/bass/harmony/layers, and can produce editable MIDI-oriented handoff data.

- **MIDI-first**: outputs are editable, inspectable, remixable, and DAW-friendly.
- **Game-scene aware**: prompts are treated as gameplay situations, not only moods.
- **Loop-oriented**: the skill considers phrase form, loop return, SFX space, and fatigue.
- **Adaptive-ready**: designs can be split into base, bass, harmony, lead, danger, reward, and texture layers.
- **Codex-native**: built as a reusable agent skill with references, output contracts, and implementation guidance.
- **Honest about sound sources**: oscillator sketches, MIDI, SoundFonts, rendered loops, and stems are kept distinct.

## Showcase

### Desert Field: Mirage Caravan

Prompt:

```text
砂漠
```

Output:

- Multi-track MIDI
- Reed-like lead motif
- 3+3+2 walking pulse
- Warm low pedal
- Sparse heat shimmer

Suggested use:

- desert overworld
- caravan travel
- ruins approach
- game jam field loop

### Snowfield: White Horizon Snowfield

Prompt:

```text
雪国
```

Output:

- Multi-track MIDI
- Wide bell motif
- Distant string plane
- Slow bass support
- Sparse high shimmer

Suggested use:

- frozen country
- quiet open field
- snow village outskirts
- low-threat exploration

### Tropical Coast: Palm Lantern Coast

Prompt:

```text
南国
```

Output:

- Multi-track MIDI
- Flute-like lead
- Marimba motion
- Offbeat nylon guitar
- Island percussion

Suggested use:

- tropical coast
- beach town approach
- island exploration
- light adventure field loop

## How It Works

1. The user asks Codex for game music in natural language.
2. The skill infers scene role, player motion, emotional function, loop fatigue target, and delivery format.
3. Codex designs a motif, phrase form, bass role, harmonic behavior, texture, and adaptive layers.
4. The output is kept editable: MIDI-like note data, `.mid`, stem plans, or engine handoff notes.
5. For higher-quality production, the MIDI can be loaded into a DAW or SoundFont renderer and exported as `.wav` or `.ogg`.

The skill is the music-direction and composition workflow. MIDI files remain editable so humans can change notes, sound sources, mix, and arrangement.

## What It Can Generate

- Exploration BGM
- Town, shop, menu, victory, failure, and title cues
- Dungeon, horror, chase, battle, boss, and final-battle plans
- MIDI-like JSON and standard `.mid` handoff
- Web Audio or Tone.js implementation guidance
- Unity/Godot loop and stem integration plans
- Gameplay SFX direction for UI, tools, impacts, warnings, victory, and failure

## Install

### Windows PowerShell

```powershell
git clone https://github.com/sora16bit/codex-game-music-skill.git
cd .\codex-game-music-skill
New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\.codex\skills" | Out-Null
Copy-Item -Recurse -Force ".\skills\*" "$env:USERPROFILE\.codex\skills\"
```

Start a new Codex session after installation.

### macOS / Linux

```bash
git clone https://github.com/sora16bit/codex-game-music-skill.git
cd ./codex-game-music-skill
mkdir -p ~/.codex/skills
cp -R ./skills/* ~/.codex/skills/
```

Start a new Codex session after installation.

## Suggested Prompts

```text
Use $compose-game-music to create desert field music as editable MIDI.
```

```text
Use $compose-game-music to make snowfield exploration BGM for a quiet RPG area.
```

```text
Use $compose-game-music to create tropical coast music for a game jam prototype.
```

```text
Use $compose-game-music to make boss battle music, but avoid default snare/backbeat tension.
```

```text
Use $compose-game-music to critique why this Web Audio battle music feels thin.
```

## Repository Layout

```text
codex-game-music-skill/
  README.md
  LICENSE
  skills/
    compose-game-music/
      SKILL.md
      agents/
        openai.yaml
      references/
        battle-music-design.md
        composition-design-gates.md
        composition-theory-core.md
        deliverable-formats.md
        game-score-study-patterns.md
        industry-concepts.md
        instrumentation-and-texture.md
        musical-surface.md
        output-contracts.md
        review-checklist.md
        scene-recipes.md
        scene-recognition-and-failures.md
        score-study-workflow.md
        sfx-recipes.md
        web-audio-patterns.md
  examples/
    midi/
      mirage_caravan_short.mid
      white_horizon_snowfield.mid
      palm_lantern_coast_tropical.mid
    prompts.md
    listening-notes.md
```

## Example MIDI Files

Open these in Midiano, MuseScore, LMMS, GarageBand, Logic, FL Studio, Ableton, Cubase, Reaper, or any DAW that can import Standard MIDI files.

```text
examples/midi/mirage_caravan_short.mid
examples/midi/white_horizon_snowfield.mid
examples/midi/palm_lantern_coast_tropical.mid
```

MIDI playback quality depends on the sound source. For better output, load the `.mid` into a DAW or SoundFont player, assign better instruments, then render to `.wav` or `.ogg`.

## Roadmap

- **v0.1**: Codex skill, output contracts, and example MIDI demos.
- **v0.2**: bundled MIDI generation scripts and more scene presets.
- **v0.3**: Godot, Unity, and browser-game handoff templates.
- **v0.4**: SoundFont rendering path and rendered-loop examples.
- **v1.0**: plugin package with installable marketplace metadata.

## Status

Experimental.

This project is designed for game jams, prototypes, composition sketches, and editable MIDI handoff. It is not a replacement for a composer, DAW, orchestration, mixing, mastering, or licensed sound libraries.

## Author

Created by [sora16bit](https://github.com/sora16bit).

## License

MIT
