#!/usr/bin/env python3
"""College 1 (blok 1, do 7 januari 2027): Wat staat er op het spel?

Bouwt het deck in de Janssen-huisstijl volgens de deck-standaard (mycampus/REVIEW_CHECKLIST.md, sectie C).
Gebruik:  python3 gen_c1.py <map met gelezen project/deck.json> <uitvoermap>
Daarna publiceren naar https://claude.ai/artifact/Cj8Y7ELraHmro3d9X9Ypgc met root = <uitvoermap>.
"""
import sys
from janssen_slides import *

LOGO = '/_blob/4abe97bd07a999a9e2be7490350a0455'
PARTS = ['Dilemma', 'Van data tot beslissing', 'Werkt, mag, verantwoord', 'Kader en eindproduct', 'Jullie casus: K1', 'Afsluiting']
D = Deck(LOGO, 'ICT A-ET · College 1 · donderdag 7 januari 2027', PARTS)
K, H, P, UL, C, R, G = D.kicker, D.h2, D.p, D.ul, D.card, D.row, D.grid

URL_BIBIS = 'https://keynews.sr/suriname-lanceert-nieuwe-e-visumapplicatie-en-ai-chatbot-tijdens-bewustwordingssessie'
URL_ROT = 'https://www.lighthousereports.com/series/suspicion-machines/'

# ============ 0. Cover ============
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

# ============ Deel 1. Dilemma ============
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
    '''[3 min · deel 1 · 0:01] Zeg: "Tot nu toe was je vooral bouwer. Vanaf vandaag ben je ook degene die zegt of het mag, en onder welke voorwaarden." Wijs op de balk: "Het rapport groeit in drie blokken. Blok 1 analyseren: K1 tot en met K6, Assessment 1 op 4 februari. Blok 2 ontwerpen: maatregelen en governance, met de Design Review in college 3 op 25 februari. Blok 3 verantwoorden: monitoring en het beslismemo, Assessment 2 op 11 maart." Vraag: "Wie heeft in A-AI1 al een ethische evaluatie gedaan? Wat stond daar als grootste zorg?" Laat 2 of 3 antwoorden toe. Overgang: "Wat kun je aan het eind van vandaag?"''', part=1)

D.frame('leerdoelen', K('Leerdoelen') + H('Aan het einde van vandaag kun je …') +
    UL(['werkt het, mag het en is het verantwoord uit elkaar houden;',
        'uitleggen waar in de keten van data tot gevolg mensen keuzes maken;',
        'een dilemma door één ethische lens bekijken en de theorie erachter noemen;',
        'jullie eigen oplossing afbakenen in het K1-canvas.'], 34, ordered=True) +
    f'<div style="background:{ICE};border-left:8px solid {BLUE};border-radius:12px;padding:28px 36px">'
    f'{P("**Eindresultaat vandaag:** een bevestigde casus en K1-canvas versie 1, met drie eerste zorgen op professioneel niveau.", 32, NAVY)}</div>',
    '''[2 min · deel 1 · 0:04] Zeg: "Vier doelen, één eindresultaat. Daar werken we vandaag naartoe, en jullie nemen het mee naar huis." Lees het eindresultaat hardop voor. Overgang: "Zo ziet de route eruit."''', part=1)

D.frame('route', K('Lesroute') + H('Zes delen, elk met een opbrengst') + D.table(
    ['Deel', 'Centrale vraag', 'Opbrengst', 'Tijd'],
    [['1 · Dilemma', 'Mag Suribank dit?', 'Je stem en je argument', '0:00–0:25'],
     ['2 · Van data tot beslissing', 'Waar zitten de keuzes van mensen?', 'De twee ketens', '0:25–0:55'],
     ['3 · Werkt, mag, verantwoord', 'Hoe weeg je een dilemma?', 'De lenzentabel', '0:55–1:35'],
     ['Pauze', '', '', '1:35–1:45'],
     ['4 · Kader en eindproduct', 'Waarop word je beoordeeld?', 'De redeneerketen', '1:45–2:10'],
     ['5 · Jullie casus: K1', 'Wat onderzoeken jullie precies?', 'K1-canvas versie 1', '2:10–2:50'],
     ['6 · Afsluiting', 'Hoe werk je tot college 2?', 'Exit ticket', '2:50–3:00']], 27, ['26%', '36%', '24%', '14%']),
    '''[2 min · deel 1 · 0:06] Zeg: "Elk deel levert iets op dat je straks in K1, in je dilemma-canvas of in de kennischeck gebruikt. De balk rechtsboven laat zien waar we zijn." Overgang: "We beginnen niet met theorie, maar met een bank."''', part=1)

D.frame('casus', H('Mag Suribank dit doen?') + G([
    C(None, 'Beoordeelt kredietaanvragen en heeft in ongeveer **twee van de drie gevallen** gelijk.', label='Het model', size=30),
    C(None, 'Een advies **binnen een minuut**, waar een medewerker nu twee weken over doet.', label='De snelheid', size=30),
    C(None, 'Van aanvragers uit het binnenland betaalt **49%** terug, aan de kust **61%**.', label='De data', size=30),
    C(None, 'Onder **SRD 50.000** neemt de bank het advies automatisch over.', label='Het plan', size=30)], 2, 28) +
    P('Suribank is fictief. De data komen uit de oefendataset van practicum 1.', 26, MUTED),
    '''[5 min · deel 1 · 0:08] Zeg: "Suribank is een fictieve, middelgrote bank met kantoren in Paramaribo, Nickerie en Albina." Lees de vier kaarten voor. Vraag: "Mag Suribank dit doen?" Nog geen theorie: studenten moeten merken dat een AI-beslissing meteen ethische vragen oproept. Verwacht: snelheid tegenover eerlijkheid, uitleg, menselijke controle. Overgang: "Je kiest eerst zelf, voordat je hoort wat anderen vinden."''', part=1)

stemkaart = lambda bg, lab, txt, fc, lc: (f'<div style="flex:1;background:{bg};border-radius:16px;padding:40px;display:flex;flex-direction:column;justify-content:space-between;gap:24px">'
                                         f'<p style="font-size:24px;font-weight:700;color:{lc};text-transform:uppercase;letter-spacing:1px">{lab}</p>'
                                         f'<p style="font-size:64px;font-weight:700;line-height:1.05;color:{fc}">{txt}</p></div>')
D.frame('stem', K('Kies eerst, verdedig daarna') + H('Wat vind jij?') +
    f'<div style="display:flex;gap:28px">{stemkaart(GREEN, "Groene kaart", "Ja", "#FFFFFF", "#DDF0E5")}{stemkaart(RED, "Rode kaart", "Nee", "#FFFFFF", "#F8DEDB")}{stemkaart(GOLD, "Gele kaart", "Onder voorwaarden", NAVY, NAVY)}</div>' +
    R(C(None, '**1 minuut alleen:** kies je kaart en schrijf één reden op.', size=28),
      C(None, '**2 minuten met je buur:** overtuig elkaar, of noteer waarom niet.', size=28),
      C(None, '**Dan tonen.** Wie kiest iets anders dan de buur? Waarom?', size=28)) +
    P('Telling: groen [__] · rood [__] · geel [__]', 28, MUTED),
    '''[12 min · deel 1 · 0:13] Werkvorm: 1 minuut individueel kiezen en een reden noteren, 2 minuten duo, dan tegelijk de kaart opsteken (of Mentimeter). Tel per kleur en vul de telling op de dia in; noteer hem ook in de docentenmap: in college 3 stemmen we opnieuw. Vraag: "Wie koos iets anders dan de buur? Wat was het sterkste argument van de ander?" Laat per kleur twee studenten hun reden geven. Schrijf kernwoorden op het bord: meestal komen eerlijkheid, snelheid, uitleg, verantwoordelijkheid en menselijke controle vanzelf langs. Laat ze tot het eind staan; dit zijn de onderwerpen van de module. Zeg: "Er is nu geen goed of fout antwoord. Onder voorwaarden is in de praktijk vaak het professionele antwoord, maar dan is de vraag: welke voorwaarden?" Overgang: "Om dat te beantwoorden, kijken we eerst waar in het systeem de keuzes zitten."''', part=1)

