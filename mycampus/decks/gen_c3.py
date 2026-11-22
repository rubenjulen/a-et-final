#!/usr/bin/env python3
"""Online sessie 1 (week 3, do 21 januari 2027, 60 min): wat lieten de practica zien?

Gebruik:  python3 gen_c3.py <map met gelezen project/deck.json> <uitvoermap>
Publiceren naar https://claude.ai/artifact/LyCGu8Fo2L4EaKVYFR45VF met root = <uitvoermap>.
"""
import sys
from janssen_slides import *

LOGO = '/_blob/b271f5a068421544537788d0eade95b6'
PARTS = ['Stelling', 'Wat lieten de practica zien?', 'Jullie oplossing', 'Afsluiting']
D = Deck(LOGO, 'ICT A-ET · College 3 · online sessie 1 · donderdag 21 januari 2027', PARTS)
K, H, P, UL, C, R, G = D.kicker, D.h2, D.p, D.ul, D.card, D.row, D.grid
KUST, BINNEN = BLUE_T, GOLD

D.frame('cover', f'''
<div style="display:flex;justify-content:space-between;align-items:flex-start">
<img src="{LOGO}" alt="Janssen University of Applied Sciences" style="width:620px;height:72px;object-fit:contain;object-position:left">
<p style="font-size:26px;font-weight:700;color:{BLUE_T};letter-spacing:2px;text-transform:uppercase;text-align:right">Minor AI · ICT A-ET</p>
</div>
<div style="flex:1;display:flex;flex-direction:column;justify-content:center;gap:28px">
<p style="font-size:30px;font-weight:700;color:{BLUE_T};letter-spacing:3px;text-transform:uppercase">AI &amp; Ethics · online sessie 1 · week 3</p>
<h1 style="font-size:112px;font-weight:700;line-height:1.02;color:{NAVY};text-transform:uppercase">Eerlijk voor wie?</h1>
<div style="width:240px;height:10px;background:{BLUE};border-radius:5px"></div>
</div>
<div style="background:{NAVY};border-radius:14px;padding:28px 40px;display:flex;justify-content:space-between">
<p style="font-size:30px;color:{ON_NAVY}">Donderdag 21 januari 2027 · [tijd] · online, 60 minuten</p>
<p style="font-size:30px;color:{GOLD};font-weight:700">Wordt opgenomen · camera optioneel</p>
</div>''', '''[0:00] Zet de opname aan en zeg dat de camera optioneel is. Zeg: "Welkom bij de eerste online sessie. Vandaag kijken we niet hoe vaak een model zich vergist, maar bij wie." Docentvoorbereiding: zie de laatste dia.''', footer=False, pad='96px 128px')

D.frame('vandaag', K('Waar staan we') + H('Vandaag meet je voor wie het misgaat') +
    P('**Route:** K4 snelle scan (zo 24/1) → K4 diep, K5, K6 (week 4) → Assessment 1 (do 4/2). Aan het einde van vandaag kun je uitleggen waarom een goed gemiddelde fouten per groep verbergt, en domein 5 en 7 van jullie oplossing scoren met bewijs.', 28) +
    D.table(['Deel', 'Opbrengst', 'Tijd'], [['1 · Stelling', 'Je standpunt, getoetst', '0:00–0:10'], ['2 · Practica', 'Eén inzicht in de chat', '0:10–0:25'],
                                         ['3 · Jullie oplossing', 'Score 5 en 7 met bron in K4_Scan', '0:25–0:48'], ['4 · Afsluiting', 'Exit ticket', '0:48–1:00']], 25, ['34%', '46%', '20%']) +
    f'<div style="background:{ICE};border-left:8px solid {BLUE};border-radius:12px;padding:18px 28px">{P("**Eindresultaat vandaag:** domein 5 en 7 staan met een score en een bron in het tabblad K4_Scan.", 28, NAVY)}</div>',
    '''[2 min · deel 1 · 0:01] Zeg: "Tot nu toe beschreven jullie de oplossing. Vandaag wordt het meten: voor wie gaat het mis?" Wijs op de route en de datum van A1. Lees het eindresultaat voor; daar komen we om 0:48 op terug. Overgang: "Eerst de stelling."''', part=1)

