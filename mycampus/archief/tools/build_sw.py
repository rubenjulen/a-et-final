import sys,re
sys.path.insert(0,'/tmp/claude-0/-home-user-menssana/175e1d50-6875-5f56-acf6-23260f0c6b9a/scratchpad/mycampus/tools')
from mdlib import *
D='/tmp/claude-0/-home-user-menssana/175e1d50-6875-5f56-acf6-23260f0c6b9a/scratchpad/mycampus/md/'
t=open(D+'raw_lesplan.md').read()
R=[
("De taakverdeling, het gastcollege en het juridisch kader stem ik af met de docenten van A-AI2 en A-DG (sectie 12).",""),
("Ik gebruik de vijf als toets of de module dekkend is; de [kruistabel](https://claude.ai/artifact/JoNqBfntw1E1JuiCBfpK8n) laat per examenonderdeel zien waar het in de module zit. Studenten leren ze kennen in vijf kaderclips; de module is geen examentraining.",
 "De docent gebruikt de vijf als toets of de module dekkend is. Je leert ze kennen in vijf kaderclips (A tot en met E). De module is geen examentraining, maar wie verder wil, vindt in week 10 een overzicht van de certificeringen."),
("Privacy en de AVG behandelt A-DG; ik stem met A-DG af dat beide vakken hetzelfde kader hanteren.","Privacy en de AVG behandelt A-DG; beide vakken gebruiken hetzelfde kader."),
("&#91;embedded content: fasering · week 0 tot 10, colleges, online sessies, practica en toetsen\\]\n",""),
]
for a,b in R:
    assert a in t,a[:50]; t=t.replace(a,b)
secs=dict(sections(t,2))
def S(k):
    for h,b in sections(t,2):
        if h.startswith(k): return h,b
    raise KeyError(k)
parts=[]
intro="""Deze studiewijzer beschrijft de module AI & Ethics (A-ET) van januari tot en met maart 2027: wat je leert, hoe de weken zijn opgebouwd, met welke instrumenten je werkt, hoe je begeleid wordt en hoe je wordt beoordeeld. Alle weekmodules, sjablonen en bestanden vind je op MyCampus.

"""
parts.append(intro)
for k in ['1. Uitgangspunten','2. Opzet en werkwijze','3. Methodiek','4. Instrumenten','5. Weekoverzicht','6. Planning per week','7. AI-practica','8. Begeleiding','9. Toetsing','10. Studielast']:
    h,b=S(k)
    if k.startswith('10.'):
        b=re.sub(r'De online sessies staan hier onder huiswerk.*?verandert alleen de indeling, niet de totale studielast\. ','',b,flags=re.S)
    if k.startswith('9.'):
        b=b.replace('De volledige rubric ontvangen studenten in week 1.','De volledige rubric staat in A-ET\\_Beoordelingsrubric\\_studenten.pdf en in de modules van week 5 en week 8.')
    parts.append(f'## {h}\n{b}')
parts.append("""## 11. AI-gebruik en AI-verklaring

Je mag generatieve AI gebruiken, bijvoorbeeld om te brainstormen, teksten te verbeteren of code uit te leggen, mits je dat verantwoordt. Bij elke inlevering hoort een korte AI-verklaring: welke tool je gebruikte, waarvoor, wat je zelf hebt gecontroleerd, en wat je bewust niet met AI deed. Gebruik het formulier AI-verklaring.docx. Zet nooit echte persoonsgegevens of vertrouwelijke gegevens van de partner in een AI-tool. Ontbreekt de AI-verklaring, dan wordt het werk pas beoordeeld als die binnen is.

## 12. Materiaal op MyCampus

| Wat | Bestand |
| --- | --- |
| Weekmodules 0 tot en met 10 | A-ET\\_Week00\\_studentversie.pdf tot en met A-ET\\_Week10\\_studentversie.pdf |
| Werkboek met de instrumenten | A-ET\\_werkboek\\_instrumenten\\_2026-2027.xlsx |
| Word-sjablonen | K1-canvas, K5-dilemmacanvas, sjabloon tussenrapport (A1), sjabloon eindrapport (A2), sjabloon reflectie, AI-verklaring |
| Beoordelingsrubric | A-ET\\_Beoordelingsrubric\\_studenten.pdf |
| Voorbeeldrapport | Voorbeeldrapport\\_ClaimWacht\\_A-ET\\_2026-2027.pdf |
| Casusdossier Suribank | A-ET\\_Casusdossier\\_Suribank.pdf |
| Practica | Notebooks, Orange-workflows en datasets per week |

""")
h,b=S('Bronnen'); 
b=b.replace('- A-ET Vakbeschrijving 2026-2027\n','')
parts.append(f'## Bronnen\n{b}')
out=''.join(parts)
# drop first-level title and byline if present
out=re.sub(r'^\s*#\s.*\n','',out)
open(D+'A-ET_Studiewijzer_2026-2027.md','w').write(clean(out))
print('ok')
