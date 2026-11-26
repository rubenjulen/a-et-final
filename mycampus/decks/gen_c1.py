#!/usr/bin/env python3
"""College 1 (blok 1, do 7 januari 2027): Wat staat er op het spel?

Opbouw: dilemma, ethische kaders (vijf theorieën, Safe City), bias en eerlijkheid, black box, K1.

Bouwt het deck in de Janssen-huisstijl volgens de deck-standaard (mycampus/REVIEW_CHECKLIST.md, sectie C).
Gebruik:  python3 gen_c1.py <map met gelezen project/deck.json> <uitvoermap>
Daarna publiceren naar https://claude.ai/artifact/Cj8Y7ELraHmro3d9X9Ypgc met root = <uitvoermap>.
"""
import sys
from janssen_slides import *

LOGO = '/_blob/4abe97bd07a999a9e2be7490350a0455'
PARTS = ['Dilemma', 'Ethische kaders', 'Bias en eerlijkheid', 'Black box', 'Jullie casus: K1', 'Afsluiting']
D = Deck(LOGO, 'ICT A-ET · College 1 · donderdag 7 januari 2027', PARTS)
K, H, P, UL, C, R, G = D.kicker, D.h2, D.p, D.ul, D.card, D.row, D.grid

URL_BIBIS = 'https://keynews.sr/suriname-lanceert-nieuwe-e-visumapplicatie-en-ai-chatbot-tijdens-bewustwordingssessie'
URL_ROT = 'https://www.lighthousereports.com/series/suspicion-machines/'
URL_TED = 'https://www.ted.com/talks/joy_buolamwini_how_i_m_fighting_bias_in_algorithms'

# ============ Deel 1. Dilemma ============
D.frame('cover', f'''
<div style="display:flex;justify-content:space-between;align-items:flex-start">
<img src="{LOGO}" alt="Janssen University of Applied Sciences" style="width:620px;height:72px;object-fit:contain;object-position:left">
<p style="font-size:26px;font-weight:700;color:{BLUE_T};letter-spacing:2px;text-transform:uppercase;text-align:right">Minor AI · ICT A-ET</p>
</div>
<div style="flex:1;display:flex;flex-direction:column;justify-content:center;gap:28px">
<p style="font-size:30px;font-weight:700;color:{BLUE_T};letter-spacing:3px;text-transform:uppercase">AI &amp; Ethics · College 1</p>
<h1 style="font-size:120px;font-weight:700;line-height:1.02;color:{NAVY};text-transform:uppercase">Wat staat er op het spel?</h1>
<div style="width:240px;height:10px;background:{BLUE};border-radius:5px"></div>
</div>
<div style="background:{NAVY};border-radius:14px;padding:28px 40px;display:flex;justify-content:space-between">
<p style="font-size:30px;color:{ON_NAVY}">Donderdag 7 januari 2027 · [tijd] · lokaal [__]</p>
<p style="font-size:30px;color:{GOLD};font-weight:700">Ruben [achternaam] · docent</p>
</div>''', '''[1 min · opening · 0:00] Zeg: "Welkom bij AI & Ethics. Drie uur, zes delen. De rode draad is één dilemma rond een fictieve Surinaamse bank, Suribank. Vanaf deel 5 gaat het over jullie eigen oplossing uit A-AI2." Overgang: "Eerst: wat verandert er vandaag aan jullie rol?"''', footer=False, pad='96px 128px')

reis = ''.join(
    f'<div style="flex:1;display:flex;flex-direction:column;gap:10px;align-items:center">'
    f'<div style="width:100%;height:14px;border-radius:7px;background:{BLUE if i == 0 else LINE}"></div>'
    f'<p style="font-size:26px;font-weight:700;color:{NAVY if i == 0 else MUTED}">{t}</p></div>'
    for i, t in enumerate(['Blok 1 · Analyseren', 'A1 · 4 feb', 'Blok 2 · Ontwerpen', 'College 3 · 25 feb', 'Blok 3 · Verantwoorden', 'A2 · 11 mrt']))

D.frame('vandaag', K('Rolwissel') + H('Vandaag word je beoordelaar') + R(
    C('In A-AI2', 'Je bouwt de oplossing. De vraag is: werkt het?', label='Tot nu toe', accent=MUTED),
    C('In A-ET', 'Je beoordeelt dezelfde oplossing. De vraag is: voor wie gaat het mis, en is dat te verantwoorden?', label='Vanaf vandaag', accent=BLUE)) +
    f'<div style="display:flex;flex-direction:column;gap:16px">{P("**Je bent hier:** blok 1, K1: het begin van de redeneerketen naar het eindrapport.", 30)}'
    f'<div style="display:flex;gap:10px">{reis}</div></div>',
    '''[2 min · deel 1 · 0:01] Zeg: "Tot nu toe was je vooral bouwer. Vanaf vandaag ben je ook degene die zegt of het mag, en onder welke voorwaarden." Wijs op de balk: "Het rapport groeit in drie blokken. Blok 1 analyseren: K1 tot en met K6, Assessment 1 op 4 februari. Blok 2 ontwerpen: maatregelen en governance, met de Design Review in college 3 op 25 februari. Blok 3 verantwoorden: monitoring en het beslismemo, Assessment 2 op 11 maart." Vraag: "Wie heeft in A-AI1 al een ethische evaluatie gedaan? Wat stond daar als grootste zorg?" Laat 2 of 3 antwoorden toe. Overgang: "Wat kun je aan het eind van vandaag?"''', part=1)

D.frame('leerdoelen', K('Leerdoelen') + H('Aan het einde van vandaag kun je …') +
    UL(['werkt het, mag het en is het verantwoord uit elkaar houden;',
        'een AI-keuze wegen met vijf ethische kaders, met hun sterke en zwakke kant;',
        'aanwijzen waar in de keten bias ontstaat, en uitleggen waarom perfecte eerlijkheid niet bestaat;',
        'beoordelen wanneer een black box aanvaardbaar is, en welke uitleg een getroffene verdient;',
        'jullie eigen oplossing afbakenen in het K1-canvas.'], 31, ordered=True) +
    f'<div style="background:{ICE};border-left:8px solid {BLUE};border-radius:12px;padding:28px 36px">'
    f'{P("**Eindresultaat vandaag:** K1-canvas versie 1, met drie eerste zorgen op professioneel niveau, waaronder één bias in jullie keten.", 32, NAVY)}</div>',
    '''[2 min · deel 1 · 0:03] Zeg: "Vijf doelen, één eindresultaat. Daar werken we vandaag naartoe, en jullie nemen het mee naar huis." Lees het eindresultaat hardop voor. Overgang: "Zo ziet de route eruit."''', part=1)

D.frame('route', K('Lesroute') + H('Zes delen, elk met een opbrengst') + D.table(
    ['Deel', 'Centrale vraag', 'Opbrengst', 'Tijd'],
    [['1 · Dilemma', 'Mag Suribank dit?', 'Je stem en je argument', '0:00–0:20'],
     ['2 · Ethische kaders', 'Hoe weeg je een AI-keuze?', 'De lenzentabel bij Safe City', '0:20–1:05'],
     ['Pauze', '', '', '1:05–1:15'],
     ['3 · Bias en eerlijkheid', 'Waar ontstaat bias, en wat is eerlijk?', 'Eén bias in jullie keten', '1:15–1:55'],
     ['4 · Black box', 'Wanneer moet je kunnen uitleggen?', 'Jullie oordeel over uitleg', '1:55–2:20'],
     ['5 · Jullie casus: K1', 'Wat onderzoeken jullie precies?', 'K1-canvas versie 1', '2:20–2:50'],
     ['6 · Afsluiting', 'Hoe werk je tot college 2?', 'Exit ticket', '2:50–3:00']], 27, ['26%', '36%', '24%', '14%']),
    '''[2 min · deel 1 · 0:05] Zeg: "Elk deel levert iets op dat je straks in K1, in je dilemma-canvas of in de kennischeck gebruikt. De balk rechtsboven laat zien waar we zijn." Overgang: "We beginnen niet met theorie, maar met een bank."''', part=1)

D.frame('casus', H('Mag Suribank dit doen?') + G([
    C(None, 'Beoordeelt kredietaanvragen en heeft in ongeveer **twee van de drie gevallen** gelijk.', label='Het model', size=30),
    C(None, 'Een advies **binnen een minuut**, waar een medewerker nu twee weken over doet.', label='De snelheid', size=30),
    C(None, 'Van aanvragers uit het binnenland betaalt **49%** terug, aan de kust **61%**.', label='De data', size=30),
    C(None, 'Onder **SRD 50.000** neemt de bank het advies automatisch over.', label='Het plan', size=30)], 2, 28) +
    P('Suribank is fictief. De data komen uit de oefendataset van practicum 1.', 26, MUTED),
    '''[4 min · deel 1 · 0:07] Zeg: "Suribank is een fictieve, middelgrote bank met kantoren in Paramaribo, Nickerie en Albina." Lees de vier kaarten voor. Vraag: "Mag Suribank dit doen?" Nog geen theorie: studenten moeten merken dat een AI-beslissing meteen ethische vragen oproept. Verwacht: snelheid tegenover eerlijkheid, uitleg, menselijke controle. Overgang: "Je kiest eerst zelf, voordat je hoort wat anderen vinden."''', part=1)

stemkaart = lambda bg, lab, txt, fc, lc: (f'<div style="flex:1;background:{bg};border-radius:16px;padding:40px;display:flex;flex-direction:column;justify-content:space-between;gap:24px">'
                                         f'<p style="font-size:24px;font-weight:700;color:{lc};text-transform:uppercase;letter-spacing:1px">{lab}</p>'
                                         f'<p style="font-size:64px;font-weight:700;line-height:1.05;color:{fc}">{txt}</p></div>')

D.frame('stem', K('Kies eerst, verdedig daarna') + H('Wat vind jij?') +
    f'<div style="display:flex;gap:28px">{stemkaart(GREEN, "Groene kaart", "Ja", "#FFFFFF", "#DDF0E5")}{stemkaart(RED, "Rode kaart", "Nee", "#FFFFFF", "#F8DEDB")}{stemkaart(GOLD, "Gele kaart", "Onder voorwaarden", NAVY, NAVY)}</div>' +
    R(C(None, '**1 minuut alleen:** kies je kaart en schrijf één reden op.', size=28),
      C(None, '**2 minuten met je buur:** overtuig elkaar, of noteer waarom niet.', size=28),
      C(None, '**Dan tonen.** Wie kiest iets anders dan de buur? Waarom?', size=28)) +
    P('Telling: groen [__] · rood [__] · geel [__]', 28, MUTED),
    '''[9 min · deel 1 · 0:11] Werkvorm: 1 minuut individueel kiezen en een reden noteren, 2 minuten duo, dan tegelijk de kaart opsteken (of Mentimeter). Tel per kleur en vul de telling op de dia in; noteer hem ook in de docentenmap: in college 3 stemmen we opnieuw. Vraag: "Wie koos iets anders dan de buur? Wat was het sterkste argument van de ander?" Laat per kleur twee studenten hun reden geven. Schrijf kernwoorden op het bord: meestal komen eerlijkheid, snelheid, uitleg, verantwoordelijkheid en menselijke controle vanzelf langs. Laat ze tot het eind staan; dit zijn de onderwerpen van de module. Zeg: "Er is nu geen goed of fout antwoord. Onder voorwaarden is in de praktijk vaak het professionele antwoord, maar dan is de vraag: welke voorwaarden?" Overgang: "Om dat te beantwoorden, beginnen we bij de vraag wat je eigenlijk vraagt."''', part=1)


