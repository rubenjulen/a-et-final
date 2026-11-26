# Genereert het studentenwerkboek met de instrumenten van A-ET (K1-K8).
# Bron: sjablonen, kolommen en schalen in de weekdocumenten 1-9 (november 2026).
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.formatting.rule import FormulaRule
from openpyxl.utils import get_column_letter as L

import sys
OUT = sys.argv[1] if len(sys.argv) > 1 else 'lesmateriaal/instrumenten/A-ET_werkboek_instrumenten_2026-2027.xlsx'

DARK, SAND, INPUT, WARN, GREY = '002060', 'EAF0F8', 'FFF6DD', 'A8432C', 'F2F2F2'
HF = PatternFill('solid', fgColor=DARK); SF = PatternFill('solid', fgColor=SAND)
IF_ = PatternFill('solid', fgColor=INPUT); GF = PatternFill('solid', fgColor=GREY)
WF = PatternFill('solid', fgColor='F4D9D2'); OKF = PatternFill('solid', fgColor='DCEBDF')
HFONT = Font(bold=True, color='FFFFFF'); TFONT = Font(bold=True, size=16, color=DARK)
EXFONT = Font(italic=True, color='7F7F7F'); BOLD = Font(bold=True, color=DARK)
WR = Alignment(wrap_text=True, vertical='top')
thin = Side(style='thin', color='C8C2B4'); B = Border(top=thin, bottom=thin, left=thin, right=thin)

wb = Workbook()
LISTS = {}


def lists_sheet():
    ws = wb.create_sheet('Lijsten')
    data = {
        'janee': ['ja', 'nee'],
        'janeedeels': ['ja', 'deels', 'nee'],
        'lmh': ['laag', 'middel', 'hoog'],
        'rol_k2': ['Gebruiker', 'Betrokkene', 'Beslisser', 'Leverancier', 'Toezichthouder'],
        'domeinen': ['1. Doel, noodzaak en proportionaliteit', '2. Governance en accountability',
                     '3. Stakeholders, mensenrechten en impact', '4. Data en privacy',
                     '5. Fairness, bias en non-discriminatie', '6. Transparantie, uitlegbaarheid en traceerbaarheid',
                     '7. Menselijke controle, bezwaar en herstel', '8. Veiligheid, security en robuustheid',
                     '9. AI-geletterdheid', '10. Duurzaamheid en bredere impact', '11. Monitoring, audit en verbetering'],
        'methode': ['Gesprek', 'Documentanalyse', 'Test', 'Observatie', 'Data-analyse'],
        'sterkte': ['Sterk', 'Goed', 'Beperkt', 'Zwak'],
        'scanscore': [0, 1, 2, 3, 'onbekend'],
        'score03': [0, 1, 2, 3],
        'kans': [1, 2, 3, 4, 5],
        'klasse': ['Onaanvaardbaar risico', 'Hoog risico', 'Beperkt risico', 'Minimaal risico', 'Twijfel (licht toe)'],
        'rol_eu': ['Aanbieder', 'Gebruiksverantwoordelijke', 'Aanbieder en gebruiksverantwoordelijke'],
        'respons': ['Vermijden', 'Verminderen', 'Delen', 'Accepteren'],
        'prioriteit': ['Hoog', 'Midden', 'Laag'],
        'functie': ['Voorkomen', 'Opsporen', 'Herstellen'],
        'soort_c': ['Techniek', 'Data en model', 'Proces', 'Mens', 'Governance'],
        'kader': ['AI-verordening, art. 4 (AI-geletterdheid)', 'AI-verordening, art. 10 (data)', 'AI-verordening, art. 12 (logging)',
                  'AI-verordening, art. 13 (informatie voor gebruikers)', 'AI-verordening, art. 14 (menselijk toezicht)',
                  'AI-verordening, art. 26 (plichten gebruiksverantwoordelijke)', 'AI-verordening, art. 27 (FRIA)',
                  'AI-verordening, art. 50 (transparantie)', 'AI-verordening, art. 86 (recht op uitleg)',
                  'ISO/IEC 42001, A.2 Beleid', 'ISO/IEC 42001, A.3 Interne organisatie', 'ISO/IEC 42001, A.4 Middelen',
                  'ISO/IEC 42001, A.5 Impactbeoordeling', 'ISO/IEC 42001, A.6 Levenscyclus', 'ISO/IEC 42001, A.7 Data',
                  'ISO/IEC 42001, A.8 Informatie voor belanghebbenden', 'ISO/IEC 42001, A.9 Gebruik', 'ISO/IEC 42001, A.10 Derde partijen',
                  'IEEE CertifAIEd, transparantie', 'IEEE CertifAIEd, verantwoording', 'IEEE CertifAIEd, algoritmische bias',
                  'IEEE CertifAIEd, privacy', 'NIST AI RMF, Govern', 'NIST AI RMF, Map', 'NIST AI RMF, Measure', 'NIST AI RMF, Manage'],
        'inbouw': ['Team in A-AI2', 'Partner', 'Beide'],
        'status_lev': ['Bekend', 'Onbekend: navragen', 'Risico: maatregel nodig'],
        'raci': ['R', 'A', 'C', 'I', 'A+R'],
        'fase': ['Direct', 'Kort', 'Structureel'],
        'soort_m': ['Groepsverschil', 'Proces', 'Mensen', 'Meerwaarde', 'Overig'],
        'oordeel': ['Werkt', 'Werkt deels', 'Werkt niet'],
        'bron_fb': ['Docent (A1)', 'Panel (Design Review)', 'Peergroep', 'Partner', 'Anders'],
        'besluit_fb': ['Overgenomen', 'Deels overgenomen', 'Niet overgenomen'],
    }
    for c, (k, vals) in enumerate(data.items(), 1):
        ws.cell(1, c, k).font = Font(bold=True)
        for r, v in enumerate(vals, 2):
            ws.cell(r, c, v)
        LISTS[k] = f"=Lijsten!${L(c)}$2:${L(c)}${len(vals) + 1}"
    ws.sheet_state = 'hidden'


def dv(ws, key, rng, strict=True):
    d = DataValidation(type='list', formula1=LISTS[key], allow_blank=True)
    if not strict:
        d.showErrorMessage = False
    ws.add_data_validation(d); d.add(rng)


