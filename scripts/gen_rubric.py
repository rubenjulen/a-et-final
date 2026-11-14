import sys
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.formatting.rule import FormulaRule
from openpyxl.utils import get_column_letter as L

OUT = sys.argv[1]
DARK, SAND, INPUT = '12312A', 'EDE7DA', 'FFF6DD'
HF = PatternFill('solid', fgColor=DARK); SF = PatternFill('solid', fgColor=SAND); IF_ = PatternFill('solid', fgColor=INPUT)
WH = Font(name='Calibri', size=11, bold=True, color='FFFFFF'); B = Font(name='Calibri', size=11, bold=True)
N = Font(name='Calibri', size=11); T = Font(name='Calibri', size=15, bold=True, color=DARK)
WR = Alignment(wrap_text=True, vertical='center'); WRT = Alignment(wrap_text=True, vertical='top')
thin = Side(style='thin', color='BFBFBF'); BD = Border(top=thin, bottom=thin, left=thin, right=thin)
LEVELS = ['Onvoldoende', 'Voldoende', 'Goed', 'Excellent']

def setup(ws):
    ws.page_setup.orientation = 'landscape'; ws.page_setup.paperSize = 9
    ws.page_setup.fitToWidth = 1; ws.page_setup.fitToHeight = 0
    ws.sheet_properties.pageSetUpPr.fitToPage = True
    ws.print_options.gridLines = False

def cell(ws, ref, v, font=N, fill=None, al=WR, border=True, fmt=None):
    c = ws[ref]; c.value = v; c.font = font; c.alignment = al
    if fill: c.fill = fill
    if border: c.border = BD
    if fmt: c.number_format = fmt
    return c

# ---------------- data ----------------
A1G = dict(title='Assessment 1 · groepsdeel (rapport)', share='Telt voor 60% van het cijfer Assessment 1 (18% van het eindcijfer).',
 src='Bron: week 5, sectie 5 (rubric groepsdeel).', crits=[
 ('1. Afbakening, context en stakeholders zijn helder en volledig', '(TC1) · H1 tot en met H3', .20,
  ['Onduidelijk welk besluit de AI ondersteunt; alleen organisatie en gebruikers als stakeholders',
   'Toepassing en afbakening helder; belangrijkste direct en indirect geraakten; datastroom op hoofdlijnen',
   'Kwetsbare groepen en machtsverschil benoemd; proces laat zien waar de mens zit en waar niet',
   "Daarnaast: het beeld van proces en data verklaart al waar de risico's later vandaan komen"]),
 ('2. Conclusies rusten op bewijs; onzekerheden zijn benoemd', '(TC1, GC2) · H4 en het hele rapport', .25,
  ['Scores zonder bron; meningen en feiten door elkaar',
   'De meeste scores hebben een bron; 4 tot 6 domeinen diep onderzocht; domeinoordeel uitgelegd',
   'Bewijssterkte consequent benoemd; tegenstrijdige bronnen opgemerkt; bij twijfel lager gescoord; uitkomsten van practicum 4 en werk uit A-AI2 en A-DG als bewijs gebruikt',
   'Bronnen van verschillende soort elkaar laten bevestigen (document, gesprek, data); onzekerheden sturen het plan van aanpak']),
 ("3. Dilemma's zijn gewogen met minimaal drie lenzen", '(TC1, GC2) · H5', .10,
  ["Minder dan drie dilemma's, of kwesties zonder echte botsing van waarden",
   "Drie dilemma's als beslisvraag met twee waarden; minstens drie lenzen per dilemma kort toegepast",
   'Vier lenzen; voorlopig oordeel en restspanning per dilemma',
   "De dilemma's dekken samen de kern van de casus; spanningen tussen de dilemma's zijn gezien"]),
 ("4. Risico's zijn concreet geformuleerd en navolgbaar geprioriteerd", '(TC1) · H6', .30,
  ['Vage risico\'s ("bias"); geen of willekeurige scores; gaps als risico opgeschreven',
   "5 tot 8 risico's als oorzaak, gebeurtenis, schade, voor wie; kans en impact gemotiveerd; escalaties genoemd",
   'Impact op individu, groep en rechten serieus gescoord; elk risico herleidbaar naar een dilemma of gap; escalaties besproken; bij een chatbot of agent ook overtuigend fout, gegevens naar buiten, AI-melding en overdracht aan een mens; herleidbaar naar een erkend kader (AI-verordening, ISO/IEC 42001, IEEE CertifAIEd of NIST AI RMF)',
   'Scores onderbouwd met data of eigen tests; onzekerheid in de score zichtbaar gemaakt; prioriteit overtuigt; herleidbaar naar een erkend kader (AI-verordening, ISO/IEC 42001, IEEE CertifAIEd of NIST AI RMF), met de EU-risicoklasse onderbouwd']),
 ('5. Advies en gewenste situatie zijn onderbouwd en proportioneel', '(TC2, GC1) · H7', .15,
  ['Geen oordeel, of een oordeel dat niet volgt uit het rapport; plan van aanpak ontbreekt of is vaag',
   "Voorlopig oordeel volgt uit de analyse; plan noemt drie risico's om eerst aan te pakken en een taakverdeling",
   'Voorwaarden en onzekerheden benoemd; plan concreet met data en ontbrekend bewijs',
   'Oordeel proportioneel: weegt de baten van de toepassing eerlijk mee; plan is realistisch binnen vijf weken'])],
 conds=[ # (vraag, type, default, cap-criteria idx list, cap value, message)
  ('Testverslag van practicum 4 (bijlage D) aanwezig?', 'janee', 'ja', [1], 6, 'Geen testverslag van practicum 4: criterium 2 kan niet hoger dan voldoende (6).'),
  ("Aantal pagina's groepsdeel", 'getal', 8, [], None, "Meer dan 8 pagina's: lees tot en met pagina 8."),
  ('AI-verklaring aanwezig?', 'janee', 'ja', [], None, 'Geen AI-verklaring: beoordeel het rapport pas als de verklaring binnen is (binnen 24 uur na een herinnering).'),
  ('Hoofdstukeigenaren op het voorblad?', 'janee', 'ja', [], None, 'Geen hoofdstukeigenaren: een correctie op basis van de peerbeoordeling kan dan alleen na een gesprek.')],
 example=[8, 6, 8, 6, 7], expect=6.8)

