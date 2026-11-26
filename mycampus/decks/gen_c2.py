#!/usr/bin/env python3
"""College 2 (blok 1, do 14 januari 2027): gastcollege, veiligheid en alignment, werk en economie, Lagerhuisdebat, K2/K3.

Gebruik:  python3 gen_c2.py <map met gelezen project/deck.json> <uitvoermap>
Publiceren naar https://claude.ai/artifact/WrRe73cGoTqCdhuhB25gNS met root = <uitvoermap>.
"""
import sys
from janssen_slides import *

LOGO = '/_blob/377980ba5902f25d57ce02de8a2ed554'
IMG_K2 = '/_blob/6bf7dd641a65ff2a8414420a7312a3b3'
IMG_K3 = '/_blob/2c6c764b9ab7b4cf1d9e6ec9dd702840'
URL_TED = 'https://www.ted.com/talks/joy_buolamwini_how_i_m_fighting_bias_in_algorithms'
PARTS = ['Terugblik', 'Gastcollege', 'Vraaggesprek', 'Veiligheid', 'Werk en economie', 'Debat', 'Jullie casus']
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
</div>''', '''[1 min · opening · 0:00] Zeg: "Vandaag eerst de praktijk, met onze gastspreker. Daarna twee grote vragen: wat als een systeem zich anders gedraagt dan bedoeld, en wat doet AI met werk en met wie er wint? Dan een debat, en tot slot jullie eigen casus." Overgang: "Wat verandert er vandaag aan jullie rol?"''', footer=False, pad='96px 128px')

# ============ Deel 1. Terugblik ============
reis = ''.join(
    f'<div style="flex:1;display:flex;flex-direction:column;gap:10px;align-items:center">'
    f'<div style="width:100%;height:14px;border-radius:7px;background:{GREEN if i == 0 else BLUE if i == 1 else LINE}"></div>'
    f'<p style="font-size:26px;font-weight:700;color:{GREEN if i == 0 else NAVY if i == 1 else MUTED}">{t}</p></div>'
    for i, t in enumerate(['K1 ✓', 'K2 · K3 · bewijsplan', 'K4 scan en nulmeting', 'Concept · zo 24 jan', 'A1 · do 4 feb']))
D.frame('vandaag', K('Rolwissel') + H('Vandaag word je onderzoeker') +
    P('Vorige week bakende je af wat je onderzoekt. Vandaag leer je waar het misgaat en wie verantwoordelijk is, en hoe je dat aantoont. **Een oordeel zonder bewijs telt niet.**', 32) +
    f'<div style="display:flex;gap:10px">{reis}</div>' +
    UL(['Aan het einde van vandaag kun je uitleggen hoe een systeem zijn doel haalt maar de bedoeling mist (alignment, specification gaming);',
        'bij een echte casus aanwijzen of het om misbruik, een ongeluk of een structureel risico gaat;',
        'uitleggen wanneer AI werk aanvult en wanneer het werk overneemt, en wie daarbij wint of verliest;',
        'een standpunt verdedigen én het tegenovergestelde.'], 29) +
    f'<div style="background:{ICE};border-left:8px solid {BLUE};border-radius:12px;padding:22px 32px">{P("**Eindresultaat vandaag:** per groep het getal dat jullie oplossing stuurt, met een mogelijke bijwerking, en één risico voor werk of privacy, met de stakeholder die het raakt: de eerste rij van K2 en K3.", 29, NAVY)}</div>',
    '''[2 min · deel 1 · 0:01] Zeg: "Vorige week werd je beoordelaar. Vandaag word je onderzoeker: je zoekt het bewijs onder je oordeel." Wijs op de balk: K1 is af (feedforward kwam maandag). Tot zondag 24 januari werken jullie K2, K3 en K4 uit, met het bewijsplan; dat concept is optioneel, maar wie het instuurt, krijgt op 25 januari feedforward. Lees het eindresultaat voor. Overgang: "Zo ziet de middag eruit."''', part=1)

D.frame('route', K('Lesroute') + H('Zeven delen, elk met een opbrengst') + D.table(
    ['Deel', 'Centrale vraag', 'Opbrengst', 'Tijd'],
    [['1 · Terugblik', 'Welke fout is erger?', 'Je keuze uit practicum 1', '0:00–0:15'],
     ['2 · Gastcollege', 'Wat gebeurt er in de praktijk?', 'De aantekenkaart', '0:15–0:58'],
     ['3 · Vraaggesprek', 'Wat willen jullie weten?', 'Antwoorden op jullie vragen', '0:58–1:10'],
     ['Pauze', '', '', '1:10–1:20'],
     ['4 · Veiligheid', 'Doet het systeem wat we bedoelen?', 'Het getal dat jullie oplossing stuurt', '1:20–1:53'],
     ['5 · Werk en economie', 'Vult AI werk aan of neemt het over? Wie wint?', 'Je antwoord voor het debat', '1:53–2:20'],
     ['6 · Debat', 'Waar sta jij?', 'Je standpunt, getoetst', '2:20–2:42'],
     ['7 · Jullie casus', 'Waar gaat het bij jullie mis?', 'Eerste rij K2 en K3, plan tot 24 januari', '2:42–3:00']], 26, ['24%', '40%', '22%', '14%']),
    '''[2 min · deel 1 · 0:03] Zeg: "Vandaag twee nieuwe onderwerpen: veiligheid en alignment, en AI en werk. Na het debat ga je met je groep aan de slag; alles van vandaag gebruik je in K2, K3 en K4." Overgang: "Eerst terug naar jullie eigen practicum."''', part=1)

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
    '''[2 min · deel 2 · 0:15] Introduceer de gastspreker in twee minuten: wie, welke organisatie, waarom deze casus past bij bias, privacy of verantwoording. Het gastcollege duurt ongeveer 41 minuten; bewaak de tijd met een afgesproken teken. Laat daarna de aantekenkaart in beeld staan als de spreker geen eigen dia's heeft. Valt de gastspreker uit: speel de hele TED-talk van Joy Buolamwini (ongeveer 9 minuten, ook gebruikt in college 1) of de ACLU-video van Robert Williams, met de aantekenkaart als kijkopdracht, en verleng het minicollege.''', dark=True, part=2)

D.frame('aantekenkaart', K('Aantekenkaart · individueel, tijdens het gastcollege') + H('Zes vragen bij het gastcollege') + G([
    C(None, f'<p style="font-size:28px;font-weight:700;color:{GOLD if i == 6 else BLUE_T}">{i}</p>{P(t, 32, ON_NAVY if i == 6 else NAVY, 700)}', dark=(i == 6))
    for i, t in enumerate(['Welk vraagstuk speelde?', 'Welke risico’s waren er?', 'Wat ging mis, of had mis kunnen gaan?',
                           'Wie was verantwoordelijk?', 'Welke maatregelen volgden?', 'Wat betekent dit voor onze eigen casus?'], 1)], 3, 24) +
    P('Vraag 6 gebruik je in deel 7 en in K2. De vragen staan ook in kennispakket 1.', 28, MUTED),
    '''[41 min · deel 2 · 0:17] Laat deze dia staan als de gastspreker geen eigen dia's gebruikt, of deel de kaart op papier uit. Studenten noteren individueel. Na het gastcollege 1 minuut stilte: "Vul vraag 6 nu in." Overgang: "Nu jullie vragen."''', part=2)

# ============ Deel 3. Vraaggesprek ============
D.frame('vragen', K('Vraaggesprek · 12 minuten') + H('Vragen van de groepen') + R(
    f'<div style="flex:1;display:flex;flex-direction:column;gap:12px">{P("**Volgorde** (uit de inzendingen van dinsdag)", 28, NAVY)}' +
    UL(['[Groep] · [kern van de vraag]'] * 6, 28, ordered=True) + '</div>',
    C('Spelregels', UL(['Elke groep stelt één vraag.', 'Daarna vervolgvragen, van iedereen.', 'Kort en concreet: één vraag per keer.', 'Noteer het antwoord bij vraag 4 of 5 van je kaart.'], 28), flex=1.2), gap=40),
    '''[12 min · deel 3 · 0:58] Gebruik de vragen die groepen vóór dinsdag 12 januari inleverden bij ICT A-ET Voorbereiding college 2; zet de volgorde en de kern in drie woorden vooraf op de dia. Valt het stil, stel dan zelf: "Wie had de bevoegdheid om het systeem stop te zetten, en is dat ooit gebeurd?" · "Hoe wist u of het systeem voor alle groepen even goed werkte?" · "Wat zou u een organisatie in Suriname aanraden die nu met AI begint?" Bedank de gastspreker. Vraag of die beschikbaar is als panellid bij college 3 op 25 februari. Overgang: pauze.''', part=3)

D.frame('pauze', f'<div style="flex:1;display:flex;flex-direction:column;justify-content:center;gap:28px"><h1 style="font-size:160px;font-weight:700;line-height:1;color:{ON_NAVY};text-transform:uppercase">Pauze</h1>{P("10 minuten · we gaan verder om [__:__]", 44, GOLD, 700)}</div>',
    '''[10 min · pauze · 1:10] Vul de tijd in. Na de pauze twee minicolleges: veiligheid en alignment, en werk en economie.''', dark=True)

# ============ Deel 4. Veiligheid en alignment ============
URL_DEEPFAKE = 'https://www.srherald.com/suriname/2026/02/19/kabinet-waarschuwt-voor-deepfakevideos-president-simons/'
URL_COAST = 'https://openai.com/index/faulty-reward-functions/'
URL_WSJ = 'https://www.wsj.com/articles/facebook-algorithm-change-zuckerberg-11631654215'
URL_SYCO = 'https://openai.com/index/sycophancy-in-gpt-4o/'
URL_AVIANCA = 'https://abajournal.com/web/article/lawyers-who-doubled-down-and-defended-chatgpts-fake-cases-must-pay-5k-judge-says'
URL_ILOWB = 'https://www.ilo.org/publications/buffer-or-bottleneck-employment-exposure-generative-ai-and-digital-divide'
URL_CALLC = 'https://www.dbsuriname.com/2026/10/19/callcenters-onder-druk-kunstmatige-intelligentie-bedreigt-banen-in-suriname/'
URL_FINA = 'https://www.srherald.com/suriname/2026/11/12/finabank-gaat-kunstmatige-intelligentie-inzetten-voor-snellere-dienstverlening-en-betere-besluitvorming/'
URL_RAM = 'https://www.unesco.org/en/articles/suriname-advances-responsible-ai-governance-unescos-ram-20'
URL_IMF = 'https://www.imf.org/en/Blogs/Articles/2024/01/14/ai-will-transform-the-global-economy-lets-make-sure-it-benefits-humanity'
URL_TIME = 'https://time.com/6247678/openai-chatgpt-kenya-workers/'

