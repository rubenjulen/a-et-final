import json, os, re, html
BASE = os.path.dirname(os.path.abspath(__file__))
C = json.load(open(os.path.join(BASE, 'clips.json')))
INK, LIGHT, SAND, CARD, AMBER, GREEN, RED, DARK = '#1C2421', '#F6F3EC', '#EDE7DA', '#FFFDF8', '#E3A92B', '#2F6B4F', '#A8432C', '#12312A'
SERIF = "'Source Serif 4', Georgia, serif"
SANS = "'Public Sans', Arial, sans-serif"
e = html.escape

def clean(t):
    t = t.replace('\\_', '_').replace('\\[', '[').replace('\\]', ']')
    t = re.sub(r'\*\*(.*?)\*\*', r'\1', t)
    t = re.sub(r'(?<!\w)\*(.*?)\*(?!\w)', r'\1', t)
    t = t.replace('Excel-tool', 'werkboek').replace('de toolkit', 'het werkboek').replace('uit de toolkit', 'uit het werkboek').replace('Toolkit, tabblad', 'Werkboek, tabblad')
    return t.strip().strip('"').replace('"', '“', 1) if False else t.strip()

def sec(sid, inner, notes, bg=LIGHT, color=INK, footer=None, extra=''):
    pad = '128px 128px 160px' if footer else '128px'
    f = f'<p style="position:absolute;left:128px;bottom:64px;width:1664px;font-size:24px;color:#6A7179">{e(footer)}</p>' if footer else ''
    return (f'<section id="{sid}" data-transition="fade" style="background:{bg};color:{color};font-family:{SANS};padding:{pad};display:flex;flex-direction:column;gap:44px{extra}">\n'
            f'{inner}\n{f}\n<aside>{e(notes)}</aside>\n</section>\n')

def head(kicker, title, kcol=GREEN, tcol=INK):
    return (f'<div style="display:flex;flex-direction:column;gap:14px"><p style="font-size:24px;font-weight:700;color:{kcol};text-transform:uppercase;letter-spacing:2px">{e(kicker)}</p>'
            f'<h2 style="font-family:{SERIF};font-size:64px;font-weight:600;line-height:1.1;color:{tcol}">{e(title)}</h2></div>')

def cards(items, cols=None, bg=CARD, size=28):
    items = [x for x in items if x[0]]
    n = len(items); cols = cols or (3 if n in (3, 5, 6, 9) else 2 if n in (2, 4) else 4)
    out = [f'<div style="display:grid;grid-template-columns:repeat({cols},1fr);gap:24px">']
    for lab, txt in items:
        out.append(f'<div style="background:{bg};border-radius:16px;padding:32px 34px;display:flex;flex-direction:column;gap:12px">'
                   f'<h3 style="font-family:{SERIF};font-size:34px;font-weight:600;line-height:1.15;color:{DARK}">{e(lab)}</h3>'
                   + (f'<p style="font-size:{size}px;line-height:1.35;color:#44504B">{e(txt)}</p>' if txt else '') + '</div>')
    out.append('</div>'); return ''.join(out)

def steps(items, accent=AMBER):
    out = ['<div style="display:flex;gap:20px;align-items:stretch">']
    for i, (lab, txt) in enumerate(items):
        out.append(f'<div style="flex:1;background:{CARD};border-radius:16px;padding:30px 26px;display:flex;flex-direction:column;gap:12px;border-top:8px solid {accent}">'
                   f'<p style="font-family:{SERIF};font-size:44px;font-weight:700;color:{DARK};line-height:1">{e(lab)}</p>'
                   + (f'<p style="font-size:26px;line-height:1.3;color:#44504B">{e(txt)}</p>' if txt else '') + '</div>')
    out.append('</div>'); return ''.join(out)

def statement(txt, size=48):
    return f'<p style="font-family:{SERIF};font-size:{size}px;font-weight:600;line-height:1.25;color:{DARK};max-width:1500px">{e(txt)}</p>'

