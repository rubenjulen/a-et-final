import sys,re
sys.path.insert(0,'/tmp/claude-0/-home-user-menssana/175e1d50-6875-5f56-acf6-23260f0c6b9a/scratchpad/mycampus/tools')
from mdlib import *
D='/tmp/claude-0/-home-user-menssana/175e1d50-6875-5f56-acf6-23260f0c6b9a/scratchpad/mycampus/md/'
t=open(D+'raw_w10.md').read()
s1=get(t,'1. Overzicht')
tijd=s1[s1.index('**Tijdsbesteding voor de student**'):s1.index('**Tijdsbesteding voor de docent')]
tijd=tijd.replace('**Tijdsbesteding voor de student**','### Tijdsbesteding')
s2=get(t,'2. Moduletekst')
modul=unquote(s2[s2.index('> **Week 10'):s2.index('### Laatste weekcheck')]).replace('**Week 10: de laatste stap**','### Week 10: de laatste stap')
wc=s2[s2.index('### Laatste weekcheck')+len('### Laatste weekcheck'):]
wc=re.sub(r'\n\*Docent:.*?\*\n','\n',wc)
wc=wc.replace('Link naar de evaluatie (sectie 8), anoniem','Link volgt op MyCampus; anoniem')
s3=get(t,'3. Online vragenuur')
alinea=get(s3,"Twee voorbeeldalinea",3)
faq=get(s3,'Veelgestelde vragen',3).replace('Na het vragenuur in de leeromgeving plaatsen en aanvullen.','Deze lijst wordt na het vragenuur aangevuld.')
s4=get(t,'4. Inleveren')
regels=get(s4,'Regels',3)
regels=regels.replace(' *Voorstel, af te stemmen met de onderwijs- en examenregeling van Janssen.*','')
regels=regels.replace('Dezelfde regels als bij Assessment 1 (week 5, sectie 9), met aangepaste data.','Dezelfde regels als bij Assessment 1, met aangepaste data.')
regels=regels.replace('hetzelfde formulier als bij Assessment 1 (week 5, sectie 7)','hetzelfde formulier als bij Assessment 1')
s6=get(t,'6. Eindcijfer')
form=get(s6,'De formules',3)
form=form.replace(' *Controleer de afrondingsregel in de onderwijs- en examenregeling van Janssen.*','')
s8=get(t,'8. Afsluiting')
verder=get(s8,'Verder na de minor',3).replace('Plaats dit blok in de leeromgeving bij het bericht over de cijfers. ','')
toest=get(s8,'Toestemming voor voorbeeldmateriaal',3).replace('Apart van de anonieme evaluatie, per groep: ','Apart van de anonieme evaluatie vraagt de docent per groep: ')
out=f"""## Deze week

Geen nieuwe stof. Deze week ronden jullie het eindrapport en je reflectie af en leveren jullie Assessment 2 in.

### Planning

| Moment | Wat |
| --- | --- |
| Maandag 8 maart | Weekmodule 10 opent met feedforward; peerfeedback uiterlijk 23:59 |
| Dinsdag 9 maart | Online vragenuur over het eindrapport en de reflectie |
| Woensdag 10 maart, 18:00 | Laatste moment voor vragen en voor het aanvragen van uitstel |
| Woensdag 10 maart, 23:59 | Laatste weekcheck: logboekregel, laatste standpunt en de module-evaluatie |
| Donderdag 11 maart, 23:59 | Inleveren Assessment 2: eindrapport, reflectie, AI-verklaring, peerbeoordeling |
| Uiterlijk vrijdag 26 maart | Cijfers en feedback (datum onder voorbehoud) |
| Na 26 maart | Herkansing volgens de onderwijs- en examenregeling |

{tijd}
## Voorbereiding

{modul}
## Laatste weekcheck
{wc}
## Online vragenuur dinsdag 9 maart

60 minuten, opgenomen. Het vragenuur opent met de stelling van de week: *"Een AI-oplossing die nu niet verantwoord is, mag toch live als de organisatie belooft het binnen een jaar te verbeteren."* Stuur je vraag gerust vooraf in. Daarna laat de docent zien hoe een beslismemo en een reflectie worden gelezen, en loop je in een breakout het memo naast hoofdstuk 12 en je eigen reflectie langs de criteria.

### Twee voorbeeldalinea's voor de reflectie (criterium B: een onjuiste aanname)
{alinea}
### Veelgestelde vragen en antwoorden
{faq}
## Inleveren Assessment 2: donderdag 11 maart
{regels}
De beoordelingsrubric staat in de week 8-module en in de studiewijzer. Je krijgt je cijfer en feedback uiterlijk vrijdag 26 maart (datum onder voorbehoud). Wil je je beoordeling bespreken, dan kun je binnen tien werkdagen een inzagegesprek van 15 minuten aanvragen. Bezwaar tegen een cijfer verloopt via de procedure van Janssen.

## Zo wordt je eindcijfer berekend
{form}
## Module-evaluatie

Anoniem, ongeveer tien minuten, open van woensdag 10 tot en met zondag 14 maart. De link volgt op MyCampus. Je antwoorden helpen de volgende groep studenten.

### Toestemming voor voorbeeldmateriaal

{toest.strip()}

## Verder na de minor
{verder}"""
open(D+'A-ET_Week10_studentversie.md','w').write(clean(out))
print('ok')
