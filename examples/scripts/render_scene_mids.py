import struct
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MIDI_DIR = ROOT / "midi"
TPQ = 480


NOTE_OFFSETS = {
    "C": -9, "C#": -8, "Db": -8, "D": -7, "D#": -6, "Eb": -6,
    "E": -5, "F": -4, "F#": -3, "Gb": -3, "G": -2, "G#": -1,
    "Ab": -1, "A": 0, "A#": 1, "Bb": 1, "B": 2,
}


def note_number(note):
    if len(note) >= 2 and note[1] in "#b":
        name = note[:2]
        octave = int(note[2:])
    else:
        name = note[0]
        octave = int(note[1:])
    return 69 + NOTE_OFFSETS[name] + (octave - 4) * 12


def vlq(n):
    out = [n & 0x7F]
    n >>= 7
    while n:
        out.append((n & 0x7F) | 0x80)
        n >>= 7
    return bytes(reversed(out))


def ev(delta, data):
    return vlq(delta) + bytes(data)


def meta(delta, typ, payload):
    return vlq(delta) + bytes([0xFF, typ]) + vlq(len(payload)) + payload


def chunk(events):
    body = b"".join(events) + meta(0, 0x2F, b"")
    return b"MTrk" + struct.pack(">I", len(body)) + body


def tick(bar, beat):
    return int(round(((bar - 1) * 4 + (beat - 1)) * TPQ))


def note_points(channel, notes):
    points = []
    for n in notes:
        start = tick(n["bar"], n["beat"])
        dur = int(round(n["dur"] * TPQ))
        pitch = note_number(n["note"])
        vel = max(1, min(127, int(round(n.get("vel", 0.72) * 112))))
        points.append((start, 0, [0x90 | channel, pitch, vel]))
        points.append((start + dur, 1, [0x80 | channel, pitch, 0]))
    points.sort(key=lambda p: (p[0], p[1]))
    out = []
    last = 0
    for when, _, data in points:
        out.append(ev(when - last, data))
        last = when
    return out


def music_track(name, channel, program, notes, volume=96, pan=64, reverb=48, chorus=12):
    events = [meta(0, 0x03, name.encode("ascii"))]
    events.append(ev(0, [0xB0 | channel, 7, volume]))
    events.append(ev(0, [0xB0 | channel, 10, pan]))
    events.append(ev(0, [0xB0 | channel, 91, reverb]))
    events.append(ev(0, [0xB0 | channel, 93, chorus]))
    events.append(ev(0, [0xC0 | channel, program]))
    events.extend(note_points(channel, notes))
    return chunk(events)


def percussion_track(name, hits, volume=96, reverb=28):
    points = []
    for h in hits:
        start = tick(h["bar"], h["beat"])
        dur = int(round(h.get("dur", 0.18) * TPQ))
        points.append((start, 0, [0x99, h["pitch"], h["vel"]]))
        points.append((start + dur, 1, [0x89, h["pitch"], 0]))
    points.sort(key=lambda p: (p[0], p[1]))
    events = [meta(0, 0x03, name.encode("ascii"))]
    events.append(ev(0, [0xB9, 7, volume]))
    events.append(ev(0, [0xB9, 91, reverb]))
    last = 0
    for when, _, data in points:
        events.append(ev(when - last, data))
        last = when
    return chunk(events)


def conductor(title, bpm, note):
    tempo = int(round(60_000_000 / bpm))
    return chunk([
        meta(0, 0x03, f"{title} - Conductor".encode("ascii")),
        meta(0, 0x01, note.encode("ascii")),
        meta(0, 0x58, bytes([4, 2, 24, 8])),
        meta(0, 0x51, tempo.to_bytes(3, "big")),
    ])


def write_midi(path, tracks):
    header = b"MThd" + struct.pack(">IHHH", 6, 1, len(tracks), TPQ)
    path.write_bytes(header + b"".join(tracks))


def arp(pattern, bars, dur=0.5, vel=0.5):
    notes = []
    for bar in bars:
        for i, note in enumerate(pattern[(bar - 1) % len(pattern)]):
            notes.append({"bar": bar, "beat": 1 + i * dur, "dur": dur * 0.82, "note": note, "vel": vel})
    return notes