def quote(txt, who=''):
    w = f'<p style="font-size:26px;color:#44504B">{e(who)}</p>' if who else ''
    return (f'<div style="border-left:10px solid {AMBER};background:{CARD};border-radius:0 16px 16px 0;padding:40px 48px;display:flex;flex-direction:column;gap:16px">'
            f'<p style="font-family:{SERIF};font-size:42px;font-weight:600;line-height:1.3;color:{DARK}">“{e(txt)}”</p>{w}</div>')

def note(txt, col=GREEN):
    return f'<p style="font-size:28px;font-weight:700;color:{col}">{e(txt)}</p>'

def big(nums):
    out = ['<div style="display:flex;gap:40px">']
    for n, lab in nums:
        out.append(f'<div style="flex:1;background:{CARD};border-radius:16px;padding:40px;display:flex;flex-direction:column;gap:10px">'
                   f'<p style="font-family:{SERIF};font-size:96px;font-weight:700;color:{AMBER};line-height:1">{e(n)}</p>'
                   f'<p style="font-size:28px;color:#44504B;line-height:1.3">{e(lab)}</p></div>')
    out.append('</div>'); return ''.join(out)

def vs(a_lab, a_txt, b_lab, b_txt, a_col=RED, b_col=GREEN):
    return (f'<div style="display:flex;gap:28px">'
            f'<div style="flex:1;background:{CARD};border-radius:16px;padding:36px;border-top:8px solid {a_col};display:flex;flex-direction:column;gap:14px"><p style="font-size:26px;font-weight:700;color:{a_col};text-transform:uppercase;letter-spacing:1.5px">{e(a_lab)}</p><p style="font-family:{SERIF};font-size:38px;font-weight:600;line-height:1.25;color:{DARK}">{e(a_txt)}</p></div>'
            f'<div style="flex:1;background:{CARD};border-radius:16px;padding:36px;border-top:8px solid {b_col};display:flex;flex-direction:column;gap:14px"><p style="font-size:26px;font-weight:700;color:{b_col};text-transform:uppercase;letter-spacing:1.5px">{e(b_lab)}</p><p style="font-family:{SERIF};font-size:38px;font-weight:600;line-height:1.25;color:{DARK}">{e(b_txt)}</p></div></div>')

def table(header, rows):
    th = ''.join(f'<th style="text-align:left;padding:18px 22px;background:{SAND};font-size:26px;color:{DARK}">{e(h)}</th>' for h in header)
    trs = ''.join('<tr>' + ''.join(f'<td style="padding:18px 22px;font-size:28px;border-bottom:2px solid {SAND};background:{CARD}">{e(c)}</td>' for c in r) + '</tr>' for r in rows)
    return f'<table style="border-collapse:collapse;width:1664px"><tr>{th}</tr>{trs}</table>'