# ============ Deel 2. Van data tot beslissing ============
D.frame('quiz', K('Uit de beginquiz') + H('Wat jullie al weten, en wat nog niet') + R(
    C(None, f'<p style="font-size:110px;font-weight:700;line-height:1;color:{RED}">[__%]</p>{P("had **[begrip 1]** goed in de beginquiz", 30)}'),
    C(None, f'<p style="font-size:110px;font-weight:700;line-height:1;color:{RED}">[__%]</p>{P("had **[begrip 2]** goed in de beginquiz", 30)}')),
    '''[5 min · deel 2 · 0:25] Vul vooraf in: de twee begrippen die in de beginquiz van blok 0 het vaakst fout gingen, met het percentage goed (de quiz sluit op 6 januari). Zeg: "Deze twee nemen we vandaag mee." Leg elk begrip in één of twee zinnen uit, met een voorbeeld uit de Suribank-data. Overgang: "Nu een echt Surinaams voorbeeld."''', part=2)

D.frame('bibis', K('Echte casus · Suriname, 30 april 2025') + H('De e-visumchatbot van BIBIS') + R(
    f'<div style="flex:1.6;display:flex;flex-direction:column;gap:20px">' +
    P('Het ministerie van BIBIS lanceerde een e-visumapp met een AI-chatbot, gebouwd met VFS Global. De chatbot beantwoordt 24 uur per dag vragen van reizigers, in het Nederlands en Engels. Volgens het ministerie de eerste overheidsdienst in Suriname die AI zo inzet.', 30) +
    f'<div style="background:{ICE};border-radius:12px;padding:24px 32px;display:flex;flex-direction:column;gap:8px">{P("**Lees- en kijkvragen**", 28, NAVY)}' +
    UL(['Wat typt een reiziger erin?', 'Wie schreef wat de chatbot mag zeggen?', 'Waar draait het taalmodel?', 'Wat doet de reiziger met een fout antwoord?'], 28, ordered=True) + '</div></div>',
    f'<div style="flex:1;display:flex;flex-direction:column;gap:16px;align-items:center;justify-content:center">{qr_svg(URL_BIBIS, 300, label="QR-code naar het artikel van Keynews over de e-visumchatbot")}'
    f'{P("Keynews · open het artikel", 26, MUTED)}{P("Bekendmaking gov.sr, 30 april 2025", 24, MUTED)}</div>'),
    '''[8 min · deel 2 · 0:30] Bron: Keynews, "Suriname lanceert nieuwe e-visumapplicatie en AI-chatbot tijdens bewustwordingssessie", en de Bekendmaking 2025.04.30 op gov.sr. Laat studenten de QR scannen of lees de kern voor (2 min). Zeg: "Dezelfde dag kregen ambtenaren een sessie over verantwoord AI-gebruik. De directeur van e-Gov waarschuwde om gevoelige overheidsgegevens niet zomaar in AI-tools te zetten." Vraag de vier vragen; duo's 3 minuten, dan 3 minuten klassikaal. Verwacht: persoonsgegevens en reisplannen; de instructies komen van ministerie en leverancier; het taalmodel draait waarschijnlijk buiten Suriname; een fout antwoord kan leiden tot een verkeerde aanvraag of een gemiste reis. Brug: "Bij elke vraag hoort een vak van de keten op de volgende dia's." Controleer vlak voor het college of de link werkt; zoek eventueel een STVS- of Starnieuws-fragment.''', part=2)

def keten(items, col):
    cells = []
    for i, (t, q) in enumerate(items):
        last = i == len(items) - 1
        bg, tc, qc = (NAVY, ON_NAVY, ON_NAVY_MUTED) if last else (CARD, NAVY, INK)
        cells.append(f'<div style="flex:1;background:{bg};border:1px solid {LINE};border-radius:12px;padding:24px 12px;display:flex;flex-direction:column;gap:10px;align-items:center">'
                     f'<h3 style="font-size:32px;font-weight:700;color:{tc};text-align:center">{e(t)}</h3>'
                     f'<p style="font-size:26px;line-height:1.25;color:{qc};text-align:center">{e(q)}</p></div>')
        if not last:
            cells.append(f'<p style="font-size:36px;font-weight:700;color:{col};align-self:center">→</p>')
    return f'<div style="display:flex;gap:10px;align-items:stretch">{"".join(cells)}</div>'

D.frame('keten-voorspellend', K('Voorspellend · zoals het kredietmodel van Suribank') + H('Van data tot gevolg') + keten(
    [('Data', 'Wie ontbreekt?'), ('Kenmerken', 'Wat telt mee?'), ('Model', 'Wat leert het?'), ('Kans', 'Hoe zeker?'),
     ('Drempel', 'Wie kiest die?'), ('Beslissing', 'Mens of machine?'), ('Gevolg', 'Voor wie?')], BLUE) +
    D.statement('Bij elke pijl zit een keuze van mensen. Waar kan het hier misgaan, en wie merkt dat?', size=38),
    '''[4 min · deel 2 · 0:38] Teken de keten ook op het bord. Vraag bij elke pijl: "Waar kan het hier misgaan, en wie merkt dat?" Verwacht bij Suribank: data waarin afgewezen aanvragers ontbreken (je weet niet of zij hadden terugbetaald); district als kenmerk; een model dat het verleden herhaalt; een drempel die de bank kiest; een beslissing zonder mens onder SRD 50.000. Overgang: "Bij een chatbot ziet de keten er anders uit."''', part=2)

D.frame('keten-generatief', K('Generatief · zoals een chatbot of agent', color=RED) + H('Van vraag tot gevolg') + keten(
    [('Vraag', 'Wat typt de gebruiker?'), ('Instructies', 'Wie schreef ze?'), ('Taalmodel', 'Waar draait het?'),
     ('Antwoord', 'Klopt het?'), ('Gebruik', 'Wat doet de gebruiker ermee?'), ('Gevolg', 'Voor wie?')], RED) +
    D.statement('Welke van de twee ketens past bij jullie eigen oplossing uit A-AI2?', size=38),
    '''[4 min · deel 2 · 0:42] Koppel aan BIBIS: wat de reiziger typt (persoonsgegevens), wie de instructies en documenten koos (ministerie en VFS Global), waar het taalmodel draait (vaak bij een buitenlandse aanbieder: een deel van de keten zit buiten de organisatie), een antwoord dat vloeiend en toch fout kan zijn, en de reiziger die erop handelt. Vraag: "Welke keten past bij jullie oplossing?" Handen omhoog per keten. Verwacht: de meeste groepen hebben een chatbot of agent. Overgang: "Terug naar Suribank: wat leert een model eigenlijk?"''', part=2)

