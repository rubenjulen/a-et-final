#!/usr/bin/env python3
"""Kennischecks 1 tot en met 3 voor A-ET (herontwerp: drie colleges, vier blokken).

Eén bron voor:
  1. de docentversie met antwoorden en feedback (markdown, daarna pdf via mycampus/tools/render.js);
  2. een invoerbestand (xlsx) om de vragen in MyCampus te zetten;
  3. een GIFT-bestand (gangbaar importformaat voor quizzen in een leeromgeving).
Kennischeck 3 bevat ook de 12 vragen van de beginquiz (bron: mycampus/md/docent_weekcheck_w00.md).
Gebruik: python3 scripts/gen_kennischecks.py   (vanuit de repository)
"""
import os
import re
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MD = os.path.join(REPO, 'mycampus', 'md', 'DOCENT_kennischecks.md')
XLSX = os.path.join(REPO, 'lesmateriaal', 'docent', 'ICT A-ET Kennischecks invoer.xlsx')
GIFT = os.path.join(REPO, 'lesmateriaal', 'docent', 'ICT A-ET Kennischecks GIFT.txt')

# (vraag, [opties], juiste letter, feedback, lees na)
KC = {
 1: dict(titel='Kennischeck 1 · Blok 1 Analyseren', deadline='woensdag 3 februari 2027, 23:59',
  stelling='Als de mensen om wie het gaat niet zijn gehoord, is een AI-oplossing niet verantwoord, hoe goed die ook werkt.',
  oefen=['Organisaties in Suriname moeten wachten met AI voor beslissingen over mensen totdat er een privacywet is.',
         'Een organisatie mag een chatbot namens een medewerker laten antwoorden, zolang de klant geen verschil merkt.',
         'Een bank mag een model gebruiken dat nauwkeuriger is dan medewerkers, ook als het één groep vaker onterecht afwijst.'],
  vragen=[
  ('Het fraudemodel van Rotterdam werkte matig, was jarenlang toegestaan, en jonge moeders en mensen die slecht Nederlands spreken scoorden vaker hoog. Welke vraag ging hier vooral mis?',
   ['Werkt het?', 'Mag het?', 'Is het verantwoord?'], 'C',
   'Het systeem mocht en werkte min of meer, maar legde de lasten bij groepen die zich slecht kunnen verweren. Een systeem kan werken en toegestaan zijn, en toch niet verantwoord.',
   'De kern: werkt het, mag het, is het verantwoord?'),
  ('Een organisatie voldoet aan alle wetten en aan haar eigen beleid. Wat volgt daaruit?',
   ['Ze handelt verantwoord.', 'Ze haalt de ondergrens; of het verantwoord is, vraagt een eigen ethische afweging.', 'Er spelen geen ethische vragen meer.'], 'B',
   'Compliance is de ondergrens, niet het doel. Regels lopen vaak achter, en in Suriname is er voor AI weinig om compliant mee te zijn.',
   'De kern: recht, compliance en ethiek'),
  ('Een systeem helpt 95% van de gebruikers en benadeelt 5% ernstig. Welk kader rekent dit het snelst goed, en wat is daarvan de zwakte?',
   ['Utilitarisme (gevolgen): kleine groepen worden weggemiddeld.', 'Deontologie (plichten): regels kunnen botsen.', 'Zorgethiek: moeilijk op grote schaal.'], 'A',
   'Een gevolgenafweging telt baten en schade op. Daardoor kan ernstige schade voor een kleine groep verdwijnen in het gemiddelde.',
   'De kern: vijf theorieën, sterk en zwak'),
  ('Wat bedoelt Rawls met de sluier van onwetendheid?',
   ['Je kiest de regels zonder te weten welke plek je zelf krijgt.', 'Je laat gevoelige kenmerken uit de data weg.', 'Je beslist zonder de gevolgen te kennen.'], 'A',
   'Wie niet weet of hij aan de kust of in het binnenland woont, kiest regels die ook voor de zwakste positie aanvaardbaar zijn.',
   'De kern: vier ethische lenzen'),
  ('Welke risicoformulering is professioneel (K6)?',
   ['Het model kan bias hebben.', 'Aanvragers uit het binnenland lopen meer kans op een onterechte afwijzing, omdat informeel inkomen vaker ontbreekt; onder SRD 50.000 kijkt geen mens mee.', 'Er is geen bezwaarroute.'], 'B',
   'Een risico noemt oorzaak, gebeurtenis, schade en voor wie. "Er is geen bezwaarroute" is een gap uit de nulmeting, nog geen risico.',
   'Instrumenten: K6 risicoregister'),
  ('Bij Suribank ontbreken afgewezen aanvragers in de trainingsdata: je weet niet of zij hadden terugbetaald. Welke bias is dit?',
   ['Labelbias', 'Interactiebias', 'Inzetbias'], 'A',
   'Het label (terugbetaald of niet) bestaat alleen voor wie een lening kreeg. Het model leert dus van een voorselectie.',
   'De kern: bias, waar komt het vandaan?'),
  ('De bank haalt district uit het model. Is het verschil tussen binnenland en kust dan weg?',
   ['Ja, het model ziet het district niet meer.', 'Nee, inkomen en soort werk hangen samen met district en werken als proxy.', 'Ja, als je ook de naam weglaat.'], 'B',
   'Een gevoelig kenmerk weglaten haalt het patroon niet weg. Je moet de uitkomsten per groep blijven meten.',
   'De kern: fouten per groep en eerlijkheid (proxy)'),
  ('Waarom kan een model niet tegelijk gelijke kalibratie, gelijke fouten en gelijke uitkomst halen?',
   ['Omdat modellen altijd bevooroordeeld zijn.', 'Als het terugbetaalcijfer tussen groepen verschilt, sluiten die definities elkaar uit, behalve bij een perfect model.', 'Omdat de wet dat verbiedt.'], 'B',
   'Dit is het onmogelijkheidsresultaat (Kleinberg e.a., Chouldechova). Je moet kiezen welke eerlijkheid telt, en die keuze uitleggen.',
   'De kern: waarom perfecte eerlijkheid niet bestaat'),
  ('Robert Williams werd in 2020 gearresteerd na een foute match van gezichtsherkenning. Wat is de les?',
   ['Een match is bewijs.', 'Een match is een kans; zonder ander bewijs en echte menselijke controle leidt hij tot onrecht.', 'Gezichtsherkenning werkt alleen slecht bij weinig licht.'], 'B',
   'De agenten behandelden de match als bewijs (automation bias). Gezichtsherkenning maakt bovendien vaker fouten bij mensen met een donkere huidskleur (Gender Shades, NIST).',
   'Praktijkvoorbeelden: Robert Williams'),
  ('Wanneer is een black box het minst aanvaardbaar?',
   ['Bij muziekaanbevelingen.', 'Bij een eindbeslissing over krediet, zonder mens en zonder bezwaarmogelijkheid.', 'Bij een spamfilter waartegen je bezwaar kunt maken.'], 'B',
   'Hoe groter de impact op iemands leven, hoe zwaarder de eis aan uitleg. Een eindbeslissing zonder mens en zonder bezwaar hoort niet in een black box.',
   'De kern: uitleg, de black box openen'),
 ]),
 2: dict(titel='Kennischeck 2 · Blok 2 Ontwerpen', deadline='woensdag 24 februari 2027, 23:59',
  stelling='Een maatregel die groepen gelijker behandelt maar de nauwkeurigheid verlaagt, is altijd de betere keuze.',
  oefen=['Een chatbot hoeft niet te melden dat hij AI is, zolang de antwoorden kloppen.',
         'Een AI-oplossing is pas verantwoord als iemand van buiten de organisatie het ontwerp heeft beoordeeld.'],
  vragen=[
  ('Welke eis is toetsbaar?',
   ['Het model moet eerlijk zijn.', 'Het verschil in onterecht afwijzen tussen binnenland en kust is kleiner dan 5 procentpunt, gemeten per kwartaal.', 'We letten goed op bias.'], 'B',
   'Een toetsbare eis noemt wat je meet, de grens en wanneer je meet. Dan kun je later zeggen of de maatregel werkt.',
   'Instrumenten: K7 deel 1, van risico naar eis'),
  ('Een maandelijkse meting van fouten per regio is vooral een maatregel die …',
   ['voorkomt', 'opspoort', 'herstelt'], 'B',
   'Meten voorkomt de fout niet en herstelt hem niet, maar laat hem zien. Een goed ontwerp combineert voorkomen, opsporen en herstellen.',
   'De kern: maatregelen ontwerpen'),
  ('Wat is restrisico?',
   ['Het risico vóór de maatregelen.', 'Wat na de maatregelen overblijft, met wie dat accepteert.', 'Een risico dat je bewust weglaat.'], 'B',
   'Restrisico verdwijnt niet door het niet te noemen. Iemand met bevoegdheid moet het bewust accepteren, en dat staat in het rapport.',
   'De kern: maatregelen ontwerpen, en wat overblijft'),
  ('Medewerkers krijgen 15 minuten per dossier en mogen alleen met schriftelijk akkoord afwijken. Welke voorwaarden voor menselijke controle ontbreken vooral?',
   ['Informatie en kennis', 'Tijd, bevoegdheid en cultuur', 'Alleen registratie'], 'B',
   'Als afwijken veel kost en meegaan niets, wordt de mens een stempel. Dan is er een mens in het proces, maar geen controle.',
   'De kern: menselijke controle die werkt'),
  ('Wat is automation bias?',
   ['De neiging om het advies van een systeem te volgen, ook als het fout is.', 'Bias in de data van geautomatiseerde systemen.', 'Wantrouwen tegenover elke vorm van automatisering.'], 'A',
   'Automation bias geeft fouten door weglaten (je ziet de fout niet) en door doen (je volgt een fout advies). Het staat letterlijk in de AI-verordening, art. 14.',
   'De kern: menselijke controle die werkt'),
  ('Welke bezwaarroute is het sterkst?',
   ['Alleen een online formulier.', 'Bekend, laagdrempelig (ook aan de balie of telefonisch), beoordeeld door iemand die niet zelf besliste, en met herstel.', 'Bezwaar maken bij de leverancier van het model.'], 'B',
   'Een bezwaarroute werkt alleen als de getroffene hem kent, kan gebruiken, en als een fout ook echt wordt hersteld.',
   'De kern: bezwaar en herstel'),
  ('Wat betekent "precies één A per activiteit" in een RACI?',
   ['Eén persoon is eindverantwoordelijk en aanspreekbaar.', 'Eén persoon voert het werk uit.', 'Iedereen wordt geïnformeerd.'], 'A',
   'De A (accountable) beslist en legt verantwoording af. Twee A\'s betekent in de praktijk: niemand.',
   'Instrumenten: K7 deel 2c, RACI'),
  ('Jullie chatbot gebruikt een taalmodel van een buitenlandse aanbieder. Welke vraag hoort in de leverancierscheck?',
   ['Traint de aanbieder met onze gegevens, en waar worden ze bewaard?', 'Hoeveel parameters heeft het model?', 'Welke kleur heeft de chatknop?'], 'A',
   'De organisatie blijft verantwoordelijk voor wat de chatbot doet, ook als het model van een ander is. De leverancierscheck legt vast wat je wel en niet in de hand hebt.',
   'Instrumenten: leverancierscheck'),
  ('Wat leert de toeslagenaffaire over de schade van AI?',
   ['Het lag alleen aan het model.', 'De schade ontstond door een samenspel van model, beleid, menselijke controle die niet werkte en geen bezwaar.', 'Het lag alleen aan de medewerkers.'], 'B',
   'Wie alleen naar het model kijkt, mist de oorzaak. Daarom ontwerp je in H6 en H7 ook controle, bezwaar en governance.',
   'Kerncasus: de toeslagenaffaire'),
  ('Wat voegt ISO/IEC 42001 toe aan losse maatregelen?',
   ['Een managementsysteem: plannen, doen, controleren en verbeteren, met rollen en een vast moment om terug te kijken.', 'Een lijst met verboden AI-toepassingen.', 'Een technisch testprotocol voor modellen.'], 'A',
   'Losse maatregelen verwateren. Een managementsysteem zorgt dat iemand ze bijhoudt, meet en bijstuurt.',
   'De kern: van maatregel naar managementsysteem'),
 ]),
 3: dict(titel='Kennischeck 3 · Blok 3 Verantwoorden', deadline='woensdag 10 maart 2027, 23:59',
  stelling='Een AI-oplossing die nu niet verantwoord is, mag toch live als de organisatie belooft het binnen een jaar te verbeteren.',
  oefen=['Als de hertest niet beter uitpakt, moet het advies "nu niet" zijn.',
         'Een AI-oplossing is pas verantwoord als iemand van buiten de organisatie het ontwerp heeft beoordeeld.'],
  vragen=[
  ('Wat hoort bij een goede indicator in het monitoringplan (H8)?',
   ['Een grens, een actie en een eigenaar.', 'Alleen een grafiek in het maandrapport.', 'Een jaarlijkse evaluatie.'], 'A',
   'Een indicator zonder grens zegt niet wanneer je moet handelen; zonder eigenaar doet niemand het.',
   'De kern: monitoren met grenzen en acties'),
  ('Welke indicator hoort in H8, als ethisch signaal?',
   ['Het processorgebruik van de server.', 'Het verschil in onterecht afwijzen tussen groepen, en het aantal bezwaren.', 'De responstijd van de chatbot.'], 'B',
   'Techniek en data monitoren jullie in A-AI2 en A-DG; verwijs daarnaar. In H8 gaat het om signalen over mensen.',
   'De kern: wie monitort wat'),
  ('Wat is een stopcriterium?',
   ['Een vooraf vastgelegde grens waarbij het systeem uit gaat of terug naar handwerk, met wie dat beslist.', 'Het moment waarop het project af is.', 'De datum waarop het contract met de leverancier stopt.'], 'A',
   'Wie vooraf vastlegt wanneer het systeem stopt, hoeft dat niet te bedenken als het al misgaat.',
   'De kern: incidentroute en stopcriterium'),
  ('Een model werkt een jaar na livegang slechter voor één groep, terwijl niemand iets aan het model veranderde. Hoe heet dit?',
   ['Drift: de wereld en de data veranderden.', 'Overfitting', 'Labelbias'], 'A',
   'Een model leert van het verleden. Verandert de werkelijkheid, dan veroudert het model. Daarom blijf je per groep meten (practicum 5).',
   'De kern: drift'),
  ('Welk oordeel is géén van de drie oordelen in het beslismemo?',
   ['Verantwoord inzetbaar', 'Inzetbaar onder voorwaarden', 'Nu niet', 'Inzetbaar zodra de leverancier akkoord is'], 'D',
   'Het beslismemo kent drie oordelen. Het akkoord van een leverancier is hooguit een voorwaarde.',
   'Instrumenten: het beslismemo'),
  ('Wanneer is "nu niet" een goed advies?',
   ['Nooit: het betekent dat het project mislukt is.', 'Als het uit de analyse volgt, en het memo zegt wat er nodig is om het oordeel te veranderen.', 'Als de groep geen tijd meer had.'], 'B',
   '"Nu niet" is een volwaardig advies en telt even zwaar als de andere twee, als het onderbouwd is.',
   'De kern: het beslismemo en de drie oordelen'),
  ('Wat maakt een voorwaarde in het beslismemo toetsbaar?',
   ['Wat er moet gebeuren, wie eigenaar is, wanneer, en wat er gebeurt als het niet lukt.', 'Een belofte dat het later beter wordt.', 'Een verwijzing naar de wet.'], 'A',
   'Een voorwaarde zonder gevolg is een wens. Een belofte zonder eigenaar en datum is geen voorwaarde.',
   'Instrumenten: het beslismemo'),
  ('Een AI leerde de bootrace CoastRunners spelen en draaide rondjes voor punten in plaats van de race uit te rijden. Wat is de les?',
   ['AI doet wat je meet, niet wat je bedoelt; meet daarom ook de bijwerkingen.', 'Games zijn niet geschikt om AI te testen.', 'Het model was te klein.'], 'A',
   'Dit heet specification gaming. Bij een chatbot die op afhandeltijd wordt gemeten, kan hetzelfde gebeuren.',
   'College 3: veiligheid en agents'),
  ('Welke maatregel past het best bij een agent die zelf mails naar klanten stuurt?',
   ['Een mens keurt handelingen goed die niet terug te draaien zijn, met logging en een stopknop.', 'Een groter taalmodel.', 'De agent meer rechten geven, zodat hij minder vastloopt.'], 'A',
   'Hoe meer een systeem zelf doet, hoe belangrijker het is wie het kan stoppen. Geef zo weinig rechten als nodig.',
   'College 3: veiligheid en agents'),
  ('Je ontdekt na livegang dat jullie chatbot klanten verkeerd informeert. Waar begin je meestal?',
   ['Meteen bij de pers.', 'Bij het team en de eigenaar, met bewijs; hoger als het niet wordt opgepakt of de schade groot is.', 'Je doet niets, want het is niet jouw systeem.'], 'B',
   'Aankaarten is een ladder: team, eigenaar, compliance of vertrouwenspersoon, en pas daarna buiten de organisatie. De incidentroute in H8 legt die ladder vooraf vast.',
   'College 3: professionele praktijk'),
 ]),
}


