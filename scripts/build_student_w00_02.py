import re, os
D='/tmp/claude-0/-home-user-menssana/175e1d50-6875-5f56-acf6-23260f0c6b9a/scratchpad/mycampus/'
IMG=D+'pdf/img/'
def raw(w): return open(D+f'md/raw_w{w:02d}.md',encoding='utf-8').read()

def block(t, start, end=None):
    """text from the line starting with `start` (inclusive) up to line starting with `end` (exclusive)"""
    L=t.split('\n'); i=next(k for k,l in enumerate(L) if l.startswith(start))
    j=len(L) if end is None else next(k for k,l in enumerate(L) if k>i and l.startswith(end))
    return '\n'.join(L[i:j]).strip('\n')

def body(t, start, end=None):
    """like block but without the heading line itself"""
    b=block(t,start,end).split('\n',1)
    return b[1].strip('\n') if len(b)>1 else ''

def demote(s, n=1):
    return re.sub(r'^(#+)', lambda m: '#'*min(6,len(m.group(1))+n), s, flags=re.M)

def no_answers(s):
    s=re.sub(r'[ \t]*\*\*Juist:[^\n]*','',s)            # **Juist: B.** uitleg
    s=re.sub(r'[ \t]*\*Juist:[^*\n]*\*','',s)            # *Juist: B.*
    s=re.sub(r'^\s*>\s*Juist:[^\n]*$','',s,flags=re.M)   # > Juist: B.
    s=re.sub(r'^\s*-\s*Juist:[^\n]*$','',s,flags=re.M)   # - Juist: B.
    s=re.sub(r'^>\s*$\n(>\s*$\n)+','>\n',s,flags=re.M)   # collapse empty quote lines
    s=re.sub(r'(\n>\s*)+\n(?!>)','\n\n',s)               # trailing empty quote line
    s=re.sub(r'\n{3,}','\n\n',s)
    return s.strip()

def no_beeld(s):
    s=re.sub(r'[ \t]*\*Beeld:[^*]*\*','',s)
    return s

def clip_questions(clipraw):
    """return only the tussenvragen (blockquotes) without answers"""
    qs=re.findall(r'((?:^>.*\n?)+)', clipraw, flags=re.M)
    return [no_answers(q) for q in qs if 'ussenvraag' in q]

def clip_transcript(clipraw, title):
    """spoken text per dia; tussenvragen replaced by a marker"""
    s=no_beeld(clipraw)
    n=[0]
    def rep(m):
        q=m.group(0)
        if 'ussenvraag' not in q: return q
        n[0]+=1
        lab=re.search(r'Tussenvraag( \d)?',q).group(0)
        return f'*[{lab}: de video stopt; beantwoord de vraag.]*\n'
    s=re.sub(r'(?:^>.*\n?)+',rep,s,flags=re.M)
    s=re.sub(r'\*\*(Dia \d+\.[^*]*)\*\*\s*','**\\1** ',s)
    s=re.sub(r'\n{3,}','\n\n',s).strip()
    return f'### {title}\n\n{s}'

def clips_section(t, clips):
    """clips: list of (heading_start, end_marker, title)"""
    out=['## Kennisclips','','Bekijk de clips in deze volgorde. Elke clip stopt bij de tussenvragen; je krijgt direct feedback. De gesproken tekst staat in de bijlage achteraan, om mee te lezen.','']
    app=['## Bijlage: tekst van de kennisclips (meelezen)','']
    for start,end,title,extra in clips:
        c=body(t,start,end)
        out+= [f'### {title}','',f'**Video:** {extra}','']
        qs=clip_questions(c)
        if qs:
            out+= ['**Tussenvragen in de clip**','']
            for q in qs: out+=[q,'']
        app+= [clip_transcript(c,title),'']
    return '\n'.join(out), '\n'.join(app)

def write(name, md):
    open(D+'md/'+name,'w',encoding='utf-8').write(md.strip()+'\n'); print('md',name,len(md))

def docfile(name, md):
    open(D+'md/'+name,'w',encoding='utf-8').write(md.strip()+'\n'); print('docent',name)

LINK='[link volgt op MyCampus]'

