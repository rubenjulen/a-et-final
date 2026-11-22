"""Word-sjablonen voor studenten A-ET: K1, K5, tussenrapport A1, eindrapport A2, reflectie A2, AI-verklaring.
Draaien vanuit scratchpad/: venv/bin/python scripts/gen_wordsjablonen.py"""
import sys, os
sys.path.insert(0, 'scripts')
from gen_feedbackforms import (shade, borders, leftbar, run, para, celltext, h, table, fixwidths,
                               minheight, box, INK, GREY, SAND, LIGHT, AMBER, logo_header)
from docx import Document
from docx.shared import Pt, Cm
from docx.enum.text import WD_BREAK
from docx.oxml.ns import qn

OUT = os.environ.get('AET_OUT', 'out') + '/instrumenten/'
os.makedirs(OUT, exist_ok=True)
WEG = 'Grijze hulptekst is uitleg: haal die weg voordat je inlevert.'


def newdoc(footer):
    doc = Document()
    st = doc.styles['Normal']; st.font.name = 'Calibri'; st.font.size = Pt(10.5)
    st.element.rPr.rFonts.set(qn('w:eastAsia'), 'Calibri')
    s = doc.sections[0]; s.page_width = Cm(21); s.page_height = Cm(29.7)
    s.left_margin = s.right_margin = Cm(2); s.top_margin = s.bottom_margin = Cm(1.8)
    logo_header(s)
    run(s.footer.paragraphs[0], 'ICT A-ET · Collegejaar 2026-2027 · ' + footer, 8, color=GREY)
    return doc


def title(doc, t, sub):
    p = para(doc, '', space_after=0); run(p, t, 18, True, False, INK, 'Calibri')
    para(doc, sub, 9, color=GREY, space_after=6)


def hint(doc, text, size=9):
    return para(doc, text, size, italic=True, color=GREY, space_after=4)


def kv(doc, rows, widths=(4.2, 12.8)):
    t = doc.add_table(rows=len(rows), cols=2); borders(t)
    for r, (k, v) in enumerate(rows):
        c0, c1 = t.rows[r].cells
        celltext(c0, k, 9, True, color=INK); shade(c0, SAND)
        celltext(c1, v, 9, hint=bool(v))
    fixwidths(t, list(widths))
    return t


def note(doc, lines, headline=None):
    t = doc.add_table(rows=1, cols=1); borders(t, AMBER); fixwidths(t, [17]); c = t.rows[0].cells[0]; shade(c, LIGHT)
    if headline: celltext(c, headline, 9, True, color=INK)
    else: c.text = ''
    first = not headline
    for ln in lines:
        p = c.paragraphs[0] if first else c.add_paragraph(); first = False
        p.paragraph_format.space_after = Pt(1); run(p, ln, 8.5)
    para(doc, '', space_after=2)


def pagebreak(doc):
    doc.add_paragraph().add_run().add_break(WD_BREAK.PAGE)


def section(doc, heading, helptext, height=3.0, omvang=None):
    h(doc, heading + (f'  ·  {omvang}' if omvang else ''))
    box(doc, helptext, height)


def voorblad(doc, toets, hoofdstukken, extra_rows=()):
    rows = [('Groep', ''), ('Casus', 'Oplossing uit A-AI2 en partnerorganisatie, of de Suribank-route'),
            ('Route', 'Eigen oplossing · andere organisatie · Suribank-casusdossier'), *extra_rows]
    kv(doc, rows)
    para(doc, '', space_after=2)
    t = table(doc, ['Naam', 'Studentnummer', 'Eigenaar van hoofdstuk(ken)'], [6, 4, 7], rows=5)
    for row in t.rows[1:]: minheight(row, 0.7)
    hint(doc, 'Elk hoofdstuk heeft precies één eigenaar. ' + ('Eigenaren wisselen ten opzichte van Assessment 1: iedereen bezit minstens één hoofdstuk uit 6 tot en met 8 of het beslismemo.' if toets == 'A2' else 'De eigenaar schrijft en verantwoordt het hoofdstuk; de groep blijft samen verantwoordelijk voor het geheel.'))


def aiverklaring_blok(doc, groep=True):
    h(doc, 'AI-verklaring' + (' van de groep' if groep else ''))
    if groep:
        txt = 'Welke AI-tools gebruikten jullie, waarvoor, en hoe controleerden jullie de uitkomst? Geen gebruik? Schrijf dat op.'
    else:
        txt = 'Hoogstens 80 woorden: welke tool, waarvoor, en wat je zelf hebt gecontroleerd. Geen gebruik? Schrijf dat op.'
    box(doc, txt, 2.0)