D.frame('stelling', K('Stelling van de week · 8 minuten', dark=True) +
    f'<h1 style="font-size:72px;font-weight:700;line-height:1.15;color:{ON_NAVY}">“Een bank mag een model gebruiken dat nauwkeuriger is dan medewerkers, ook als het één groep vaker onterecht afwijst.”</h1>' +
    R(C('Voor · 2 min', 'Eén student verdedigt, met bronnen.', dark=True, size=28), C('Tegen · 2 min', 'Eén student bestrijdt, met bronnen.', dark=True, size=28),
      C('Iedereen · 4 min', 'Kies eerst in de chat: eens, oneens of twijfel. Daarna: wie kiest iets anders?', dark=True, size=28)),
    '''[8 min · deel 1 · 0:02] De eerste keer van de debatlijn online. Vraag de twee studenten die je vooraf hebt gevraagd: eerst verdedigen, dan bestrijden, elk twee minuten. Zet daarna de peiling in de chat (eens / oneens / twijfel) en noteer de stand. Lees twee reacties voor, één van elke kant. Vraag: "Wie koos iets anders dan de meerderheid? Waarom?" Kom terug op de stelling na de dia over nauwkeurigheid: met versie B is het model voor het binnenland nauwkeuriger (66,0% tegen 61,5%), en toch wijst het 64,3% van de goede betalers daar af. Vraag dan: is iemand van kant gewisseld?''', dark=True, part=1)

D.frame('peiling', K('In de chat · 1 minuut') + f'<h1 style="font-size:80px;font-weight:700;line-height:1.1;color:{NAVY}">Heb je practicum 2 en 3 af? Typ ja, bijna of nee.</h1>' +
    P('En in één zin: wat verraste je het meest?', 36, BLUE_T, 700),
    '''[1 min · deel 2 · 0:10] Lees een paar antwoorden voor. Verwacht: in practicum 2 de sprong naar 64,3% onterecht afgewezen in het binnenland; in practicum 3 dat de lange boom (63,1% goed) slechter scoort dan de korte boom (67,9%) en bij TB0046 100% zeker ja zegt (korte boom 67%, regressie 41%; de aanvrager betaalde terug). Wie practicum 2 nog niet af heeft: maak het toch, de evidence cards vragen je eigen getallen. Noteer wie "nee" typt.''', part=2)

def staaf(v, h, col, lab):
    return (f'<div style="display:flex;flex-direction:column;gap:8px;align-items:center"><p style="font-size:30px;font-weight:700;color:{NAVY}">{v}</p>'
            f'<div style="width:150px;height:{h}px;background:{col};border-radius:8px 8px 0 0"></div></div>')
groep = lambda a, b, t: (f'<div style="display:flex;flex-direction:column;gap:14px;align-items:center"><div style="display:flex;gap:16px;align-items:end">{staaf(*a)}{staaf(*b)}</div>'
                         f'<p style="font-size:28px;font-weight:700;color:{NAVY}">{t}</p></div>')
D.frame('grafiek', H('Goede betalers die onterecht zijn afgewezen') +
    f'<div style="display:flex;gap:40px;align-items:center"><div style="display:flex;gap:12px;align-items:center"><div style="width:32px;height:32px;background:{KUST};border-radius:6px"></div>{P("Kust", 26)}</div>'
    f'<div style="display:flex;gap:12px;align-items:center"><div style="width:32px;height:32px;background:{BINNEN};border-radius:6px"></div>{P("Binnenland", 26)}</div>{P("Testset, logistische regressie, Orange 3.40", 26, MUTED)}</div>' +
    f'<div style="display:flex;gap:110px;align-items:end;justify-content:center;flex:1">'
    f'{groep(("12,8%", 90, KUST, ""), ("23,4%", 164, BINNEN, ""), "Versie A")}'
    f'{groep(("11,1%", 78, KUST, ""), ("64,3%", 420, BINNEN, ""), "Versie B: scheve labels")}'
    f'{groep(("14,8%", 104, KUST, ""), ("33,3%", 233, BINNEN, ""), "B zonder gevoelige kenmerken")}</div>',
    '''[5 min · deel 2 · 0:11] De belangrijkste dia. Zeg: "Met versie A worden goede betalers uit het binnenland al bijna twee keer zo vaak afgewezen als aan de kust: 23 tegenover 13 procent. Met versie B, de data met de scheve historische labels uit Albina, schiet dat naar 64 procent: bijna twee op de drie goede betalers in het binnenland krijgen geen lening. Aan de kust verandert bijna niets." Laat de derde groep nog liggen. Getallen uit het antwoordmodel; wijken de weekcheckgetallen af, noem dan die van de groep. Zeg: "Gebruik in je evidence card je eigen getallen." Overgang: "Dan een vreemde vraag."''', part=2)