def make_snowfield():
    title = "White Horizon Snowfield"
    bpm = 76

    lead = [
        {"bar": 1, "beat": 1.0, "dur": 1.5, "note": "D5", "vel": 0.62},
        {"bar": 1, "beat": 3.0, "dur": 1.0, "note": "A5", "vel": 0.55},
        {"bar": 2, "beat": 1.5, "dur": 1.0, "note": "G#5", "vel": 0.50},
        {"bar": 2, "beat": 3.0, "dur": 1.5, "note": "E5", "vel": 0.56},
        {"bar": 5, "beat": 1.0, "dur": 1.5, "note": "F#5", "vel": 0.58},
        {"bar": 5, "beat": 3.0, "dur": 1.0, "note": "A5", "vel": 0.52},
        {"bar": 6, "beat": 1.5, "dur": 1.0, "note": "B5", "vel": 0.50},
        {"bar": 6, "beat": 3.0, "dur": 1.5, "note": "A5", "vel": 0.55},
        {"bar": 9, "beat": 1.0, "dur": 1.0, "note": "E5", "vel": 0.54},
        {"bar": 9, "beat": 2.5, "dur": 1.0, "note": "F#5", "vel": 0.52},
        {"bar": 10, "beat": 1.0, "dur": 2.5, "note": "D5", "vel": 0.56},
        {"bar": 13, "beat": 1.0, "dur": 1.5, "note": "A5", "vel": 0.57},
        {"bar": 13, "beat": 3.0, "dur": 1.0, "note": "G#5", "vel": 0.50},
        {"bar": 14, "beat": 1.0, "dur": 1.0, "note": "F#5", "vel": 0.50},
        {"bar": 14, "beat": 3.0, "dur": 1.5, "note": "E5", "vel": 0.52},
        {"bar": 16, "beat": 3.0, "dur": 1.0, "note": "C#5", "vel": 0.45},
    ]

    bass = []
    bass_roots = ["D2", "D2", "A1", "A1", "B1", "B1", "G2", "A1",
                  "D2", "D2", "F#2", "F#2", "G2", "A1", "D2", "A1"]
    for bar, root in enumerate(bass_roots, start=1):
        bass.append({"bar": bar, "beat": 1.0, "dur": 3.7, "note": root, "vel": 0.48})

    strings = []
    chords = [
        ("D3", "A3", "E4"), ("D3", "A3", "F#4"), ("A2", "E3", "G#3"), ("A2", "E3", "C#4"),
        ("B2", "F#3", "A3"), ("B2", "F#3", "D4"), ("G2", "D3", "A3"), ("A2", "E3", "C#4"),
        ("D3", "A3", "E4"), ("D3", "A3", "F#4"), ("F#2", "C#3", "A3"), ("F#2", "C#3", "E4"),
        ("G2", "D3", "B3"), ("A2", "E3", "C#4"), ("D3", "A3", "F#4"), ("A2", "E3", "G#3"),
    ]
    for bar, chord in enumerate(chords, start=1):
        for note in chord:
            strings.append({"bar": bar, "beat": 1.0, "dur": 3.85, "note": note, "vel": 0.38})

    harp = arp([
        ["D4", "A4", "E5", "A4", "D5", "A4", "E5", "A4"],
        ["D4", "A4", "F#5", "A4", "E5", "A4", "F#5", "A4"],
        ["A3", "E4", "G#4", "E4", "C#5", "E4", "G#4", "E4"],
        ["A3", "E4", "C#5", "E4", "B4", "E4", "G#4", "E4"],
    ], range(1, 17), dur=0.5, vel=0.34)

    shimmer = [
        {"bar": 2, "beat": 4.0, "dur": 1.5, "note": "A6", "vel": 0.34},
        {"bar": 4, "beat": 3.5, "dur": 1.5, "note": "E6", "vel": 0.28},
        {"bar": 8, "beat": 4.0, "dur": 1.0, "note": "C#6", "vel": 0.30},
        {"bar": 12, "beat": 4.0, "dur": 1.5, "note": "F#6", "vel": 0.32},
        {"bar": 15, "beat": 3.0, "dur": 1.5, "note": "A6", "vel": 0.30},
    ]

    hits = []
    for bar in [1, 5, 9, 13]:
        hits.append({"bar": bar, "beat": 1.0, "pitch": 49, "vel": 38, "dur": 1.0})  # crash as soft wind swell
    for bar in [4, 8, 12, 16]:
        hits.append({"bar": bar, "beat": 4.0, "pitch": 84, "vel": 34, "dur": 0.5})  # bell tree

    tracks = [
        conductor(title, bpm, "Snowfield loop, D Lydian color, wide motif and open fifths."),
        music_track("Fragile Bell Motif", 0, 10, lead, volume=82, pan=72, reverb=72, chorus=18),
        music_track("Warm Low Snow Bass", 1, 43, bass, volume=75, pan=52, reverb=48, chorus=10),
        music_track("Distant String Plane", 2, 48, strings, volume=76, pan=64, reverb=78, chorus=20),
        music_track("Soft Harp Crystals", 3, 46, harp, volume=58, pan=44, reverb=66, chorus=16),
        music_track("Sparse High Shimmer", 4, 14, shimmer, volume=50, pan=82, reverb=84, chorus=24),
        percussion_track("Snow Air Events", hits, volume=60, reverb=82),
    ]
    MIDI_DIR.mkdir(parents=True, exist_ok=True)
    write_midi(MIDI_DIR / "white_horizon_snowfield.mid", tracks)