# ---------------------------------------------------------------- 1. K1
def k1():
    doc = newdoc('K1 AI Use Case & Scope Canvas')
    title(doc, 'K1 · AI Use Case & Scope Canvas', 'Blok 1 · groep · inleveren zondag 10 januari, 23:59 · wordt hoofdstuk 1 van het rapport · omvang: één pagina, plus de vijf teamafspraken')
    note(doc, ['Het canvas legt vast wat jullie precies onderzoeken. Zonder heldere afbakening is elke latere score of aanbeveling vaag.',
               'Is de oplossing een chatbot, assistent of agent? Beantwoord dan ook de vraag in de kolom "Bij generatieve AI".',
               'Inleveren uiterlijk zondag 10 januari, 23:59: dit canvas (of een duidelijke foto van het A3-blad), met de teamafspraken en een AI-verklaring.',
               WEG], 'Zo gebruik je dit canvas')
    kv(doc, [('Groep', ''), ('Partner (A-AI2)', ''), ('Datum', '')])
    para(doc, '', space_after=2)
    F = [('Organisatie en context', 'Waar speelt dit, en wat voor organisatie is het?', 'Wie is de partner uit A-AI2?'),
         ('Probleem', 'Welk probleem moet de AI oplossen, en waarom nu?', 'Wat lost de assistent op voor de gebruiker, en wat voor de organisatie?'),
         ('AI-toepassing', 'Wat doet de AI precies: herkennen, voorspellen, aanbevelen of maken?', 'Wat maakt het: antwoorden, samenvattingen, teksten of voorstellen?'),
         ('Soort AI', 'Regels, machine learning of generatieve AI? Zelf gebouwd of van een leverancier?', 'Welk taalmodel of welke dienst, en welke instructies en documenten krijgt het mee?'),
         ('Input', 'Welke gegevens gaan erin, en van wie?', 'Wat typt of zegt de gebruiker, en gaan die gegevens naar een externe dienst?'),
         ('Output', 'Wat komt eruit?', 'Weet de gebruiker dat het antwoord door AI is gemaakt?'),
         ('Beslissing', 'Wat gebeurt er met de output, en wie beslist?', 'Wat doet de gebruiker met het antwoord, en leest er een mens mee?'),
         ('Gebruikers', 'Wie werkt met het systeem?', 'Wie chat of werkt met de assistent?'),
         ('Betrokkenen', 'Over wie gaat het, en wie merkt de gevolgen?', 'Over wie gaat het antwoord, ook als die persoon niet zelf chat?'),
         ('Doel en succes', 'Wat moet beter worden, en hoe meet je dat?', 'Hoe weet je dat de antwoorden goed genoeg zijn, en voor wie?'),
         ('Afbakening', 'Wat onderzoeken jullie wel, en wat bewust niet?', 'Welke vragen of taken mag de assistent niet doen?'),
         ('Casus en bewijs', 'Welke casus, en welke bronnen en mensen gebruiken jullie?', 'Welke documentatie uit A-AI2 en A-DG, en welke tests?'),
         ('Eerste zorgen', 'Welke drie ethische zorgen zien jullie nu al, elk in één zin?', 'Denk aan de vier vragen uit clip 4.')]
    t = table(doc, ['#', 'Veld en vraag', 'Bij generatieve AI', 'Jullie antwoord'], [0.9, 5.0, 4.3, 6.8], rows=len(F))
    for i, (veld, vraag, gen) in enumerate(F, 1):
        cs = t.rows[i].cells
        celltext(cs[0], str(i), 9, True, color=INK)
        celltext(cs[1], veld, 9, True, color=INK)
        p = cs[1].add_paragraph(); p.paragraph_format.space_after = Pt(1); run(p, vraag, 8.5)
        celltext(cs[2], gen, 8.5, hint=True)
        celltext(cs[3], '', 9); minheight(t.rows[i], 1.25)
    h(doc, 'Teamafspraken voor A-ET')
    hint(doc, 'Vul de afspraken uit A-AI2 aan met deze vijf punten.')
    T = ['Wie coördineert?', 'Wie is eigenaar van welke hoofdstukken?', 'Wanneer overleggen jullie?',
         'Hoe verdelen jullie het werk naast A-AI2 en A-DG?', 'Wat doen jullie als iemand niet levert?']
    t = table(doc, ['Afspraak', 'Wat jullie afspreken'], [6, 11], rows=5)
    for i, a in enumerate(T, 1):
        celltext(t.rows[i].cells[0], a, 9, True, color=INK); minheight(t.rows[i], 0.9)
    h(doc, 'Check vóór het inleveren')
    for c in ['Probleem en oplossing staan los van elkaar: het probleem is niet "we hebben geen AI".',
              'Output en beslissing zijn apart beschreven, met wie beslist.',
              'Bij betrokkenen staan ook mensen die het systeem niet zelf gebruiken.',
              'Bij generatieve AI is duidelijk wat het systeem maakt, wie het antwoord ziet, en welke gegevens naar een externe dienst gaan.',
              'De afbakening noemt concreet wat niet wordt onderzocht.',
              'De casus is haalbaar en de bewijsbronnen zijn concreet, inclusief wat A-AI2 en A-DG opleveren.',
              'Elke zorg noemt wie geraakt wordt en hoe.']:
        para(doc, '☐  ' + c, 9, space_after=1)
    aiverklaring_blok(doc)
    return doc