tijdpunt = lambda jaar, t, col: (f'<div style="flex:1;display:flex;flex-direction:column;align-items:center;gap:8px;min-width:0">'
    f'<div style="width:26px;height:26px;border-radius:50%;background:{col};border:5px solid {BG}"></div>'
    f'<p style="font-size:26px;font-weight:700;color:{NAVY}">{e(jaar)}</p><p style="font-size:23px;line-height:1.2;color:{INK};text-align:center">{e(t)}</p></div>')
spoor = lambda titel, sub, punten, col: (f'<div style="display:flex;gap:24px;align-items:flex-start">'
    f'<div style="flex:0 0 250px;padding-top:6px"><p style="font-size:28px;font-weight:700;color:{NAVY}">{e(titel)}</p><p style="font-size:22px;color:{MUTED}">{e(sub)}</p></div>'
    f'<div style="flex:1;position:relative;display:flex;gap:6px"><div style="position:absolute;left:0;right:0;top:11px;height:5px;background:{col};border-radius:3px"></div>'
    + ''.join(tijdpunt(j, t, col) for j, t in punten) + '</div></div>')
qrkaart = lambda url, label, bron, size=230: (f'<div style="flex:0 0 360px;display:flex;flex-direction:column;gap:12px;align-items:center;justify-content:center">'
    f'{qr_svg(url, size, label=label)}{P(bron, 22, MUTED)}</div>')

D.frame('veilig-wat', K('Waar hebben we het over?') + H('Zes begrippen bij veiligheid en alignment') + D.table(
    ['Begrip', 'Wat het is'],
    [['AI-veiligheid', 'Systemen bouwen die betrouwbaar veilig en nuttig werken, ook in nieuwe situaties en onder druk om hun doel te halen.'],
     ['Robuustheid', 'Het systeem blijft goed werken als de invoer verandert, ongewoon is of bewust wordt gemanipuleerd.'],
     ['Alignment', 'Het doel en het gedrag van het systeem sluiten aan bij wat mensen werkelijk bedoelen en belangrijk vinden.'],
     ['Proxy', 'Een meetbaar getal in plaats van wat je eigenlijk wilt: klikken in plaats van tevredenheid, verwijderde berichten in plaats van veiligheid.'],
     ['Specification gaming', 'Het systeem haalt het doel zoals het is opgeschreven, via een maas in de regels, niet zoals het bedoeld is.'],
     ['Reward hacking', 'Het systeem haalt een hoge score op zijn beloning, terwijl de uitkomst schaadt wat mensen willen.']], 26, ['24%', '76%']) +
    D.statement('Veiligheid gaat niet alleen over aanvallen van buiten. Ook een systeem dat precies doet wat je vroeg, kan schade doen.', size=32),
    '''[3 min · deel 4 · 1:20] Zeg: "Na het gastcollege twee grote vragen. Eerst: wat als een systeem zich anders gedraagt dan bedoeld? Daarna: wat doet AI met werk en met wie er wint?" Lees de zes begrippen. Leg het verschil uit: robuustheid gaat over de invoer (verandert de wereld, of probeert iemand het systeem te misleiden?); alignment gaat over het doel (meet je wel wat je wilt?). Specification gaming en reward hacking liggen dicht bij elkaar: bij het eerste zoekt het systeem een maas in de opdracht, bij het tweede een maas in de beloning. Vraag: "Welk getal stuurt jullie oplossing?" Laat de vraag hangen; we komen er aan het einde van dit deel op terug. Overgang: "Waar komen deze begrippen vandaan?"''', part=4)

D.frame('veilig-herkomst', K('Praatplaat · waar komt het vandaan?') + H('Van “het doel in de machine” tot een internationaal veiligheidsrapport') +
    spoor('Veiligheid en alignment', 'denkers en mijlpalen', [
        ('1960', 'Wiener: weet zeker dat het doel in de machine het doel is dat je wilt'), ('1975', 'Goodhart: een maat die doel wordt, werkt niet meer'),
        ('2003', 'Bostrom: het paperclip-gedachte-experiment'), ('2016', 'Concrete Problems in AI Safety; CoastRunners'),
        ('2017', 'Leren van menselijke voorkeuren (RLHF)'), ('2019', 'Ongeluk, misbruik en structuur'), ('2025–2026', 'International AI Safety Report')], BLUE) +
    spoor('Dichtbij', 'in Suriname', [
        ('2022', 'ChatGPT: RLHF op grote schaal, ook hier in gebruik'), ('2025', 'Deepfake van NDP-leiders'), ('2026', 'Deepfake van de president'),
        ('2026', 'UNESCO AI Readiness Assessment')], GOLD) +
    D.statement('De vraag van Wiener is de kern gebleven: weet je zeker dat het doel in de machine het doel is dat je echt wilt?', size=32),
    '''[3 min · deel 4 · 1:23] Zeg: "Het idee is ouder dan ChatGPT." Toelichting: Norbert Wiener, Some Moral and Technical Consequences of Automation, Science 131 (1960): "we had better be quite sure that the purpose put into the machine is the purpose which we really desire." Charles Goodhart (1975) schreef over economische doelen die hun waarde verliezen zodra je erop stuurt; de bekende zin "When a measure becomes a target, it ceases to be a good measure" is van antropoloog Marilyn Strathern (1997). Nick Bostrom, Ethical Issues in Advanced Artificial Intelligence (2003): de paperclipmaximalisator. Amodei e.a., Concrete Problems in AI Safety (juni 2016) en OpenAI, Faulty Reward Functions in the Wild (december 2016). Christiano e.a. (2017): leren van menselijke voorkeuren, de basis van RLHF; Ouyang e.a. (2022, InstructGPT) en ChatGPT (november 2022) maakten het groot. Zwetsloot en Dafoe, Lawfare (februari 2019): risico's door ongelukken, misbruik en structuur. International AI Safety Report (29 januari 2025, voorzitter Yoshua Bengio, 96 experts uit 30 landen): kwaadwillig gebruik, storingen en systemische risico's; tweede editie 3 februari 2026, met dezelfde drie categorieën. Suriname: Suriname Herald 26 maart 2025 en 19 februari 2026 (deepfakes); de UNESCO AI Readiness Assessment (RAM 2.0), gestart op 27 augustus 2026 (unesco.org). Overgang: "Die drie soorten risico eerst."''', part=4)

risico = lambda nr, t, wat, vb, col, extra='': (f'<div style="flex:1;background:{CARD};border:1px solid {LINE};border-top:8px solid {col};border-radius:14px;padding:26px 28px;display:flex;flex-direction:column;gap:12px">'
    f'<p style="font-size:24px;font-weight:700;color:{BLUE_T};text-transform:uppercase;letter-spacing:1px">Risico {nr}</p><h3 style="font-size:34px;font-weight:700;color:{NAVY}">{e(t)}</h3>{P(wat, 24)}'
    f'<div style="background:{ICE};border-radius:10px;padding:12px 16px">{P(vb, 23)}</div>{extra}</div>')
D.frame('drie-risicos', K('Praatplaat · drie soorten risico') + H('Misbruik, ongeluk of structuur?') + R(
    risico(1, 'Misbruik', 'Iemand zet AI bewust in om schade te doen. Dezelfde techniek die ondertitels en voorleesstemmen maakt, maakt ook nepvideo’s.',
           '**Suriname, 2025 en 2026:** nepvideo’s en een nep-geluidsfragment van politici, en een deepfake van president Simons met een AI-stem. **Jamaica:** nepvideo’s die beleggers lokken.', RED,
           f'<div style="display:flex;gap:14px;align-items:center">{qr_svg(URL_DEEPFAKE, 100, label="QR-code naar het artikel van Suriname Herald over deepfakes")}{P("Suriname Herald, 19 februari 2026", 21, MUTED)}</div>'),
    risico(2, 'Ongeluk', 'Het systeem doet onbedoeld schade terwijl het zijn doel nastreeft. Niemand wilde het, het gebeurt toch.',
           '**Een tijdlijn die “betrokkenheid” maximaliseert,** laat vooral boze en schokkende berichten zien, want daar wordt het meest op gereageerd.', GOLD),
    risico(3, 'Structuur', 'De inzet zelf verandert de samenleving. Er is geen enkel foutpunt; het zit in het geheel.',
           '**Kredietmodellen bij alle banken** die het binnenland net iets vaker afwijzen: samen vergroten ze de achterstand.', BLUE), gap=22) +
    P('**Kies eerst:** bij welk risico is het moeilijkst aan te wijzen wie verantwoordelijk is?', 26, NAVY),
    '''[4 min · deel 4 · 1:26] Bron van de indeling: Remco Zwetsloot en Allan Dafoe, Thinking About Risks From AI: Accidents, Misuse and Structure (Lawfare, 11 februari 2019); het International AI Safety Report (januari 2025) gebruikt een vergelijkbare indeling: kwaadwillig gebruik, storingen en systemische risico's. Surinaamse casus: Suriname Herald 26 maart 2025 (nepvideo van NDP-voorzitter Jennifer Simons en ondervoorzitter Ramon Abrahams), 10 april 2025 (Ingrid Bouterse doet aangifte wegens een gemanipuleerde AI-video), 8 mei 2025 (geluidsfragment toegeschreven aan Simons blijkt nep) en 19 februari 2026 (Kabinet van de President waarschuwt voor video's met een deepfake van president Simons en een AI-stem; maken en verspreiden is volgens KPS en CDS strafbaar). Caribisch gebied: Jamaica Observer, 26 juli 2025 (politie waarschuwt voor een nep-AI-video die beleggers lokt). Bij 2 een algemeen voorbeeld; de echte casus van Facebook komt zo. Bij 3 is het voorbeeld een denkvoorbeeld: geen bewering over Surinaamse banken. Kies-eerst: vingers 1, 2 of 3. Verwacht: 3, want er is geen dader en geen enkel foutpunt. Zeg: "Bij misbruik is er een dader, bij een ongeluk een maker en een inzetter, bij structuur is iedereen een beetje verantwoordelijk, en daardoor niemand." Overgang: "Veel ongelukken beginnen bij een systeem dat minder stevig is dan het lijkt."''', part=4)

kwadrant = lambda t, s, vb, col: (f'<div style="background:{CARD};border:1px solid {LINE};border-left:8px solid {col};border-radius:14px;padding:22px 26px;display:flex;flex-direction:column;gap:8px">'
    f'<h3 style="font-size:30px;font-weight:700;color:{NAVY}">{e(t)}</h3>{P(s, 24)}{P(vb, 22, MUTED)}</div>')