A1I = dict(title='Assessment 1 · individueel deel (dilemma-canvas)', share='Telt voor 40% van het cijfer Assessment 1 (12% van het eindcijfer).',
 src='Bron: week 5, sectie 6 (rubric individueel deel). Taal wordt niet apart beoordeeld: is de tekst zo onduidelijk dat de redenering niet te volgen is, dan telt dat mee bij het criterium waar het gebeurt.', crits=[
 ('A. Beslisvraag en waarden', '(canvas 1 en 4)', .15,
  ['Geen keuze, of een kwestie met één duidelijke oplossing', 'Beslisvraag met twee waarden die echt botsen',
   'Waarden scherp benoemd en gekoppeld aan UNESCO-principes', 'De vraag legt precies de kern van de casus bloot']),
 ('B. Feiten, onzekerheid en stakeholders', '(canvas 2 en 3)', .20,
  ['Meningen en aannames door elkaar; geen bronnen', 'Belangrijkste feiten met bron; aannames apart; direct en indirect geraakten',
   'Onzekerheden die het oordeel kunnen veranderen benoemd; kwetsbaarheid en machtsverschil', 'Bronnen van verschillende soort; laat zien welk bewijs nog ontbreekt']),
 ('C. Alternatieven', '(canvas 5)', .10,
  ['Alleen doorgaan of stoppen', 'Drie reële opties', 'Waaronder een minder ingrijpende of niet-AI-optie', 'Opties combineren of faseren is overwogen']),
 ('D. Toepassing van de lenzen', '(canvas 6 tot en met 9)', .30,
  ['Lenzen als etiket, of minder dan drie lenzen uitgewerkt', 'Minstens drie lenzen echt toegepast, elk met een conclusie',
   'Alle vier lenzen, concreet voor deze casus, met eigen conclusie', 'Conflicten tussen de lenzen expliciet vergeleken en gewogen']),
 ('E. Oordeel, voorwaarden en restspanning', '(canvas 10)', .20,
  ['Conclusie zonder redenering, of "het is een afweging"', 'Eigen oordeel, dat volgt uit de analyse; voorwaarden genoemd',
   'Zegt wat wordt opgegeven; voorwaarden concreet; restspanning eerlijk benoemd',
   'Grenzen expliciet (wat nooit tegen nut mag worden weggestreept); overtuigend en proportioneel; laat zien hoe het eigen oordeel zich ontwikkelde']),
 ('F. Vertaling naar risico', '(canvas 11)', .05,
  ['Geen koppeling', 'Minstens één risico-ID uit het groepsregister', 'Uitgelegd welke kant van het dilemma welk risico oplevert', 'Ook een risico van de gekozen optie zelf benoemd'])],
 conds=[
  ('Aantal lenzen dat echt is uitgewerkt (0 tot 4)', 'getal', 4, [3], 5, 'Minder dan drie uitgewerkte lenzen: criterium D kan niet hoger dan 5.'),
  ('Aantal woorden van het canvas', 'getal', 900, [], None, 'Boven 1100 woorden: lees tot 1100 woorden, de rest telt niet. Onder 720 woorden: ontbrekende onderdelen tellen als niet gedaan.')],
 example=[7, 8, 6, 7, 8, 8], expect=None)