# ============ Deel 2. Ethische kaders ============

vraag = lambda t, s, gold=False: (f'<div style="flex:1;border-top:6px solid {GOLD if gold else ON_NAVY_MUTED};padding:28px 0 0;display:flex;flex-direction:column;gap:14px">'
                                  f'<h2 style="font-size:60px;font-weight:700;color:{GOLD if gold else ON_NAVY}">{e(t)}</h2>{P(s, 30, ON_NAVY_MUTED)}</div>')

D.frame('drievragen', K('Theorie', dark=True) + R(vraag('Werkt het?', 'Is het model goed genoeg? Een technische vraag. Centraal in A-AI2.'),
    vraag('Mag het?', 'Welke regels gelden? Een juridische vraag. In Suriname vaak kort beantwoord.'),
    vraag('Is het verantwoord?', 'Is het goed om het zó te doen, voor iedereen die geraakt wordt? De vraag van A-ET.', True), gap=40) +
    D.statement('Een systeem kan werken en toegestaan zijn, en toch niet verantwoord.', dark=True, size=44),
    '''[3 min · deel 2 · 0:20] Zeg: "Drie vragen die niet hetzelfde zijn." Vraag: "Welke van de drie stelt A-AI2? En A-DG?" Verwacht: werkt het; mag het met deze data. Zeg: "In Suriname is de tweede vraag vaak kort: er is geen AI-wet en nog geen privacywet in werking. Dat maakt de derde vraag niet kleiner, maar groter." Overgang: "Mag het, is dat hetzelfde als compliance? Niet helemaal."''', dark=True, part=2)

D.frame('compliance', K('Theorie') + H('Recht, compliance en ethiek') + R(
    C('Recht', 'Wetten en regels die gelden. Ze komen vaak pas na schade, en verschillen per land.', label='Wat moet', accent=MUTED),
    C('Compliance', 'Aantonen dat je je houdt aan de wet, aan contracten en aan je eigen beleid. Vaak een vinklijst.', label='Wat je aantoont', accent=BLUE),
    C('Ethiek', 'De vraag of het goed is, voor iedereen die geraakt wordt, ook waar de wet zwijgt of achterloopt.', label='Wat hoort', accent=GOLD)) +
    D.statement('Compliance is de ondergrens, niet het doel.', size=44) +
    C(None, '**Kies eerst:** een organisatie voldoet aan alle regels en aan haar eigen beleid. Is ze daarmee verantwoord bezig? Ja, nee of hangt ervan af?', size=30, bg=ICE),
    '''[3 min · deel 2 · 0:23] Zeg: "Recht zegt wat moet. Compliance is het werk om aan te tonen dat je je daaraan houdt, en aan je eigen beleid: denk aan een compliance officer bij een bank, of aan een audit volgens ISO/IEC 42001. Ethiek vraagt of het goed is, ook als niemand het verplicht." Check: vingers opsteken, 1 = ja, 2 = nee, 3 = hangt ervan af. Verwacht: de meesten kiezen 3. Doorvragen: "Waarvan hangt het af?" Verwacht: van wie de schade draagt, of de regels de nieuwe risico's al dekken, of er uitleg en bezwaar is. Zeg: "In Suriname is er voor AI weinig om compliant mee te zijn. Dan komt het neer op ethiek en op internationale kaders. Werkt jullie partner voor Europese klanten of met Europese data, dan wordt de AI-verordening wel een compliance-eis." Overgang: "Is dat nieuw, dat regels achterlopen? Nee."''', part=2)

D.frame('lessen', K('Lessen uit eerdere technologieën') + H('Regels kwamen telkens na de schade') + G([
    C('De auto', 'Na Unsafe at Any Speed van Ralph Nader (1965) kwamen in de VS in 1966 verplichte veiligheidsnormen, zoals gordels in elke nieuwe auto.', label='1965 → 1966', size=27),
    C('Medicijnen', 'Softenon (thalidomide) werd vanaf 1957 verkocht als veilig slaapmiddel. Duizenden kinderen werden met afwijkingen geboren. Daarna kwam strenger testen vóór toelating.', label='1957 → 1962', size=27),
    C('Sociale media', 'Platforms groeiden jarenlang zonder regels voor hun algoritmes. Europa stelde pas in 2022 de Digital Services Act vast.', label='2004 → 2022', size=27)], 3, 24) +
    D.statement('Bij AI gaat het sneller. Wie nu bouwt en beoordeelt, bepaalt mee wat normaal wordt.', size=38),
    '''[3 min · deel 2 · 0:26] Zeg: "Drie voorbeelden met hetzelfde patroon: een nieuwe technologie, snelle groei, schade bij mensen die er niet om vroegen, en pas daarna regels." Auto: Ralph Nader, Unsafe at Any Speed (1965); in 1966 de National Traffic and Motor Vehicle Safety Act, met federale veiligheidsnormen. Medicijnen: thalidomide (Softenon) kwam in 1957 op de markt, werd in 1961 teruggetrokken; wereldwijd werden meer dan 10.000 kinderen met afwijkingen geboren; in 1962 kwamen in de VS de Kefauver-Harris Amendments, met strengere eisen aan bewijs van veiligheid en werking. Sociale media: de Digital Services Act (Verordening (EU) 2022/2065). Vraag: "Welke les past het best bij AI in Suriname, waar nog geen AI-wet is?" Verwacht: niet wachten op de wet; testen vóór gebruik (zoals bij medicijnen); wie bouwt, draagt verantwoordelijkheid. Zeg: "Daarom testen jullie in practicum 4 je eigen oplossing voordat iemand anders er last van heeft." Overgang: "Een recent voorbeeld waar het misging, in een land mét regels."''', part=2)

D.frame('rotterdam', K('Echte casus · Nederland, 2017–2021') + H('Rotterdam: werkte, mocht, maar was het verantwoord?') + R(
    f'<div style="flex:1.6;display:flex;flex-direction:column;gap:20px">' +
    P('Rotterdam gaf bijstandsontvangers een risicoscore voor fraudeonderzoek, met ruim 300 kenmerken, zoals leeftijd, geslacht en taalvaardigheid. Journalisten kregen het model in handen: jonge moeders en mensen die slecht Nederlands spreken, scoorden vaker hoog. De gemeente legde het eind 2021 stil.', 30) +
    f'<div style="background:{ICE};border-radius:12px;padding:24px 32px;display:flex;flex-direction:column;gap:8px">{P("**Kies eerst, per vraag: ja, nee of twijfel**", 28, NAVY)}' +
    UL(['Werkte het? Mocht het? Was het verantwoord?', 'Wat zegt de lens gevolgen, en wat de lens rechtvaardigheid?', 'Wie had het kunnen stoppen, en wie deed het?'], 28, ordered=True) + '</div></div>',
    f'<div style="flex:1;display:flex;flex-direction:column;gap:16px;align-items:center;justify-content:center">{qr_svg(URL_ROT, 300, label="QR-code naar de serie Suspicion Machines van Lighthouse Reports")}'
    f'{P("Lighthouse Reports · Suspicion Machines (maart 2023)", 24, MUTED)}{P("Interactief: WIRED, Inside the Suspicion Machine", 24, MUTED)}</div>'),
    '''[4 min · deel 2 · 0:29] Bronnen: Lighthouse Reports, serie "Suspicion Machines" (maart 2023, met WIRED, Vers Beton, Follow the Money en Argos); WIRED, "Inside the Suspicion Machine", 7 maart 2023, met een interactieve uitleg van de score; Binnenlands Bestuur: "Algoritme ziet jonge moeders en anderstaligen als risicogroep voor bijstandsfraude". Laat zo mogelijk 2 minuten de interactieve WIRED-pagina zien (test vooraf). Vraag de drie vragen; eerst iedereen tegelijk vingers: 1 = ja, 2 = nee, 3 = twijfel. Verwacht: werkte matig (experts: nauwelijks beter dan willekeurig); mocht jarenlang; niet verantwoord voor groepen die hoger scoorden door kenmerken waar ze niets aan kunnen doen. De Rekenkamer Rotterdam waarschuwde in 2021; de gemeente stopte. Brug: "Hoe weeg je dat? Daarvoor heb je ethische kaders nodig." Let op: de toeslagenaffaire komt terug in kennispakket 1 en in college 2.''', part=2)

# ---------- nieuw: waarom kaders ----------
D.frame('kaders-waarom', K('Ethische kaders') + H('Waarom kaders? Omdat redelijke mensen het oneens zijn') + R(
    C('Structuur', 'Je weegt stap voor stap, in plaats van op gevoel of mening.', label='1'),
    C('Consistentie', 'Je oordeelt over vergelijkbare gevallen op dezelfde manier.', label='2'),
    C('Onderbouwing', 'Je kunt uitleggen waarom, ook aan wie het met je oneens is.', label='3')) +
    D.table(['AI vraagt vaak om een afweging', 'Voorbeeld'],
            [['Nauwkeurigheid of eerlijkheid', 'Een kredietmodel dat beter voorspelt, maar één groep vaker onterecht afwijst'],
             ['Veiligheid of privacy', 'Camera’s met gezichtsherkenning in de binnenstad'],
             ['Vernieuwing of terughoudendheid', 'Een chatbot snel live zetten, of eerst testen met lastige vragen']], 27, ['38%', '62%']),
    '''[3 min · deel 2 · 0:33] Zeg: "Ethiek is geen mening. Een kader geeft structuur, maakt je oordeel consistent, en laat je uitleggen waarom. Het verklaart ook waarom redelijke mensen het oneens zijn: ze wegen andere dingen zwaarder." Lees de drie afwegingen voor. Vraag: "Welke afweging speelt bij jullie oplossing?" Verwacht: nauwkeurigheid of eerlijkheid bij voorspellende modellen; vernieuwing of terughoudendheid bij chatbots. Overgang: "Er zijn vijf klassieke manieren om zo'n afweging te maken."''', part=2)

lens = lambda t, th, q: C(t, P(q, 28), label=th, accent=BLUE, size=28)

D.frame('lenzen', f"""<div style="display:flex;justify-content:space-between;align-items:flex-end">{K('Praatplaat · ethische kaders')}</div>""" + H('Eén keuze, vijf vragen') + (
    f'<div style="position:relative;width:1664px;height:470px">'
    f'<svg width="1664" height="470" style="position:absolute;left:0;top:0">' +
    ''.join(f'<line x1="832" y1="270" x2="{x}" y2="{y}" stroke="{LINE}" stroke-width="5"/>' for x, y in [(832, 65), (250, 165), (1414, 165), (400, 405), (1264, 405)]) +
    f'</svg>'
    f'<div style="position:absolute;left:702px;top:140px;width:260px;height:260px;border-radius:50%;background:{NAVY};display:flex;flex-direction:column;align-items:center;justify-content:center;gap:10px;padding:30px">'
    f'<p style="font-size:26px;font-weight:700;color:{GOLD};text-transform:uppercase;letter-spacing:1px">Een AI-keuze</p>'
    f'<p style="font-size:28px;line-height:1.2;font-weight:700;color:{ON_NAVY};text-align:center">Welke vraag stel jij eerst?</p></div>' +
    ''.join(
        f'<div style="position:absolute;left:{x - 210}px;top:{y - 65}px;width:420px;height:130px;background:{CARD};border:1px solid {LINE};border-top:8px solid {col};border-radius:14px;padding:16px 22px;display:flex;flex-direction:column;gap:4px">'
        f'<p style="font-size:30px;font-weight:700;color:{NAVY}">{e(t)} <span style="font-size:22px;font-weight:700;color:{MUTED}">· {e(th)}</span></p>'
        f'<p style="font-size:24px;line-height:1.25;color:{INK}">{e(q)}</p></div>'
        for x, y, t, th, q, col in [
            (832, 65, 'Gevolgen', 'utilitarisme', 'Wat levert het op, en voor wie niet?', BLUE),
            (250, 165, 'Plichten', 'Kant', 'Welke grens mag nooit over, ook niet voor nut?', BLUE),
            (1414, 165, 'Rechtvaardigheid', 'Rawls', 'Wie draagt de lasten? Hoe vergaat het de zwakste?', BLUE),
            (400, 405, 'Deugd', 'Aristoteles', 'Wat doet een goede professional hier?', GOLD),
            (1264, 405, 'Zorg', 'Gilligan, Tronto', 'Wie is afhankelijk, en wie kan zich niet verweren?', GOLD)]) +
    '</div>') + P('**In het dilemma-canvas:** deugd en zorg samen vormen de lens professionele integriteit.', 26, MUTED),
    '''[2 min · deel 2 · 0:36] Zeg: "Vijf theorieën, vier lenzen. In het dilemma-canvas (K5) gebruik je deze vier lenzen en noem je de theorie erachter; deugd en zorg vallen samen onder professionele integriteit. We bekijken ze nu één voor één: wat vraagt het kader, wat is sterk, wat is zwak, en een AI-voorbeeld." Overgang: "Eerst gevolgen."''', part=2)

