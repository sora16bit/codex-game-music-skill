# Web Audio Patterns

Use Web Audio for fast prototypes, procedural SFX, and interactive sketches. If the user asks for production-quality music, prefer rendered loops/stems or MIDI plus a real synth unless the project needs procedural audio.

## Minimal Audio State

```js
const audio = {
  ctx: null,
  master: null,
  musicGain: null,
  sfxGain: null,
  enabled: false,
  beatStep: 0,
  phraseStep: 0,
  nextBeatAt: 0,
  stepSeconds: 0.125,
  musicIntensity: 0.25
};

function initAudio() {
  if (audio.ctx) return;
  audio.ctx = new (window.AudioContext || window.webkitAudioContext)();
  audio.master = audio.ctx.createGain();
  audio.musicGain = audio.ctx.createGain();
  audio.sfxGain = audio.ctx.createGain();
  audio.master.gain.value = 0.7;
  audio.musicGain.gain.value = 0.28;
  audio.sfxGain.gain.value = 0.7;
  audio.musicGain.connect(audio.master);
  audio.sfxGain.connect(audio.master);
  audio.master.connect(audio.ctx.destination);
  audio.enabled = true;
}
```

## Safe One-Shot Tone

```js
function playTone(freq, duration, type = "sine", volume = 0.04, endFreq = freq, delay = 0, bus = audio.musicGain) {
  if (!audio.ctx || !audio.master || !audio.enabled) return;
  const start = audio.ctx.currentTime + delay;
  const end = start + duration;
  const osc = audio.ctx.createOscillator();
  const gain = audio.ctx.createGain();
  osc.type = type;
  osc.frequency.setValueAtTime(freq, start);
  osc.frequency.exponentialRampToValueAtTime(Math.max(1, endFreq), end);
  gain.gain.setValueAtTime(0.0001, start);
  gain.gain.exponentialRampToValueAtTime(volume, start + 0.01);
  gain.gain.exponentialRampToValueAtTime(0.0001, end);
  osc.connect(gain);
  gain.connect(bus || audio.musicGain || audio.master);
  osc.start(start);
  osc.stop(end + 0.03);
}
```

## Short Noise Burst

```js
function playNoise(duration = 0.08, volume = 0.04, filterFreq = 3200, delay = 0, bus = audio.sfxGain) {
  if (!audio.ctx || !audio.enabled) return;
  const start = audio.ctx.currentTime + delay;
  const end = start + duration;
  const buffer = audio.ctx.createBuffer(1, Math.max(1, audio.ctx.sampleRate * duration), audio.ctx.sampleRate);
  const data = buffer.getChannelData(0);
  for (let i = 0; i < data.length; i++) data[i] = Math.random() * 2 - 1;
  const src = audio.ctx.createBufferSource();
  const filter = audio.ctx.createBiquadFilter();
  const gain = audio.ctx.createGain();
  src.buffer = buffer;
  filter.type = "bandpass";
  filter.frequency.setValueAtTime(filterFreq, start);
  gain.gain.setValueAtTime(0.0001, start);
  gain.gain.exponentialRampToValueAtTime(volume, start + 0.005);
  gain.gain.exponentialRampToValueAtTime(0.0001, end);
  src.connect(filter);
  filter.connect(gain);
  gain.connect(bus || audio.sfxGain || audio.master);
  src.start(start);
  src.stop(end + 0.02);
}
```

## Chord Stab

```js
function playChord(freqs, duration = 0.18, volume = 0.025, delay = 0) {
  freqs.forEach((freq, index) => {
    playTone(freq, duration, index === 0 ? "triangle" : "sawtooth", volume, freq * 0.997, delay + index * 0.006);
  });
}
```

## Bass Pulse

```js
function playBass(freq, step, intensity = audio.musicIntensity) {
  const dur = step % 8 === 0 ? 0.18 : 0.11;
  const vol = 0.045 + intensity * 0.035;
  playTone(freq, dur, "square", vol, freq * 0.5);
}
```

## Hat / Tick

```js
function playHat(step, intensity = audio.musicIntensity) {
  if (intensity < 0.35 && step % 4 !== 2) return;
  playNoise(0.025, 0.012 + intensity * 0.018, 7200, 0, audio.musicGain);
}
```

## Game Loop Sequencer

```js
function updateMusic() {
  if (!audio.ctx || !audio.enabled) return;
  if (state.time < audio.nextBeatAt) return;
  audio.nextBeatAt = state.time + audio.stepSeconds;
  const step = audio.beatStep++;
  if (step % 4 === 0) playKick();
  if (step % 2 === 0) playBass(step);
  if (step % 8 === 0) playChord(step);
  playHat(step, audio.musicIntensity);
  if (state.stageIndex >= 1 && step % 2 === 0) playLead(audio.phraseStep++);
}
```

## Adaptive Layer Controls

- `stageIndex`: unlock musical layers as the game introduces mechanics.
- `danger`: add alarm or high pulse when hazards/enemies are near.
- `energy`: thin music or add warning motif at low resources.
- `won`: stop danger layers and play a bright stinger.
- `alive`: mute drums during respawn or play death hit.
- `speed`: increase hat density, bass octave accents, and phrase fills.
- `combo`: add reward notes or call-response lead fragments.
- `bossPhase`: change section at phrase boundary and add a new layer.

## Mixing

- Keep SFX louder than individual music tones.
- Use short envelopes for busy gameplay.
- Use low drone sparingly; it can mask impact sounds.
- Use noise hats at low volume and short duration.
- Use separate music and SFX gains so gameplay sounds remain readable.
- For browser games, initialize/resume the context from a pointer/keyboard gesture.

## Cleanup

```js
function stopAudio() {
  if (!audio.ctx) return;
  audio.enabled = false;
  audio.beatStep = 0;
  audio.phraseStep = 0;
  audio.nextBeatAt = 0;
  if (audio.musicGain) audio.musicGain.gain.setTargetAtTime(0.0001, audio.ctx.currentTime, 0.04);
}
```

Track long-lived oscillators, delays, and intervals explicitly and stop/disconnect them on scene change. Prefer short scheduled sources for SFX.
