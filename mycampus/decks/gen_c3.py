#!/usr/bin/env python3
"""College 3 (blok 2, do 25 februari 2027): Van analyse naar verantwoord ontwerp.

Feedback op Assessment 1, minicollege (verdieping op college 2: veiligheid en agents, macht en regelgeving, werk in het ontwerp,
professionele praktijk), Design Review en een plan naar Assessment 2. Janssen-huisstijl, deck-standaard.
Gebruik:  python3 gen_c3.py <map met gelezen project/deck.json> <uitvoermap>
Daarna publiceren naar https://claude.ai/artifact/LyCGu8Fo2L4EaKVYFR45VF met root = <uitvoermap>.
"""
import sys
from janssen_slides import *

LOGO = '/_blob/b271f5a068421544537788d0eade95b6'
PARTS = ['Feedback op A1', 'Minicollege', 'Design Review', 'Op weg naar A2', 'Afsluiting']
D = Deck(LOGO, 'ICT A-ET · College 3 · donderdag 25 februari 2027', PARTS)
K, H, P, UL, C, R, G = D.kicker, D.h2, D.p, D.ul, D.card, D.row, D.grid

URL_COAST = 'https://openai.com/index/faulty-reward-functions/'
URL_TIME = 'https://time.com/6247678/openai-chatgpt-kenya-workers/'

# ============ Cover ============
D.frame('cover', f'''
<div style="display:flex;justify-content:space-between;align-items:flex-start">
<img src="{LOGO}" alt="Janssen University of Applied Sciences" style="width:620px;height:72px;object-fit:contain;object-position:left">
<p style="font-size:26px;font-weight:700;color:{BLUE_T};letter-spacing:2px;text-transform:uppercase;text-align:right">Minor AI · ICT A-ET</p>
</div>
<div style="flex:1;display:flex;flex-direction:column;justify-content:center;gap:28px">
<p style="font-size:30px;font-weight:700;color:{BLUE_T};letter-spacing:3px;text-transform:uppercase">AI &amp; Ethics · College 3</p>
<h1 style="font-size:112px;font-weight:700;line-height:1.02;color:{NAVY};text-transform:uppercase">Van analyse naar verantwoord ontwerp</h1>
<div style="width:240px;height:10px;background:{BLUE};border-radius:5px"></div>
</div>
<div style="background:{NAVY};border-radius:14px;padding:28px 40px;display:flex;justify-content:space-between">
<p style="font-size:30px;color:{ON_NAVY}">Donderdag 25 februari 2027 · [tijd] · lokaal [__]</p>
<p style="font-size:30px;color:{GOLD};font-weight:700">Panel: [docent] en [naam panel]</p>
</div>''', '''[1 min · opening · 0:00] Zeg: "Het laatste college. Vandaag drie dingen: wat jullie leren van de feedback op Assessment 1, wat er op het spel staat als een AI-oplossing echt wordt ingezet, en jullie ontwerp voor een panel. Jullie gaan naar huis met een plan naar 11 maart." Overgang: "Eerst: waar staan we?"''', footer=False, pad='96px 128px')

# ============ Deel 1. Feedback op A1 ============
reis = ''.join(
    f'<div style="flex:1;display:flex;flex-direction:column;gap:10px;align-items:center">'
    f'<div style="width:100%;height:14px;border-radius:7px;background:{GREEN if i < 2 else BLUE if i == 2 else LINE}"></div>'
    f'<p style="font-size:26px;font-weight:700;color:{GREEN if i < 2 else NAVY if i == 2 else MUTED}">{t}</p></div>'
    for i, t in enumerate(['Blok 1 · Analyseren ✓', 'A1 ✓', 'Blok 2 · Ontwerpen', 'Blok 3 · Verantwoorden', 'A2 · do 11 mrt']))
D.frame('vandaag', K('Rolwissel') + H('Vandaag word je ontwerper') +
    P('In blok 1 analyseerde je wat er mis kan gaan. In blok 2 ontwerp je wat het voorkomt. Vandaag toets je dat ontwerp, voordat het in het eindrapport staat.', 31) +
    f'<div style="display:flex;gap:10px">{reis}</div>' +
    UL(['Aan het einde van vandaag kun je de feedback op A1 vertalen naar besluiten in de verwerkingslijst;',
        'uitleggen wat er bij inzet op het spel staat: agents, macht, werk en professionele verantwoordelijkheid;',
        'jullie maatregelen verdedigen voor een panel, en feedback op andere ontwerpen geven.'], 29) +
    f'<div style="background:{ICE};border-left:8px solid {BLUE};border-radius:12px;padding:22px 32px">{P("**Eindresultaat vandaag:** een verwerkingslijst met besluiten, feedback van het panel op jullie ontwerp, en een plan met namen en data tot donderdag 11 maart.", 29, NAVY)}</div>',
    '''[2 min · deel 1 · 0:01] Zeg: "Vorige keer werd je onderzoeker. Vandaag word je ontwerper: je laat zien dat je maatregelen werken, en voor wie." Lees het eindresultaat voor. Overgang: "Zo ziet de middag eruit."''', part=1)