kader = lambda sid, lens, titel, denkers, kern, voorbeeld, sterk, zwak, notes: D.frame(sid,
    K(f'Lens · {lens}') + H(titel) + P(f'**{denkers}**', 27, MUTED) + D.statement(kern, size=36) +
    R(C('Sterk', UL(sterk, 26), accent=GREEN), C('Zwak', UL(zwak, 26), accent=RED), C('AI-voorbeeld', voorbeeld, accent=GOLD, size=26), gap=22),
    notes, part=2)

kader('kader-gevolgen', 'Gevolgen', 'Gevolgen: wat levert het op, en voor wie?', 'Utilitarisme · Bentham, Mill',
    'Kies wat de meeste baten en de minste schade oplevert, voor iedereen die geraakt wordt.',
    'Een AI herkent kanker in 80% van de gevallen goed. Goed genoeg? Dat hangt af van wie de 20% fouten krijgt, en wat die fouten kosten.',
    ['Praktisch en meetbaar', 'Past bij risicobeheer en beleid', 'Werkt op grote schaal'],
    ['Kleine groepen worden weggemiddeld', 'Rechten kunnen worden ingeruild voor nut', 'Niet alles is meetbaar: angst, vernedering'],
    '''[3 min · deel 2 · 0:38] Zeg: "Bij gevolgen telt alleen de uitkomst, niet de bedoeling." Rekenvoorbeeld: een systeem dat 95% van de mensen helpt en 5% benadeelt, scoort goed. Vraag: "Stel dat jij in die 5% zit. Vind je het dan nog goed?" Verwacht: nee; dat is precies de zwakte. Zeg: "Deze lens zit in elk risicoregister: kans keer impact is een gevolgenberekening." Overgang: "Wat als iets veel oplevert, maar toch niet mag?"''')

kader('kader-plichten', 'Rechten en plichten', 'Plichten: wat mag nooit, ook niet voor nut?', 'Deontologie · Kant',
    'Behandel mensen altijd ook als doel, nooit alleen als middel. Sommige grenzen ga je niet over.',
    'Een verkoopchatbot die klanten manipuleert, levert veel omzet op. Vanuit plichten is dat fout, hoe hoog de winst ook is.',
    ['Beschermt rechten en waardigheid', 'Geeft heldere grenzen', 'Werkt als vangrail'],
    ['Regels kunnen botsen', 'Star in grijze gevallen', 'Gevolgen tellen niet mee'],
    '''[3 min · deel 2 · 0:41] Zeg: "Kant: handel alleen volgens een regel waarvan je wilt dat iedereen hem volgt, en behandel mensen nooit alleen als middel." Vraag: "Je mag niet liegen. Maar wat als een leugen een leven redt?" Verwacht: verdeeld; dat laat de zwakte zien: regels kunnen botsen. Zeg: "Bij AI: een automatische afwijzing zonder uitleg behandelt de aanvrager als datapunt." Overgang: "Maar wat is een eerlijke verdeling van baten en lasten?"''')

kader('kader-rechtvaardigheid', 'Rechtvaardigheid', 'Rechtvaardigheid: is het eerlijk verdeeld?', 'Rechtvaardigheidstheorie · Rawls (1971)',
    'Kies de regels alsof je niet weet welke plek je zelf krijgt. Ongelijkheid mag alleen als de zwakste er beter van wordt.',
    'Zou je het kredietmodel van Suribank accepteren als je niet weet of je aan de kust of in het binnenland woont?',
    ['Kijkt naar de zwakste positie', 'Maakt de verdeling van lasten zichtbaar', 'Sluit aan bij non-discriminatie'],
    ['Er zijn meerdere definities van eerlijk', 'Botst soms met nut', 'Abstract zonder cijfers per groep'],
    '''[3 min · deel 2 · 0:44] Zeg: "Rawls vraagt je te kiezen achter een sluier van onwetendheid: je weet niet wie je bent." Doe de oefening: "Ogen dicht. Je weet niet of je aanvrager aan de kust of in het binnenland bent. Accepteer je het model?" Verwacht: de stem verschuift naar onder voorwaarden. Zeg: "In deel 3 zie je dat er meerdere definities van eerlijk zijn, die niet tegelijk kunnen." Overgang: "De laatste twee kaders kijken niet naar het systeem, maar naar mensen."''')

kader('kader-deugd', 'Professionele integriteit (1)', 'Deugd: wat doet een goede professional?', 'Deugdethiek · Aristoteles; beroepscodes',
    'Vraag niet alleen wat het systeem doet, maar wie het bouwt: eerlijk, zorgvuldig, moedig genoeg om nee te zeggen?',
    'Een ontwikkelaar ziet dat het model slechter werkt voor één groep, en meldt het, ook al schuift de livegang dan op.',
    ['Gaat over karakter en cultuur', 'Praktische wijsheid in grijze gevallen', 'Sluit aan bij beroepscodes (ACM, 2018)'],
    ['Vaag zonder criteria', 'Wiens deugden? Cultuur verschilt', 'Alleen niet genoeg voor bestuur'],
    '''[2 min · deel 2 · 0:47] Zeg: "Aristoteles: wat zou een goed mens, een goede vakman, hier doen? Bij AI gaat het om de makers: zijn ze eerlijk, zorgvuldig, en durven ze nee te zeggen?" Vraag: "Wie bepaalt wat een goede ontwikkelaar is?" Verwacht: beroepscodes, collega's, de organisatie; en dat het per cultuur kan verschillen. Zeg: "In het dilemma-canvas vallen deugd en zorg samen onder de lens professionele integriteit." Overgang: "Zorgethiek kijkt naar wie afhankelijk is."''')

kader('kader-zorg', 'Professionele integriteit (2)', 'Zorg: wie is afhankelijk, en wie wordt geraakt?', 'Zorgethiek · Gilligan (1982), Tronto (1993)',
    'Begin bij relaties en afhankelijkheid: wie kan zich niet verweren, en wat heeft die nodig?',
    'Een aanvrager uit het binnenland krijgt een afwijzing zonder uitleg en kan niemand bellen. Zorgethiek kijkt eerst naar die persoon.',
    ['Maakt kwetsbare groepen zichtbaar', 'Gevoelig voor context', 'Empathie naast analyse'],
    ['Moeilijk op grote schaal', 'Welke groep gaat voor?', 'Zorg alleen is geen verantwoording'],
    '''[3 min · deel 2 · 0:49] Zeg: "Zorgethiek vraagt niet eerst naar regels of uitkomsten, maar naar wie er van het systeem afhankelijk is. Tronto noemt vier stappen: opmerken dat zorg nodig is, verantwoordelijkheid nemen, de zorg geven, en nagaan hoe die aankomt." Vraag: "Wie is bij jullie oplossing het meest afhankelijk, en het minst gehoord?" Verwacht: de klant zonder digitale vaardigheden, de aanvrager die afgewezen wordt, de medewerker die moet uitvoeren. Zeg: "Geen enkel kader heeft alle antwoorden. Daarom gebruik je ze samen." Overgang: "Nu een Surinaamse casus, door alle kaders."''')

URL_SAFECITY = 'https://www.waterkant.net/suriname/2026/07/05/monorath-onze-safe-city-cameras-functioneren-wel/'
D.frame('safecity', K('Surinaamse casus · 2026') + H('Safe City: moet de politie gezichtsherkenning aanzetten?') + R(
    f'<div style="flex:1.6;display:flex;flex-direction:column;gap:18px">' +
    P('Met Safe City fase 3 hangen sinds begin 2026 camera’s in Paramaribo en de districten. Ze hielpen de politie al bij het opsporen van straatrovers in het centrum. Volgens de minister van Justitie en Politie kunnen de nieuwe camera’s ook kentekens en gezichten herkennen; die mogelijkheden worden nog niet volledig gebruikt.', 29) +
    R(C('Voor', 'Snellere opsporing, meer veiligheid op straat, minder angst om ’s avonds over straat te gaan.', size=26, accent=GREEN),
      C('Tegen', 'Iedereen wordt gevolgd, ook wie niets deed. Foute treffers, vaker bij sommige groepen. Geen privacywet en geen toezichthouder.', size=26, accent=RED), gap=18) + '</div>',
    f'<div style="flex:1;display:flex;flex-direction:column;gap:14px;align-items:center;justify-content:center">{qr_svg(URL_SAFECITY, 280, label="QR-code naar het artikel van Waterkant over de Safe City-camera’s")}'
    f'{P("Waterkant, 5 juli 2026", 24, MUTED)}{P("Suriname Herald, 27 februari 2026", 24, MUTED)}</div>'),
    '''[3 min · deel 2 · 0:52] Bronnen: Suriname Herald, 27 februari 2026, "Safe City 3 landelijk uitgerold; camera's actief in districten" (wnd. korpschef Melvin Pinas); Waterkant, 5 juli 2026, "Monorath: Onze Safe City camera's functioneren wel" (minister Harish Monorath in De Nationale Assemblée: de nieuwe camera's hebben kenteken- en gezichtsherkenning; de volledige capaciteit wordt nog niet benut); Starnieuws over de aanhouding van straatrovers in het centrum met Safe City-beelden. Let op: andere berichten beschrijven gezichtsherkenning als wens van de politie, niet als iets wat al draait. Formuleer het dus als: "volgens de minister kan het". Controleer vlak voor het college of er nieuws is. Zeg: "Dit is de afweging veiligheid of privacy, in ons eigen land. Elk groepje bekijkt hem nu door één kader." Koppeling met deel 3: gezichtsherkenning maakt niet bij iedereen even vaak fouten (Gender Shades, NIST, Robert Williams). Overgang: werkblok.''', part=2)

