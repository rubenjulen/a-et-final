import json,os,shutil
S='/tmp/claude-0/-home-user-menssana/175e1d50-6875-5f56-acf6-23260f0c6b9a/scratchpad/'
L=json.load(open('live.json')); missing={}
for k,d in L.items():
    out=f'{k}/project/slides'; os.makedirs(out,exist_ok=True)
    cands=sorted([S+c+'/project' for c in d['cands']],key=lambda p:os.path.getmtime(p+'/deck.json'),reverse=True)
    # deck.json
    got=None
    for c in cands:
        if os.path.getsize(c+'/deck.json')==d['deck']: got=c; break
    if got: shutil.copy(got+'/deck.json',f'{k}/project/deck.json')
    else: missing.setdefault(k,[]).append('project/deck.json')
    for sid,sz in d['s'].items():
        g=None
        for c in cands:
            p=f'{c}/slides/{sid}.html'
            if os.path.exists(p) and os.path.getsize(p)==sz: g=p; break
        if g: shutil.copy(g,f'{out}/{sid}.html')
        else: missing.setdefault(k,[]).append(f'project/slides/{sid}.html')
json.dump(missing,open('missing.json','w'),indent=1)
for k,v in missing.items(): print(k,len(v),v)