A2G = dict(title='Assessment 2 · groepsdeel (eindrapport)', share='Telt voor 60% van het cijfer Assessment 2 (42% van het eindcijfer).',
 src="Bron: week 8, sectie 9 (rubric Assessment 2, groepsdeel). De nummering volgt het lesplan: criterium 3 (dilemma's) hoort alleen bij Assessment 1, criterium 9 (reflectie) bij het individuele deel.", crits=[
 ('1. Afbakening, context en stakeholders', '(TC1) · H1–3 herzien', .05,
  ['Feedback uit A1 niet verwerkt; afbakening onduidelijk', 'Feedback verwerkt; helder en beknopt',
   'Kwetsbare groepen lopen als rode draad door het ontwerp', 'Context verklaart waarom dit ontwerp past bij deze organisatie']),
 ('2. Conclusies rusten op bewijs; onzekerheden benoemd', '(TC1, GC2) · hele rapport', .10,
  ['Ontwerpkeuzes zonder onderbouwing', "Keuzes verwijzen naar risico's en bronnen",
   'Onzekerheden benoemd en meegenomen in fasering of monitoring', 'Ontbrekend bewijs uit A1 is opgehaald of het ontwerp houdt er expliciet rekening mee']),
 ("4. Risico's concreet en navolgbaar geprioriteerd", '(TC1) · H6 en H12', .10,
  ['Top 5 onduidelijk; restrisico ontbreekt', 'Top 5 onderbouwd; restrisico per risico',
   'Restrisico gemotiveerd per maatregel; escalaties krijgen een besluit; herleidbaar naar een erkend kader (AI-verordening, ISO/IEC 42001, IEEE CertifAIEd of NIST AI RMF)', 'Restrisico eerlijk: zegt wat ondanks alles kan misgaan; herleidbaar naar een erkend kader (AI-verordening, ISO/IEC 42001, IEEE CertifAIEd of NIST AI RMF)']),
 ('5. Advies en gewenste situatie onderbouwd en proportioneel', '(TC2, GC1) · H7', .15,
  ['Doelniveaus willekeurig of overal 3', 'Doelniveau per domein met norm; gap en prioriteit',
   'Proportioneel: doel 3 waar het risico het vraagt; maximaal vier keer hoog',
   'Normen uit de Surinaamse context (Grondwet, ontwerpwet privacy, sector) en de organisatie zelf meegewogen']),
 ('6. Maatregelen toetsbaar en met een eigenaar', '(TC3, TC4, GC5) · H8–10', .30,
  ['Maatregelen zijn wensen; geen eigenaar; geen verificatie; niets ingebouwd',
   'Eisen met acceptatiecriterium; 2–3 maatregelen per risico met eigenaar; controle, bezwaar en RACI aanwezig; minstens twee maatregelen aantoonbaar ingebouwd via A-AI2',
   'Voorkomen, opsporen, herstellen gecombineerd; zes voorwaarden voor controle met rekensom; bezwaarroute getoetst; precies één A; de hertest laat het effect zien op de foutpercentages per groep, niet alleen op de gepaarde test; bij een chatbot zijn AI-melding, overdracht en de testset met lastige vragen hertest; herleidbaar naar een erkend kader (AI-verordening, ISO/IEC 42001, IEEE CertifAIEd of NIST AI RMF)',
   'Ontwerp is uitvoerbaar in deze organisatie: kosten, capaciteit en spanning met de business case benoemd en gewogen; herleidbaar naar een erkend kader (AI-verordening, ISO/IEC 42001, IEEE CertifAIEd of NIST AI RMF)']),
 ('7. Monitoring met indicatoren, drempels en acties, incidentroute en stopcriterium', '(TC5) · H11', .15,
  ['Geen of vage indicatoren ("we monitoren"); of de incidentroute of het stopcriterium ontbreekt',
   'Indicatoren voor ethische signalen met grens, actie en eigenaar; fasering; voor techniek en data een verwijzing naar A-AI2 en A-DG; een incidentroute (wat is een incident, wie meldt aan wie, binnen welke termijn) en een stopcriterium (wanneer gaat het systeem uit of terug naar handwerk, en wie beslist dat)',
   'Indicatoren dekken groepsverschillen, proces (afwijken, bezwaar, overdracht aan een mens) en mensen (klachten, signalen van medewerkers); incidentroute en stopcriterium zijn concreet voor deze oplossing en sluiten aan op de drempels; herleidbaar naar een erkend kader (AI-verordening, ISO/IEC 42001, IEEE CertifAIEd of NIST AI RMF)',
   'Plan laat zien hoe het systeem wordt bijgestuurd, hertraind of stilgezet, met wie beslist; het beslismemo noemt het stopcriterium en de datum van de volgende review; herleidbaar naar een erkend kader (AI-verordening, ISO/IEC 42001, IEEE CertifAIEd of NIST AI RMF)']),
 ('8. Eindoordeel helder, met voorwaarden en restrisico', '(TC2, GC4) · beslismemo, H12', .15,
  ['Geen duidelijk oordeel, of een oordeel dat niet uit het rapport volgt',
   'Een van de drie oordelen, met voorwaarden; "nu niet" telt even zwaar als de andere twee, als het uit het rapport volgt',
   'Voorwaarden toetsbaar; restrisico en wie het accepteert benoemd; memo leesbaar voor een beslisser',
   'Weegt baten en lasten eerlijk, noemt wat het oordeel kan veranderen, en wanneer het opnieuw bekeken moet worden'])],
 conds=[
  ("Aantal pagina's (hoofdtekst)", 'getal', 12, [], None, "Meer dan 12 pagina's: lees tot en met pagina 12."),
  ('Verwerkingslijst (bijlage E) aanwezig?', 'janee', 'ja', [0, 1, 2], 6, 'Geen verwerkingslijst (bijlage E): criteria 1, 2 en 4 kunnen niet hoger dan voldoende (6).'),
  ('Bewijs dat maatregelen zijn ingebouwd en hertest (bijlage F) aanwezig?', 'janee', 'ja', [4], 6, 'Geen bijlage F: criterium 6 kan niet hoger dan voldoende (6).'),
  ('Beslismemo aanwezig?', 'janee', 'ja', [6], 4, 'Geen beslismemo: criterium 8 is onvoldoende (hoogstens 4).'),
  ('AI-verklaring en hoofdstukeigenaren aanwezig?', 'janee', 'ja', [], None, 'Ontbreekt de AI-verklaring of staan de hoofdstukeigenaren niet op het voorblad: zoals bij Assessment 1 (eerst verklaring, peercorrectie alleen na een gesprek).')],
 example=[7, 7, 7, 8, 6, 7, 8], expect=7.0)