D.frame('route', K('Lesroute') + H('Vijf delen, elk met een opbrengst') + D.table(
    ['Deel', 'Centrale vraag', 'Opbrengst', 'Tijd'],
    [['1 · Feedback op A1', 'Wat leren we van Assessment 1?', 'Verwerkingslijst gestart', '0:00–0:25'],
     ['2 · Minicollege', 'Wat staat er bij inzet op het spel?', 'Eén aanvulling op jullie ontwerp', '0:25–1:10'],
     ['Pauze', '', '', '1:10–1:20'],
     ['3 · Design Review', 'Houdt jullie ontwerp stand?', 'Feedback van panel en groepen', '1:20–2:35'],
     ['4 · Op weg naar A2', 'Wat doen we tot 11 maart?', 'Plan met namen en data', '2:35–2:55'],
     ['5 · Afsluiting', 'Wat neem je mee?', 'Exit ticket', '2:55–3:00']], 27, ['24%', '38%', '26%', '12%']),
    '''[2 min · deel 1 · 0:03] Zeg: "De Design Review is het hart van vandaag. Het minicollege ervoor geeft jullie vragen die het panel ook kan stellen." Noem de volgorde van presenteren (staat sinds woensdag op MyCampus). Overgang: "Eerst terug naar het begin van de module."''', part=1)

stemkaart = lambda bg, lab, txt, fc, lc: (f'<div style="flex:1;background:{bg};border-radius:16px;padding:36px;display:flex;flex-direction:column;justify-content:space-between;gap:20px">'
                                         f'<p style="font-size:24px;font-weight:700;color:{lc};text-transform:uppercase;letter-spacing:1px">{lab}</p>'
                                         f'<p style="font-size:56px;font-weight:700;line-height:1.05;color:{fc}">{txt}</p></div>')
D.frame('stem-terug', K('Kies eerst · terug naar college 1') + H('Mag Suribank dit doen? En nu?') +
    P('Suribank wil leningen onder SRD 50.000 automatisch laten beslissen door een model dat aanvragers uit het binnenland vaker afwijst.', 30) +
    f'<div style="display:flex;gap:24px">{stemkaart(GREEN, "Groene kaart", "Ja", "#FFFFFF", "#DDF0E5")}{stemkaart(RED, "Rode kaart", "Nee", "#FFFFFF", "#F8DEDB")}{stemkaart(GOLD, "Gele kaart", "Onder voorwaarden", NAVY, NAVY)}</div>' +
    R(C(None, 'Telling college 1: groen [__] · rood [__] · geel [__]', size=27), C(None, 'Telling nu: groen [__] · rood [__] · geel [__]', size=27, accent=GOLD)),
    '''[4 min · deel 1 · 0:05] Werkvorm: 30 seconden zelf kiezen, dan tegelijk de kaart opsteken. Zet de telling van college 1 vooraf op de dia (uit je docentenmap). Vraag: "Wie koos anders dan op 7 januari? Waardoor?" Laat twee studenten antwoorden. Verwacht: meer geel, en scherpere voorwaarden (uitleg, menselijke beoordeling, meten per groep). Zeg: "Dat is precies wat er in jullie reflectie moet: welk standpunt veranderde, en waardoor." Overgang: "Nu de feedback op jullie eigen werk."''', part=1)

D.frame('feedback-patroon', K('Feedback op Assessment 1') + H('Wat ging goed, en waar ging het mis?') + R(
    C('Wat sterk was', UL(['[sterk punt 1, met een voorbeeld]', '[sterk punt 2]', '[sterk punt 3]'], 27), label='Bij de meeste groepen', accent=GREEN),
    C('Waar het misging', UL(['[verbeterpunt 1, met het criterium]', '[verbeterpunt 2]', '[verbeterpunt 3]'], 27), label='Bij de meeste groepen', accent=RED)) +
    P('Gemiddeld groepscijfer [__] · individueel deel [__] · spreiding [__] tot [__]', 27, MUTED),
    '''[5 min · deel 1 · 0:09] Vul vooraf in uit je beoordelingen (schriftelijke feedback is op donderdag 18 februari teruggegeven). Noem per punt een geanonimiseerd voorbeeld en het rubriccriterium. Veel voorkomende verbeterpunten die je kunt verwachten: risico's zonder oorzaak of zonder "voor wie" (criterium 4); scores zonder bron of zonder bewijssterkte (criterium 2); een voorlopig oordeel dat niet uit de analyse volgt (criterium 5); bij het canvas: lenzen als etiket (criterium D). Zeg: "Een onvoldoende voor A1 kun je compenseren: het tussenrapport komt herzien terug in Assessment 2." Overgang: "Waar breekt de redenering het vaakst?"''', part=1)

