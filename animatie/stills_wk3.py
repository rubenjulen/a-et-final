import json, subprocess, sys, os
B='/opt/pw-browsers/chromium_headless_shell-1243/chrome-headless-shell-linux64/chrome-headless-shell'
comp, tfile, prefix, spec = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
t=json.load(open(tfile)); c={x['key']:x for x in t['cues']}
for item in spec.split(','):
    name,k,o=item.split(':')
    o=float(o) if o!='end' else None
    fr=int((c[k]['start']+(c[k]['dur']+3.5 if o is None else o))*30)
    out=f'stills_wk3/{prefix}_{name}.png'
    r=subprocess.run(['npx','remotion','still','src/entry_wk3.jsx',comp,out,f'--frame={fr}','--scale=0.5',f'--browser-executable={B}'],capture_output=True,text=True)
    print(name, fr, 'ok' if r.returncode==0 else r.stderr[-400:])