A2R = dict(title='Assessment 2 · individueel deel (reflectie)', share='Telt voor 40% van het cijfer Assessment 2 (28% van het eindcijfer).',
 src='Bron: week 8, sectie 10 (rubric individuele reflectie), uitwerking van lesplancriterium 9 (GC3). Eerlijkheid boven gelijk hebben; geen moraalcijfer; vergelijk met het logboek.', crits=[
 ('A. Het lastigste dilemma', '', .20, ['Een dilemma beschreven, geen twijfel zichtbaar', 'Zegt waarom dit dilemma lastig was',
   'Laat zien waar de student heen en weer ging, met argumenten van beide kanten', 'Benoemt wat nog steeds schuurt, en hoe de student daarmee omgaat']),
 ('B. Een onjuiste aanname', '', .20, ['Geen aanname, of een aanname over anderen', 'Een eigen aanname, en hoe die onjuist bleek',
   'Ook waarom de student het aannam en wat het veranderde', 'Verbindt het met hoe de student voortaan naar AI of organisaties kijkt']),
 ('C. Feedback die het oordeel veranderde', '', .20, ['Feedback opgesomd zonder effect', 'Eén feedbackpunt met het oordeel ervoor en erna',
   'Ook waarom de student overtuigd raakte, of juist bewust niet', 'Ziet een patroon in hoe de student met kritiek omgaat']),
 ('D. Eigen rol in het team', '', .20, ['Beschrijft taken, of geeft anderen de schuld', 'Eigen bijdrage en een eigen tekortkoming',
   'Concreet moment, eigen aandeel, en wat het team ervan merkte', 'Eerlijk, evenwichtig, met een concreet voornemen voor de volgende samenwerking']),
 ('E. Diepgang', '', .10, ['Verslag van wat er gebeurde', 'Gebeurtenis en gedachten; enige verklaring',
   'Alle vijf de stappen herkenbaar, inclusief alternatieven', 'Een overtuigend voornemen dat volgt uit de reflectie']),
 ('F. Onderbouwing met eigen materiaal', '', .10, ['Geen verwijzingen', 'Vier verwijzingen naar logboek, standpunten, practica, canvas of feedback',
   'Letterlijke citaten die het verschil tussen toen en nu laten zien', 'Het eigen materiaal draagt het betoog'])],
 conds=[
  ('Bestaat de reflectie vooral uit algemeenheden zonder concreet moment?', 'janee', 'nee', [0, 1, 2, 3, 4, 5], 5, 'Algemeenheden zonder moment ("ik heb geleerd dat ethiek belangrijk is"): elk criterium hoogstens 5.'),
  ('Aantal woorden van de reflectie', 'getal', 1800, [], None, 'Boven 2200 woorden: lees niet verder. Onder 1350 woorden ontbreken vrijwel altijd onderdelen.')],
 example=[8, 7, 7, 6, 6, 6], expect=None)