# On-slide visuals per clip, index-aligned with the table rows (row 0 = title).
V = {
11: [None,
     lambda: cards([('Eind jaren 80', 'Carnegie Mellon (SEI) ontwikkelt het Capability Maturity Model, voor het Amerikaanse ministerie van Defensie'), ('De vraag', 'Kan deze leverancier betrouwbaar software opleveren?'), ('Het antwoord', 'Niet in beloftes, maar in vastgelegde, herhaalbare processen')]),
     lambda: steps([('1', 'Initial: het hangt af van helden'), ('2', 'Repeatable'), ('3', 'Defined'), ('4', 'Managed'), ('5', 'Optimizing')]) + note('CMMI kijkt ook per procesgebied: hoe goed beheerst een organisatie precies dít onderdeel?'),
     lambda: steps([('0', 'Niet aanwezig of onbekend'), ('1', 'Ad hoc'), ('2', 'Gedeeltelijk beheerst'), ('3', 'Aantoonbaar beheerst')], GREEN) + note('Vier niveaus: fijner kun je in een korte module niet betrouwbaar aantonen'),
     lambda: cards([('1. Bewijs', 'Een score zonder bewijs telt niet'), ('2. Twijfel', 'Kies het laagste niveau en schrijf op wat ontbreekt'), ('3. Geen totaal', 'Goede beveiliging compenseert geen ontbrekende bezwaarprocedure')]),
     lambda: steps([('Sterk', 'Document én observatie of data'), ('Goed', 'Een document of concreet voorbeeld'), ('Beperkt', 'Eén interview of uitspraak'), ('Zwak', 'Aanname of “dat zal wel”')], GREEN) + note('Suribank: het document zegt 2 (D3), de praktijk zegt 1: 4 afwijkingen op 211 aanvragen (D11)'),
     lambda: vs('Maturity', 'Hoe goed is het geregeld?', 'Risico', 'Hoe erg is het als het misgaat?', GREEN, RED) + note('Maturity 3 en toch een onomkeerbare fout mogelijk? Daarom ook een risicoregister'),
     None],
12: [None,
     lambda: cards([('Waarde', 'Wat we belangrijk vinden'), ('Kwestie', 'Een waarde staat onder druk'), ('Dilemma', 'Kiezen tussen twee zware waarden'), ('Hazard', 'Bron van mogelijke schade'), ('Risico', 'Hazard + kans + schade'), ('Control', 'Maatregel die kans of schade verkleint'), ('Restrisico', 'Wat overblijft na de control')], 4, size=26),
     lambda: cards([('Is het een keuze?', '→ een dilemma'), ('Kan het gebeuren, met kans en schade?', '→ een risico'), ('Ontbreekt er iets in de organisatie?', '→ een maturity gap')]),
     lambda: quote('Door [oorzaak] kan [gebeurtenis] optreden, met als gevolg [schade] voor [wie].') + note('Voorbeeld: aanvragers uit het binnenland vaker onterecht afgewezen → uitsluiting van krediet'),
     lambda: vs('Kies je voor snelheid', 'Risico: onterechte afwijzing zonder menselijke blik', 'Kies je voor persoonlijke beoordeling', 'Risico: langere wachttijd en willekeur tussen medewerkers', AMBER, AMBER) + note('Beide horen in het register'),
     lambda: quote('Een dilemma los je niet op met een control. Je maakt een keuze, en dan beheers je de risico’s van die keuze.'),
     None],
13: [
     lambda: statement('Dit is het register. Elke rij is één risico.') + note('Werkboek A-ET, tabblad Risk_Register'),
     lambda: steps([('1', 'Zeldzaam'), ('2', 'Onwaarschijnlijk'), ('3', 'Mogelijk'), ('4', 'Waarschijnlijk'), ('5', 'Bijna zeker')]) + note('Onderbouw de kans: een cijfer uit het dossier, een vergelijkbaar geval, practicum 2 of 4'),
     lambda: cards([('Individu', ''), ('Groep of samenleving', ''), ('Rechten en waardigheid', ''), ('Organisatie', '')], 4) + statement('Totale impact = de hoogste van de vier, niet het gemiddelde', 40),
     lambda: note('Score = kans × impact', DARK) + steps([('Low', '1 tot 4'), ('Moderate', '5 tot 9'), ('High', '10 tot 14'), ('Very high', '15 tot 19'), ('Critical', '20 tot 25')], RED),
     lambda: cards([('Rechten', 'Impact op rechten 4 of hoger'), ('Onomkeerbaar', 'De schade is niet terug te draaien'), ('Kwetsbare groep', 'Geraakt met impact 4 of hoger'), ('Geen bezwaar', 'Geen bezwaarmogelijkheid en impact 3 of hoger')], 4, size=26) + note('Dan escaleren, los van de score'),
     lambda: statement('Eén getal voor “hoe ethisch” verbergt welke waarde je hebt opgeofferd.') + note('Daarom scoren we risico’s, en wegen we dilemma’s met argumenten'),
     None],
14: [None,
     lambda: steps([('Bewijs', ''), ('Gap', ''), ('Dilemma', ''), ('Risico', ''), ('Oordeel', 'aan het eind van de keten')], GREEN) + note('Elke zin in het oordeel is terug te voeren op iets eerder in het rapport'),
     lambda: cards([('Verantwoord inzetbaar', ''), ('Inzetbaar onder voorwaarden', ''), ('Nu niet', '')]) + note('In Assessment 1 is het oordeel voorlopig: wat verwacht je nu, en wat kan het veranderen?'),
     lambda: quote('Voorlopig: nu niet in de huidige vorm, wel onder voorwaarden. Voorwaarden: een bezwaarroute, menselijke beoordeling van afwijzingen, testen per regio.', 'Onzeker: of de verschillen tussen regio’s deels terecht zijn'),
     lambda: cards([('1', 'Welke drie risico’s eerst, en waarom?'), ('2', 'Welk bewijs ontbreekt, en hoe krijgen we het?'), ('3', 'Welke maatregel bouwen we met A-AI2 in, en welke test doen we in week 9 opnieuw?'), ('4', 'Wie is eigenaar van welk hoofdstuk in A2?'), ('5', 'Wat doen we wanneer, tot 11 maart?')], 3, size=26),
     lambda: vs('Geen plan', '“We gaan meer onderzoek doen.”', 'Wel een plan', '“Vóór 15 februari vragen we het afwijzingscijfer per filiaal op bij de afdeling krediet.”'),
     None],
15: [None,
     lambda: vs('Wat de norm vraagt', 'UNESCO, NIST AI RMF, Grondwet art. 8 lid 2, de ontwerpwet privacy; de AI-verordening ter vergelijking', 'Wat er op het spel staat', 'De risico’s uit jullie register', GREEN, AMBER),
     lambda: steps([('3', 'High of hoger risico, of een escalatievlag'), ('2', 'Een basisniveau is genoeg'), ('1', 'Speelt nauwelijks; zeg waarom')], GREEN) + note('Overal 3 is niet ambitieus maar onrealistisch'),
     lambda: quote('Gap = doelniveau − huidig niveau') + statement('Prioriteit is niet de grootte van de gap: een kleine gap bij een kritisch risico gaat voor.', 38),
     lambda: table(['Domein', 'Nu', 'Doel', 'Prioriteit'], [['7 Menselijke controle en bezwaar', '1', '3', 'Hoog: vier risico’s escaleren'], ['8 Security', '2', '2', 'Geen gap, en dat mag']]),
     None],
16: [None,
     lambda: cards([('Vermijden', 'Avoid/stop: het risicovolle deel eruit'), ('Verminderen', 'Treat of Redesign: kans of impact kleiner'), ('Delen', 'Transfer: gevolgen deels bij een ander'), ('Accepteren', 'Accept: bewust niets extra, met een eigenaar')], 4, size=26),
     lambda: statement('Een contract verschuift kosten. De klant die onterecht wordt afgewezen, heeft daar niets aan.') + note('Bij risico’s voor mensen is delen hooguit een aanvulling'),
     lambda: quote('Aanvragers uit het binnenland worden niet vaker onterecht afgewezen dan aanvragers aan de kust.', 'Ontwerpdoel = het risico omgedraaid, in gewone taal'),
     lambda: cards([('De eis', 'Vóór ingebruikname worden prestaties en fouttypen per groep getest'), ('Het acceptatiecriterium', 'Overschrijding van vooraf bepaalde grenzen blokkeert ingebruikname of vraagt herontwerp')]),
     lambda: vs('Een wens', '“Het model moet eerlijk zijn.”', 'De toets voor een eis', 'Kan iemand anders over drie maanden zeggen of hieraan is voldaan?'),
     lambda: statement('Een grens is een bestuurlijke keuze, geen technisch feit.') + note('Stel er een voor met een reden, en zeg wie hem vaststelt'),
     None],
17: [None,
     lambda: cards([('Voorkomen', 'Het gaat niet mis'), ('Opsporen', 'Je merkt het als het misgaat'), ('Herstellen', 'Je maakt het goed')]) + note('Per belangrijk risico minstens twee van de drie'),
     lambda: steps([('Techniek', ''), ('Data en model', ''), ('Proces', ''), ('Mens', ''), ('Governance', '')], GREEN) + note('Generatieve AI: AI-melding, overdracht aan een mens, beperkte bronnen, geen persoonsgegevens naar buiten, vaste testset'),
     lambda: cards([('Doel', ''), ('Eigenaar', ''), ('Werking', ''), ('Bewijs', ''), ('Controle', ''), ('Plus', 'Wie bouwt het in A-AI2, en welke testvraag laat het in week 9 zien?')], 3, size=26),
     lambda: statement('Inspiratie, geen boodschappenlijst.') + cards([('Menselijke beoordeling verplicht', ''), ('Bezwaar en herbeoordeling', ''), ('Subgroeptest', '')]) + note('Werkboek A-ET, tabblad Control_Catalog'),
     lambda: vs('Voorkomen', 'verlaagt vooral de kans', 'Opsporen en herstellen', 'verlagen vaak de impact', GREEN, GREEN) + note('Blijft de impact op rechten hoog? Dan blijft het besluit bij de directie'),
     lambda: quote('Een restrisico van 1 bij alles is niet geloofwaardig. Wat kan er ondanks je maatregelen nog misgaan?'),
     None],
18: [None,
     lambda: cards([('In de lus', 'Elk besluit gaat langs een mens'), ('Op de lus', 'Het systeem beslist; een mens houdt toezicht en kan ingrijpen'), ('Aan het roer', 'Een mens bepaalt of, waar en hoe het systeem wordt ingezet')]),
     lambda: big([('4 / 211', 'afwijkingen van het advies bij Suribank')]) + quote('Als het model het zegt, ligt het niet bij mij.', 'Medewerker Suribank (D8)'),
     lambda: cards([('Informatie', 'Ziet waarom'), ('Tijd', 'Genoeg om echt te kijken'), ('Kennis', 'Weet wanneer je het systeem niet vertrouwt'), ('Bevoegdheid', 'Mag afwijken zonder toestemming'), ('Cultuur', 'Afwijken met reden is normaal'), ('Registratie', 'Afwijkingen worden bijgehouden')], 3, size=26) + note('AI-verordening, artikel 14: hetzelfde bij hoog risico'),
     lambda: vs('Reviewtrigger', 'Afwijzingen, scores bij de drempel, kwetsbare groepen, onvolledige gegevens', 'Escalatietrigger', 'Wanneer gaat het hoger op?', AMBER, RED),
     lambda: steps([('Bezwaar', ''), ('Boosheid', ''), ('Kwetsbaar', ''), ('Belangrijk besluit', ''), ('Op verzoek', '')], AMBER) + note('Wanneer draagt de chatbot over aan een mens?'),
     lambda: statement('Leg medewerkers een dossier voor waarin het model aantoonbaar fout zit. Wijken ze af?') + note('Bij een chatbot: blok 4 van de testset uit practicum 4 (mens spreken)'),
     None],
19: [None,
     lambda: cards([('Bekend', 'Staat in het besluit zelf'), ('Laagdrempelig', 'Geen advocaat of lang formulier'), ('Met uitleg', 'Je weet waartegen'), ('Onafhankelijk', 'Iemand die niet bij het besluit betrokken was'), ('Snel', 'Een vaste termijn'), ('Herstellend', 'Bij gelijk wordt de schade goedgemaakt')], 3, size=26),
     lambda: statement('Elk gegrond bezwaar is een signaal.') + note('Hoeveel, waarover, en wat doen we ermee in het model en het proces?'),
     lambda: statement('Ouders wisten niet waartegen ze bezwaar maakten: dossiers bleven dicht of waren zwartgelakt.') + note('Zie de casus toeslagenaffaire'),
     lambda: steps([('Excuus', ''), ('Besluit herzien', ''), ('Gegevens corrigeren', ''), ('Label verwijderen', '')], GREEN) + note('Wat is herstel voor jouw getroffene?'),
     None],
20: [None,
     lambda: cards([('Getroffenen', 'Dat er een systeem meebeslist, waarvoor, wat de uitkomst betekent, hoe bezwaar werkt'), ('Gebruikers', 'Wat het systeem kan en niet kan, en waarom het dit adviseert'), ('Toezicht en directie', 'Hoe het werkt, hoe het presteert, wat er is gelogd')], size=26),
     lambda: steps([('Kort', 'Korte zinnen'), ('Gewoon', 'Geen vakjargon'), ('Eerst', 'Het belangrijkste vooraan')], GREEN) + note('Toets: begrijpt iemand zonder IT-opleiding na één keer lezen wat er gebeurt en wat ze kan doen?'),
     lambda: statement('Zeg dat het AI is: aan het begin van het gesprek, niet alleen op de website.') + note('Europa: AI-verordening, artikel 50. Suriname: een goede maatstaf. En denk aan Air Canada'),
     lambda: cards([('R', 'Responsible: voert uit'), ('A', 'Accountable: eindverantwoordelijk, precies één'), ('C', 'Consulted: vooraf gevraagd'), ('I', 'Informed: achteraf geïnformeerd')], 4, size=26) + note('Werkboek A-ET, tabblad Governance_RACI'),
     lambda: cards([('Wie mag stoppen?', ''), ('Wie besluit over hertraining?', ''), ('Wie accepteert restrisico?', '')]) + quote('Ik neem aan de directie.', 'Suribank (D7)'),
     None],
21: [None,
     lambda: vs('Wie er aanvraagt', 'De invoer verandert', 'Wat er gebeurt', 'De uitkomst verandert', AMBER, AMBER) + note('Andere klanten, inflatie, een nieuwe wet, een nieuw filiaal'),
     lambda: vs('Vroeg', 'Invoer en beslissingen zie je meteen', 'Laat', 'Uitkomsten zie je pas na maanden of jaren', GREEN, AMBER) + note('Monitor allebei. Practicum 5 laat zien waarom'),
     lambda: cards([('Groepsverschillen', 'Fouten, afwijzingen en goedkeuringen per groep'), ('Proces', 'Afwijkingen, bezwaren binnen termijn, overdrachten'), ('Mensen', 'Klachten, gegronde bezwaren, signalen van medewerkers')], size=26),
     lambda: steps([('Wat', ''), ('Hoe vaak', ''), ('Wie', ''), ('Grens', ''), ('Actie', 'en door wie')], GREEN) + note('Zonder grens is het een getal; zonder actie een alarm dat niemand hoort'),
     lambda: statement('Een grens is een bestuurlijke keuze. Begin streng en versoepel als je meer weet.') + note('Geef een reden, en zeg wie hem vaststelt'),
     lambda: steps([('Onderzoeken', ''), ('Bijsturen', 'drempel aanpassen, meer gevallen naar een mens'), ('Stilzetten', 'terug naar handmatig')], RED) + note('De RACI zegt wie wat besluit. In K8 ook altijd: incidentroute en stopcriterium'),
     None],
22: [None,
     lambda: cards([('Verantwoord inzetbaar', 'Doorgaan met monitoring'), ('Onder voorwaarden', 'Doorgaan, mits maatregelen op tijd; anders stoppen of terugschalen'), ('Nu niet', 'Stoppen, herontwerpen of niet beginnen')], size=26),
     lambda: cards([('1 Oordeel', 'In de eerste zin'), ('2 Waarom', 'Drie redenen, één uit de hertest'), ('3 Wat het oplevert', ''), ('4 Voorwaarden', 'Toetsbaar, termijn, eigenaar'), ('5 Restrisico', 'En wie het accepteert'), ('6 Wat het kan veranderen', ''), ('7 Managementreview', 'Stopcriterium en datum volgende review')], 4, size=24),
     lambda: steps([('Zwak', '“Er komt een bezwaarroute”'), ('Beter', '“De bezwaarroute werkt binnen drie maanden”'), ('Met tanden', '“Werkt hij op 1 juli niet, dan gaan alle afwijzingen weer handmatig”')], GREEN),
     lambda: big([('14 → 1,6', 'werkdagen doorlooptijd bij Suribank')]) + note('Noem ook de baten. Een memo met alleen risico’s overtuigt geen directeur'),
     lambda: statement('Het memo herhaalt het rapport niet. Het verwijst ernaar: “zie hoofdstuk 8”.'),
     None],
}
EXTRA_NOTES = {
    (21, 6): ' Leg in K8 ook altijd de incidentroute en het stopcriterium vast: wat is een incident, wie meldt aan wie, en wanneer gaat het systeem uit, en wie beslist dat.',
    (22, 2): ' Het memo heeft zeven vaste onderdelen: oordeel, waarom, wat het oplevert, voorwaarden, restrisico en wie het accepteert, wat het oordeel kan veranderen, en de managementreview met het stopcriterium en de datum van de volgende review.',
}
DECKS = {'week4': ('04', [11, 12, 13], 'Week 4'), 'week5': ('05', [14], 'Week 5'), 'week6': ('06', [15, 16, 17], 'Week 6'), 'week7': ('07', [18, 19, 20], 'Week 7'), 'week9': ('09', [21, 22], 'Week 9')}
FACES = {"source-serif-4": {"family": "Source Serif 4", "href": "https://fonts.googleapis.com/css2?family=Source+Serif+4:wght@400..700&display=swap"},
         "public-sans": {"family": "Public Sans", "href": "https://fonts.googleapis.com/css2?family=Public+Sans:wght@400;600;700&display=swap"}}

