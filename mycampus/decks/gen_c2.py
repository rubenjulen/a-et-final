#!/usr/bin/env python3
"""College 2 (week 2, do 14 januari 2027): van verhaal naar bewijs. Gastcollege, minicollege, Lagerhuisdebat, K2/K3.

Gebruik:  python3 gen_c2.py <map met gelezen project/deck.json> <uitvoermap>
Publiceren naar https://claude.ai/artifact/WrRe73cGoTqCdhuhB25gNS met root = <uitvoermap>.
"""
import sys
from janssen_slides import *

LOGO = '/_blob/377980ba5902f25d57ce02de8a2ed554'
IMG_K2 = '/_blob/6bf7dd641a65ff2a8414420a7312a3b3'
IMG_K3 = '/_blob/2c6c764b9ab7b4cf1d9e6ec9dd702840'
URL_TED = 'https://www.ted.com/talks/joy_buolamwini_how_i_m_fighting_bias_in_algorithms'
PARTS = ['Terugblik', 'Gastcollege', 'Vraaggesprek', 'Minicollege', 'Debat', 'Jullie casus: K2 en K3']
D = Deck(LOGO, 'ICT A-ET · College 2 · donderdag 14 januari 2027', PARTS)
K, H, P, UL, C, R, G = D.kicker, D.h2, D.p, D.ul, D.card, D.row, D.grid

# ============ Cover ============
D.frame('cover', f'''
<div style="display:flex;justify-content:space-between;align-items:flex-start">
<img src="{LOGO}" alt="Janssen University of Applied Sciences" style="width:620px;height:72px;object-fit:contain;object-position:left">
<p style="font-size:26px;font-weight:700;color:{BLUE_T};letter-spacing:2px;text-transform:uppercase;text-align:right">Minor AI · ICT A-ET</p>
</div>
<div style="flex:1;display:flex;flex-direction:column;justify-content:center;gap:28px">
<p style="font-size:30px;font-weight:700;color:{BLUE_T};letter-spacing:3px;text-transform:uppercase">AI &amp; Ethics · College 2</p>
<h1 style="font-size:112px;font-weight:700;line-height:1.02;color:{NAVY};text-transform:uppercase">Waar gaat het mis, en wie is verantwoordelijk?</h1>
<div style="width:240px;height:10px;background:{BLUE};border-radius:5px"></div>
</div>
<div style="background:{NAVY};border-radius:14px;padding:28px 40px;display:flex;justify-content:space-between">
<p style="font-size:30px;color:{ON_NAVY}">Donderdag 14 januari 2027 · [tijd] · lokaal [__]</p>
<p style="font-size:30px;color:{GOLD};font-weight:700">Met gastspreker [naam], [organisatie]</p>
</div>''', '''[1 min · opening · 0:00] Zeg: "Vandaag eerst de praktijk, met onze gastspreker. Daarna de theorie die die praktijk verklaart: bias, privacy en verantwoording. Dan een debat, en tot slot jullie eigen casus." Overgang: "Wat verandert er vandaag aan jullie rol?"''', footer=False, pad='96px 128px')

# ============ Deel 1. Terugblik ============
reis = ''.join(
    f'<div style="flex:1;display:flex;flex-direction:column;gap:10px;align-items:center">'
    f'<div style="width:100%;height:14px;border-radius:7px;background:{GREEN if i == 0 else BLUE if i == 1 else LINE}"></div>'
    f'<p style="font-size:26px;font-weight:700;color:{GREEN if i == 0 else NAVY if i == 1 else MUTED}">{t}</p></div>'
    for i, t in enumerate(['K1 ✓', 'K2 · K3 · bewijsplan', 'K4 nulmeting', 'K5–K6', 'A1 · 4 feb']))
D.frame('vandaag', K('Rolwissel') + H('Vandaag word je onderzoeker') +
    P('Vorige week bakende je af wat je onderzoekt. Vandaag leer je waar het misgaat en wie verantwoordelijk is, en hoe je dat aantoont. **Een oordeel zonder bewijs telt niet.**', 32) +
    f'<div style="display:flex;gap:10px">{reis}</div>' +
    UL(['Aan het einde van vandaag kun je bij een echte casus de bron van bias, het privacyrisico en de verantwoordelijke aanwijzen;',
        'uitleggen waarom een mens in het proces nog geen controle is;',
        'een standpunt verdedigen én het tegenovergestelde.'], 29) +
    f'<div style="background:{ICE};border-left:8px solid {BLUE};border-radius:12px;padding:22px 32px">{P("**Eindresultaat vandaag:** per groep één bron van bias en één privacyrisico voor jullie oplossing, met de stakeholder die het raakt: de eerste rij van K2 en K3.", 29, NAVY)}</div>',
    '''[2 min · deel 1 · 0:01] Zeg: "Vorige week werd je beoordelaar. Vandaag word je onderzoeker: je zoekt het bewijs onder je oordeel." Wijs op de balk: K1 is af (feedforward kwam maandag), deze week K2, K3 en het bewijsplan. Lees het eindresultaat voor. Overgang: "Zo ziet de middag eruit."''', part=1)

