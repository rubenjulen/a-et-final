import re
MD='/tmp/claude-0/-home-user-menssana/175e1d50-6875-5f56-acf6-23260f0c6b9a/scratchpad/mycampus/md/'
def load(n): return open(MD+f'raw_w{n}.md',encoding='utf-8').read()
def sec(t,start,end=None):
    i=t.find(start); assert i>=0,start
    if end is None: return t[i:]
    j=t.find(end,i+len(start)); assert j>=0,end
    return t[i:j]
def drop_first_line(s): return s.split('\n',1)[1] if '\n' in s else ''
def cut(s,start,end=None):
    """remove part of s from start up to end (exclusive)"""
    i=s.find(start); assert i>=0,start
    if end is None: return s[:i]
    j=s.find(end,i+len(start)); assert j>=0,end
    return s[:i]+s[j:]
def strip_beeld(s): return re.sub(r'\*Beeld:[^*]*\*\s*','',s)
def strip_juist(s):
    # remove '*Juist: X.*' and any explanation after it on that line
    s=re.sub(r'\s*\*Juist:[^*]*\*[^\n]*','',s)
    s=re.sub(r'\s*\*Antwoord:[^*]*\*[^\n]*','',s)
    return s
def strip_bold_options(s):
    return re.sub(r'^(- [a-e]\. )\*\*(.*?)\*\*\s*$',r'\1\2',s,flags=re.M)
def strip_feedback_lines(s):
    return re.sub(r'^\*Feedback:[^\n]*\n?','',s,flags=re.M)
def demote(s,n=1):
    return re.sub(r'^(#{2,5}) ',lambda m:'#'*(len(m.group(1))+n)+' ',s,flags=re.M)
def promote(s,n=1):
    return re.sub(r'^(#{3,6}) ',lambda m:'#'*(len(m.group(1))-n)+' ',s,flags=re.M)
def renum(s):
    # '## 4. Practicum 2: ...' -> '## Practicum 2: ...'
    return re.sub(r'^(#{2,3}) \d+\. ',r'\1 ',s,flags=re.M)
def table_clip_text(block):
    """Tijd|Beeld|Kern table -> paragraphs with Kern text"""
    out=[]
    for l in block.splitlines():
        m=re.match(r'^\|\s*\d+:\d+\s*\|[^|]*\|\s*(.*?)\s*\|\s*$',l)
        if m: out.append(m.group(1).replace('\\|','|'))
        elif l.startswith('| Tijd') or l.startswith('| ---'): continue
        else: out.append(l)
    return '\n\n'.join(x for x in out if x.strip()) if out else ''
def clean(s):
    s=re.sub(r'\n{3,}','\n\n',s)
    return s.strip()+'\n'