D.frame('nauwkeurigheid', K('Kies eerst · typ A, B of C in de chat', dark=True) +
    f'<h2 style="font-size:56px;font-weight:700;line-height:1.15;color:{ON_NAVY}">In versie B werden meer goede betalers afgewezen. Toch steeg de nauwkeurigheid voor het binnenland. Hoe kan dat?</h2>' +
    R(C('Binnenland, versie A', f'<p style="font-size:96px;font-weight:700;color:{ON_NAVY};line-height:1">61,5%</p>{P("goed voorspeld · 61,3% goedgekeurd", 26, ON_NAVY_MUTED)}', dark=True),
      C('Binnenland, versie B', f'<p style="font-size:96px;font-weight:700;color:{GOLD};line-height:1">66,0%</p>{P("goed voorspeld · 21,7% goedgekeurd", 26, ON_NAVY_MUTED)}', dark=True)) +
    P('A · het model werd beter   ·   B · er wordt vaker afgewezen, en afwijzen is vaak goed   ·   C · de meting klopt niet', 28, ON_NAVY),
    '''[3 min · deel 2 · 0:16] Iedereen typt eerst A, B of C. Vraag: "Wie koos iets anders dan B? Verdedig het in één zin." Vat samen: in het binnenland betaalt in deze data minder dan de helft terug. Wie vaker afwijst, heeft dan vaker gelijk. De bank ziet minder onterechte goedkeuringen, de goede betalers betalen de prijs. Een hogere nauwkeurigheid kan samengaan met meer onrecht. Terug naar de stelling: is iemand van kant gewisseld?''', dark=True, part=2)

D.frame('verkapt', H('Gevoelige kenmerken weglaten halveert het probleem, maar lost het niet op') + R(
    C('Binnenland, versie B', f'<p style="font-size:88px;font-weight:700;color:{RED};line-height:1">64,3%</p>{P("onterecht afgewezen", 26)}', accent=RED),
    C('Zonder geslacht, district, regio', f'<p style="font-size:88px;font-weight:700;color:{RED};line-height:1">33,3%</p>{P("onterecht afgewezen", 26)}', accent=RED),
    C('Ter vergelijking: de kust', f'<p style="font-size:88px;font-weight:700;color:{BLUE_T};line-height:1">14,8%</p>{P("onterecht afgewezen", 26)}')) +
    P('Inkomen en soort werk hangen samen met waar iemand woont: ze werken als **proxy**. En de labels blijven scheef.', 30) +
    D.statement('Een organisatie die alleen de totale nauwkeurigheid meet, ziet dit nooit. Kijk daarom bij domein 5 en 11: wordt er per groep gemeten?', size=32),
    '''[3 min · deel 2 · 0:19] Zeg: "Veel van jullie verwachtten dat het probleem weg is als je de gevoelige kolommen weghaalt. Het verschil wordt kleiner, maar blijft meer dan twee keer zo groot." Het model herkent het binnenland via inkomen en informeel werk (proxy), en de labels blijven fout: het probleem moet bij de data worden opgelost. Wie geslacht weglaat, kan niet meer testen of het model op geslacht verschilt (AI-verordening art. 10 lid 5 staat daarom gebruik van gevoelige gegevens toe om bias op te sporen). Vraag: "Wie weet al of hun organisatie fouten per groep meet?" Meestal niemand: dat is bewijs dat ze nog moeten zoeken.''', part=2)