schakels = ['Bewijs', 'Gap', 'Risico', 'Eis', 'Maatregel', 'Eigenaar', 'Monitoring', 'Oordeel']
D.frame('keten-breuk', K('Redeneerketen-check') + H('Hier brak de keten het vaakst') +
    f'<div style="display:flex;gap:10px;align-items:stretch">' + ''.join(
        f'<div style="flex:1;background:{RED if t == "[breuk]" else (CARD if i < 3 else ICE)};border:1px solid {LINE};border-radius:12px;padding:22px 8px;display:flex;align-items:center;justify-content:center">'
        f'<p style="font-size:27px;font-weight:700;color:{NAVY if i < 3 else MUTED};text-align:center">{t}</p></div>'
        for i, t in enumerate(schakels)) + '</div>' +
    P('In A1 liep de keten van bewijs tot risico. Vanaf nu loopt hij door tot het oordeel. Een breuk is bijna altijd actiepunt 1.', 30) +
    D.statement('Volg één risico van bewijs tot oordeel. Waar je niet verder kunt, zit je volgende werk.', size=36),
    '''[3 min · deel 1 · 0:14] Wijs aan waar de keten in A1 het vaakst brak: meestal tussen gap en risico (een gap opgeschreven als risico) of tussen bewijs en gap (geen bron). Zeg: "In blok 2 en 3 komt de rest van de keten erbij: eis, maatregel, eigenaar, monitoring en oordeel. Elk risico uit jullie top 5 moet je kunnen volgen tot het beslismemo." Overgang: "Nu jullie eigen feedback."''', part=1)

D.frame('werkblok-feedback', D.werkblok('8 min', 'Groep') + H('Van feedback naar besluit') +
    UL(['Lees samen de kernboodschap en de actiepunten van jullie feedback op A1.', 'Zet elk actiepunt in de verwerkingslijst (werkboektab Verwerkingslijst).',
        'Besluit per punt: overgenomen, deels overgenomen of niet overgenomen, en schrijf waar of waarom.'], 30, ordered=True) +
    D.klaar('elk actiepunt uit de feedback staat in de verwerkingslijst, met een besluit en een eigenaar.', 28) +
    P('"Geen tijd" is geen argument. Niet overnemen mag, als je uitlegt waarom.', 28, MUTED),
    '''[8 min · deel 1 · 0:17] Loop rond, begin bij groepen met een lage score. Docentvraag: "Welk actiepunt verandert jullie oordeel het meest?" en "Wat nemen jullie bewust niet over, en waarom?" Herinner: zonder verwerkingslijst (bijlage E) kunnen criteria 1, 2 en 4 bij A2 niet hoger dan voldoende. Overgang: "Nu breder: wat staat er op het spel als een oplossing echt wordt ingezet?"''', part=1)

# ============ Deel 2. Minicollege ============
D.frame('veiligheid', K('Minicollege 1/4 · Veiligheid, verdieping op college 2') + H('Het getal, de bijwerking en de stopknop') + R(
    C('Het getal', 'Welk getal stuurt jullie oplossing? Jullie schreven het op in het exit ticket van college 2.', label='1 · Proxy', accent=BLUE),
    C('De bijwerking', 'Hoe kan het systeem dat getal halen zonder het doel te dienen? Welke test of welk signaal laat dat zien?', label='2 · Monitoren', accent=GOLD),
    C('De grens', 'Bij welke waarde stop je, of ga je terug naar handwerk? En wie beslist dat?', label='3 · Stopcriterium', accent=RED)) +
    D.statement('Een systeem haalt wat je meet, niet wat je bedoelt. Ontwerp dus ook wat je meet naast het doel.', size=36) +
    C(None, '**Kies eerst:** welke maatregel in jullie K7 voorkomt dat de oplossing haar doel op de verkeerde manier haalt? Is er al een?', size=28, bg=ICE),
    '''[6 min · deel 2 · 0:25] Zeg: "In college 2 zag je specification gaming en reward hacking: CoastRunners, de moderatie-AI die meer verwijdert, de taalmodellen die tests omzeilen. Nu de vertaling naar jullie ontwerp." Laat groepen hun getal uit het exit ticket van college 2 erbij pakken. Vraag de kies-eerst-vraag; duo's 1 minuut, dan twee groepen. Verwacht: een chatbot gemeten op afgehandelde gesprekken die te snel afkapt (maatregel: ook meten hoe vaak klanten terugkomen of klagen); een kredietmodel gemeten op terugbetaling dat het binnenland laat wegvallen (maatregel: goedkeuringen per regio volgen). Koppeling: dit wordt in blok 3 een ethisch signaal met grens, actie en eigenaar in H8. Overgang: "Het wordt spannender als AI niet alleen antwoordt, maar ook handelt."''', part=2)

D.frame('agents', K('Minicollege 1/4 · Veiligheid') + H('Als AI zelf handelt: agents') + R(
    C('Wat een agent doet', 'Plant stappen en voert ze uit met tools: mail versturen, een afspraak boeken, een dossier aanpassen, een andere agent aanroepen.', label='Nieuw', accent=BLUE),
    C('Wat er mis kan gaan', 'Een fout antwoord wordt een foute handeling. Rechten die te ruim zijn. Gegevens die via een tool naar buiten gaan. Niemand die het merkt.', label='Risico', accent=RED),
    C('Wat je ontwerpt', 'Zo weinig rechten als nodig. Een mens bij elke handeling die niet terug te draaien is. Alles loggen. Een stopknop met een eigenaar.', label='Maatregel', accent=GREEN)) +
    D.statement('Hoe meer een systeem zelf doet, hoe belangrijker het is wie het kan stoppen.', size=38) +
    P('**Nu jij:** welke handeling van jullie oplossing is niet terug te draaien, en wie keurt die goed?', 29, NAVY),
    '''[6 min · deel 2 · 0:31] Zeg: "Veel groepen bouwen in A-AI2 een agent, bijvoorbeeld in n8n of Copilot Studio. Dan is de vraag niet alleen of het antwoord klopt, maar ook wat het systeem daarna doet." Vraag de nu-jij-vraag aan drie groepen. Verwacht: een mail aan een klant, een wijziging in een dossier, een afspraak. Koppel aan de RACI (H7): wie mag stoppen, en aan de leverancierscheck: welke tool krijgt welke gegevens. Standaarden: AIGP (governance over de levenscyclus, kaderclip D); AI-verordening art. 14 (menselijk toezicht). Overgang: "Wie bepaalt eigenlijk de regels voor dit soort systemen?"''', part=2)