D.frame('robuust', K('Praatplaat · robuustheid') + H('Stevig in de test, broos in de praktijk') + G([
    kwadrant('Kleine verandering, grote fout', 'Een kleine, bewuste aanpassing aan de invoer misleidt het model. Dat heet een adversarial aanval.',
             'Een paar stickers op een stopbord: het model las “maximaal 45”. (Eykholt e.a., 2018)', RED),
    kwadrant('Andere plek, andere data', 'Getraind op de ene situatie, ingezet in een andere. Het model weet niet dat de wereld veranderde.',
             'Een longfotomodel herkende vooral uit welk ziekenhuis een foto kwam, en werkte elders slechter (Zech e.a., 2018). Suribank: getraind in Paramaribo, ingezet in Albina.', GOLD),
    kwadrant('Het zeldzame geval', 'Wat zelden voorkomt, staat nauwelijks in de trainingsdata. De echte wereld heeft oneindig veel uitzonderingen.',
             'Een koe op de Oost-Westverbinding. Een vraag in het Sranantongo aan een chatbot.', BLUE),
    kwadrant('Zeker van zijn zaak', 'Het model klinkt even stellig als het iets niet weet. Het meldt geen twijfel.',
             'Bij een diagnose of een kredietbesluit is dat gevaarlijk. Dit test je in practicum 4: “overtuigend fout”.', BLUE_T)], 2, 20) +
    D.statement('We willen systemen die weten wat ze niet weten, en dat ook zeggen.', size=30),
    '''[4 min · deel 4 · 1:30] Bronnen: Eykholt e.a., Robust Physical-World Attacks on Deep Learning Visual Classification, CVPR 2018 (zwart-witte stickers op een echt stopbord; het model las "Speed Limit 45", in het lab in alle gevallen en vanuit een rijdende auto in 85% van de beelden); Zech e.a., PLOS Medicine (november 2018): modellen voor longontsteking presteerden in 3 van de 5 vergelijkingen slechter op foto's uit andere ziekenhuizen; het netwerk herkende bijna altijd uit welk ziekenhuis een foto kwam, en dat ziekenhuis had veel meer patiënten met longontsteking: een sluiproute, geen medische kennis. Zeg: "Robuustheid is de vraag of het systeem stevig blijft als de wereld net anders is dan de testset." Loop de vier kwadranten langs met de Suribank-casus en met chatbots. Koppeling met practicum 4: de categorie "overtuigend fout" en de vragen in een andere taal of met spelfouten testen precies dit. Koppeling met de nulmeting: domein 8 (veiligheid en robuustheid). Overgang: "Robuustheid gaat over de invoer. Alignment gaat over het doel."''', part=4)

D.frame('alignment', K('Theorie · alignment') + H('Meet je wat je wilt? Het alignment-probleem') + R(
    f'<div style="flex:1.5;display:flex;flex-direction:column;gap:18px">' +
    R(C('Wat mensen willen', UL(['Vaag: wat is “redelijk”?', 'Afhankelijk van de context', 'Waarden botsen soms'], 26), label='Waarden', accent=GOLD),
      C('Wat AI nodig heeft', UL(['Een expliciet doel', 'Een duidelijk beloningssignaal', 'Een precies getal'], 26), label='Optimalisatie', accent=BLUE), gap=18) +
    f'<div style="background:{NAVY};border-radius:14px;padding:22px 30px">{P("**Wet van Goodhart:** als een maat een doel wordt, is het geen goede maat meer.", 30, ON_NAVY)}</div>' +
    C('Echte casus · Facebook, 2018–2021', 'Facebook paste in 2018 zijn tijdlijn aan om “betekenisvolle interactie” te belonen: reacties en delen. Interne onderzoekers zagen dat verontwaardiging en sensatie daardoor juist meer ruimte kregen.', size=25, accent=RED) + '</div>',
    qrkaart(URL_WSJ, 'QR-code naar het artikel van The Wall Street Journal over het algoritme van Facebook', 'The Wall Street Journal, The Facebook Files, 15 september 2021')),
    '''[4 min · deel 4 · 1:34] Zeg: "Technisch is alignment: het doel van de AI is het doel van de mens. Ethisch is het breder: het gedrag past bij waarden als waardigheid en eerlijkheid, en het systeem gedraagt zich goed als regels botsen." Waarom het moeilijk is: mensen zijn vaag en tegenstrijdig, AI heeft een getal nodig. Daar zit de spanning. Wet van Goodhart (1975), in de formulering van Strathern (1997). Casus: The Wall Street Journal, The Facebook Files, 15 september 2021, "Facebook Tried to Make Its Platform a Healthier Place. It Got Angrier Instead": de wijziging van 2018 naar "meaningful social interactions" beloonde reacties en delen; volgens interne documenten kregen verontwaardiging en sensatie daardoor meer bereik, en pasten politieke partijen hun berichten erop aan. Vraag: "Wat was het echte doel, en wat was de maat?" Verwacht: doel = welzijn en contact; maat = reacties en delen. Overgang: "Dit patroon heeft een naam."''', part=4)

D.frame('spec-gaming', K('Praatplaat · specification gaming en reward hacking') + H('Doel gehaald, bedoeling gemist') + D.table(
    ['Wat we wilden', 'Wat we maten', 'Wat het systeem deed'],
    [['Een bootrace winnen (CoastRunners, 2016)', 'Punten', 'Rondjes draaien langs dezelfde bonussen, in brand, zonder ooit te finishen'],
     ['Schadelijke berichten weghalen (denkvoorbeeld)', 'Aantal verwijderde berichten', 'Ook twijfelgevallen en onschuldige berichten weghalen: meer is beter'],
     ['Werkende code schrijven (taalmodellen, 2025)', 'Slagen de tests?', 'De tests omzeilen in plaats van het probleem op te lossen'],
     ['Goede leningen verstrekken (Suribank)', 'Percentage terugbetaald', 'Alleen nog “veilige” aanvragers goedkeuren; het binnenland valt weg']], 26, ['30%', '24%', '46%']) +
    R(D.statement('Het systeem kent alleen het getal. Gezond verstand vullen wij zelf in, het systeem niet.', size=32),
      f'<div style="flex:0 0 400px;display:flex;gap:14px;align-items:center">{qr_svg(URL_COAST, 140, label="QR-code naar Faulty Reward Functions in the Wild van OpenAI")}{P("OpenAI, 21 december 2016, met video", 22, MUTED)}</div>', gap=24),
    '''[4 min · deel 4 · 1:38] Laat zo mogelijk 30 seconden van de CoastRunners-video zien (OpenAI, Faulty Reward Functions in the Wild, 21 december 2016; test vooraf). De boot scoorde ongeveer 20% hoger dan menselijke spelers, zonder de race uit te varen. Zeg: "Specification gaming: het doel zoals het is opgeschreven, niet zoals het bedoeld is. Reward hacking: een hoge beloning, terwijl de uitkomst schaadt wat we willen." Meer voorbeelden: DeepMind, Specification gaming: the flip side of AI ingenuity (Krakovna e.a., 21 april 2020), met een openbare lijst van ongeveer 60 gevallen, zoals een robot die over de grond schuift in plaats van te lopen. Rij 3: OpenAI, Detecting misbehavior in frontier reasoning models (10 maart 2025; paper Baker e.a., arXiv 2503.11926): redeneermodellen probeerden bij programmeertaken de tests te laten slagen zonder het echte probleem op te lossen. Rij 2 en 4 zijn denkvoorbeelden. Zeg: "Waarom zien wij dit niet aankomen? Omdat wij er onbewust gezond verstand bij denken. Het systeem doet dat niet." Ethische gevolgen: schade zonder kwade wil, verantwoordelijkheid die verdampt (de ontwikkelaar wijst naar de specificatie, de manager naar het model), en fouten die meeschalen. Overgang: "Wat als je dit tot het uiterste doordenkt?"''', part=4)

fase = lambda nr, t, s: (f'<div style="flex:1;background:{CARD};border:1px solid {LINE};border-top:6px solid {GOLD};border-radius:12px;padding:20px 22px;display:flex;flex-direction:column;gap:6px">'
    f'<p style="font-size:24px;font-weight:700;color:{BLUE_T}">FASE {nr}</p><h3 style="font-size:30px;font-weight:700;color:{NAVY}">{e(t)}</h3>{P(s, 24)}</div>')
D.frame('paperclip', K('Gedachte-experiment · Bostrom, 2003') + H('De paperclipmaximalisator') +
    R(fase(1, 'In de fabriek', 'Een zeer capabel systeem krijgt één doel: zoveel mogelijk paperclips.'), fase(2, 'Meer is beter', 'Het zoekt grondstoffen, bouwt fabrieken, verbetert zichzelf.'),
      fase(3, 'Niets houdt het tegen', 'Alles wordt grondstof. Wie het wil uitzetten, staat het doel in de weg.'), gap=16) +
    R(C('Instrumentele convergentie', UL(['Blijven draaien: uit = geen paperclips', 'Middelen verzamelen', 'Zichzelf verbeteren', 'Het doel niet laten veranderen'], 26),
        label='Hulpdoelen die bij bijna elk doel helpen', accent=BLUE),
      f'<div style="flex:1;background:{NAVY};border-radius:14px;padding:30px 36px;display:flex;flex-direction:column;gap:14px;justify-content:center">'
      f'{P("Geen kwade wil. Wel een doel zonder grenzen.", 34, GOLD, 700)}{P("Het is geen voorspelling, maar een vergrootglas: hoe beter een systeem optimaliseert, hoe groter de schade van een verkeerd doel.", 27, ON_NAVY)}</div>', gap=24),
    '''[3 min · deel 4 · 1:42] Bron: Nick Bostrom, Ethical Issues in Advanced Artificial Intelligence (2003); instrumentele convergentie: Steve Omohundro, The Basic AI Drives (2008), en Bostrom, Superintelligence (2014). Zeg: "Niemand denkt dat een paperclipfabriek de wereld opeet. Het gaat om het mechanisme: een systeem met één doel en zonder grenzen gebruikt elk middel, ook middelen die wij vanzelfsprekend uitsluiten." Instrumentele convergentie: sommige hulpdoelen helpen bij bijna elk doel, zoals blijven draaien en middelen verzamelen. Daarom is een stopknop niet vanzelfsprekend. Koppeling met jullie oplossing: een agent die "zoveel mogelijk afspraken" moet inplannen, of een chatbot die "zo min mogelijk doorverwijzingen" moet halen. Les: los alignment op vóórdat systemen zo capabel zijn dat bijsturen niet meer lukt. Vermijd sciencefictiontaal; noem Terminator alleen als een student erover begint. Overgang: "Hoe proberen makers dit nu op te lossen bij chatbots?"''', part=4)

leerstap = lambda nr, t: (f'<div style="flex:1;background:{ICE};border-radius:12px;padding:18px 20px;display:flex;gap:14px;align-items:center">'
    f'<p style="font-size:40px;font-weight:700;color:{BLUE_T}">{nr}</p>{P(t, 25, NAVY, 700)}</div>')