# ---------------------------------------------------------------- 2. K5
K5 = [('1. Identificatie', 'Het dilemma in één zin, de beslisvraag, en waar in het proces dit speelt. Schrijf de beslisvraag zo: "Moeten / mogen wij [handeling], ondanks [wat daardoor onder druk komt]?"', '60 woorden', 1.8),
      ('2. Feiten en onzekerheid', 'Wat is aangetoond (met bronnummer, bijvoorbeeld [B4] of [D8])? Wat wordt aangenomen? Wat zou je oordeel kunnen veranderen? Houd die drie uit elkaar.', '120 woorden', 2.6),
      ('3. Stakeholders', 'Wie wordt direct en indirect geraakt? Wie heeft weinig invloed maar kan veel schade lijden?', '80 woorden', 2.0),
      ('4. Waarden', 'Waarde A en waarde B: welke twee waarden of plichten botsen, en welke UNESCO-principes spelen en waarom?', '60 woorden', 1.8),
      ('5. Alternatieven', 'Minstens drie reële opties, waarvan één minder ingrijpend of zonder AI.', '100 woorden', 2.2),
      ('6. Lens: gevolgen (utilitarisme)', 'Baten en schade, voor wie, op korte en lange termijn. Sluit af met een conclusie: welke optie is vanuit deze lens het best?', '90 woorden', 2.2),
      ('7. Lens: rechten en plichten (deontologie)', 'Welke rechten en plichten spelen? Is er een grens die je niet tegen nut mag wegstrepen? Conclusie.', '90 woorden', 2.2),
      ('8. Lens: rechtvaardigheid (rechtvaardigheidstheorie, Rawls)', 'Hoe zijn baten, fouten en lasten verdeeld? Wordt een groep structureel benadeeld? Conclusie.', '90 woorden', 2.2),
      ('9. Lens: professionele integriteit (deugdethiek en beroepscodes)', 'Wat vraagt zorgvuldig professioneel handelen? Verzwakt AI het vakmanschap of de relatie met de klant? Conclusie.', '90 woorden', 2.2),
      ('10. Synthese', 'Waar botsen de lenzen? Wat is jouw oordeel en waarom? Onder welke voorwaarden? Wat geef je op, en welke spanning blijft? "Het is een afweging" is geen oordeel.', '150 woorden', 3.0),
      ('11. Vertaling naar risico', 'Welke risico-ID\'s in het risicoregister van de groep (H5) volgen uit dit dilemma?', '30 woorden', 1.2)]