D.frame('route', K('Lesroute') + H('Zes delen, elk met een opbrengst') + D.table(
    ['Deel', 'Centrale vraag', 'Opbrengst', 'Tijd'],
    [['1 · Terugblik', 'Welke fout is erger?', 'Je keuze uit practicum 1', '0:00–0:15'],
     ['2 · Gastcollege', 'Wat gebeurt er in de praktijk?', 'De aantekenkaart', '0:15–1:00'],
     ['3 · Vraaggesprek', 'Wat willen jullie weten?', 'Antwoorden op jullie vragen', '1:00–1:20'],
     ['Pauze', '', '', '1:20–1:30'],
     ['4 · Minicollege', 'Hoe onderzoek je bias, privacy en verantwoording?', 'Drie onderzoeksvragen', '1:30–2:00'],
     ['5 · Debat', 'Waar sta jij?', 'Je standpunt, getoetst', '2:00–2:38'],
     ['6 · Jullie casus', 'Waar gaat het bij jullie mis?', 'Eerste rij K2 en K3, exit ticket', '2:38–3:00']], 27, ['24%', '40%', '22%', '14%']),
    '''[2 min · deel 1 · 0:03] Zeg: "Na het debat ga je met je groep aan de slag; alles van vandaag gebruik je in K2 en K3." Overgang: "Eerst terug naar jullie eigen practicum."''', part=1)

D.frame('fout-erger', K('Kies eerst, verdedig daarna') + H('Welke fout is erger?') + D.table(
    ['Model, 360 testaanvragen (practicum 1)', 'Juist', 'Onterecht goedgekeurd', 'Onterecht afgewezen'],
    [['Logistische regressie', '69,4%', '80', '30'], ['Beslisboom', '67,8%', '65', '51']], 30, ['34%', '16%', '25%', '25%']) +
    R(C(None, '**[__] studenten** kozen logistische regressie', size=30, bg=ICE), C(None, '**[__] studenten** kozen de beslisboom', size=30, bg=ICE)) +
    P('Wie draagt de 51 onterechte afwijzingen? Wie kiest iets anders dan de buur?', 30, NAVY, 700),
    '''[5 min · deel 1 · 0:05] Vul vooraf in hoeveel studenten in practicum 1 (evidence card 1, individueel) voor welk model kozen. Werkvorm: 30 seconden zelf kiezen, dan handopsteken. Vraag twee studenten met een verschillende keuze waarom. Zeg: "Het model dat het vaakst gelijk heeft, maakt niet dezelfde fouten: de regressie keurt vaker onterecht goed (80 tegen 65), de boom wijst vaker onterecht af (51 tegen 30)." Vraag door: "Wie draagt de 51 onterechte afwijzingen?" Verwacht: aanvragers die konden terugbetalen, vaak uit het binnenland. De getallen komen uit practicum 1 met de Suribank-oefendata in Orange; in Python bijna gelijk. Overgang: "Het hangt af van de bril waarmee je kijkt."''', part=1)

bril = lambda lab, col, t, s: (f'<div style="flex:1;background:{CARD};border:1px solid {LINE};border-top:8px solid {col};border-radius:14px;padding:40px;display:flex;flex-direction:column;gap:18px">'
    f'<p style="font-size:26px;font-weight:700;color:{col};text-transform:uppercase;letter-spacing:2px">{lab}</p><h3 style="font-size:52px;font-weight:700;color:{NAVY}">{e(t)}</h3>{P(s, 30)}</div>')
D.frame('twee-brillen', H('Twee brillen, twee soorten fouten') + R(
    bril('De bril van de bank', BLUE_T, 'Onterecht goedgekeurd', 'De lening wordt niet terugbetaald. De bank verliest geld, en de klant zit in de schulden.'),
    bril('De bril van de aanvrager', RED, 'Onterecht afgewezen', 'Wie kon terugbetalen, krijgt geen krediet. Vaak volgt een informele geldschieter.'), gap=32) +
    D.statement('Een model optimaliseren betekent kiezen welke fout je accepteert. Die keuze is ethisch, niet technisch.', size=36),
    '''[3 min · deel 1 · 0:10] Zeg: "De bank let vooral op onterecht goedgekeurd: dat kost geld. De aanvrager let op onterecht afgewezen: dat kost een kans." Vraag: "Wie in deze zaal zou de bank adviseren de boom te nemen?" Verwacht: weinig handen. Zeg: "Wie bepaalt welke fout zwaarder weegt? En wie merkt het als die keuze niemand opvalt?" Overgang: "Jullie zagen zelf ook risico's in jullie casus."''', part=1)

D.frame('exit-tickets', K('Uit jullie exit tickets van college 1') + H('Wat jullie zagen in jullie eigen casus') + R(
    *[C(None, f'<p style="font-size:72px;font-weight:700;color:{BLUE_T};line-height:1">{i}</p>{P(f"[risico {i}]", 32, NAVY, 700)}{P("[__] keer genoemd", 26, MUTED)}') for i in (1, 2, 3)]) +
    P('Let in het gastcollege op: kwam de gastspreker deze risico’s ook tegen?', 30, NAVY, 700),
    '''[2 min · deel 1 · 0:13] Vul vooraf de drie risico's in die het vaakst in de exit tickets van college 1 stonden (MyCampus: ICT A-ET Exit ticket college 1). Zeg: "Let er vandaag op of de gastspreker deze risico's ook tegenkwam." Overgang: "Daarvoor gebruik je een aantekenkaart."''', part=1)

