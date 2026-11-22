import sys
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.formatting.rule import FormulaRule
from openpyxl.utils import get_column_letter as L

OUT = sys.argv[1]
DARK, SAND, INPUT = '002060', 'EAF0F8', 'FFF6DD'
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
KADER = 'herleidbaar naar een erkend kader (AI-verordening, ISO/IEC 42001, IEEE CertifAIEd of NIST AI RMF)'
A1G = dict(title='Assessment 1 · groepsdeel (rapport)', share='Telt voor 60% van het cijfer Assessment 1 (18% van het eindcijfer).',
 src='Bron: studiewijzer, sectie 9, en kennispakket 1 (tussenrapport, H1 tot en met H5).', crits=[
 ('1. Afbakening, context en stakeholders zijn helder en volledig', '(TC1) · H1 tot en met H3', .20,
  ['Onduidelijk welk besluit de AI ondersteunt; alleen organisatie en gebruikers als stakeholders',
   'Toepassing en afbakening helder; belangrijkste direct en indirect geraakten; datastroom op hoofdlijnen, met de externe diensten',
   'Kwetsbare groepen en machtsverschil benoemd; proces laat zien waar de mens zit en waar niet',
   "Daarnaast: het beeld van proces en data verklaart al waar de risico's later vandaan komen"]),
 ('2. Conclusies rusten op bewijs; onzekerheden zijn benoemd', '(TC1, GC2) · H4 en het hele rapport', .30,
  ['Scores zonder bron; meningen en feiten door elkaar',
   'Alle 11 domeinen kort gescoord; de meeste scores hebben een bron; 3 tot 4 domeinen diep onderzocht met bewijs; domeinoordeel uitgelegd',
   'Bewijssterkte consequent benoemd; tegenstrijdige bronnen opgemerkt; bij twijfel lager gescoord; uitkomsten van een eigen test (practicum 4) of ander databewijs, en werk uit A-AI2 en A-DG, als bewijs gebruikt',
   'Bronnen van verschillende soort bevestigen elkaar (document, gesprek, data); onzekerheden sturen het plan van aanpak']),
 ("4. Risico's zijn concreet geformuleerd en navolgbaar geprioriteerd", "(TC1) · H5, risico's", .30,
  ['Vage risico\'s ("bias"); geen of willekeurige scores; gaps als risico opgeschreven',
   "De 5 belangrijkste risico's als oorzaak, gebeurtenis, schade, voor wie; kans en impact gemotiveerd; escalaties genoemd; de regel EU-risicoklasse en rol staat erboven",
   'Impact op individu, groep en rechten serieus gescoord; elk risico herleidbaar naar een gap uit H4 of een dilemma uit een canvas; escalaties besproken; bij een chatbot of agent ook overtuigend fout, gegevens naar buiten, AI-melding en overdracht aan een mens; ' + KADER,
   'Scores onderbouwd met data of eigen tests; onzekerheid in de score zichtbaar gemaakt; prioriteit overtuigt; ' + KADER + ', met de EU-risicoklasse onderbouwd']),
 ('5. Plan van aanpak en advies zijn onderbouwd en proportioneel', '(TC2, GC1) · H5, voorlopig oordeel en plan', .20,
  ['Geen oordeel, of een oordeel dat niet volgt uit het rapport; plan van aanpak ontbreekt of is vaag',
   "Voorlopig oordeel volgt uit de analyse; plan noemt de drie risico's die eerst worden aangepakt en een taakverdeling",
   'Voorwaarden en onzekerheden benoemd; plan concreet, met het ontbrekende bewijs, eigenaren en data',
   'Oordeel proportioneel: weegt de baten van de toepassing eerlijk mee; plan is realistisch tot 11 maart'])],
 conds=[
  ("Aantal pagina's groepsdeel", 'getal', 8, [], None, "Meer dan 8 pagina's: lees tot en met pagina 8."),
  ('AI-verklaring aanwezig?', 'janee', 'ja', [], None, 'Geen AI-verklaring: beoordeel het rapport pas als de verklaring binnen is (binnen 24 uur na een herinnering).'),
  ('Hoofdstukeigenaren op het voorblad?', 'janee', 'ja', [], None, 'Geen hoofdstukeigenaren: een correctie op basis van de peerbeoordeling kan dan alleen na een gesprek.')],
 example=[8, 6, 6, 7], expect=6.6)