def k5():
    doc = newdoc('K5 Ethical Dilemma Canvas (individueel)')
    title(doc, 'K5 · Ethical Dilemma Canvas', 'Blok 1 · individueel · Assessment 1, individueel deel (40% van A1, 12% van het eindcijfer) · 800 tot 1.000 woorden')
    note(doc, ['Je werkt één dilemma uit de casus van je groep volledig uit. Stem in de groep af dat iedereen een ander dilemma kiest.',
               'Omvang 800 tot 1.000 woorden, zonder kopjes, tabelkoppen en bronnenlijst. Zet het aantal woorden hieronder. Boven 1.100 woorden lezen we niet verder; onder 720 ontbreken bijna altijd onderdelen.',
               'Werk alle vier de lenzen uit, elk met een eigen conclusie. Minimaal drie lenzen goed uitgewerkt is nodig voor een voldoende.',
               'Je mag het bewijs van je groep gebruiken; de redenering is van jou. Lever één pdf in.',
               WEG], 'Zo gebruik je dit canvas')
    kv(doc, [('Naam', ''), ('Studentnummer', ''), ('Groep', ''), ('Dilemma', 'In één zin, en het risico-ID uit H5 dat erbij hoort, bijvoorbeeld R-02'), ('Aantal woorden', '')])
    for kop, vraag, rl, hgt in K5:
        section(doc, kop, vraag, hgt, rl)
    h(doc, 'Check vóór het inleveren')
    for c in ['De beslisvraag is een echt dilemma: twee waarden die allebei zwaar wegen.',
              'Feiten (met bronnummer), aannames en onzekerheden staan apart.',
              'Alle vier de lenzen zijn toegepast, elk met een eigen conclusie en de naam van de theorie.',
              'Het oordeel volgt uit de lenzen, zegt wat je opgeeft en welke spanning blijft.',
              'Minstens één risico in het risicoregister van de groep (H5) is herleidbaar naar dit canvas.']:
        para(doc, '☐  ' + c, 9, space_after=1)
    aiverklaring_blok(doc, groep=False)
    return doc


# ---------------------------------------------------------------- 3. Tussenrapport A1
A1H = [('Samenvatting', '¼ pagina', '', 'De toepassing, de belangrijkste bevindingen en het voorlopig oordeel in één alinea.', 1.6),
       ('1. Toepassing en afbakening', '¾ pagina', 'K1', 'Wat doet de AI, voor wie, welk besluit ondersteunt of neemt het, wat valt buiten het onderzoek? Werk bij met de feedforward van 11 januari.', 2.4),
       ('2. Stakeholders en impact', '1¼ pagina', 'K2', 'Wie wordt geraakt, direct en indirect? Welke groepen zijn kwetsbaar, en wie heeft invloed? Hoe zijn ze gehoord? K2 is de eerste helft van de AI-impactbeoordeling.', 2.8),
       ('3. Proces en data', '1 pagina', 'K3', 'Hoe komt het besluit tot stand? Welke data, van waar naar waar? Waar zit de mens? Markeer elke externe dienst (bijvoorbeeld n8n, een taalmodel-API, een vectordatabase, hosting): welke gegevens gaan erheen en waar staan ze?', 2.6),
       ('4. Nulmeting', '2 pagina\'s', 'K4', 'Snelle scan van alle 11 domeinen, elk met een score en een bronnummer. Werk 3 tot 4 domeinen diep uit, met bewijs en bewijssterkte, en noem de belangrijkste gaps. Samen met hoofdstuk 2 is dit jullie AI-impactbeoordeling. Deden jullie practicum 4? Gebruik minstens twee uitkomsten als bewijs.', 4.0),
       ('5. Risico\'s en plan van aanpak', '2½ pagina\'s', 'K6', 'Bovenaan de regel "EU-risicoklasse en rol": de klasse, de onderbouwing (artikel of bijlage van de AI-verordening) en de rol van de partner; ter vergelijking, want de verordening geldt niet in Suriname. Daaronder de 5 belangrijkste risico\'s, geschreven als oorzaak, gebeurtenis, schade, voor wie, met kans, impact en de besproken escalaties. Sluit af met het voorlopig oordeel (met voorwaarden en onzekerheden) en het plan van aanpak: de drie risico\'s die jullie eerst aanpakken, het ontbrekende bewijs, de taakverdeling en de planning tot 11 maart.', 4.6)]