D.frame('verleden', H('Een model leert het verleden') + R(
    f'<div style="flex:1;border-top:8px solid {RED};padding:28px 0 0;display:flex;flex-direction:column;gap:8px"><p style="font-size:160px;font-weight:700;line-height:1;color:{RED}">49%</p>{P("van de aanvragers uit het **binnenland** betaalde terug", 32)}</div>',
    f'<div style="flex:1;border-top:8px solid {BLUE};padding:28px 0 0;display:flex;flex-direction:column;gap:8px"><p style="font-size:160px;font-weight:700;line-height:1;color:{BLUE_T}">61%</p>{P("van de aanvragers aan de **kust** betaalde terug", 32)}</div>', gap=48) +
    f'<div style="background:{NAVY};border-radius:14px;padding:32px 44px">{P("Uit practicum 1: **is het probleem weg als de bank district weglaat?**", 36, ON_NAVY)}</div>',
    '''[5 min · deel 2 · 0:46] Gebruik de antwoorden op vraag 6 van practicum 1 (blok 0); zet er vooraf twee anonieme antwoorden uit de leeromgeving bij. Vraag: "Wie zegt ja, wie zegt nee?" Laat twee studenten met verschillende antwoorden reageren. Verwacht en kernpunt: het verschil hangt samen met inkomen en soort werk, en die hangen weer samen met waar iemand woont. District weglaten haalt het patroon niet weg (proxy). Zeg: "Een model leert patronen uit het verleden, inclusief eerdere ongelijkheid. Een taalmodel doet hetzelfde met teksten." Bron: oefendataset suribank_kredietaanvragen.csv, 1.200 aanvragen. Overgang: "En wat doet de bank met de uitkomst van het model?"''', part=2)

stap = lambda lab, big, small, col: C(None, f'<p style="font-size:24px;font-weight:700;color:{col};text-transform:uppercase;letter-spacing:1px">{lab}</p><p style="font-size:{60 if len(big) < 6 else 34}px;font-weight:700;color:{NAVY}">{e(big)}</p>{P(small, 26)}', accent=col)
pijl = f'<p style="font-size:40px;font-weight:700;color:{BLUE};align-self:center">→</p>'
D.frame('kans', H('Een kans is geen beslissing') +
    f'<div style="display:flex;gap:14px;align-items:stretch">{stap("Model", "72%", "kans op terugbetaling", BLUE)}{pijl}{stap("Keuze bank", "60%", "drempel", RED)}{pijl}{stap("Advies", "Goedkeuren", "boven de drempel", BLUE)}{pijl}{stap("Keuze bank", "Wie beslist?", "Onder SRD 50.000 automatisch, daarboven een medewerker", RED)}</div>' +
    R(C(None, '**Kies eerst:** wie bepaalt de drempel, of wat een chatbot wel en niet mag zeggen?', size=30, bg=ICE),
      C(None, '**Kies eerst:** is een model dat 69% goed heeft een goed model? Wie kiest iets anders?', size=30, bg=ICE)),
    '''[4 min · deel 2 · 0:51] Zeg: "De uitkomst van het model is een kans. De drempel en wat er daarna gebeurt, zijn keuzes van de organisatie: daarom staat daar Keuze bank. Bij een chatbot is het net zo: de instructies, de documenten en wat er met het antwoord gebeurt, kiest de organisatie, niet het taalmodel." Check met handopsteken, eerst kiezen, dan pas praten. Vraag 1: wie bepaalt de drempel? Verwacht: de bank (en dus is de bank verantwoordelijk). Vraag 2: is 69% goed een goed model? Vraag: "Wie kiest iets anders?" Verwacht: in practicum 1 haalde altijd ja zeggen (Constant) al 59%; het model is maar tien procentpunt beter, en het percentage zegt niets over wie de fouten krijgt. Overgang naar deel 3: "Werkt het dan? Een beetje. Maar dat is maar één van drie vragen."''', part=2)

# ============ Deel 3. Werkt, mag, verantwoord ============
vraag = lambda t, s, gold=False: (f'<div style="flex:1;border-top:6px solid {GOLD if gold else ON_NAVY_MUTED};padding:28px 0 0;display:flex;flex-direction:column;gap:14px">'
                                  f'<h2 style="font-size:60px;font-weight:700;color:{GOLD if gold else ON_NAVY}">{e(t)}</h2>{P(s, 30, ON_NAVY_MUTED)}</div>')
D.frame('drievragen', K('Theorie', dark=True) + R(vraag('Werkt het?', 'Is het model goed genoeg? Een technische vraag. Centraal in A-AI2.'),
    vraag('Mag het?', 'Welke regels gelden? Een juridische vraag. In Suriname vaak kort beantwoord.'),
    vraag('Is het verantwoord?', 'Is het goed om het zó te doen, voor iedereen die geraakt wordt? De vraag van A-ET.', True), gap=40) +
    D.statement('Een systeem kan werken en toegestaan zijn, en toch niet verantwoord.', dark=True, size=44),
    '''[4 min · deel 3 · 0:55] Zeg: "Drie vragen die niet hetzelfde zijn." Vraag: "Welke van de drie stelt A-AI2? En A-DG?" Verwacht: werkt het; mag het met deze data. Zeg: "In Suriname is de tweede vraag vaak kort: er is geen AI-wet en nog geen privacywet in werking. Dat maakt de derde vraag niet kleiner, maar groter." Overgang: "Mag het, is dat hetzelfde als compliance? Niet helemaal."''', dark=True, part=3)


D.frame('compliance', K('Theorie') + H('Recht, compliance en ethiek') + R(
    C('Recht', 'Wetten en regels die gelden. Ze komen vaak pas na schade, en verschillen per land.', label='Wat moet', accent=MUTED),
    C('Compliance', 'Aantonen dat je je houdt aan de wet, aan contracten en aan je eigen beleid. Vaak een vinklijst.', label='Wat je aantoont', accent=BLUE),
    C('Ethiek', 'De vraag of het goed is, voor iedereen die geraakt wordt, ook waar de wet zwijgt of achterloopt.', label='Wat hoort', accent=GOLD)) +
    D.statement('Compliance is de ondergrens, niet het doel.', size=44) +
    C(None, '**Kies eerst:** een organisatie voldoet aan alle regels en aan haar eigen beleid. Is ze daarmee verantwoord bezig? Ja, nee of hangt ervan af?', size=30, bg=ICE),
    '''[3 min · deel 3 · 0:59] Zeg: "Recht zegt wat moet. Compliance is het werk om aan te tonen dat je je daaraan houdt, en aan je eigen beleid: denk aan een compliance officer bij een bank, of aan een audit volgens ISO/IEC 42001. Ethiek vraagt of het goed is, ook als niemand het verplicht." Check: vingers opsteken, 1 = ja, 2 = nee, 3 = hangt ervan af. Verwacht: de meesten kiezen 3. Doorvragen: "Waarvan hangt het af?" Verwacht: van wie de schade draagt, of de regels de nieuwe risico's al dekken, of er uitleg en bezwaar is. Zeg: "In Suriname is er voor AI weinig om compliant mee te zijn. Dan komt het neer op ethiek en op internationale kaders. Werkt jullie partner voor Europese klanten of met Europese data, dan wordt de AI-verordening wel een compliance-eis." Overgang: "Is dat nieuw, dat regels achterlopen? Nee."''', part=3)