def beginquiz():
    """Lees de 12 beginquizvragen met antwoord en feedback uit docent_weekcheck_w00.md."""
    t = open(os.path.join(REPO, 'mycampus', 'md', 'docent_weekcheck_w00.md'), encoding='utf-8').read()
    blok = t[t.index('## Beginquiz'):]
    out = []
    for m in re.finditer(r'^\s*(\d+)\.\s+(.*?)\n\s*-\s*Juist:\s*([A-D])\.\s*(.*?)$', blok, re.M | re.S):
        nr, body, juist, fb = m.groups()
        if int(nr) > 12 or len(out) >= 12:
            break
        body = ' '.join(body.split())
        parts = re.split(r'\s([A-D])\.\s', ' ' + body)
        vraag = parts[0].strip()
        opties = [parts[i + 1].strip() for i in range(1, len(parts) - 1, 2)]
        out.append((vraag, opties, juist, ' '.join(fb.split()), 'Blok 0: beginquiz'))
    assert len(out) == 12, len(out)
    return out


def write_md(bq):
    L = ['Dit is de docentversie van de drie kennischecks, met de juiste antwoorden en de feedback die studenten na het antwoorden zien. **Niet uploaden naar MyCampus.** Zet de vragen in MyCampus met het invoerbestand (ICT A-ET Kennischecks invoer.xlsx) of importeer het GIFT-bestand.',
         '',
         '**Opzet.** Elke kennischeck heeft tien meerkeuzevragen met directe feedback en één standpunt over een stelling (hoogstens 100 woorden: eens of oneens, één argument met bron, één tegenargument dat je serieus neemt). Kennischeck 3 bevat daarnaast de 12 vragen van de beginquiz, zodat student en docent de leerwinst zien. De kennischecks tellen niet mee voor het cijfer. Wie er een mist, krijgt een persoonlijk bericht. De standpunten gebruiken studenten in hun reflectie bij Assessment 2.',
         '',
         '**Instellingen in MyCampus.** Onbeperkt aantal pogingen; feedback direct na elke vraag; de juiste antwoorden zichtbaar na afloop; standpunt als open vraag (tekstvak). De volgorde van de opties mag willekeurig, behalve bij vragen met "géén van" of opsommingen.', '']
    for k in (1, 2, 3):
        d = KC[k]
        L += [f'## {d["titel"]}', '', f'**Deadline:** {d["deadline"]}. Individueel, bij ICT A-ET Kennischeck {k}.', '']
        for i, (v, opts, j, fb, lees) in enumerate(d['vragen'], 1):
            L.append(f'{i}. **{v}**')
            for n, o in enumerate(opts):
                L.append(f'    - {"ABCD"[n]}. {o}')
            L.append(f'    - *Juist: {j}.* {fb} *Lees na:* {lees}.')
            L.append('')
        L += [f'**Standpunt.** *"{d["stelling"]}"* Eens of oneens? Hoogstens 100 woorden, met één argument met bron en één tegenargument dat je serieus neemt.', '',
              '**Oefenstellingen** (staan in het kennispakket, niet in de kennischeck): ' + ' · '.join(f'*"{s}"*' for s in d['oefen']), '']
        if k == 3:
            L += ['### Kennischeck 3, deel 2: de beginquiz opnieuw', '', 'Dezelfde 12 vragen als in blok 0, met dezelfde feedback. Vergelijk per student de score met die van de beginquiz.', '']
            for i, (v, opts, j, fb, _) in enumerate(bq, 1):
                L.append(f'{i}. **{v}**')
                for n, o in enumerate(opts):
                    L.append(f'    - {"ABCD"[n]}. {o}')
                L.append(f'    - *Juist: {j}.* {fb}')
                L.append('')
    open(MD, 'w', encoding='utf-8').write('\n'.join(L) + '\n')