D.frame('opdracht-lens', D.werkblok('5 min werken + 3 min verslag', 'Groepjes van 3–4') + H('Safe City door één lens') +
    UL(['Elk groepje krijgt één lenzenkaart.', 'Beantwoord de hulpvragen op de kaart.', 'Formuleer één conclusie en noem de theorie achter je lens.'], 32, ordered=True) +
    f'<div style="background:{ICE};border-radius:12px;padding:28px 36px">{P("“Vanuit onze lens mag de politie gezichtsherkenning **wel** / **niet** / **alleen onder deze voorwaarden** aanzetten, omdat …”", 31, NAVY)}</div>' +
    D.klaar('één conclusiezin in deze vorm, de theorie genoemd, en één hulpvraag waarop jullie géén antwoord wisten.'),
    '''[8 min · deel 2 · 0:55] Deel de vijf lenzenkaarten uit (A5: gevolgen, rechten en plichten, rechtvaardigheid, deugd, zorg; zie docentvoorbereiding); bij meer dan vijf groepjes krijgen sommige lenzen twee groepjes. 5 minuten werken; loop rond. Docentvraag: "Welke informatie mist jullie om te kunnen oordelen?" Daarna per lens hooguit 30 seconden verslag; vul tijdens het verslag de tabel op de volgende dia. Verwacht per lens: gevolgen: minder criminaliteit en snellere opsporing tegenover foute treffers en een gevoel van gevolgd worden; rechten en plichten: privacy (Grondwet art. 17), zonder privacywet en zonder toezichthouder; rechtvaardigheid: wie krijgt de foute treffers (NIST, Gender Shades), en in welke wijken hangen de camera's; deugd: wat voor samenleving worden we, en wat doet een goede politieleiding; zorg: wie is kwetsbaar, zoals jongeren in bepaalde wijken, en wie kan zich niet verweren. Overgang: "Valt jullie iets op als we ze naast elkaar zetten?"''', part=2)

D.frame('tegenspraak', H('De lenzen spreken elkaar tegen') + D.table(
    ['Lens', 'Mag het?', 'Belangrijkste argument'],
    [['Gevolgen', ' ', ' '], ['Rechten en plichten', ' ', ' '], ['Rechtvaardigheid', ' ', ' '], ['Deugd', ' ', ' '], ['Zorg', ' ', ' ']], 28, ['30%', '20%', '50%']) +
    D.statement('Daarom heb je een gestructureerde afweging nodig. Die leer je in deze module.', size=38),
    '''[2 min · deel 2 · 1:03] Vul de tabel tijdens het verslag in, op het scherm of op het bord: wel, niet of onder voorwaarden, en het belangrijkste argument. Zeg: "Geen enkel kader heeft alle antwoorden. Daarom weeg je ze samen, en zeg je wat je opgeeft. Vóór 4 februari doe je dat individueel voor een dilemma uit jullie eigen casus, in het dilemma-canvas." Overgang: pauze; daarna bias."''', part=2)

D.frame('pauze', f'<div style="flex:1;display:flex;flex-direction:column;justify-content:center;gap:28px"><h1 style="font-size:160px;font-weight:700;line-height:1;color:{ON_NAVY};text-transform:uppercase">Pauze</h1>{P("10 minuten · we gaan verder om [__:__]", 44, GOLD, 700)}</div>',
    '''[10 min · pauze · 1:05] Vul de tijd in. Laat de woorden van het bord uit deel 1 en de lenzentabel staan.''', dark=True)


# ============ Deel 3. Bias, eerlijkheid en discriminatie ============

# ---------- nieuw: bias in de keten ----------
D.frame('bias-keten', K('Praatplaat · bias in de keten') + H('Waar in de keten ontstaat bias?') + (
    '<div style="position:relative;width:1664px;height:470px">'
    f'<svg width="1664" height="470" style="position:absolute;left:0;top:0"><defs><marker id="pijlb" markerWidth="10" markerHeight="10" refX="8" refY="5" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="{GOLD}"/></marker></defs>'
    f'<path d="M1560,300 L1560,440 L104,440 L104,312" fill="none" stroke="{GOLD}" stroke-width="5" stroke-dasharray="14 10" marker-end="url(#pijlb)"/></svg>'
    '<div style="position:absolute;left:0;top:0;width:1664px;display:flex;gap:0;align-items:flex-start">' +
    ''.join(
        f'<div style="width:{208 if i < 6 else 208}px;display:flex;flex-direction:column;align-items:center;gap:12px">'
        f'<div style="display:flex;align-items:center;width:100%"><div style="flex:1;background:{NAVY if i in (0, 6) else BLUE_T};border-radius:12px;padding:16px 6px"><p style="font-size:27px;font-weight:700;color:#FFFFFF;text-align:center">{e(stap)}</p></div>'
        f'{"<p style=" + chr(34) + "font-size:34px;font-weight:700;color:" + BLUE + ";width:30px;text-align:center" + chr(34) + ">→</p>" if i < 6 else ""}</div>'
        f'<div style="width:{"178" if i < 6 else "208"}px;align-self:flex-start;background:{ICE};border-radius:10px;padding:12px 12px;min-height:190px"><p style="font-size:23px;font-weight:700;color:{RED if i >= 4 else NAVY}">{e(soort)}</p>'
        f'<p style="font-size:21px;line-height:1.3;color:{INK}">{e(uitleg)}</p></div></div>'
        for i, (stap, soort, uitleg) in enumerate([
            ('Data', 'Data en representatie', 'Wie ontbreekt? Ook het label: wie werd afgewezen?'),
            ('Verleden', 'Historisch', 'Juiste data met oude ongelijkheid erin.'),
            ('Kenmerken', 'Meting en proxy', 'District meet stiekem inkomen of afkomst.'),
            ('Model', 'Algoritmisch', 'Het doel bevoordeelt de grootste groep.'),
            ('Inzet', 'Inzet', 'Gebruikt waar het niet voor gemaakt is.'),
            ('Gebruik', 'Interactie', 'Gebruikers sturen het systeem bij.'),
            ('Terugkoppeling', 'Bevestiging', 'Het systeem bevestigt wat men al dacht.')])) +
    '</div>'
    f'<p style="position:absolute;left:640px;top:400px;background:{BG};padding:0 16px;font-size:24px;font-weight:700;color:#8A6A1F">Feedbacklus: het systeem leert van zijn eigen uitkomsten</p>'
    '</div>') + P('**Waar zag je het al?** Suribank: data, verleden, kenmerken · Gender Shades: data · Robert Williams en Rite Aid: data en inzet', 25, MUTED),
    '''[6 min · deel 3 · 1:15] Zeg: "Bias in AI: een systeem geeft stelselmatig oneerlijke uitkomsten, door aannames in de data of in het ontwerp. Clip 6 noemde zes bronnen; hier staan ze op de plek in de keten waar ze ontstaan, plus wat er gebeurt als het systeem draait." Koppeling met clip 6: historisch (2), representatie en label (1), meting (3), aggregatie (4), gebruik (5). Nieuw: interactiebias (6) en bevestigingsbias (7): een systeem dat leert van gebruikers of van eerdere beslissingen kan bestaande vooroordelen versterken (feedbacklus). Voorbeeld van een feedbacklus: als een fraudemodel vooral in één wijk laat controleren, vind je daar meer fraude, en het model leert dat die wijk riskanter is. Kies eerst: "Welke bias zie je het eerst bij Suribank?" Verwacht: historisch en label (alleen goedgekeurde leningen), meting (inkomen ontbreekt bij informeel werk), proxy (district). Gevolgen van bias: discriminatie, verlies van vertrouwen, juridische risico's. Overgang: "Terug naar de Suribank-data."''', part=3)

D.frame('verleden', H('Een model leert het verleden') + R(
    f'<div style="flex:1;border-top:8px solid {RED};padding:28px 0 0;display:flex;flex-direction:column;gap:8px"><p style="font-size:160px;font-weight:700;line-height:1;color:{RED}">49%</p>{P("van de aanvragers uit het **binnenland** betaalde terug", 32)}</div>',
    f'<div style="flex:1;border-top:8px solid {BLUE};padding:28px 0 0;display:flex;flex-direction:column;gap:8px"><p style="font-size:160px;font-weight:700;line-height:1;color:{BLUE_T}">61%</p>{P("van de aanvragers aan de **kust** betaalde terug", 32)}</div>', gap=48) +
    f'<div style="background:{NAVY};border-radius:14px;padding:32px 44px">{P("Uit practicum 1: **is het probleem weg als de bank district weglaat?**", 36, ON_NAVY)}</div>',
    '''[4 min · deel 3 · 1:21] Gebruik de antwoorden op vraag 6 van practicum 1 (blok 0); zet er vooraf twee anonieme antwoorden uit de leeromgeving bij. Vraag: "Wie zegt ja, wie zegt nee?" Laat twee studenten met verschillende antwoorden reageren. Verwacht en kernpunt: het verschil hangt samen met inkomen en soort werk, en die hangen weer samen met waar iemand woont. District weglaten haalt het patroon niet weg (proxy). Zeg: "Een model leert patronen uit het verleden, inclusief eerdere ongelijkheid. Een taalmodel doet hetzelfde met teksten." Bron: oefendataset suribank_kredietaanvragen.csv, 1.200 aanvragen. Overgang: "En wat doet de bank met de uitkomst van het model?"''', part=3)

stap = lambda lab, big, small, col: C(None, f'<p style="font-size:24px;font-weight:700;color:{col};text-transform:uppercase;letter-spacing:1px">{lab}</p><p style="font-size:{60 if len(big) < 6 else 34}px;font-weight:700;color:{NAVY}">{e(big)}</p>{P(small, 26)}', accent=col)

pijl = f'<p style="font-size:40px;font-weight:700;color:{BLUE};align-self:center">→</p>'

D.frame('kans', H('Een kans is geen beslissing') +
    f'<div style="display:flex;gap:14px;align-items:stretch">{stap("Model", "72%", "kans op terugbetaling", BLUE)}{pijl}{stap("Keuze bank", "60%", "drempel", RED)}{pijl}{stap("Advies", "Goedkeuren", "boven de drempel", BLUE)}{pijl}{stap("Keuze bank", "Wie beslist?", "Onder SRD 50.000 automatisch, daarboven een medewerker", RED)}</div>' +
    R(C(None, '**Kies eerst:** wie bepaalt de drempel, of wat een chatbot wel en niet mag zeggen?', size=30, bg=ICE),
      C(None, '**Kies eerst:** is een model dat 69% goed heeft een goed model? Wie kiest iets anders?', size=30, bg=ICE)),
    '''[3 min · deel 3 · 1:25] Zeg: "De uitkomst van het model is een kans. De drempel en wat er daarna gebeurt, zijn keuzes van de organisatie: daarom staat daar Keuze bank. Bij een chatbot is het net zo: de instructies, de documenten en wat er met het antwoord gebeurt, kiest de organisatie, niet het taalmodel." Check met handopsteken, eerst kiezen, dan pas praten. Vraag 1: wie bepaalt de drempel? Verwacht: de bank (en dus is de bank verantwoordelijk). Vraag 2: is 69% goed een goed model? Vraag: "Wie kiest iets anders?" Verwacht: in practicum 1 haalde altijd ja zeggen (Constant) al 59%; het model is maar tien procentpunt beter, en het percentage zegt niets over wie de fouten krijgt. Overgang: "En als die fouten niet gelijk verdeeld zijn over groepen?"''', part=3)