D.frame('lessen', K('Lessen uit eerdere technologieën') + H('Regels kwamen telkens na de schade') + G([
    C('De auto', 'Na Unsafe at Any Speed van Ralph Nader (1965) kwamen in de VS in 1966 verplichte veiligheidsnormen, zoals gordels in elke nieuwe auto.', label='1965 → 1966', size=27),
    C('Medicijnen', 'Softenon (thalidomide) werd vanaf 1957 verkocht als veilig slaapmiddel. Duizenden kinderen werden met afwijkingen geboren. Daarna kwam strenger testen vóór toelating.', label='1957 → 1962', size=27),
    C('Sociale media', 'Platforms groeiden jarenlang zonder regels voor hun algoritmes. Europa stelde pas in 2022 de Digital Services Act vast.', label='2004 → 2022', size=27)], 3, 24) +
    D.statement('Bij AI gaat het sneller. Wie nu bouwt en beoordeelt, bepaalt mee wat normaal wordt.', size=38),
    '''[4 min · deel 3 · 1:02] Zeg: "Drie voorbeelden met hetzelfde patroon: een nieuwe technologie, snelle groei, schade bij mensen die er niet om vroegen, en pas daarna regels." Auto: Ralph Nader, Unsafe at Any Speed (1965); in 1966 de National Traffic and Motor Vehicle Safety Act, met federale veiligheidsnormen. Medicijnen: thalidomide (Softenon) kwam in 1957 op de markt, werd in 1961 teruggetrokken; wereldwijd werden meer dan 10.000 kinderen met afwijkingen geboren; in 1962 kwamen in de VS de Kefauver-Harris Amendments, met strengere eisen aan bewijs van veiligheid en werking. Sociale media: de Digital Services Act (Verordening (EU) 2022/2065). Vraag: "Welke les past het best bij AI in Suriname, waar nog geen AI-wet is?" Verwacht: niet wachten op de wet; testen vóór gebruik (zoals bij medicijnen); wie bouwt, draagt verantwoordelijkheid. Zeg: "Daarom testen jullie in practicum 4 je eigen oplossing voordat iemand anders er last van heeft." Overgang: "Een recent voorbeeld waar het misging, in een land mét regels."''', part=3)

D.frame('rotterdam', K('Echte casus · Nederland, 2017–2021') + H('Rotterdam: werkte, mocht, maar was het verantwoord?') + R(
    f'<div style="flex:1.6;display:flex;flex-direction:column;gap:20px">' +
    P('Rotterdam gaf bijstandsontvangers een risicoscore voor fraudeonderzoek, met ruim 300 kenmerken, zoals leeftijd, geslacht en taalvaardigheid. Journalisten kregen het model in handen: jonge moeders en mensen die slecht Nederlands spreken, scoorden vaker hoog. De gemeente legde het eind 2021 stil.', 30) +
    f'<div style="background:{ICE};border-radius:12px;padding:24px 32px;display:flex;flex-direction:column;gap:8px">{P("**Kies eerst, per vraag: ja, nee of twijfel**", 28, NAVY)}' +
    UL(['Werkte het? Mocht het? Was het verantwoord?', 'Wat zegt de lens gevolgen, en wat de lens rechtvaardigheid?', 'Wie had het kunnen stoppen, en wie deed het?'], 28, ordered=True) + '</div></div>',
    f'<div style="flex:1;display:flex;flex-direction:column;gap:16px;align-items:center;justify-content:center">{qr_svg(URL_ROT, 300, label="QR-code naar de serie Suspicion Machines van Lighthouse Reports")}'
    f'{P("Lighthouse Reports · Suspicion Machines (maart 2023)", 24, MUTED)}{P("Interactief: WIRED, Inside the Suspicion Machine", 24, MUTED)}</div>'),
    '''[5 min · deel 3 · 1:06] Bronnen: Lighthouse Reports, serie "Suspicion Machines" (maart 2023, met WIRED, Vers Beton, Follow the Money en Argos); WIRED, "Inside the Suspicion Machine", 7 maart 2023, met een interactieve uitleg van de score; Binnenlands Bestuur: "Algoritme ziet jonge moeders en anderstaligen als risicogroep voor bijstandsfraude". Laat zo mogelijk 2 minuten de interactieve WIRED-pagina zien (test vooraf). Vraag de drie vragen; eerst iedereen tegelijk vingers: 1 = ja, 2 = nee, 3 = twijfel. Verwacht: werkte matig (experts: nauwelijks beter dan willekeurig); mocht jarenlang; niet verantwoord voor groepen die hoger scoorden door kenmerken waar ze niets aan kunnen doen. De Rekenkamer Rotterdam waarschuwde in 2021; de gemeente stopte. Brug: "Hoe weeg je dat? Daarvoor gebruiken we vier lenzen." Let op: de toeslagenaffaire komt terug in kennispakket 1 en in college 2.''', part=3)

lens = lambda t, th, q: C(t, P(q, 28), label=th, accent=BLUE, size=28)
D.frame('lenzen', H('Vier lenzen om een keuze te wegen') + G([
    lens('Gevolgen', 'Utilitarisme', 'Welke keuze levert de meeste baten en de minste schade op, voor wie en op welke termijn?'),
    lens('Rechten en plichten', 'Deontologie', 'Welke rechten, plichten en grenzen gelden, ongeacht het nut?'),
    lens('Rechtvaardigheid', 'Rechtvaardigheidstheorie (Rawls)', 'Zijn kansen, lasten en risico’s eerlijk verdeeld, ook voor wie het zwakst staat?'),
    lens('Professionele integriteit', 'Deugdethiek, zorgethiek en beroepscodes', 'Wat vraagt zorgvuldig vakmanschap, en wat heeft wie van ons afhankelijk is nodig?')], 2, 28),
    '''[5 min · deel 3 · 1:11] Zeg per lens één zin en noem de theorie: gevolgen is utilitarisme, rechten en plichten is deontologie, rechtvaardigheid is de rechtvaardigheidstheorie van Rawls, professionele integriteit is deugdethiek en beroepscodes, aangevuld met zorgethiek (Carol Gilligan, Joan Tronto): wie is van het systeem afhankelijk, wie kan zich niet goed verweren, en wat vraagt goede zorg voor die mensen? Bij Suribank: de aanvrager uit het binnenland die geen uitleg krijgt en niemand kan bellen. "In het dilemma-canvas (K5) noem je de lens én de theorie." Valkuilen: bij gevolgen worden kleine of kwetsbare groepen weggemiddeld; rechten en plichten lossen botsende rechten niet vanzelf op; van eerlijk bestaan meerdere, soms tegenstrijdige definities; professionele integriteit kan zonder criteria vaag blijven. Overgang: "Nu zelf: elk groepje krijgt één lens."''', part=3)

D.frame('opdracht-lens', D.werkblok('9 min werken + 6 min verslag', 'Groepjes van 3–4') + H('Bekijk Suribank door één lens') +
    UL(['Elk groepje krijgt één lenzenkaart.', 'Beantwoord de hulpvragen op de kaart.', 'Formuleer één conclusie en noem de theorie achter je lens.'], 32, ordered=True) +
    f'<div style="background:{ICE};border-radius:12px;padding:28px 36px">{P("“Vanuit onze lens mag Suribank dit **wel** / **niet** / **alleen onder deze voorwaarden**, omdat …”", 32, NAVY)}</div>' +
    D.klaar('één conclusiezin in deze vorm, de theorie genoemd, en één hulpvraag waarop jullie géén antwoord wisten.'),
    '''[15 min · deel 3 · 1:16] Deel de vier lenzenkaarten uit (A5, zie docentvoorbereiding); bij meer dan vier groepjes krijgen sommige lenzen twee groepjes. 9 minuten werken. Loop rond. Docentvraag: "Welke hulpvraag kunnen jullie niet beantwoorden, en welke informatie zou je daarvoor nodig hebben?" Daarna per lens hoogstens 90 seconden verslag (6 min); vul tijdens het verslag de tabel op de volgende dia. Overgang: "Valt jullie iets op als we de vier naast elkaar zetten?"''', part=3)