# ---------------- form sheet ----------------
def form(wb, name, d):
    ws = wb.create_sheet(name); setup(ws)
    widths = {'A': 44, 'B': 9, 'C': 34, 'D': 34, 'E': 34, 'F': 34, 'G': 15, 'H': 11, 'I': 10, 'J': 11, 'K': 40, 'L': 40}
    for k, v in widths.items(): ws.column_dimensions[k].width = v
    ws.merge_cells('A1:L1'); cell(ws, 'A1', 'AI & Ethics (A-ET) · ' + d['title'], T, al=Alignment(vertical='center'), border=False)
    ws.row_dimensions[1].height = 26
    labels = [('A2', 'Groep / casus'), ('C2', 'Student(en)'), ('G2', 'Beoordelaar'), ('J2', 'Datum')]
    vals = [('B2', None), ('D2:F2', None), ('H2:I2', None), ('K2', None)]
    for (lr, lt), (vr, _) in zip(labels, vals):
        cell(ws, lr, lt, B, SF)
        first = vr.split(':')[0]
        if ':' in vr: ws.merge_cells(vr)
        cell(ws, first, None, N, IF_)
    ws['K2'].number_format = 'DD-MM-YYYY'
    ws.merge_cells('A3:L3'); cell(ws, 'A3', d['share'] + ' Kies per criterium een niveau, of vul een cijfer van 1 tot 10 in (een cijfer gaat voor). Tussenscores (5, 7, 9) mogen als het werk tussen twee niveaus in zit.', N, al=WR, border=False)
    ws.row_dimensions[3].height = 32
    hdr = ['Criterium', 'Weging', 'Onvoldoende', 'Voldoende', 'Goed', 'Excellent', 'Niveau (kies)', 'Cijfer (1–10)', 'Maximum', 'Geldend cijfer', 'Waarom (met vindplaats)', 'Naar het volgende niveau']
    for i, h in enumerate(hdr, 1): cell(ws, f'{L(i)}4', h, WH, HF)
    pts = ['', '', '4', '6', '8', '10', '', 'optioneel', 'na voorwaarden', '', 'wat je zag, met hoofdstuk, tabel of zin', 'wat ontbreekt, in de woorden van de rubric']
    for i, p in enumerate(pts, 1): cell(ws, f'{L(i)}5', p, B, SF, al=Alignment(horizontal='center', vertical='center', wrap_text=True))
    ws.row_dimensions[4].height = 30; ws.freeze_panes = 'A6'
    n = len(d['crits']); r0 = 6
    # condition block positions (computed first so caps can reference)
    cr0 = r0 + n + 3
    cond_cells = []
    dv_lvl = DataValidation(type='list', formula1='"' + ','.join(LEVELS) + '"', allow_blank=True); ws.add_data_validation(dv_lvl)
    dv_num = DataValidation(type='decimal', operator='between', formula1='1', formula2='10', allow_blank=True,
                            error='Vul een cijfer van 1 tot 10 in.', showErrorMessage=True); ws.add_data_validation(dv_num)
    dv_jn = DataValidation(type='list', formula1='"ja,nee"', allow_blank=False); ws.add_data_validation(dv_jn)
    for k, (q, typ, default, idxs, cap, msg) in enumerate(d['conds']):
        cond_cells.append((f'C{cr0 + 1 + k}', typ, idxs, cap, msg, q))
    for i, (nm, sub, w, lv) in enumerate(d['crits']):
        r = r0 + i
        c = ws.cell(r, 1); c.value = nm + (('\n' + sub) if sub else '') + f'\nWeging {int(round(w*100))}%'
        c.font = B; c.alignment = WR; c.border = BD
        cell(ws, f'B{r}', w, N, fmt='0%', al=Alignment(horizontal='center', vertical='center'))
        for j, t in enumerate(lv): cell(ws, f'{L(3 + j)}{r}', t, N, al=WRT)
        cell(ws, f'G{r}', None, N, IF_); dv_lvl.add(f'G{r}')
        cell(ws, f'H{r}', None, N, IF_, fmt='0.0'); dv_num.add(f'H{r}')
        caps = []
        for ref, typ, idxs, cap, msg, q in cond_cells:
            if i in idxs and cap is not None:
                if typ == 'janee':
                    bad = 'nee' if 'aanwezig' in q.lower() or 'op het voorblad' in q.lower() else 'ja'
                    caps.append(f'IF({ref}="{bad}",{cap},10)')
                else:
                    caps.append(f'IF(AND({ref}<>"",{ref}<3),{cap},10)')
        cell(ws, f'I{r}', ('=MIN(' + ','.join(caps) + ')') if caps else 10, N, al=Alignment(horizontal='center', vertical='center'))
        base = f'IF(H{r}<>"",H{r},IF(G{r}="","",MATCH(G{r},{{"Onvoldoende","Voldoende","Goed","Excellent"}},0)*2+2))'
        cell(ws, f'J{r}', f'=IF({base}="","",MIN({base},I{r}))', B, fmt='0.0', al=Alignment(horizontal='center', vertical='center'))
        cell(ws, f'K{r}', None, N, IF_, al=WRT)
        cell(ws, f'L{r}', None, N, IF_, al=WRT)
        ws.row_dimensions[r].height = 120
        ws.conditional_formatting.add(f'I{r}', FormulaRule(formula=[f'I{r}<10'], fill=PatternFill('solid', fgColor='F2D3CC')))
    rt = r0 + n
    ws.merge_cells(f'A{rt}:I{rt}')
    cell(ws, f'A{rt}', 'Cijfer ' + d['title'].split(' · ')[0] + ' ' + d['title'].split(' · ')[1].split(' (')[0] + ' (gewogen gemiddelde, één decimaal)', WH, HF)
    rng_b, rng_j = f'B{r0}:B{rt-1}', f'J{r0}:J{rt-1}'
    cell(ws, f'J{rt}', f'=IF(COUNT({rng_j})={n},ROUND(SUMPRODUCT({rng_b},{rng_j})/SUM({rng_b})+0.000001,1),"nog niet compleet")',
         Font(name='Calibri', size=13, bold=True), SF, fmt='0.0', al=Alignment(horizontal='center', vertical='center'))
    cell(ws, f'K{rt}', f'=IF(ROUND(SUM({rng_b}),4)<>1,"Let op: de wegingen tellen niet op tot 100%","")', N, SF)
    ws.row_dimensions[rt].height = 24
    # conditions
    ws.merge_cells(f'A{cr0}:L{cr0}'); cell(ws, f'A{cr0}', 'Voorwaarden (vul in; het gevolg verschijnt rechts en de kolom Maximum past zich aan)', WH, HF)
    dv_int = DataValidation(type='whole', operator='between', formula1='0', formula2='100000', allow_blank=True); ws.add_data_validation(dv_int)
    for k, (q, typ, default, idxs, cap, msg) in enumerate(d['conds']):
        r = cr0 + 1 + k
        ws.merge_cells(f'A{r}:B{r}'); cell(ws, f'A{r}', q, B, SF)
        cell(ws, f'C{r}', default, N, IF_, al=Alignment(horizontal='center', vertical='center'))
        (dv_jn if typ == 'janee' else dv_int).add(f'C{r}')
        ws.merge_cells(f'D{r}:L{r}')
        msg = msg.replace('"', '""')
        if typ == 'janee':
            bad = 'nee' if 'aanwezig' in q.lower() or 'op het voorblad' in q.lower() else 'ja'
            f = f'=IF(C{r}="{bad}","{msg}","in orde")'
        elif 'lenzen' in q:
            f = f'=IF(C{r}="","",IF(C{r}<3,"{msg}","in orde"))'
        elif "pagina" in q:
            lim = 8 if '8' in msg else 12
            f = f'=IF(C{r}="","",IF(C{r}>{lim},"{msg}","in orde"))'
        else:  # woorden
            hi, lo = (1100, 720) if '1100' in msg else (2200, 1350)
            f = (f'=IF(C{r}="","",IF(C{r}>{hi},"Boven {hi} woorden: ' + ('lees tot 1100 woorden, de rest telt niet.' if hi == 1100 else 'lees niet verder.') +
                 f'",IF(C{r}<{lo},"Onder {lo} woorden: ' + ('ontbrekende onderdelen tellen als niet gedaan.' if lo == 720 else 'er ontbreken vrijwel altijd onderdelen.') + '","in orde")))')
        cell(ws, f'D{r}', f, N, al=WR)
        ws.row_dimensions[r].height = 30
        ws.conditional_formatting.add(f'D{r}', FormulaRule(formula=[f'AND(D{r}<>"in orde",D{r}<>"")'], fill=PatternFill('solid', fgColor='F2D3CC')))
    rs = cr0 + len(d['conds']) + 2
    ws.merge_cells(f'A{rs}:L{rs}'); cell(ws, f'A{rs}', d['src'], Font(name='Calibri', size=10, italic=True), al=WR, border=False)
    ws.row_dimensions[rs].height = 30
    ws.print_title_rows = '4:5'
    return ws, r0, n, rt