D.frame('genai', K('Bij een chatbot of agent') + H('Dezelfde vraag: voor wie gaat het mis?') + G([
    C(None, f'<p style="font-size:32px;font-weight:700;color:{RED}">{i}</p>{P(t, 29, NAVY, 700)}') for i, t in enumerate(
        ['Kan het overtuigend fout zijn?', 'Waar gaan de gegevens naartoe?', 'Weet de gebruiker dat het AI is?', 'Helpt het iedereen even goed, ook met een andere naam, in een andere taal of via een spraakbericht?'], 1)], 2, 22) +
    P('Een chatbot heeft geen afwijzingspercentage, maar wel groepen voor wie het slechter werkt.', 28, MUTED),
    '''[2 min · deel 2 · 0:22] Vraag in de chat welke groepen een chatbot of agent bouwen. De les van de grafiek geldt ook daar: een goed gemiddelde kan verbergen dat het voor één groep slechter werkt, bijvoorbeeld voor wie een naam heeft die het model minder vaak zag, informeel typt, of een spraakbericht in het Sranantongo stuurt. Voorbeeld uit de studentversie: AI-detectoren markeerden meer dan de helft van de essays van niet-moedertaalsprekers ten onrechte als AI-tekst (Liang e.a., 2023). Vraag 1 en 3 komen terug in practicum 4.''', part=2)

D.frame('ieee', K('IEEE CertifAIEd · kaderclip B') + H('Wat helpt, en wat werkt tegen?') + R(
    C('Drivers: dit helpt', UL(['De gebruiker weet meteen dat het AI is', 'De gebruiker kan ingrijpen of een alternatief kiezen', 'Het gedrag per groep wordt gevolgd en bias gecorrigeerd'], 27), accent=GREEN),
    C('Inhibitors: dit werkt tegen', UL(['Gedrag verhullen of mensen manipuleren', 'Angst voor aansprakelijkheid, of een bedrijfsgeheim beschermen', 'Een proces zo ondoorzichtig dat niemand bias kan meten'], 27), accent=RED)) +
    P('CertifAIEd scoort van 1 tot 5, jullie snelle scan van 0 tot 3. Het principe is hetzelfde: **geen score zonder bewijs**.', 28),
    '''[1 min · deel 2 · 0:24] Alleen de kern; kaderclip B gaat dieper. Zeg: "Inhibitors zijn vaak begrijpelijke redenen, geen kwade wil." Vraag: "Welke inhibitor herkennen jullie bij jullie partner of een leverancier?" Laat dat in het groepswerk terugkomen bij domein 6. Overgang naar deel 3.''', part=2)

niv = lambda lab, col, t, fc='#FFFFFF': (f'<div style="display:flex;border:1px solid {LINE};border-radius:14px;overflow:hidden">'
    f'<p style="width:250px;flex:none;background:{col};color:{fc};font-size:30px;font-weight:700;padding:22px 28px">{lab}</p>'
    f'<p style="flex:1;background:{CARD};font-size:28px;line-height:1.35;color:{INK};padding:22px 30px">{e(t)}</p></div>')
D.frame('niveaus', H('Eén score op drie niveaus') + niv('Zwak', RED, 'Fairness: 2, het model is eerlijk.') +
    niv('Redelijk', GOLD, 'Fairness: 1, er wordt niet per groep gemeten (interview teamleider).', NAVY) +
    niv('Professioneel', GREEN, 'Fairness: 1. Er wordt alleen de totale nauwkeurigheid gemeten (interview teamleider, 12 januari; geen rapportage per groep gevonden). Bewijs nodig: afwijzingen per regio uit A-AI2.') +
    P('Basis = score + bron · Goed = + sterkte van het bewijs · Sterk = + wat nog ontbreekt en bij wie je het haalt', 28, NAVY, 700),
    '''[2 min · deel 3 · 0:25] Vraag: "Welke schakel ontbreekt in de zwakke versie?" Verwacht: de bron, en dat 2 zonder bewijs niet kan. Laat één student de bron in de professionele versie aanwijzen. Zeg: "Zo wil ik domein 5 en 7 straks in jullie K4_Scan zien."''', part=3)