D.frame('macht', K('Minicollege 2/4 · Macht en regelgeving') + H('Wie bepaalt de regels?') + G([
    C('Een paar bedrijven', 'De grote taalmodellen komen van een handvol bedrijven. Wie daarop bouwt, hangt af van hun keuzes, prijzen en voorwaarden.', label='Macht', size=26, accent=RED),
    C('Internationaal', 'UNESCO-aanbeveling (2021), OECD-principes (2019, herzien 2024), en het AI-verdrag van de Raad van Europa (ter ondertekening sinds 5 september 2024).', label='Afspraken', size=26),
    C('De Europese Unie', 'De AI-verordening geldt in fasen. Na uitstel (Digital Omnibus, 2026) gelden de regels voor hoog risico, zoals krediet en werving, vanaf december 2027. De AI-melding bij chatbots geldt al.', label='Wet', size=26, accent=GOLD),
    C('Suriname', 'Nog geen AI-wet en geen privacywet in werking. Met UNESCO loopt sinds augustus 2026 de AI Readiness Assessment, als basis voor een nationale strategie.', label='Thuis', size=26, accent=GREEN)], 2, 22),
    '''[6 min · deel 2 · 0:37] Zeg: "Regels komen van drie kanten: internationale afspraken, wetten zoals de Europese AI-verordening, en de macht van de bedrijven die de modellen maken." Feiten: UNESCO Recommendation on the Ethics of AI (november 2021); OECD AI Principles (2019, herzien 2024); Raad van Europa, Framework Convention on Artificial Intelligence (CETS 225), aangenomen 17 mei 2024, ter ondertekening geopend op 5 september 2024 in Vilnius; volgens de Raad het eerste juridisch bindende internationale AI-verdrag. AI-verordening: volgens juridische commentaren is de Digital Omnibus on AI aangenomen als Verordening (EU) 2026/1744 (in werking eind juli 2026); hoog-risicosystemen uit bijlage III gaan van 2 augustus 2026 naar 2 december 2027; de transparantieplicht van art. 50 geldt vanaf 2 augustus 2026; de verboden en de plicht tot AI-geletterdheid golden al eerder. Controleer dit vlak voor het college op EUR-Lex. Suriname: RAM 2.0 met UNESCO, gestart 27 augustus 2026 (controleer het nieuws). Vraag: "Jullie partner gebruikt een taalmodel van een buitenlands bedrijf. Wie bepaalt wat dat model mag, en wat kan jullie partner zelf regelen?" Verwacht: contract, leverancierscheck, eigen beleidsregel. Overgang: "Regels gaan ook over wie er beter of slechter van wordt."''', part=2)

D.frame('werk', K('Minicollege 3/4 · Werk, verdieping op college 2') + H('Aanvullen, niet overlaten: werk in jullie ontwerp') + R(
    C('Augmentatie inbouwen', 'De medewerker kan het advies negeren of overrulen, heeft er tijd voor, en wordt niet afgerekend op afwijken. Afwijkingen worden geregistreerd.', label='1 · Menselijke controle', accent=GREEN),
    C('De tweede kring', 'Wie op het loket, het kantoor of de telefoon aangewezen is, houdt een andere weg: geen smartphone is geen reden om buiten te vallen.', label='2 · Toegang', accent=GOLD),
    C('Wie deelt in de winst?', 'Taken die verdwijnen: wat gebeurt er met de mensen? Omscholen, taken herverdelen, of eerlijk zeggen wat er verandert.', label='3 · Werk', accent=BLUE)) +
    D.statement('Of AI werk aanvult of overneemt, is een ontwerpkeuze. Leg die keuze vast, en laat zien wie hem maakte.', size=34) +
    P('**Kies eerst:** welke maatregel in jullie K7 zorgt dat de oplossing aanvult in plaats van overneemt?', 28, NAVY),
    '''[7 min · deel 2 · 0:43] Zeg: "In college 2 zag je hoe augmentatie ongemerkt delegatie wordt: door een zekere toon, tijdsdruk en een schuldcultuur. Ook de cijfers (IMF, ILO en Wereldbank) en de Surinaamse stemmen: callcenters onder druk, Finabank met een mens in het proces." Vraag de kies-eerst-vraag aan drie groepen. Verwacht: een werkinstructie die afwijken toestaat en registreert (de zes voorwaarden van college 2), een alternatief kanaal, een afspraak over taken van medewerkers. Koppeling: domein 10 (duurzaamheid en bredere impact) van de nulmeting, en de maatregelen in K7. Overgang: "Wat doe je als professional, als je ziet dat het misgaat?"''', part=2)

