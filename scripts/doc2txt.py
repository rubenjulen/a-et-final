import json,re,html,sys
src,out=sys.argv[1],sys.argv[2]
raw=open(src).read(); i=raw.find('{'); d=json.loads(raw[i:raw.rfind('}')+1])
x=d['data']['xml']; open(out+'.xml','w').write(x)
t=re.sub(r"<(paragraph|embed|pending)\s+id='([^']+)'([^>]*)>", lambda m: "\n[%s%s h=%s] "%(m.group(2), (' H'+re.search(r"heading='(\d)'",m.group(3)).group(1)) if "heading=" in m.group(3) else '', (re.search(r"h='([0-9a-f]+)'",m.group(3)) or [0,''])[1] if re.search(r"h='([0-9a-f]+)'",m.group(3)) else ''), x)
t=re.sub(r"<row id='([^']+)'[^>]*>", r"\n  {row \1}", t)
t=re.sub(r"<cell id='([^']+)'[^>]*>", r" | ", t)
t=re.sub(r"<(table|list|blockquote) id='([^']+)'([^>]*)>", lambda m: "\n<%s %s %s>"%(m.group(1),m.group(2),(re.search(r"h='([0-9a-f]+)'",m.group(3)) or [0,''])[1] if re.search(r"h='([0-9a-f]+)'",m.group(3)) else ''), t)
t=re.sub(r"<listItem id='([^']+)'[^>]*>", r"\n  - ", t)
t=re.sub(r"<[^>]+>","",t); t=html.unescape(t)
open(out+'.txt','w').write(t); print(d['data']['rev'], d['data'].get('complete'), len(t))