# ============ Deel 2. Gastcollege ============
D.frame('welkom', K('Gastcollege · 45 minuten', dark=True) +
    f'<div style="flex:1;display:flex;flex-direction:column;justify-content:center;gap:28px"><h1 style="font-size:104px;font-weight:700;line-height:1.05;color:{ON_NAVY}">Welkom, [naam gastspreker]</h1>'
    f'{P("[functie] · [organisatie]", 44, GOLD, 700)}{P("[Eén zin over het onderwerp van het gastcollege]", 34, ON_NAVY_MUTED)}</div>',
    '''[2 min · deel 2 · 0:15] Introduceer de gastspreker in twee minuten: wie, welke organisatie, waarom deze casus past bij bias, privacy of verantwoording. Het gastcollege duurt ongeveer 43 minuten; bewaak de tijd met een afgesproken teken. Laat daarna de aantekenkaart in beeld staan als de spreker geen eigen dia's heeft. Valt de gastspreker uit: gebruik de dia "gender-shades" en speel de hele TED-talk (ongeveer 9 minuten), met de aantekenkaart als kijkopdracht, en verleng het minicollege.''', dark=True, part=2)

D.frame('aantekenkaart', K('Aantekenkaart · individueel, tijdens het gastcollege') + H('Zes vragen bij het gastcollege') + G([
    C(None, f'<p style="font-size:28px;font-weight:700;color:{GOLD if i == 6 else BLUE_T}">{i}</p>{P(t, 32, ON_NAVY if i == 6 else NAVY, 700)}', dark=(i == 6))
    for i, t in enumerate(['Welk vraagstuk speelde?', 'Welke risico’s waren er?', 'Wat ging mis, of had mis kunnen gaan?',
                           'Wie was verantwoordelijk?', 'Welke maatregelen volgden?', 'Wat betekent dit voor onze eigen casus?'], 1)], 3, 24) +
    P('Vraag 6 gebruik je in deel 6 en in K2. De vragen staan ook in de studentversie van week 2.', 28, MUTED),
    '''[43 min · deel 2 · 0:17] Laat deze dia staan als de gastspreker geen eigen dia's gebruikt, of deel de kaart op papier uit. Studenten noteren individueel. Na het gastcollege 1 minuut stilte: "Vul vraag 6 nu in." Overgang: "Nu jullie vragen."''', part=2)

# ============ Deel 3. Vraaggesprek ============
D.frame('vragen', K('Vraaggesprek · 20 minuten') + H('Vragen van de groepen') + R(
    f'<div style="flex:1;display:flex;flex-direction:column;gap:12px">{P("**Volgorde** (uit de inzendingen van dinsdag)", 28, NAVY)}' +
    UL(['[Groep] · [kern van de vraag]'] * 6, 28, ordered=True) + '</div>',
    C('Spelregels', UL(['Elke groep stelt één vraag.', 'Daarna vervolgvragen, van iedereen.', 'Kort en concreet: één vraag per keer.', 'Noteer het antwoord bij vraag 4 of 5 van je kaart.'], 28), flex=1.2), gap=40),
    '''[20 min · deel 3 · 1:00] Gebruik de vragen die groepen vóór dinsdag 12 januari inleverden bij ICT A-ET Voorbereiding college 2; zet de volgorde en de kern in drie woorden vooraf op de dia. Valt het stil, stel dan zelf: "Wie had de bevoegdheid om het systeem stop te zetten, en is dat ooit gebeurd?" · "Hoe wist u of het systeem voor alle groepen even goed werkte?" · "Wat zou u een organisatie in Suriname aanraden die nu met AI begint?" Bedank de gastspreker. Vraag of die beschikbaar is als panellid bij college 3 op 25 februari. Overgang: pauze.''', part=3)

D.frame('pauze', f'<div style="flex:1;display:flex;flex-direction:column;justify-content:center;gap:28px"><h1 style="font-size:160px;font-weight:700;line-height:1;color:{ON_NAVY};text-transform:uppercase">Pauze</h1>{P("10 minuten · we gaan verder om [__:__]", 44, GOLD, 700)}</div>',
    '''[10 min · pauze · 1:20] Vul de tijd in. Na de pauze het minicollege: hoe onderzoek je bias, privacy en verantwoording in je eigen casus?''', dark=True)

# ============ Deel 4. Minicollege ============
D.frame('bias-onderzoeken', K('Minicollege 1/3 · Bias') + H('Bias onderzoeken: welke vraag, welk bewijs?') + D.table(
    ['Bron', 'Vraag aan de organisatie', 'Bewijs dat je zoekt'],
    [['Historisch', 'Welke beslissingen uit het verleden zitten in de data?', 'Beschrijving van de trainingsdata en de periode'],
     ['Representatie', 'Welke groepen komen weinig voor?', 'Aantallen per groep in de data'],
     ['Meting', 'Wordt een kenmerk voor elke groep even goed gemeten?', 'Ontbrekende waarden per groep'],
     ['Label', 'Waar komt het label vandaan, en wie ontbreekt?', 'Uitleg over hoe het label is bepaald'],
     ['Aggregatie', 'Wordt de prestatie per groep gemeten?', 'Testresultaten per groep'],
     ['Gebruik', 'Wordt het systeem gebruikt waarvoor het gemaakt is?', 'Werkinstructies en gesprekken met gebruikers']], 27, ['18%', '44%', '38%']),
    '''[6 min · deel 4 · 1:30] Zeg: "Ik herhaal de zes bronnen uit clip 6 niet. Ik laat per bron zien welke vraag je stelt en welk bewijs je zoekt. Deze tabel gebruik je in week 3 en 4." Verbind steeds met een voorbeeld uit het gastcollege. Suribank: historisch, alleen goedgekeurde leningen in de trainingsdata; meting, ontbrekend inkomen vooral bij informeel werk. Vraag: "Welke bron speelde bij de gastspreker?" Overgang: "Is bias dan ook discriminatie?"''', part=4)