D.frame('gender-nist', K('Echte casus · onderzoek naar gezichtsherkenning') + H('Een goed gemiddelde verbergt grote verschillen') + R(
    f'<div style="flex:1.6;display:flex;flex-direction:column;gap:18px">' +
    R(C(None, f'<p style="font-size:88px;font-weight:700;line-height:1;color:{BLUE_T}">0,8%</p>{P("fout bij mannen met een lichte huidskleur (Gender Shades, 2018)", 26)}'),
      C(None, f'<p style="font-size:88px;font-weight:700;line-height:1;color:{RED}">34,7%</p>{P("fout bij vrouwen met een donkere huidskleur, bij hetzelfde systeem", 26)}', accent=RED), gap=18) +
    C('NIST, december 2019', 'Het Amerikaanse standaardeninstituut NIST testte 189 algoritmen. Valse treffers verschilden per groep vaak 10 tot meer dan 100 keer.', size=26, accent=GOLD) + '</div>',
    f'<div style="flex:1;display:flex;flex-direction:column;gap:14px;align-items:center;justify-content:center">{qr_svg(URL_TED, 260, label="QR-code naar de TED-talk van Joy Buolamwini")}'
    f'{P("TED · Joy Buolamwini, How I’m fighting bias in algorithms", 23, MUTED)}{P("NIST IR 8280 (2019)", 23, MUTED)}</div>'),
    '''[4 min · deel 3 · 1:28] Speel zo mogelijk 2 minuten van de TED-talk (het witte masker); test vooraf. Bronnen: Buolamwini & Gebru (2018), Gender Shades, PMLR 81, 77–91; NIST IR 8280, Face Recognition Vendor Test Part 3: Demographic Effects (Grother, Ngan en Hanaoka, december 2019): 189 algoritmen; valse treffers verschilden vaak met een factor 10 tot meer dan 100. Bij veel in de VS ontwikkelde algoritmen waren valse treffers hoger voor Aziatische en Afro-Amerikaanse gezichten; de hoogste waarden zag NIST bij Amerikaanse indianen; sommige in Azië ontwikkelde algoritmen lieten dat verschil niet zien. Vraag: "Welke bias uit de keten zie je?" Verwacht: representatiebias (te weinig donkere gezichten in de trainingsdata) en algoritmische bias (alleen het gemiddelde geoptimaliseerd). Koppeling met Safe City: dit is precies het risico als de camera's gezichten gaan herkennen. Overgang: "Wat dit betekent voor één mens."''', part=3)

URL_WILLIAMS = 'https://www.aclu.org/news/privacy-technology/wrongfully-arrested-because-face-recognition-cant-tell-black-people-apart'
D.frame('williams', K('Echte casus · Verenigde Staten, 2020–2024') + H('Robert Williams: gearresteerd na een foute match') + R(
    f'<div style="flex:1.6;display:flex;flex-direction:column;gap:14px">' +
    P('In januari 2020 arresteerde de politie van Detroit Robert Williams bij zijn huis, waar zijn vrouw en dochters bij waren. Gezichtsherkenning had hem ten onrechte gekoppeld aan beelden van een winkeldiefstal. In juni 2024 schikte de stad: 300.000 dollar en nieuwe regels.', 27) +
    R(C(None, '**Nieuwe regel 1:** geen arrestatie alleen op basis van gezichtsherkenning.', size=24),
      C(None, '**Nieuwe regel 2:** geen fotoconfrontatie op basis van een zoekopdracht in gezichtsherkenning.', size=24),
      C(None, '**Nieuwe regel 3:** eerdere zaken met gezichtsherkenning worden nagelopen.', size=24), gap=16) +
    f'<div style="background:{ICE};border-radius:12px;padding:16px 28px;display:flex;flex-direction:column;gap:4px">{P("**Kies eerst, per vraag**", 25, NAVY)}' +
    UL(['Welke bias uit de keten zie je terug?', 'Waarom geloofden de agenten de computer?', 'Wie is verantwoordelijk: leverancier, politie of agent?'], 24, ordered=True) + '</div></div>',
    f'<div style="flex:1;display:flex;flex-direction:column;gap:14px;align-items:center;justify-content:center">{qr_svg(URL_WILLIAMS, 260, label="QR-code naar het verhaal van Robert Williams bij de ACLU")}'
    f'{P("ACLU · het verhaal van Robert Williams, met video", 23, MUTED)}{P("Michigan Public, 28 juni 2024", 23, MUTED)}</div>'),
    '''[5 min · deel 3 · 1:32] Bronnen: ACLU, "Wrongfully Arrested Because Face Recognition Can't Tell Black People Apart" (juni 2020, met video waarin Williams zelf vertelt); ACLU, zaakpagina Williams v. City of Detroit en persbericht over de schikking; Michigan Public, 28 juni 2024. Feiten: arrestatie januari 2020 in Farmington Hills, in het bijzijn van zijn vrouw en jonge dochters; ongeveer een dag vastgehouden; rechtszaak door de ACLU van Michigan in april 2021; schikking juni 2024 met 300.000 dollar en de drie regels. Volgens de ACLU waren alle drie de bekende mensen die in Detroit onterecht werden gearresteerd na een gezichtsherkenningsmatch zwart. Noem geen leverancier van de software en geen exact aantal uren: daarover verschillen bronnen. Verwacht: (1) representatiebias, zoals bij Gender Shades; (2) automation bias: de match werd behandeld als bewijs; (3) de keten: leverancier, korps zonder regels, agenten; de schikking legt de verantwoording bij de organisatie. Kernzin: een match is een kans, geen bewijs. Overgang: "Het gebeurt niet alleen bij de politie."''', part=3)

URL_RITEAID = 'https://techcrunch.com/2023/12/20/rite-aid-facial-recognition/'
D.frame('riteaid', K('Echte casus · Verenigde Staten, 2023') + H('Rite Aid: “winkeldief” volgens de camera') + R(
    f'<div style="flex:1.6;display:flex;flex-direction:column;gap:16px">' +
    P('De drogisterijketen Rite Aid gebruikte jarenlang gezichtsherkenning om vermeende winkeldieven te herkennen. Medewerkers kregen meldingen, vaak onterecht, en spraken klanten aan of belden de politie. In december 2023 verbood de toezichthouder FTC het gebruik voor vijf jaar.', 28) +
    R(C('Wat misging', 'Vage beelden, nauwelijks training over foute treffers, geen controle op de uitkomsten.', size=25, accent=RED),
      C('Voor wie', 'Volgens de FTC vaker foute meldingen in winkels in wijken met vooral zwarte en Aziatische bewoners, en vaak bij vrouwen.', size=25, accent=GOLD), gap=16) + '</div>',
    f'<div style="flex:1;display:flex;flex-direction:column;gap:14px;align-items:center;justify-content:center">{qr_svg(URL_RITEAID, 260, label="QR-code naar het artikel van TechCrunch over Rite Aid")}'
    f'{P("TechCrunch, 20 december 2023", 23, MUTED)}</div>'),
    '''[3 min · deel 3 · 1:37] Bronnen: FTC, persbericht van 19 december 2023 (Rite Aid banned from using AI facial recognition); TechCrunch en Axios, 20 december 2023. Feiten: vijf jaar verbod op gezichtsherkenning voor beveiliging en toezicht; beelden en daarmee gemaakte modellen verwijderen; volgens de FTC de eerste keer dat zij een organisatie verbood gezichtsherkenning te gebruiken. Vraag: "Welke plek in de keten?" Verwacht: inzet (vage beelden, geen training), en geen menselijke controle die werkt. Koppeling met Safe City: de vragen die de FTC stelde, kun je ook in Suriname stellen: wie test de foute treffers, en per groep? Overgang: "Is elk onderscheid dan discriminatie?"''', part=3)

D.frame('bias-discriminatie', H('Bias of discriminatie?') + R(
    C('Bias', 'Een technisch begrip: een model wijkt systematisch af voor een groep.', accent=BLUE),
    C('Discriminatie', 'Een juridisch en ethisch begrip: een ongerechtvaardigd onderscheid.', accent=RED)) +
    f'<div style="background:{NAVY};border-radius:14px;padding:30px 44px;display:flex;flex-direction:column;gap:12px">{P("**Grondwet van Suriname, artikel 8 lid 2**", 26, GOLD)}'
    f'{P("Verbiedt onderscheid op onder meer geboorte, geslacht, ras, taal, godsdienst en afkomst, maar ook op economische positie en sociale omstandigheden.", 30, ON_NAVY)}</div>' +
    D.statement('De vraag is niet óf er onderscheid is, maar of het gerechtvaardigd en proportioneel is.', size=36),
    '''[3 min · deel 3 · 1:40] Vraag eerst (kies eerst): "Is een kredietmodel dat rekening houdt met inkomen discriminerend? Ja of nee?" Verwacht: verdeeld. Zeg: "Niet zonder meer: terugbetaalcapaciteit is een legitiem doel, maar het onderscheid moet proportioneel zijn en niet verder gaan dan nodig. En district? Daar is de rechtvaardiging veel lastiger, want district werkt als proxy." Overgang: "Kun je een model dan gewoon eerlijk maken?"''', part=3)

D.frame('eerlijkheid', H('Perfecte eerlijkheid bestaat niet') + R(
    C('Gelijke betekenis', 'Een score van 70% betekent voor elke groep hetzelfde: van wie 70% krijgt, betaalt ongeveer 70% terug.', label='Kalibratie'),
    C('Gelijke fouten', 'Elke groep wordt even vaak onterecht afgewezen, en even vaak onterecht goedgekeurd.', label='Foutverdeling', accent=GOLD),
    C('Gelijke uitkomst', 'Elke groep wordt even vaak goedgekeurd.', label='Uitkomst', accent=RED)) +
    D.statement('Verschilt het terugbetaalcijfer tussen groepen, dan kan een model niet alle drie tegelijk halen. Je moet kiezen, en die keuze verantwoorden.', size=34) +
    C(None, '**Kies eerst:** bij Suribank betaalt 49% uit het binnenland terug en 61% aan de kust. Welke eerlijkheid kies jij, en wie betaalt de prijs?', size=28, bg=ICE),
    '''[4 min · deel 3 · 1:43] Zeg: "Er bestaan meerdere definities van eerlijk. Als groepen verschillen in hoe vaak de uitkomst voorkomt, kan geen model aan allemaal tegelijk voldoen, behalve een perfect model." Bron: Kleinberg, Mullainathan & Raghavan (2017), Inherent Trade-Offs in the Fair Determination of Risk Scores (arXiv 1609.05807); Chouldechova (2017), Big Data 5(2). Achtergrond: de discussie over COMPAS (ProPublica, 2016): de score was voor zwarte en witte verdachten even goed gekalibreerd, maar zwarte verdachten kregen vaker onterecht een hoge score. Beide kanten hadden gelijk, met een andere definitie. Extra voorbeeld: een bedrijf neemt 50 mannen en 50 vrouwen aan (gelijke uitkomst), terwijl er 60 geschikte mannen en 40 geschikte vrouwen solliciteerden: dan worden 10 geschikte mannen afgewezen en 10 minder geschikte vrouwen aangenomen. Ook dat is een keuze voor één definitie. Zeg: "Eerlijk is niet één getal. Het is een keuze die je steeds opnieuw maakt, en die je uitlegt." Overgang: "Wat kun je dan wel doen?"''', part=3)

D.frame('bias-antwoord', K('Wat doe je ertegen?') + H('Bias beheersen, niet wegtoveren') + G([
    C('Testen per groep', 'Een bias-audit: meet fouten per groep, en meld de verschillen eerlijk.', size=26),
    C('Een divers team', 'Meer perspectieven, minder blinde vlekken, risico’s eerder gezien.', size=26),
    C('Een mens beslist', 'Bij grote gevolgen houdt een mens echt het laatste woord.', size=26),
    C('Iemand is verantwoordelijk', '“Het algoritme besliste” is geen excuus.', size=26),
    C('Recht op bezwaar', 'Wie geraakt wordt, kan een uitkomst aanvechten en laten herstellen.', size=26),
    C('Soms geen AI', 'Kunnen is niet hetzelfde als moeten. Soms doet een mens het beter.', size=26, accent=GOLD)], 3, 20) +
    D.statement('Ethische AI is niet AI zonder bias, maar AI waarvan je de bias opspoort, beperkt en eerlijk benoemt.', size=34),
    '''[4 min · deel 3 · 1:47] Zeg: "Bias krijg je nooit helemaal weg. Het doel is: opsporen, beperken, en de gevolgen verantwoord beheren." Koppel elk vak aan het werk in de module: testen per groep (practicum 2 en 4, domein 5 van de nulmeting); een divers team en de stem van wie geraakt wordt (K2); een mens beslist en recht op bezwaar (H7); verantwoordelijk (de RACI in H7); soms geen AI (de optie zonder AI in het dilemma-canvas, en het oordeel "nu niet" in het beslismemo). Overgang: "Nu jullie eigen keten."''', part=3)

