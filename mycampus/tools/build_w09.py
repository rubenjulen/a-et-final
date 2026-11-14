import sys,re
sys.path.insert(0,'/tmp/claude-0/-home-user-menssana/175e1d50-6875-5f56-acf6-23260f0c6b9a/scratchpad/mycampus/tools')
from mdlib import *
D='/tmp/claude-0/-home-user-menssana/175e1d50-6875-5f56-acf6-23260f0c6b9a/scratchpad/mycampus/md/'
t=open(D+'raw_w09.md').read()
s1=get(t,'1. Overzicht')
leer=s1[s1.index('**Leerdoelen.**'):s1.index('**Planning')]
plan=s1[s1.index('**Planning'):s1.index('**Tijdsbesteding')]
tijd=s1[s1.index('**Tijdsbesteding'):s1.index('**Checklist')]
s2=get(t,'2. Moduletekst')
modul=s2[s2.index('> **Week 9'):s2.index('### Weekcheck 9')]
modul=unquote(modul).replace('**Week 9: van ontwerp naar besluit**','### Week 9: van ontwerp naar besluit')
wc=s2[s2.index('### Weekcheck 9')+len('### Weekcheck 9'):]
wc=strip_answers(wc)
s3=get(t,'3. Kennisclips')
c21=get(s3,'Clip 21',3); c22=get(s3,'Clip 22',3)
def doel(b): 
    m=re.search(r'\*\*Doel\.\*\* (.+)',b); return m.group(1) if m else ''
s4=get(t,'4. Practicum 4b')
s4=s4[:s4.index('**Docent.**')]
s5=get(t,'5. K8'); s6=get(t,'6. Het beslismemo'); s7=get(t,'7. Practicum 5'); s9=get(t,'9. Laatste peercheck')
out=f"""## Deze week

{leer}
{plan.replace('**Planning en deadlines**','### Planning en deadlines')}
{tijd.replace('**Tijdsbesteding voor de student**','### Tijdsbesteding')}
## Voorbereiding

{modul}
## Kennisclips

Samen 15 minuten. Ze bouwen voort op het minicollege van college 3. De tekst van de clips staat achteraan om mee te lezen.

### Clip 21: Monitoren met grenzen en acties (8 minuten)

**Doel.** {doel(c21)}

Video: [link volgt op MyCampus]

### Clip 22: Het beslismemo (7 minuten)

**Doel.** {doel(c22)}

Video: [link volgt op MyCampus]

## Practicum 4b: de hertest
{drop_markers(s4)}
## K8: implementatie- en monitoringplan
{drop_markers(s5)}
Werk K8 uit in het werkboek A-ET\\_werkboek\\_instrumenten\\_2026-2027.xlsx, tabblad K8\\_Monitoring (delen A tot en met D) en tabblad Hertest.

## Het beslismemo
{drop_markers(s6)}
Gebruik het sjabloon voor het eindrapport (Sjabloon\\_eindrapport\\_A2.docx); het beslismemo staat daar vooraan.

## Practicum 5 (optioneel): het model een jaar later
{s7.replace('*Studententekst. ','*')}
## Weekcheck 9
{wc}
## Online sessie donderdag 4 maart: monitoring en het beslismemo

60 minuten, opgenomen. De sessie opent met de stelling: *"Als de hertest niet beter uitpakt dan de eerste test, mag de oplossing niet live."* Twee studenten verdedigen en bestrijden de stelling, daarna volgt een peiling. Bereid je standpunt voor (zie de weekcheck).

Neem het concept van jullie beslismemo mee. In een breakout lezen twee groepen elkaar de eerste drie zinnen van hun memo voor, met de uitkomst van de hertest, en stelt de andere groep als directeur drie vragen: wat moet ik nu doen, wat kost het, en wat gebeurt er als het niet lukt? Denk ook na over jullie incidentroute en stopcriterium (K8, deel D).

## Laatste peercheck: zondag 7 en maandag 8 maart
{s9}
## Bijlage: tekst van de kennisclips (meelezen)

### Clip 21: Monitoren met grenzen en acties

{clip_transcript(c21)}

### Clip 22: Het beslismemo

{clip_transcript(c22)}
"""
open(D+'A-ET_Week09_studentversie.md','w').write(clean(out))
print(len(out))