def tussenrapport():
    doc = newdoc('Sjabloon tussenrapport (Assessment 1)')
    title(doc, 'Tussenrapport · Assessment 1', 'Groepsdeel · 60% van A1 (18% van het eindcijfer) · inleveren donderdag 4 februari, 23:59 · maximaal 8 pagina\'s plus bijlagen')
    note(doc, ['De pagina\'s per hoofdstuk zijn een richtlijn. Het totaal van 8 pagina\'s is een eis: wat erna komt, lezen we niet.',
               'Vormeisen: lettertype 11 punt, regelafstand 1,15, gewone marges; één vaste bronstijl (bij voorkeur APA 7); één pdf, ingeleverd door één groepslid.',
               'Werk je met een echte organisatie? Noem geen namen van medewerkers of klanten; gebruik functies. Geen persoonsgegevens in bijlagen.',
               WEG], 'Zo gebruik je dit sjabloon')
    h(doc, 'Voorblad')
    voorblad(doc, 'A1', A1H)
    pagebreak(doc)
    for kop, oms, basis, txt, hgt in A1H:
        section(doc, kop, txt, hgt, oms + (f' · basis {basis}' if basis else ''))
    pagebreak(doc)
    h(doc, 'Bijlagen (tellen niet mee voor de 8 pagina\'s)')
    hint(doc, 'Bijlagen zijn bewijs, geen verlengstuk van het betoog. Een conclusie die alleen in een bijlage staat, telt niet.')
    for k, v, hg in [('Bijlage A · Bewijsoverzicht', 'Genummerde lijst van alle bronnen: documenten, interviews (datum, functie, geen naam), observaties, eigen tests, en stukken uit A-AI2 en A-DG. In de tekst verwijs je naar het nummer, bijvoorbeeld [B4]. Suribank-route: dossiernummers [D1] tot en met [D12].', 2.2),
                     ('Bijlage B · Volledige nulmetingtabellen', 'Van de diep onderzochte domeinen.', 1.4),
                     ('Bijlage C · Export uit het werkboek', 'Het tabblad Risk_Register (alle risico\'s, ook die buiten de top 5).', 1.4),
                     ('Bijlage D · Testverslag van practicum 4 (sterk aanbevolen)', 'Hoogstens twee pagina\'s, met het testlogboek. Verwijzen jullie naar practicum 2 of 3? Voeg dan ook die uitkomsten toe. Een eigen test is het sterkste bewijs voor de nulmeting (criterium 2, niveau goed).', 2.0)]:
        section(doc, k, v, hg)
    h(doc, 'Inlevercheck')
    for c in ['Elk hoofdstuk heeft een eigenaar op het voorblad.',
              'De feedforward op K1 (11 januari) en op het concept van K2 tot en met K4 (25 januari) is verwerkt.',
              'Alle 11 domeinen hebben een score en een bronnummer; 3 tot 4 domeinen zijn diep uitgewerkt.',
              'Deden jullie practicum 4? Dan zit het testverslag als bijlage D bij en staan minstens twee uitkomsten als bewijs in hoofdstuk 4.',
              'Boven het risicoregister staat de regel EU-risicoklasse en rol.',
              'Elk risico is geschreven als oorzaak, gebeurtenis, schade, voor wie; elke escalatievlag is besproken.',
              'Elk risico is herleidbaar naar een gap uit hoofdstuk 4 of een dilemma uit een canvas.',
              'Het voorlopig oordeel volgt uit de hoofdstukken ervoor, en noemt wat het nog kan veranderen.',
              'Het plan van aanpak noemt drie risico\'s, het ontbrekende bewijs, de taakverdeling en data tot 11 maart.',
              'Maximaal 8 pagina\'s, AI-verklaring aanwezig, één pdf. De dilemma-canvassen lever je elk apart in.']:
        para(doc, '☐  ' + c, 9, space_after=1)
    aiverklaring_blok(doc)
    return doc


# ---------------------------------------------------------------- 4. Eindrapport A2
MEMO = [('Ons oordeel', 'Eén van drie: verantwoord inzetbaar, inzetbaar onder voorwaarden, of nu niet. "Nu niet" is een volwaardig advies. Zeg in één of twee zinnen wat dat concreet betekent.'),
        ('Waarom', 'De twee of drie belangrijkste redenen, met de cijfers uit jullie bewijs (en de hertest, als jullie die deden) en een verwijzing naar het hoofdstuk.'),
        ('Wat het oplevert', 'De baat van de toepassing, eerlijk gewogen.'),
        ('Voorwaarden', 'Per voorwaarde: wat moet er gebeuren, wie is eigenaar, wanneer, en wat gebeurt er als het niet lukt.'),
        ('Restrisico', 'Wat ondanks alles kan misgaan, voor wie, en wie dat restrisico accepteert.'),
        ('Wat ons oordeel kan veranderen', 'Een harde grens die vooraf is vastgelegd: bij welke uitkomst adviseren jullie iets anders?'),
        ('Managementreview', 'Dit memo is de managementreview (ISO/IEC 42001, 9.3). Noem het stopcriterium uit hoofdstuk 8 en de datum van de volgende review.')]
