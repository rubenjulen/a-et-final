import re
def sections(text, level=2):
    """split markdown into list of (heading, body) at given level"""
    pat=re.compile(r'^(#{%d}) (.+)$'%level, re.M)
    out=[]; ms=list(pat.finditer(text))
    for i,m in enumerate(ms):
        end=ms[i+1].start() if i+1<len(ms) else len(text)
        out.append((m.group(2).strip(), text[m.end():end]))
    return out
def get(text, title_start, level=2):
    for h,b in sections(text,level):
        if h.startswith(title_start): return b
    raise KeyError(title_start)
def unquote(s):
    return '\n'.join(re.sub(r'^> ?','',l) for l in s.split('\n'))
def strip_answers(s):
    """weekcheck: remove bold correct option markers and feedback lines"""
    lines=[]
    for l in s.split('\n'):
        if re.match(r'^\*Feedback:.*\*\s*$', l.strip()): continue
        m=re.match(r'^(- [a-d]\. )\*\*(.+)\*\*\s*$', l)
        if m: l=m.group(1)+m.group(2)
        lines.append(l)
    out='\n'.join(lines)
    return re.sub(r'\n{3,}','\n\n',out)
def clip_transcript(block):
    """from Tijd|Beeld|Kern table: return Kern texts as paragraphs"""
    rows=[]
    for l in block.split('\n'):
        if l.startswith('|') and not re.match(r'^\|\s*-', l) and 'Tijd' not in l[:8]:
            cells=[c.strip() for c in l.strip().strip('|').split('|')]
            if len(cells)>=3: rows.append(cells[-1].strip('"“”'))
    return '\n\n'.join(rows)
def drop_markers(s):
    s=re.sub(r'^\*Studententekst\.\*\s*','',s,flags=re.M)
    s=re.sub(r'\*Studententekst\.\s*','*',s)
    return s
def clean(s):
    return re.sub(r'\n{3,}','\n\n',s).strip()+'\n'