D.frame('groepswerk', D.werkblok('21 min', 'Groep, in een aparte kamer') + H('Wie draagt de fouten in jullie oplossing?') +
    UL(['Welke gebruikers of betrokkenen lopen het risico dat de fouten bij hen terechtkomen?', 'Hoe zou je dat kunnen meten of testen?', 'Welke score krijgen domein 5 en 7 nu, en waarop baseren jullie die?'], 30, ordered=True) +
    D.klaar('domein 5 en 7 hebben in het tabblad K4_Scan een score (0–3 of onbekend) én een bron, of “bewijs nodig: …”.', 28) +
    P('**Nu verwerken, niet later:** één persoon deelt het werkboek en vult K4_Scan direct in. Chatbot of agent? Neem bij vraag 1 de vier vragen mee.', 27),
    '''[21 min · deel 3 · 0:27] Zet de groepen in aparte kamers en bezoek elke kamer kort, ongeveer 3 minuten. Luister vooral naar vraag 3: bewijs of gevoel? Vraag: "Welk document of gesprek laat dat zien?" Wie geen bron heeft, schrijft "onbekend" met wat ze zoeken. Vraag 2 is de opstap naar practicum 4: wat zouden jullie testen? Groepen met Suribank: de verwachte scores staan in het docentmateriaal van week 2; geef ze niet, vraag naar het bewijs. Haal iedereen om 0:48 terug.''', part=3)

D.frame('schaal', H('De snelle scan: een score zonder bewijs telt niet') + D.table(
    ['Score', 'Betekenis', 'Herken je aan'],
    [['0', 'Niet aanwezig of onbekend', 'Niemand weet ervan, of er is geen enkel spoor van'], ['1', 'Ad hoc', 'Er gebeurt iets, maar informeel en afhankelijk van personen'],
     ['2', 'Gedeeltelijk beheerst', 'Er zijn afspraken, maar uitvoering of bewijs is onvolledig'], ['3', 'Aantoonbaar beheerst', 'Beleid of proces, duidelijke rollen, uitvoering aantoonbaar en gecontroleerd']], 27, ['12%', '30%', '58%']) +
    P('Weet je het nog niet? Schrijf “onbekend” en noteer welk bewijs je zoekt. Kies daarna 4 tot 6 domeinen voor week 4; bij beslissingen over mensen altijd 5 en 7.', 27),
    '''[3 min · deel 4 · 0:48] Zeg: "De score zegt hoe aantoonbaar iets geregeld is, niet hoe goed de bedoelingen zijn. Een 2 vraagt afspraken én gedeeltelijk bewijs." Vraag één groep: "Welke score gaven jullie domein 7, en waarom?"''', part=4)

D.frame('deze-week', H('Deze week nog') + D.table(
    ['Wanneer', 'Wat', 'Waar'],
    [['zo 24 januari, 23:59', 'Evidence card 2 en 3 in één pdf (individueel)', 'ICT A-ET Evidence cards week 3'],
     ['zo 24 januari, 23:59', 'K4 snelle scan in het werkboek, met AI-verklaring (groep)', 'ICT A-ET Rapportstuk week 3'],
     ['ma 25 januari', 'Laatste dag om van casus te wisselen', 'Bij de docent'],
     ['do 28 januari', 'Online sessie 2: van dilemma naar risico', 'Online']], 27, ['24%', '46%', '30%']) +
    P('Volgende week: practicum 4. Jullie testen je eigen oplossing met een vaste testset, en doen in week 9 precies dezelfde test opnieuw.', 28, NAVY, 700),
    '''[2 min · deel 4 · 0:51] Kondig practicum 4 kort aan: chatbots en agents krijgen een testset van minstens 30 vragen, voorspellende modellen een gepaarde test. Vraag in de chat of het gesprek met de partner uit A-AI2 gepland staat. Groepen die vastlopen, kunnen tot maandag 25 januari overstappen.''', part=4)