def eind(wb):
    ws = wb.create_sheet('Eindcijfer'); setup(ws)
    ws.merge_cells('A1:Q1'); cell(ws, 'A1', 'AI & Ethics (A-ET) · eindcijfer per student', T, al=Alignment(vertical='center'), border=False)
    ws.merge_cells('A2:Q2')
    cell(ws, 'A2', 'Neem per student de cijfers over uit de beoordelingsformulieren. Cijfer A1 = 0,6 × groepscijfer na correctie + 0,4 × individueel deel. '
         'Cijfer A2 = 0,6 × groepscijfer na correctie + 0,4 × reflectie. Eindcijfer = 0,3 × A1 + 0,7 × A2, minimaal 5,5. Alle cijfers op één decimaal.', N, al=WR, border=False)
    ws.row_dimensions[2].height = 34
    hdr = ['Nr', 'Student', 'Groep', 'A1 groepscijfer', 'A1 peercorrectie', 'A1 groep na correctie', 'A1 individueel', 'Cijfer A1', 'Signaal A1',
           'A2 groepscijfer', 'A2 peercorrectie', 'A2 groep na correctie', 'A2 reflectie', 'Cijfer A2', 'Eindcijfer', 'Status', 'Opmerking']
    w = [5, 26, 14, 11, 16, 11, 11, 10, 16, 11, 16, 11, 11, 10, 11, 24, 30]
    for i, (h, ww) in enumerate(zip(hdr, w), 1):
        cell(ws, f'{L(i)}4', h, WH, HF); ws.column_dimensions[L(i)].width = ww
    ws.row_dimensions[4].height = 32; ws.freeze_panes = 'C5'
    opts = ['geen', '10% lager', '20% lager', '30% lager', '1,0 (vrijwel geen bijdrage)']
    dv = DataValidation(type='list', formula1='"' + ','.join(opts) + '"', allow_blank=True); ws.add_data_validation(dv)
    dvn = DataValidation(type='decimal', operator='between', formula1='1', formula2='10', allow_blank=True); ws.add_data_validation(dvn)
    def corr(g, c):
        return (f'=IF({g}="","",IF({c}="1,0 (vrijwel geen bijdrage)",1,ROUND({g}*(1-IF({c}="10% lager",0.1,IF({c}="20% lager",0.2,IF({c}="30% lager",0.3,0))))+0.000001,1)))')
    for k in range(40):
        r = 5 + k
        cell(ws, f'A{r}', k + 1, N, al=Alignment(horizontal='center'))
        for col in 'BCDEGJKMQ': cell(ws, f'{col}{r}', None, N, IF_)
        for col in 'DGJM': ws[f'{col}{r}'].number_format = '0.0'; dvn.add(f'{col}{r}')
        dv.add(f'E{r}'); dv.add(f'K{r}')
        cell(ws, f'F{r}', corr(f'D{r}', f'E{r}'), N, fmt='0.0')
        cell(ws, f'H{r}', f'=IF(OR(F{r}="",G{r}=""),"",ROUND(0.6*F{r}+0.4*G{r}+0.000001,1))', B, fmt='0.0')
        cell(ws, f'I{r}', f'=IF(H{r}="","",IF(H{r}<5.5,"herstelplan voor A2",""))', N)
        cell(ws, f'L{r}', corr(f'J{r}', f'K{r}'), N, fmt='0.0')
        cell(ws, f'N{r}', f'=IF(OR(L{r}="",M{r}=""),"",ROUND(0.6*L{r}+0.4*M{r}+0.000001,1))', B, fmt='0.0')
        cell(ws, f'O{r}', f'=IF(OR(H{r}="",N{r}=""),"",ROUND(0.3*H{r}+0.7*N{r}+0.000001,1))', Font(name='Calibri', size=11, bold=True), SF, fmt='0.0')
        cell(ws, f'P{r}', f'=IF(O{r}="","",IF(O{r}>=5.5,"voldoende","onvoldoende: herkansing"))', N)
    ws.conditional_formatting.add('P5:P44', FormulaRule(formula=['LEFT(P5,11)="onvoldoende"'], fill=PatternFill('solid', fgColor='F2D3CC')))
    ws.conditional_formatting.add('I5:I44', FormulaRule(formula=['I5<>""'], fill=PatternFill('solid', fgColor='F2D3CC')))
    ws.merge_cells('A46:Q46')
    cell(ws, 'A46', 'Peercorrectie: alleen na een gesprek en met ander bewijs dan het formulier (week 5, sectie 7). Een student die veel meer deed dan de rest krijgt geen hoger groepscijfer. '
         'Herkansing: een onvoldoende voor A1 kan worden gecompenseerd. Is het eindcijfer lager dan 5,5, dan volgt een herkansing volgens de onderwijs- en examenregeling (data en vorm nog afspreken met Janssen).',
         Font(name='Calibri', size=10, italic=True), al=WR, border=False)
    ws.row_dimensions[46].height = 44
    ws.print_title_rows = '4:4'
    return ws

