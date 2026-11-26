import re,sys
sys.path.insert(0,'.')
from lib import *
t=load('05')
ov=drop_first_line(cut(sec(t,'## 1. Overzicht','## 2. Moduletekst'),'**Checklist**'))
ov=ov.replace('| Vrijdag 5 tot en met woensdag 10 februari | Beoordelen, met kalibratie op twee rapporten |','| Vrijdag 5 tot en met woensdag 10 februari | De docent beoordeelt |')
mod=sec(t,'## 2. Moduletekst','### Clip 14')
voor=mod.split('\n',1)[1].replace('Deze tekst staat op maandag 1 februari in de leeromgeving, onder het feedforward-bericht uit week 4.','')
clip=sec(t,'### Clip 14','### Weekcheck 5')
wc=sec(t,'### Weekcheck 5','## 3. Assessment')
wc_s=strip_feedback_lines(strip_bold_options(wc)).replace('### Weekcheck 5','')
head=clip.splitlines()[0][4:]
lst=f'### {head}\n\nVideo: [link volgt op MyCampus]\n'
bijl=f'### {head}\n\n'+table_clip_text('\n'.join(clip.splitlines()[1:]))
a1=sec(t,'## 3. Assessment','## 4. Assessment')
a1=a1.replace('*Deze opdracht staat sinds week 1 in de leeromgeving. Dit is de volledige tekst voor studenten.*','')
ind=sec(t,'## 4. Assessment','## 5. Rubric')
ind=ind.replace('*Studententekst, staat sinds week 1 in de leeromgeving.*','')
r1=sec(t,'## 5. Rubric','## 6. Rubric')
r1=r1.replace('Schrijf per criterium twee zinnen: wat goed is, en wat in Assessment 2 beter moet. Gebruik daarvoor het feedbackformulier in sectie 9. De feedback is gericht op het vervolg: elk hoofdstuk komt in Assessment 2 herzien terug.',
 'Je krijgt per criterium twee zinnen feedback: wat goed is, en wat in Assessment 2 beter moet. De feedback is gericht op het vervolg: elk hoofdstuk komt in Assessment 2 herzien terug.')
r2=sec(t,'## 6. Rubric','## 7. Hoofdstuk')
peer=sec(t,'## 7. Hoofdstuk','## 8. Online')
peer=re.sub(r'\n\*Afstemmen met Janssen[^\n]*\n','\n',peer)
faq=sec(t,'### Veelgestelde vragen en antwoorden','## 9. Inleveren')
faq=faq.replace('Plaats deze lijst na het vragenuur in de leeromgeving en vul hem aan.','Deze lijst wordt na het vragenuur aangevuld.')
inl=sec(t,'## 9. Inleveren','## 10. Docentnotitie')
inl=cut(inl,'### Beoordelen','### Teruggave en feedbackgesprek')
inl=re.sub(r'\n\*Voorstel, af te stemmen[^\n]*\n','\n',inl)
inl=inl.replace(' (zie sectie 11)','')
inl=inl.replace('*De data en vorm moeten nog met Janssen worden afgesproken.*','De data en de vorm van de herkansing volgen via MyCampus.')
inl=inl.replace('## 9. Inleveren, beoordelen en feedback','## Inleveren en feedback')
vu=f'''## Online vragenuur dinsdag 2 februari

60 minuten, met opname. Het doel: elke groep gaat weg met één concrete verbetering voor donderdag.

| Tijd | Onderdeel |
| --- | --- |
| 0:00 | Stelling: twee studenten verdedigen en bestrijden de stelling, daarna een peiling |
| 0:06 | Wat er donderdag in moet, waar en hoe laat |
| 0:09 | De drie meest gestelde vragen |
| 0:15 | Zo leest de docent: twee geanonimiseerde fragmenten naast de rubric. Jij typt in de chat welk niveau je zou geven |
| 0:27 | Inlevercheck in je eigen groep: kies de één verbetering met het meeste effect |
| 0:47 | Elke groep noemt zijn verbetering; open vragen |
| 0:57 | Afsluiting |

**Stelling.** *"Als de mensen om wie het gaat niet zijn gehoord, is een AI-oplossing niet verantwoord, hoe goed die ook werkt."*

**Neem mee:** je eigen concept en de inlevercheck. Vragen kun je vooraf sturen. Na het vragenuur kun je nog vragen stellen tot woensdag 18:00; op donderdag worden geen inhoudelijke vragen meer beantwoord.

{promote(faq)}
'''
md=f'''## Deze week

{ov}

## Voorbereiding

{voor}

## Kennisclip

{lst}

{renum(a1)}

{renum(ind)}

{renum(r1)}

{renum(r2)}

{renum(peer)}

{vu}

{renum(inl)}

## Weekcheck

{wc_s}

## Bijlage: tekst van de kennisclip (meelezen)

{bijl}
'''
md=md.replace('de inlevercheck uit sectie 3','de inlevercheck bij het groepsdeel').replace('Export van de Excel-tool','Export van het werkboek').replace('met de kwaliteitscriteria uit de Excel-tool','met de kwaliteitscriteria van het canvas').replace('de Excel-tool','het werkboek')
open(MD+'A-ET_Week05_studentversie.md','w').write(clean(md))
open(MD+'docent_weekcheck_w05.md','w').write('## Week 5: weekcheck met antwoorden (vetgedrukt = juist)\n\n'+wc.replace('### Weekcheck 5','')+'\n')
print(len(md))
for l in md.splitlines():
    if re.search(r'Juist|sectie \d|draaiboek|[Aa]ntwoordmodel|Excel-tool|Antwoord:|Feedback:|^- [a-d]\. \*\*|Janssen|kalibratie|benchmark',l): print('CHECK>',l[:200])