stap = lambda n, t, s: (f'<div style="flex:1;background:{CARD};border:1px solid {LINE};border-top:6px solid {BLUE};border-radius:12px;padding:22px 20px;display:flex;flex-direction:column;gap:8px">'
                        f'<p style="font-size:26px;font-weight:700;color:{BLUE_T}">{n}</p><h3 style="font-size:30px;font-weight:700;color:{NAVY}">{e(t)}</h3>{P(s, 24)}</div>')
D.frame('besluit', K('Minicollege 4/4 · Professionele praktijk') + H('Een ethisch besluit nemen in zes stappen') +
    f'<div style="display:flex;gap:14px">{stap("1", "Feiten", "Wat weten we, en wat niet?")}{stap("2", "Betrokkenen", "Wie raakt het, ook wie niet aan tafel zit?")}{stap("3", "Opties", "Minstens drie, waaronder een zonder AI.")}'
    f'{stap("4", "Lenzen", "Gevolgen, rechten, rechtvaardigheid, integriteit.")}{stap("5", "Besluit", "Wat kies je, wat geef je op?")}{stap("6", "Uitleg", "Kun je het uitleggen aan wie het raakt?")}</div>' +
    D.statement('Dit is je dilemma-canvas, in het klein. Een professional gebruikt het ook onder tijdsdruk.', size=36),
    '''[5 min · deel 2 · 0:50] Zeg: "Je kent deze stappen uit het dilemma-canvas. In de praktijk heb je geen 1.000 woorden en geen week. Dan helpt het om de zes stappen in je hoofd te hebben." Vergelijkbare stappenplannen: Markkula Center for Applied Ethics, A Framework for Ethical Decision Making; de beroepscode van de ACM (2018) vraagt om schade te voorkomen en om grondige evaluatie van systemen en hun risico's. Vraag: "Welke stap wordt in de praktijk het vaakst overgeslagen?" Verwacht: 2 (wie niet aan tafel zit) en 3 (de optie zonder AI). Overgang: "En als je besluit dat het niet deugt, maar je baas wil door?"''', part=2)

ladder = lambda n, t, s, col: (f'<div style="display:flex;border:1px solid {LINE};border-radius:12px;overflow:hidden">'
    f'<p style="width:90px;flex:none;background:{col};color:#FFFFFF;font-size:36px;font-weight:700;display:flex;align-items:center;justify-content:center">{n}</p>'
    f'<div style="flex:1;background:{CARD};padding:14px 24px"><p style="font-size:27px;font-weight:700;color:{NAVY}">{e(t)}</p>{P(s, 24)}</div></div>')
D.frame('aankaarten', K('Minicollege 4/4 · Professionele praktijk') + H('Wanneer kaart je iets aan, en bij wie?') + R(
    f'<div style="flex:1.3;display:flex;flex-direction:column;gap:10px">' +
    ladder('1', 'Bij het team', 'Benoem wat je ziet, met bewijs. Vaak is het een vergissing.', BLUE) +
    ladder('2', 'Bij de eigenaar', 'De A in de RACI, of je leidinggevende. Schriftelijk.', BLUE_T) +
    ladder('3', 'Bij compliance of een vertrouwenspersoon', 'Als het niet wordt opgepakt, of als het gevaarlijk is.', NAVY) +
    ladder('4', 'Buiten de organisatie', 'Toezichthouder of pers: alleen als binnen niets werkt, en als de schade groot is.', RED) + '</div>',
    C('Frances Haugen', 'Productmanager bij Facebook. Ze deelde in 2021 interne documenten en getuigde voor de Amerikaanse Senaat over de schade die het bedrijf kende maar niet aanpakte.', label='Voorbeeld', size=26, accent=GOLD)) +
    P('**Kies eerst:** je ontdekt na livegang dat jullie chatbot klanten verkeerd informeert over vergoedingen. Op welke trede begin je?', 28, NAVY),
    '''[5 min · deel 2 · 0:55] Zeg: "Aankaarten is een ladder. Je begint dichtbij, met bewijs, en je gaat pas een trede hoger als het niet werkt of als de schade groot is." Frances Haugen deelde in 2021 interne documenten van Facebook (onder meer met The Wall Street Journal) en getuigde op 5 oktober 2021 voor een subcommissie van de Amerikaanse Senaat. Gebruik haar als voorbeeld van trede 4, niet als norm. Vraag de kies-eerst-vraag. Verwacht: trede 1 of 2, met het testlogboek als bewijs; als de eigenaar niets doet en klanten schade lijden, trede 3. Koppeling: de incidentroute in H8 is precies deze ladder, maar dan vooraf afgesproken. Overgang: "Het beste is een organisatie waar je die ladder bijna nooit nodig hebt."''', part=2)