A1I = dict(title='Assessment 1 · individueel deel (dilemma-canvas)', share='Telt voor 40% van het cijfer Assessment 1 (12% van het eindcijfer).',
 src='Bron: studiewijzer, sectie 9, en kennispakket 1 (dilemma-canvas). Taal wordt niet apart beoordeeld: is de tekst zo onduidelijk dat de redenering niet te volgen is, dan telt dat mee bij het criterium waar het gebeurt.', crits=[
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
  ['Geen koppeling', 'Minstens één risico-ID uit het risicoregister van de groep (H5)', 'Uitgelegd welke kant van het dilemma welk risico oplevert', 'Ook een risico van de gekozen optie zelf benoemd'])],
 conds=[
  ('Aantal lenzen dat echt is uitgewerkt (0 tot 4)', 'getal', 4, [3], 5, 'Minder dan drie uitgewerkte lenzen: criterium D kan niet hoger dan 5.'),
  ('Aantal woorden van het canvas', 'getal', 900, [], None, 'Boven 1100 woorden: lees tot 1100 woorden, de rest telt niet. Onder 720 woorden: ontbrekende onderdelen tellen als niet gedaan.')],
 example=[7, 8, 6, 7, 8, 8], expect=None)

A2G = dict(title='Assessment 2 · groepsdeel (eindrapport)', share='Telt voor 60% van het cijfer Assessment 2 (42% van het eindcijfer).',
 src="Bron: studiewijzer, sectie 9, en kennispakket 2 en 3 (eindrapport, H1 tot en met H8 en beslismemo). De nummering volgt het lesplan: criterium 3 (dilemma) hoort bij het individuele deel van Assessment 1, criterium 9 (reflectie) bij het individuele deel van Assessment 2.", crits=[
 ('1. Afbakening, context en stakeholders', '(TC1) · H1 tot en met H3, herzien', .05,
  ['Feedback uit A1 niet verwerkt; afbakening onduidelijk', 'Feedback verwerkt; helder en beknopt',
   'Kwetsbare groepen lopen als rode draad door het ontwerp', 'Context verklaart waarom dit ontwerp past bij deze organisatie']),
 ('2. Conclusies rusten op bewijs; onzekerheden benoemd', '(TC1, GC2) · hele rapport', .10,
  ['Ontwerpkeuzes zonder onderbouwing', "Keuzes verwijzen naar risico's en bronnen",
   'Onzekerheden benoemd en meegenomen in fasering of monitoring', 'Ontbrekend bewijs uit A1 is opgehaald, of het ontwerp houdt er expliciet rekening mee']),
 ("4. Risico's concreet en navolgbaar geprioriteerd", '(TC1) · H5 herzien en H6', .10,
  ['Top 5 onduidelijk; restrisico ontbreekt', 'Top 5 onderbouwd; restrisico per risico',
   'Restrisico gemotiveerd per maatregel; escalaties krijgen een besluit; ' + KADER,
   'Restrisico eerlijk: zegt wat ondanks alles kan misgaan; ' + KADER]),
 ('5. Plan en advies onderbouwd en proportioneel', '(TC2, GC1) · H6, eisen en fasering', .10,
  ['Eisen willekeurig, of overal het zwaarste; baten van de toepassing niet meegewogen',
   'Per risico uit de top 5 een eis, met de norm waarop die rust; prioriteit of fasering uitgelegd',
   'Proportioneel: zware eisen waar het risico erom vraagt, lichtere waar het kan; baten eerlijk meegewogen',
   'Normen uit de Surinaamse context (Grondwet, ontwerpwet privacy, sector) en van de organisatie zelf meegewogen']),
 ('6. Maatregelen toetsbaar en met een eigenaar', '(TC3, TC4, GC5) · H6, en de RACI in H7', .25,
  ['Maatregelen zijn wensen; geen eigenaar; geen controle of ze werken',
   'Per risico uit de top 5 een eis met acceptatiecriterium; 2 tot 3 maatregelen met eigenaar en hoe je controleert dat ze werken; RACI aanwezig',
   'Voorkomen, opsporen en herstellen gecombineerd; minstens twee maatregelen aantoonbaar ingebouwd via A-AI2 (bijlage F); precies één A per activiteit in de RACI; bij een chatbot AI-melding, overdracht aan een mens en een testset met lastige vragen; ' + KADER,
   'Een hertest (practicum 4 opnieuw) laat het effect zien op de foutpercentages per groep; het ontwerp is uitvoerbaar in deze organisatie: kosten, capaciteit en spanning met de business case gewogen; ' + KADER]),
 ('7. Menselijke controle, bezwaar en monitoring zijn concreet, met een incidentroute en een stopcriterium', '(TC5) · H7 en H8', .25,
  ['Menselijke controle of bezwaar alleen als wens; geen of vage indicatoren ("we monitoren"); de incidentroute of het stopcriterium ontbreekt',
   'Menselijke controle met de zes voorwaarden; een bezwaarroute; indicatoren voor ethische signalen met grens, actie en eigenaar; voor techniek en data een verwijzing naar A-AI2 en A-DG; een incidentroute (wat is een incident, wie meldt aan wie, binnen welke termijn) en een stopcriterium (wanneer gaat het systeem uit of terug naar handwerk, en wie beslist dat)',
   'Een rekensom laat zien dat de controle haalbaar is; bezwaarroute en transparantieverklaring kloppen met het ontwerp; indicatoren dekken groepsverschillen, proces (afwijken, bezwaar, overdracht aan een mens) en mensen (klachten, signalen van medewerkers); incidentroute en stopcriterium zijn concreet en sluiten aan op de drempels; ' + KADER,
   'Het plan laat zien hoe het systeem wordt bijgestuurd, hertraind of stilgezet, en wie beslist; de bezwaarroute is getoetst met een getroffene of een rollenspel; het beslismemo noemt het stopcriterium en de datum van de volgende review; ' + KADER]),
 ('8. Eindoordeel helder, met voorwaarden en restrisico', '(TC2, GC4) · beslismemo', .15,
  ['Geen duidelijk oordeel, of een oordeel dat niet uit het rapport volgt',
   'Een van de drie oordelen, met voorwaarden; "nu niet" telt even zwaar als de andere twee, als het uit het rapport volgt',
   'Voorwaarden toetsbaar; restrisico en wie het accepteert benoemd; memo leesbaar voor een beslisser',
   'Weegt baten en lasten eerlijk, noemt wat het oordeel kan veranderen, en wanneer het opnieuw bekeken moet worden'])],
 conds=[
  ("Aantal pagina's (hoofdtekst)", 'getal', 12, [], None, "Meer dan 12 pagina's: lees tot en met pagina 12."),
  ('Verwerkingslijst (bijlage E) aanwezig?', 'janee', 'ja', [0, 1, 2], 6, 'Geen verwerkingslijst (bijlage E): criteria 1, 2 en 4 kunnen niet hoger dan voldoende (6).'),
  ('Beslismemo aanwezig?', 'janee', 'ja', [6], 4, 'Geen beslismemo: criterium 8 is onvoldoende (hoogstens 4).'),
  ('AI-verklaring en hoofdstukeigenaren aanwezig?', 'janee', 'ja', [], None, 'Ontbreekt de AI-verklaring of staan de hoofdstukeigenaren niet op het voorblad: zoals bij Assessment 1 (eerst verklaring, peercorrectie alleen na een gesprek).')],
 example=[7, 7, 7, 8, 6, 7, 8], expect=7.0)