def make_tropical():
    title = "Palm Lantern Coast"
    bpm = 112

    lead = [
        {"bar": 1, "beat": 1.0, "dur": 0.5, "note": "B4", "vel": 0.72},
        {"bar": 1, "beat": 1.5, "dur": 0.5, "note": "D5", "vel": 0.76},
        {"bar": 1, "beat": 2.0, "dur": 0.75, "note": "E5", "vel": 0.74},
        {"bar": 1, "beat": 3.0, "dur": 0.5, "note": "D5", "vel": 0.68},
        {"bar": 1, "beat": 3.5, "dur": 0.5, "note": "B4", "vel": 0.66},
        {"bar": 2, "beat": 1.0, "dur": 0.75, "note": "A4", "vel": 0.68},
        {"bar": 2, "beat": 2.0, "dur": 0.5, "note": "G4", "vel": 0.66},
        {"bar": 2, "beat": 2.5, "dur": 0.5, "note": "A4", "vel": 0.68},
        {"bar": 2, "beat": 3.5, "dur": 1.0, "note": "D5", "vel": 0.72},
        {"bar": 5, "beat": 1.0, "dur": 0.5, "note": "E5", "vel": 0.76},
        {"bar": 5, "beat": 1.5, "dur": 0.5, "note": "G5", "vel": 0.78},
        {"bar": 5, "beat": 2.0, "dur": 0.75, "note": "A5", "vel": 0.76},
        {"bar": 5, "beat": 3.0, "dur": 0.5, "note": "G5", "vel": 0.70},
        {"bar": 5, "beat": 3.5, "dur": 0.5, "note": "E5", "vel": 0.68},
        {"bar": 6, "beat": 1.0, "dur": 0.75, "note": "D5", "vel": 0.72},
        {"bar": 6, "beat": 2.0, "dur": 0.5, "note": "B4", "vel": 0.68},
        {"bar": 6, "beat": 2.5, "dur": 0.5, "note": "D5", "vel": 0.70},
        {"bar": 6, "beat": 3.5, "dur": 1.0, "note": "G5", "vel": 0.76},
        {"bar": 9, "beat": 1.0, "dur": 0.5, "note": "D5", "vel": 0.70},
        {"bar": 9, "beat": 1.5, "dur": 0.5, "note": "E5", "vel": 0.72},
        {"bar": 9, "beat": 2.5, "dur": 0.5, "note": "G5", "vel": 0.76},
        {"bar": 9, "beat": 3.0, "dur": 0.5, "note": "E5", "vel": 0.70},
        {"bar": 10, "beat": 1.0, "dur": 0.75, "note": "D5", "vel": 0.68},
        {"bar": 10, "beat": 2.0, "dur": 0.75, "note": "B4", "vel": 0.66},
        {"bar": 10, "beat": 3.0, "dur": 1.0, "note": "A4", "vel": 0.65},
        {"bar": 13, "beat": 1.0, "dur": 0.5, "note": "B4", "vel": 0.72},
        {"bar": 13, "beat": 1.5, "dur": 0.5, "note": "D5", "vel": 0.75},
        {"bar": 13, "beat": 2.0, "dur": 0.5, "note": "E5", "vel": 0.74},
        {"bar": 13, "beat": 2.5, "dur": 0.5, "note": "G5", "vel": 0.76},
        {"bar": 14, "beat": 1.0, "dur": 0.75, "note": "A5", "vel": 0.78},
        {"bar": 14, "beat": 2.0, "dur": 0.5, "note": "G5", "vel": 0.70},
        {"bar": 14, "beat": 2.5, "dur": 0.5, "note": "E5", "vel": 0.68},
        {"bar": 14, "beat": 3.5, "dur": 1.0, "note": "D5", "vel": 0.70},
    ]

    bass = []
    roots = ["G2", "G2", "F2", "F2", "C2", "C2", "D2", "D2",
             "G2", "G2", "F2", "F2", "C2", "D2", "G2", "D2"]
    for bar, root in enumerate(roots, start=1):
        fifth = {"G2": "D3", "F2": "C3", "C2": "G2", "D2": "A2"}[root]
        bass.extend([
            {"bar": bar, "beat": 1.0, "dur": 0.65, "note": root, "vel": 0.78},
            {"bar": bar, "beat": 2.0, "dur": 0.45, "note": fifth, "vel": 0.56},
            {"bar": bar, "beat": 2.75, "dur": 0.55, "note": root, "vel": 0.66},
            {"bar": bar, "beat": 4.0, "dur": 0.55, "note": fifth, "vel": 0.58},
        ])

    guitar = []
    chords = [
        ("G4", "B4", "D5"), ("G4", "B4", "D5"), ("F4", "A4", "C5"), ("F4", "A4", "C5"),
        ("E4", "G4", "C5"), ("E4", "G4", "C5"), ("F#4", "A4", "D5"), ("F#4", "A4", "D5"),
    ]
    for bar in range(1, 17):
        chord = chords[(bar - 1) % len(chords)]
        for beat in [1.5, 2.5, 3.5, 4.5]:
            for note in chord:
                guitar.append({"bar": bar, "beat": beat, "dur": 0.32, "note": note, "vel": 0.44})

    marimba = arp([
        ["G4", "B4", "D5", "B4", "E5", "D5", "B4", "A4"],
        ["G4", "B4", "D5", "G5", "E5", "D5", "B4", "D5"],
        ["F4", "A4", "C5", "A4", "D5", "C5", "A4", "G4"],
        ["C4", "E4", "G4", "E4", "A4", "G4", "E4", "D4"],
    ], range(1, 17), dur=0.5, vel=0.48)

    pad = []
    for bar, chord in enumerate(chords + chords, start=1):
        for note in chord:
            pad.append({"bar": bar, "beat": 1.0, "dur": 3.8, "note": note, "vel": 0.25})

    hits = []
    for bar in range(1, 17):
        hits.append({"bar": bar, "beat": 1.0, "pitch": 36, "vel": 66, "dur": 0.18})  # kick
        hits.append({"bar": bar, "beat": 3.0, "pitch": 36, "vel": 54, "dur": 0.18})
        for beat in [1.5, 2.5, 3.5, 4.5]:
            hits.append({"bar": bar, "beat": beat, "pitch": 75, "vel": 48, "dur": 0.12})  # claves
        for beat in [1.75, 2.75, 3.75, 4.75]:
            hits.append({"bar": bar, "beat": beat, "pitch": 70, "vel": 36, "dur": 0.10})  # maracas
        for beat in [2.0, 4.0]:
            hits.append({"bar": bar, "beat": beat, "pitch": 63, "vel": 50, "dur": 0.16})  # conga

    tracks = [
        conductor(title, bpm, "Tropical coast loop, G Mixolydian, syncopated offbeats and bright motif."),
        music_track("Flute Coast Motif", 0, 73, lead, volume=100, pan=70, reverb=38, chorus=10),
        music_track("Marimba Waterline", 1, 12, marimba, volume=82, pan=48, reverb=30, chorus=8),
        music_track("Offbeat Nylon Guitar", 2, 24, guitar, volume=70, pan=36, reverb=34, chorus=10),
        music_track("Round Island Bass", 3, 32, bass, volume=98, pan=58, reverb=18, chorus=4),
        music_track("Warm Sea Pad", 4, 89, pad, volume=48, pan=72, reverb=58, chorus=20),
        percussion_track("Island Percussion", hits, volume=92, reverb=22),
    ]
    MIDI_DIR.mkdir(parents=True, exist_ok=True)
    write_midi(MIDI_DIR / "palm_lantern_coast_tropical.mid", tracks)