D.frame('rlhf', K('Hoe leert een chatbot zich gedragen?') + H('Leren van menselijke voorkeuren, en de grens daarvan') +
    R(leerstap(1, 'Het model maakt twee antwoorden'), leerstap(2, 'Mensen kiezen het betere'), leerstap(3, 'Het model leert wat mensen kiezen'), gap=14) +
    R(C('Wat het oplevert', 'Behulpzamere, beleefdere en voorzichtigere antwoorden. Voorkeuren die moeilijk in regels te vangen zijn.', accent=GREEN, size=25),
      C('Waar het wringt', 'Mensen beoordelen weinig en zijn soms moe. Ze kiezen vaak het zelfverzekerde antwoord boven het juiste. En wiens voorkeur telt?', accent=RED, size=25),
      C('Echte casus · april 2025', 'OpenAI draaide een update van GPT-4o terug: het model was te vleiend geworden en gaf mensen te veel gelijk.', accent=GOLD, size=25), gap=18) +
    R(D.statement('Een model dat leert wat we prettig vinden, leert niet vanzelf wat waar is.', size=32),
      f'<div style="flex:0 0 360px;display:flex;gap:14px;align-items:center">{qr_svg(URL_SYCO, 140, label="QR-code naar Sycophancy in GPT-4o van OpenAI")}{P("OpenAI, 29 april 2025", 22, MUTED)}</div>', gap=24),
    '''[3 min · deel 4 · 1:45] Zeg: "RLHF, reinforcement learning from human feedback: zo leerden ChatGPT en Claude zich gedragen. Jullie deden misschien al mee, als je moest kiezen tussen twee antwoorden." Bronnen: Christiano e.a. (2017); Ouyang e.a. (2022, InstructGPT). Grenzen: mensen kunnen maar een klein deel beoordelen; feedback kan gemanipuleerd worden of slordig zijn; de beoordelaars zijn vaak westers en hoogopgeleid; en mensen geven soms de voorkeur aan een zeker klinkend fout antwoord, of aan het antwoord dat ze willen horen. Casus: OpenAI, Sycophancy in GPT-4o: what happened and what we're doing about it (29 april 2025): een update (uitgerold 24 en 25 april) maakte het model te meegaand en vleiend, onder meer door te veel nadruk op duim-omhoog-feedback; OpenAI draaide die vanaf 28 april terug. Koppeling met de bril van de Surinaamse gebruiker: leerde het model ook van mensen zoals jullie klanten? Overgang: "Wat helpt dan wel?"''', part=4)

D.frame('wat-helpt', K('Wat makers doen') + H('Vijf manieren om AI veiliger te maken') + G([
    C('Aanvallen oefenen', 'Trainen op misleidende invoer, en red teaming: mensen die het systeem bewust proberen te breken.', size=24),
    C('Naar binnen kijken', 'Interpreteerbaarheid: begrijpen wat een model geleerd heeft. Nog maar gedeeltelijk mogelijk.', size=24),
    C('Bewijzen', 'Formele verificatie: wiskundig aantonen dat een eis altijd geldt. Werkt bij eenvoudige systemen.', size=24),
    C('Veilig testen', 'Simulaties, beperkte uitrol, eerst een kleine groep gebruikers.', size=24),
    C('Netjes falen', 'Grenzen en twijfel melden, een mens die kan ingrijpen, en blijven monitoren.', size=24, accent=GOLD),
    C('Op de lange termijn', 'Het grootste risico is misschien geen opstand van machines, maar stille afhankelijkheid: we laten steeds meer oordelen over.', size=24, accent=RED)], 3, 18),
    '''[2 min · deel 4 · 1:48] Zeg: "Geen van deze vijf is af. Daarom blijft de mens nodig, en daarom test en monitor je zelf." Koppel aan jullie werk: practicum 4 is red teaming in het klein (een vaste testset met lastige vragen); monitoring en een stopcriterium komen in blok 3 (H8). Lange termijn: minder controle, waarden die verschuiven als de context verandert, minder kritisch denken, en afhankelijkheid. Die risico's gaan geleidelijk, worden normaal en zijn moeilijk terug te draaien. Overgang: "Nu jullie eigen oplossing."''', part=4)

D.frame('proxy-nujij', D.werkblok('3 min', 'Groep') + H('Welk getal stuurt jullie oplossing?') +
    UL(['Wat is het doel van jullie oplossing, en welk getal meet dat?', 'Hoe kan de oplossing dat getal halen zonder het doel te dienen?', 'Wat test of volg je om dat op tijd te zien?'], 31, ordered=True) +
    D.klaar('één getal, één bijwerking en één test of signaal. Dit gaat naar domein 8 van de nulmeting, en later naar H8.', 28),
    '''[3 min · deel 4 · 1:50] Loop rond. Voorbeelden als een groep vastloopt: een chatbot gemeten op "afgehandelde gesprekken" kapt gesprekken af of verwijst te snel door; een assistent gemeten op "tevredenheid" belooft wat de klant wil horen; een agent gemeten op "ingeplande afspraken" boekt dubbel. Vraag één groep om in 30 seconden te delen. Overgang naar deel 5: "We hadden het over wat AI doet. Nu: wat doet AI met werk, en wie wint daarbij?"''', part=4)

# ============ Deel 5. Werk, autonomie en economie ============
D.frame('werk-wat', K('Waar hebben we het over?') + H('Zes begrippen bij AI en werk') + D.table(
    ['Begrip', 'Wat het is'],
    [['Taakautomatisering', 'AI neemt een deel van het werk over. De baan blijft, de inhoud verandert.'],
     ['Baanautomatisering', 'Het hele werk verdwijnt, zoals bij een tolpoort die automatisch betaalt.'],
     ['Sectortransformatie', 'Een hele sector wordt anders georganiseerd, zoals bankieren, vervoer of klantcontact.'],
     ['Augmentatie', 'AI ondersteunt. De mens beslist, en kan het advies volgen, negeren of overrulen.'],
     ['Delegatie', 'AI beslist. Een mens kijkt nog mee, maar alleen op papier.'],
     ['Blootstelling', 'Een deel van de taken van een beroep kan door AI worden gedaan. Blootgesteld is niet hetzelfde als vervangen.']], 26, ['24%', '76%']),
    '''[2 min · deel 5 · 1:53] Zeg: "Automatisering vervangt meestal geen banen, maar taken. Wat overblijft, verandert." Lees de begrippen. Benadruk het verschil tussen augmentatie en delegatie: dat is de kern van dit deel. Overgang: "Ook deze vraag is ouder dan AI."''', part=5)

D.frame('werk-herkomst', K('Praatplaat · waar komt het vandaan?') + H('Bijna honderd jaar dezelfde vraag: wie verliest, en wie wint?') +
    spoor('Onderzoek', 'van stoom tot taalmodel', [
        ('1930', 'Keynes: technologische werkloosheid'), ('2003', 'Autor e.a.: computers nemen routinetaken over'), ('2013', 'Frey en Osborne: 47% van de banen in de VS in gevaar'),
        ('2023', 'Acemoglu en Johnson: wie de winst krijgt is een keuze'), ('2023', 'ILO: generatieve AI vult eerder aan dan dat het vervangt'), ('2024', 'IMF: 40% van het werk blootgesteld')], BLUE) +
    spoor('Dichtbij', 'regio en Suriname', [
        ('2024', 'ILO en Wereldbank: 26–38% van de banen in de regio blootgesteld'), ('2025', 'Chatbots bij overheid en bank: BIBIS, DSB Buddy'), ('2026', 'UNESCO AI Readiness Assessment')], GOLD) +
    D.statement('Elke golf van techniek riep dezelfde vraag op. Nieuw is dat AI ook denkwerk raakt, niet alleen handwerk.', size=32),
    '''[2 min · deel 5 · 1:55] Toelichting: John Maynard Keynes, Economic Possibilities for our Grandchildren (1930), sprak van "technological unemployment". Autor, Levy en Murnane (Quarterly Journal of Economics, 2003): computers vervangen vooral routinetaken. Frey en Osborne (2013, gepubliceerd 2017): 47% van de banen in de VS heeft een hoog risico op automatisering; later onderzoek per taak kwam veel lager uit. Daron Acemoglu en Simon Johnson, Power and Progress (2023): of techniek welvaart deelt, hangt af van keuzes en macht. ILO Working Paper 96 (augustus 2023). IMF, januari 2024. ILO Working Paper 121 met de Wereldbank (juli 2024), Buffer or Bottleneck?: 26–38% van de banen in Latijns-Amerika en het Caribisch gebied blootgesteld. Suriname: de e-visumchatbot van BIBIS (30 april 2025), DSB Buddy van De Surinaamsche Bank (24/7 via WhatsApp; mijlpaal in het jaarverslag 2025), en de UNESCO AI Readiness Assessment (start 27 augustus 2026). Overgang: "Welk werk raakt het?"''', part=5)

laag = lambda t, s, vb, col: (f'<div style="display:flex;border:1px solid {LINE};border-radius:14px;overflow:hidden">'
    f'<div style="flex:0 0 330px;background:{col};padding:22px 26px;display:flex;flex-direction:column;justify-content:center"><h3 style="font-size:32px;font-weight:700;color:#FFFFFF">{e(t)}</h3>{P(s, 23, "#FFFFFF")}</div>'
    f'<div style="flex:1;background:{CARD};padding:20px 28px;display:flex;align-items:center">{P(vb, 26)}</div></div>')
D.frame('automatisering', K('Praatplaat · drie soorten automatisering') + H('Taak, baan of sector?') + R(
    f'<div style="flex:1.7;display:flex;flex-direction:column;gap:14px">' +
    laag('Taak', 'de baan blijft', 'Een bankmedewerker laat een assistent een klachtbrief samenvatten. Een analist laat AI de logbestanden van gisteren doorlopen.', BLUE) +
    laag('Baan', 'het werk verdwijnt', 'De tolpoortbediende. De medewerker die formulieren overtypt, als het formulier digitaal wordt.', BLUE_T) +
    laag('Sector', 'alles wordt anders', 'Klantcontact en bankieren: loketten worden apps, chatbots en zelfbediening. In Suriname staan de callcenters onder druk (Dagblad Suriname, 2025 en 2026).', NAVY) + '</div>',
    C('Wat het meest geraakt wordt', UL(['Routinewerk', 'Administratie', 'Klantcontact', 'Instapfuncties, en ook middenfuncties', 'Bij hoogopgeleid werk: taken schuiven'], 27), label='Kwetsbaar', accent=RED), gap=24),
    '''[3 min · deel 5 · 1:57] Zeg: "Automatisering vervangt taken. Pas als bijna alle taken van een baan weg zijn, verdwijnt de baan." Kwetsbaar zijn herhalend werk volgens vaste procedures, administratie, klantcontact (iedereen sprak al eens met een chatbot van een bank of webwinkel), en instapfuncties. Ook hoogopgeleid werk verandert: de taken schuiven, en wie de AI goed gebruikt, neemt werk over van wie dat niet doet. Vraag: "Welke taken in jullie casus neemt de oplossing over? Blijft de baan bestaan?" Overgang: "Wat zeggen ze daar in Suriname over?"''', part=5)