def setup(ws, title, sub, ncols, week=None):
    ws['A1'] = title; ws['A1'].font = TFONT
    ws['A2'] = sub; ws['A2'].alignment = WR; ws['A2'].fill = SF
    ws.merge_cells(start_row=2, start_column=1, end_row=2, end_column=max(ncols, 2))
    ws.row_dimensions[2].height = max(30, 15 * (len(sub) // 150 + 1))
    ws.page_setup.orientation = 'landscape'; ws.page_setup.paperSize = ws.PAPERSIZE_A4
    ws.page_setup.fitToWidth = 1; ws.page_setup.fitToHeight = 0
    ws.sheet_properties.pageSetUpPr.fitToPage = True
    ws.print_options.gridLines = False
    ws.sheet_view.zoomScale = 90


def header(ws, row, cols, widths):
    for i, (c, w) in enumerate(zip(cols, widths), 1):
        x = ws.cell(row, i, c); x.font = HFONT; x.fill = HF; x.border = B
        x.alignment = Alignment(wrap_text=True, vertical='center')
        ws.column_dimensions[L(i)].width = w
    ws.row_dimensions[row].height = 34
    ws.freeze_panes = ws.cell(row + 1, 1)
    ws.print_title_rows = f'{row}:{row}'


def example(ws, row, vals):
    for i, v in enumerate(vals, 1):
        x = ws.cell(row, i, v); x.font = EXFONT; x.fill = GF; x.alignment = WR; x.border = B
    ws.row_dimensions[row].height = 60


def inputs(ws, start, n, ncols, formula_cols=(), height=30):
    for r in range(start, start + n):
        for c in range(1, ncols + 1):
            x = ws.cell(r, c); x.border = B; x.alignment = WR
            if c not in formula_cols:
                x.fill = IF_
            else:
                x.fill = SF
        ws.row_dimensions[r].height = height


def section(ws, row, text, ncols):
    x = ws.cell(row, 1, text); x.font = Font(bold=True, size=12, color=DARK)
    ws.row_dimensions[row].height = 22


def note(ws, row, text, ncols, warn=False):
    x = ws.cell(row, 1, text); x.alignment = WR
    x.font = Font(italic=True, color=WARN if warn else '44504B')
    ws.merge_cells(start_row=row, start_column=1, end_row=row, end_column=ncols)
    ws.row_dimensions[row].height = max(18, 15 * (len(text) // 160 + 1))


lists_sheet()

# ---------------- Start ----------------
ws = wb.active; ws.title = 'Start'
setup(ws, 'A-ET werkboek instrumenten 2026-2027',
      'Dit werkboek bevat de instrumenten van AI & Ethics (A-ET) in één bestand. In de kennispakketten heet het soms de Ethical Dilemma & AI Risk Assessment-tool (blok 1) of de Responsible AI Design & Governance Toolkit (blok 2 en 3): dat zijn de tabbladen van dit werkboek. Gele cellen vul je zelf in. Grijze cursieve rijen zijn voorbeelden: lees ze en overschrijf ze. Lichtblauwe cellen rekent het werkboek zelf uit.', 6)
for c, w in zip('ABCDEF', [30, 34, 14, 22, 40, 10]):
    ws.column_dimensions[c].width = w
r = 4
for lab in ['Groep', 'Oplossing (uit A-AI2)', 'Partnerorganisatie', 'Groepsleden', 'Versie van de oplossing bij A1 (4 februari)', 'Versie van de oplossing bij A2 (11 maart)']:
    ws.cell(r, 1, lab).font = BOLD
    x = ws.cell(r, 2); x.fill = IF_; x.border = B
    ws.merge_cells(start_row=r, start_column=2, end_row=r, end_column=5); r += 1
r += 1
section(ws, r, 'Welk tabblad in welk blok, voor welk hoofdstuk', 6); r += 1
for i, h in enumerate(['Tabblad', 'Instrument', 'Blok · hoofdstuk', 'Toets', 'Waar je het voor gebruikt'], 1):
    x = ws.cell(r, i, h); x.font = HFONT; x.fill = HF; x.border = B
r += 1
plan = [
    ('K1_Scope', 'K1 AI Use Case & Scope Canvas', '1 · H1', 'A1', 'Wat onderzoeken we precies? (Het A3-canvas staat ook als Word-bestand.)'),
    ('K2_Stakeholders', 'K2 Stakeholder & Impact Map', '1 · H2', 'A1', 'Wie wordt geraakt, en wie heeft weinig macht maar veel te verliezen? Eerste helft van de AI-impactbeoordeling.'),
    ('K3_Proces_Data', 'K3 AI Process & Data Map', '1 · H3', 'A1', 'Waar in de keten kan iets misgaan, en welke gegevens gaan naar externe diensten?'),
    ('Bewijsplan', 'Bewijsplan', '1 · H4', 'A1', 'Welk bewijs zoeken we, waar, met welke methode, en wie doet het?'),
    ('K4_Scan', 'K4 snelle scan', '1 · H4', 'A1', 'Eerste score op alle 11 domeinen; kies 3 tot 4 domeinen om diep te onderzoeken.'),
    ('K4_Nulmeting', 'K4 nulmeting met bewijs', '1 · H4', 'A1', 'Normvragen per domein, met score, bewijs en sterkte. Samen met K2: de AI-impactbeoordeling.'),
    ('Dilemma_Log', 'Dilemma\'s verzamelen (hulpmiddel)', '1 · –', 'A1 individueel', 'Verzamel dilemma\'s en spreek af wie welk dilemma uitwerkt. Komt niet in het rapport: elk groepslid werkt één dilemma uit in het K5-canvas (Word-bestand).'),
    ('Risk_Register', 'K6 AI Risk Register', '1 · H5; 2 · H6', 'A1, A2', 'Bovenaan de EU-risicoklasse en rol; alle risico\'s die je vindt, inherent gescoord; de top 5 gaat het rapport in. In blok 2 de respons en het restrisico.'),
    ('Gewenste_situatie', 'K4 gewenste situatie (hulpmiddel)', '2 · H6', 'A2', 'Doelniveau per domein, gap en prioriteit; helpt bij de norm onder elke eis.'),
    ('Design_Requirements', 'K7 deel 1: eisen', '2 · H6', 'A2', 'Van risico naar toetsbare eis.'),
    ('Control_Catalog', 'Voorbeeldmaatregelen', '2', '-', 'Inspiratie, geen boodschappenlijst.'),
    ('Controls', 'K7 deel 1: maatregelen', '2 · H6', 'A2', 'Maatregelen met eigenaar, kolom Kader en (optioneel) hertest.'),
    ('Leverancierscheck', 'K7: leverancierscheck', '2 · H7', 'A2', 'De vier vragen per externe dienst.'),
    ('Human_Oversight', 'K7 deel 2: menselijke controle en bezwaar', '2 · H7', 'A2', 'Controle voor de belangrijkste beslissing, rekensom, bezwaarroute.'),
    ('Governance_RACI', 'K7 deel 2c: RACI en AI-beleidsregel', '2 · H7', 'A2', 'Wie beslist over ethische vragen, precies één A per activiteit; AI-beleidsregel van hoogstens 100 woorden.'),
    ('Verwerkingslijst', 'Bijlage E: verwerkingslijst', '2 en 3 · bijlage E', 'A2', 'Elk feedbackpunt van docent, Design Review en peergroep, met besluit.'),
    ('K8_Monitoring', 'K8 implementatie- en monitoringplan', '3 · H8', 'A2', 'Implementatie, ethische signalen, herbeoordeling, en de vaste regels incidentroute en stopcriterium.'),
    ('Hertest', 'Hertest (optioneel)', '3 · bijlage F', 'A2', 'Per maatregel: werkt, werkt deels of werkt niet. Niet verplicht; telt mee voor excellent.'),
]
for row in plan:
    for i, v in enumerate(row, 1):
        x = ws.cell(r, i, v); x.border = B; x.alignment = WR
    ws.row_dimensions[r].height = 30; r += 1
r += 1
section(ws, r, 'Spelregels', 6); r += 1
for t in ['Gebruik alleen verzonnen persoonsgegevens. Echte klantgegevens van de partner horen nooit in dit werkboek.',
          'Een score zonder bewijs telt niet. Twijfel je tussen twee scores, kies dan de lagere en noteer wat je nog moet uitzoeken.',
          'Kijk voor een volledig uitgewerkt voorbeeld in het voorbeeldrapport ClaimWacht (Tamarinde Zorgverzekeraar, fictief) en in het casusdossier Suribank.',
          'Verwijs waar het kan naar het werk uit A-AI2 (werking, techniek) en A-DG (data, privacyregels) in plaats van het te herhalen.',
          'Lever bij elke inlevering ook de AI-verklaring in (Word-bestand).']:
    note(ws, r, '• ' + t, 6); r += 1

# ---------------- K1 ----------------
ws = wb.create_sheet('K1_Scope')
setup(ws, 'K1 AI Use Case & Scope Canvas (blok 1, hoofdstuk 1)',
      'Vul per veld een korte, concrete beschrijving in. Schrijf apart op wat het systeem maakt, wat er daarna mee gebeurt en wat mensen daarvan merken. Zet altijd zowel gebruikers als betrokkenen. Werkt jullie oplossing met generatieve AI? Beantwoord dan ook de vraag in kolom D.', 6)
header(ws, 4, ['#', 'Veld', 'Vraag', 'Bij generatieve AI', 'Jullie antwoord', 'Voorbeeld Suribank'], [4, 20, 38, 38, 55, 45])
k1 = [
    ('1', 'Organisatie en context', 'Waar speelt dit, en wat voor organisatie is het?', 'Wie is de partner uit A-AI2?', 'Suribank, een fictieve middelgrote bank met kantoren in Paramaribo, Nickerie en Albina'),
    ('2', 'Probleem', 'Welk probleem moet de AI oplossen, en waarom nu?', 'Wat lost de assistent op voor de gebruiker, en wat voor de organisatie?', 'Een kredietaanvraag duurt twee weken; klanten haken af, en medewerkers beoordelen vergelijkbare aanvragen verschillend'),
    ('3', 'AI-toepassing', 'Wat doet de AI precies: herkennen, voorspellen, aanbevelen of maken?', 'Wat maakt het: antwoorden, samenvattingen, teksten of voorstellen?', 'Voorspelt per aanvraag de kans dat de lening wordt terugbetaald'),
    ('4', 'Soort AI', 'Regels, machine learning of generatieve AI? Zelf gebouwd of van een leverancier?', 'Welk taalmodel of welke dienst, en welke instructies en documenten krijgt het mee?', 'Machine learning (logistische regressie), gebouwd door een extern bureau op aanvragen uit 2019 tot 2025'),
    ('5', 'Input', 'Welke gegevens gaan erin, en van wie?', 'Wat typt de gebruiker, en gaan die gegevens naar een externe dienst?', 'Leeftijd, geslacht, district, soort werk, inkomen, schulden, bedrag, looptijd, betalingsverleden en klantduur'),
    ('6', 'Output', 'Wat komt eruit?', 'Weet de gebruiker dat het antwoord door AI is gemaakt?', 'Een kans van 0 tot 100% en een advies: goedkeuren boven 60%, anders afwijzen'),
    ('7', 'Beslissing', 'Wat gebeurt er met de output, en wie beslist?', 'Wat doet de gebruiker met het antwoord, en leest er een mens mee?', 'Onder SRD 50.000 wordt het advies automatisch overgenomen; daarboven beslist een kredietmedewerker'),
    ('8', 'Gebruikers', 'Wie werkt met het systeem?', 'Wie chat of werkt met de assistent?', 'Kredietmedewerkers en het hoofd kredietverlening'),
    ('9', 'Betrokkenen', 'Over wie gaat het, en wie merkt de gevolgen?', 'Over wie gaat het antwoord, ook als die persoon niet zelf chat?', 'Aanvragers, vooral uit het binnenland en met informeel werk, en hun gezinnen'),
    ('10', 'Doel en succes', 'Wat moet beter worden, en hoe meet je dat?', 'Hoe weet je dat de antwoorden goed genoeg zijn, en voor wie?', 'Beslissing binnen twee dagen, zonder meer wanbetaling dan nu'),
    ('11', 'Afbakening', 'Wat onderzoeken jullie wel, en wat bewust niet?', 'Welke vragen of taken mag de assistent niet doen?', 'Wel: beoordeling van consumptief krediet. Niet: hypotheken, zakelijk krediet en incasso'),
    ('12', 'Casus en bewijs', 'Welke casus, en welke bronnen en mensen gebruiken jullie?', 'Welke documentatie uit A-AI2 en A-DG, en welke tests?', 'Oefencasus met het casusdossier: beleidsnotitie, modeldocumentatie, interviewverslagen en testresultaten'),
    ('13', 'Eerste zorgen', 'Welke drie ethische zorgen zien jullie nu al, elk in één zin?', 'Denk aan de vier vragen uit clip 4.', 'Aanvragers uit het binnenland worden vaker afgewezen. Bij kleine bedragen kijkt geen mens mee en krijgt niemand uitleg. Bij informeel werk ontbreekt vaker het inkomen'),
]
for i, row in enumerate(k1, 5):
    for c, v in enumerate(row[:4], 1):
        x = ws.cell(i, c, v); x.alignment = WR; x.border = B
    ws.cell(i, 2).font = BOLD
    x = ws.cell(i, 5); x.fill = IF_; x.border = B; x.alignment = WR
    x = ws.cell(i, 6, row[4]); x.font = EXFONT; x.fill = GF; x.border = B; x.alignment = WR
    ws.row_dimensions[i].height = 48
note(ws, 19, 'Teamafspraken (rollen, overleg, wie levert wat) zet je onder het canvas in het Word-bestand of in jullie teamdocument.', 6)

# ---------------- K2 ----------------
ws = wb.create_sheet('K2_Stakeholders')
setup(ws, 'K2 Stakeholder & Impact Map (blok 1, hoofdstuk 2)',
      'Eén rij per stakeholder. Splits groepen als ze verschillend geraakt worden. Kolom J signaleert wie weinig macht maar veel te verliezen heeft. K2 is samen met de nulmeting de AI-impactbeoordeling: wat de AI-verordening een FRIA noemt (artikel 27) en ISO/IEC 42005 een impactbeoordeling.', 10)
cols = ['Stakeholder', 'Rol', 'Belang', 'Mogelijke baat', 'Mogelijke schade', 'Macht', 'Kwetsbaarheid', 'Betrokken?', 'Hoe gehoord (of waarom niet)', 'Signaal']
header(ws, 4, cols, [26, 15, 26, 26, 30, 10, 13, 11, 28, 26])
example(ws, 5, ['Aanvragers uit het binnenland met informeel werk', 'Betrokkene', 'Snel en eerlijk krediet', 'Sneller een besluit', 'Vaker onterecht afgewezen; uitwijken naar informele geldschieters', 'laag', 'hoog', 'nee', 'Nog niet: gesprek met twee klanten in Albina gepland', 'Extra aandacht: weinig macht, veel te verliezen'])
inputs(ws, 6, 15, 10, formula_cols=(10,))
for r in range(6, 21):
    ws.cell(r, 10, f'=IF(AND(F{r}="laag",G{r}="hoog"),"Extra aandacht: weinig macht, veel te verliezen",IF(AND(G{r}="hoog",H{r}="nee"),"Kwetsbaar en niet gehoord",""))')
dv(ws, 'rol_k2', 'B6:B20'); dv(ws, 'lmh', 'F6:G20'); dv(ws, 'janeedeels', 'H6:H20')
ws.conditional_formatting.add('J6:J20', FormulaRule(formula=['LEN(J6)>0'], fill=WF, font=Font(color=WARN, bold=True)))

# ---------------- K3 ----------------
ws = wb.create_sheet('K3_Proces_Data')
setup(ws, 'K3 AI Process & Data Map (blok 1, hoofdstuk 3)',
      'Eén rij per stap in de keten, van aanvraag of vraag tot terugkoppeling. Markeer elke externe dienst (n8n, taalmodel-API, vectordatabase, hosting): welke gegevens gaan erheen, en waar staan ze? Die rijen gebruik je in blok 2 voor de leverancierscheck.', 10)
cols = ['Stap', 'Wat gebeurt er', 'Gegevens en wie', 'Wat kan misgaan', 'Risico (soort)', 'Mens in de lus?', 'Externe dienst?', 'Welke dienst', 'Welke gegevens gaan erheen', 'Waar staan ze (land, omgeving)']
header(ws, 4, cols, [18, 30, 28, 28, 18, 16, 11, 22, 28, 24])
example(ws, 5, ['2. Antwoord opstellen (orderagent Frisco)', 'De agent zoekt in de productcatalogus en stelt een offerte op', 'Klantvraag, naam en adres; klant en agent', 'Verzonnen prijs of levertijd', 'Overtuigend fout', 'Nee, onder SRD 10.000', 'ja', 'Taalmodel-API, vectordatabase, n8n', 'Klantvraag met naam en adres; catalogus', 'Vectordatabase in een datacenter in de VS; n8n bij de partner'])
inputs(ws, 6, 12, 10)
dv(ws, 'janee', 'G6:G17')
ws.conditional_formatting.add('H6:J17', FormulaRule(formula=['AND($G6="ja",LEN(H6)=0)'], fill=WF))
note(ws, 19, 'Risicosoorten om uit te kiezen: meetbias, historische bias, labelbias, representatiebias, aggregatiebias, automation bias, privacy, geen transparantie, geen herstel, drift, overtuigend fout. Rood in H tot en met J: externe dienst aangevinkt, maar nog niet beschreven.', 10)

# ---------------- Bewijsplan ----------------
ws = wb.create_sheet('Bewijsplan')
setup(ws, 'Bewijsplan en evidence cards (blok 1)',
      'Plan per domein welk bewijs jullie zoeken. Veel bewijs ligt al bij A-AI2 en A-DG: gebruik het, en kijk het zelf na. Rechts staat hoe sterk bewijs is.', 9)
cols = ['Domein', 'Wat willen we weten?', 'Bron', 'Methode', 'Wie', 'Wanneer', 'Gevonden (kort)', 'Bewijssterkte', 'Evidence card nr.']
header(ws, 4, cols, [30, 36, 26, 16, 14, 12, 34, 13, 11])
example(ws, 5, ['2. Governance en accountability', 'Wie is eigenaar van de oplossing, en wie mag die stopzetten?', 'Partner uit A-AI2', 'Gesprek', 'Student A', '20 januari', '"Ik neem aan de directie" (D7); geen document', 'Beperkt', 'EC-04'])
inputs(ws, 6, 15, 9)
dv(ws, 'domeinen', 'A6:A20'); dv(ws, 'methode', 'D6:D20', strict=False); dv(ws, 'sterkte', 'H6:H20')
ws.column_dimensions['K'].width = 12; ws.column_dimensions['L'].width = 60
ws['K4'] = 'Niveau'; ws['L4'] = 'Voorbeelden'
for c in ('K4', 'L4'):
    ws[c].font = HFONT; ws[c].fill = HF
for i, (a, b) in enumerate([('Sterk', 'Testresultaten, systeemlogs, goedgekeurde documenten, meerdere bronnen die hetzelfde zeggen'),
                            ('Goed', 'Een gesprek plus een document dat het bevestigt'),
                            ('Beperkt', 'Eén gesprek of één onvolledig document'),
                            ('Zwak', 'Een aanname of indruk zonder bron')], 5):
    ws.cell(i, 11, a).border = B; x = ws.cell(i, 12, b); x.border = B; x.alignment = WR

# ---------------- K4 scan ----------------
ws = wb.create_sheet('K4_Scan')
setup(ws, 'K4 AI Ethics & Risk Maturity Scan: snelle scan (blok 1, hoofdstuk 4)',
      'Geef alle 11 domeinen een eerste score en kies 3 tot 4 domeinen om diep te onderzoeken. Het is een eerste beeld, geen eindoordeel. Gebruik bij domein 5 en 6 de checklist uit IEEE CertifAIEd hieronder.', 6)
cols = ['Domein', 'Eerste score (0-3 of onbekend)', 'Waarop is die gebaseerd?', 'Welk bewijs is nog nodig?', 'Diep onderzoeken?', '']
header(ws, 4, cols[:5], [42, 14, 42, 42, 12])
example(ws, 5, ['Voorbeeld: 7. Menselijke controle, bezwaar en herstel', '1', 'Werkinstructie staat afwijken toe, maar medewerkers doen het bijna nooit (gesprek Albina)', 'Cijfers over afwijkingen; de afwijzingsbrief', 'ja'])
doms = ['1. Doel, noodzaak en proportionaliteit', '2. Governance en accountability', '3. Stakeholders, mensenrechten en impact', '4. Data en privacy',
        '5. Fairness, bias en non-discriminatie', '6. Transparantie, uitlegbaarheid en traceerbaarheid', '7. Menselijke controle, bezwaar en herstel',
        '8. Veiligheid, security en robuustheid', '9. AI-geletterdheid', '10. Duurzaamheid en bredere impact', '11. Monitoring, audit en verbetering']
inputs(ws, 6, 11, 5, formula_cols=(1,))
for i, d in enumerate(doms, 6):
    ws.cell(i, 1, d).font = BOLD
dv(ws, 'scanscore', 'B6:B16'); dv(ws, 'janee', 'E6:E16')
ws['A18'] = 'Aantal domeinen om diep te onderzoeken'; ws['A18'].font = BOLD
ws['B18'] = '=COUNTIF(E6:E16,"ja")'; ws['B18'].fill = SF
ws['C18'] = '=IF(B18=0,"",IF(AND(B18>=3,B18<=4),"Goed: 3 tot 4 domeinen","Kies 3 tot 4 domeinen"))'
ws.conditional_formatting.add('C18', FormulaRule(formula=['AND(B18>0,OR(B18<4,B18>6))'], font=Font(color=WARN, bold=True)))
r = 20
section(ws, r, 'Schaal', 5); r += 1
for a, b, c in [('0', 'Niet aanwezig of onbekend', 'Niemand weet ervan, of er is geen enkel spoor van'),
                ('1', 'Ad hoc', 'Er gebeurt iets, maar informeel en afhankelijk van personen'),
                ('2', 'Gedeeltelijk beheerst', 'Er zijn afspraken of maatregelen, maar de uitvoering of het bewijs is onvolledig'),
                ('3', 'Aantoonbaar beheerst', 'Er is beleid of een proces, verantwoordelijkheden zijn duidelijk, de uitvoering is aan te tonen en wordt gecontroleerd')]:
    for i, v in enumerate([a, b, c], 1):
        x = ws.cell(r, i, v); x.border = B; x.alignment = WR
    ws.merge_cells(start_row=r, start_column=3, end_row=r, end_column=4); ws.row_dimensions[r].height = 30; r += 1
r += 1
section(ws, r, 'Checklist uit IEEE CertifAIEd (kaderclip B): drivers en inhibitors', 5); r += 1
for i, h in enumerate(['Domein', 'Ja / deels / nee', 'Vraag', 'Toelichting of bewijs'], 1):
    x = ws.cell(r, i, h); x.font = HFONT; x.fill = HF; x.border = B
r += 1; c0 = r
chk = [('6 (driver)', 'Weet de gebruiker meteen dat die met AI te maken heeft?'),
       ('6 (driver)', 'Is de werking helder beschreven voor wie ermee werkt?'),
       ('6 (driver)', 'Kan de gebruiker ingrijpen, feedback geven of een alternatief kiezen?'),
       ('6 (inhibitor)', 'Wordt informatie achtergehouden uit angst voor aansprakelijkheid?'),
       ('6 (inhibitor)', 'Wordt informatie achtergehouden om een bedrijfsgeheim te beschermen, of wordt gedrag verhuld?'),
       ('5 (driver)', 'Is het gebruik of weglaten van beschermde kenmerken (zoals geslacht of district) onderbouwd?'),
       ('5 (driver)', 'Wordt het gedrag per groep gevolgd, ook na livegang?'),
       ('5 (driver)', 'Kan de organisatie bias corrigeren als die opduikt?'),
       ('5 (inhibitor)', 'Is het proces zo onduidelijk (data, bronnen) dat niemand bias kan meten?')]
for d, q in chk:
    ws.cell(r, 1, d).border = B
    x = ws.cell(r, 2); x.fill = IF_; x.border = B
    x = ws.cell(r, 3, q); x.alignment = WR; x.border = B
    x = ws.cell(r, 4); x.fill = IF_; x.border = B; x.alignment = WR
    ws.row_dimensions[r].height = 30; r += 1
dv(ws, 'janeedeels', f'B{c0}:B{r - 1}')
note(ws, r + 1, 'Let op bij een inhibitor: "ja" is hier slecht nieuws. Zo werkt ook een certificering: per doel bewijs, en een score die zegt hoe aantoonbaar iets geregeld is.', 5)

# ---------------- K4 nulmeting ----------------
ws = wb.create_sheet('K4_Nulmeting')
setup(ws, 'K4 nulmeting met bewijs (blok 1, hoofdstuk 4)',
      'Werk de 3 tot 4 domeinen uit die je in de snelle scan koos. Score per normvraag 0 tot 3, met bewijs en bron. Een score zonder bewijs telt niet (rood). Score wat er nu is: wat de groep in A-AI2 nog gaat bouwen, hoort bij de gap. Onderaan geef je per domein het domeinoordeel en de belangrijkste gap.', 7)
cols = ['Nr', 'Normvraag', 'Voorbeeld van bewijs voor score 3', 'Score 0-3', 'Bewijs en bron', 'Sterkte', 'Diep onderzocht (uit scan)']
header(ws, 4, cols, [6, 48, 34, 9, 50, 11, 12])
example(ws, 5, ['7.2', 'Hebben medewerkers in de praktijk tijd, informatie en bevoegdheid om af te wijken?', 'Cijfers over afwijkingen, observatie van het werk', '1',
                '15 minuten per dossier (D3); medewerker Albina: "Dat kan ik niet uitleggen, want ik zie alleen een getal" (D8); afwijking bij 4 van 211 aanvragen in oktober (D11)', 'Sterk', 'ja'])
norm = {
    1: [('1.1', 'Is het doel van de toepassing schriftelijk vastgelegd, inclusief voor wie het een probleem oplost?', 'Goedgekeurde business case of projectopdracht'),
        ('1.2', 'Is onderzocht of het doel ook zonder AI of met minder ingrijpende middelen haalbaar is?', 'Vastgelegde vergelijking van alternatieven'),
        ('1.3', 'Is de inzet in verhouding tot de mogelijke schade voor betrokkenen?', 'Afweging in een besluitstuk, met de zwaarste schade benoemd'),
        ('1.4', 'Is vastgelegd waarvoor de toepassing níet gebruikt mag worden?', 'Gebruiksbeperking in werkinstructie of beleid')],
    2: [('2.1', 'Is er één persoon of functie eindverantwoordelijk voor de toepassing?', 'Naam en functie in een besluit of RACI'),
        ('2.2', 'Zijn rollen en bevoegdheden rond het systeem beschreven (bouwen, gebruiken, wijzigen, stoppen)?', 'RACI-matrix of rolbeschrijving'),
        ('2.3', 'Is er een formeel besluit genomen over de inzet, met voorwaarden?', 'Besluitverslag van directie of commissie'),
        ('2.4', 'Zijn afspraken met leveranciers vastgelegd over verantwoordelijkheid, toegang en informatie?', 'Contract met auditrecht en informatieplicht')],
    3: [('3.1', 'Zijn alle groepen in kaart gebracht die door de toepassing geraakt worden, ook indirect?', 'Stakeholderanalyse met indirecte groepen'),
        ('3.2', 'Zijn kwetsbare groepen benoemd, en is nagegaan hoe zij anders geraakt worden?', 'Analyse per groep, bijvoorbeeld per regio'),
        ('3.3', 'Zijn geraakte groepen zelf gehoord?', 'Verslag van gesprekken of klantpanel'),
        ('3.4', 'Is een impact- of mensenrechtentoets uitgevoerd vóór de invoering?', 'Ingevulde impact assessment met datum')],
    4: [('4.1', 'Is bekend welke persoonsgegevens het systeem gebruikt, en waarom elk gegeven nodig is?', 'Dataregister met doel per veld'),
        ('4.2', 'Worden betrokkenen begrijpelijk geïnformeerd over het gebruik van hun gegevens door het systeem?', 'Actuele privacyverklaring die het systeem noemt'),
        ('4.3', 'Zijn bewaartermijnen, toegang en doorgifte aan derden geregeld?', 'Bewaarbeleid, toegangslijst, verwerkersovereenkomst'),
        ('4.4', 'Is de kwaliteit en herkomst van de trainingsdata gecontroleerd?', 'Datakwaliteitsrapport, beschrijving van de herkomst')],
    5: [('5.1', 'Is vastgelegd welke groepen niet benadeeld mogen worden, en wat "eerlijk" hier betekent?', 'Fairnessdefinitie in ontwerp of beleid'),
        ('5.2', 'Is getest of fouten van het systeem ongelijk verdeeld zijn over groepen?', 'Testrapport met foutpercentages per groep'),
        ('5.3', 'Is nagegaan of variabelen indirect voor een beschermd kenmerk staan?', 'Analyse van proxyvariabelen, zoals woonplaats'),
        ('5.4', 'Is er een grens afgesproken waarboven een verschil tussen groepen tot actie leidt?', 'Drempelwaarde met eigenaar en actie')],
    6: [('6.1', 'Weten betrokkenen dat er een AI-systeem bij het besluit betrokken is?', 'Vermelding in brief, website of formulier'),
        ('6.2', 'Kan aan een individu worden uitgelegd waarom het besluit zo uitviel?', 'Voorbeeld van een uitleg per besluit'),
        ('6.3', 'Is het systeem gedocumenteerd: model, data, prestaties, beperkingen?', 'Modeldocumentatie of factsheet met beperkingen'),
        ('6.4', 'Wordt per besluit vastgelegd welke modelversie en invoer zijn gebruikt?', 'Logbestand of audittrail')],
    7: [('7.1', 'Is beschreven wanneer en hoe een mens het besluit van het systeem beoordeelt of overneemt?', 'Werkinstructie met criteria voor menselijke beoordeling'),
        ('7.2', 'Hebben medewerkers in de praktijk tijd, informatie en bevoegdheid om af te wijken?', 'Cijfers over afwijkingen, observatie van het werk'),
        ('7.3', 'Kunnen betrokkenen bezwaar maken, en weten ze hoe?', 'Bezwaarprocedure in de besluitbrief'),
        ('7.4', 'Wordt een onterecht besluit hersteld, en wordt daarvan geleerd?', 'Hersteldossiers en aanpassingen naar aanleiding daarvan')],
    8: [('8.1', 'Is de toegang tot het systeem en de data beveiligd?', 'Toegangsbeleid, recente securitytest'),
        ('8.2', 'Is getest hoe het systeem reageert op ontbrekende, foute of ongewone invoer?', 'Testresultaten met randgevallen'),
        ('8.3', 'Is er een terugvaloptie als het systeem uitvalt of onbetrouwbaar blijkt?', 'Noodprocedure, getest'),
        ('8.4', 'Is er een procedure voor incidenten, inclusief melden en stoppen?', 'Incidentprocedure en incidentregister')],
    9: [('9.1', 'Weten gebruikers wat het systeem wel en niet kan?', 'Training of handleiding met beperkingen'),
        ('9.2', 'Herkennen gebruikers wanneer ze het systeem niet moeten volgen?', 'Casusoefening of voorbeelden in de training'),
        ('9.3', 'Begrijpt het management genoeg om goede besluiten over het systeem te nemen?', 'Briefing of sessie voor het management'),
        ('9.4', 'Wordt de kennis bijgehouden bij nieuwe medewerkers en bij wijzigingen?', 'Inwerkprogramma, trainingsregistratie')],
    10: [('10.1', 'Is nagegaan wat de toepassing betekent voor werk en rollen van medewerkers?', 'Analyse van effecten op werk, met afspraken'),
         ('10.2', 'Is nagegaan of de toepassing ongelijkheid of afhankelijkheid in de samenleving versterkt?', 'Analyse van maatschappelijke effecten'),
         ('10.3', 'Is het energie- en middelengebruik bekend en afgewogen?', 'Gegevens van leverancier of eigen meting'),
         ('10.4', 'Is de afhankelijkheid van een leverancier of buitenlandse infrastructuur afgewogen?', 'Exit-plan, afweging van de hostinglocatie')],
    11: [('11.1', 'Worden prestaties van het systeem na invoering gemeten, ook per groep?', 'Maandrapport met indicatoren per groep'),
         ('11.2', 'Zijn er signalen afgesproken die tot een herbeoordeling leiden?', 'Lijst met triggers, zoals stijgende klachten'),
         ('11.3', 'Wordt het systeem periodiek onafhankelijk getoetst?', 'Auditrapport of reviewverslag'),
         ('11.4', 'Worden klachten en incidenten gebruikt om het systeem te verbeteren?', 'Verbeterlog met acties en datum')],
}
r = 6; score_rows = {}
for d in range(1, 12):
    x = ws.cell(r, 1); x.font = HFONT; x.fill = PatternFill('solid', fgColor='2E5597')
    x = ws.cell(r, 2, doms[d - 1]); x.font = HFONT; x.fill = PatternFill('solid', fgColor='2E5597')
    for c in range(3, 8):
        ws.cell(r, c).fill = PatternFill('solid', fgColor='2E5597')
    ws.cell(r, 7, f'=IF(INDEX(K4_Scan!$E$6:$E$16,{d})="","",INDEX(K4_Scan!$E$6:$E$16,{d}))').font = HFONT
    r += 1; first = r
    for nr, q, ev in norm[d]:
        ws.cell(r, 1, nr).border = B
        x = ws.cell(r, 2, q); x.alignment = WR; x.border = B
        x = ws.cell(r, 3, ev); x.alignment = WR; x.border = B; x.font = Font(color='44504B')
        for c in (4, 5, 6):
            x = ws.cell(r, c); x.fill = IF_; x.border = B; x.alignment = WR
        ws.row_dimensions[r].height = 36; r += 1
    score_rows[d] = (first, r - 1)
dv(ws, 'score03', f'D7:D{r}'); dv(ws, 'sterkte', f'F7:F{r}')
ws.conditional_formatting.add(f'E7:E{r}', FormulaRule(formula=['AND(LEN($D7)>0,LEN($E7)=0)'], fill=WF))
r += 1
section(ws, r, 'Domeinoordeel en belangrijkste gap', 7); r += 1
sum_hdr = r
for i, h in enumerate(['Nr', 'Domein', 'Laagste normscore', 'Domeinoordeel (0-3)', 'Waarom deze score, in 1 tot 3 zinnen', 'Belangrijkste gap', ''], 1):
    if h:
        x = ws.cell(r, i, h); x.font = HFONT; x.fill = HF; x.border = B; x.alignment = Alignment(wrap_text=True)
r += 1; sum_first = r
for d in range(1, 12):
    a, b = score_rows[d]
    ws.cell(r, 1, d).border = B
    x = ws.cell(r, 2, doms[d - 1]); x.border = B; x.alignment = WR
    x = ws.cell(r, 3, f'=IF(COUNT(D{a}:D{b})=0,"",MIN(D{a}:D{b}))'); x.fill = SF; x.border = B
    for c in (4, 5, 6):
        x = ws.cell(r, c); x.fill = IF_; x.border = B; x.alignment = WR
    ws.row_dimensions[r].height = 36; r += 1
dv(ws, 'scanscore', f'D{sum_first}:D{r - 1}')
note(ws, r + 1, 'Het domeinoordeel is jullie oordeel; de laagste normscore helpt als richting. Voor domeinen die je niet diep onderzocht, neem je de score uit de snelle scan over. Samen met K2 is dit de AI-impactbeoordeling.', 7)
NUL_SUM = (sum_first, r - 1)

# ---------------- Dilemma_Log ----------------
ws = wb.create_sheet('Dilemma_Log')
setup(ws, 'Dilemma\'s verzamelen (blok 1, hulpmiddel; komt niet in het rapport)',
      'Verzamel als groep dilemma\'s en spreek af wie welk dilemma uitwerkt in het individuele K5-canvas: iedereen een ander. Schrijf elk dilemma elk als beslisvraag met twee waarden die allebei zwaar wegen. De lenskolommen mogen kort: de diepte zit in het Dilemma Canvas (individueel, Word-bestand). Noem bij elke lens ook de theorie erachter.', 17)
cols = ['ID', 'Korte titel', 'Beslisvraag', 'Belangrijkste stakeholders', 'Waarde A', 'Waarde B', 'Feiten en bewijs',
        'Lens gevolgen (utilitarisme)', 'Lens rechten en plichten (deontologie)', 'Lens rechtvaardigheid (Rawls)', 'Lens professionele integriteit (deugdethiek, beroepscodes)',
        'Alternatieven', 'Voorlopig oordeel', 'Voorwaarden', 'Onopgeloste spanning', 'Gelinkte risico\'s', 'Bron']
header(ws, 4, cols, [7, 18, 32, 22, 16, 16, 28, 24, 24, 24, 24, 26, 24, 22, 22, 12, 14])
example(ws, 5, ['D-01', 'Snel of persoonlijk', 'Moet Suribank kleine aanvragen automatisch laten beslissen, of elke afwijzing door een medewerker laten bekijken?', 'Aanvragers uit het binnenland, kredietmedewerkers, directie', 'Efficiëntie', 'Gelijke behandeling en gehoord worden',
                'Albina 63% afwijzing (D11); 4 van 211 afwijkingen (D11)', 'Snel voor velen, maar de fouten vallen bij één groep', 'Wie wordt afgewezen, heeft recht op uitleg en bezwaar', 'De minst bevoordeelde groep draagt de last', 'Een goede bankier kijkt naar de mens achter de aanvraag',
                'A: alles automatisch. B: alles met de hand. C: afwijzingen langs een medewerker', 'Optie C', 'Capaciteit voor ongeveer 85 uur per maand', 'Langere doorlooptijd bij afwijzingen', 'R-01, R-04', 'D3, D8, D11'])
inputs(ws, 6, 8, 17)
ws['A15'] = 'Aantal dilemma\'s'; ws['A15'].font = BOLD
ws['C15'] = '=COUNTA(C6:C13)'; ws['C15'].fill = SF
ws['D15'] = '=IF(C15>=3,"Goed: minstens drie","Nog niet: minstens drie dilemma\'s")'
ws.conditional_formatting.add('D15', FormulaRule(formula=['C15<3'], font=Font(color=WARN, bold=True)))

# ---------------- Risk_Register ----------------
ws = wb.create_sheet('Risk_Register')
setup(ws, 'K6 AI Risk Register (blok 1, hoofdstuk 5; restrisico in blok 2, hoofdstuk 6)',
      'Eerst bovenaan de regel EU-risicoklasse en rol. Daarna de risico\'s die jullie vinden, inherent gescoord; de 5 belangrijkste gaan het rapport in. Inherent betekent: de situatie zoals die nu is. Kans 1 tot 5 (zeldzaam, onwaarschijnlijk, mogelijk, waarschijnlijk, bijna zeker); impact 1 tot 5 (beperkt, matig, ernstig, zeer ernstig, kritiek) op vier dimensies. Het werkboek rekent de totale impact (de hoogste van de vier), de score, de band en de escalatie uit. De kolommen voor respons, restrisico en eigenaar vul je pas in week 6 in.', 29)
section(ws, 4, 'EU-risicoklasse en rol (AI-verordening, ter vergelijking: de verordening geldt niet in Suriname)', 8)
for i, h in enumerate(['Veld', 'Wat je invult', 'Jullie antwoord', 'Voorbeeld Suribank', 'Voorbeeld orderagent'], 1):
    x = ws.cell(5, i, h); x.font = HFONT; x.fill = HF; x.border = B
eu = [('Klasse', 'Onaanvaardbaar, hoog, beperkt of minimaal risico', 'Hoog risico', 'Beperkt risico'),
      ('Onderbouwing', 'Het artikel of de bijlage, in één zin', 'Bijlage III, punt 5b: beoordeling van de kredietwaardigheid van natuurlijke personen', 'Artikel 50: een systeem dat met mensen praat, moet melden dat het AI is'),
      ('Rol van de partner', 'Aanbieder, gebruiksverantwoordelijke of beide', 'Gebruiksverantwoordelijke: de bank koopt het model bij een leverancier, die aanbieder is. De bank moet een FRIA doen (artikel 27)', 'Aanbieder én gebruiksverantwoordelijke: het bedrijf laat de agent bouwen en zet hem onder eigen naam in'),
      ('Twijfel of toelichting', 'Tussen welke klassen twijfel je, en waarom? De klasse is een ondergrens: ook beperkt risico kan iemand ernstig raken', '', '')]
for i, (a, b, c, d) in enumerate(eu, 6):
    ws.cell(i, 1, a).font = BOLD; ws.cell(i, 1).border = B
    x = ws.cell(i, 2, b); x.alignment = WR; x.border = B
    x = ws.cell(i, 3); x.fill = IF_; x.border = B; x.alignment = WR
    for col, v in ((4, c), (5, d)):
        x = ws.cell(i, col, v); x.font = EXFONT; x.fill = GF; x.border = B; x.alignment = WR
    ws.row_dimensions[i].height = 45
dv(ws, 'klasse', 'C6'); dv(ws, 'rol_eu', 'C8')
H = 11
cols = ['ID', 'Gelinkt dilemma', 'Maturitydomein', 'Bron van het risico', 'Oorzaak', 'Gebeurtenis', 'Gevolg', 'Getroffen stakeholders', 'Geraakte waarden of rechten', 'Bestaande controls',
        'Kans (1-5)', 'Impact individu', 'Impact groep of samenleving', 'Impact rechten en waardigheid', 'Impact organisatie',
        'Kwetsbare groep?', 'Onomkeerbaar?', 'Bezwaarmogelijkheid ontbreekt?', 'Bewijs en onzekerheid',
        'Totale impact', 'Score', 'Band', 'Escalatie',
        'Risicorespons (blok 2)', 'Restkans', 'Restimpact', 'Restscore', 'Restband', 'Eigenaar']
header(ws, H, cols, [7, 9, 22, 18, 24, 24, 24, 20, 18, 20, 8, 9, 9, 9, 9, 10, 10, 11, 26, 9, 8, 11, 12, 14, 8, 8, 8, 11, 16])
ws.freeze_panes = ws.cell(H + 1, 2)
example(ws, H + 1, ['R-03', 'D-01', '7. Menselijke controle, bezwaar en herstel', 'Afwijzingsbrief en proces', 'De brief bevat geen reden, geen vermelding van het model en geen bezwaarroute',
                    'Klanten kunnen een onterecht besluit niet begrijpen of aanvechten', 'Fouten blijven onhersteld', 'Afgewezen aanvragers', 'Recht op uitleg en herstel', 'Geen',
                    5, 3, 3, 3, 3, 'nee', 'nee', 'ja', 'D2, D4, D7, D9, klacht 3; klachten van 9 naar 23', 3, 15, 'Very high', 'Ja', 'Verminderen', 2, 2, 4, 'Low', 'Hoofd kredietverlening'])
F0, F1 = H + 2, H + 13
inputs(ws, F0, 12, 29, formula_cols=(20, 21, 22, 23, 27, 28))
band = lambda s: (f'IF({s}="","",IF({s}>=20,"Critical",IF({s}>=15,"Very high",IF({s}>=10,"High",IF({s}>=5,"Moderate","Low")))))')
for r in range(F0, F1 + 1):
    ws.cell(r, 20, f'=IF(COUNT(L{r}:O{r})=0,"",MAX(L{r}:O{r}))')
    ws.cell(r, 21, f'=IF(OR(K{r}="",T{r}=""),"",K{r}*T{r})')
    ws.cell(r, 22, '=' + band(f'U{r}'))
    ws.cell(r, 23, f'=IF(T{r}="","",IF(OR(N{r}>=4,Q{r}="ja",AND(P{r}="ja",T{r}>=4),AND(R{r}="ja",T{r}>=3)),"Ja","Nee"))')
    ws.cell(r, 27, f'=IF(OR(Y{r}="",Z{r}=""),"",Y{r}*Z{r})')
    ws.cell(r, 28, '=' + band(f'AA{r}'))
dv(ws, 'domeinen', f'C{F0}:C{F1}'); dv(ws, 'kans', f'K{F0}:O{F1}'); dv(ws, 'janee', f'P{F0}:R{F1}')
dv(ws, 'respons', f'X{F0}:X{F1}'); dv(ws, 'kans', f'Y{F0}:Z{F1}')
for col in ('V', 'AB'):
    rng = f'{col}{F0}:{col}{F1}'
    ws.conditional_formatting.add(rng, FormulaRule(formula=[f'OR({col}{F0}="Critical",{col}{F0}="Very high")'], fill=PatternFill('solid', fgColor='E8A598'), font=Font(bold=True)))
    ws.conditional_formatting.add(rng, FormulaRule(formula=[f'{col}{F0}="High"'], fill=PatternFill('solid', fgColor='F5C98A')))
    ws.conditional_formatting.add(rng, FormulaRule(formula=[f'{col}{F0}="Moderate"'], fill=PatternFill('solid', fgColor='FFF0B3')))
ws.conditional_formatting.add(f'W{F0}:W{F1}', FormulaRule(formula=[f'W{F0}="Ja"'], fill=WF, font=Font(color=WARN, bold=True)))
note(ws, F1 + 2, 'Banden: 1 tot 4 Low, 5 tot 9 Moderate, 10 tot 14 High, 15 tot 19 Very high, 20 tot 25 Critical. Escaleren los van de score als: impact op rechten 4 of hoger; de schade onomkeerbaar is; een kwetsbare groep geraakt wordt met een impact van 4 of hoger; of er geen bezwaarmogelijkheid is en de impact 3 of hoger is. Is de onzekerheid groot, noteer dan welk aanvullend onderzoek nodig is.', 20)
note(ws, F1 + 3, 'Schrijf het volledige risico als: doordat [oorzaak] kan [gebeurtenis], met als gevolg [schade] voor [wie]. In het rapport komt een korte tabel; de volledige formulering staat in de bijlage.', 20)
ws['A' + str(F1 + 5)] = 'Aantal risico\'s'; ws['A' + str(F1 + 5)].font = BOLD
ws['C' + str(F1 + 5)] = f'=COUNTA(A{F0}:A{F1})'; ws['C' + str(F1 + 5)].fill = SF
ws['D' + str(F1 + 5)] = f'=IF(C{F1 + 5}=0,"",IF(C{F1 + 5}>=5,"Goed: kies de top 5 voor het rapport","Zoek minstens 5 risico\'s"))'
RR = (F0, F1)

# ---------------- Gewenste situatie ----------------
ws = wb.create_sheet('Gewenste_situatie')
setup(ws, 'K4 gewenste situatie per domein (blok 2, hulpmiddel bij hoofdstuk 6)',
      'Bepaal per domein het doelniveau op basis van een norm en proportionaliteit: doel 3 waar het risico het vraagt, niet overal. Het werkboek neemt het huidige niveau over uit de nulmeting en rekent de gap uit.', 6)
header(ws, 4, ['Domein', 'Nu', 'Doel', 'Gap', 'Prioriteit', 'Onderbouwing (norm, risico, proportionaliteit)'], [42, 8, 8, 8, 12, 70])
example(ws, 5, ['Voorbeeld: 6. Transparantie', '1', '3', '2', 'Hoog', 'Klanten weten niet dat het model meebeslist en krijgen geen reden (R-03). Bij een besluit over krediet is uitleg nodig; dit is een voorbeeld, niet het antwoord voor jullie casus'])
a, b = NUL_SUM
inputs(ws, 6, 11, 6, formula_cols=(1, 2, 4))
for i, d in enumerate(doms):
    r = 6 + i
    ws.cell(r, 1, d).font = BOLD
    ws.cell(r, 2, f'=IF(K4_Nulmeting!D{a + i}<>"",K4_Nulmeting!D{a + i},IF(K4_Scan!B{6 + i}="","",K4_Scan!B{6 + i}))')
    ws.cell(r, 4, f'=IFERROR(IF(OR(B{r}="",C{r}="",B{r}="onbekend"),"",VALUE(C{r})-VALUE(B{r})),"")')
dv(ws, 'score03', 'C6:C16'); dv(ws, 'prioriteit', 'E6:E16')
ws['A18'] = 'Aantal domeinen met doel 3'; ws['A18'].font = BOLD
ws['B18'] = '=COUNTIF(C6:C16,3)'; ws['B18'].fill = SF
ws['C18'] = '=IF(B18>4,"Let op: meer dan vier keer doel 3 is zelden proportioneel","")'
ws['C18'].font = Font(color=WARN, bold=True)

# ---------------- Design_Requirements ----------------
ws = wb.create_sheet('Design_Requirements')
setup(ws, 'K7 deel 1: van risico naar eis (blok 2, hoofdstuk 6)',
      'Per risico uit de top 5: het ontwerpdoel en één of meer eisen. Een goede eis zegt wat er aantoonbaar waar moet zijn, met een acceptatiecriterium dat iemand anders kan controleren. De band haalt het werkboek uit het Risk_Register.', 12)
cols = ['Risk ID', 'Risico (één regel)', 'Getroffen stakeholder en schade', 'Band (uit K6)', 'Escalatie (uit K6)', 'Ethisch principe', 'Risicorespons (met één zin waarom)', 'Ontwerpdoel', 'Req ID', 'Eis', 'Acceptatiecriterium', 'Eigenaar', 'Bron']
header(ws, 4, cols, [8, 26, 26, 11, 10, 18, 22, 26, 8, 30, 30, 16, 18])
example(ws, 5, ['R-03', 'Afgewezen klanten krijgen geen reden en geen bezwaarroute', 'Afgewezen aanvragers: onterecht besluit blijft staan', 'Very high', 'Ja', 'Transparantie en uitlegbaarheid (UNESCO)', 'Verminderen: uitleg en bezwaar zijn haalbaar',
                'Elke afgewezen klant begrijpt waarom en kan bezwaar maken', 'REQ-03', 'Elke afwijzingsbrief noemt de twee belangrijkste redenen en de bezwaarroute', 'Steekproef van 20 brieven per maand: 20 van 20 voldoen', 'Hoofd klantenservice', 'R-03, gap 7.3'])
F0d, F1d = 6, 20
inputs(ws, F0d, 15, 13, formula_cols=(4, 5))
a, b = RR
for r in range(F0d, F1d + 1):
    ws.cell(r, 4, f'=IF(A{r}="","",IFERROR(INDEX(Risk_Register!$V${a}:$V${b},MATCH(A{r},Risk_Register!$A${a}:$A${b},0)),"onbekend ID"))')
    ws.cell(r, 5, f'=IF(A{r}="","",IFERROR(INDEX(Risk_Register!$W${a}:$W${b},MATCH(A{r},Risk_Register!$A${a}:$A${b},0)),""))')
note(ws, F1d + 2, 'Accepteren mag, als je zegt waarom en wie het restrisico accepteert. Bij een geëscaleerd risico beslist de directie daarover.', 13)

# ---------------- Control_Catalog ----------------
ws = wb.create_sheet('Control_Catalog')
setup(ws, 'Voorbeeldmaatregelen (inspiratie)',
      'Gebruik dit als inspiratie, niet als boodschappenlijst: kies wat past bij jullie risico en jullie organisatie. De kaderverwijzing is een suggestie; controleer of die past.', 6)
header(ws, 4, ['Patroon', 'Wat het doet', 'Functie', 'Soort', 'Past vooral bij', 'Kader (suggestie)'], [30, 48, 12, 14, 30, 34])
cat = [
    ('Menselijke beoordeling verplicht', 'Bepaalde besluiten (bijvoorbeeld elke afwijzing) gaan altijd langs een medewerker met tijd, informatie en bevoegdheid', 'Voorkomen', 'Proces', 'Besluiten met grote gevolgen', 'AI-verordening, art. 14 (menselijk toezicht)'),
    ('Bezwaar en herbeoordeling', 'Een vaste route om bezwaar te maken, beoordeeld door iemand die niet bij het eerste besluit betrokken was', 'Herstellen', 'Proces', 'Elke toepassing die over mensen beslist', 'AI-verordening, art. 86 (recht op uitleg)'),
    ('Uitleg per besluit', 'De betrokkene krijgt de belangrijkste redenen in gewone taal', 'Voorkomen', 'Techniek', 'Afwijzingen, scores', 'IEEE CertifAIEd, transparantie'),
    ('Subgroeptest vóór elke release', 'Foutpercentages per groep (regio, geslacht, taal) worden getest voordat een versie live gaat', 'Opsporen', 'Data en model', 'Modellen die over groepen beslissen', 'IEEE CertifAIEd, algoritmische bias'),
    ('Grens voor groepsverschil met actie', 'Een vastgestelde grens; wordt die overschreden, dan volgt een afgesproken actie door een eigenaar', 'Opsporen', 'Governance', 'Na livegang', 'NIST AI RMF, Manage'),
    ('AI-melding', 'De gebruiker ziet meteen dat die met AI praat, en wat het systeem wel en niet kan', 'Voorkomen', 'Techniek', 'Chatbots en agents', 'AI-verordening, art. 50 (transparantie)'),
    ('Overdracht aan een medewerker', 'Op elk moment kan de gebruiker een mens spreken; bij boosheid of kwetsbaarheid gebeurt dat vanzelf', 'Herstellen', 'Proces', 'Chatbots en agents', 'IEEE CertifAIEd, transparantie'),
    ('Kennisbronnen beperken', 'De assistent antwoordt alleen uit gecontroleerde eigen documenten, en zegt het als hij het niet weet', 'Voorkomen', 'Techniek', 'Generatieve AI', 'NIST AI RMF, Manage'),
    ('Testset met lastige vragen', 'Een vaste set vragen (gelijke behandeling, overtuigend fout, gegevens, misbruik) bij elke wijziging', 'Opsporen', 'Techniek', 'Generatieve AI', 'NIST AI RMF, Measure'),
    ('Logging van advies en beslissing', 'Per besluit: advies, menselijke beslissing en reden bij afwijken; iemand kijkt naar het afwijkingspercentage', 'Opsporen', 'Techniek', 'Menselijke controle die echt werkt', 'AI-verordening, art. 12 (logging)'),
    ('Training: wanneer volg je het systeem niet?', 'Medewerkers oefenen met gevallen waarin het model aantoonbaar fout zat', 'Voorkomen', 'Mens', 'Automation bias', 'AI-verordening, art. 4 (AI-geletterdheid)'),
    ('Leverancierscheck en contractafspraken', 'Afspraken over hergebruik van gegevens, opslaglocatie, logging en informatieplicht', 'Voorkomen', 'Governance', 'Externe diensten', 'ISO/IEC 42001, A.10 Derde partijen'),
    ('Stopprocedure en terugval naar handwerk', 'Een vast criterium om het systeem uit te zetten, met wie beslist en hoe het werk doorgaat', 'Herstellen', 'Governance', 'Elke toepassing', 'NIST AI RMF, Manage'),
    ('Bezwaren- en incidentregister', 'Elk gegrond bezwaar en elk incident wordt vastgelegd en leidt tot een verbeteractie', 'Herstellen', 'Proces', 'Leren van fouten', 'ISO/IEC 42001, A.8 Informatie voor belanghebbenden'),
]
for i, row in enumerate(cat, 5):
    for c, v in enumerate(row, 1):
        x = ws.cell(i, c, v); x.alignment = WR; x.border = B
    ws.row_dimensions[i].height = 42

# ---------------- Controls ----------------
ws = wb.create_sheet('Controls')
setup(ws, 'K7 deel 1: maatregelen (blok 2, hoofdstuk 6)',
      '2 tot 3 maatregelen per risico uit de top 5, met een eigenaar. Combineer voorkomen, opsporen en herstellen. Kolom Kader: op welk erkend kader sluit de maatregel aan? Eén verwijzing is genoeg (kies uit de lijst of typ zelf). Bouw minstens twee maatregelen echt in via A-AI2 (nodig voor niveau goed bij criterium 6).', 15)
cols = ['Control ID', 'Req ID', 'Risk ID', 'Titel', 'Beschrijving: wat, door wie, wanneer', 'Functie', 'Soort', 'Kader', 'Eigenaar', 'Frequentie of aanleiding', 'Bewijs', 'Verificatie', 'Inbouwen door', 'Klaar voor AI Solutions Day?', 'Hertest (optioneel): welke vraag, welk paar of welke meting, en welke uitkomst verwacht je?']
header(ws, 4, cols, [9, 8, 8, 20, 34, 11, 13, 28, 16, 16, 18, 18, 13, 11, 34])
example(ws, 5, ['C-02', 'REQ-01', 'R-01', 'Afwijzing langs een medewerker', 'Elke afwijzing door het model gaat naar een kredietmedewerker, die het dossier bekijkt en mag afwijken zonder toestemming vooraf', 'Voorkomen', 'Proces',
                'AI-verordening, art. 14 (menselijk toezicht)', 'Hoofd kredietverlening', 'Elke aanvraag', 'Logboek met advies en beslissing', 'Maandelijkse steekproef van 20 afwijzingen', 'Beide', 'ja', 'Gepaarde test regio: aantal paren met ander besluit daalt van 11 naar 0 na menselijke beoordeling'])
inputs(ws, 6, 25, 15)
dv(ws, 'functie', 'F6:F30'); dv(ws, 'soort_c', 'G6:G30'); dv(ws, 'kader', 'H6:H30', strict=False); dv(ws, 'inbouw', 'M6:M30'); dv(ws, 'janee', 'N6:N30')
ws.conditional_formatting.add('H6:H30', FormulaRule(formula=['AND(LEN($A6)>0,LEN($H6)=0)'], fill=WF))
ws.conditional_formatting.add('I6:I30', FormulaRule(formula=['AND(LEN($A6)>0,LEN($I6)=0)'], fill=WF))
ws['A32'] = 'Kadercheck'; ws['A32'].font = BOLD
ws['D32'] = '=COUNTA(A6:A30)'; ws['E32'] = 'maatregelen'
ws['D33'] = '=COUNTIFS(A6:A30,"<>",H6:H30,"")'; ws['E33'] = 'zonder Kader (rood): vul aan vóór de inlevering van K7'
ws['D34'] = '=COUNTIF(N6:N30,"ja")'; ws['E34'] = 'klaar voor de AI Solutions Day (minstens twee ingebouwd)'
for c in ('D32', 'D33', 'D34'):
    ws[c].fill = SF

# ---------------- Leverancierscheck ----------------
ws = wb.create_sheet('Leverancierscheck')
setup(ws, 'Leverancierscheck (blok 2, hoofdstuk 7 en bijlage C)',
      'Eén rij per externe dienst uit K3 (n8n, taalmodel-API, vectordatabase, hosting, leverancier van het model). Weet je een antwoord niet? Schrijf "onbekend: navragen" en behandel dat als risico. Verzin geen feiten. Verwijs waar het kan naar het architectuurdocument uit A-AI2.', 9)
cols = ['Externe dienst', 'Wat doet de leverancier met onze gegevens, ook voor training?', 'Waar staan de gegevens?', 'Wat wordt gelogd en wie kan erbij?', 'Wat mag de agent of het systeem zelf doen zonder mens?', 'Bron (voorwaarden, contract, A-AI2-document)', 'Status', 'Gevolg (risico of maatregel)', 'Kader']
header(ws, 4, cols, [22, 32, 24, 28, 32, 24, 18, 24, 22])
example(ws, 5, ['Orderagent Frisco: taalmodel-API, vectordatabase en n8n', 'De taalmodel-API gebruikt invoer volgens de voorwaarden niet voor training; dat staat in het abonnement dat A-AI2 gebruikt', 'De vectordatabase draait in een datacenter in de Verenigde Staten',
                'n8n bewaart elk gesprek 30 dagen; alleen de beheerder van de partner kan erbij', 'De agent mag een offerte opstellen, maar een bestelling boven SRD 10.000 bevestigt een medewerker', 'Voorwaarden API; architectuurdocument A-AI2', 'Bekend', 'C-08: bewaartermijn n8n korter', 'ISO/IEC 42001, A.10 Derde partijen'])
inputs(ws, 6, 6, 9)
dv(ws, 'status_lev', 'G6:G11'); dv(ws, 'kader', 'I6:I11', strict=False)
ws.conditional_formatting.add('A6:I11', FormulaRule(formula=['ISNUMBER(SEARCH("onbekend",A6))'], fill=PatternFill('solid', fgColor='F5C98A')))
note(ws, 13, 'Waarom deze vier vragen? Gegevens kunnen buiten het zicht van de partner worden hergebruikt; wetten en afspraken verschillen per land; logs zijn nodig om fouten op te sporen maar bevatten ook persoonsgegevens; en hoe meer de agent zelf mag, hoe groter de schade bij een fout.', 9)

# ---------------- Human_Oversight ----------------
ws = wb.create_sheet('Human_Oversight')
setup(ws, 'K7 deel 2: menselijke controle en bezwaar (blok 2, hoofdstuk 7)',
      'Werk de menselijke controle uit voor de belangrijkste beslissing van jullie toepassing. Controleer met de rekensom of de controle haalbaar is. Beschrijf daarna de bezwaarroute vanuit de betrokkene en toets die aan de zes kenmerken uit clip 19: bekend, laagdrempelig, met uitleg, onafhankelijk, snel, herstellend.', 4)
header(ws, 4, ['Vraag', 'Wat je invult', 'Jullie antwoord', 'Voorbeeld Suribank'], [22, 46, 56, 46])
ho = [('Beslissing en rol van AI', 'Welke beslissing, en doet het systeem een advies, een voorselectie, of beslist het zelf?', 'Kredietbesluit; het model geeft een advies'),
      ('Impact', 'Laag, midden of hoog, met een verwijzing naar je risicoregister', 'Hoog: R-01 en R-03'),
      ('Positie van de mens', 'In de lus, op de lus, of aan het roer (clip 18), en waarom die past bij de impact', 'In de lus bij elke afwijzing'),
      ('Bevoegdheid', 'Mag de mens afwijken zonder toestemming vooraf? Wie mag het systeem stilzetten?', 'Ja, met een reden; stilzetten: hoofd kredietverlening'),
      ('Informatie', 'Wat ziet de mens: score, belangrijkste redenen, onzekerheid, het originele dossier?', 'Score, twee belangrijkste redenen en het dossier'),
      ('Tijd', 'Hoeveel tijd per geval, en is dat haalbaar bij het aantal gevallen?', '20 minuten per afwijzing; zie rekensom'),
      ('Kennis', 'Welke training, en specifiek: wanneer moet je het systeem niet volgen?', 'Training met gevallen waarin het model fout zat'),
      ('Cultuur', 'Is afwijken met een reden normaal, of telt het mee in de beoordeling van de medewerker? Wie dekt de medewerker als het later misgaat?', 'Afwijken telt niet negatief; het hoofd dekt de medewerker'),
      ('Registratie', 'Wat wordt per beslissing gelogd (advies, menselijke beslissing, reden bij afwijken), en wie kijkt naar het afwijkingspercentage?', 'Alle drie; maandelijks door het hoofd'),
      ('Reviewtrigger', 'Welke gevallen gaan altijd langs een mens?', 'Elke afwijzing, en elke aanvraag uit het binnenland'),
      ('Escalatietrigger', 'Wanneer gaat een geval of een patroon naar een hoger niveau?', 'Verschil tussen regio\'s boven de grens'),
      ('Test', 'Hoe test je dat de controle werkt (bijvoorbeeld: dossiers waarin het model aantoonbaar fout zit)?', '10 testdossiers met een bekende fout'),
      ('Eigenaar', 'Welke functie is verantwoordelijk?', 'Hoofd kredietverlening')]
for i, (q, w, e) in enumerate(ho, 5):
    ws.cell(i, 1, q).font = BOLD; ws.cell(i, 1).border = B
    x = ws.cell(i, 2, w); x.alignment = WR; x.border = B
    x = ws.cell(i, 3); x.fill = IF_; x.border = B; x.alignment = WR
    x = ws.cell(i, 4, e); x.font = EXFONT; x.fill = GF; x.border = B; x.alignment = WR
    ws.row_dimensions[i].height = 40
r = 5 + len(ho) + 1
section(ws, r, 'Rekensom: is de controle haalbaar?', 4); r += 1
rk = r
for lab, val in [('Gevallen per maand die langs een mens gaan', None), ('Minuten per geval', None), ('Uren nodig per maand', 'calc'), ('Uren beschikbaar per maand bij de partner', None), ('Haalbaar?', 'chk')]:
    ws.cell(r, 1, lab).font = BOLD
    ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=2)
    x = ws.cell(r, 3); x.border = B
    if val == 'calc':
        x.value = f'=IF(OR(C{rk}="",C{rk + 1}=""),"",ROUND(C{rk}*C{rk + 1}/60,0))'; x.fill = SF
    elif val == 'chk':
        x.value = f'=IF(OR(C{rk + 2}="",C{rk + 3}=""),"",IF(C{rk + 2}<=C{rk + 3},"Ja, met "&(C{rk + 3}-C{rk + 2})&" uur ruimte","Nee: "&(C{rk + 2}-C{rk + 3})&" uur tekort"))'; x.fill = SF
    else:
        x.fill = IF_
    r += 1
r += 1
section(ws, r, 'Bezwaarroute, vanuit de betrokkene', 4); r += 1
for q, w in [('Hoe hoor ik ervan?', 'Waar in het besluit staat dat ik bezwaar kan maken, en hoe?'),
             ('Hoe dien ik het in?', 'Kanaal (balie, telefoon, WhatsApp, formulier), en wat ik moet aanleveren. Denk aan mensen zonder internet of die moeite hebben met lezen.'),
             ('Wat krijg ik te zien?', 'Welke uitleg krijg ik over het besluit, zodat ik weet waartegen ik bezwaar maak?'),
             ('Wie kijkt ernaar?', 'Iemand die niet bij het eerste besluit betrokken was, met de bevoegdheid het te veranderen.'),
             ('Hoe snel?', 'Een vaste termijn voor ontvangstbevestiging en voor de uitkomst.'),
             ('Wat als ik gelijk krijg?', 'Herstel: het besluit herzien, gegevens corrigeren, excuus, en zo nodig vergoeding.'),
             ('Wat leert de organisatie ervan?', 'Hoe gegronde bezwaren terugkomen in monitoring en model.')]:
    ws.cell(r, 1, q).font = BOLD; ws.cell(r, 1).border = B
    x = ws.cell(r, 2, w); x.alignment = WR; x.border = B
    x = ws.cell(r, 3); x.fill = IF_; x.border = B; x.alignment = WR
    ws.row_dimensions[r].height = 40; r += 1

# ---------------- Governance_RACI ----------------
ws = wb.create_sheet('Governance_RACI')
setup(ws, 'K7 deel 2c: RACI voor ethische beslissingen en AI-beleidsregel (blok 2, hoofdstuk 7)',
      'Zet bovenaan de functies bij de partner (geen namen). Minstens acht activiteiten, met de vijf verplichte erbij. Precies één A per activiteit, met echte bevoegdheid; de leverancier is hooguit C. Technisch beheer staat in A-AI2 en databeheer in A-DG: verwijs daarnaar.', 9)
roles = ['Directie', 'Eigenaar toepassing', 'Medewerker die ermee werkt', 'Team A-AI2 / IT', 'Klantenservice', 'Leverancier']
header(ws, 4, ['Activiteit of besluit'] + roles + ['Aantal A', 'Controle'], [40, 14, 14, 14, 14, 14, 14, 9, 22])
for c in range(2, 8):
    ws.cell(4, c).fill = PatternFill('solid', fgColor='2E5597')
ws.row_dimensions[4].height = 46
note(ws, 3, 'Pas de functienamen in rij 4 aan aan jullie partner (de groene kopcellen mag je overschrijven).', 9)
example(ws, 5, ['Voorbeeld: het systeem stilzetten', 'I', 'A', 'R', 'C', 'I', 'I', 1, 'OK'])
acts = ['Goedkeuren van het doel en de inzet van de toepassing', 'Vaststellen van fairnessgrenzen (wanneer is een verschil tussen groepen te groot?)',
        'Afhandelen van bezwaren', 'Besluiten over grote wijzigingen en hertraining', 'Het systeem stilzetten of uitfaseren', 'Live gaan of doorgaan (met het bewijs dat daarvoor nodig is)', '', '', '', '']
inputs(ws, 6, 10, 9, formula_cols=(8, 9))
for i, a_ in enumerate(acts):
    r = 6 + i
    if a_:
        ws.cell(r, 1, a_).font = BOLD if i < 5 else Font(color=DARK)
    ws.cell(r, 8, f'=IF(A{r}="","",COUNTIF(B{r}:G{r},"A")+COUNTIF(B{r}:G{r},"A+R"))')
    ws.cell(r, 9, f'=IF(A{r}="","",IF(H{r}=1,IF(OR(G{r}="A",G{r}="A+R"),"Leverancier als A: niet toegestaan","OK"),IF(H{r}=0,"Geen A","Meer dan één A")))')
dv(ws, 'raci', 'B6:G15')
ws.conditional_formatting.add('I6:I15', FormulaRule(formula=['AND(LEN(I6)>0,I6<>"OK")'], fill=WF, font=Font(color=WARN, bold=True)))
ws.conditional_formatting.add('I6:I15', FormulaRule(formula=['I6="OK"'], fill=OKF))
ws['A17'] = 'Aantal activiteiten'; ws['A17'].font = BOLD
ws['B17'] = '=COUNTA(A6:A15)'; ws['B17'].fill = SF
ws['C17'] = '=IF(B17>=8,"Goed: minstens acht","Nog niet: minstens acht activiteiten")'
ws.merge_cells('C17:F17')
note(ws, 18, 'De eerste vijf activiteiten (vet) zijn verplicht. R = voert uit (minstens één); A = eindverantwoordelijk, tekent af (precies één); C = wordt vooraf om advies gevraagd; I = wordt achteraf geïnformeerd.', 9)
section(ws, 20, 'AI-beleidsregel (hoogstens 100 woorden), die de partner kan overnemen', 9)
ws.merge_cells('A21:G25')
x = ws['A21']; x.fill = IF_; x.alignment = WR; x.border = B
ws['H21'] = 'Woorden'; ws['H21'].font = BOLD
ws['H22'] = '=IF(LEN(TRIM(A21))=0,0,LEN(TRIM(A21))-LEN(SUBSTITUTE(TRIM(A21)," ",""))+1)'; ws['H22'].fill = SF
ws['I22'] = '=IF(H22=0,"",IF(H22<=100,"Binnen 100 woorden","Te lang: hoogstens 100"))'
for rr in range(21, 26):
    ws.row_dimensions[rr].height = 24
section(ws, 27, 'Staat alles erin? (ISO/IEC 42001, A.2)', 9)
c0 = 28
for i, t in enumerate(['Waarvoor het systeem wordt gebruikt, en waarvoor niet', 'Wat een mens beslist', 'Dat gebruikers en betrokkenen horen dat het AI is', 'Welke gegevens het gebruikt', 'Wie het systeem stilzet, en wie het weer aanzet'], c0):
    x = ws.cell(i, 1, t); x.border = B
    x = ws.cell(i, 2); x.fill = IF_; x.border = B
dv(ws, 'janee', f'B{c0}:B{c0 + 4}')
note(ws, c0 + 6, 'Wat er bij stilzetten gebeurt en wie weer aanzet, moet overeenkomen met deze RACI en met het stopcriterium in K8 (hoofdstuk 8).', 9)

# ---------------- Verwerkingslijst ----------------
ws = wb.create_sheet('Verwerkingslijst')
setup(ws, 'Bijlage E: verwerkingslijst (blok 2 en 3)',
      'Alle feedbackpunten: de actiepunten uit de feedback op Assessment 1, het panel van de Design Review en de peergroep. Per punt een besluit, wat jullie veranderden of waarom niet, en waar het in het rapport staat. "Niet overgenomen" mag, als je uitlegt waarom. Bij Assessment 2 kijkt de docent eerst naar deze lijst.', 7)
cols = ['Nr', 'Actiepunt-ID (bijv. A1-2)', 'Bron', 'Feedbackpunt', 'Besluit', 'Wat we veranderden, of waarom niet', 'Waar in het rapport']
header(ws, 4, cols, [5, 14, 18, 40, 18, 48, 22])
example(ws, 5, [1, '', 'Panel (Design Review)', 'Bezwaarroute alleen via de website', 'Overgenomen', 'Bezwaar kan nu ook aan de balie en telefonisch', 'Hoofdstuk 7, bezwaarroute'])
inputs(ws, 6, 25, 7)
for i in range(25):
    ws.cell(6 + i, 1, i + 1)
dv(ws, 'bron_fb', 'C6:C30'); dv(ws, 'besluit_fb', 'E6:E30')
ws.conditional_formatting.add('F6:F30', FormulaRule(formula=['AND(LEN($D6)>0,LEN($F6)=0)'], fill=WF))
ws['A32'] = 'Samenvatting'; ws['A32'].font = BOLD
for i, s in enumerate(['Overgenomen', 'Deels overgenomen', 'Niet overgenomen'], 33):
    ws.cell(i, 4, s); x = ws.cell(i, 5, f'=COUNTIF(E6:E30,"{s}")'); x.fill = SF
ws.cell(36, 4, 'Zonder besluit'); x = ws.cell(36, 5, '=COUNTIFS(D6:D30,"<>",E6:E30,"")'); x.fill = SF

# ---------------- K8 ----------------
ws = wb.create_sheet('K8_Monitoring')
setup(ws, 'K8 implementatie- en monitoringplan (blok 3, hoofdstuk 8)',
      'Vier delen. A: hoe komen de maatregelen in de organisatie. B: welke ethische signalen volgen jullie (vijf tot acht), met grens, actie en wie besluit. C: wanneer gaat het systeem opnieuw langs de beoordeling. D: twee vaste regels, verplicht voor criterium 7 van de A2-rubric: de incidentroute en het stopcriterium. Voor technische monitoring verwijs je naar A-AI2, voor datamonitoring naar A-DG.', 9)
r = 4
section(ws, r, 'Deel A: implementatieplan', 9); r += 1
hdr = ['Control ID', 'Fase', 'Wat er moet gebeuren', 'Eigenaar', 'Middelen', 'Klaar wanneer', 'Besluitmoment']
for i, (h, w) in enumerate(zip(hdr, [11, 13, 40, 20, 22, 14, 30, 22, 22]), 1):
    x = ws.cell(r, i, h); x.font = HFONT; x.fill = HF; x.border = B
    ws.column_dimensions[L(i)].width = w
ws.column_dimensions['H'].width = 22; ws.column_dimensions['I'].width = 22
r += 1
example(ws, r, ['C-02', 'Direct', 'Afwijzingen weer langs een medewerker; werkinstructie aanpassen', 'Hoofd kredietverlening', 'Ongeveer 85 uur per maand extra', '1 april', 'Directie keurt de extra capaciteit goed'])
r += 1; a0 = r
inputs(ws, r, 10, 7); r += 10
dv(ws, 'fase', f'B{a0}:B{r - 1}')
note(ws, r, 'Fases: Direct = binnen een maand (schade nu stoppen); Kort = binnen drie maanden (processen, documenten, training, bezwaarroute); Structureel = binnen een jaar (hertraining, contracten, dashboards, onafhankelijke toets).', 9); r += 2
section(ws, r, 'Deel B: monitoringplan, vijf tot acht ethische signalen', 9); r += 1
hdr = ['Indicator', 'Soort', 'Bron en meting', 'Hoe vaak', 'Wie meet', 'Grens', 'Actie bij overschrijding', 'Wie besluit']
for i, h in enumerate(hdr, 1):
    x = ws.cell(r, i, h); x.font = HFONT; x.fill = HF; x.border = B
r += 1
example(ws, r, ['Afwijzingspercentage per filiaal', 'Groepsverschil', 'Kernsysteem', 'Maandelijks', 'Data-analist IT', 'Verschil met Paramaribo groter dan de grens die de directie vaststelt', 'Review binnen twee weken; zo nodig meer afwijzingen naar een mens', 'Hoofd kredietverlening'])
r += 1; b0 = r
inputs(ws, r, 8, 8); r += 8
dv(ws, 'soort_m', f'B{b0}:B{r - 1}')
for col in ('F', 'H'):
    ws.conditional_formatting.add(f'{col}{b0}:{col}{r - 1}', FormulaRule(formula=[f'AND(LEN($A{b0})>0,LEN({col}{b0})=0)'], fill=WF))
ws.cell(r, 1, 'Aantal indicatoren').font = BOLD
x = ws.cell(r, 3, f'=COUNTA(A{b0}:A{r - 1})'); x.fill = SF
ws.cell(r, 4, f'=IF(C{r}=0,"",IF(AND(C{r}>=5,C{r}<=8),"Goed: vijf tot acht","Advies: vijf tot acht ethische signalen"))')
r += 1
note(ws, r, 'Kijk niet alleen naar het model: of mensen bezwaar kunnen maken en of medewerkers afwijken, is net zo belangrijk (soort Proces en Mensen). Rood: een indicator zonder grens of zonder iemand die besluit.', 9); r += 2
section(ws, r, 'Deel C: herbeoordeling', 9); r += 1
for lab in ['Vast moment (bijvoorbeeld jaarlijks, en wanneer)', 'Bij welke gebeurtenissen extra (wijziging, incident, nieuwe wet, grensoverschrijding)']:
    ws.cell(r, 1, lab).font = BOLD; ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=2)
    x = ws.cell(r, 3); x.fill = IF_; x.border = B; x.alignment = WR
    ws.merge_cells(start_row=r, start_column=3, end_row=r, end_column=8); ws.row_dimensions[r].height = 30; r += 1
r += 1
section(ws, r, 'Deel D: twee vaste regels (verplicht, A2-criterium 7)', 9); r += 1
note(ws, r, 'Ze sluiten de verbetercyclus uit kaderclip E: ISO/IEC 42001 vraagt erom in clausule 10 (afwijkingen en corrigerende maatregelen). Een incident is meer dan een storing: een besluit of antwoord dat iemand schade doet of had kunnen doen.', 9); r += 1
d_rows = []
for grp, items in [('Incidentroute', ['Wat is bij jullie een incident?', 'Wie mag melden (ook klanten en medewerkers)?', 'Bij wie komt de melding binnen?', 'Hoe snel wordt er gereageerd (termijn)?', 'Wie informeert de getroffene?']),
                   ('Stopcriterium', ['Wanneer gaat het systeem uit of terug naar handwerk? (koppel aan een grens uit deel B of een ernstig incident)', 'Wie beslist (snel bereikbaar)?', 'Hoe gaat het werk door zolang het systeem uit staat?', 'Wie besluit dat het weer aan mag, en op basis waarvan?'])]:
    x = ws.cell(r, 1, grp); x.font = HFONT; x.fill = HF
    for c in range(2, 9):
        ws.cell(r, c).fill = HF
    r += 1
    for q in items:
        x = ws.cell(r, 1, q); x.alignment = WR; x.border = B
        ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=2)
        x = ws.cell(r, 3); x.fill = IF_; x.border = B; x.alignment = WR
        ws.merge_cells(start_row=r, start_column=3, end_row=r, end_column=8)
        ws.row_dimensions[r].height = 34; d_rows.append(r); r += 1
ws.cell(r, 1, 'Status deel D').font = BOLD
cnt = '+'.join([f'(LEN(C{x})>0)' for x in d_rows])
x = ws.cell(r, 3, f'=IF(({cnt})={len(d_rows)},"Compleet","Nog niet compleet: "&({len(d_rows)}-({cnt}))&" van {len(d_rows)} vragen open; verplicht voor criterium 7")')
x.fill = SF; ws.merge_cells(start_row=r, start_column=3, end_row=r, end_column=8)
ws.conditional_formatting.add(f'C{r}', FormulaRule(formula=[f'LEFT(C{r},4)="Nog "'], font=Font(color=WARN, bold=True), fill=WF))
for x_ in d_rows:
    ws.conditional_formatting.add(f'C{x_}', FormulaRule(formula=[f'LEN(C{x_})=0'], fill=WF))
r += 2
note(ws, r, 'Voorbeeld stopcriterium (Suribank): indicator 1 of 3 twee keer achter elkaar boven de grens: alle aanvragen terug naar handmatige beoordeling. Besluit: hoofd kredietverlening. Het beslismemo noemt het stopcriterium en de datum van de volgende review.', 9)
ws.freeze_panes = None

# ---------------- Hertest ----------------
ws = wb.create_sheet('Hertest')
setup(ws, 'Hertest: practicum 4 opnieuw (optioneel, bijlage F)',
      'Per maatregel die jullie inbouwden: welke test uit practicum 4 laat het effect zien, wat was de uitkomst bij de eerste test en bij de hertest, en wat is jullie oordeel? Gebruik dezelfde testset als bij de eerste test (testlogboek). De hertest is niet verplicht; hij telt mee voor het niveau excellent. Kijk niet alleen naar de gepaarde test, maar ook naar de foutpercentages per groep.', 10)
cols = ['Control ID', 'Risk ID', 'Test (vraag, paar of meting uit practicum 4)', 'Verwachte uitkomst', 'Uitkomst eerste test', 'Uitkomst hertest', 'Oordeel', 'Toelichting', 'Gevolg (aanpassen, monitoren, accepteren)', 'Restrisico bijgewerkt in K6?']
header(ws, 4, cols, [10, 8, 34, 24, 18, 18, 13, 34, 28, 12])
example(ws, 5, ['C-02', 'R-01', 'Gepaarde test regio (100 paren) en onterecht afgewezen per regio', 'Geen paren met ander besluit; verschil tussen regio\'s kleiner', '11 van 100 paren anders; 12,8% tegenover 23,4%', '0 van 100; 13,1% tegenover 17,0%', 'Werkt deels', 'Paren gelijk, maar het verschil tussen regio\'s is kleiner, niet weg', 'Monitoren met indicator 1; hertraining in fase 3', 'ja'])
inputs(ws, 6, 15, 10)
dv(ws, 'oordeel', 'G6:G20'); dv(ws, 'janee', 'J6:J20')
ws.conditional_formatting.add('G6:G20', FormulaRule(formula=['G6="Werkt"'], fill=OKF))
ws.conditional_formatting.add('G6:G20', FormulaRule(formula=['G6="Werkt niet"'], fill=WF, font=Font(color=WARN, bold=True)))
ws['A22'] = 'Samenvatting'; ws['A22'].font = BOLD
for i, s in enumerate(['Werkt', 'Werkt deels', 'Werkt niet'], 23):
    ws.cell(i, 3, s); x = ws.cell(i, 4, f'=COUNTIF(G6:G20,"{s}")'); x.fill = SF
note(ws, 27, 'De voorbeeldgetallen in rij 5 zijn verzonnen en dienen alleen als vorm. Jullie eigen cijfers komen uit het testlogboek van practicum 4.', 10)

# order sheets
order = ['Start', 'K1_Scope', 'K2_Stakeholders', 'K3_Proces_Data', 'Bewijsplan', 'K4_Scan', 'K4_Nulmeting', 'Dilemma_Log', 'Risk_Register',
         'Gewenste_situatie', 'Design_Requirements', 'Control_Catalog', 'Controls', 'Leverancierscheck', 'Human_Oversight', 'Governance_RACI',
         'Verwerkingslijst', 'K8_Monitoring', 'Hertest', 'Lijsten']
wb._sheets = [wb[n] for n in order]
colors = {'Start': DARK, 'Lijsten': '999999'}
for n in order:
    wb[n].sheet_properties.tabColor = colors.get(n, 'E3A92B' if n in ('Risk_Register', 'Controls', 'K8_Monitoring') else '2F6B4F')
wb.active = 0
wb.save(OUT)
print('saved', OUT)