D.frame('bias-nujij', D.werkblok('4 min', 'Groep') + H('Welke bias zit in jullie keten?') +
    UL(['Kies één plek in de keten van jullie oplossing.', 'Welke soort bias kan daar ontstaan?', 'Wie raakt het, en hoe toon je het aan?'], 31, ordered=True) +
    D.klaar('één bias met plek, groep en test. Dit wordt een van de drie zorgen in veld 13 van K1.', 28),
    '''[4 min · deel 3 · 1:51] Loop rond. Docentvraag bij een chatbot: "Krijgt iemand die in een andere taal of met spelfouten schrijft even goede antwoorden?" Bij een voorspellend model: "Welk kenmerk werkt als proxy?" Laat één groep in 30 seconden voorlezen. Overgang naar deel 4: "Om bias te vinden, moet je kunnen zien hoe een systeem beslist. Wat als dat niet kan?"''', part=3)

# ============ Deel 4. Black box ============
D.frame('blackbox-wat', K('Black box en uitlegbaarheid', dark=True) + H('Een black box: wel een antwoord, geen reden', dark=True) +
    P('Een black box geeft een uitkomst zonder begrijpelijke uitleg hoe die tot stand kwam. Dat gebeurt vooral bij deep learning en grote taalmodellen: modellen met miljarden getallen, de gewichten, waarvan niemand de betekenis kan aflezen.', 31, ON_NAVY_MUTED) +
    R(C('“Lees dan de code”', 'Kan, maar de code zegt weinig. De kennis zit in de gewichten, en die vertellen niet wat ze betekenen.', label='Waarom het niet helpt', dark=True),
      C('Bij jullie oplossing', 'Gebruiken jullie een taalmodel van een externe aanbieder? Dan is dat voor jullie altijd een black box.', label='Nu jij', dark=True)) +
    D.statement('Hoe slimmer het model, hoe moeilijker vaak de uitleg.', dark=True, size=40),
    '''[4 min · deel 4 · 1:55] Zeg: "Een model kan heel nauwkeurig zijn en toch niet kunnen zeggen waarom." Uitleg: een neuraal netwerk bestaat uit lagen met gewichten; een groot taalmodel heeft er honderden miljarden of meer. Let op: het getal van 1,76 biljoen parameters voor GPT-4 dat online rondgaat, is een schatting die OpenAI nooit heeft bevestigd; noem het niet als feit. Vraag: "Is jullie oplossing een black box? Voor wie: voor jullie, voor de partner, voor de klant?" Verwacht: een taalmodel via een API is voor iedereen een black box; een beslisboom of regelset niet. Overgang: "Er zijn drie soorten ondoorzichtigheid."''', dark=True, part=4)

URL_SYRI = 'https://www.rechtspraak.nl/organisatie-en-contact/organisatie/rechtbanken/rechtbank-den-haag/nieuws/2020/02/syri-wetgeving-in-strijd-met-het-europees-verdrag-voor-de-rechten-voor-de-mens'
soort = lambda nr, t, s, casus, col: (f'<div style="flex:1;background:{CARD};border:1px solid {LINE};border-top:6px solid {col};border-radius:14px;padding:26px 28px;display:flex;flex-direction:column;gap:10px">'
    f'<p style="font-size:24px;font-weight:700;color:{BLUE_T};text-transform:uppercase;letter-spacing:1px">Soort {nr}</p><h3 style="font-size:32px;font-weight:700;color:{NAVY}">{e(t)}</h3>{P(s, 25)}'
    f'<div style="background:{ICE};border-radius:10px;padding:14px 18px">{P(casus, 23)}</div></div>')
D.frame('blackbox-soorten', K('Burrell (2016)') + H('Drie soorten ondoorzichtigheid') + R(
    soort(1, 'Bewust geheim', 'Een bedrijf of overheid houdt het model geheim: bedrijfsgeheim of staatsgeheim.',
          '**SyRI (Nederland):** het risicomodel was geheim. Op 5 februari 2020 oordeelde de rechter dat de wet in strijd was met het recht op privéleven (art. 8 EVRM). **Loomis (VS, 2016):** een rechter gebruikte de geheime COMPAS-score bij de strafmaat.', RED),
    soort(2, 'Te ingewikkeld voor wie het raakt', 'De uitleg bestaat, maar alleen in vaktaal. Wie het niet begrijpt, kan geen bezwaar maken.',
          '**Een afgewezen aanvrager** krijgt “score 42” of een lijst met kenmerken. Wat moet die ermee?', GOLD),
    soort(3, 'Ook voor de makers onbekend', 'Het model is zo complex dat zelfs experts niet precies weten waarom een uitkomst zo uitvalt.',
          '**Grote taalmodellen:** ook de makers kunnen niet aanwijzen waarom een antwoord zo is geformuleerd.', BLUE), gap=20) +
    P('Elke soort vraagt een ander antwoord: openheid, uitleg in gewone taal, of een ander, leesbaar model.', 28, NAVY, 700),
    '''[6 min · deel 4 · 1:59] Bron: Burrell, J. (2016). How the machine 'thinks': Understanding opacity in machine learning algorithms. Big Data & Society 3(1); drie soorten: opzettelijke geheimhouding door bedrijf of staat, technisch analfabetisme, en ondoorzichtigheid door de aard en schaal van machine learning. Casussen: SyRI, rechtbank Den Haag 5 februari 2020 (ECLI:NL:RBDHA:2020:865): de wetgeving voldeed niet aan art. 8 lid 2 EVRM; het risicomodel en de indicatoren waren niet openbaar, dus onvoldoende inzichtelijk en controleerbaar. State v. Loomis, Wisconsin Supreme Court 2016: gebruik van COMPAS bij de strafmaat toegestaan, maar met waarschuwingen; de verdachte kon het bedrijfsgeheime model niet toetsen. Apple Card (2019 tot 2021): klanten kregen geen uitleg bij verschillende kredietlimieten; de toezichthouder NYDFS vond geen onwettige discriminatie, maar wel gebrek aan transparantie naar klanten (staat in kennispakket 1). Vraag per soort: "Wat is de oplossing?" Verwacht: (1) openbaarheid of een onafhankelijke audit; (2) uitleg in gewone taal en een loket; (3) een leesbaar model, of strengere menselijke controle. Overgang: "Waarom is transparantie dan zo belangrijk?"''', part=4)

D.frame('transparantie', H('Transparantie is geen luxe') + G([
    C('Verantwoording', 'Alleen wat je kunt zien, kun je controleren, auditen en herstellen.', label='1', size=27),
    C('Vertrouwen', 'Mensen gebruiken en accepteren wat ze kunnen begrijpen.', label='2', size=27),
    C('Eerlijkheid', 'Verborgen logica kan verborgen bias bevatten.', label='3', size=27),
    C('Toestemming', 'Je kunt niet echt instemmen met iets wat je niet begrijpt.', label='4', size=27)], 2, 22) +
    P('Transparant betekent niet de broncode delen, maar eerlijk zijn over het doel, de data, de beslisregels in gewone taal en de beperkingen.', 29, NAVY),
    '''[3 min · deel 4 · 2:05] Zeg: "Transparantie is geen ethische luxe, het is een voorwaarde." Koppel aan het werk: transparantie is domein 6 van de nulmeting, en in H7 schrijven groepen een transparantieverklaring van één A4 voor de getroffenen. Bij chatbots geldt in de EU sinds 2 augustus 2026 een AI-melding (art. 50 AI-verordening); in Suriname is dat nog geen wet, maar wel goede praktijk. Overgang: "Maar wat bedoelen we precies met uitleg?"''', part=4)

D.frame('uitleg', K('Black box · uitleg') + H('Interpreteerbaar of uitlegbaar?') + R(
    C('Interpreteerbaar', 'Het model zelf is te volgen. De vraag is: hoe werkt het?', label='Zit in het model'),
    C('Uitlegbaar', 'Je kunt een beslissing begrijpelijk maken. De vraag is: waarom deze uitkomst?', label='Achteraf, in gewone taal', accent=GOLD)) +
    D.table(['Route', 'Wat het is', 'Voor wie het werkt'],
            [['Een leesbaar model', 'Beslisboom of scorekaart; bij grote gevolgen vaak even goed (Rudin, 2019)', 'Medewerker, toezichthouder'],
             ['Uitleg achteraf', 'Welke kenmerken wogen het zwaarst? Een benadering, geen kijkje in het model', 'Ontwikkelaar, auditor'],
             ['Wat had anders moeten zijn?', '“Met SRD 2.000 meer vast inkomen was u goedgekeurd” (Wachter e.a., 2018)', 'De aanvrager']], 25, ['24%', '50%', '26%']),
    '''[5 min · deel 4 · 2:08] Zeg: "Interpreteerbaar gaat over de bouw van het model, uitlegbaar over de communicatie." Bronnen: Rudin, C. (2019), Nature Machine Intelligence 1, 206–215 (doi 10.1038/s42256-019-0048-x): bij beslissingen met grote gevolgen liever een leesbaar model als het even goed presteert; Wachter, Mittelstadt & Russell (2018), Counterfactual explanations without opening the black box, Harvard Journal of Law & Technology 31(2). Vraag: "Welke uitleg verdient een afgewezen aanvrager bij Suribank?" Verwacht: de contrafactische, in gewone taal, plus de weg naar een mens. Kernzin: "Een model kan nauwkeurig zijn en toch onverantwoord, als de mensen om wie het gaat de uitkomst niet kunnen begrijpen." Koppel aan practicum 3. Overgang: "Mag een black box dan nooit?"''', part=4)