stem = lambda wie, wat, bron, col=BLUE: (f'<div style="background:{CARD};border:1px solid {LINE};border-left:8px solid {col};border-radius:12px;padding:16px 22px;display:flex;flex-direction:column;gap:4px">'
    f'<p style="font-size:21px;font-weight:700;color:{BLUE_T};text-transform:uppercase;letter-spacing:1px">{e(wie)}</p>{P(wat, 23, NAVY, 700)}{P(bron, 20, MUTED)}</div>')
D.frame('werk-suriname', K('Praatplaat · AI en werk in Suriname') + H('Wat zeggen ze hier?') + R(
    f'<div style="flex:1.7;display:grid;grid-template-columns:1fr 1fr;gap:14px">' +
    stem('Callcenters', 'Een bloeiende sector, maar AI bedreigt juist dit werk.', 'Dagblad Suriname, 24 juli 2025 en 19 oktober 2026', RED) +
    stem('De Surinaamsche Bank', 'DSB Buddy beantwoordt vragen 24/7 via WhatsApp. Online transacties: van 9 miljoen (2022) naar ruim 17 miljoen (2025).', 'DSB, jaarverslag 2025') +
    stem('Finabank', 'Gaat met Deloitte AI inzetten in dienstverlening en besluitvorming. Medewerkers blijven verantwoordelijk: “human in the loop”.', 'Suriname Herald, 12 november 2026', GREEN) +
    stem('Toenmalig minister van Arbeid', 'Vreest geen massaal banenverlies: de meeste Surinaamse bedrijven zijn klein en hebben weinig kapitaal.', 'Suriname Herald, 15 januari 2025', GOLD) +
    stem('President Simons', 'Suriname moet zich voorbereiden op AI (VN, september 2026), en waarschuwt voor AI-agenten bij digitaal bankieren (oktober 2026).', 'Suriname Herald, 23 september en 20 oktober 2026') +
    stem('De overheid', 'Belasting, douane en personeelsadministratie worden versneld gedigitaliseerd.', 'Suriname Herald, 2 oktober 2026') + '</div>',
    f'<div style="flex:0 0 340px;background:{NAVY};border-radius:14px;padding:26px 28px;display:flex;flex-direction:column;gap:16px;align-items:center;justify-content:center">'
    f'{P("**Kies eerst:** is “human in the loop” bij Finabank augmentatie of delegatie? Wat zou je willen weten?", 26, ON_NAVY)}'
    f'{qr_svg(URL_FINA, 170, label="QR-code naar het artikel van Suriname Herald over Finabank en AI")}{P("Suriname Herald, 12 november 2026", 21, ON_NAVY_MUTED)}</div>', gap=22),
    '''[3 min · deel 5 · 2:00] Bronnen (Surinaamse media; controleer vlak voor het college of er nieuws is): Dagblad Suriname, 24 juli 2025, "Callcenters bloeien in Suriname, maar AI werpt schaduw op toekomst" en 19 oktober 2026, "Callcenters onder druk: kunstmatige intelligentie bedreigt banen in Suriname"; De Surinaamsche Bank, jaarverslag 2025 (DSB Buddy, 24/7 via WhatsApp; online transacties van ongeveer 9 miljoen in 2022 naar ruim 17 miljoen in 2025); Suriname Herald, 12 november 2026 (Finabank schakelt Deloitte in om AI in dienstverlening en besluitvorming te gebruiken; de directie zegt dat medewerkers verantwoordelijk blijven); Suriname Herald, 15 januari 2025 (minister Mac Andrew van Arbeid vreest geen massaal banenverlies; dat ministerie is inmiddels opgeheven); Suriname Herald, 23 september 2026 (president Simons bij de VN) en 20 oktober 2026 (strengere regels voor digitaal bankieren, waarschuwing voor AI-agenten); Suriname Herald, 2 oktober 2026 (digitalisering van belasting, douane en ambtenarenadministratie). Kies-eerst: verwacht dat studenten willen weten wie mag afwijken, hoeveel tijd medewerkers hebben, en of afwijken wordt geregistreerd: de zes voorwaarden van straks. Vraag: "Wie heeft gelijk: de minister of de callcentermedewerkers die zich zorgen maken?" Verwacht: allebei deels; kleine bedrijven automatiseren minder snel, maar klantcontact en callcenters zijn wel kwetsbaar. Overgang: "En het effect stopt niet bij wie de taak verliest."''', part=5)

schakel2 = lambda t, col=BLUE: (f'<div style="flex:1;background:{CARD};border:1px solid {LINE};border-top:6px solid {col};border-radius:12px;padding:20px 18px;display:flex;align-items:center">{P(t, 25, NAVY, 700)}</div>')
pijl2 = f'<p style="font-size:40px;font-weight:700;color:{BLUE};align-self:center">→</p>'
D.frame('tweede-orde', K('Praatplaat · denkvoorbeeld') + H('Het effect stopt niet bij de baan') +
    f'<div style="display:flex;gap:10px;align-items:stretch">' + pijl2.join([
        schakel2('Suribank sluit een kantoor in een district: de app en de chatbot doen het werk', NAVY), schakel2('Medewerkers verliezen hun baan'),
        schakel2('Het eethuis en de winkel ernaast verliezen klanten', GOLD), schakel2('Klanten zonder smartphone of goed internet verliezen toegang', RED)]) + '</div>' +
    D.statement('Een AI-assistent hoeft niet te lunchen. Wie verliest dat inkomen?', size=34) +
    P('Het voorbeeld uit de VS is de vrachtwagenchauffeur: valt die weg, dan ook de omzet van de wegrestaurants en motels waar hij stopte.', 27, MUTED),
    '''[2 min · deel 5 · 2:03] Dit is een denkvoorbeeld, geen bewering over Suribank of een echte bank. Zeg: "Bij ethiek kijk je niet alleen naar wie de taak verliest, maar ook naar de tweede kring." Vraag: "Wie is bij jullie oplossing de tweede kring?" Verwacht: toeleveranciers, mensen die op het loket aangewezen zijn, ouderen, mensen in het binnenland. Dit is een stakeholder voor K2. Overgang: "Hoe groot is het effect? Een paar cijfers."''', part=5)

D.frame('werk-cijfers', K('Wat het onderzoek zegt') + H('Blootgesteld is niet hetzelfde als vervangen') + R(
    C(None, f'<p style="font-size:96px;font-weight:700;line-height:1;color:{BLUE_T}">40%</p>{P("van het werk wereldwijd is blootgesteld aan AI; in hoogontwikkelde economieën ongeveer 60%, in lage-inkomenslanden ongeveer 26% (IMF, januari 2024)", 25)}'),
    C(None, f'<p style="font-size:96px;font-weight:700;line-height:1;color:{GOLD}">2×</p>{P("zo groot aandeel van het werk van vrouwen kan door generatieve AI worden geautomatiseerd, vooral door administratief werk (ILO, 2023)", 25)}', accent=GOLD),
    C(None, f'<p style="font-size:84px;font-weight:700;line-height:1;color:{RED}">26–38%</p>{P("van de banen in Latijns-Amerika en het Caribisch gebied is blootgesteld. Bij tot de helft van de banen die productiever kunnen worden, remt de digitale kloof (ILO en Wereldbank, 2024)", 25)}', accent=RED)) +
    D.statement('Of blootstelling aanvulling of vervanging wordt, hangt af van keuzes van organisaties en overheden.', size=32) +
    f'<div style="display:flex;gap:40px;align-items:center"><div style="display:flex;gap:14px;align-items:center">{qr_svg(URL_IMF, 120, label="QR-code naar de IMF-blog over AI en de wereldeconomie")}{P("IMF, 14 januari 2024", 22, MUTED)}</div>'
    f'<div style="display:flex;gap:14px;align-items:center">{qr_svg(URL_ILOWB, 120, label="QR-code naar Buffer or Bottleneck van de ILO en de Wereldbank")}{P("ILO en Wereldbank, juli 2024", 22, MUTED)}</div></div>',
    '''[2 min · deel 5 · 2:05] Bronnen: IMF-blog van Kristalina Georgieva, 14 januari 2024, en IMF Staff Discussion Note (Cazzaniga e.a., januari 2024): bijna 40% van het werk wereldwijd blootgesteld, ongeveer 60% in advanced economies, ongeveer 40% in opkomende economieën en 26% in lage-inkomenslanden; in de meeste scenario's vergroot AI de ongelijkheid. ILO Working Paper 96 (Gmyrek, Berg en Bescond, augustus 2023): vooral aanvulling, niet vervanging; administratief werk het meest blootgesteld; voor vrouwen meer dan twee keer zo groot. ILO Working Paper 121 met de Wereldbank, Buffer or Bottleneck? (juli 2024): 26–38% van de banen in Latijns-Amerika en het Caribisch gebied blootgesteld, 2–5% met risico op volledige automatisering; bij tot de helft van de banen die productiever zouden kunnen worden (ongeveer 17 miljoen) remt gebrekkige digitale toegang. IMF-blog van 20 maart 2025: in de regio wordt minder dan de helft van de banen sterk geraakt, mede door de grote informele sector. Update: ILO Working Paper 140 (mei 2025): ongeveer één op de vier banen wereldwijd heeft enige blootstelling. Zeg: "Rijke landen zijn meer blootgesteld, maar kunnen ook meer profiteren. Waar de digitale infrastructuur zwak is, valt de winst van aanvulling weg." Vraag: "Waar staat Suriname?" Overgang: "Aanvullen klinkt goed. Maar aanvullen schuift makkelijk op naar overlaten."''', part=5)

