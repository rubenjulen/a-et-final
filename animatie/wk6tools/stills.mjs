// node wk6tools/stills.mjs  -> renders one still per scene moment of KaderD into stills_wk6/
import { bundle } from '@remotion/bundler';
import { renderStill, selectComposition } from '@remotion/renderer';
import fs from 'fs'; import path from 'path';
const t = JSON.parse(fs.readFileSync('src/timing_kD.json', 'utf8'));
const cue = Object.fromEntries(t.cues.map((c) => [c.key, c]));
const at = (k, o) => Math.round((cue[k].start + (o === 'end' ? cue[k].dur - 0.3 : o)) * 30);
const shots = (process.argv[2] ? JSON.parse(process.argv[2]) : [
  ['00_title', 'D0a', 'end'], ['01_intro', 'D0d', 'end'], ['02_phases', 'D1d', 'end'], ['03_phases_live', 'D1e', 'end'],
  ['04_roles', 'D2e', 'end'], ['05_roles_banner', 'D2f', 'end'], ['06_agent', 'D3c', 'end'], ['07_agent_data', 'D3d', 5.5],
  ['08_agent_k3', 'D3e', 'end'], ['09_check', 'D4e', 'end'], ['10_check_risk', 'D4f', 'end'], ['11_q1', 'DQ1', 'end'],
  ['12_q1_answer', 'DQ1b', 'end'], ['13_agent_actions', 'D5c', 'end'], ['14_lanes', 'D5e', 'end'], ['15_log', 'D5f', 'end'],
  ['16_contract', 'D5g', 'end'], ['17_q2_answer', 'DQ2b', 'end'], ['18_kader', 'D6c', 'end'], ['19_kader_banner', 'D6d', 'end'], ['20_now', 'D7e', 'end'],
]);
const serveUrl = await bundle({ entryPoint: path.resolve('src/entry_wk6.jsx') });
const composition = await selectComposition({ serveUrl, id: 'KaderD', browserExecutable: '/opt/pw-browsers/chromium_headless_shell-1243/chrome-headless-shell-linux64/chrome-headless-shell' });
fs.mkdirSync('stills_wk6', { recursive: true });
for (const [name, k, o] of shots) {
  await renderStill({ composition, serveUrl, output: `stills_wk6/KaderD_${name}.png`, frame: at(k, o), scale: 0.5,
    browserExecutable: '/opt/pw-browsers/chromium_headless_shell-1243/chrome-headless-shell-linux64/chrome-headless-shell' });
  console.log('ok', name);
}