D.frame('tegenspraak', H('De lenzen spreken elkaar tegen') + D.table(
    ['Lens', 'Mag het?', 'Belangrijkste argument'],
    [['Gevolgen', ' ', ' '], ['Rechten en plichten', ' ', ' '], ['Rechtvaardigheid', ' ', ' '], ['Professionele integriteit', ' ', ' ']], 30, ['30%', '20%', '50%']) +
    D.statement('Daarom heb je een gestructureerde afweging nodig. Die leer je in deze module.', size=38),
    '''[4 min · deel 3 · 1:31] Vul de tabel tijdens het verslag in, op het scherm of op het bord: wel, niet of onder voorwaarden, en het belangrijkste argument. Spreekpunten. Gevolgen: snelheid en meer leningen voor veel mensen, maar welke schade voor wie onterecht wordt afgewezen? Rechten en plichten: heeft een aanvrager recht op uitleg en op een menselijke beoordeling, ook bij een klein bedrag? Rechtvaardigheid: mensen uit het binnenland lopen meer kans op een afwijzing; is dat eerlijk als het verschil voortkomt uit inkomen en soort werk? Professionele integriteit: mag een medewerker zich achter het model verschuilen? Zeg: "Vóór 4 februari werk je zo'n afweging uit voor een dilemma uit jullie eigen casus, individueel, in het dilemma-canvas." Overgang: pauze.''', part=3)

D.frame('pauze', f'<div style="flex:1;display:flex;flex-direction:column;justify-content:center;gap:28px"><h1 style="font-size:160px;font-weight:700;line-height:1;color:{ON_NAVY};text-transform:uppercase">Pauze</h1>{P("10 minuten · we gaan verder om [__:__]", 44, GOLD, 700)}</div>',
    '''[10 min · pauze · 1:35] Vul de tijd in. Laat de woorden van het bord uit deel 1 staan.''', dark=True)

# ============ Deel 4. Kader en eindproduct ============
D.frame('suriname', H('AI-beleid in Suriname: nog in opbouw') + R(
    C('Geen AI-wet', 'Er zijn geen regels die specifiek over AI gaan.', accent=RED),
    C('Nog geen privacywet', 'De ontwerpwet Bescherming Privacy en Persoonsgegevens ligt bij De Nationale Assemblée.', accent=RED),
    C('UNESCO-traject', 'Sinds 27 augustus 2026 een AI Readiness Assessment, als basis voor een nationale AI-strategie.', accent=GREEN)) +
    P('Daarom werken we met internationale kaders. De Europese AI-verordening gebruiken we als vergelijking. Voorbeeld: voor chatbots geldt daar een transparantieplicht (artikel 50): mensen moeten weten dat ze met AI praten.', 30),
    '''[4 min · deel 4 · 1:45] Zeg: "Suriname heeft nog geen AI-wet en geen privacywet in werking. Sinds 27 augustus 2026 voert Suriname met UNESCO een AI Readiness Assessment uit." Vraag: "Bij BIBIS: wie houdt toezicht als er geen AI-wet is?" Verwacht: het ministerie zelf, e-Gov, de leverancier via het contract; niemand onafhankelijk. Controleer vlak voor het college of er nieuws is over de ontwerpwet of het UNESCO-traject en pas de dia aan (bron op de bronnendia). Overgang: "Zonder wet heb je een kader nodig. Dit is het onze."''', part=4)

laag = lambda l, t, s, erbij, dark=False: (f'<div style="flex:1;background:{NAVY if dark else CARD};border:1px solid {LINE};border-radius:14px;padding:30px;display:flex;flex-direction:column;gap:12px">'
    f'<p style="font-size:26px;font-weight:700;color:{GOLD if dark else BLUE_T};text-transform:uppercase;letter-spacing:2px">{l}</p>'
    f'<h3 style="font-size:34px;font-weight:700;color:{ON_NAVY if dark else NAVY}">{e(t)}</h3>{P(s, 26, ON_NAVY_MUTED if dark else INK)}'
    f'<p style="font-size:24px;line-height:1.35;color:{ON_NAVY if dark else INK};border-top:2px solid {"#33507F" if dark else LINE};padding:14px 0 0">{e(erbij)}</p></div>')
D.frame('aanpak', H('Eén kader, vier lagen') + R(
    laag('Wat', '11 domeinen', 'Waarop je je oplossing beoordeelt.', '**Erbij:** IEEE CertifAIEd, met transparantie, verantwoording, bias en privacy', True),
    laag('Hoe', 'NIST AI RMF', 'Govern, Map, Measure, Manage.', '**Erbij:** ISO/IEC 42001 (managementsysteem) en AIGP'),
    laag('Waarom', 'UNESCO en vier lenzen', 'De waarden achter elk oordeel.', '**Erbij:** OECD-principes; elke lens met de theorie, zoals in CEET'),
    laag('Waar', 'Surinaamse wet en beleid', 'Wat juridisch geldt.', '**Erbij:** de AI-verordening (EU), als vergelijking'), gap=22) +
    f'<div style="background:{ICE};border-radius:12px;padding:22px 32px">{P("**In de minor:** A-AI2: hoe de oplossing werkt · A-DG: de data · A-ET: de gevolgen voor mensen, en wie daarover beslist", 28, NAVY)}</div>',
    '''[5 min · deel 4 · 1:49] Zeg: "Eén kader, vier lagen. Kom je een nieuwe norm tegen, vraag dan: in welke laag hoort deze?" Wat: de 11 domeinen; IEEE CertifAIEd hangt erin met vier ontologieën (transparantie bij domein 6, verantwoording bij 2, bias bij 5, privacy bij 4). Hoe: NIST AI RMF; ISO/IEC 42001 voegt het managementsysteem toe (plan-do-check-act), AIGP de governance bij bouwen en bij gebruik. Waarom: UNESCO, OECD en de vier lenzen. Waar: Surinaamse wet en beleid; de AI-verordening als vergelijking, en als eis bij Europese klanten of data. "Je hoeft ze niet uit je hoofd te kennen: de Kaderkaart in de map Naslag laat zien waar je wat vindt. Kaderclip A in kennispakket 1 herhaalt dit overzicht." Leg de onderste balk uit: wat A-AI2 en A-DG opleveren, mag je als bewijs gebruiken. Overgang: "Wat in de laag Wat staat, zijn de 11 domeinen."''', part=4)

dom = ['Doel, noodzaak en proportionaliteit', 'Governance en verantwoording', 'Stakeholders, mensenrechten en impact', 'Data en privacy',
       'Fairness en non-discriminatie', 'Transparantie en uitlegbaarheid', 'Menselijke controle, bezwaar en herstel', 'Veiligheid, security en robuustheid',
       'AI-geletterdheid', 'Duurzaamheid en bredere impact', 'Monitoring, audit en verbetering']
D.frame('domeinen', H('De 11 domeinen') + G([
    f'<div style="background:{CARD};border:1px solid {LINE};border-radius:12px;padding:20px 24px;display:flex;gap:16px;align-items:baseline"><p style="font-size:30px;font-weight:700;color:{BLUE_T}">{i + 1}</p><p style="font-size:28px;line-height:1.25;color:{NAVY}">{e(t)}</p></div>'
    for i, t in enumerate(dom)], 3, 18),
    '''[3 min · deel 4 · 1:54] Laat de 11 domeinen zien, leg ze niet allemaal uit. Zeg: "Dit is de checklist waarmee jullie straks je eigen oplossing doorlichten. In blok 1 geven jullie alle 11 een score van 0 tot 3, en werken jullie er 3 tot 4 uit met bewijs: uit gesprekken met de partner, uit A-AI2 en A-DG, en uit jullie eigen test in practicum 4." Vraag: "Welk domein speelde net bij Rotterdam het sterkst?" Verwacht: 5 (fairness), 6 (transparantie), 7 (menselijke controle). Overgang: "Hoe wordt dat een rapport?"''', part=4)