def build(name):
    wk, clips, wlabel = DECKS[name]
    root = os.path.join(BASE, name, 'project'); os.makedirs(os.path.join(root, 'slides'), exist_ok=True)
    order, sections, files, stats = [], {}, {}, {}
    tot = sum(C[str(c)]['dur'] for c in clips)
    cl = ', '.join(str(c) for c in clips)
    # cover
    sid = 'cover'
    inner = (f'<p style="font-size:26px;font-weight:700;color:{AMBER};text-transform:uppercase;letter-spacing:2px">AI &amp; Ethics (A-ET) · {wlabel} · opnamekit</p>'
             f'<h1 style="font-family:{SERIF};font-size:96px;font-weight:700;line-height:1.05;color:{LIGHT}">Kennisclip{"s" if len(clips) > 1 else ""} {e(cl)}</h1>'
             + ''.join(f'<p style="font-size:32px;color:{SAND}">Clip {c}: {e(C[str(c)]["title"])} · {C[str(c)]["dur"]} min</p>' for c in clips)
             + f'<p style="font-size:28px;color:{AMBER};font-weight:700">Samen {tot} minuten</p>')
    files[sid] = sec(sid, inner, f'Opnamekit voor {wlabel}: clip {cl}. Begin bij de dia "Zo neem je deze clips op".', bg=DARK, color=LIGHT, extra=';justify-content:center')
    order.append(sid); sections['s0'] = {'description': 'Opnamekit en werkwijze', 'start': 'cover'}
    sid = 'opnemen'
    rows = [[f'Clip {c}', C[str(c)]['title'], f'{C[str(c)]["dur"]} min'] for c in clips]
    inner = head('Voor de docent', 'Zo neem je deze clips op') + cards([
        ('1 Exporteer', 'Share › Export naar pptx, open in PowerPoint'),
        ('2 Neem op', 'Opnemen › Vanaf huidige dia, op de titeldia van de clip'),
        ('3 Notities', 'Houd de sprekersnotities in beeld; praat vrij langs de kernzinnen'),
        ('4 Per clip', 'Verberg de andere clips (Dia verbergen) of werk in een kopie'),
        ('5 Video', 'Exporteren › Video maken: mp4, 1080p'),
        ('6 Pauzes', 'Laat bij een vraag een korte stilte; studenten pauzeren zelf')], 3, size=24) + table(['Clip', 'Titel', 'Richtduur'], rows)
    files[sid] = sec(sid, inner, 'De tekst in de notities is een draaiboek, geen voorleestekst. Lees hem een keer hardop door en praat dan vrij langs de kernzinnen. Neem elke clip apart op en exporteer als mp4 in 1080p. Upload de video op MyCampus bij de week en vervang daar de regel "Video: link volgt".', bg=LIGHT)
    order.append(sid)
    for c in clips:
        d = C[str(c)]; rows = d['rows']; foot = f'Clip {c} · {d["title"]}'
        sid = f'c{c}-titel'; order.append(sid); sections[f's{c}'] = {'description': f'Clip {c}: {d["title"]}', 'start': sid}
        n0 = clean(rows[0][2]) if rows[0][1] == 'Titeldia' else ''
        inner = (f'<p style="font-size:26px;font-weight:700;color:{AMBER};text-transform:uppercase;letter-spacing:2px">Kennisclip {c} · {d["dur"]} minuten</p>'
                 f'<h1 style="font-family:{SERIF};font-size:88px;font-weight:700;line-height:1.08;color:{LIGHT}">{e(d["title"])}</h1>'
                 f'<p style="font-size:30px;line-height:1.4;color:{SAND};max-width:1400px">{e(clean(d["doel"]).replace("De student", "Na deze clip"))}</p>' if d['doel'] else
                 f'<p style="font-size:26px;font-weight:700;color:{AMBER};text-transform:uppercase;letter-spacing:2px">Kennisclip {c} · {d["dur"]} minuten</p>'
                 f'<h1 style="font-family:{SERIF};font-size:88px;font-weight:700;line-height:1.08;color:{LIGHT}">{e(d["title"])}</h1>')
        files[sid] = sec(sid, inner, n0 or f'Kennisclip {c}: {d["title"]}.', bg=DARK, color=LIGHT, extra=';justify-content:center')
        cnt = 1
        for i, (tijd, beeld, kern) in enumerate(rows):
            if i == 0 and beeld == 'Titeldia':
                continue
            last = i == len(rows) - 1
            bl = clean(beeld); bl = bl[:1].upper() + bl[1:]
            notes = clean(kern) + EXTRA_NOTES.get((c, i), '')
            sid = f'c{c}-{i}'; order.append(sid); cnt += 1
            if last:
                inner = (f'<p style="font-size:26px;font-weight:700;color:{AMBER};text-transform:uppercase;letter-spacing:2px">Clip {c} · {e(bl)}</p>'
                         f'<p style="font-family:{SERIF};font-size:60px;font-weight:600;line-height:1.2;color:{LIGHT};max-width:1500px">{e(clean(kern).strip(chr(34)))}</p>')
                files[sid] = sec(sid, inner, notes, bg=GREEN, color=LIGHT, extra=';justify-content:center')
            else:
                vis = V[c][i]() if V[c][i] else statement(clean(kern))
                files[sid] = sec(sid, head(f'Clip {c} · {tijd}', bl) + vis, notes, bg=LIGHT if i % 2 else CARD, footer=foot)
        stats[c] = cnt
    for sid, h in files.items():
        open(os.path.join(root, 'slides', sid + '.html'), 'w').write(h)
    return root, order, sections, stats

if __name__ == '__main__':
    import sys
    out = {}
    for name in DECKS:
        root, order, sections, stats = build(name)
        out[name] = {'order': order, 'sections': sections, 'stats': stats, 'n': len(order)}
    json.dump(out, open(os.path.join(BASE, 'build.json'), 'w'), indent=1)
    for k, v in out.items(): print(k, v['n'], v['stats'])
