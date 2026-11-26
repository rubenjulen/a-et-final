// node stills_any.mjs <entry.jsx> <CompId> <timing.json> <keys of frames>  -> stills_any/<Comp>_<frame>.png (scale 0.5)
// frames: komma-lijst van frames, of sleutel+seconden (bijv. d7c+5).
import { bundle } from '@remotion/bundler';
import { renderStill, selectComposition } from '@remotion/renderer';
import path from 'path';
import fs from 'fs';
const [entry, comp, tpath, list] = process.argv.slice(2);
const timing = JSON.parse(fs.readFileSync(tpath, 'utf8'));
const cue = Object.fromEntries(timing.cues.map((c) => [c.key, c]));
const frames = list.split(',').map((s) => (/^\d+$/.test(s) ? Number(s) : Math.round((cue[s.split('+')[0]].start + Number(s.split('+')[1] || 0)) * 30)));
const serveUrl = await bundle({ entryPoint: path.resolve(entry) });
const browserExecutable = '/opt/pw-browsers/chromium_headless_shell-1243/chrome-headless-shell-linux64/chrome-headless-shell';
const composition = await selectComposition({ serveUrl, id: comp, browserExecutable });
fs.mkdirSync('stills_any', { recursive: true });
for (const f of frames) {
  const out = `stills_any/${comp}_${String(f).padStart(5, '0')}.png`;
  await renderStill({ composition, serveUrl, output: out, frame: f, scale: 0.5, browserExecutable });
  console.log(out);
}