stappen = [('1 · blok 1', 'Bewijs'), ('2 · blok 1', 'Gap'), ('3 · blok 1, canvas', 'Dilemma'), ('4 · blok 1', 'Risico'),
           ('5 · blok 2', 'Eis'), ('6 · blok 2', 'Maatregel'), ('7 · blok 3', 'Monitoring'), ('8 · blok 3', 'Oordeel')]
D.frame('redeneerketen', H('De redeneerketen: van bewijs tot oordeel', dark=True) +
    f'<div style="display:flex;flex-direction:column;gap:14px"><p style="font-size:26px;font-weight:700;color:{GOLD};letter-spacing:1px;text-transform:uppercase">Vandaag · K1: de afbakening vóór stap 1</p></div>' +
    G([f'<div style="border-top:6px solid {GOLD if i == 7 else ON_NAVY_MUTED};padding:22px 0 0;display:flex;flex-direction:column;gap:8px"><p style="font-size:24px;font-weight:700;color:{GOLD}">{w}</p><h3 style="font-size:42px;font-weight:700;color:{GOLD if i == 7 else ON_NAVY}">{t}</h3></div>'
       for i, (w, t) in enumerate(stappen)], 4, 28) +
    P('Elke stap volgt uit de vorige. Een oordeel zonder bewijs telt niet.', 32, ON_NAVY_MUTED),
    '''[3 min · deel 4 · 1:57] Zeg: "Het rapport groeit per blok langs deze keten: bewijs, gap, dilemma, risico, eis, maatregel, monitoring, oordeel. Vandaag doen jullie de stap ervóór: afbakenen. Zonder heldere afbakening wordt elke latere stap vaag." Overgang: "En aan het eind beantwoord je één vraag."''', dark=True, part=4)

D.frame('eindproduct', K('Het eindproduct beantwoordt één vraag') +
    f'<h1 style="font-size:84px;font-weight:700;line-height:1.08;color:{NAVY}">Is jullie oplossing verantwoord inzetbaar, en onder welke voorwaarden?</h1>' +
    R(*[f'<div style="flex:1;background:{bg};border-radius:14px;padding:28px 32px"><p style="font-size:32px;font-weight:700;color:{fc}">{t}</p></div>'
        for t, bg, fc in [('Verantwoord inzetbaar', GREEN, '#FFFFFF'), ('Inzetbaar onder voorwaarden', GOLD, NAVY), ('Nu niet', RED, '#FFFFFF')]]) +
    P('“Nu niet” is een volwaardig advies, geen mislukking.', 30, MUTED),
    '''[4 min · deel 4 · 2:00] Zeg: "Het eindrapport eindigt met een beslismemo van één pagina, met een van deze drie oordelen." Laat kort het voorbeeldrapport zien (ClaimWacht bij Tamarinde, fictief): het beslismemo vooraan en de kanttekeningen van de docent na elk hoofdstuk. "Jullie onderbouwen het oordeel met bewijs, het liefst uit een eigen test van jullie oplossing (practicum 4). Wie na de maatregelen opnieuw test, laat zien dat ze werken: dat telt mee voor excellent." Overgang: "Hoe wordt dat beoordeeld?"''', part=4)

D.frame('toetsing', H('Toetsing: twee momenten, elk met een groeps- en een eigen deel') + D.table(
    ['Onderdeel', 'Inleveren', 'Wat', 'Eindcijfer'],
    [['A1 groepsdeel', 'do 4 februari', 'Tussenrapport H1–H5, max. 8 pagina’s', '18%'],
     ['A1 individueel', 'do 4 februari', 'Dilemma-canvas, 800–1000 woorden', '12%'],
     ['A2 groepsdeel', 'do 11 maart', 'Eindrapport H1–H8 en beslismemo, max. 12 pagina’s', '42%'],
     ['A2 individueel', 'do 11 maart', 'Reflectie, 1500–2000 woorden', '28%']], 28, ['26%', '20%', '40%', '14%']) +
    P('Eindcijfer minimaal **5,5**. Rubric en voorbeeldrapport staan onder Algemeen: ICT A-ET Beoordelingsrubric en ICT A-ET Voorbeeldrapport.', 28),
    '''[6 min · deel 4 · 2:04] Zeg: "Assessment 1 telt 30%, Assessment 2 70%. Binnen elke toets is het groepsdeel 60% en het individuele deel 40%, zodat elke student een eigen cijfer krijgt. Elke student is eigenaar van benoemde hoofdstukken; peerbeoordeling kan het groepscijfer per student verlagen bij aantoonbaar te weinig bijdrage." Laat 3 minuten de rubric zien, met criterium 1, Afbakening, context en stakeholders: daar krijgt K1 feedback op. Bij A1 mag het testverslag van practicum 4 als bijlage (sterk aanbevolen); dat telt niet mee voor de 8 pagina’s. Overgang naar deel 5: "Nu jullie eigen casus."''', part=4)

# ============ Deel 5. Jullie casus: K1 ============
D.frame('kies-casus', H('Jullie casus: de oplossing uit A-AI2') + R(
    C('Standaard', 'De oplossing die jullie in A-AI2 verder bouwen, met de partner uit A-AI2 als organisatie. Zelfde groep in drie vakken.', dark=True, flex=1.3),
    C('Uitzondering 1', 'Raakt jullie oplossing nauwelijks mensen? Kies een andere organisatie, met een contactpersoon die meewerkt.'),
    C('Uitzondering 2', 'Lopen jullie vast? Werk met het Suribank-casusdossier. Wisselen kan tot maandag 25 januari.')) +
    P('Een geschikte casus: de oplossing beïnvloedt uitkomsten voor mensen, er is genoeg bewijs, en het past in tien weken. **Vrijdag 8 januari bevestig ik per groep de casus.**', 28),
    '''[3 min · deel 5 · 2:10] Groepen leggen hun beschrijving uit blok 0 op tafel en toetsen die aan de drie eisen onderaan. Bewijs komt uit gesprekken met de partner, ontwerpkeuzes, tests en de documentatie uit A-AI2 en A-DG. Onderzoeksethiek, ook zonder Surinaamse privacywet: de contactpersoon geeft toestemming (ICT A-ET Toestemmingsformulier interview, map Naslag), gesprekspartners mogen weigeren, geen persoonsgegevens van klanten of medewerkers, en anonimiseren tenzij de organisatie anders wil. Voorbeeld van uitzondering 1: een interne tool die vergaderverslagen samenvat. Overgang: "Zo ziet een uitgewerkt canvas eruit."''', part=5)

D.frame('k1-voorbeeld', K('Zo werk je K1 uit') + H('Vier velden van Suribank') + D.table(
    ['Veld', 'Suribank'],
    [['6 · Output', 'Een kans van 0 tot 100% en een advies: goedkeuren boven 60%, anders afwijzen'],
     ['7 · Beslissing', 'Onder SRD 50.000 wordt het advies automatisch overgenomen; daarboven beslist een kredietmedewerker'],
     ['9 · Betrokkenen', 'Aanvragers, vooral uit het binnenland en met informeel werk, en hun gezinnen'],
     ['13 · Zorg', 'Bij kleine bedragen kijkt geen mens mee en krijgt niemand uitleg (UNESCO: menselijk toezicht; transparantie)']], 29, ['26%', '74%']) +
    D.statement('Let op het verschil tussen output en beslissing, en tussen gebruikers en betrokkenen.', size=34),
    '''[3 min · deel 5 · 2:13] Zeg: "Output is wat het model maakt. Beslissing is wat de organisatie ermee doet, en wie dat doet. Betrokkenen zijn mensen die de gevolgen merken, ook als ze het systeem nooit zien: de gezinnen." Vraag: "Wie is bij Suribank gebruiker, en wie betrokkene?" Verwacht: kredietmedewerkers en het hoofd kredietverlening zijn gebruikers; aanvragers en gezinnen betrokkenen. Het volledige voorbeeld staat in de studentversie en in het werkboek. Overgang: "Het lastigste veld is 13: de zorgen."''', part=5)