D.frame('cultuur', K('Minicollege 4/4 · Professionele praktijk') + H('Een ethische cultuur bouw je, je koopt hem niet') + G([
    C('Iemand is eigenaar', 'Precies één A per beslissing, en iemand die mag stoppen.', size=27),
    C('Afwijken is normaal', 'Medewerkers die afwijken van het advies, worden niet afgerekend. Afwijkingen worden geteld.', size=27),
    C('Een vaste regel', 'Een AI-beleidsregel die iedereen kent, en een vast moment om terug te kijken.', size=27),
    C('Melden is veilig', 'Een incidentroute, en wie meldt, wordt bedankt, niet gestraft.', size=27)], 2, 22) +
    P('Elk van deze vier zit al in jullie ontwerp: RACI (H7), menselijke controle (H7), beleidsregel (H7) en incidentroute (H8).', 28, MUTED),
    '''[4 min · deel 2 · 1:00] Zeg: "Een beleidsdocument maakt nog geen cultuur. Cultuur zie je aan wat er gebeurt als iemand afwijkt of een fout meldt." Koppeling met de zes voorwaarden voor menselijke controle (cultuur, registratie) uit college 2, en met ISO/IEC 42001 (rollen, competentie, verbetering; kaderclip E). Vraag: "Welke van de vier is bij jullie partner het zwakst?" Overgang: "Nu jullie ontwerp: wat moet erbij?"''', part=2)

D.frame('ontwerp-check', D.werkblok('6 min', 'Groep') + H('Wat betekent dit voor jullie ontwerp?') +
    UL(['Kies één thema uit het minicollege dat jullie ontwerp nog niet dekt: doel dat misgaat, agent die handelt, leverancier, werk, of aankaarten.',
        'Schrijf één eis of maatregel erbij, met een eigenaar.', 'Zet hem in H6 of H7, en in de verwerkingslijst met als bron "college 3".'], 30, ordered=True) +
    D.klaar('één nieuwe eis of maatregel met eigenaar, in het werkboek en in de verwerkingslijst.', 28),
    '''[6 min · deel 2 · 1:04] Loop rond. Docentvraag: "Wat doet jullie systeem als het doel en de bedoeling uit elkaar lopen?" en "Wie mag bij jullie stoppen?" Groepen die al alles dekken: laat ze het panel een vraag voorleggen in dia 8. Overgang: pauze; daarna de Design Review.''', part=2)

D.frame('pauze', f'<div style="flex:1;display:flex;flex-direction:column;justify-content:center;gap:28px"><h1 style="font-size:160px;font-weight:700;line-height:1;color:{ON_NAVY};text-transform:uppercase">Pauze</h1>{P("10 minuten · daarna de Design Review, om [__:__]", 44, GOLD, 700)}</div>',
    '''[10 min · pauze · 1:10] Vul de tijd in. Zet de laptop voor de eerste groep klaar; deel de feedbackkaarten uit.''', dark=True)

# ============ Deel 3. Design Review ============
D.frame('dr-opzet', K('Design Review · zo werkt het') + H('Houdt jullie ontwerp stand?') + R(
    C('8 minuten', 'Presentatie, hoogstens 8 dia’s. Iedereen in de groep is aan het woord.', label='Groep', accent=BLUE),
    C('3 minuten', 'Vragen van het panel, en één vraag uit de zaal.', label='Panel', accent=GOLD),
    C('Na afloop', 'Het panel scoort vier vragen van 0 tot 3 en geeft drie verbeterpunten.', label='Feedback', accent=GREEN)) +
    D.table(['De vier reviewvragen', 'Waar het panel naar kijkt'],
            [['Is elk groot risico gekoppeld aan een maatregel?', 'Van risico naar eis naar maatregel; voorkomen, opsporen, herstellen; proportioneel'],
             ['Kan een mens echt ingrijpen?', 'Informatie, tijd, kennis, bevoegdheid, cultuur en registratie'],
             ['Kan een getroffene bezwaar maken?', 'Bekend, laagdrempelig, snel; de verklaring klopt met het ontwerp'],
             ['Heeft elke maatregel een eigenaar?', 'Precies één A; wie mag stoppen; de leverancier geregeld']], 25, ['42%', '58%']),
    '''[3 min · deel 3 · 1:20] Zeg: "De Design Review telt niet mee voor het cijfer. Het is de generale repetitie voor Assessment 2: wat het panel vandaag vraagt, vraagt de rubric op 11 maart." Het panel heeft de concepten van dinsdag 23 februari gelezen. Bewaak de tijd streng: 8 minuten presentatie, 3 minuten vragen. Bij meer dan zes groepen: twee panels in twee lokalen, of de vragen per groep inkorten tot 2 minuten. De scores en verbeterpunten gaan dezelfde dag als bericht naar de groep. Overgang: "Ook als je luistert, werk je."''', part=3)

D.frame('dr-luisteren', K('Design Review · als je luistert') + H('Luister als een panel') + R(
    C('Per groep', UL(['Eén ding dat sterk is, en waarom.', 'Eén vraag die het panel niet stelde.'], 28), label='Op je feedbackkaart'),
    C('Voor jezelf', UL(['Welke vraag aan een andere groep past ook op jullie ontwerp?', 'Schrijf hem meteen in jullie verwerkingslijst.'], 28), label='Voor je eigen groep', accent=GOLD)) +
    D.statement('Je leert vaak het meest van de vragen aan een andere groep.', size=38),
    '''[2 min · deel 3 · 1:23] Deel de feedbackkaarten uit (A6, of via een formulier op MyCampus). Na elke presentatie geven twee groepen hun kaart af aan de presenterende groep. Overgang: de eerste groep.''', part=3)