D.frame('bias-discriminatie', H('Bias of discriminatie?') + R(
    C('Bias', 'Een technisch begrip: een model wijkt systematisch af voor een groep.', accent=BLUE),
    C('Discriminatie', 'Een juridisch en ethisch begrip: een ongerechtvaardigd onderscheid.', accent=RED)) +
    f'<div style="background:{NAVY};border-radius:14px;padding:32px 44px;display:flex;flex-direction:column;gap:12px">{P("**Grondwet van Suriname, artikel 8 lid 2**", 26, GOLD)}'
    f'{P("Verbiedt onderscheid op onder meer geboorte, geslacht, ras, taal, godsdienst en afkomst, maar ook op economische positie en sociale omstandigheden.", 30, ON_NAVY)}</div>' +
    D.statement('De vraag is niet óf er onderscheid is, maar of het gerechtvaardigd en proportioneel is.', size=36),
    '''[4 min · deel 4 · 1:36] Vraag eerst (kies eerst): "Is een kredietmodel dat rekening houdt met inkomen discriminerend? Ja of nee?" Verwacht: verdeeld. Zeg: "Niet zonder meer: terugbetaalcapaciteit is een legitiem doel, maar het onderscheid moet proportioneel zijn en niet verder gaan dan nodig. En district? Daar is de rechtvaardiging veel lastiger." Overgang: "Hoe zie je bias als het gemiddelde goed is?"''', part=4)

D.frame('gender-shades', K('Echte casus · kernbron van deze week') + H('Gender Shades: een goed gemiddelde verbergt grote verschillen') + R(
    f'<div style="flex:1.6;display:flex;flex-direction:column;gap:20px">' +
    R(C(None, f'<p style="font-size:96px;font-weight:700;line-height:1;color:{BLUE_T}">0,8%</p>{P("fout bij mannen met een lichte huidskleur", 28)}'),
      C(None, f'<p style="font-size:96px;font-weight:700;line-height:1;color:{RED}">34,7%</p>{P("fout bij vrouwen met een donkere huidskleur", 28)}', accent=RED)) +
    f'<div style="background:{ICE};border-radius:12px;padding:22px 30px;display:flex;flex-direction:column;gap:8px">{P("**Kijkvragen bij het fragment**", 28, NAVY)}' +
    UL(['Welke van de zes bronnen van bias zie je?', 'Waarom zag niemand het in het gemiddelde?', 'Wie had per groep moeten meten?'], 27, ordered=True) + '</div></div>',
    f'<div style="flex:1;display:flex;flex-direction:column;gap:14px;align-items:center;justify-content:center">{qr_svg(URL_TED, 280, label="QR-code naar de TED-talk van Joy Buolamwini")}'
    f'{P("TED · Joy Buolamwini, How I’m fighting bias in algorithms", 24, MUTED)}{P("Buolamwini & Gebru (2018), PMLR 81", 24, MUTED)}</div>'),
    '''[5 min · deel 4 · 1:40] Speel de eerste ongeveer 3 minuten van de TED-talk (het witte masker), of vertel het kort als er geen geluid is. Bron: TED, Joy Buolamwini, "How I'm fighting bias in algorithms" (TEDxBeaconStreet, ongeveer 9 minuten); Buolamwini & Gebru (2018), Gender Shades, PMLR 81, 77–91. Vraag de drie kijkvragen. Verwacht: representatiebias (lichte mannen veel vaker in de trainingsdata) en aggregatiebias (alleen het gemiddelde gemeten); de bouwer, maar ook de organisatie die het koopt en inzet. Zeg: "Daarom maak je in practicum 2 de verwarringsmatrix per groep." Reserve bij afzegging van de gastspreker: speel de hele talk met de aantekenkaart.''', part=4)

