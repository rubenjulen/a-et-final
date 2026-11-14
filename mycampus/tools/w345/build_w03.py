import re,sys
sys.path.insert(0,'.')
from lib import *
t=load('03')
ov=sec(t,'## 1. Overzicht','## 2. Moduletekst')
ov=cut(ov,'**Checklist.**')  # drops checklist + reserve-stelling (both at end)
ov=drop_first_line(ov)
mod=sec(t,'## 2. Moduletekst','## 3. Kennisclips')
voor=sec(mod,'**Moduletekst.**','**Weekcheck week 3.**')
wc=sec(mod,'**Weekcheck week 3.**')
clips=sec(t,'## 3. Kennisclips','### Studietekst')
studie=sec(t,'### Studietekst','## 4. Practicum 2')
p2=sec(t,'## 4. Practicum 2','## 5. Practicum 3')
p3=sec(t,'## 5. Practicum 3','## 6. K4')
k4=sec(t,'## 6. K4','## 7. Online')
os_=sec(t,'## 7. Online','## 8. Antwoord')

# clip list
blocks=re.split(r'(?=^### (?:Clip|Kaderclip))',clips,flags=re.M)[1:]
lst=[]; bijl=[]
for b in blocks:
    head=b.splitlines()[0][4:]
    qs=[l for l in b.splitlines() if l.startswith('> **Tussenvraag')]
    lst.append(f'### {head}\n\nVideo: [link volgt op MyCampus]\n')
    if qs:
        lst.append('Vragen in de clip:\n\n'+'\n'.join('- '+strip_juist(q[2:]).replace('**','',0) for q in qs)+'\n')
    body='\n'.join(b.splitlines()[1:])
    bijl.append(f'### {head}\n\n'+strip_juist(strip_beeld(body)))
studie=promote(studie)
os_student=f'''## Online sessie donderdag 21 januari

Een uur, online, met opname; camera is optioneel.

| Tijd | Onderdeel |
| --- | --- |
| 0:00 tot 0:08 | Stelling: twee studenten verdedigen en bestrijden de stelling uit de weekcheck, daarna een peiling in de chat |
| 0:08 tot 0:25 | Wat lieten de practica zien, wat is anders bij generatieve AI, en wat toetst IEEE CertifAIEd? |
| 0:25 tot 0:50 | Wie draagt de fouten in jullie oplossing? Groepswerk in aparte kamers |
| 0:50 tot 1:00 | Vragen en uitleg snelle scan |

**Neem mee:** je eigen uitkomsten van practicum 2 (uit de weekcheck) en je standpunt over de stelling: *"Een bank mag een model gebruiken dat nauwkeuriger is dan medewerkers, ook als het één groep vaker onterecht afwijst."*

**Groepswerk.** Elke groep beantwoordt drie vragen voor de eigen oplossing. Welke gebruikers of betrokkenen lopen het risico dat de fouten bij hen terechtkomen? Hoe zou je dat kunnen meten of testen? Welke score krijgen domein 5 en 7 nu in jullie snelle scan, en waarop baseren jullie die? Groepen met een chatbot of agent nemen bij de eerste vraag ook de vier vragen uit de studietekst mee.
'''
wc_s=strip_juist(wc).replace('**Weekcheck week 3.**','')
md=f'''## Deze week

{ov}

## Voorbereiding

{voor.replace('**Moduletekst.**','')}

## Kennisclips

{chr(10).join(lst)}

{studie}

{renum(p2)}

{renum(p3)}

{renum(k4)}

{os_student}

## Weekcheck

Sluit woensdag 20 januari om 23:59.

{wc_s}

## Bijlage: tekst van de kennisclips (meelezen)

{chr(10).join(bijl)}
'''
md=md.replace('Gebruik de studietekst uit sectie 3','Gebruik de studietekst hierboven')
md=md.replace('**Kernbron: Rudin (2019).** Samenvatting voor de reader.','**Kernbron: Rudin (2019).** Samenvatting.')
open(MD+'A-ET_Week03_studentversie.md','w').write(clean(md))
# docent weekcheck
open(MD+'docent_weekcheck_w03.md','w').write('## Week 3: weekcheck met antwoorden\n\n'+wc.replace('**Weekcheck week 3.**','')+'\n')
print(clean(md)[:100]); print(len(md))
for l in md.splitlines():
    if re.search(r'[Dd]ocent|Juist|sectie \d|draaiboek|[Aa]ntwoordmodel',l): print('CHECK>',l[:180])
