import json, subprocess, os
z=json.load(open('clip4/zinnen.json')); t=0.8; cues=[]; est=[]
for k,txt,g in z:
    p=f'public/aud_c4/{k}.mp3'
    if os.path.exists(p):
        d=float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',p],capture_output=True,text=True).stdout)
    else:
        d=round(len(txt)/15.5,2); est.append(k)
    cues.append({'key':k,'text':txt,'start':round(t,3),'dur':round(d,3),'audio':os.path.exists(p)}); t+=d+g
json.dump({'cues':cues,'total':round(t+0.5,2),'audioDir':'aud_c4','estimated':est},open('src/timing_c4.json','w'),ensure_ascii=False,indent=1)
print('total',round(t+0.5,2),'geschat:',len(est))