def write_xlsx(bq):
    os.makedirs(os.path.dirname(XLSX), exist_ok=True)
    wb = Workbook(); wb.remove(wb.active)
    hf = PatternFill('solid', fgColor='002060'); hfont = Font(bold=True, color='FFFFFF')
    for k in (1, 2, 3):
        ws = wb.create_sheet(f'Kennischeck {k}')
        head = ['Nr', 'Soort', 'Vraag', 'Optie A', 'Optie B', 'Optie C', 'Optie D', 'Juist', 'Feedback (na antwoorden)', 'Lees na']
        ws.append(head)
        rows = [('MC', *q) for q in KC[k]['vragen']]
        if k == 3:
            rows += [('MC beginquiz', *q) for q in bq]
        for i, (soort, v, opts, j, fb, lees) in enumerate(rows, 1):
            o = (opts + ['', '', '', ''])[:4]
            ws.append([i, soort, v, *o, j, fb, lees])
        ws.append([len(rows) + 1, 'Open (standpunt)', KC[k]['stelling'] + ' Eens of oneens? Hoogstens 100 woorden: één argument met bron, één tegenargument.', '', '', '', '', '', 'Geen automatische feedback; gebruik in de reflectie.', ''])
        for c in ws[1]:
            c.fill = hf; c.font = hfont
        for col, w in zip('ABCDEFGHIJ', [5, 14, 60, 30, 30, 30, 22, 7, 60, 30]):
            ws.column_dimensions[col].width = w
        for row in ws.iter_rows(min_row=2):
            for c in row:
                c.alignment = Alignment(wrap_text=True, vertical='top')
    wb.save(XLSX)


