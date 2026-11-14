# usage: python3 scripts_timing_wk1.py  -> maakt src/timing_kA.json en src/timing_c5.json
# Per zin: echte mp3-duur als public/<audioDir>/<key>.mp3 bestaat, anders schatting len/15.5 s.
import json, subprocess, os
JOBS = [('kaders/A/zinnen.json', 'aud_kA', 'src/timing_kA.json'), ('clip5/zinnen.json', 'aud_c5', 'src/timing_c5.json')]
for src, aud, out in JOBS:
    z = json.load(open(src)); t = 0.8; cues = []; est = []
    for k, txt, g in z:
        p = f'public/{aud}/{k}.mp3'
        if os.path.exists(p):
            d = float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', p], capture_output=True, text=True).stdout)
        else:
            d = round(len(txt) / 15.5, 2); est.append(k)
        cues.append({'key': k, 'text': txt, 'start': round(t, 3), 'dur': round(d, 3), 'audio': os.path.exists(p)}); t += d + g
    json.dump({'cues': cues, 'total': round(t + 0.5, 2), 'audioDir': aud, 'estimated': est}, open(out, 'w'), ensure_ascii=False, indent=1)
    print(out, 'total', round(t + 0.5, 1), 's, geschat:', len(est), 'van', len(z), ', tekens:', sum(len(x[1]) for x in z))