# ---------------- WEEK 0 ----------------
t=raw(0)
mod=body(t,'## 3. Moduletekst','## 4.')
mod=mod.split('\n',1)[1].strip() if mod.startswith('Deze tekst') else mod
leer=block(t,'**Leerdoelen.**','**Planning.**')
tijd=block(t,'**Tijdsbesteding voor de student.**','**Checklist')
welkom=block(t,'> **Onderwerp: Welkom','**Intakeformulier.**')
intake=block(t,'**Intakeformulier.**','**Gebruik van de antwoorden.**')
clips_md, app = clips_section(t,[
 ('### Clip 1.','### Clip 2.','Clip 1. Van deel 1 naar AI & Ethics (6 minuten)',LINK),
 ('### Clip 2.','## 5.','Clip 2. Waarom maakt AI fouten? (8 minuten)',LINK),
 ('### Clip 3.','### Clip 4.','Clip 3. Fouten tellen (7 minuten)',LINK),
 ('### Clip 4.','## 6.','Clip 4. Wat is anders bij generatieve AI? (8 minuten)',LINK)])
inst=demote(block(t,'## 6. Installatie','## 7.')).replace('### 6. ','## ')
data=block(t,'## 7. Over de dataset','## 8.').replace('## 7. ','## ')
prac=block(t,'## 8. Practicum 1','## 9.').replace('## 8. ','## ')
eigen=block(t,'## 9. De eigen oplossing','**Voor de docent.**').replace('## 9. ','## ')
quiz=no_answers(body(t,'## 10. Beginquiz','**Gebruik door de docent.**'))
quiz=quiz.replace('Studenten zien pas na afloop de juiste antwoorden en de feedback.','Na afloop zie je de juiste antwoorden en de feedback.')
md=f'''## Welkom

{welkom}

## Deze week

{mod}

**Belangrijke data.**

| Moment | Wat |
| --- | --- |
| Maandag 14 december | Week 0 opent |
| Dinsdag 5 januari, 19:00 tot 20:00 | Online inloopmoment voor installatie en vragen |
| Woensdag 6 januari, 23:59 | Alles afgerond: intake, practicum 1 met evidence card 1, beschrijving van de eigen oplossing (per groep), beginquiz |
| Donderdag 7 januari | College 1 |

{leer.replace('**Leerdoelen.** Na week 0 kan de student:','**Leerdoelen.** Na week 0 kun je:')}

{tijd.replace('**Tijdsbesteding voor de student.**','**Tijdsbesteding.**')}

## Intakeformulier

{intake.replace('**Intakeformulier.** ','')}

{clips_md}

{inst}

{data}

{prac}

{eigen}

## Beginquiz

{quiz}

## Inloopmoment

Dinsdag 5 januari, 19:00 tot 20:00, online. Voor hulp bij de installatie en vragen over de clips, het practicum en de eigen oplossing. De link staat in de leeromgeving; de opname komt er later bij, met de veelgestelde vragen.

{app}
'''
md=md.replace('Download suribank\\_kredietaanvragen.csv uit de leeromgeving.','Download suribank\\_kredietaanvragen.csv en practicum1.ipynb uit de leeromgeving.')
write('A-ET_Week00_studentversie.md',md)
docfile('docent_weekcheck_w00.md','# Week 0: antwoorden (alleen docent)\n\n## Beginquiz\n\n'+body(t,'## 10. Beginquiz','## 11.')+'\n\n## Tussenvragen in de clips\n\n'+'\n\n'.join(
  f'### {h}\n\n'+'\n\n'.join(q for q in re.findall(r'((?:^>.*\n?)+)',body(t,s,e),flags=re.M) if 'ussenvraag' in q)
  for h,s,e in [('Clip 1','### Clip 1.','### Clip 2.'),('Clip 2','### Clip 2.','## 5.'),('Clip 3','### Clip 3.','### Clip 4.'),('Clip 4','### Clip 4.','## 6.')]))

