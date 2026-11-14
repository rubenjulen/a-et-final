import json, subprocess, os, sys
# usage: python3 scripts_timing_wk3.py <zinnen.json> <audiodir under public> <out timing json>
zp, ad, out = sys.argv[1], sys.argv[2], sys.argv[3]
z=json.load(open(zp)); t=0.8; cues=[]; est=[]
for k,txt,g in z:
    p=f'public/{ad}/{k}.mp3'
    if os.path.exists(p):
        d=float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',p],capture_output=True,text=True).stdout)
    else:
        d=round(len(txt)/15.5,2); est.append(k)
    cues.append({'key':k,'text':txt,'start':round(t,3),'dur':round(d,3),'audio':os.path.exists(p)}); t+=d+g
json.dump({'cues':cues,'total':round(t+0.5,2),'audioDir':ad,'estimated':est},open(out,'w'),ensure_ascii=False,indent=1)
print(out,'total',round(t+0.5,2),'geschat:',len(est))