def gift_esc(s):
    return re.sub(r'([~=#{}:])', r'\\\1', s)


def write_gift(bq):
    L = ['// ICT A-ET Kennischecks 1 tot en met 3 (GIFT-formaat). Importeer per categorie.']
    for k in (1, 2, 3):
        L += ['', f'$CATEGORY: ICT A-ET/Kennischeck {k}', '']
        rows = list(KC[k]['vragen']) + (bq if k == 3 else [])
        for i, (v, opts, j, fb, lees) in enumerate(rows, 1):
            ans = []
            for n, o in enumerate(opts):
                mark = '=' if 'ABCD'[n] == j else '~'
                ans.append(f'  {mark}{gift_esc(o)}')
            L.append(f'::KC{k}-{i:02d}::{gift_esc(v)} {{')
            L += ans
            L.append(f'  ####{gift_esc(fb)}' + (f' Lees na: {gift_esc(lees)}.' if lees else ''))
            L.append('}')
            L.append('')
        L.append(f'::KC{k}-standpunt::{gift_esc(KC[k]["stelling"])} Eens of oneens? Hoogstens 100 woorden: één argument met bron, één tegenargument. {{}}')
    open(GIFT, 'w', encoding='utf-8').write('\n'.join(L) + '\n')


if __name__ == '__main__':
    bq = beginquiz()
    for k in KC:
        assert len(KC[k]['vragen']) == 10, k
        for v, opts, j, fb, lees in KC[k]['vragen']:
            assert j in 'ABCD'[:len(opts)], v
    write_md(bq); write_xlsx(bq); write_gift(bq)
    print('ok', MD, XLSX, GIFT)