# ---------------- WEEK 1 ----------------
t=raw(1)
leer=block(t,'**Leerdoelen.**','**Planning en deadlines.**').replace('Na week 1 kan de student:','Na week 1 kun je:')
plan=block(t,'| Moment | Wat |','**Tijdsbesteding')
plan=plan.replace('| Woensdag 6 januari, 23:59 | Deadline week 0. Bekijk donderdagochtend de beginquiz, practicum 1 en de beschrijvingen van de eigen oplossingen |\n','')
plan=plan.replace('Feedforward-bericht aan alle groepen','Feedforward-bericht van de docent aan alle groepen')
tijd=block(t,'**Tijdsbesteding voor de student.**','**Checklist').replace('**Tijdsbesteding voor de student.**','**Tijdsbesteding.**')
groep=block(t,'## 2. Groepen en casus','## 3.').replace('## 2. ','## ')
lenzen=block(t,'**Lenzenkaarten.**','## 6.')
lenzen=lenzen.replace('**Lenzenkaarten.** Print elke kaart op A5. Elk groepje krijgt er één en beoordeelt het Suribank-dilemma alleen door die lens.','**Lenzenkaarten.** In het college krijgt elk groepje één lens en beoordeelt het Suribank-dilemma alleen door die lens. Je gebruikt de lenzen de hele module, ook in het dilemma-canvas (K5).')
k1=block(t,'## 6. K1 AI Use Case','## 7.').replace('## 6. ','## ')
k1=k1.replace('**Checklist voor een goed canvas.** De docent gebruikt deze punten voor de feedback; groepen controleren er zelf op vóór het inleveren.','**Checklist voor een goed canvas.** Controleer deze punten vóór het inleveren; de docent gebruikt ze ook voor de feedback.')
k1+='\n\n**Sjabloon.** Gebruik K1\\_AI\\_Use\\_Case\\_en\\_Scope\\_Canvas.docx, of het tabblad K1\\_Scope in A-ET\\_werkboek\\_instrumenten\\_2026-2027.xlsx.'
mod=block(t,'> **Week 1.','### Clip 5.')
clips_md, app = clips_section(t,[
 ('### Clip 5.','### Kaderclip A.','Clip 5. Wie beslist er eigenlijk? (6 minuten)',LINK),
 ('### Kaderclip A.','### Kernbron','Kaderclip A. Het kaderlandschap (5 minuten)',LINK)])
kern=block(t,'### Kernbron','### Weekcheck').replace('### ','## ')
wc=no_answers(block(t,'### Weekcheck week 1','### Voorbereiding college 2')).replace('### Weekcheck week 1','## Weekcheck')
wc=wc.replace('Vijf kennisvragen met directe feedback','Vijf kennisvragen met directe feedback na het invullen')
vc2=block(t,'### Voorbereiding college 2','## 8.').replace('### ','## ')
md=f'''## Deze week

{mod}

{leer}

**Planning en deadlines.**

{plan}

{tijd}

## College 1 (donderdag 7 januari)

Neem de beschrijving van jullie eigen oplossing uit week 0 mee, en jullie ethische evaluatie uit A-AI1. Het college opent met een dilemma van Suribank waarover je stemt. Daarna kijk je met je groepje door één ethische lens naar dat dilemma, en vullen jullie als groep het K1-canvas in.

{lenzen}

{groep}

{k1}

{clips_md}

{kern}

{wc}

{vc2}

{app}
'''
write('A-ET_Week01_studentversie.md',md)
docfile('docent_weekcheck_w01.md','# Week 1: antwoorden (alleen docent)\n\n'+block(t,'### Weekcheck week 1','**Logboekregel')+'\n\n## Tussenvragen in de clips\n\n'+'\n\n'.join(
  f'### {h}\n\n'+'\n\n'.join(q for q in re.findall(r'((?:^>.*\n?)+)',body(t,s,e),flags=re.M) if 'ussenvraag' in q)
  for h,s,e in [('Clip 5','### Clip 5.','### Kaderclip A.'),('Kaderclip A','### Kaderclip A.','### Kernbron')]))