D.frame('exit', K('Exit ticket · 4 minuten · ICT A-ET Exit ticket college 3', dark=True) +
    UL(['Welk getal uit practicum 2 onthoud je, en waarom?', 'Voor wie in jullie oplossing kan het misgaan?', 'Welk bewijs zoeken jullie deze week, en bij wie?', 'Bonus: ben je van standpunt veranderd over de stelling?'], 34, ON_NAVY, ordered=True) +
    D.statement('Een goed gemiddelde zegt niets over wie de fouten draagt.', dark=True, size=44),
    '''[4 min · deel 4 · 0:53] Zet de link naar de MyCampus-opdracht ICT A-ET Exit ticket college 3 in de chat. Zeg: "Vul hem in voordat je de sessie verlaat." Lees er twee voor als er tijd is. Daarna open vragen tot het einde van het uur. Na afloop: opname binnen 24 uur in de leeromgeving; gebruik de exit tickets in het feedforward-bericht van maandag 25 januari.''', dark=True, part=4)

D.frame('bronnen', H('Bronnen') + UL([
    'Rudin, C. (2019). Stop explaining black box machine learning models for high stakes decisions. Nature Machine Intelligence 1, 206–215. doi.org/10.1038/s42256-019-0048-x',
    'Buolamwini, J. & Gebru, T. (2018). Gender Shades. PMLR 81, 77–91.',
    'Kleinberg, J., Mullainathan, S. & Raghavan, M. (2016). Inherent Trade-Offs in the Fair Determination of Risk Scores. arXiv 1609.05807.',
    'Chouldechova, A. (2017). Fair prediction with disparate impact. Big Data 5(2).',
    'Liang, W. e.a. (2023). GPT detectors are biased against non-native English writers. Patterns. arXiv 2304.02819.',
    'NYDFS (maart 2021). Report on Apple Card Investigation; Banking Dive, Goldman cleared of bias claims.',
    'IEEE CertifAIEd, ontologieën Transparency en Algorithmic Bias.',
    'NIST AI 600-1 (2024), Generative AI Profile; NIST AI RMF 1.0, MEASURE 2.9 en 2.11.',
    'Verordening (EU) 2024/1689, art. 10, 13, 50 en 86.',
    'Practicum 2 en 3: Suribank-oefendata (fictief), Orange 3.40, standaardinstellingen.'], 25),
    '''[niet tonen tenzij gevraagd] Bronnen bij de dia's en de studentversie van week 3.''')

D.frame('docent-voorbereiding', K('Docent · niet tonen') + H('Voorbereiding online sessie 1') + G([
    UL(['Twee studenten voor de stelling gevraagd (voor en tegen)', 'Getallen uit weekcheck 3 verzameld; vergelijk met de grafiek', 'Breakout-kamers per groep klaargezet', 'Opname aan; link in de agenda en op MyCampus'], 26),
    UL(['Peiling in de chat voorbereid (eens / oneens / twijfel)', 'Link naar ICT A-ET Exit ticket college 3 klaar om te plakken', 'Inleverpunten Evidence cards week 3 en Rapportstuk week 3 open', 'Na afloop: opname binnen 24 uur online'], 26)], 2, 40),
    '''Deze dia staat achteraan en wordt niet getoond of gedeeld. Deel de pdf van de dia's pas na zondag 24 januari 23:59: de grafiek toont de uitkomsten van practicum 2.''')

if __name__ == '__main__':
    src, out = sys.argv[1], sys.argv[2]
    sections = {
        's1': {'description': 'Deel 1. Waar staan we, en de stelling van de week', 'start': 'cover'},
        's2': {'description': 'Deel 2. Wat lieten de practica zien? Fouten per groep, proxy, generatieve AI, CertifAIEd', 'start': 'peiling'},
        's3': {'description': 'Deel 3. Jullie oplossing: domein 5 en 7 scoren met bewijs', 'start': 'niveaus'},
        's4': {'description': 'Deel 4. Schaal, deze week, exit ticket, bronnen', 'start': 'schaal'},
    }
    idx = D.write(out, src + '/project/deck.json', 'College 3 (online sessie 1) AI & Ethics: Eerlijk voor wie?', sections, {})
    print(len(idx['order']), "dia's")