D.frame('dr-volgorde', K('Design Review · 70 minuten') + H('Volgorde van presenteren') + D.table(
    ['Tijd', 'Groep', 'Casus', 'Feedbackkaart van'],
    [['1:25', '[Groep]', '[oplossing, partner]', '[Groep] en [Groep]'], ['1:36', '[Groep]', '[oplossing, partner]', '[Groep] en [Groep]'],
     ['1:47', '[Groep]', '[oplossing, partner]', '[Groep] en [Groep]'], ['1:58', '[Groep]', '[oplossing, partner]', '[Groep] en [Groep]'],
     ['2:09', '[Groep]', '[oplossing, partner]', '[Groep] en [Groep]'], ['2:20', '[Groep]', '[oplossing, partner]', '[Groep] en [Groep]']], 27, ['12%', '22%', '36%', '30%']) +
    P('Elke groep: 8 minuten presenteren, 3 minuten vragen. Dia 8 is jullie eigen open vraag aan het panel.', 28, MUTED),
    '''[70 min · deel 3 · 1:25] Vul de volgorde in zoals op MyCampus (uiterlijk woensdag 24 februari gepubliceerd). Laat deze dia staan tussen de presentaties. Paneltips: begin elke vraagronde met de dia 8-vraag van de groep; vraag naar één risico door de hele keten; vraag "wat kost dit, en wie betaalt het?" en "wie mag stoppen?". Noteer per groep de vier scores (0 tot 3) en drie verbeterpunten. Sluit na de laatste groep af met de twee of drie patronen die je bij alle groepen zag.''', part=3)

# ============ Deel 4. Op weg naar A2 ============
D.frame('verwerken', D.werkblok('8 min', 'Groep') + H('Verwerk de feedback van vandaag') +
    UL(['Zet de vragen en verbeterpunten van het panel en de feedbackkaarten in de verwerkingslijst.', 'Rangschik alles: eerst wat het oordeel verandert, dan wat een breuk in de keten herstelt, dan de rest.',
        'Kies de drie punten die jullie als eerste aanpakken, met een eigenaar.'], 30, ordered=True) +
    D.klaar('alle feedback van vandaag staat in de verwerkingslijst; drie punten hebben een eigenaar.', 28),
    '''[8 min · deel 4 · 2:35] Loop rond. Docentvraag: "Welk punt van het panel raakt jullie beslismemo?" Herinner: de verwerkingslijst wordt bijlage E van het eindrapport; elk punt krijgt een besluit en een plek in het rapport. Overgang: "Wat er in blok 3 nog bij komt."''', part=4)

D.frame('monitoring', K('Vooruitblik blok 3') + H('Na de livegang: wat volg je, en wanneer stop je?') + R(
    C('Ethische signalen', 'Verschillen tussen groepen, afwijken door medewerkers, bezwaren, klachten. Met grens, actie en eigenaar.', label='Indicatoren'),
    C('Incidentroute', 'Wat is een incident, wie meldt aan wie, binnen welke termijn?', label='Melden', accent=GOLD),
    C('Stopcriterium', 'Wanneer gaat het systeem uit of terug naar handwerk, en wie beslist dat?', label='Stoppen', accent=RED)) +
    D.statement('Een plan zonder stopcriterium is een wens. Dit wordt H8, en het staat ook in het beslismemo.', size=34),
    '''[4 min · deel 4 · 2:43] Zeg: "Techniek en data monitoren jullie al in A-AI2 en A-DG; verwijs daarnaar. In H8 gaat het om ethische signalen." Koppeling met ISO/IEC 42001: plan, do, check, act (kaderclip E); het beslismemo is de managementreview en noemt de datum van de volgende review. Voorbeeld ClaimWacht (voorbeeldrapport, H8): het systeem gaat voor een regio uit na twee maanden boven de grens voor onterecht aanhouden. Overgang: "Zet het in een plan."''', part=4)

D.frame('plan-a2', D.werkblok('8 min', 'Groep') + H('Jullie plan tot donderdag 11 maart') + D.table(
    ['Wanneer', 'Wat', 'Wie'],
    [['vóór zo 7 mrt', 'H6 en H7 bijgewerkt met de feedback; H8 monitoring en stopcriterium; beslismemo', '[naam] per hoofdstuk'],
     ['zo 7 mrt, 23:59', 'Concept eindrapport naar de peergroep', '[naam]'],
     ['di 9 mrt, 23:59', 'Peerfeedback terug aan de andere groep', '[naam]'],
     ['wo 10 mrt, 23:59', 'Kennischeck 3 en module-evaluatie (individueel)', 'iedereen'],
     ['do 11 mrt, 23:59', 'Eindrapport, reflectie, AI-verklaring, peerbeoordeling', 'iedereen']], 26, ['20%', '56%', '24%']) +
    D.klaar('bij elke regel een naam; de eigenaren van H6, H7, H8 en het beslismemo zijn anders dan bij A1.', 27),
    '''[8 min · deel 4 · 2:47] Zeg: "Eigenaren wisselen ten opzichte van Assessment 1: iedereen is eigenaar van minstens één hoofdstuk uit H6 tot en met H8 of van het beslismemo." Een hertest (practicum 4 opnieuw) is niet verplicht, maar telt mee voor excellent; wie hem doet, plant hem vóór 7 maart. De details staan in kennispakket 3 (Blok 3 Verantwoorden). Overgang: exit ticket.''', part=4)