D.frame('privacy-onderzoeken', K('Minicollege 2/3 · Privacy') + H('De regels leer je in A-DG. Hier stel je drie vragen.') + R(
    C('Wat leidt het systeem af?', 'Draagkracht uit woonplaats, gezondheid uit aankopen. Niemand gaf het op, toch weegt het mee.', label='Vraag 1'),
    C('Waar gaan de gegevens heen?', 'Ook wat klanten en medewerkers in een chatbot typen. Naar wie, in welk land, en voor hoe lang?', label='Vraag 2', accent=GOLD),
    C('Kun je de klant recht aankijken?', 'Als de mensen om wie het gaat wisten wat er met hun gegevens gebeurt: zouden ze het goedvinden?', label='Vraag 3', accent=RED)) +
    P('**Kies eerst:** een medewerker plakt een klantbrief in een gratis chatbot om snel een antwoord te laten schrijven. Welke vraag gaat hier mis?', 30, NAVY),
    '''[5 min · deel 4 · 1:45] Zeg: "A-DG behandelt de regels: persoonsgegevens, gevoelige gegevens, doelbinding en dataminimalisatie. Hier gaat het om de vraag erachter." Vraag 1 is inferentie: AI leidt af wat niemand opgaf, en een combinatie zonder naam kan toch naar een persoon wijzen. Vraag 2 is nieuw bij generatieve AI. Bij het voorbeeld: eerst vingers omhoog, 1, 2 of 3. Verwacht: vraag 2 gaat mis (de gegevens van de klant gaan zonder dat die het weet naar buiten), en daardoor ook vraag 3. Suribank bij vraag 1: district werkt als schatting van draagkracht. Overgang: "En welke regels gelden in Suriname?"''', part=4)

D.frame('privacy-suriname', H('Privacy in Suriname') + R(
    C('De Grondwet', 'Artikel 17 beschermt de persoonlijke levenssfeer.', accent=GREEN),
    C('Nog geen privacywet', 'De ontwerpwet Bescherming Privacy en Persoonsgegevens ligt bij De Nationale Assemblée: onder meer een toezichthouder en regels voor doorgifte naar het buitenland.', accent=RED),
    C('Over de grens', 'Draait de AI bij een buitenlandse leverancier, of gebruikt de chatbot een buitenlands taalmodel? Welke afspraken zijn er over beveiliging, bewaren en hergebruik?')) +
    f'<div style="background:{NAVY};border-radius:14px;padding:30px 44px">{P("Welke regels zou jullie organisatie nu al moeten volgen, ook zonder wet?", 36, ON_NAVY, 700)}</div>',
    '''[3 min · deel 4 · 1:50] Zeg: "Wettelijk is niet hetzelfde als verantwoord. Waar de wet nog zwijgt, is veel toegestaan, maar de ethische vraag blijft." Controleer vlak voor het college of er nieuws is over de ontwerpwet (DNA). Dit is de opmaat voor stelling 1 van het debat: iedereen schreef er in de weekcheck al een standpunt over. Overgang: "Als het misgaat: wie is dan verantwoordelijk?"''', part=4)

schakel = lambda t: f'<div style="flex:1;background:{CARD};border:1px solid {LINE};border-radius:12px;padding:26px 14px;display:flex;align-items:center;justify-content:center"><h3 style="font-size:30px;font-weight:700;color:{NAVY};text-align:center">{e(t)}</h3></div>'
pijl = f'<p style="font-size:36px;font-weight:700;color:{BLUE};align-self:center">→</p>'
D.frame('verantwoordelijk', K('Minicollege 3/3 · Verantwoording') + H('Het model wijst iemand onterecht af. Wie is verantwoordelijk?') +
    f'<div style="display:flex;gap:12px;align-items:stretch">{pijl.join(schakel(t) for t in ["Ontwikkelaar", "Leverancier, ook van het taalmodel", "Organisatie", "Management", "Medewerker"])}</div>' +
    f'<div style="background:{NAVY};border-radius:14px;padding:30px 44px">{P("Nooit alleen “het model” of “de programmeur”. **Verantwoording** betekent: je kunt aanwijzen wie waarvoor verantwoordelijk is, en aantonen hoe de risico’s worden beheerst.", 32, ON_NAVY)}</div>' +
    P('Bij een chatbot zit de leverancier van het taalmodel in de keten. Toch blijft de organisatie verantwoordelijk voor wat haar chatbot zegt.', 28),
    '''[4 min · deel 4 · 1:53] Teken de keten op het bord. Vraag bij elke schakel: "Wat had deze partij kunnen doen?" Gebruik een voorbeeld uit het gastcollege: wie had daar de bevoegdheid om in te grijpen? Vooruitblik week 4: de chatbot van Air Canada beloofde een klant een korting die niet bestond; de rechter oordeelde dat de organisatie verantwoordelijk is voor wat haar chatbot zegt (Moffatt v. Air Canada, 2024 BCCRT 149). Vraag: "Wie is bij jullie oplossing eindverantwoordelijk voor de antwoorden van het systeem?" (In week 6 heet dat in de RACI-tabel de A.) Overgang: "En is een mens in het proces genoeg?"''', part=4)

D.frame('menselijke-controle', H('Een mens in het proces is nog geen controle') + G([
    C(t, q, size=27) for t, q in [('Informatie', 'Zie je waarom het systeem dit adviseert?'), ('Tijd', 'Heb je genoeg tijd om echt te kijken?'),
                                   ('Kennis', 'Weet je wanneer het systeem niet te vertrouwen is?'), ('Bevoegdheid', 'Mag je afwijken van het advies?'),
                                   ('Cultuur', 'Is afwijken normaal, of word je erop afgerekend?'), ('Registratie', 'Worden afwijkingen bijgehouden?')]], 3, 20) +
    P('**Kies eerst:** 15 minuten per dossier, en afwijken alleen met schriftelijk akkoord. Hoe vaak wijkt iemand dan af?', 30, NAVY),
    '''[3 min · deel 4 · 1:57] Zeg: "Automation bias: wie een mens in het proces zet, moet ook zorgen dat die mens echt kan ingrijpen." Vraag: "Welke van deze zes voorwaarden ontbraken in het verhaal van de gastspreker?" Leesopdracht voor deze week: de toeslagenaffaire (Amnesty International, Xenophobic Machines, 25 oktober 2021) staat in de studentversie; daar ontbraken meerdere voorwaarden. Bij generatieve AI is het risico groter: een chatbot schrijft vloeiend en zelfverzekerd, ook als het antwoord fout is. Standaard: AI-verordening art. 14 lid 4 onder b noemt automation bias letterlijk. Overgang naar deel 5: "Nu jullie standpunt."''', part=4)

