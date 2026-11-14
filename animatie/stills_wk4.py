# Rendert per scène een still van kaderclip C: python3 stills_wk4.py [sleutel:fractie ...]
import json, subprocess, sys, os
t = json.load(open('src/timing_kC.json')); cue = {c['key']: c for c in t['cues']}
BR = '/opt/pw-browsers/chromium_headless_shell-1243/chrome-headless-shell-linux64/chrome-headless-shell'
shots = sys.argv[1:] or ['C0:0.9', 'C0c:0.95', 'C1d:0.95', 'C2f:0.9', 'C3e:0.95', 'CQ1:1.2', 'CQ1b:0.9', 'C4e:0.95', 'C5e:0.95', 'CQ2b:0.9', 'C6e:0.95', 'C7d:0.95', 'C7e:0.95', 'C7f:0.95', 'C8c:0.95']
os.makedirs('stills_wk4', exist_ok=True)
for s in shots:
    k, p = s.split(':'); p = float(p)
    fr = round((cue[k]['start'] + cue[k]['dur'] * p) * 30) if p <= 1 else round((cue[k]['start'] + cue[k]['dur'] + (p - 1) * 8) * 30)
    out = f'stills_wk4/KaderC_{k}.png'
    r = subprocess.run(['npx', 'remotion', 'still', 'src/entry_wk4.jsx', 'KaderC', out, f'--frame={fr}', '--scale=0.5', f'--browser-executable={BR}'], capture_output=True, text=True)
    print(out, 'ok' if r.returncode == 0 else r.stderr[-600:])