niv = lambda lab, col, t, fc='#FFFFFF': (f'<div style="display:flex;gap:0;border:1px solid {LINE};border-radius:14px;overflow:hidden">'
    f'<p style="width:260px;flex:none;background:{col};color:{fc};font-size:30px;font-weight:700;padding:28px">{lab}</p>'
    f'<p style="flex:1;background:{CARD};font-size:30px;line-height:1.35;color:{INK};padding:28px 32px">{e(t)}</p></div>')
D.frame('niveaus', H('Eén zorg op drie niveaus') + niv('Zwak', RED, 'Het model kan bias hebben.') +
    niv('Redelijk', GOLD, 'Mensen uit het binnenland worden vaker afgewezen.', NAVY) +
    niv('Professioneel', GREEN, 'Aanvragers uit het binnenland lopen meer kans op een onterechte afwijzing, omdat bij informeel werk vaker het inkomen ontbreekt; onder SRD 50.000 kijkt geen mens mee. Bewijs nodig: fouten per regio (practicum 4).') +
    P('Professioneel = **wie** · **hoe** · **waardoor** · **hoe je het aantoont**', 32, NAVY),
    '''[3 min · deel 5 · 2:16] Zeg: "Professioneel betekent: wie wordt geraakt, hoe, waardoor, en hoe je het gaat aantonen. Dat is de redeneerketen in het klein." Vraag: "Wat mist er in de redelijke versie?" Verwacht: waardoor (informeel werk, ontbrekend inkomen), en welk bewijs. Overgang: "Nu jullie: twee fragmenten van een andere groep."''', part=5)

frag = lambda lab, t: (f'<div style="flex:1;background:{CARD};border:1px solid {LINE};border-top:6px solid {BLUE};border-radius:14px;padding:30px 34px;display:flex;flex-direction:column;gap:14px">'
                       f'<p style="font-size:28px;font-weight:700;color:{BLUE_T};text-transform:uppercase;letter-spacing:1px">{lab}</p>{P(t, 29)}</div>')
D.frame('fragmenten', K('Kwaliteitscheck · duo · 5 minuten') + H('Markeer de schakels: wie, hoe, waardoor, bewijs') + R(
    frag('Fragment A', '“Een zorg is dat de chatbot soms verkeerde antwoorden geeft. Dat is slecht voor de klanten en voor de organisatie.”'),
    frag('Fragment B', '“Oudere klanten die niet gewend zijn aan chat, volgen een fout antwoord over vergoedingen vaker op zonder het te controleren, omdat de chatbot niet zegt dat hij AI is en niet doorverwijst naar een medewerker. Dit toetsen we met twintig lastige vragen uit de klachtenlijst.”')) +
    P('Welke schakels ontbreken in A? Herschrijf A in één zin tot het niveau van B.', 30, NAVY, 700),
    '''[5 min · deel 5 · 2:19] Fragmenten zijn geconstrueerd (een fictieve groep met een chatbot van een zorgverzekeraar). Duo's, 3 minuten: markeer in B wie (oudere klanten die niet gewend zijn aan chat), hoe (volgen een fout antwoord op), waardoor (geen AI-melding, geen overdracht aan een mens) en bewijs (twintig lastige vragen). Vraag: "Welke schakel ontbreekt in fragment A?" Verwacht: alle vier; "de klanten" is geen wie, "slecht" is geen hoe. Laat 2 duo's hun herschreven zin voorlezen. Zeg: "Dit niveau vraag ik in veld 13. En het is meteen de stelling op het exit ticket: weet de klant dat het AI is?" Overgang: "Zo meet je of jullie canvas goed genoeg is."''', part=5)

lat = lambda lab, col, fc, t: (f'<div style="flex:1;background:{CARD};border:1px solid {LINE};border-radius:14px;overflow:hidden;display:flex;flex-direction:column">'
    f'<p style="background:{col};color:{fc};font-size:32px;font-weight:700;padding:18px 28px">{lab}</p>{UL(t, 27)}</div>')
D.frame('lat-k1', H('Is jullie K1 basis, goed of sterk?') + R(
    lat('Basis', ICE, NAVY, ['Alle 13 velden ingevuld', 'Output en beslissing apart', 'Vijf teamafspraken']),
    lat('Goed', BLUE_T, '#FFFFFF', ['Plus: betrokkenen naast gebruikers', 'Concrete afbakening: wat níet', 'Bewijsbronnen uit A-AI2 en A-DG']),
    lat('Sterk', NAVY, GOLD, ['Plus: zorgen op professioneel niveau', 'Elke zorg met een UNESCO-principe', 'Keten naar externe diensten zichtbaar'])) +
    P('Dit sluit aan op rubriccriterium 1, **Afbakening, context en stakeholders**. Lever minstens “goed” in.', 30),
    '''[2 min · deel 5 · 2:24] Zeg: "Lever minstens goed in. De feedforward van maandag gaat over de stap naar sterk." Koppeling rubric criterium 1: voldoende = toepassing en afbakening helder, direct en indirect geraakten, datastroom op hoofdlijnen; goed = kwetsbare groepen en waar de mens zit; excellent = het beeld verklaart al waar de risico's vandaan komen. Overgang: "Aan de slag."''', part=5)

D.frame('k1-canvas', D.werkblok('16 min', 'Groep') + H('K1-canvas: wat onderzoeken jullie precies?') +
    G([f'<div style="background:{CARD};border:1px solid {LINE};border-radius:10px;padding:12px 18px;display:flex;gap:12px;align-items:baseline"><p style="font-size:26px;font-weight:700;color:{BLUE_T}">{i + 1}</p><p style="font-size:26px;color:{NAVY}">{t}</p></div>'
       for i, t in enumerate(['Organisatie en context', 'Probleem', 'AI-toepassing', 'Soort AI', 'Input', 'Output', 'Beslissing', 'Gebruikers', 'Betrokkenen',
                              'Doel en succes', 'Afbakening', 'Casus en bewijs', 'Drie eerste zorgen'])] +
      [f'<div style="background:{NAVY};border-radius:10px;padding:12px 18px"><p style="font-size:26px;font-weight:700;color:{GOLD}">+ Vijf teamafspraken</p></div>'], 5, 14) +
    D.klaar('alle 13 velden in één zin; output en beslissing apart; minstens één betrokkene die het systeem niet gebruikt; drie zorgen met wie, hoe en waardoor.', 28) +
    P('**Nu verwerken, niet thuis:** de laatste 4 minuten zet je het canvas in de werkboektab K1_Scope (één laptop per groep). Chatbot of agent? Vul ook de vragen voor generatieve AI in.', 27),
    '''[16 min · deel 5 · 2:26] 12 minuten invullen, 4 minuten in de werkboektab K1_Scope zetten (wie op A3 werkte, maakt een foto). Loop rond. Docentvragen: "Wat gebeurt er direct ná de output, en wie merkt dat?" · "Wie gebruikt het, en wie merkt de gevolgen zonder het zelf te gebruiken?" · "Welke gegevens gaan naar een externe dienst?" · "Wat onderzoeken jullie bewust niet?" · Bij een chatbot of agent: "Weet de gebruiker dat het AI is, en kan die een mens bereiken?" Teamafspraken: wie coördineert, wie is eigenaar van welke hoofdstukken, wanneer overleggen jullie, hoe verdelen jullie het werk naast A-AI2 en A-DG, en wat doen jullie als iemand niet levert. Overgang: "Ruil je canvas met de buurgroep."''', part=5)