# ============ Deel 5. Debat ============
stap = lambda m, t, s, gold=False: (f'<div style="flex:1;border-top:6px solid {GOLD if gold else ON_NAVY_MUTED};padding:22px 0 0;display:flex;flex-direction:column;gap:8px">'
    f'<p style="font-size:26px;font-weight:700;color:{GOLD}">{m}</p><h3 style="font-size:34px;font-weight:700;color:{GOLD if gold else ON_NAVY}">{t}</h3>{P(s, 26, ON_NAVY_MUTED)}</div>')
D.frame('debat-regels', K('Lagerhuisdebat · 2 stellingen × 18 minuten', dark=True) + H('Kies een kant, en wissel dan', dark=True) +
    f'<div style="display:flex;gap:18px">{stap("1 min", "Kiezen", "Vóór, tegen of het midden")}{stap("2 min", "Openen", "Per kant het sterkste argument")}{stap("7 min", "Debatteren", "Overtuigd? Loop naar de andere kant")}{stap("6 min", "Wisselen", "Verdedig nu het andere standpunt", True)}{stap("2 min", "Afsluiten", "Kies opnieuw; wie wisselde?")}</div>' +
    f'<div style="background:{ICE};border-radius:14px;padding:28px 40px;display:flex;flex-direction:column;gap:8px">{P("**Spelregels**", 26, NAVY)}' +
    UL(['Reageer op het argument, niet op de persoon.', 'Gebruik een feit met bron, een voorbeeld uit het gastcollege of een van de vier lenzen.', 'Herhaal geen argument dat al is gegeven.'], 28) + '</div>',
    '''[2 min · deel 5 · 2:00] De docent is voorzitter. Zet twee rijen stoelen tegenover elkaar; het middenvak is voor wie twijfelt. Bijdragen van hooguit een minuut, steeds reagerend op de vorige spreker. Zeg: "Wisselen is geen spel: wie de sterkste tegenargumenten kent, onderbouwt een eigen standpunt beter." Overgang: stelling 1.''', dark=True, part=5)

stelling = lambda sid, lab, t, notes: D.frame(sid, K(lab, dark=True) +
    f'<h1 style="font-size:80px;font-weight:700;line-height:1.15;color:{ON_NAVY}">{e(t)}</h1>' +
    R(*[f'<div style="flex:1;background:{bg};border-radius:14px;padding:24px 30px"><p style="font-size:30px;font-weight:700;color:{fc};text-align:center">{x}</p></div>'
        for x, bg, fc in [('Vóór: deze kant', GREEN, '#FFFFFF'), ('Twijfel: het midden', GOLD, NAVY), ('Tegen: die kant', RED, '#FFFFFF')]]) +
    P('Telling begin [__] / [__] / [__] · eind [__] / [__] / [__]', 26, ON_NAVY_MUTED), notes, dark=True, part=5)
stelling('stelling-1', 'Stelling 1 · uit de weekcheck', 'Organisaties in Suriname moeten wachten met AI voor beslissingen over mensen totdat er een privacywet is.',
    '''[18 min · deel 5 · 2:02] Iedereen schreef hierover al een standpunt in de weekcheck. Vraag vooraf twee studenten met een verschillend standpunt het voor te lezen (elk hooguit een minuut). Tel bij begin en eind. Verwacht vóór: zonder wet geen toezichthouder en geen bezwaarrecht, dus de burger staat zwak. Verwacht tegen: wachten kan jaren duren, de Grondwet (art. 17) beschermt de persoonlijke levenssfeer al, en een organisatie kan zelf strengere regels volgen. Vraag door met het verschil tussen wettelijk en verantwoord. Afsluiten: wie wisselde, en waardoor?''')
stelling('stelling-2', 'Stelling 2 · ingezonden door groep [__]', 'Een AI-systeem dat gemiddeld beter presteert dan mensen mag worden ingezet, ook als het niet voor iedere groep even goed werkt.',
    '''[18 min · deel 5 · 2:20] Vervang deze reservestelling door de beste stelling uit de inzendingen: één zin, echt betwistbaar, een botsing tussen twee waarden, twee bronnen. Laat de groep die hem instuurde openen met haar sterkste bron. Andere reservestellingen: "Als een bank geslacht en district uit het model haalt, kan het model niet meer discrimineren." · "Een klant die door een algoritme is afgewezen, heeft altijd recht op een herbeoordeling door een mens." · "Een chatbot van de overheid hoeft niet te melden dat hij AI is, zolang de antwoorden kloppen." · "Wie de data levert, is verantwoordelijk voor de bias in het model." Bij deze reservestelling: verbind met Gender Shades. Afsluiten: vraag welke lenzen gebruikt zijn en welke niet. Kondig aan: vanaf week 3 opent elke online sessie met een stelling; vraag wie op 21 januari wil verdedigen of bestrijden.''')

