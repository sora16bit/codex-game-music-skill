# Codex Game Music Skill

Languages: [English](README.md) | 日本語

Codexで、ゲームBGMを編集可能なマルチトラックMIDIとして作るためのSkillです。

自然言語で依頼すると、Codexが `desert field`、`snowfield`、`tropical coast`、`active battle`、`volcano final boss`、`town`、`dungeon` のようなゲーム場面を、作曲ブリーフ、ループ設計、再生可能な `.mid` ファイルへ落とし込みます。出力したMIDIは Midiano、MuseScore、LMMS、DAW、ゲーム制作パイプラインで扱えます。

v0.1 は実験版です。現時点で公開デモとして確認している主な強みは、フィールド/探索BGMのMIDIプロトタイプです。加えて、通常戦闘とラストボス戦の初期テストも追加しています。

## Output Format

このSkillが出すのは、完成済みのマスタリング音源ではなく、作曲方針と編集可能な音楽データです。

- **主な出力**: 複数トラックの Standard MIDI (`.mid`)
- **対応できるもの**: MIDI風JSON、ループ設計、ステム設計、Web Audio/Tone.js方針、ゲームエンジン向け受け渡しメモ
- **まだ同梱していないもの**: `.wav` / `.ogg` のレンダリング音源、SoundFontミックス、DAWプロジェクト、マスタリング済み音源
- **おすすめの再生方法**: `.mid` を [Midiano](https://app.midiano.com/)、MuseScore、LMMS、GarageBand、Logic、FL Studio、Ableton、Cubase、Reaper などで開く

デモ動画は Midiano でMIDIを再生して録画したものです。ここでの Midiano は再生・可視化ツールであり、MIDI生成自体は同梱PythonスクリプトとCodex Skillワークフローで行っています。

## Demo

最初の v0.1 フィールドデモは、短い日本語プロンプト3つから生成しました。各出力は編集可能なマルチトラックMIDIで、Midianoで再生しています。戦闘とラストボスのMIDIテストも、フィールドBGM以外の初期サンプルとして下に載せています。

### Desert Field: Mirage Caravan

https://github.com/user-attachments/assets/4684707e-872c-4910-bd1f-950ac8bac3b2

### Snowfield: White Horizon Snowfield

https://github.com/user-attachments/assets/3f21145a-561a-4501-afcd-d1fe7f8d4ef8

### Tropical Coast: Palm Lantern Coast

https://github.com/user-attachments/assets/9b613e45-158d-4228-b184-94aed9c2b2b0

| Prompt | MIDI | Scene | Notes |
| --- | --- | --- | --- |
| `Create desert field music as editable MIDI.` | `examples/midi/mirage_caravan_short.mid` | Mirage Caravan | 砂漠フィールド。reed風メロディ、3+3+2の歩行パルス、低音ペダル、控えめな熱気の装飾。 |
| `Create snowfield exploration music as editable MIDI.` | `examples/midi/white_horizon_snowfield.mid` | White Horizon Snowfield | 雪原探索。広いベル風モチーフ、遠いストリングス、遅い低音、冷たい空間。 |
| `Create tropical coast music as editable MIDI.` | `examples/midi/palm_lantern_coast_tropical.mid` | Palm Lantern Coast | 南国海岸。フルート風リード、マリンバ、裏拍ギター、島っぽいパーカッション。 |

元の短い日本語プロンプト:

```text
砂漠 / 雪国 / 南国
```

### Experimental Battle Test

これは、SkillがフィールドBGM以外にも進めるかを見るための初期テストです。戦闘BGMワークフローの完成証明ではなく、検証用サンプルとして扱ってください。

| Prompt | MIDI | Scene | Notes |
| --- | --- | --- | --- |
| `Create active battle music as editable MIDI, without relying on default snare/backbeat tension.` | `examples/midi/iron_vow_skirmish_battle.mid` | Iron Vow Skirmish | brass風モチーフ衝突、歪んだ低音エンジン、ストリングススタブ、高域の脅威カウンター、タム中心の圧力。 |

### Final Boss Battle Test

火山の魔王ラストボス戦という、より具体的で緊張感の高いシーンのテストです。

| Prompt | MIDI | Scene | Notes |
| --- | --- | --- | --- |
| `Create editable MIDI for a final boss battle against the Demon King inside a volcano.` | `examples/midi/volcanic_demon_king_final_boss.mid` | Volcanic Demon King | 32小節のラストボスループ。魔王brass風モチーフ、lava bass、doom choir、火山string stabs、高域heat threat、儀式的な低音impact。 |

## What Makes It Different

これは単なるプロンプト集ではありません。

`compose-game-music` は Codex-first の音楽制作ワークフローです。ゲーム場面を、プレイヤーの移動、場所の印象、戦闘状況、ループ疲労、モチーフ、低音、和声、レイヤー構成、MIDI出力へ変換します。

- **MIDI-first**: 編集、確認、再アレンジ、DAW連携がしやすい。
- **Game-scene aware**: 雰囲気だけでなく、場所、戦闘状況、プレイヤーの行動を扱う。
- **Loop-oriented**: フレーズ、ループ復帰、SFXの余白、疲労しにくさを考慮する。
- **Codex-native**: CodexのSkillとして、参照資料、出力契約、実装ガイドを含む。
- **Code included**: 外部パッケージなしでデモMIDIを生成するPythonスクリプトを同梱。
- **Honest output**: MIDI、SoundFont、Web Audio、レンダリング済み音源を混同しない。

GitHubのdescription、topics、公開時の投稿文、見せ方の方針は [docs/promotion.md](docs/promotion.md) にまとめています。

## 現時点の強みと制限

v0.1で強く見せられるのは、フィールド/探索BGMのMIDIプロトタイプです。通常戦闘とラストボス戦の初期テストも追加しています。

ダンジョン、街、アダプティブミュージック、SFX設計のワークフローはSkill内にあります。ただし、公開デモとして特に検証できているのは `砂漠 / 雪国 / 南国`、そして戦闘/ラストボステストです。

## Install

### Windows PowerShell

```powershell
git clone https://github.com/sora16bit/codex-game-music-skill.git
cd .\codex-game-music-skill
New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\.codex\skills" | Out-Null
Copy-Item -Recurse -Force ".\skills\*" "$env:USERPROFILE\.codex\skills\"
```

インストール後、新しいCodexセッションを開始してください。

### macOS / Linux

```bash
git clone https://github.com/sora16bit/codex-game-music-skill.git
cd ./codex-game-music-skill
mkdir -p ~/.codex/skills
cp -R ./skills/* ~/.codex/skills/
```

インストール後、新しいCodexセッションを開始してください。

## Suggested Prompts

```text
Use $compose-game-music to create editable MIDI for 砂漠 / desert field exploration.
```

```text
Use $compose-game-music to create editable MIDI for 雪国 / quiet snowfield exploration.
```

```text
Use $compose-game-music to create editable MIDI for 南国 / bright tropical coast exploration.
```

```text
Use $compose-game-music to create editable MIDI for 火山の魔王ラスボス戦 / a final boss battle against the Demon King inside a volcano.
```

```text
Use $compose-game-music to make boss battle music, but avoid default snare/backbeat tension.
```

```text
Use $compose-game-music to critique why this Web Audio battle music feels thin.
```

## Roadmap

- **v0.1**: Skill本体、出力契約、フィールド/探索MIDIデモ、通常戦闘テスト、ラストボステスト。
- **v0.2**: MIDI生成スクリプトとシーンプリセットの強化。
- **v0.3**: ダンジョン、街、メニュー、勝利、敗北、アダプティブMIDI例。
- **v0.4**: Godot / Unity / ブラウザゲーム向けの受け渡し。
- **v0.5**: SoundFontレンダリングと音源例。
- **v1.0**: Codex plugin化。

## License

MIT