A2H = [('1 tot en met 5. Het tussenrapport, herzien', '5 pagina\'s', 'A1 en feedback', 'Toepassing, stakeholders, proces en data, nulmeting, en risico\'s, herzien met de feedback op Assessment 1 en ingekort waar het kan. Schrap wat niet nodig is voor het advies, verplaats details naar de bijlagen en verwijs naar A-AI2 en A-DG. Houd de regel "EU-risicoklasse en rol" boven het risicoregister. Het plan van aanpak uit A1 vervalt: wat jullie deden, staat in hoofdstuk 6 tot en met 8.', 4.0),
       ('6. Maatregelen', '2½ pagina\'s', 'K7', 'Per risico uit de top 5: de eis (met de norm waarop die rust), 2 tot 3 maatregelen (voorkomen, opsporen, herstellen), de eigenaar, hoe je controleert dat de maatregel werkt, en het restrisico. Geef aan welke maatregelen via A-AI2 zijn ingebouwd. Elke maatregel heeft een verwijzing in de kolom Kader (artikel uit de AI-verordening, Annex A-gebied van ISO/IEC 42001, ontologie van IEEE CertifAIEd of functie van NIST AI RMF). Deden jullie een hertest? Vat de uitkomst hier samen; het verslag gaat in bijlage F.', 4.2),
       ('7. Menselijke controle, bezwaar en governance', '2 pagina\'s', 'K7 (vervolg), RACI', 'Ontwerp van de menselijke controle met de zes voorwaarden en een rekensom; de bezwaarroute; de kern van de transparantieverklaring. Bij een chatbot: de AI-melding en de overdracht aan een mens. Governance: wie is eindverantwoordelijk, wie mag stoppen, wie accepteert restrisico, en één AI-beleidsregel van hoogstens 100 woorden die de partner kan overnemen. De RACI en de leverancierscheck staan in bijlage C.', 3.6),
       ('8. Monitoring en stopcriterium', '1½ pagina', 'K8', 'Fasering; indicatoren voor ethische signalen met grens, actie en eigenaar; verwijzing naar A-AI2 en A-DG voor techniek en data. Verplicht: de incidentroute (wat is een incident, wie meldt aan wie, binnen welke termijn) en het stopcriterium (wanneer gaat het systeem uit of terug naar handwerk, en wie beslist dat). Sluit af met een korte conclusie die naar het beslismemo leidt.', 3.4)]