def make_battle():
    title = "Iron Vow Skirmish"
    bpm = 150

    # Active battle test: short boss/threat cell collides with a brighter answer.
    lead = [
        {"bar": 1, "beat": 1.0, "dur": 0.5, "note": "C5", "vel": 0.86},
        {"bar": 1, "beat": 1.5, "dur": 0.5, "note": "Db5", "vel": 0.84},
        {"bar": 1, "beat": 2.0, "dur": 0.5, "note": "G5", "vel": 0.88},
        {"bar": 1, "beat": 2.5, "dur": 0.5, "note": "F5", "vel": 0.80},
        {"bar": 2, "beat": 1.0, "dur": 0.5, "note": "Eb5", "vel": 0.78},
        {"bar": 2, "beat": 1.5, "dur": 0.5, "note": "G5", "vel": 0.82},
        {"bar": 2, "beat": 2.0, "dur": 0.5, "note": "Bb5", "vel": 0.84},
        {"bar": 2, "beat": 3.0, "dur": 1.0, "note": "G5", "vel": 0.78},
        {"bar": 5, "beat": 1.0, "dur": 0.5, "note": "G5", "vel": 0.88},
        {"bar": 5, "beat": 1.5, "dur": 0.5, "note": "Ab5", "vel": 0.86},
        {"bar": 5, "beat": 2.0, "dur": 0.5, "note": "F5", "vel": 0.80},
        {"bar": 5, "beat": 2.5, "dur": 0.5, "note": "Db5", "vel": 0.82},
        {"bar": 6, "beat": 1.0, "dur": 0.5, "note": "C5", "vel": 0.82},
        {"bar": 6, "beat": 1.5, "dur": 0.5, "note": "Eb5", "vel": 0.82},
        {"bar": 6, "beat": 2.0, "dur": 0.5, "note": "G5", "vel": 0.86},
        {"bar": 6, "beat": 3.0, "dur": 1.0, "note": "C6", "vel": 0.88},
        {"bar": 9, "beat": 1.0, "dur": 0.375, "note": "C6", "vel": 0.90},
        {"bar": 9, "beat": 1.5, "dur": 0.375, "note": "Bb5", "vel": 0.84},
        {"bar": 9, "beat": 2.0, "dur": 0.375, "note": "Ab5", "vel": 0.82},
        {"bar": 9, "beat": 2.5, "dur": 0.375, "note": "G5", "vel": 0.82},
        {"bar": 10, "beat": 1.0, "dur": 0.5, "note": "Db5", "vel": 0.86},
        {"bar": 10, "beat": 1.5, "dur": 0.5, "note": "F5", "vel": 0.82},
        {"bar": 10, "beat": 2.0, "dur": 0.5, "note": "G5", "vel": 0.86},
        {"bar": 10, "beat": 3.0, "dur": 1.0, "note": "Eb5", "vel": 0.78},
        {"bar": 13, "beat": 1.0, "dur": 0.5, "note": "C5", "vel": 0.86},
        {"bar": 13, "beat": 1.5, "dur": 0.5, "note": "Db5", "vel": 0.84},
        {"bar": 13, "beat": 2.0, "dur": 0.5, "note": "G5", "vel": 0.88},
        {"bar": 13, "beat": 2.5, "dur": 0.5, "note": "F5", "vel": 0.82},
        {"bar": 14, "beat": 1.0, "dur": 0.5, "note": "Eb5", "vel": 0.84},
        {"bar": 14, "beat": 1.5, "dur": 0.5, "note": "G5", "vel": 0.86},
        {"bar": 14, "beat": 2.0, "dur": 0.5, "note": "Bb5", "vel": 0.88},
        {"bar": 14, "beat": 2.5, "dur": 0.5, "note": "C6", "vel": 0.90},
        {"bar": 16, "beat": 3.0, "dur": 0.5, "note": "Bb4", "vel": 0.78},
        {"bar": 16, "beat": 3.5, "dur": 0.5, "note": "Db5", "vel": 0.82},
        {"bar": 16, "beat": 4.0, "dur": 0.5, "note": "C5", "vel": 0.86},
    ]

    bass = []
    patterns = [
        ["C2", "G1", "C2", "Db2", "C2", "G1", "Bb1", "G1"],
        ["C2", "G1", "Eb2", "C2", "Db2", "C2", "G1", "Bb1"],
        ["Ab1", "Eb2", "Ab1", "G1", "F1", "C2", "G1", "C2"],
        ["C2", "G1", "Db2", "G1", "C2", "Bb1", "Db2", "C2"],
    ]
    for bar in range(1, 17):
        pattern = patterns[(bar - 1) % len(patterns)]
        for step, note in enumerate(pattern):
            bass.append({"bar": bar, "beat": 1 + step * 0.5, "dur": 0.38, "note": note, "vel": 0.86 if step in (0, 3, 6) else 0.66})

    strings = []
    chords = [
        ("C3", "G3", "Db4"), ("C3", "Eb3", "G3"), ("Ab2", "Eb3", "G3"), ("G2", "Db3", "F3"),
        ("C3", "G3", "Db4"), ("C3", "Eb3", "Bb3"), ("Ab2", "C3", "G3"), ("G2", "Db3", "F3"),
        ("C3", "G3", "C4"), ("Bb2", "F3", "Ab3"), ("Ab2", "Eb3", "C4"), ("G2", "Db3", "B3"),
        ("C3", "G3", "Db4"), ("C3", "Eb3", "G3"), ("Ab2", "Eb3", "Bb3"), ("G2", "Db3", "F3"),
    ]
    for bar, chord in enumerate(chords, start=1):
        for note in chord:
            strings.append({"bar": bar, "beat": 1.0, "dur": 1.85, "note": note, "vel": 0.48})
            strings.append({"bar": bar, "beat": 3.0, "dur": 1.65, "note": note, "vel": 0.42})

    counter = []
    for bar in range(1, 17):
        if bar % 4 == 0:
            counter.extend([
                {"bar": bar, "beat": 2.5, "dur": 0.25, "note": "F5", "vel": 0.58},
                {"bar": bar, "beat": 3.0, "dur": 0.25, "note": "G5", "vel": 0.62},
                {"bar": bar, "beat": 3.5, "dur": 0.25, "note": "Ab5", "vel": 0.60},
                {"bar": bar, "beat": 4.0, "dur": 0.25, "note": "Bb5", "vel": 0.64},
            ])
        else:
            counter.extend([
                {"bar": bar, "beat": 2.0, "dur": 0.5, "note": "G4", "vel": 0.52},
                {"bar": bar, "beat": 3.5, "dur": 0.5, "note": "Db5", "vel": 0.55},
            ])

    pulse = []
    for bar in range(1, 17):
        for beat in [1.0, 1.75, 2.5, 3.25, 4.0]:
            pulse.append({"bar": bar, "beat": beat, "dur": 0.18, "note": "C4", "vel": 0.42})
            pulse.append({"bar": bar, "beat": beat, "dur": 0.18, "note": "G4", "vel": 0.34})

    hits = []
    for bar in range(1, 17):
        for beat, pitch, vel in [(1.0, 41, 92), (2.5, 45, 72), (3.5, 47, 60), (4.0, 41, 78)]:
            hits.append({"bar": bar, "beat": beat, "pitch": pitch, "vel": vel, "dur": 0.12})
        if bar in [4, 8, 12, 16]:
            hits.append({"bar": bar, "beat": 4.0, "pitch": 49, "vel": 78, "dur": 0.65})

    tracks = [
        conductor(title, bpm, "Experimental active battle loop, C minor/Phrygian color, motif collision and tom-driven pressure."),
        music_track("Brass Battle Motif", 0, 61, lead, volume=106, pan=66, reverb=38, chorus=8),
        music_track("Distorted Bass Engine", 1, 38, bass, volume=104, pan=52, reverb=16, chorus=4),
        music_track("String Stab Plane", 2, 48, strings, volume=82, pan=70, reverb=44, chorus=10),
        music_track("High Counter Threat", 3, 80, counter, volume=76, pan=82, reverb=34, chorus=12),
        music_track("Muted Pulse Chords", 4, 29, pulse, volume=58, pan=42, reverb=24, chorus=4),
        percussion_track("Low Toms And Hits", hits, volume=102, reverb=24),
    ]
    MIDI_DIR.mkdir(parents=True, exist_ok=True)
    write_midi(MIDI_DIR / "iron_vow_skirmish_battle.mid", tracks)