# ============ Deel 5. Afsluiting ============
D.frame('exit', K('Exit ticket · 5 minuten · ICT A-ET Exit ticket college 3', dark=True) +
    UL(['De belangrijkste vraag van het panel aan onze groep was …, en we doen er dit mee: …', 'Welk thema uit het minicollege raakt jullie oplossing het meest, en waarom?', 'Wat heb je nog nodig om het beslismemo te schrijven?',
        'Bonus: welk standpunt van jou veranderde sinds college 1, en waardoor?'], 32, ON_NAVY, ordered=True) +
    D.statement('Verantwoord inzetbaar is geen eigenschap van een model. Het is een ontwerp, met een eigenaar en een stopknop.', dark=True, size=36),
    '''[5 min · deel 5 · 2:55] Individueel, via de MyCampus-opdracht ICT A-ET Exit ticket college 3. De bonusvraag is een opstap naar de reflectie. Sluit af met de kernboodschap en bedank het panel. Na het college: scores en verbeterpunten per groep dezelfde dag als bericht; lees de exit tickets en beantwoord veelgestelde vragen in de leeromgeving.''', dark=True, part=5)

D.frame('bronnen', H('Bronnen') + UL([
    'OpenAI (21 december 2016). Faulty Reward Functions in the Wild. openai.com/index/faulty-reward-functions',
    'Raad van Europa (2024). Framework Convention on Artificial Intelligence, CETS 225; ter ondertekening sinds 5 september 2024.',
    'Verordening (EU) 2024/1689 (AI-verordening) en de Digital Omnibus on AI, Verordening (EU) 2026/1744 [tekst controleren op EUR-Lex].',
    'UNESCO (2021). Recommendation on the Ethics of AI; OECD (2019, herzien 2024). AI Principles.',
    'IMF, K. Georgieva (14 januari 2024). AI Will Transform the Global Economy. imf.org',
    'ILO Working Paper 96 (2023). Gmyrek, Berg & Bescond, Generative AI and Jobs. ilo.org',
    'TIME, B. Perrigo (18 januari 2023). OpenAI Used Kenyan Workers on Less Than $2 Per Hour. time.com',
    'Markkula Center for Applied Ethics. A Framework for Ethical Decision Making; ACM Code of Ethics (2018).',
    'Frances Haugen, getuigenis voor de Amerikaanse Senaat (5 oktober 2021).',
    'ISO/IEC 42001:2023; NIST AI RMF 1.0 (2023); AIGP Body of Knowledge (IAPP).'], 22),
    '''[niet tonen tenzij gevraagd] Bronnen bij de dia's. Controleer vlak voor het college de stand van de AI-verordening (Digital Omnibus) en van het UNESCO-traject in Suriname.''')

D.frame('docent-voorbereiding', K('Docent · niet tonen') + H('Voorbereiding college 3') + G([
    UL(['Telling college 1 op “stem-terug”', 'Drie sterke punten, drie verbeterpunten en cijfers op “feedback-patroon”', 'Breuk in de keten markeren op “keten-breuk”',
        'Volgorde, tijden en feedbackgroepen op “dr-volgorde” (MyCampus uiterlijk wo 24 februari)', 'Concepten van 23 februari gelezen, met per groep twee vragen'], 25),
    UL(['Panel: [naam panel] uitgenodigd, scoreformulier gedeeld', 'Kaarten groen, rood, geel; feedbackkaarten A6', 'Video CoastRunners en QR-codes testen',
        'Stand AI-verordening en UNESCO-traject checken', 'Inleverpunt Exit ticket college 3 open; tijd, lokaal, pauze invullen'], 25)], 2, 40),
    '''Deze dia staat achteraan en wordt niet getoond. Na het college: scores en verbeterpunten per groep dezelfde dag als bericht; exit tickets lezen; kennispakket 3 openzetten.''')

if __name__ == '__main__':
    src, out = sys.argv[1], sys.argv[2]
    sections = {
        's1': {'description': 'Deel 1. Rolwissel, stemming opnieuw en feedback op Assessment 1', 'start': 'cover'},
        's2': {'description': 'Deel 2. Minicollege: veiligheid en agents, macht en regelgeving, werk in het ontwerp (verdieping op college 2), professionele praktijk', 'start': 'veiligheid'},
        's3': {'description': 'Deel 3. Design Review', 'start': 'dr-opzet'},
        's4': {'description': 'Deel 4. Feedback verwerken, monitoring en plan naar Assessment 2', 'start': 'verwerken'},
        's5': {'description': 'Deel 5. Exit ticket, bronnen en docentvoorbereiding', 'start': 'exit'},
    }
    idx = D.write(out, src + '/project/deck.json', 'College 3 AI & Ethics: Van analyse naar verantwoord ontwerp', sections, {})
    print(len(idx['order']), "dia's")
