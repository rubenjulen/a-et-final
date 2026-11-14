import json, subprocess, wave, sys, os
d=sys.argv[1]; voice=sys.argv[2]; z=json.load(open(f'{d}/zinnen.json'))
os.makedirs(f'{d}/aud',exist_ok=True); starts={}; t=0.8; parts=[]
for key,text,gap in z:
    w=f'{d}/aud/{key}.wav'
    if not os.path.exists(w):
        subprocess.run([sys.executable,'-m','piper','-m',voice,'-f',w,'--sentence-silence','0.3'],input=text.encode(),check=True,stderr=subprocess.DEVNULL)
    with wave.open(w) as f: dur=f.getnframes()/f.getframerate()
    starts[key]=round(t,2); parts.append((w,t)); t+=dur+gap
total=round(t+1.0,2)
json.dump({'starts':starts,'total':total},open(f'{d}/timing.json','w'))
# concat via silence padding (sequential, avoids huge amix)
lst=[]; cur=0.0
for i,(w,st) in enumerate(parts):
    sil=st-cur
    if sil>0.01:
        s=f'{d}/aud/_sil{i}.wav'; subprocess.run(['ffmpeg','-y','-loglevel','error','-f','lavfi','-i','anullsrc=r=22050:cl=mono','-t',f'{sil:.3f}',s],check=True); lst.append(s)
    lst.append(w)
    with wave.open(w) as f: cur=st+f.getnframes()/f.getframerate()
s=f'{d}/aud/_silend.wav'; subprocess.run(['ffmpeg','-y','-loglevel','error','-f','lavfi','-i','anullsrc=r=22050:cl=mono','-t',f'{total-cur:.3f}',s],check=True); lst.append(s)
open(f'{d}/aud/list.txt','w').write(''.join(f"file '{os.path.abspath(x)}'\n" for x in lst))
subprocess.run(['ffmpeg','-y','-loglevel','error','-f','concat','-safe','0','-i',f'{d}/aud/list.txt','-ar','44100',f'{d}/narration.wav'],check=True)
print(total, len(z))