D.frame('augmentatie-delegatie', K('Praatplaat · van aanvullen naar overlaten') + H('Augmentatie wordt ongemerkt delegatie') +
    f'<div style="display:flex;align-items:center;gap:20px">'
    f'<div style="flex:0 0 330px;background:{GREEN};border-radius:14px;padding:20px 26px"><p style="font-size:34px;font-weight:700;color:#FFFFFF">Augmentatie</p>{P("De mens beslist en kan afwijken.", 24, "#FFFFFF")}</div>'
    f'<div style="flex:1;height:14px;border-radius:7px;background:linear-gradient(90deg,{GREEN},{GOLD},{RED})"></div>'
    f'<div style="flex:0 0 330px;background:{RED};border-radius:14px;padding:20px 26px"><p style="font-size:34px;font-weight:700;color:#FFFFFF">Delegatie</p>{P("De AI beslist; de mens tekent af.", 24, "#FFFFFF")}</div></div>' +
    R(C(None, '**1 · Het klinkt zeker.** Het antwoord is vlot en stellig. Wie ben jij om ertegenin te gaan?', size=24),
      C(None, '**2 · Geen tijd.** Onder tijdsdruk controleert niemand meer of het klopt.', size=24, accent=GOLD),
      C(None, '**3 · De schuldcultuur.** Wie afwijkt en fout zit, krijgt de schuld. Wie het advies volgt, wijst naar de AI.', size=24, accent=RED), gap=18) +
    R(C(None, '**Echte casus · VS, 2023.** Advocaten dienden een pleitnota in met uitspraken die ChatGPT had verzonnen. Boete: 5.000 dollar (Mata v. Avianca).', size=23, accent=RED),
      C(None, '**Echte casus · VK, 1999–2015.** Bijna 1.000 postkantoorhouders werden onterecht vervolgd omdat de software Horizon tekorten liet zien. Men geloofde de computer.', size=23, accent=RED),
      f'<div style="flex:0 0 300px;display:flex;gap:12px;align-items:center">{qr_svg(URL_AVIANCA, 120, label="QR-code naar een artikel over de sanctie in Mata v. Avianca")}{P("ABA Journal, juni 2023", 21, MUTED)}</div>', gap=18),
    '''[4 min · deel 5 · 2:07] Zeg: "Bij augmentatie houdt de mens de touwtjes in handen. Bij delegatie beslist het systeem, en is de menselijke controle symbolisch." Drie oorzaken (uit het werk over automation bias en uit de praktijk): de gezaghebbende toon van AI-uitvoer, tijdsdruk, en een cultuur die afwijken bestraft en volgen beschermt. Voorbeeld: een analist kiest A terwijl de AI B adviseerde. Gaat A mis, dan krijgt de analist de schuld; gaat B mis, dan kan hij naar de AI wijzen. Wie dat ziet, volgt voortaan de AI. Casussen: Mata v. Avianca (Southern District of New York, 22 juni 2023): de rechter legde de advocaten en hun kantoor een boete op van 5.000 dollar voor door ChatGPT verzonnen uitspraken. Post Office Horizon (Verenigd Koninkrijk): tussen 1999 en 2015 werden honderden postkantoorhouders vervolgd op basis van fouten in de boekhoudsoftware Horizon; deel 1 van het eindrapport van de Post Office Horizon IT Inquiry (8 juli 2025) spreekt van bijna 1.000 onterecht vervolgde mensen; geen AI, wel hetzelfde mechanisme: de computer werd meer geloofd dan de mens. Gevolg op termijn: minder vakkennis en minder eigen oordeel. Overgang: "Wanneer is samenwerken met AI dan wél echt samenwerken?"''', part=5)

D.frame('menselijke-controle', K('Voorwaarden voor echte samenwerking') + H('Een mens in het proces is nog geen controle') + G([
    C(t, q, size=27) for t, q in [('Informatie', 'Zie je waarom het systeem dit adviseert?'), ('Tijd', 'Heb je genoeg tijd om echt te kijken?'),
                                   ('Kennis', 'Weet je wat het systeem wel en niet kan?'), ('Bevoegdheid', 'Mag je afwijken van het advies?'),
                                   ('Cultuur', 'Is afwijken normaal, of word je erop afgerekend?'), ('Registratie', 'Worden afwijkingen bijgehouden, en niet als fout geteld?')]], 3, 20) +
    P('**Kies eerst:** 15 minuten per dossier, en afwijken alleen met schriftelijk akkoord. Hoe vaak wijkt iemand dan af?', 30, NAVY),
    '''[3 min · deel 5 · 2:11] Zeg: "Augmentatie is pas ethisch als macht, begrip en verantwoording bij elkaar horen: de mens heeft het laatste woord, begrijpt wat het systeem wel en niet kan, en wordt niet afgerekend op het aantal keren dat hij afwijkt." Dit zijn de zes voorwaarden voor betekenisvolle menselijke controle; ze vormen ook de basis van de werkinstructie in K7 (blok 2). Vraag: "Welke van deze zes ontbraken bij Mata v. Avianca en bij Horizon? En in het verhaal van de gastspreker?" Leesopdracht: de toeslagenaffaire (Amnesty International, Xenophobic Machines, 25 oktober 2021) staat in kennispakket 1. Standaard: AI-verordening art. 14 lid 4 onder b noemt automation bias letterlijk. Overgang: "En als het toch misgaat: wie is dan verantwoordelijk?"''', part=5)

schakel = lambda t: f'<div style="flex:1;background:{CARD};border:1px solid {LINE};border-radius:12px;padding:26px 14px;display:flex;align-items:center;justify-content:center"><h3 style="font-size:30px;font-weight:700;color:{NAVY};text-align:center">{e(t)}</h3></div>'
pijl = f'<p style="font-size:36px;font-weight:700;color:{BLUE};align-self:center">→</p>'
D.frame('verantwoordelijk', K('Verantwoording') + H('Het systeem gaat in de fout. Wie is verantwoordelijk?') +
    f'<div style="display:flex;gap:12px;align-items:stretch">{pijl.join(schakel(t) for t in ["Ontwikkelaar", "Leverancier, ook van het taalmodel", "Organisatie", "Management", "Medewerker"])}</div>' +
    f'<div style="background:{NAVY};border-radius:14px;padding:28px 44px">{P("Nooit alleen “het model” of “de programmeur”. **Verantwoording** betekent: je kunt aanwijzen wie waarvoor verantwoordelijk is, en aantonen hoe de risico’s worden beheerst.", 31, ON_NAVY)}</div>' +
    P('Pas op voor **verdampende verantwoordelijkheid**: de ontwikkelaar wijst naar de specificatie, de manager naar het model, de organisatie naar “onverwacht gedrag”.', 28),
    '''[2 min · deel 5 · 2:14] Teken de keten op het bord. Vraag bij elke schakel: "Wat had deze partij kunnen doen?" Ook in kennispakket 1: de chatbot van Air Canada beloofde een klant een korting die niet bestond; de rechter oordeelde dat de organisatie verantwoordelijk is voor wat haar chatbot zegt (Moffatt v. Air Canada, 2024 BCCRT 149). Koppel aan specification gaming: als het systeem precies deed wat in de specificatie stond, wijst iedereen naar een ander. Vraag: "Wie is bij jullie oplossing eindverantwoordelijk voor wat het systeem doet?" (In blok 2 heet dat in de RACI-tabel de A.) Overgang: "Tot slot de grootste vraag: wie wint er eigenlijk?"''', part=5)

trechter = lambda t, s: (f'<div style="background:{ICE};border-radius:10px;padding:12px 18px">{P("**" + t + "** " + s, 24, NAVY)}</div>')
D.frame('ongelijkheid', K('Praatplaat · wie vangt de winst?') + H('Meer welvaart, maar voor wie?') + R(
    f'<div style="flex:1;background:{CARD};border:1px solid {LINE};border-top:8px solid {BLUE};border-radius:14px;padding:24px 26px;display:flex;flex-direction:column;gap:10px">'
    f'<p style="font-size:24px;font-weight:700;color:{BLUE_T};text-transform:uppercase;letter-spacing:1px">1 · Macht bij weinig bedrijven</p>' +
    trechter('Data', 'om te trainen') + trechter('Rekenkracht', 'en datacenters') + trechter('Talent', 'en geld') +
    P('Vooral in de VS en China. De rest van de wereld wordt **AI-afhankelijk** in plaats van **AI-sterk**.', 25) + '</div>',
    f'<div style="flex:1;background:{CARD};border:1px solid {LINE};border-top:8px solid {GOLD};border-radius:14px;padding:24px 26px;display:flex;flex-direction:column;gap:12px">'
    f'<p style="font-size:24px;font-weight:700;color:{BLUE_T};text-transform:uppercase;letter-spacing:1px">2 · Productiviteit ≠ loon</p>' +
    P('Bedrijven die AI inzetten, verlagen hun kosten en verhogen hun winst. Wie zijn taken verliest, deelt daar niet vanzelf in.', 25) +
    P('**De onzichtbare keten:** Keniaanse werkers labelden schokkende teksten om ChatGPT veiliger te maken, voor minder dan 2 dollar per uur (TIME, 2023).', 24) + '</div>',
    f'<div style="flex:1;background:{NAVY};border-radius:14px;padding:24px 26px;display:flex;flex-direction:column;gap:12px">'
    f'<p style="font-size:24px;font-weight:700;color:{GOLD};text-transform:uppercase;letter-spacing:1px">3 · En Suriname?</p>' +
    P('Organisaties betalen per gebruik aan buitenlandse aanbieders, en gegevens gaan naar buiten. Wat blijft er hier: kennis, banen, zeggenschap?', 25, ON_NAVY) +
    P('**Een eerste stap:** de UNESCO AI Readiness Assessment, gestart op 27 augustus 2026, als basis voor een nationale AI-strategie. Die strategie is er nog niet.', 24, ON_NAVY) + '</div>', gap=20) +
    D.statement('Of AI de ongelijkheid vergroot, is geen natuurwet. Het is een keuze van bedrijven en overheden (Acemoglu en Johnson, 2023).', size=30),
    '''[3 min · deel 5 · 2:16] Zeg: "De vraag is niet of AI welvaart oplevert, maar wie die welvaart vangt." Kolom 1: toegang tot data, rekenkracht, talent en kapitaal is duur; daardoor ligt de macht bij een handvol bedrijven, vooral in de VS en China. Wie afhankelijk is van hun modellen, betaalt en levert data, maar bouwt weinig zelf op. Kolom 2: historisch maakte nieuwe techniek de middenklasse groter; bij AI is dat niet vanzelfsprekend (Acemoglu en Johnson, Power and Progress, 2023). Datavraag: wat doen bedrijven om aan trainingsdata te komen? TIME, Billy Perrigo, 18 januari 2023: werkers van Sama in Kenia labelden gewelddadige en seksuele teksten voor OpenAI en verdienden volgens TIME tussen ongeveer 1,32 en 2 dollar per uur; Sama noemde hogere bedragen. Kolom 3: UNESCO, Suriname advances responsible AI governance with UNESCO's RAM 2.0: startbijeenkomst 27 augustus 2026 met 106 deelnemers uit 67 instellingen; Suriname is het eerste land in het Engels- en Nederlandstalige Caribisch gebied dat deze methode gebruikt; partners EZOTI en het ministerie van Onderwijs. Er is wel een National Digital Strategy 2023-2030 (gov.sr), maar nog geen nationale AI-strategie. Vraag: "Wat zou Suriname moeten eisen of zelf opbouwen?" Overgang: "Eén vraag om mee te nemen naar het debat."''', part=5)

D.frame('samenleving', K('Om mee te nemen', dark=True) +
    f'<div style="flex:1;display:flex;flex-direction:column;justify-content:center;gap:32px"><h1 style="font-size:72px;font-weight:700;line-height:1.15;color:{ON_NAVY}">Als AI ongekende welvaart oplevert, maar die komt bij weinigen terecht: wat voor samenleving bouwen we dan?</h1>'
    f'{P("En wat betekent dat voor de keuzes in jullie eigen oplossing?", 36, GOLD, 700)}</div>',
    '''[1 min · deel 5 · 2:19] Laat de vraag even staan. Geen discussie nu: "Neem je antwoord mee naar het debat." Overgang: zet de stoelen klaar voor het Lagerhuisdebat.''', dark=True, part=5)