D.frame('blackbox-wanneer', K('Praatplaat · black box') + H('Wanneer mag een black box?') + R(
    '<div style="position:relative;width:1080px;height:600px;flex:none">'
    f'<p style="position:absolute;left:0;top:0;width:60px;height:540px;display:flex;align-items:center;justify-content:center;writing-mode:vertical-rl;transform:rotate(180deg);font-size:24px;font-weight:700;color:{MUTED}">advies  →  eindbeslissing</p>'
    f'<p style="position:absolute;left:70px;top:556px;width:1010px;text-align:center;font-size:24px;font-weight:700;color:{MUTED}">impact op iemands leven: laag  →  hoog</p>' +
    ''.join(
        f'<div style="position:absolute;left:{x}px;top:{y}px;width:495px;height:262px;background:{bg};border-radius:14px;padding:18px 22px;display:flex;flex-direction:column;gap:8px">'
        f'<p style="font-size:26px;font-weight:700;color:{fc}">{e(kop)}</p>' +
        ''.join(f'<p style="font-size:23px;line-height:1.25;color:{INK};background:#FFFFFF;border-radius:999px;padding:6px 16px;align-self:flex-start">● {e(v)}</p>' for v in vb) + '</div>'
        for x, y, bg, fc, kop, vb in [
            (70, 0, '#FFF4DA', '#8A6A1F', 'Mag, met bezwaar en herstel', ['Automatisch spamfilter']),
            (585, 0, '#F8DEDB', RED, 'Geen black box', ['Suribank onder SRD 50.000', 'SyRI', 'Strafmaat met COMPAS (Loomis)']),
            (70, 278, '#DDF0E5', GREEN, 'Black box vaak aanvaardbaar', ['Muziekaanbevelingen']),
            (585, 278, '#FFF4DA', '#8A6A1F', 'Alleen met uitleg en echte controle', ['Match gezichtsherkenning als tip (Williams, Safe City)', 'E-visumchatbot BIBIS'])]) +
    '</div>',
    f'<div style="flex:1;display:flex;flex-direction:column;gap:20px">' + D.statement('Hoe groter de impact, hoe zwaarder de eis aan uitleg.', size=32) +
    C('Niet aanvaardbaar als', UL(['rechten of vrijheid op het spel staan', 'er geen bezwaar mogelijk is', 'de macht scheef verdeeld is', 'geen mens echt ingrijpt'], 24), accent=RED, size=24) +
    C(None, '**Kies eerst:** waar staat jullie oplossing op deze plaat?', size=26, bg=ICE) + '</div>', gap=28),
    '''[7 min · deel 4 · 2:13] Loop de vier vakken langs: horizontaal de impact op iemands leven, verticaal of het systeem adviseert of zelf beslist. Laat studenten eerst raden waar elk voorbeeld staat, dan pas tonen. Verwacht: muziekaanbevelingen linksonder; de e-visumchatbot van het ministerie van BIBIS (gelanceerd 30 april 2025, met VFS Global; Keynews en gov.sr): het antwoord zelf is advies, maar een fout antwoord kan leiden tot een verkeerde aanvraag of een gemiste reis; dus wel een AI-melding, bronnen en een weg naar een mens; Suribank onder SRD 50.000 rechtsboven: een eindbeslissing over krediet zonder mens en zonder uitleg; de match bij Williams is formeel een tip, maar werd behandeld als bewijs: zonder echte controle schuift hij naar rechtsboven. Laat drie groepen hun eigen oplossing plaatsen. Nog een Surinaams voorbeeld als het past: de WhatsApp-assistent van een bank (DSB Buddy, volgens het register van het Straits Institute; controleer dit vooraf). De vuistregel sluit aan bij de AI-verordening: hoe hoger het risico, hoe zwaarder de eisen, met bij hoog risico een recht op uitleg van een individuele beslissing (art. 86). Overgang naar deel 5: "Nu jullie eigen oplossing: wat onderzoeken jullie precies?"''', part=4)


# ============ Deel 5. Jullie casus: K1 ============

D.frame('kies-casus', H('Jullie casus: de oplossing uit A-AI2') + R(
    C('Standaard', 'De oplossing die jullie in A-AI2 verder bouwen, met de partner uit A-AI2 als organisatie. Zelfde groep in drie vakken.', dark=True, flex=1.3),
    C('Uitzondering 1', 'Raakt jullie oplossing nauwelijks mensen? Kies een andere organisatie, met een contactpersoon die meewerkt.'),
    C('Uitzondering 2', 'Lopen jullie vast? Werk met het Suribank-casusdossier. Wisselen kan tot maandag 25 januari.')) +
    P('Een geschikte casus: de oplossing beïnvloedt uitkomsten voor mensen, er is genoeg bewijs, en het past in tien weken. **Vrijdag 8 januari bevestig ik per groep de casus.**', 28),
    '''[2 min · deel 5 · 2:20] Groepen leggen hun beschrijving uit blok 0 op tafel en toetsen die aan de drie eisen onderaan. Bewijs komt uit gesprekken met de partner, ontwerpkeuzes, tests en de documentatie uit A-AI2 en A-DG. Onderzoeksethiek, ook zonder Surinaamse privacywet: de contactpersoon geeft toestemming (ICT A-ET Toestemmingsformulier interview, map Naslag), gesprekspartners mogen weigeren, geen persoonsgegevens van klanten of medewerkers, en anonimiseren tenzij de organisatie anders wil. Voorbeeld van uitzondering 1: een interne tool die vergaderverslagen samenvat. Overgang: "Zo ziet een uitgewerkt canvas eruit."''', part=5)

D.frame('k1-voorbeeld', K('Zo werk je K1 uit') + H('Vier velden van Suribank') + D.table(
    ['Veld', 'Suribank'],
    [['6 · Output', 'Een kans van 0 tot 100% en een advies: goedkeuren boven 60%, anders afwijzen'],
     ['7 · Beslissing', 'Onder SRD 50.000 wordt het advies automatisch overgenomen; daarboven beslist een kredietmedewerker'],
     ['9 · Betrokkenen', 'Aanvragers, vooral uit het binnenland en met informeel werk, en hun gezinnen'],
     ['13 · Zorg', 'Bij kleine bedragen kijkt geen mens mee en krijgt niemand uitleg (UNESCO: menselijk toezicht; transparantie)']], 29, ['26%', '74%']) +
    D.statement('Let op het verschil tussen output en beslissing, en tussen gebruikers en betrokkenen.', size=34),
    '''[2 min · deel 5 · 2:22] Zeg: "Output is wat het model maakt. Beslissing is wat de organisatie ermee doet, en wie dat doet. Betrokkenen zijn mensen die de gevolgen merken, ook als ze het systeem nooit zien: de gezinnen." Vraag: "Wie is bij Suribank gebruiker, en wie betrokkene?" Verwacht: kredietmedewerkers en het hoofd kredietverlening zijn gebruikers; aanvragers en gezinnen betrokkenen. Het volledige voorbeeld staat in de studentversie en in het werkboek. Overgang: "Het lastigste veld is 13: de zorgen."''', part=5)

niv = lambda lab, col, t, fc='#FFFFFF': (f'<div style="display:flex;gap:0;border:1px solid {LINE};border-radius:14px;overflow:hidden">'
    f'<p style="width:260px;flex:none;background:{col};color:{fc};font-size:30px;font-weight:700;padding:28px">{lab}</p>'
    f'<p style="flex:1;background:{CARD};font-size:30px;line-height:1.35;color:{INK};padding:28px 32px">{e(t)}</p></div>')

D.frame('niveaus', H('Eén zorg op drie niveaus') + niv('Zwak', RED, 'Het model kan bias hebben.') +
    niv('Redelijk', GOLD, 'Mensen uit het binnenland worden vaker afgewezen.', NAVY) +
    niv('Professioneel', GREEN, 'Aanvragers uit het binnenland lopen meer kans op een onterechte afwijzing, omdat bij informeel werk vaker het inkomen ontbreekt; onder SRD 50.000 kijkt geen mens mee. Bewijs nodig: fouten per regio (practicum 4).') +
    P('Professioneel = **wie** · **hoe** · **waardoor** · **hoe je het aantoont**', 32, NAVY),
    '''[2 min · deel 5 · 2:24] Zeg: "Professioneel betekent: wie wordt geraakt, hoe, waardoor, en hoe je het gaat aantonen. Dat is de redeneerketen in het klein." Vraag: "Wat mist er in de redelijke versie?" Verwacht: waardoor (informeel werk, ontbrekend inkomen), en welk bewijs. Overgang: "Nu jullie eigen canvas. Lever minstens goed in; basis, goed en sterk staan in kennispakket 1."''', part=5)

D.frame('k1-canvas', D.werkblok('16 min', 'Groep') + H('K1-canvas: wat onderzoeken jullie precies?') +
    G([f'<div style="background:{CARD};border:1px solid {LINE};border-radius:10px;padding:12px 18px;display:flex;gap:12px;align-items:baseline"><p style="font-size:26px;font-weight:700;color:{BLUE_T}">{i + 1}</p><p style="font-size:26px;color:{NAVY}">{t}</p></div>'
       for i, t in enumerate(['Organisatie en context', 'Probleem', 'AI-toepassing', 'Soort AI', 'Input', 'Output', 'Beslissing', 'Gebruikers', 'Betrokkenen',
                              'Doel en succes', 'Afbakening', 'Casus en bewijs', 'Drie eerste zorgen'])] +
      [f'<div style="background:{NAVY};border-radius:10px;padding:12px 18px"><p style="font-size:26px;font-weight:700;color:{GOLD}">+ Vijf teamafspraken</p></div>'], 5, 14) +
    D.klaar('alle 13 velden in één zin; output en beslissing apart; minstens één betrokkene die het systeem niet gebruikt; drie zorgen met wie, hoe en waardoor.', 28) +
    P('**Nu verwerken, niet thuis:** de laatste 4 minuten zet je het canvas in de werkboektab K1_Scope (één laptop per groep). Chatbot of agent? Vul ook de vragen voor generatieve AI in.', 27),
    '''[16 min · deel 5 · 2:26] 12 minuten invullen, 4 minuten in de werkboektab K1_Scope zetten (wie op A3 werkte, maakt een foto). Loop rond. Docentvragen: "Wat gebeurt er direct ná de output, en wie merkt dat?" · "Wie gebruikt het, en wie merkt de gevolgen zonder het zelf te gebruiken?" · "Welke gegevens gaan naar een externe dienst?" · "Wat onderzoeken jullie bewust niet?" · Bij een chatbot of agent: "Weet de gebruiker dat het AI is, en kan die een mens bereiken?" Teamafspraken: wie coördineert, wie is eigenaar van welke hoofdstukken, wanneer overleggen jullie, hoe verdelen jullie het werk naast A-AI2 en A-DG, en wat doen jullie als iemand niet levert. Overgang: "Ruil je canvas met de buurgroep."''', part=5)

D.frame('canvasruil', D.werkblok('8 min', 'Twee groepen') + H('Ruil je canvas') +
    UL(['Staat er een betrokkene die het systeem níet gebruikt?', 'Is duidelijk wat er ná de output gebeurt, en wie dat beslist?', 'Is elke zorg professioneel: wie, hoe, waardoor, bewijs?'], 32, ordered=True) +
    R(C(None, '**5 minuten:** lees het canvas van de buurgroep en schrijf bij elke vraag één opmerking.', size=28),
      C(None, '**3 minuten:** terug naar je eigen canvas. **Na afloop verbeter je minimaal één veld.**', size=28, accent=GOLD)),
    '''[8 min · deel 5 · 2:42; loopt door tot 2:50] Koppel groepen per twee. Loop rond. Vraag: "Welke opmerking van de andere groep nemen jullie over, en welke bewust niet?" Laat aan het eind één groep in 30 seconden zeggen welk veld ze verbeterden. Overgang: "Hoe werk je tot college 2, en daarna?"''', part=5)


# ============ Deel 6. Afsluiting ============

def blokkaart(nr, naam, datum, items, nu=False):
    bg, tc, lc, ic = (NAVY, ON_NAVY, GOLD, ON_NAVY_MUTED) if nu else (CARD, NAVY, BLUE_T, INK)
    border = '' if nu else f'border:1px solid {LINE};border-top:6px solid {BLUE};'
    return (f'<div style="flex:1;background:{bg};{border}border-radius:14px;padding:26px 28px;display:flex;flex-direction:column;gap:10px">'
            f'<p style="font-size:24px;font-weight:700;color:{lc};text-transform:uppercase;letter-spacing:1px">Blok {nr}{" · nu" if nu else ""}</p>'
            f'<h3 style="font-size:36px;font-weight:700;color:{tc}">{e(naam)}</h3><p style="font-size:24px;color:{lc}">{e(datum)}</p>'
            f'{UL(items, 24, ic)}</div>')