A2R = dict(title='Assessment 2 · individueel deel (reflectie)', share='Telt voor 40% van het cijfer Assessment 2 (28% van het eindcijfer).',
 src='Bron: studiewijzer, sectie 9, en kennispakket 3 (reflectie), uitwerking van lesplancriterium 9 (GC3). Eerlijkheid boven gelijk hebben; geen moraalcijfer; vergelijk met de evidence cards en de standpunten uit de kennischecks.', crits=[
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
 ('F. Onderbouwing met eigen materiaal', '', .10, ['Geen verwijzingen', 'Vier verwijzingen naar evidence cards, standpunten uit de kennischecks, practica, canvas of feedback',
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
    cell(ws, 'A46', 'Peercorrectie: alleen na een gesprek en met ander bewijs dan het formulier (studiewijzer, sectie 9). Een student die veel meer deed dan de rest krijgt geen hoger groepscijfer. '
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
     ('Doel', 'Deze werkmap helpt bij het beoordelen van Assessment 1 (donderdag 4 februari) en Assessment 2 (donderdag 11 maart). De criteria, niveaus, wegingen en voorwaarden zijn dezelfde als in de rubric voor studenten (ICT A-ET Beoordelingsrubric.pdf) en in de studiewijzer, sectie 9.'),
     ('Tabbladen', 'A1 Groep (tussenrapport H1 tot en met H5, 4 criteria) · A1 Individueel (dilemma-canvas, 6 criteria) · A2 Groep (eindrapport H1 tot en met H8 en beslismemo, 7 criteria) · A2 Reflectie (6 criteria) · Eindcijfer (per student).'),
     ('Werkwijze', 'Maak per groep of per student een kopie van het tabblad (rechtsklik op de tab, Verplaatsen of kopiëren, Kopie maken). Vul bovenaan groep, student(en), beoordelaar en datum in. Kies per criterium een niveau, of vul een cijfer in: een ingevuld cijfer gaat voor het niveau. Schrijf per criterium twee regels: Waarom (wat je zag, met hoofdstuk, tabel of zin) en Naar het volgende niveau (wat ontbreekt, in de woorden van de rubric). Kernboodschap, redeneerketen-check, actiepunten en expertblik schrijf je in het Word-feedbackformulier van die toets (Feedbackformulier_A1_groep, _A1_individueel, _A2_groep, _A2_reflectie); het cijfer komt uit deze werkmap.'),
     ('Niveaus', 'Onvoldoende = 4 · Voldoende = 6 · Goed = 8 · Excellent = 10. Tussenscores (5, 7, 9) mogen als het werk tussen twee niveaus in zit. Een score onder 4 kan als iets vrijwel ontbreekt.'),
     ('Cijfer per tabblad', 'Het cijfer is het gewogen gemiddelde van de geldende criteriumscores, afgerond op één decimaal. Voorbeeld A1 groep: 8, 6, 6 en 7 geven 6,6. Voorbeeld A2 groep: 7, 7, 7, 8, 6, 7 en 8 geven 7,0.'),
     ('Voorwaarden', "Onder elke rubric staan de voorwaarden. Vul ze in; de kolom Maximum laat zien of een criterium begrensd is, en de kolom Geldend cijfer rekent daarmee. A1 groep: meer dan 8 pagina's → lees tot pagina 8. A1 individueel: minder dan drie uitgewerkte lenzen → criterium D hoogstens 5; 720 tot 1100 woorden. A2 groep: meer dan 12 pagina's → lees tot pagina 12; geen verwerkingslijst (bijlage E) → criteria 1, 2 en 4 hoogstens 6; geen beslismemo → criterium 8 onvoldoende. A2 reflectie: algemeenheden zonder concreet moment → elk criterium hoogstens 5; 1350 tot 2200 woorden. Practicum 4 en de hertest zijn geen voorwaarde: een eigen test telt mee bij criterium 2 (niveau goed), een hertest bij criterium 6 (niveau excellent)."),
     ('Cijfer per toets', 'Cijfer A1 = 0,6 × groepscijfer (na eventuele peercorrectie) + 0,4 × individueel deel. Cijfer A2 = 0,6 × groepscijfer (na eventuele peercorrectie) + 0,4 × reflectie.'),
     ('Eindcijfer', 'Eindcijfer = 0,3 × A1 + 0,7 × A2, afgerond op één decimaal, minimaal 5,5. Assessment 1 heeft geen eigen minimum; een student met een A1 onder 5,5 krijgt bij de feedback (18 februari) en in college 3 een herstelplan voor Assessment 2. Voorbeeld: A1 7,0; A2 groep 7,0 en reflectie 6,5 geeft A2 6,8 en een eindcijfer van 6,9.'),
     ('Peercorrectie', 'Bij aantoonbaar te weinig bijdrage kan het groepscijfer van één student 10%, 20% of 30% lager worden; bij vrijwel geen bijdrage een 1,0. Nooit alleen op basis van het peerformulier: er moet ook ander bewijs zijn, en de docent legt besluit en reden vast.'),
     ('Herkansing', 'Een onvoldoende voor A1 kan worden gecompenseerd. Is het eindcijfer lager dan 5,5, dan volgt een herkansing volgens de onderwijs- en examenregeling. De data en vorm moeten nog met Janssen worden afgesproken.'),
     ('Competenties', 'De codes bij de criteria (TC1 tot en met TC5, GC1 tot en met GC5) verwijzen naar de leeruitkomsten in de vakbeschrijving en het lesplan.'),
    ]
    for i, (a, b) in enumerate(rows, 3):
        cell(ws, f'A{i}', a, WH, HF, al=Alignment(vertical='top', wrap_text=True)); cell(ws, f'B{i}', b, N, al=WRT)
        ws.row_dimensions[i].height = max(30, 15 * (len(b) // 105 + 1))

def student_md(path):
    def esc(t): return t.replace('|', '/').replace('\n', ' ')
    out = ['Dit is de rubric waarmee je werk wordt beoordeeld. Elk criterium kent vier niveaus: onvoldoende (4), voldoende (6), goed (8) en excellent (10). Tussenscores (5, 7, 9) zijn mogelijk als je werk tussen twee niveaus in zit. Het cijfer per onderdeel is het gewogen gemiddelde van de criteria, afgerond op één decimaal.', '',
           'De nummering van de criteria volgt het lesplan. Criterium 3 (het dilemma) beoordelen we in het dilemma-canvas, criterium 9 (de reflectie) in de reflectie. Een eigen test (practicum 4) en een hertest zijn geen voorwaarde: ze helpen je naar de niveaus goed en excellent.', '']
    heads = {'A1 Groep': "Assessment 1, groepsdeel: tussenrapport H1 tot en met H5 (60% van A1, 18% van het eindcijfer)",
             'A1 Individueel': 'Assessment 1, individueel deel: dilemma-canvas (40% van A1, 12% van het eindcijfer)',
             'A2 Groep': 'Assessment 2, groepsdeel: eindrapport H1 tot en met H8 en beslismemo (60% van A2, 42% van het eindcijfer)',
             'A2 Reflectie': 'Assessment 2, individueel deel: reflectie (40% van A2, 28% van het eindcijfer)'}
    for nm, d in [('A1 Groep', A1G), ('A1 Individueel', A1I), ('A2 Groep', A2G), ('A2 Reflectie', A2R)]:
        out += ['## ' + heads[nm], '', '| Criterium | Onvoldoende (4) | Voldoende (6) | Goed (8) | Excellent (10) |', '| --- | --- | --- | --- | --- |']
        for crit, sub, w, lv in d['crits']:
            out.append('| ' + ' · '.join(x for x in [esc(crit), esc(sub), f'Weging {int(round(w * 100))}%'] if x) + ' | ' + ' | '.join(esc(x) for x in lv) + ' |')
        out += ['', '**Wat de docent controleert:** ' + '; '.join(c[5] for c in d['conds']), '']
    out += ['**Cijfer per toets.** Cijfer A1 = 0,6 × groepscijfer (na eventuele peercorrectie) + 0,4 × individueel deel. Cijfer A2 = 0,6 × groepscijfer (na eventuele peercorrectie) + 0,4 × reflectie.', '',
            '**Eindcijfer.** Eindcijfer = 0,3 × A1 + 0,7 × A2, afgerond op één decimaal, minimaal 5,5. Assessment 1 heeft geen eigen minimum; heb je voor A1 minder dan 5,5, dan krijg je bij de feedback (18 februari) en in college 3 een herstelplan voor Assessment 2. Voorbeeld: A1 7,0; A2 groep 7,0 en reflectie 6,5 geeft A2 6,8 en een eindcijfer van 6,9.', '',
            '**Peercorrectie.** Bij aantoonbaar te weinig bijdrage kan het groepscijfer van één student 10%, 20% of 30% lager worden; bij vrijwel geen bijdrage een 1,0. Nooit alleen op basis van het peerformulier: er moet ook ander bewijs zijn, en de docent legt besluit en reden vast.', '']
    open(path, 'w', encoding='utf-8').write('\n'.join(out))


wb = Workbook()
toelichting(wb)
res = {}
for nm, d in [('A1 Groep', A1G), ('A1 Individueel', A1I), ('A2 Groep', A2G), ('A2 Reflectie', A2R)]:
    res[nm] = form(wb, nm, d)
eind(wb)
wb.save(OUT)
if len(sys.argv) > 2:
    student_md(sys.argv[2])
if len(sys.argv) > 3:  # criteria.json voor de Word-feedbackformulieren (gen_feedbackforms.py)
    import json
    cj = {nm: dict(crit=[[c[0], c[2]] for c in d['crits']], conds=[c[0] for c in d['conds']],
                   title='AI & Ethics (A-ET) · ' + d['title'], share=d['share'])
          for nm, d in [('A1 Groep', A1G), ('A1 Individueel', A1I), ('A2 Groep', A2G), ('A2 Reflectie', A2R)]}
    json.dump(cj, open(sys.argv[3], 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('ok', OUT)