D.frame('canvasruil', D.werkblok('10 min', 'Twee groepen') + H('Ruil je canvas') +
    UL(['Staat er een betrokkene die het systeem níet gebruikt?', 'Is duidelijk wat er ná de output gebeurt, en wie dat beslist?', 'Is elke zorg professioneel: wie, hoe, waardoor, bewijs?'], 32, ordered=True) +
    R(C(None, '**6 minuten:** lees het canvas van de buurgroep en schrijf bij elke vraag één opmerking.', size=28),
      C(None, '**4 minuten:** terug naar je eigen canvas. **Na afloop verbeter je minimaal één veld.**', size=28, accent=GOLD)),
    '''[10 min · deel 5 · 2:42; loopt door tot 2:52] Koppel groepen per twee. Loop rond. Vraag: "Welke opmerking van de andere groep nemen jullie over, en welke bewust niet?" Laat aan het eind één groep in 30 seconden zeggen welk veld ze verbeterden. Overgang: "Hoe werk je tot college 2, en daarna?"''', part=5)

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

D.frame('deze-week', H('Tot college 2') + R(
    C('Uiterlijk zondag 10 januari, 23:59', UL(['K1-canvas met teamafspraken → **ICT A-ET K1**', 'Kennispakket 1: clip 5, kaderclip A en de kernbron UNESCO (hoofdstuk III)'], 28), accent=BLUE),
    C('Uiterlijk dinsdag 12 januari, 23:59', UL(['Drie vragen voor de gastspreker', 'Twee debatstellingen, elk met twee bronnen', '→ **ICT A-ET Voorbereiding college 2**'], 28), accent=GOLD)) +
    P('Vrijdag 8 januari: casus bevestigd. Maandag 11 januari: feedforward per groep op K1. Vast? Veelgestelde vragen, Begrippenlijst en Kaderkaart in de map Naslag; daarna [kanaal].', 27, MUTED),
    '''[3 min · deel 6 · 2:53] Loop de lijst door. Zeg: "Vragen en stellingen zijn voor college 2 op donderdag 14 januari, met de gastspreker [naam, organisatie]. Een goede stelling is één zin, echt betwistbaar, met een botsing tussen twee waarden." Overgang: "Nog één ding voordat je gaat."''', part=6)

D.frame('exit', K('Exit ticket · 4 minuten · ICT A-ET Exit ticket college 1', dark=True) +
    UL(['Het grootste ethische risico van onze oplossing is …, omdat …', 'Welke lens vind jij voor onze casus het belangrijkst, en waarom?', 'Wat is mij nog onduidelijk over K1?',
        'Bonus: je stem van vandaag, groen, rood of geel? En nu?'], 34, ON_NAVY, ordered=True) +
    f'<div style="background:#0B2A6B;border-radius:14px;padding:24px 32px">{P("**Stelling om over na te denken:** “Een organisatie mag een chatbot namens een medewerker laten antwoorden, zolang de klant geen verschil merkt.”", 28, ON_NAVY)}</div>' +
    D.statement('Een systeem kan werken en toegestaan zijn, en toch niet verantwoord. Dat beoordelen is jullie vak in deze module.', dark=True, size=36),
    '''[4 min · deel 6 · 2:56] Studenten vullen het exit ticket in bij de MyCampus-opdracht ICT A-ET Exit ticket college 1 (telefoon of laptop), individueel. Lees de stelling voor: "Hij komt terug in kennischeck 1; neem hem mee naar het debat in college 2." Sluit af met de kernboodschap. Na het college: lees de antwoorden en gebruik ze in het feedforward-bericht van maandag; noteer de stemming (bonusvraag) naast de telling van deel 1.''', dark=True, part=6)

D.frame('bronnen', H('Bronnen') + UL([
    'UNESCO (2021). Recommendation on the Ethics of Artificial Intelligence, hoofdstuk III. unesdoc.unesco.org/ark:/48223/pf0000381137',
    'OECD (2019, herzien 2024). Recommendation of the Council on Artificial Intelligence (OECD AI Principles).',
    'NIST (2023). AI Risk Management Framework 1.0 (NIST AI 100-1), functie Map, MAP 1.1.',
    'ISO/IEC 42001:2023. Artificial intelligence: management system, clausule 4.1 en 4.3.',
    'Verordening (EU) 2024/1689 (AI-verordening), art. 3, art. 6 met bijlage III punt 5(b), art. 50.',
    'IEEE CertifAIEd, ontologieën transparantie, verantwoording, algoritmische bias en privacy.',
    'Regering van Suriname (30 april 2025). Bekendmaking 2025.04.30; Keynews, e-visumapplicatie en AI-chatbot.',
    'Lighthouse Reports (maart 2023). Suspicion Machines; WIRED (7 maart 2023). Inside the Suspicion Machine.',
    'UNESCO en Suriname (2026). AI Readiness Assessment [link controleren].',
    'Nader, R. (1965). Unsafe at Any Speed; Kefauver-Harris Amendments (1962), na thalidomide; Verordening (EU) 2022/2065 (Digital Services Act).',
    'Gilligan, C. (1982). In a Different Voice; Tronto, J. (1993). Moral Boundaries (zorgethiek).',
    'Suribank en de oefendataset suribank_kredietaanvragen.csv zijn fictief (A-ET, 2026).'], 22),
    '''[niet tonen tenzij gevraagd] Bronnen bij de dia's. Controleer vóór het college de links van BIBIS, Rotterdam en het UNESCO-traject.''')

D.frame('docent-voorbereiding', K('Docent · niet tonen') + H('Voorbereiding college 1') + G([
    UL(['Kaarten groen, rood, geel (of Mentimeter klaarzetten)', 'Beginquiz: twee begrippen en percentages op dia “quiz”', 'Twee anonieme antwoorden op vraag 6 van practicum 1 (dia “verleden”)',
        'Lenzenkaarten A5 printen, vier lenzen × aantal groepjes', 'K1-canvas A3 per groep'], 26),
    UL(['Links BIBIS en Rotterdam testen (QR en WIRED-pagina)', 'Nieuws ontwerpwet privacy en UNESCO-traject checken', 'Tijd, lokaal, je achternaam en de pauzetijd invullen',
        'Inleverpunten K1, Voorbereiding college 2 en Exit ticket college 1 open', 'Telling van de stemming noteren (terug in college 3)'], 26)], 2, 40),
    '''Deze dia staat achteraan en wordt niet getoond. Na het college: exit tickets lezen, casus per groep bevestigen (vr 8 januari), feedforward-bericht (ma 11 januari).''')

if __name__ == '__main__':
    src, out = sys.argv[1], sys.argv[2]
    sections = {
        's1': {'description': 'Deel 1. Rolwissel, leerdoelen en het dilemma van Suribank', 'start': 'cover'},
        's2': {'description': 'Deel 2. Van data tot beslissing: de keuzes van mensen in de keten', 'start': 'quiz'},
        's3': {'description': 'Deel 3. Werkt het, mag het, is het verantwoord? Recht en compliance, lessen uit eerdere technologie, vier lenzen', 'start': 'drievragen'},
        's4': {'description': 'Deel 4. Suriname, het kader en het eindproduct', 'start': 'suriname'},
        's5': {'description': 'Deel 5. Jullie casus: K1-canvas met kwaliteitscheck en canvasruil', 'start': 'kies-casus'},
        's6': {'description': 'Deel 6. Drie colleges en vier blokken, tot college 2, exit ticket, bronnen en docentvoorbereiding', 'start': 'blokken'},
    }
    idx = D.write(out, src + '/project/deck.json', 'College 1 AI & Ethics: Wat staat er op het spel?', sections, {})
    print(len(idx['order']), 'dia\'s')