# ---------------- WEEK 2 ----------------
t=raw(2)
leer=block(t,'**Leerdoelen.**','**Planning en deadlines.**').replace('Na week 2 kan de student:','Na week 2 kun je:')
plan=block(t,'| Moment | Wat |','**Tijdsbesteding')
plan=plan.replace('| Woensdag 13 januari | Vragen doorsturen naar de gastspreker; weekcheck met standpunt sluit om 23:59 |','| Woensdag 13 januari, 23:59 | Weekcheck met standpunt sluit |')
plan=plan.replace('| Maandag 18 januari | Feedforward-bericht |','| Maandag 18 januari | Feedforward-bericht van de docent |')
plan=plan.replace('Weekmodule 2 opent; feedforward op week 1','Weekmodule 2 opent; feedforward van de docent op week 1')
tijd=block(t,'**Tijdsbesteding voor de student.**','**Checklist').replace('**Tijdsbesteding voor de student.**','**Tijdsbesteding.**')
mod=block(t,'> **Week 2.','**Kernbron')
kern=block(t,'**Kernbron: Gender Shades.**','**Weekcheck week 2.**').replace(' Dit is een samenvatting voor de reader.',' Een samenvatting:')
wc=no_answers(block(t,'**Weekcheck week 2.**','## 3.'))
wc=wc.replace('**Weekcheck week 2.** ','')
clips_md, app = clips_section(t,[
 ('### Clip 6.','### Clip 7.','Clip 6. Waar komt bias vandaan? (8 minuten)',LINK),
 ('### Clip 7.','### Clip 8.','Clip 7. Privacy als ethische vraag (8 minuten)',LINK),
 ('### Clip 8.','## 4.','Clip 8. Automation bias (7 minuten)',LINK)])
verloop=block(t,'**Verloop per stelling.**','**Nabespreking.**')
k2=block(t,'## 7. K2','## 8.').replace('## 7. ','## ')
k2=k2.replace('&#91;embedded content: K2-voorbeeld · Suribank, macht tegenover kwetsbaarheid\\]',f'![K2-voorbeeld: Suribank, macht tegenover kwetsbaarheid]({IMG}w02_k2.png)\n\n*K2-voorbeeld · Suribank, macht tegenover kwetsbaarheid*')
k2=k2.replace('**Sjabloon.**','**Sjabloon.** Gebruik het tabblad K2\\_Stakeholders in A-ET\\_werkboek\\_instrumenten\\_2026-2027.xlsx. De kolommen:')
k3=block(t,'## 8. K3','## 9.').replace('## 8. ','## ')
k3=k3.replace('&#91;embedded content: K3-voorbeeld · Suribank, procesplaat met risicopunten\\]',f'![K3-voorbeeld: Suribank, procesplaat met risicopunten]({IMG}w02_k3.png)\n\n*K3-voorbeeld · Suribank, procesplaat met risicopunten*')
k3+='\n\n**Sjabloon.** Gebruik het tabblad K3\\_Proces\\_Data in A-ET\\_werkboek\\_instrumenten\\_2026-2027.xlsx.'
bp=block(t,'## 9. Bewijsplan','## 10.').replace('## 9. ','## ')
bp=bp.replace('**Sjabloon bewijsplan.**','**Sjabloon bewijsplan.** Gebruik het tabblad Bewijsplan in A-ET\\_werkboek\\_instrumenten\\_2026-2027.xlsx.')
md=f'''## Deze week

{leer}

**Planning en deadlines.**

{plan}

{tijd}

## Voorbereiding

{mod}

{kern}

{clips_md}

## Weekcheck

{wc}

## College 2 (donderdag 14 januari)

Een gastspreker vertelt over een echte casus, daarna stellen jullie je vragen. Daarna volgt een debat in Lagerhuisvorm over twee stellingen: de stelling uit de weekcheck, en een stelling uit de inzendingen van de groepen.

**Lever vóór dinsdag 12 januari, 23:59 met je groep in:** drie vragen voor de gastspreker en twee debatstellingen, elk met twee bronnen (zie week 1). Neem je standpunt uit de weekcheck mee naar het debat.

{verloop}

Het debat loopt door: vanaf week 3 opent elke online sessie met een stelling. Twee studenten verdedigen en bestrijden die, daarna volgt een peiling.

{k2}

{k3}

{bp}

{app}
'''
write('A-ET_Week02_studentversie.md',md)
docfile('docent_weekcheck_w02.md','# Week 2: antwoorden (alleen docent)\n\n'+block(t,'**Weekcheck week 2.**','**Logboekregel')+'\n\n## Tussenvragen in de clips\n\n'+'\n\n'.join(
  f'### {h}\n\n'+'\n\n'.join(q for q in re.findall(r'((?:^>.*\n?)+)',body(t,s,e),flags=re.M) if 'ussenvraag' in q)
  for h,s,e in [('Clip 6','### Clip 6.','### Clip 7.'),('Clip 7','### Clip 7.','### Clip 8.'),('Clip 8','### Clip 8.','## 4.')]))