def toelichting(wb):
    ws = wb.active; ws.title = 'Toelichting'; setup(ws)
    ws.column_dimensions['A'].width = 28; ws.column_dimensions['B'].width = 110
    cell(ws, 'A1', 'Beoordelingsrubric AI & Ethics (A-ET), 2026-2027', T, border=False, al=Alignment(vertical='center'))
    ws.merge_cells('A1:B1'); ws.row_dimensions[1].height = 26
    rows = [
     ('Doel', 'Deze werkmap helpt bij het beoordelen van Assessment 1 (week 5) en Assessment 2 (week 10). De criteria, niveaus, wegingen en voorwaarden zijn letterlijk overgenomen uit het lesmateriaal: week 5, sectie 5 en 6, en week 8, sectie 9 en 10.'),
     ('Tabbladen', 'A1 Groep (rapport, 5 criteria) · A1 Individueel (dilemma-canvas, 6 criteria) · A2 Groep (eindrapport, 7 criteria) · A2 Reflectie (6 criteria) · Eindcijfer (per student).'),
     ('Werkwijze', 'Maak per groep of per student een kopie van het tabblad (rechtsklik op de tab, Verplaatsen of kopiëren, Kopie maken). Vul bovenaan groep, student(en), beoordelaar en datum in. Kies per criterium een niveau, of vul een cijfer in: een ingevuld cijfer gaat voor het niveau. Schrijf per criterium twee regels: Waarom (wat je zag, met hoofdstuk, tabel of zin) en Naar het volgende niveau (wat ontbreekt, in de woorden van de rubric). Kernboodschap, redeneerketen-check, actiepunten en expertblik schrijf je in het Word-feedbackformulier van die toets (Feedbackformulier_A1_groep, _A1_individueel, _A2_groep, _A2_reflectie); het cijfer komt uit deze werkmap.'),
     ('Niveaus', 'Onvoldoende = 4 · Voldoende = 6 · Goed = 8 · Excellent = 10. Tussenscores (5, 7, 9) mogen als het werk tussen twee niveaus in zit. Een score onder 4 kan als iets vrijwel ontbreekt.'),
     ('Cijfer per tabblad', 'Het cijfer is het gewogen gemiddelde van de geldende criteriumscores, afgerond op één decimaal. Voorbeeld A1 groep: 8, 6, 8, 6 en 7 geven 6,75, afgerond 6,8. Voorbeeld A2 groep: 7, 7, 7, 8, 6, 7 en 8 geven 7,0.'),
     ('Voorwaarden', 'Onder elke rubric staan de voorwaarden. Vul ze in; de kolom Maximum laat zien of een criterium begrensd is, en de kolom Geldend cijfer rekent daarmee. A1 groep: geen testverslag van practicum 4 (bijlage D) → criterium 2 hoogstens 6; meer dan 8 pagina\'s → lees tot pagina 8. A1 individueel: minder dan drie uitgewerkte lenzen → criterium D hoogstens 5; 720 tot 1100 woorden. A2 groep: meer dan 12 pagina\'s → lees tot pagina 12; geen verwerkingslijst (bijlage E) → criteria 1, 2 en 4 hoogstens 6; geen bijlage F (ingebouwd en hertest) → criterium 6 hoogstens 6; geen beslismemo → criterium 8 onvoldoende. A2 reflectie: algemeenheden zonder concreet moment → elk criterium hoogstens 5; 1350 tot 2200 woorden.'),
     ('Cijfer per toets', 'Cijfer A1 = 0,6 × groepscijfer (na eventuele peercorrectie) + 0,4 × individueel deel. Cijfer A2 = 0,6 × groepscijfer (na eventuele peercorrectie) + 0,4 × reflectie.'),
     ('Eindcijfer', 'Eindcijfer = 0,3 × A1 + 0,7 × A2, afgerond op één decimaal, minimaal 5,5. Assessment 1 heeft geen eigen minimum; een student met een A1 onder 5,5 krijgt in het feedbackgesprek een herstelplan voor Assessment 2. Voorbeeld: A1 7,0; A2 groep 7,0 en reflectie 6,5 geeft A2 6,8 en een eindcijfer van 6,9.'),
     ('Peercorrectie', 'Bij aantoonbaar te weinig bijdrage kan het groepscijfer van één student 10%, 20% of 30% lager worden; bij vrijwel geen bijdrage een 1,0. Nooit alleen op basis van het peerformulier: er moet ook ander bewijs zijn, en de docent legt besluit en reden vast.'),
     ('Herkansing', 'Een onvoldoende voor A1 kan worden gecompenseerd. Is het eindcijfer lager dan 5,5, dan volgt een herkansing volgens de onderwijs- en examenregeling. De data en vorm moeten nog met Janssen worden afgesproken.'),
     ('Competenties', 'De codes bij de criteria (TC1 tot en met TC5, GC1 tot en met GC5) verwijzen naar de leeruitkomsten in de vakbeschrijving en het lesplan.'),
    ]
    for i, (a, b) in enumerate(rows, 3):
        cell(ws, f'A{i}', a, WH, HF, al=Alignment(vertical='top', wrap_text=True)); cell(ws, f'B{i}', b, N, al=WRT)
        ws.row_dimensions[i].height = max(30, 15 * (len(b) // 105 + 1))

wb = Workbook()
toelichting(wb)
res = {}
for nm, d in [('A1 Groep', A1G), ('A1 Individueel', A1I), ('A2 Groep', A2G), ('A2 Reflectie', A2R)]:
    res[nm] = form(wb, nm, d)
eind(wb)
wb.save(OUT)
print('ok', OUT)