def eindrapport():
    doc = newdoc('Sjabloon eindrapport (Assessment 2)')
    title(doc, 'Eindrapport · Assessment 2', 'Groepsdeel · 60% van A2 (42% van het eindcijfer) · inleveren donderdag 11 maart, 23:59 · maximaal 12 pagina\'s plus bijlagen')
    note(doc, ['Het totaal van 12 pagina\'s is een eis: wat erna komt, lezen we niet. De richtlijn per onderdeel is een advies.',
               'Vormeisen: lettertype 11 punt, regelafstand 1,15, gewone marges; één vaste bronstijl; één pdf, ingeleverd door één groepslid.',
               'Waar A-AI2 of A-DG iets al vastlegt, verwijzen jullie daarnaar in plaats van het te herhalen.',
               WEG], 'Zo gebruik je dit sjabloon')
    h(doc, 'Voorblad')
    voorblad(doc, 'A2', A2H)
    pagebreak(doc)
    h(doc, 'Beslismemo  ·  1 pagina, vooraan')
    hint(doc, 'Voor de beslisser bij de partner. Aan: [functie] · Van: [groep] · Datum: [datum] · Onderwerp: advies over [oplossing].')
    t = table(doc, ['Onderdeel', 'Wat erin staat'], [4.2, 12.8], rows=len(MEMO))
    for i, (k, v) in enumerate(MEMO, 1):
        celltext(t.rows[i].cells[0], k, 9, True, color=INK); celltext(t.rows[i].cells[1], v, 8.5, hint=True); minheight(t.rows[i], 1.6)
    pagebreak(doc)
    for kop, oms, basis, txt, hgt in A2H:
        section(doc, kop, txt, hgt, oms + f' · basis {basis}')
    pagebreak(doc)
    h(doc, 'Bijlagen (tellen niet mee voor de 12 pagina\'s)')
    for k, v, hg in [('Bijlage A · Bewijsoverzicht (bijgewerkt)', 'Genummerde lijst van alle bronnen, aangevuld sinds Assessment 1.', 1.3),
                     ('Bijlage B · Volledige nulmetingtabellen', '', 1.2),
                     ('Bijlage C · Exports uit het werkboek', 'Risk_Register met restrisico, Design_Requirements, Controls met de kolom Kader, Leverancierscheck, Human_Oversight, Governance_RACI (alleen ethische beslissingen; precies één A per activiteit).', 1.8),
                     ('Bijlage D · Transparantieverklaring en leestest', 'De volledige A4 voor de eindgebruiker en de uitkomst van de leestest.', 1.4),
                     ('Bijlage E · Verwerkingslijst', 'Alle feedbackpunten: de actiepunten uit de feedback op Assessment 1 (18 februari en college 3), de feedback uit de Design Review en de peerfeedback (9 maart). Per punt: nummer, bron, feedbackpunt, besluit (overgenomen, deels, niet overgenomen), wat jullie veranderden of waarom niet, en waar in het rapport. "Geen tijd" is geen argument.', 2.4),
                     ('Bijlage F · Ingebouwd en hertest', 'Bewijs dat maatregelen zijn ingebouwd via A-AI2 (nodig voor criterium 6, niveau goed). Deden jullie een hertest (practicum 4 opnieuw, niet verplicht, telt mee voor excellent)? Zet dan de eerste uitkomsten naast die van de hertest, met de testlogboeken.', 2.2),
                     ('Bijlage G · Incidentoverzicht (aanbevolen)', 'Detail bij de incidentroute uit hoofdstuk 8: per soort incident wanneer iets een incident is, aan wie je meldt en binnen welke termijn. De kern blijft in hoofdstuk 8.', 1.8)]:
        section(doc, k, v, hg)
    h(doc, 'Inlevercheck')
    for c in ['Het beslismemo staat vooraan, past op één pagina, en noemt het stopcriterium en de datum van de volgende review.',
              'De actiepunten uit de feedback op Assessment 1, de Design Review en de peerfeedback zijn verwerkt (bijlage E).',
              'Elk risico uit de top 5 is te volgen tot een eis, maatregelen, een eigenaar, een indicator en een restrisico.',
              'Elke maatregel heeft een verwijzing in de kolom Kader.',
              'Menselijke controle heeft alle zes voorwaarden en een rekensom. Bij een chatbot: AI-melding, overdracht aan een mens en een vaste testset met lastige vragen.',
              'De bezwaarroute en de transparantieverklaring kloppen met elkaar en met het ontwerp.',
              'Elke activiteit in de RACI heeft precies één A; er is een AI-beleidsregel.',
              'Elke indicator heeft een grens, een actie en een eigenaar, en gaat over een ethisch signaal; de incidentroute en het stopcriterium staan in hoofdstuk 8.',
              'Het eindoordeel is één van de drie uitkomsten, volgt uit het rapport en noemt voorwaarden en restrisico.',
              'Maximaal 12 pagina\'s, AI-verklaring, één pdf.']:
        para(doc, '☐  ' + c, 9, space_after=1)
    aiverklaring_blok(doc)
    return doc


