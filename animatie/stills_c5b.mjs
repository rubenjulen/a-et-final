// node stills_c5b.mjs <frames|keys>  -> stills_c5b/Clip5b_<frame>.png (scale 0.5)
// Argument: komma-lijst van frames, of sleutels met offset in seconden (bijv. G2+5,P3+4).
import { bundle } from '@remotion/bundler';
import { renderStill, selectComposition } from '@remotion/renderer';
import path from 'path';
import fs from 'fs';
const timing = JSON.parse(fs.readFileSync('src/timing_c5b.json', 'utf8'));
const cue = Object.fromEntries(timing.cues.map((c) => [c.key, c]));
const frames = process.argv[2].split(',').map((s) => {
  if (/^\d+$/.test(s)) return Number(s);
  const [k, off] = s.split('+'); return Math.round((cue[k].start + Number(off || 0)) * 30);
});
const serveUrl = await bundle({ entryPoint: path.resolve('src/entry_c5b.jsx') });
const browserExecutable = '/opt/pw-browsers/chromium_headless_shell-1243/chrome-headless-shell-linux64/chrome-headless-shell';
const composition = await selectComposition({ serveUrl, id: 'Clip5b', browserExecutable });
fs.mkdirSync('stills_c5b', { recursive: true });
for (const f of frames) {
  const out = `stills_c5b/Clip5b_${String(f).padStart(5, '0')}.png`;
  await renderStill({ composition, serveUrl, output: out, frame: f, scale: 0.5, browserExecutable });
  console.log(out);
}