def make_volcano_demon_king():
    title = "Volcanic Demon King"
    bpm = 168

    boss = []
    boss_cells = [
        [("D5", 0.5, 0.92), ("Eb5", 0.5, 0.88), ("A5", 0.5, 0.94), ("G5", 0.5, 0.86)],
        [("F5", 0.5, 0.86), ("A5", 0.5, 0.90), ("C6", 0.5, 0.92), ("Bb5", 0.5, 0.86)],
        [("D6", 0.375, 0.94), ("C6", 0.375, 0.86), ("A5", 0.375, 0.88), ("G5", 0.375, 0.82)],
        [("Eb5", 0.5, 0.92), ("A5", 0.5, 0.96), ("Bb5", 0.5, 0.92), ("D6", 0.5, 0.98)],
    ]
    for block in range(8):
        base_bar = block * 4 + 1
        cell = boss_cells[block % len(boss_cells)]
        for i, (note, dur, vel) in enumerate(cell):
            boss.append({"bar": base_bar, "beat": 1 + i * 0.5, "dur": dur, "note": note, "vel": vel})
        boss.extend([
            {"bar": base_bar + 1, "beat": 1.0, "dur": 0.5, "note": "D5", "vel": 0.86},
            {"bar": base_bar + 1, "beat": 1.5, "dur": 0.5, "note": "F5", "vel": 0.84},
            {"bar": base_bar + 1, "beat": 2.0, "dur": 0.5, "note": "A5", "vel": 0.88},
            {"bar": base_bar + 1, "beat": 3.0, "dur": 1.0, "note": "Eb5" if block % 2 == 0 else "C6", "vel": 0.86},
        ])
        if block >= 4:
            boss.extend([
                {"bar": base_bar + 2, "beat": 1.0, "dur": 0.25, "note": "A5", "vel": 0.92},
                {"bar": base_bar + 2, "beat": 1.5, "dur": 0.25, "note": "Bb5", "vel": 0.88},
                {"bar": base_bar + 2, "beat": 2.0, "dur": 0.25, "note": "C6", "vel": 0.92},
                {"bar": base_bar + 2, "beat": 2.5, "dur": 0.25, "note": "Eb6", "vel": 0.96},
            ])
        boss.extend([
            {"bar": base_bar + 3, "beat": 3.0, "dur": 0.5, "note": "C5", "vel": 0.78},
            {"bar": base_bar + 3, "beat": 3.5, "dur": 0.5, "note": "Eb5", "vel": 0.82},
            {"bar": base_bar + 3, "beat": 4.0, "dur": 0.5, "note": "D5", "vel": 0.88},
        ])

    bass = []
    bass_patterns = [
        ["D2", "A1", "D2", "Eb2", "D2", "A1", "C2", "A1"],
        ["Bb1", "F2", "Bb1", "A1", "G1", "D2", "A1", "D2"],
        ["D2", "Eb2", "F2", "A1", "D2", "C2", "A1", "D2"],
        ["G1", "D2", "Bb1", "A1", "Eb2", "D2", "A1", "D2"],
    ]
    for bar in range(1, 33):
        pattern = bass_patterns[(bar - 1) % len(bass_patterns)]
        for step, note in enumerate(pattern):
            bass.append({"bar": bar, "beat": 1 + step * 0.5, "dur": 0.34, "note": note, "vel": 0.94 if step in (0, 3, 6) else 0.72})

    choir = []
    chords = [
        ("D3", "A3", "Eb4"), ("D3", "F3", "A3"), ("Bb2", "F3", "A3"), ("A2", "Eb3", "G3"),
        ("D3", "A3", "D4"), ("C3", "G3", "Bb3"), ("Bb2", "F3", "D4"), ("A2", "Eb3", "C4"),
    ]
    for bar in range(1, 33):
        chord = chords[(bar - 1) % len(chords)]
        for note in chord:
            choir.append({"bar": bar, "beat": 1.0, "dur": 3.75, "note": note, "vel": 0.44 if bar < 17 else 0.54})

    strings = []
    for bar in range(1, 33):
        stab_notes = chords[(bar - 1) % len(chords)]
        for beat in [1.0, 2.5, 3.5]:
            for note in stab_notes:
                strings.append({"bar": bar, "beat": beat, "dur": 0.28, "note": note, "vel": 0.56 if beat == 1.0 else 0.45})

    heat = []
    for bar in range(1, 33):
        if bar % 4 in (2, 0):
            heat.extend([
                {"bar": bar, "beat": 2.0, "dur": 0.5, "note": "A6", "vel": 0.44},
                {"bar": bar, "beat": 2.5, "dur": 0.5, "note": "Bb6", "vel": 0.40},
                {"bar": bar, "beat": 3.0, "dur": 0.75, "note": "Eb7", "vel": 0.46},
            ])
        if bar in (16, 24, 32):
            heat.extend([
                {"bar": bar, "beat": 3.0, "dur": 0.25, "note": "D7", "vel": 0.62},
                {"bar": bar, "beat": 3.5, "dur": 0.25, "note": "Eb7", "vel": 0.64},
                {"bar": bar, "beat": 4.0, "dur": 0.25, "note": "A7", "vel": 0.70},
            ])

    hits = []
    for bar in range(1, 33):
        for beat, pitch, vel in [(1.0, 41, 104), (2.5, 45, 78), (3.5, 47, 68), (4.0, 41, 82)]:
            hits.append({"bar": bar, "beat": beat, "pitch": pitch, "vel": vel if bar < 17 else min(118, vel + 10), "dur": 0.12})
        if bar % 4 == 0:
            hits.append({"bar": bar, "beat": 4.0, "pitch": 49, "vel": 90, "dur": 0.5})
        if bar in (8, 16, 24, 32):
            hits.append({"bar": bar, "beat": 4.5, "pitch": 57, "vel": 92, "dur": 0.35})

    tracks = [
        conductor(title, bpm, "Final boss battle against a Demon King in a volcano. D Phrygian/diminished color, motif collision, lava pressure, unresolved loop."),
        music_track("Demon King Brass Motif", 0, 61, boss, volume=112, pan=66, reverb=40, chorus=8),
        music_track("Lava Bass Engine", 1, 38, bass, volume=110, pan=50, reverb=14, chorus=4),
        music_track("Doom Choir Plane", 2, 52, choir, volume=82, pan=64, reverb=72, chorus=20),
        music_track("Volcanic String Stabs", 3, 48, strings, volume=88, pan=70, reverb=42, chorus=10),
        music_track("High Heat Threat", 4, 80, heat, volume=76, pan=84, reverb=48, chorus=16),
        percussion_track("Ritual Lava Impacts", hits, volume=110, reverb=28),
    ]
    MIDI_DIR.mkdir(parents=True, exist_ok=True)
    write_midi(MIDI_DIR / "volcanic_demon_king_final_boss.mid", tracks)


if __name__ == "__main__":
    MIDI_DIR.mkdir(parents=True, exist_ok=True)
    make_snowfield()
    make_tropical()
    make_battle()
    make_volcano_demon_king()
    print(MIDI_DIR / "white_horizon_snowfield.mid")
    print(MIDI_DIR / "palm_lantern_coast_tropical.mid")
    print(MIDI_DIR / "iron_vow_skirmish_battle.mid")
    print(MIDI_DIR / "volcanic_demon_king_final_boss.mid")