# ============ Deel 6. Jullie casus ============
D.frame('k2k3-voorbeeld', K('Zo werk je K2 en K3 uit') + H('Suribank: macht, kwetsbaarheid en de keten') + R(
    f'<div style="flex:1;display:flex;flex-direction:column;gap:12px"><img src="{IMG_K2}" alt="K2-voorbeeld Suribank: stakeholders op macht en kwetsbaarheid" style="width:810px;height:430px;object-fit:contain;background:#FFFFFF;border:1px solid {LINE};border-radius:12px">{P("K2 · het kwadrant met veel kwetsbaarheid en veel macht is leeg", 26, NAVY, 700)}</div>',
    f'<div style="flex:1;display:flex;flex-direction:column;gap:12px"><img src="{IMG_K3}" alt="K3-voorbeeld Suribank: procesplaat met risicopunten" style="width:810px;height:430px;object-fit:contain;background:#FFFFFF;border:1px solid {LINE};border-radius:12px">{P("K3 · de risico’s zitten in stap 1, 5, 6 en 7, niet alleen in het model", 26, NAVY, 700)}</div>', gap=36),
    '''[3 min · deel 6 · 2:38] Zeg: "Teken de keten niet opnieuw: neem het schema uit A-AI2 en het datastroomschema uit A-DG, en leg de ethische laag erover." Wijs in K2 op de groep aanvragers uit het binnenland: weinig macht, veel te verliezen, niet gehoord. Wijs in K3 op stap 5 tot 7: automation bias, geen uitleg, geen bezwaarroute. Overgang: "Hoe goed moet een rij zijn?"''', part=6)

niv = lambda lab, col, t, fc='#FFFFFF': (f'<div style="display:flex;border:1px solid {LINE};border-radius:14px;overflow:hidden">'
    f'<p style="width:250px;flex:none;background:{col};color:{fc};font-size:30px;font-weight:700;padding:24px 28px">{lab}</p>'
    f'<p style="flex:1;background:{CARD};font-size:28px;line-height:1.35;color:{INK};padding:24px 30px">{e(t)}</p></div>')
D.frame('niveaus-k2', H('Eén stakeholderrij op drie niveaus') + niv('Zwak', RED, 'Klanten · kunnen benadeeld worden.') +
    niv('Redelijk', GOLD, 'Klanten met informeel werk · vaker afgewezen · macht laag.', NAVY) +
    niv('Professioneel', GREEN, 'Aanvragers uit het binnenland met informeel werk · doel: toegang tot krediet · schade: vaker onterecht afgewezen, uitwijken naar informele geldschieters · macht zeer laag, kwetsbaarheid hoog · niet gehoord; gesprek gepland in Albina.') +
    P('Welke kolom maakt het verschil tussen redelijk en professioneel?', 30, NAVY, 700),
    '''[3 min · deel 6 · 2:41] Vraag: "Welke kolom maakt het verschil tussen redelijk en professioneel?" Verwacht: de onderbouwing van macht en kwetsbaarheid, de concrete schade, en "hoe gehoord". Zeg: "Splits groepen die verschillend geraakt worden; 'klanten' is geen stakeholder." Het werkboek markeert zelf wie weinig macht en veel te verliezen heeft (kolom Signaal). Overgang: aan de slag.''', part=6)

D.frame('eigen-casus', D.werkblok('8 min', 'Groep') + H('Waar gaat het bij jullie mis?') +
    UL(['Kies voor jullie oplossing één bron van bias: welke van de zes, en waar in de keten?', 'Kies één privacyrisico: welke gegevens, naar welke externe dienst?', 'Wie raakt het? Zet die stakeholder in K2 met macht en kwetsbaarheid.'], 30, ordered=True) +
    D.klaar('één bron van bias met naam uit de zes; één privacyrisico met de externe dienst erbij; de stakeholder met macht en kwetsbaarheid, in de werkboektabs K2_Stakeholders en K3_Proces_Data.', 28) +
    P('**Nu verwerken, niet thuis:** één laptop per groep, direct in het werkboek.', 28),
    '''[8 min · deel 6 · 2:44] Loop rond. Docentvraag: "Wie merkt dit, zonder het systeem zelf te gebruiken?" en "Waar staat de server van die dienst?" Help groepen die vastlopen met vraag 6 van de aantekenkaart. Herinner: gesprekken met de partner vóór zondag inplannen voor week 3. Overgang: "Ruil met de buurgroep."''', part=6)

D.frame('ruil-risico', D.werkblok('4 min', 'Twee groepen') + H('Ruil je twee rijen') +
    UL(['Is de bron van bias een van de zes, en klopt de naam?', 'Staat er bij het privacyrisico waar de gegevens heen gaan?', 'Wie mist er als stakeholder?'], 32, ordered=True) +
    f'<div style="background:{ICE};border-left:8px solid {GOLD};border-radius:12px;padding:22px 32px">{P("**Na afloop verbeter je minimaal één regel.**", 30, NAVY)}</div>',
    '''[4 min · deel 6 · 2:52] Koppel groepen per twee: 2 minuten lezen en één opmerking per vraag, 2 minuten verbeteren. Vraag één groep: "Welke regel verbeterden jullie?" Overgang: exit ticket.''', part=6)