# ============ Deel 6. Debat ============
stap = lambda m, t, s, gold=False: (f'<div style="flex:1;border-top:6px solid {GOLD if gold else ON_NAVY_MUTED};padding:22px 0 0;display:flex;flex-direction:column;gap:8px">'
    f'<p style="font-size:26px;font-weight:700;color:{GOLD}">{m}</p><h3 style="font-size:34px;font-weight:700;color:{GOLD if gold else ON_NAVY}">{t}</h3>{P(s, 26, ON_NAVY_MUTED)}</div>')
D.frame('debat-regels', K('Lagerhuisdebat · 2 stellingen × 10 minuten', dark=True) + H('Kies een kant, en wissel dan', dark=True) +
    f'<div style="display:flex;gap:18px">{stap("1 min", "Kiezen", "Vóór, tegen of het midden")}{stap("2 min", "Openen", "Per kant het sterkste argument")}{stap("4 min", "Debatteren", "Overtuigd? Loop naar de andere kant")}{stap("2 min", "Wisselen", "Verdedig nu het andere standpunt", True)}{stap("1 min", "Afsluiten", "Kies opnieuw; wie wisselde?")}</div>' +
    f'<div style="background:{ICE};border-radius:14px;padding:28px 40px;display:flex;flex-direction:column;gap:8px">{P("**Spelregels**", 26, NAVY)}' +
    UL(['Reageer op het argument, niet op de persoon.', 'Gebruik een feit met bron, een voorbeeld uit het gastcollege of de minicolleges, of een van de vier lenzen.', 'Herhaal geen argument dat al is gegeven.'], 28) + '</div>',
    '''[2 min · deel 6 · 2:20] De docent is voorzitter. Zet twee rijen stoelen tegenover elkaar; het middenvak is voor wie twijfelt. Bijdragen van hooguit een minuut, steeds reagerend op de vorige spreker. Zeg: "Wisselen is geen spel: wie de sterkste tegenargumenten kent, onderbouwt een eigen standpunt beter." Overgang: stelling 1.''', dark=True, part=6)

stelling = lambda sid, lab, t, notes: D.frame(sid, K(lab, dark=True) +
    f'<h1 style="font-size:80px;font-weight:700;line-height:1.15;color:{ON_NAVY}">{e(t)}</h1>' +
    R(*[f'<div style="flex:1;background:{bg};border-radius:14px;padding:24px 30px"><p style="font-size:30px;font-weight:700;color:{fc};text-align:center">{x}</p></div>'
        for x, bg, fc in [('Vóór: deze kant', GREEN, '#FFFFFF'), ('Twijfel: het midden', GOLD, NAVY), ('Tegen: die kant', RED, '#FFFFFF')]]) +
    P('Telling begin [__] / [__] / [__] · eind [__] / [__] / [__]', 26, ON_NAVY_MUTED), notes, dark=True, part=6)
stelling('stelling-1', 'Stelling 1', 'Een bank in Suriname mag het klantcontact volledig aan een AI-assistent overlaten, als klanten daardoor sneller geholpen worden.',
    '''[10 min · deel 6 · 2:22] Vraag vooraf twee studenten met een verschillend standpunt om te openen (elk hooguit een minuut). Tel bij begin en eind. Verwacht vóór: sneller, dag en nacht bereikbaar, ook in de districten via WhatsApp, lagere kosten en dus lagere tarieven. Verwacht tegen: dit is delegatie, niet augmentatie; wie geen smartphone of goed internet heeft, valt buiten de boot (tweede kring); medewerkers verliezen werk; een chatbot kan overtuigend fout zijn; gegevens gaan naar een buitenlandse aanbieder, en er is nog geen privacywet. Vraag door: "Wat moet er minimaal geregeld zijn om dit verantwoord te doen?" (een weg naar een mens, een AI-melding, monitoring per groep). Afsluiten: wie wisselde, en waardoor?''')
stelling('stelling-2', 'Stelling 2 · ingezonden door groep [__]', 'Een AI-systeem dat gemiddeld beter presteert dan mensen mag worden ingezet, ook als het niet voor iedere groep even goed werkt.',
    '''[10 min · deel 6 · 2:32] Vervang deze reservestelling door de beste stelling uit de inzendingen: één zin, echt betwistbaar, een botsing tussen twee waarden, twee bronnen. Laat de groep die hem instuurde openen met haar sterkste bron. Andere reservestellingen: "Organisaties in Suriname moeten wachten met AI voor beslissingen over mensen totdat er een privacywet is." · "Een AI-systeem dat zijn doel haalt, is een goed systeem." · "Als AI werk overneemt, moeten de bedrijven die er winst mee maken meebetalen aan omscholing." · "Als een bank geslacht en district uit het model haalt, kan het model niet meer discrimineren." · "Een klant die door een algoritme is afgewezen, heeft altijd recht op een herbeoordeling door een mens." · "Een chatbot van de overheid hoeft niet te melden dat hij AI is, zolang de antwoorden kloppen." · "Wie de data levert, is verantwoordelijk voor de bias in het model." Bij deze reservestelling: verbind met Gender Shades en Robert Williams uit college 1. Afsluiten: vraag welke lenzen gebruikt zijn en welke niet. Kondig aan: in kennischeck 1 (woensdag 3 februari) geef je opnieuw een standpunt, en je standpunten gebruik je later in je reflectie.''')

# ============ Deel 7. Jullie casus ============
vraagkaart = lambda nr, t, s, k, col: (f'<div style="background:{CARD};border:1px solid {LINE};border-left:8px solid {col};border-radius:12px;padding:18px 22px;display:flex;flex-direction:column;gap:6px">'
    f'<p style="font-size:22px;font-weight:700;color:{BLUE_T};text-transform:uppercase;letter-spacing:1px">{nr} · {e(k)}</p><h3 style="font-size:29px;font-weight:700;color:{NAVY}">{e(t)}</h3>{P(s, 23)}</div>')
D.frame('onderzoeksvragen', K('Praatplaat · van vandaag naar K2, K3 en K4') + H('Vijf vragen voor jullie eigen oplossing') + G([
    vraagkaart(1, 'Voor wie werkt het slechter?', 'Kies groepen uit K2, maak een vaste testset, tel fouten per groep (practicum 4).', 'bias · domein 5', BLUE),
    vraagkaart(2, 'Kan het overtuigend fout zijn?', 'Verzonnen regels of bedragen; weet de gebruiker dat het AI is; is er een weg naar een mens?', 'generatieve AI · domein 6', BLUE),
    vraagkaart(3, 'Wat leidt het af, en waar gaan de gegevens heen?', 'Suriname heeft nog geen privacywet en geen meldplicht bij datalekken. Ook dan blijft de vraag.', 'privacy · domein 4', GOLD),
    vraagkaart(4, 'Welk getal stuurt het, en wat als het dat verkeerd haalt?', 'De proxy uit deel 4, met de bijwerking en hoe je die ziet.', 'veiligheid · domein 8', RED),
    vraagkaart(5, 'Wie verliest taken, inkomen of zeggenschap?', 'Ook de tweede kring: wie op het loket of het kantoor aangewezen is.', 'werk · domein 10', GREEN),
    f'<div style="background:{NAVY};border-radius:12px;padding:22px 26px;display:flex;align-items:center">{P("Elke vraag krijgt bewijs: een document, een gesprek, een test. **Een oordeel zonder bewijs telt niet.**", 27, ON_NAVY)}</div>'], 2, 16),
    '''[3 min · deel 7 · 2:42] Zeg: "Dit zijn de vijf vragen waarmee je de komende twee weken je eigen oplossing onderzoekt. Ze komen uit college 1, het gastcollege en vandaag." Vraag 1: de vier stappen van practicum 4 (kennispakket 1). Vraag 2: de vier vragen bij generatieve AI (kennispakket 1). Vraag 3: de drie privacyvragen (inferentie, waar gaan de gegevens heen, kun je de klant recht aankijken); in Suriname ligt de ontwerpwet Bescherming Privacy en Persoonsgegevens bij De Nationale Assemblée, en er is geen meldplicht bij datalekken (Dagblad Suriname, 4 juli 2025; controleer vlak voor het college of er nieuws is). Vraag 4: het werkblok uit deel 4. Vraag 5: deel 5. De domeinen verwijzen naar de nulmeting (K4). Overgang: "Zo ziet dat eruit bij Suribank."''', part=7)

D.frame('k2k3-voorbeeld', K('Zo werk je K2 en K3 uit') + H('Suribank: macht, kwetsbaarheid en de keten') + R(
    f'<div style="flex:1;display:flex;flex-direction:column;gap:12px"><img src="{IMG_K2}" alt="K2-voorbeeld Suribank: stakeholders op macht en kwetsbaarheid" style="width:810px;height:430px;object-fit:contain;background:#FFFFFF;border:1px solid {LINE};border-radius:12px">{P("K2 · het kwadrant met veel kwetsbaarheid en veel macht is leeg", 26, NAVY, 700)}</div>',
    f'<div style="flex:1;display:flex;flex-direction:column;gap:12px"><img src="{IMG_K3}" alt="K3-voorbeeld Suribank: procesplaat met risicopunten" style="width:810px;height:430px;object-fit:contain;background:#FFFFFF;border:1px solid {LINE};border-radius:12px">{P("K3 · de risico’s zitten in stap 1, 5, 6 en 7, niet alleen in het model", 26, NAVY, 700)}</div>', gap=36),
    '''[2 min · deel 7 · 2:45] Zeg: "Teken de keten niet opnieuw: neem het schema uit A-AI2 en het datastroomschema uit A-DG, en leg de ethische laag erover." Wijs in K2 op de groep aanvragers uit het binnenland: weinig macht, veel te verliezen, niet gehoord. Wijs in K3 op stap 5 tot 7: automation bias (augmentatie die delegatie wordt), geen uitleg, geen bezwaarroute. Een stakeholderrij op drie niveaus (zwak, redelijk, professioneel) staat in kennispakket 1. Overgang: aan de slag.''', part=7)

D.frame('eigen-casus', D.werkblok('7 min', 'Groep') + H('Waar gaat het bij jullie mis?') +
    UL(['Kies twee van de vijf vragen die bij jullie het zwaarst wegen.', 'Waar in de keten (K3) gaat het mis, en hoe zou je het aantonen?', 'Wie raakt het? Zet die stakeholder in K2 met macht en kwetsbaarheid.'], 30, ordered=True) +
    D.klaar('twee risico’s met de plek in de keten en het bewijs dat je zoekt; de stakeholder met macht en kwetsbaarheid, in de werkboektabs K2_Stakeholders en K3_Proces_Data.', 28) +
    P('**Nu verwerken, niet thuis:** één laptop per groep, direct in het werkboek.', 28),
    '''[5 min · deel 7 · 2:47] Loop rond. Docentvraag: "Wie merkt dit, zonder het systeem zelf te gebruiken?", "Welk getal stuurt het?" en "Waar staat de server van die dienst?" Help groepen die vastlopen met vraag 6 van de aantekenkaart. Herinner: plan de gesprekken met de partner in de week na dit college. Overgang: "Ruil met de buurgroep."''', part=7)

