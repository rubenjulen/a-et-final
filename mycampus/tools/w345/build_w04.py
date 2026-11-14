import re,sys
sys.path.insert(0,'.')
from lib import *
t=load('04')
ov=drop_first_line(cut(sec(t,'## 1. Overzicht','## 2. Moduletekst'),'**Checklist.**'))
mod=sec(t,'## 2. Moduletekst','### Weekcheck 4')
voor=mod.split('\n',1)[1].replace('Deze tekst staat op maandag 25 januari in de leeromgeving.','')
wc=sec(t,'### Weekcheck 4','## 3. Kennisclips')
wc_doc=wc
wc=cut(wc,'Docent: lees de logboekregels')
wc_s=strip_feedback_lines(strip_bold_options(wc)).replace('### Weekcheck 4','')
wc_s=wc_s.replace('uit sectie 5','uit de praktijkcasussen')
clips=sec(t,'## 3. Kennisclips','## 4. K4')
blocks=re.split(r'(?=^### (?:Clip|Kaderclip))',clips,flags=re.M)[1:]
lst=[];bijl=[]
for b in blocks:
    head=b.splitlines()[0][4:]
    body='\n'.join(b.splitlines()[1:])
    qpart=''
    if '**Vragen in de clip**' in body:
        body,qpart=body.split('**Vragen in de clip**',1)
    doel=re.search(r'\*\*Doel\.\*\*[^\n]*',body)
    lst.append(f'### {head}\n\n'+(doel.group(0)+'\n\n' if doel else '')+'Video: [link volgt op MyCampus]\n')
    if qpart.strip():
        qs=strip_juist(qpart.strip())
        lst.append('Vragen in de clip:\n\n'+qs+'\n')
    body2=re.sub(r'\*\*Doel\.\*\*[^\n]*\n','',body)
    bijl.append(f'### {head}\n\n'+table_clip_text(body2))
k4=renum(sec(t,'## 4. K4','## 5. Praktijk'))
pk=sec(t,'## 5. Praktijk','## 6. Practicum 4')
pk=cut(pk,'### Docent: wat je wilt horen')
pk=re.sub(r'\*\*Zo zet je het in\.\*\*[^\n]*',
 '**Zo gebruik je de casussen.** Kijk vóór de online sessie de NOS-video over de toeslagenaffaire en lees één korte casus die past bij jullie variant (samen 20 minuten). De stelling van de online sessie gaat over de MyCity-chatbot. In practicum 4 voegt elke groep minstens één vraag of paar toe dat uit een casus komt (ID X01 in het testlogboek). In K6 mag een casus dienen als "vergelijkbaar geval" om een kans te onderbouwen.',pk)
pk=renum(pk)
p4=sec(t,'## 6. Practicum 4','## 7. K5')
p4=re.sub(r'\n\*\*Docent\.\*\*[^\n]*\n','\n',p4)
p4=renum(p4)
k5=renum(sec(t,'## 7. K5','## 8. K6'))
k6=renum(sec(t,'## 8. K6','## 9. Online'))
peer=sec(t,'## 10. Peercheck','## 11. Antwoordmodel')
peer=re.sub(r'\n\*\*Docent:\*\*[^\n]*\n?','\n',peer)
peer=renum(peer)
os_s='''## Online sessie donderdag 28 januari: van dilemma naar risico

60 minuten, met opname.

| Tijd | Onderdeel |
| --- | --- |
| 0:00 | Stelling: twee studenten verdedigen en bestrijden de stelling, daarna een poll |
| 0:06 | Sorteeroefening: is een uitspraak een dilemma, een risico of een maturity gap? |
| 0:09 | Samen uitwerken: van een dilemma naar een risico in het Risk Register |
| 0:14 | De AI-verordening: in welke risicoklasse valt een toepassing, en welke rol heeft de partner? |
| 0:20 | Breakout-groepen: je presenteert je eigen dilemma |
| 0:45 | Vragen over Assessment 1 |

**Stelling.** *"Een organisatie mag een chatbot inzetten die soms een fout antwoord geeft, zolang ze dat vooraf meldt."*

**Neem mee:** je eigen dilemma, met de beslisvraag, waarde A en B, en je voorlopige oordeel. Groepen noemen in de chat hun eigen EU-risicoklasse en de rol van hun partner, met één zin onderbouwing.

**Breakout-groepen.** In groepen van 3 of 4, elk uit een andere projectgroep. Per student 6 minuten:

1. **3 minuten:** je presenteert je eigen dilemma: beslisvraag, waarde A en B, en het voorlopige oordeel.
2. **3 minuten:** de anderen reageren met twee vaste vragen:
   - *Welke lens heb je nog niet goed gebruikt?*
   - *Welke derde optie zie je over het hoofd?*

Je noteert de feedback die je krijgt.

**Niet aanwezig?** Kijk de opname en stuur je dilemma (beslisvraag en voorlopig oordeel, hoogstens 100 woorden) vóór zaterdag 30 januari naar een lid van je peergroep.
'''
files='''**Bestanden in de leeromgeving.** practicum4\\_testlogboek.xlsx, practicum4\\_suribank.ows, practicum4\\_paren.ipynb en suribank\\_paren.csv (bij de bestanden uit practicum 2), en het werkboek A-ET\\_werkboek\\_instrumenten\\_2026-2027.xlsx.'''
md=f'''## Deze week

{ov}

{files}

## Voorbereiding

{voor}

## Kennisclips

{chr(10).join(lst)}

{pk}

{p4}

{k4}

{k5}

{k6}

{os_s}

{peer}

## Weekcheck

{wc_s}

## Bijlage: tekst van de kennisclips (meelezen)

{chr(10).join(bijl)}
'''
md=md.replace('De Excel-tool Ethical Dilemma & AI Risk Assessment heeft een tabblad voor elk instrument, met een uitgewerkt voorbeeld.','Het werkboek A-ET\\_werkboek\\_instrumenten\\_2026-2027.xlsx heeft een tabblad voor elk instrument, met een voorbeeldrij.')
md=md.replace('(uit de Excel-tool)','(voorbeeld)').replace('van de Excel-tool','van het werkboek').replace('in de Excel-tool','in het werkboek').replace('de Excel-tool','het werkboek')
open(MD+'A-ET_Week04_studentversie.md','w').write(clean(md))
open(MD+'docent_weekcheck_w04.md','w').write('## Week 4: weekcheck met antwoorden\n\n'+wc_doc.replace('### Weekcheck 4','')+'\n')
print(len(md))
for l in md.splitlines():
    if re.search(r'[Dd]ocent|Juist|sectie \d|draaiboek|[Aa]ntwoordmodel|Excel-tool|Antwoord:|Feedback:|\*\*[a-d]\.|^- [a-d]\. \*\*|studenten ',l): print('CHECK>',l[:200])