D.frame('blokken', H('Drie colleges, vier blokken') + R(
    blokkaart(0, 'Voorbereiden', '14 dec – 6 jan', ['Kennispakket 0', 'Beginquiz', 'Practicum 1']),
    blokkaart(1, 'Analyseren', '7 jan – 4 feb', ['College 1 en 2', 'K1 tot en met K6', 'Kennischeck 1 (3 feb)', '**A1: do 4 feb**'], True),
    blokkaart(2, 'Ontwerpen', '5 – 25 feb', ['Feedback A1 (18 feb)', 'K7: maatregelen', 'Kennischeck 2 (24 feb)', '**College 3: Design Review**']),
    blokkaart(3, 'Verantwoorden', '26 feb – 11 mrt', ['K8: monitoring', 'Beslismemo en reflectie', 'Kennischeck 3 (10 mrt)', '**A2: do 11 mrt**']), gap=20) +
    R(C(None, '**Tussen de colleges:** het kennispakket van het blok, feedback op vaste momenten (11 jan, 25 jan, 18 feb) en een kennischeck aan het eind van elk blok.', size=26),
      C(None, '**Afspraken:** generatieve AI mag, met de AI-verklaring bij elke inlevering. Mis je een kennischeck of een groepsdeadline, dan neem ik contact met je op.', size=26)),
    '''[3 min · deel 6 · 2:50] Zeg: "Er zijn drie colleges: vandaag, volgende week met een gastspreker en een debat, en op 25 februari de feedback op Assessment 1 en de Design Review. Daartussen werk je met het kennispakket van het blok: korte teksten, clips, practica en voorbeelden." Wijs de feedbackmomenten aan: maandag 11 januari feedforward op K1; maandag 25 januari op het concept van K2 tot en met K4 (wie dat op 24 januari inlevert); donderdag 18 februari de schriftelijke feedback op Assessment 1. Kennischecks: tien vragen met directe feedback en één standpunt over een stelling; ze tellen niet mee, maar je gebruikt je standpunten in de reflectie. Zeg: "Mis je een kennischeck of een groepsdeadline, dan neem ik contact met je op."''', part=6)

D.frame('toetsing', H('Toetsing: twee momenten, elk met een groeps- en een eigen deel') + D.table(
    ['Onderdeel', 'Inleveren', 'Wat', 'Eindcijfer'],
    [['A1 groepsdeel', 'do 4 februari', 'Tussenrapport H1–H5, max. 8 pagina’s', '18%'],
     ['A1 individueel', 'do 4 februari', 'Dilemma-canvas, 800–1000 woorden', '12%'],
     ['A2 groepsdeel', 'do 11 maart', 'Eindrapport H1–H8 en beslismemo, max. 12 pagina’s', '42%'],
     ['A2 individueel', 'do 11 maart', 'Reflectie, 1500–2000 woorden', '28%']], 28, ['26%', '20%', '40%', '14%']) +
    P('**Eindproduct:** een beslismemo met één van drie oordelen: verantwoord inzetbaar, onder voorwaarden, of nu niet. Eindcijfer minimaal **5,5**. Rubric en voorbeeldrapport staan onder Algemeen: ICT A-ET Beoordelingsrubric en ICT A-ET Voorbeeldrapport.', 28),
    '''[2 min · deel 6 · 2:53] Zeg: "Assessment 1 telt 30%, Assessment 2 70%. Binnen elke toets is het groepsdeel 60% en het individuele deel 40%, zodat elke student een eigen cijfer krijgt. Elke student is eigenaar van benoemde hoofdstukken; peerbeoordeling kan het groepscijfer per student verlagen bij aantoonbaar te weinig bijdrage." Wijs op de rubric (criterium 1 voor K1) en het voorbeeldrapport ClaimWacht. Bij A1 mag het testverslag van practicum 4 als bijlage (sterk aanbevolen); dat telt niet mee voor de 8 pagina’s. Overgang: "Wat doe je tot college 2?"''', part=6)

D.frame('deze-week', H('Tot college 2') + R(
    C('Uiterlijk zondag 10 januari, 23:59', UL(['K1-canvas met teamafspraken → **ICT A-ET K1**', 'Kennispakket 1: clip 5, kaderclip A en de kernbron UNESCO (hoofdstuk III)'], 28), accent=BLUE),
    C('Uiterlijk dinsdag 12 januari, 23:59', UL(['Drie vragen voor de gastspreker', 'Twee debatstellingen, elk met twee bronnen', '→ **ICT A-ET Voorbereiding college 2**'], 28), accent=GOLD)) +
    P('Vrijdag 8 januari: casus bevestigd. Maandag 11 januari: feedforward per groep op K1. Vast? Veelgestelde vragen, Begrippenlijst en Kaderkaart in de map Naslag; daarna [kanaal].', 27, MUTED),
    '''[1 min · deel 6 · 2:55] Loop de lijst door. Zeg: "Vragen en stellingen zijn voor college 2 op donderdag 14 januari, met de gastspreker [naam, organisatie]. Een goede stelling is één zin, echt betwistbaar, met een botsing tussen twee waarden." Overgang: "Nog één ding voordat je gaat."''', part=6)

D.frame('exit', K('Exit ticket · 4 minuten · ICT A-ET Exit ticket college 1', dark=True) +
    UL(['Het grootste ethische risico van onze oplossing is …, omdat …', 'Welke lens vind jij voor onze casus het belangrijkst, en waarom?', 'Wat is mij nog onduidelijk over K1?',
        'Bonus: je stem van vandaag, groen, rood of geel? En nu?'], 34, ON_NAVY, ordered=True) +
    f'<div style="background:#0B2A6B;border-radius:14px;padding:24px 32px">{P("**Stelling om over na te denken:** “Een organisatie mag een chatbot namens een medewerker laten antwoorden, zolang de klant geen verschil merkt.”", 28, ON_NAVY)}</div>' +
    D.statement('Een systeem kan werken en toegestaan zijn, en toch niet verantwoord. Dat beoordelen is jullie vak in deze module.', dark=True, size=36),
    '''[4 min · deel 6 · 2:56] Studenten vullen het exit ticket in bij de MyCampus-opdracht ICT A-ET Exit ticket college 1 (telefoon of laptop), individueel. Lees de stelling voor: "Hij komt terug in kennischeck 1; neem hem mee naar het debat in college 2." Sluit af met de kernboodschap. Na het college: lees de antwoorden en gebruik ze in het feedforward-bericht van maandag; noteer de stemming (bonusvraag) naast de telling van deel 1.''', dark=True, part=6)

D.frame('bronnen', H('Bronnen (1/2)') + UL([
    'UNESCO (2021). Recommendation on the Ethics of Artificial Intelligence, hoofdstuk III. unesdoc.unesco.org/ark:/48223/pf0000381137',
    'OECD (2019, herzien 2024). Recommendation of the Council on Artificial Intelligence (OECD AI Principles).',
    'NIST (2023). AI Risk Management Framework 1.0 (NIST AI 100-1), functie Map, MAP 1.1.',
    'ISO/IEC 42001:2023. Artificial intelligence: management system, clausule 4.1 en 4.3.',
    'Verordening (EU) 2024/1689 (AI-verordening), art. 3, art. 6 met bijlage III punt 5(b), art. 50.',
    'IEEE CertifAIEd, ontologieën transparantie, verantwoording, algoritmische bias en privacy.',
    'Regering van Suriname (30 april 2025). Bekendmaking 2025.04.30; Keynews, e-visumapplicatie en AI-chatbot.',
    'Lighthouse Reports (maart 2023). Suspicion Machines; WIRED (7 maart 2023). Inside the Suspicion Machine.',
    'UNESCO en Suriname (2026). AI Readiness Assessment [link controleren].'], 22),
    '''[niet tonen tenzij gevraagd] Bronnen bij de dia's. Controleer vóór het college de links van Safe City, BIBIS, Rotterdam, Williams en Rite Aid, en het nieuws over het UNESCO-traject.''')

D.frame('bronnen-2', H('Bronnen (2/2)') + UL([
    'Nader, R. (1965). Unsafe at Any Speed; Kefauver-Harris Amendments (1962), na thalidomide; Verordening (EU) 2022/2065 (Digital Services Act).',
    'Gilligan, C. (1982). In a Different Voice; Tronto, J. (1993). Moral Boundaries (zorgethiek).',
    'Burrell, J. (2016). How the machine ‘thinks’. Big Data & Society 3(1).',
    'NIST IR 8280 (2019). Face Recognition Vendor Test Part 3: Demographic Effects; Buolamwini & Gebru (2018). Gender Shades.',
    'ACLU (2020) en Michigan Public (28 juni 2024): Robert Williams; FTC (19 december 2023) en TechCrunch: Rite Aid.',
    'Rechtbank Den Haag, 5 februari 2020, SyRI (ECLI:NL:RBDHA:2020:865); State v. Loomis, 881 N.W.2d 749 (Wis. 2016).',
    'Kleinberg, Mullainathan & Raghavan (2017); Chouldechova (2017); Rudin (2019); Wachter, Mittelstadt & Russell (2018).',
    'Suriname Herald (27 februari 2026) en Waterkant (5 juli 2026): Safe City.',
    'Suribank en de oefendataset suribank_kredietaanvragen.csv zijn fictief (A-ET, 2026).'], 22),
    '''[niet tonen tenzij gevraagd] Vervolg van de bronnen.''')

D.frame('docent-voorbereiding', K('Docent · niet tonen') + H('Voorbereiding college 1') + G([
    UL(['Kaarten groen, rood, geel (of Mentimeter klaarzetten)', 'Vijf lenzenkaarten A5: gevolgen, plichten, rechtvaardigheid, deugd, zorg', 'Twee anonieme antwoorden op vraag 6 van practicum 1 (dia “verleden”)',
        'TED-fragment en QR-codes testen (Safe City, Williams, Rite Aid)', 'K1-canvas A3 per groep'], 26),
    UL(['Nieuws over Safe City en gezichtsherkenning checken', 'Nieuws ontwerpwet privacy en UNESCO-traject checken', 'Tijd, lokaal, je achternaam en de pauzetijd invullen',
        'Inleverpunten K1, Voorbereiding college 2 en Exit ticket college 1 open', 'Telling van de stemming noteren (terug in college 3)'], 26)], 2, 40),
    '''Deze dia staat achteraan en wordt niet getoond. Na het college: exit tickets lezen, casus per groep bevestigen (vr 8 januari), feedforward-bericht (ma 11 januari).''')

if __name__ == '__main__':
    src, out = sys.argv[1], sys.argv[2]
    sections = {
        's1': {'description': 'Deel 1. Rolwissel, leerdoelen en het dilemma van Suribank', 'start': 'cover'},
        's2': {'description': 'Deel 2. Ethische kaders: werkt, mag, verantwoord; compliance; vijf theorieën; Safe City', 'start': 'drievragen'},
        's3': {'description': 'Deel 3. Bias, eerlijkheid en discriminatie: de keten, Gender Shades, Robert Williams, Rite Aid', 'start': 'bias-keten'},
        's4': {'description': 'Deel 4. Black box en uitlegbaarheid: drie soorten, transparantie, wanneer aanvaardbaar', 'start': 'blackbox-wat'},
        's5': {'description': 'Deel 5. Jullie casus: K1-canvas en canvasruil', 'start': 'kies-casus'},
        's6': {'description': 'Deel 6. Blokken en toetsing, tot college 2, exit ticket, bronnen en docentvoorbereiding', 'start': 'blokken'},
    }
    idx = D.write(out, src + '/project/deck.json', 'College 1 AI & Ethics: Wat staat er op het spel?', sections, {})
    print(len(idx['order']), 'dia\'s')

