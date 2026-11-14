// node stills_wk8.mjs Comp frame1,frame2,...  -> stills_wk8/<Comp>_<frame>.png (scale 0.5)
import { bundle } from '@remotion/bundler';
import { renderStill, selectComposition } from '@remotion/renderer';
import path from 'path';
import fs from 'fs';
const [comp, framesArg] = process.argv.slice(2);
const frames = framesArg.split(',').map(Number);
const serveUrl = await bundle({ entryPoint: path.resolve('src/entry_wk8.jsx') });
const browserExecutable = '/opt/pw-browsers/chromium_headless_shell-1243/chrome-headless-shell-linux64/chrome-headless-shell';
const composition = await selectComposition({ serveUrl, id: comp, browserExecutable });
fs.mkdirSync('stills_wk8', { recursive: true });
for (const f of frames) {
  const out = `stills_wk8/${comp}_${String(f).padStart(5, '0')}.png`;
  await renderStill({ composition, serveUrl, output: out, frame: f, scale: 0.5, browserExecutable });
  console.log(out);
}
