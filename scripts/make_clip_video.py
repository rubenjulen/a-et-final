import sys, json, re, html, subprocess, wave, os
root, outdir, voice = sys.argv[1], sys.argv[2], sys.argv[3]
deck = json.load(open(f'{root}/project/deck.json'))
os.makedirs(f'{outdir}/aud', exist_ok=True); os.makedirs(f'{outdir}/seg', exist_ok=True)
def speak_text(t):
    t = html.unescape(re.sub(r'<[^>]+>', ' ', t))
    rep = [(r'\bA-AI2\b','A A I twee'),(r'\bA-AI1\b','A A I één'),(r'\bA-DG\b','A D G'),(r'\bA-ET\b','A E T'),
           (r'\bAI\b','A I'),(r'\bSRD\b','S R D'),(r'&',' en '),(r'\s+',' ')]
    for a,b in rep: t = re.sub(a,b,t)
    return t.strip()
segs=[]
for sid in deck['order']:
    src = open(f'{root}/project/slides/{sid}.html', encoding='utf-8').read()
    m = re.search(r'<aside>([\s\S]*?)</aside>', src)
    text = speak_text(m.group(1)) if m else ''
    wav = f'{outdir}/aud/{sid}.wav'
    subprocess.run([sys.executable,'-m','piper','-m',voice,'-f',wav,'--sentence-silence','0.35'], input=text.encode(), check=True, stderr=subprocess.DEVNULL)
    with wave.open(wav) as w: dur = w.getnframes()/w.getframerate()
    pause = 5.0 if re.match(r'tv\d+$', sid) else 0.8   # denktijd na een tussenvraag
    seg = f'{outdir}/seg/{sid}.mp4'
    subprocess.run(['ffmpeg','-y','-loglevel','error','-loop','1','-i',f'{outdir}/img/{sid}.png','-i',wav,
        '-af',f'apad=pad_dur={pause}','-t',f'{dur+pause:.2f}','-c:v','libx264','-tune','stillimage','-pix_fmt','yuv420p',
        '-r','25','-c:a','aac','-b:a','128k','-ar','44100',seg], check=True)
    segs.append(seg); print(sid, round(dur,1), 's', len(text.split()), 'woorden')
lst=f'{outdir}/list.txt'; open(lst,'w').write(''.join(f"file '{os.path.abspath(s)}'\n" for s in segs))
out=sys.argv[4]
subprocess.run(['ffmpeg','-y','-loglevel','error','-f','concat','-safe','0','-i',lst,'-c','copy','-movflags','+faststart',out],check=True)
print('klaar', out)
