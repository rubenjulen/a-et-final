import { bundle } from '@remotion/bundler';
import { renderStill, selectComposition } from '@remotion/renderer';
import fs from 'fs'; import path from 'path';
const B = '/tmp/claude-0/-home-user-menssana/175e1d50-6875-5f56-acf6-23260f0c6b9a/scratchpad/remotion/';
const exe = '/opt/pw-browsers/chromium_headless_shell-1243/chrome-headless-shell-linux64/chrome-headless-shell';
const only = process.argv[2] ? process.argv[2].split(',') : null; // e.g. "Clip6:d2a,Clip7:q1"
const serveUrl = await bundle({ entryPoint: B + 'src/entry_wk2.jsx', webpackOverride: (c) => c });
fs.mkdirSync(B + 'stills_wk2', { recursive: true });
const scenesOf = {
  Clip6: ['t0','d1a','d2a','d3a','d4a','q1','d5a','d6a','d7a','d8a','q2','d9a'],
  Clip7: ['t0','d1a','d2a','q1','d3a','d4a','d5a','q2','d6a','d7a'],
  Clip8: ['t0','d1a','d2a','d3a','d4a','d5a','q1','d6a','d7a'],
};
for (const [comp, keys] of Object.entries(scenesOf)) {
  const n = comp.slice(4);
  const t = JSON.parse(fs.readFileSync(B + `src/timing_c${n}.json`));
  const cue = Object.fromEntries(t.cues.map((c) => [c.key, c]));
  const composition = await selectComposition({ serveUrl, id: comp, browserExecutable: exe });
  for (let i = 0; i < keys.length; i++) {
    const k = keys[i];
    if (only && !only.includes(`${comp}:${k}`)) continue;
    const nextStart = i + 1 < keys.length ? cue[keys[i + 1]].start : t.total;
    // late in the scene: last cue of the scene (before next scene), 0.6 s before its end; quiz: during answer
    let sec = nextStart - 1.2;
    const frame = Math.max(0, Math.min(composition.durationInFrames - 1, Math.round(sec * 30)));
    const out = B + `stills_wk2/${comp}_${String(i).padStart(2,'0')}_${k}.png`;
    await renderStill({ composition, serveUrl, output: out, frame, scale: 0.5, browserExecutable: exe });
    console.log(out, frame);
  }
}
