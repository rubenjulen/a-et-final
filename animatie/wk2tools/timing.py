import json, subprocess, os
B='/tmp/claude-0/-home-user-menssana/175e1d50-6875-5f56-acf6-23260f0c6b9a/scratchpad/remotion/'
for n in (6,7,8):
    z=json.load(open(B+f'clip{n}/zinnen.json')); t=0.8; cues=[]; est=[]
    for k,txt,g in z:
        p=B+f'public/aud_c{n}/{k}.mp3'
        if os.path.exists(p):
            d=float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',p],capture_output=True,text=True).stdout)
        else:
            d=round(len(txt)/15.5,2); est.append(k)
        cues.append({'key':k,'text':txt,'start':round(t,3),'dur':round(d,3),'audio':os.path.exists(p)}); t+=d+g
    json.dump({'cues':cues,'total':round(t+0.5,2),'audioDir':f'aud_c{n}','estimated':est},open(B+f'src/timing_c{n}.json','w'),ensure_ascii=False,indent=1)
    print(n,'total',round(t+0.5,1),'s =',round((t+0.5)/60,1),'min, geschat:',len(est))