D.frame('exit', K('Exit ticket · 4 minuten · ICT A-ET Exit ticket college 2', dark=True) +
    UL(['Na vandaag zie ik in onze oplossing vooral het risico …, omdat …', 'Welke van de zes voorwaarden voor menselijke controle ontbreekt bij ons?', 'Welk standpunt veranderde vandaag, en waardoor?',
        'Bonus: welke vraag had jij nog aan de gastspreker?'], 33, ON_NAVY, ordered=True) +
    f'<div style="background:#0B2A6B;border-radius:14px;padding:24px 32px">{P("**Zondag 17 januari, 23:59:** K2, K3 en het bewijsplan bij ICT A-ET Rapportstuk week 2. Plan de gesprekken met de partner voor week 3.", 28, ON_NAVY)}</div>' +
    D.statement('Een mens in het proces is nog geen controle, en een goed gemiddelde is nog geen eerlijk systeem.', dark=True, size=36),
    '''[4 min · deel 6 · 2:56] Individueel, via de MyCampus-opdracht ICT A-ET Exit ticket college 2. Sluit af met de kernboodschap. Na het college: gebruik de antwoorden in het feedforward-bericht van maandag 18 januari, en noteer de tellingen van het debat.''', dark=True, part=6)

D.frame('bronnen', H('Bronnen') + UL([
    'Buolamwini, J. & Gebru, T. (2018). Gender Shades. Proceedings of Machine Learning Research 81, 77–91.',
    'Buolamwini, J. (2016). How I’m fighting bias in algorithms. TEDxBeaconStreet. ted.com',
    'Amnesty International (25 oktober 2021). Xenophobic Machines. amnesty.org, EUR 35/4686/2021.',
    'Grondwet van de Republiek Suriname, artikel 8 en 17.',
    'Ontwerpwet Bescherming Privacy en Persoonsgegevens (De Nationale Assemblée, dna.sr).',
    'NIST (2022). SP 1270, Towards a Standard for Identifying and Managing Bias in AI.',
    'Verordening (EU) 2024/1689 (AI-verordening), art. 10, 14 lid 4 onder b, 27.',
    'NIST AI RMF 1.0 (2023), GOVERN 2.1, MAP 4.1; ISO/IEC 42001:2023, 6.1.4; ISO/IEC 42005:2025.',
    'Moffatt v. Air Canada, 2024 BCCRT 149 (vooruitblik week 4).',
    'Mendelow, A. (1991). Stakeholder mapping (macht-belangschema), basis voor de 2x2 in K2.'], 25),
    '''[niet tonen tenzij gevraagd] Bronnen bij de dia's. Controleer de TED-link en het nieuws over de ontwerpwet vlak voor het college.''')

D.frame('docent-voorbereiding', K('Docent · niet tonen') + H('Voorbereiding college 2') + G([
    UL(['Aantallen practicum 1 per model op “fout-erger”', 'Top 3 uit de exit tickets van college 1 op “exit-tickets”', 'Naam, functie, organisatie gastspreker (cover, welkom)',
        'Volgorde groepen en kern van hun vraag op “vragen”', 'Stelling 2 kiezen uit de inzendingen'], 26),
    UL(['Twee studenten voor stelling 1 vooraf vragen', 'Stoelen in twee rijen met een middenvak; aantekenkaarten printen', 'TED-fragment testen (geluid); reserveplan bij afzegging',
        'Nieuws ontwerpwet privacy checken; tijd, lokaal, pauze invullen', 'Inleverpunten Exit ticket college 2 en Rapportstuk week 2 open'], 26)], 2, 40),
    '''Deze dia staat achteraan en wordt niet getoond of gedeeld. Na het college: exit tickets lezen, debattellingen noteren, feedforward maandag 18 januari, rapportstuk week 2 nakijken met de checklists en de kwaliteitslat.''')

if __name__ == '__main__':
    src, out = sys.argv[1], sys.argv[2]
    sections = {
        's1': {'description': 'Deel 1. Rolwissel, lesroute en terugblik: welke fout is erger?', 'start': 'cover'},
        's2': {'description': 'Deel 2. Gastcollege met aantekenkaart', 'start': 'welkom'},
        's3': {'description': 'Deel 3. Vraaggesprek en pauze', 'start': 'vragen'},
        's4': {'description': 'Deel 4. Minicollege: bias, privacy en verantwoording onderzoeken', 'start': 'bias-onderzoeken'},
        's5': {'description': 'Deel 5. Lagerhuisdebat over twee stellingen', 'start': 'debat-regels'},
        's6': {'description': 'Deel 6. Jullie casus: K2 en K3, ruil, exit ticket, bronnen', 'start': 'k2k3-voorbeeld'},
    }
    idx = D.write(out, src + '/project/deck.json', 'College 2 AI & Ethics: Waar gaat het mis, en wie is verantwoordelijk?', sections, {})
    print(len(idx['order']), "dia's")