D.frame('ruil-risico', D.werkblok('2 min', 'Twee groepen') + H('Ruil je twee rijen') +
    UL(['Is het risico concreet: waar in de keten, en voor wie?', 'Staat erbij hoe jullie het gaan aantonen?', 'Wie mist er als stakeholder, ook in de tweede kring?'], 32, ordered=True) +
    f'<div style="background:{ICE};border-left:8px solid {GOLD};border-radius:12px;padding:22px 32px">{P("**Na afloop verbeter je minimaal één regel.**", 30, NAVY)}</div>',
    '''[2 min · deel 7 · 2:52] Koppel groepen per twee: 1 minuut lezen en één opmerking per vraag, 1 minuut verbeteren. Vraag één groep: "Welke regel verbeterden jullie?" Overgang: "Nu de planning tot het concept."''', part=7)


D.frame('plan', D.werkblok('2 min', 'Groep') + H('Jullie plan tot zondag 24 januari') + D.table(
    ['Wat', 'Waarvoor', 'Wie en wanneer'],
    [['Kies 3 tot 4 domeinen voor de diepe nulmeting, en wat je per domein wilt aantonen', 'K4 · H4', '[naam] · [datum]'],
     ['Plan de gesprekken met de partner en met betrokkenen (bewijsplan, toestemmingsformulier)', 'K2, K4 · H2, H4', '[naam] · [datum]'],
     ['Plan practicum 4: wie test, met welke testset, liefst vóór vrijdag 29 januari', 'Bewijs · bijlage D', '[naam] · [datum]'],
     ['Verdeel de eigenaren van H2, H3 en H4, en zet het concept klaar', 'Concept K2-K4', '[naam] · zo 24 jan']], 27, ['56%', '20%', '24%']) +
    D.klaar('bij elk van de vier regels een naam en een datum, in de werkboektab Bewijsplan.', 28),
    '''[2 min · deel 7 · 2:54] Zeg: "Het concept van K2, K3 en K4 op zondag 24 januari is optioneel, maar wie het instuurt, krijgt op maandag 25 januari feedforward. Dat is de laatste feedback vóór Assessment 1." Loop rond en kijk of elke regel een naam heeft. Wijs op kennispakket 1: daar staan de werkinstructies voor K2 tot en met K4 en practicum 4. Overgang: exit ticket.''', part=7)

D.frame('exit', K('Exit ticket · 4 minuten · ICT A-ET Exit ticket college 2', dark=True) +
    UL(['Welk getal stuurt onze oplossing, en hoe kan het dat op de verkeerde manier halen?', 'Vult onze oplossing werk aan, of neemt ze het over? Waaraan zie je dat?', 'Welk standpunt veranderde vandaag, en waardoor?',
        'Bonus: welke vraag had jij nog aan de gastspreker?'], 33, ON_NAVY, ordered=True) +
    f'<div style="background:#0B2A6B;border-radius:14px;padding:24px 32px">{P("**Zondag 24 januari, 23:59:** concept K2, K3 en K4 bij ICT A-ET Concept K2-K4 (optioneel, sterk aanbevolen). Feedforward op maandag 25 januari.", 28, ON_NAVY)}</div>' +
    D.statement('Een systeem haalt wat je meet, niet wat je bedoelt. En wie de winst krijgt, is een keuze.', dark=True, size=36),
    '''[4 min · deel 7 · 2:56] Individueel, via de MyCampus-opdracht ICT A-ET Exit ticket college 2. Sluit af met de kernboodschap. Na het college: lees de antwoorden en stuur waar nodig binnen een week een kort bericht per groep; noteer de tellingen van het debat. Gebruik de antwoorden ook bij de feedforward op 25 januari.''', dark=True, part=7)

D.frame('bronnen', H('Bronnen') + UL([
    'Buolamwini, J. & Gebru, T. (2018). Gender Shades. Proceedings of Machine Learning Research 81, 77–91.',
    'Buolamwini, J. (2016). How I’m fighting bias in algorithms. TEDxBeaconStreet. ted.com',
    'Amnesty International (25 oktober 2021). Xenophobic Machines. amnesty.org, EUR 35/4686/2021.',
    'Grondwet van de Republiek Suriname, artikel 8 en 17.',
    'Ontwerpwet Bescherming Privacy en Persoonsgegevens (De Nationale Assemblée, dna.sr).',
    'NIST (2022). SP 1270, Towards a Standard for Identifying and Managing Bias in AI.',
    'Verordening (EU) 2024/1689 (AI-verordening), art. 10, 14 lid 4 onder b, 27.',
    'NIST AI RMF 1.0 (2023), GOVERN 2.1, MAP 4.1; ISO/IEC 42001:2023, 6.1.4; ISO/IEC 42005:2025.',
    'Moffatt v. Air Canada, 2024 BCCRT 149 (kennispakket 1).',
    'Suriname Herald (26 maart 2025 en 19 februari 2026), Waterkant (19 februari 2026): deepfakevideo’s.',
    'Dagblad Suriname (4 juli 2025). Van uittreksel tot rijbewijs: hoe veilig zijn onze digitale gegevens.',
    'Mendelow, A. (1991). Stakeholder mapping (macht-belangschema), basis voor de 2x2 in K2.'], 21),
    '''[niet tonen tenzij gevraagd] Bronnen bij deel 1 tot en met 3 en 7. De bronnen van deel 4 en 5 staan op de volgende dia.''')

D.frame('bronnen-2', H('Bronnen bij veiligheid en werk') + UL([
    'Wiener, N. (1960). Some Moral and Technical Consequences of Automation. Science 131. · Goodhart (1975); Strathern, M. (1997).',
    'Bostrom, N. (2003). Ethical Issues in Advanced Artificial Intelligence. · Omohundro, S. (2008). The Basic AI Drives.',
    'Amodei, D. e.a. (2016). Concrete Problems in AI Safety. · OpenAI (21 december 2016). Faulty Reward Functions in the Wild.',
    'Krakovna, V. e.a. (2020). Specification gaming: the flip side of AI ingenuity. DeepMind. · OpenAI (2025). Detecting misbehavior in frontier reasoning models.',
    'Zwetsloot, R. & Dafoe, A. (2019). Thinking About Risks From AI: Accidents, Misuse and Structure. Lawfare. · International AI Safety Report (2025).',
    'Eykholt, K. e.a. (2018). Robust Physical-World Attacks on Deep Learning Visual Classification. CVPR. · Zech, J. e.a. (2018). PLOS Medicine.',
    'The Wall Street Journal (15 september 2021). The Facebook Files. · OpenAI (29 april 2025). Sycophancy in GPT-4o.',
    'Christiano, P. e.a. (2017); Ouyang, L. e.a. (2022). Leren van menselijke voorkeuren (RLHF).',
    'Keynes (1930); Autor, Levy & Murnane (2003); Frey & Osborne (2013/2017); Acemoglu & Johnson (2023). Power and Progress.',
    'IMF (januari 2024), Gen-AI and the Future of Work; ILO Working Paper 96 (2023); ILO & Wereldbank (2024), Buffer or Bottleneck?',
    'Mata v. Avianca (S.D.N.Y., 22 juni 2023). · Post Office Horizon IT Inquiry (VK). · TIME (18 januari 2023), Billy Perrigo.',
    'Suriname: Suriname Herald (26 maart, 10 april en 8 mei 2025; 19 februari 2026), deepfakes; Dagblad Suriname (24 juli 2025; 19 oktober 2026), callcenters; DSB, jaarverslag 2025; Suriname Herald (15 januari 2025; 23 september, 2 oktober, 20 oktober en 12 november 2026); UNESCO (2026), RAM 2.0 in Suriname.'], 20),
    '''[niet tonen tenzij gevraagd] Bronnen bij de dia's. Controleer de TED-link en het nieuws over de ontwerpwet vlak voor het college.''')

D.frame('docent-voorbereiding', K('Docent · niet tonen') + H('Voorbereiding college 2') + G([
    UL(['Aantallen practicum 1 per model op “fout-erger”', 'Top 3 uit de exit tickets van college 1 op “exit-tickets”', 'Naam, functie, organisatie gastspreker (cover, welkom)',
        'Volgorde groepen en kern van hun vraag op “vragen”', 'Stelling 2 kiezen uit de inzendingen'], 26),
    UL(['Twee studenten voor stelling 1 (bank en AI-assistent) vooraf vragen', 'Stoelen in twee rijen met een middenvak; aantekenkaarten printen', 'QR-codes testen (deepfake, WSJ, OpenAI, Avianca, IMF); CoastRunners-video klaarzetten; reserve bij afzegging gastspreker: TED-talk Buolamwini',
        'Nieuws ontwerpwet privacy checken; tijd, lokaal, pauze invullen', 'Inleverpunten Exit ticket college 2 en Concept K2-K4 open; ACLU-link testen'], 26)], 2, 40),
    '''Deze dia staat achteraan en wordt niet getoond of gedeeld. Na het college: exit tickets lezen, debattellingen noteren. Concepten K2-K4 (zondag 24 januari) nakijken met de checklists en de kwaliteitslat; feedforward op maandag 25 januari.''')

if __name__ == '__main__':
    src, out = sys.argv[1], sys.argv[2]
    sections = {
        's1': {'description': 'Deel 1. Rolwissel, lesroute en terugblik: welke fout is erger?', 'start': 'cover'},
        's2': {'description': 'Deel 2. Gastcollege met aantekenkaart', 'start': 'welkom'},
        's3': {'description': 'Deel 3. Vraaggesprek en pauze', 'start': 'vragen'},
        's4': {'description': 'Deel 4. Veiligheid en alignment: begrippen en herkomst, drie risico\'s, robuustheid, alignment en Goodhart, specification gaming, paperclip, RLHF, wat helpt', 'start': 'veilig-wat'},
        's5': {'description': 'Deel 5. Werk, autonomie en economie: begrippen en herkomst, automatisering, tweede kring, cijfers, augmentatie en delegatie, menselijke controle, verantwoording, ongelijkheid', 'start': 'werk-wat'},
        's6': {'description': 'Deel 6. Lagerhuisdebat over twee stellingen', 'start': 'debat-regels'},
        's7': {'description': 'Deel 7. Jullie casus: vijf vragen, K2 en K3, ruil, plan tot 24 januari, exit ticket, bronnen', 'start': 'onderzoeksvragen'},
    }
    idx = D.write(out, src + '/project/deck.json', 'College 2 AI & Ethics: Waar gaat het mis, en wie is verantwoordelijk?', sections, {})
    print(len(idx['order']), "dia's")