# ---------------------------------------------------------------- 5. Reflectie
def reflectie():
    doc = newdoc('Sjabloon reflectie (Assessment 2)')
    title(doc, 'Reflectie · Assessment 2', 'Individueel · 40% van A2 (28% van het eindcijfer) · inleveren donderdag 11 maart, 23:59 · 1.500 tot 2.000 woorden')
    note(doc, ['Een reflectie is geen verslag van wat je deed. Schrijf in de ik-vorm: het gaat over jou, niet over de groep.',
               'Gebruik bij elke vraag de vijf stappen (naar Korthagen): wat gebeurde er (concreet moment, met datum of college); wat dacht, voelde en deed je; wat was de kern; welke alternatieven zie je nu; wat doe je voortaan.',
               'Verwijs minstens vier keer naar eigen materiaal: je evidence cards, je standpunten uit de kennischecks en exit tickets, testverslagen, je dilemma-canvas en de feedback erop, feedback uit de Design Review of van de peergroep. Citeer jezelf letterlijk waar dat helpt.',
               '1.500 tot 2.000 woorden; boven 2.200 lezen we niet verder. Eén pdf.',
               WEG], 'Zo gebruik je dit sjabloon')
    kv(doc, [('Naam', ''), ('Studentnummer', ''), ('Groep en casus', ''), ('Aantal woorden', '')])
    R = [('Inleiding', '150 woorden', 'Je casus in twee zinnen, en waar je stond aan het begin van de module.', 2.0),
         ('Vraag 1 · Het lastigste dilemma', '400 woorden', 'Welk dilemma vond je het lastigst, en waarom? Niet: welk dilemma was het belangrijkst. Waar twijfelde je echt, en waar twijfel je nog?', 4.0),
         ('Vraag 2 · De aanname die onjuist bleek', '350 woorden', 'Over de toepassing, over de organisatie, over AI, of over jezelf. Hoe kwam je erachter?', 3.6),
         ('Vraag 3 · De feedback die je oordeel veranderde', '350 woorden', 'Van de docent, het panel, een peergroep, een groepsgenoot of een stakeholder. Wat dacht je ervoor, en wat erna? Vergelijk een standpunt uit kennischeck 1 met een van later.', 3.6),
         ('Vraag 4 · Je rol in het team', '350 woorden', 'Wat deed je, wat liet je liggen, en wat zou je de volgende keer anders doen? Eerlijk over de samenwerking, zonder anderen de schuld te geven.', 3.6),
         ('Afsluiting', '250 woorden', 'Wat je meeneemt als professional die met AI werkt. Eindig met iets wat je echt gaat doen, niet met "ik heb veel geleerd".', 2.8)]
    for kop, rl, txt, hg in R:
        section(doc, kop, txt, hg, rl)
    h(doc, 'Check vóór het inleveren')
    for c in ['Alle vier de vragen zijn beantwoord, in de ik-vorm.',
              'Bij elke vraag een concreet moment, met datum, college of kennischeck.',
              'Minstens vier verwijzingen naar eigen materiaal.',
              'Er staat een moment in waarop je ongelijk had, en wat je daarvan leerde.',
              'Je laat zien welke ethische spanning blijft, met je eigen oordeel.',
              '1.500 tot 2.000 woorden, AI-verklaring onderaan, één pdf.']:
        para(doc, '☐  ' + c, 9, space_after=1)
    h(doc, 'AI-verklaring')
    box(doc, 'Hoogstens 80 woorden. Generatieve AI mag je gebruiken voor taal, niet om je reflectie te schrijven: een reflectie die niet van jou is, is geen reflectie.', 2.0)
    return doc


# ---------------------------------------------------------------- 6. AI-verklaring
def aiverklaring():
    doc = newdoc('AI-verklaring')
    title(doc, 'AI-verklaring', 'Bij elke inlevering in A-ET · groep of individueel')
    note(doc, ['Je mag generatieve AI gebruiken, mits je dat verantwoordt. Deze verklaring hoort onderaan elke inlevering.',
               'Individueel (dilemma-canvas, reflectie): hoogstens 80 woorden. Groep (canvas, tussenrapport, eindrapport): zo kort als het kan.',
               'Het oordeel moet van jou of van de groep zijn. Bij de reflectie mag AI alleen helpen met taal.',
               WEG], 'Zo gebruik je dit formulier')
    kv(doc, [('Inlevering', 'Bijvoorbeeld K1-canvas, tussenrapport, dilemma-canvas, eindrapport, reflectie'),
             ('Naam of groep', ''), ('Datum', '')])
    para(doc, '', space_after=2)
    t = table(doc, ['Welke tool', 'Waarvoor gebruikt', 'Wat we zelf controleerden', 'Waar in het werk'], [3.5, 4.8, 4.9, 3.8], rows=4)
    ex = ['Bijvoorbeeld een chatassistent', 'Tegenargumenten zoeken bij dilemma D-02', 'Elk argument getoetst aan ons bewijs [B4, B7]; twee verzonnen bronnen geschrapt', 'Hoofdstuk 5']
    for j, v in enumerate(ex): celltext(t.rows[1].cells[j], v, 8.5, hint=True)
    for r in t.rows[1:]: minheight(r, 1.2)
    h(doc, 'Wat we bewust niet met AI deden')
    box(doc, 'Bijvoorbeeld: het oordeel, de scores in de nulmeting, de reflectie. Of: geen AI gebruikt.', 1.8)
    h(doc, 'Gegevens')
    para(doc, '☐  We hebben geen persoonsgegevens of vertrouwelijke gegevens van de partner in een AI-tool gezet.', 9, space_after=1)
    para(doc, '☐  Waar we dat wel deden, staat hierboven waarom en met welke toestemming.', 9, space_after=1)
    return doc


if __name__ == '__main__':
    for nm, fn in [('K1_AI_Use_Case_en_Scope_Canvas', k1), ('K5_Ethical_Dilemma_Canvas', k5),
                   ('Sjabloon_tussenrapport_A1', tussenrapport), ('Sjabloon_eindrapport_A2', eindrapport),
                   ('Sjabloon_reflectie_A2', reflectie), ('AI-verklaring', aiverklaring)]:
        fn().save(OUT + nm + '.docx'); print(nm)
