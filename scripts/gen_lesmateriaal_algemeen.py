#!/usr/bin/env python3
"""Maakt twee Word-formulieren voor Lesmateriaal op MyCampus:
- ICT A-ET Toestemmingsformulier interview.docx
- ICT A-ET Peerfeedback.docx
Draaien vanuit de repository: python3 scripts/gen_lesmateriaal_algemeen.py
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from docx_kit import *  # noqa: F401,F403  (huisstijl-hulpfuncties)

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(REPO, 'lesmateriaal', 'algemeen')
os.makedirs(OUT, exist_ok=True)


def new_doc(footer):
    doc = Document()
    st = doc.styles['Normal']; st.font.name = 'Arial'; st.font.size = Pt(10)
    st.element.rPr.rFonts.set(qn('w:eastAsia'), 'Arial')
    s = doc.sections[0]; s.page_width = Cm(21); s.page_height = Cm(29.7)
    for m in ('left_margin', 'right_margin'):
        setattr(s, m, Cm(2))
    s.top_margin = Cm(1.6); s.bottom_margin = Cm(1.6)
    run(s.footer.paragraphs[0], footer, 8, color=GREY)
    return doc


def title(doc, text, sub):
    p = para(doc, '', space_after=0); run(p, text, 18, True, False, INK, 'Georgia')
    para(doc, sub, 9, color=GREY, space_after=6)


def kv_table(doc, rows, widths=(4.2, 12.8)):
    t = doc.add_table(rows=len(rows), cols=2); borders(t); fixwidths(t, list(widths))
    for r, (k, v) in enumerate(rows):
        c0, c1 = t.rows[r].cells
        celltext(c0, k, 9, True, color=INK); shade(c0, SAND)
        celltext(c1, v, 9, hint=v.startswith('['))
    return t


def checkbox_line(cell_or_doc, label, options):
    p = para(cell_or_doc, '', space_after=2)
    run(p, label + '   ', 9, True, color=INK)
    run(p, '   '.join('☐ ' + o for o in options), 9)
    return p


# ---------------------------------------------------------------- toestemming
def toestemming():
    doc = new_doc('ICT A-ET Toestemmingsformulier interview · AI & Ethics (A-ET) · minor AI · Janssen University')
    title(doc, 'Toestemming voor een interview',
          'AI & Ethics (A-ET) · minor AI · Janssen University · 2026-2027')
    para(doc, 'Wij zijn studenten van de minor AI van Janssen University. Voor het vak AI & Ethics (A-ET) '
              'onderzoeken we of een AI-oplossing verantwoord kan worden ingezet, en wat daarvoor nodig is. '
              'Uw ervaring helpt ons daarbij. Lees dit formulier en kruis aan waar u mee instemt.', 9.5, space_after=6)

    h(doc, 'Over het interview')
    kv_table(doc, [
        ('Interviewers', '[namen van de studenten]'),
        ('Groep en oplossing', '[groep, naam van de AI-oplossing]'),
        ('Doel', 'Een studieopdracht van A-ET: inzicht in hoe de AI-oplossing wordt gebruikt, wie erdoor wordt geraakt en welke afspraken er zijn.'),
        ('Duur', 'Ongeveer 30 tot 45 minuten.'),
        ('Contact docent', '[naam en e-mail docent]'),
    ])

    h(doc, 'Wat er met uw antwoorden gebeurt')
    for t in [
        'We gebruiken uw antwoorden alleen voor deze studieopdracht.',
        'In het rapport noemen we uw naam en de naam van de organisatie niet, tenzij u daarvoor hieronder toestemming geeft.',
        'We nemen het gesprek alleen op als u dat goedvindt. Anders maken we aantekeningen.',
        'Meedoen is vrijwillig. U mag elke vraag overslaan en op elk moment stoppen, zonder reden.',
        'We bewaren aantekeningen en opnamen alleen zolang de module loopt, en verwijderen ze uiterlijk na de beoordeling (maart 2027). '
        'Alleen de studenten van de groep en de docent kunnen erbij.',
        'U kunt vragen om uw antwoorden in te zien of te laten verwijderen. Neem dan contact op met de interviewers of de docent.',
    ]:
        p = para(doc, '', 9.5, space_after=2); run(p, '•  ', 9.5, True, color=INK); run(p, t, 9.5)

    h(doc, 'Uw keuzes')
    t = doc.add_table(rows=4, cols=2); borders(t); fixwidths(t, [8.0, 9.0])
    rows = [('Ik doe mee aan het interview', ['ja', 'nee']),
            ('Het gesprek mag worden opgenomen (alleen geluid)', ['ja', 'nee']),
            ('Mijn uitspraken mogen worden geciteerd', ['anoniem', 'met mijn functie', 'niet']),
            ('De naam van de organisatie mag in het rapport', ['ja', 'nee'])]
    for r, (q, opts) in enumerate(rows):
        c0, c1 = t.rows[r].cells
        celltext(c0, q, 9, True, color=INK); shade(c0, LIGHT)
        celltext(c1, '    '.join('☐ ' + o for o in opts), 9.5)

    h(doc, 'Ondertekening')
    t = doc.add_table(rows=4, cols=3); borders(t); fixwidths(t, [4.2, 6.4, 6.4])
    heads = ['', 'Geïnterviewde', 'Interviewer (namens de groep)']
    for i, x in enumerate(heads):
        celltext(t.rows[0].cells[i], x, 9, True, color=INK); shade(t.rows[0].cells[i], SAND)
    for r, lab in enumerate(['Naam', 'Datum', 'Handtekening'], 1):
        celltext(t.rows[r].cells[0], lab, 9, True, color=INK); shade(t.rows[r].cells[0], SAND)
        celltext(t.rows[r].cells[1], '', 9); celltext(t.rows[r].cells[2], '', 9)
        minheight(t.rows[r], 0.9 if lab != 'Handtekening' else 1.4)
    para(doc, 'Maak twee exemplaren: één voor de geïnterviewde, één voor de groep. Bewaar het getekende formulier bij jullie bewijs (bijlage van het rapport); '
              'neem het formulier zelf niet op in het rapport als er namen op staan.', 8.5, italic=True, color=GREY, space_after=0)
    path = os.path.join(OUT, 'ICT A-ET Toestemmingsformulier interview.docx')
    doc.save(path); return path


# ---------------------------------------------------------------- peerfeedback
# Eén ronde in blok 3: concept eindrapport (zo 7 maart) -> feedback terug (di 9 maart). Gelijk aan kennispakket 3.
QUESTIONS = [
    ('Wat is het sterkste punt?', 'Welk deel van het advies overtuigt het meest, en waarom?'),
    ('Waar ontbreekt bewijs?', 'Welke voorwaarde, indicator of welk restrisico hangt in de lucht? Noem de vindplaats.'),
    ('Welke stap in de keten mist?', 'Volg één risico: dilemma of gap, risico, eis, maatregel met eigenaar, test of hertest, indicator, restrisico, terug in het memo. Waar breekt de lijn?'),
]
CHECKS = [
    'Beslismemo: één pagina, oordeel in de eerste zin',
    'Beslismemo: voorwaarden met eigenaar, datum en gevolg',
    'Beslismemo: baten en restrisico benoemd, met wie het accepteert',
    'Beslismemo: stopcriterium en datum van de volgende review',
    'H6: per risico uit de top 5 een eis, maatregelen met eigenaar, en een restrisico',
    'Bijlage F: bewijs dat minstens twee maatregelen zijn ingebouwd via A-AI2',
    'Als er een hertest is: eerste test en hertest naast elkaar, met per maatregel de conclusie',
    'H8: drie fasen, met eigenaar en middelen per maatregel',
    'H8: vijf tot acht ethische signalen, met grens, actie en wie besluit',
    'H8: minstens één vroeg signaal en één indicator die tot stilzetten kan leiden',
    'H8: incidentroute en stopcriterium, concreet voor deze oplossing',
    'Het oordeel in het memo volgt uit H6, H8 en het bewijs',
    "Maximaal 12 pagina's, verwerkingslijst aanwezig (bijlage E)",
]


def peerfeedback():
    doc = new_doc('ICT A-ET Peerfeedback · AI & Ethics (A-ET) · blok 3, concept eindrapport')
    title(doc, 'Peerfeedback', 'AI & Ethics (A-ET) · blok 3 · concept eindrapport · terug vóór dinsdag 9 maart, 23:59')

    t = doc.add_table(rows=2, cols=4); borders(t); fixwidths(t, [3.6, 4.9, 3.6, 4.9])
    for r, ((a, av), (b, bv)) in enumerate([(('Feedback van groep', '[groep]'), ('Aan groep', '[groep]')),
                                            (('Concept ontvangen', '[datum]'), ('Teruggestuurd', '[datum]'))]):
        cs = t.rows[r].cells
        celltext(cs[0], a, 9, True, color=INK); shade(cs[0], SAND); celltext(cs[1], av, 9, hint=av.startswith('['))
        celltext(cs[2], b, 9, True, color=INK); shade(cs[2], SAND); celltext(cs[3], bv, 9, hint=bv.startswith('['))

    p = para(doc, '', 8.5, space_after=4); p.paragraph_format.space_before = Pt(6)
    run(p, 'Zo geef je bruikbare feedback: ', 8.5, True, color=INK)
    run(p, 'wees concreet en noem de vindplaats ("indicator 3 in H8 heeft geen grens"); zeg wat je mist en doe een voorstel; '
           'begin bij wat het zwaarst weegt (het oordeel en de keten gaan voor taal en vorm); je geeft geen cijfer. '
           'Stuur het formulier via [kanaal] terug, met de docent in de cc.', 8.5)

    h(doc, 'Stap 1. Lees eerst alleen het beslismemo (5 minuten)')
    para(doc, 'Ieder voor zich, zonder het rapport te lezen. Wat is het oordeel, wat moet er gebeuren, door wie, en wanneer? '
              'Lezen jullie allemaal hetzelfde? Lukt het niet, dan is dat jullie eerste feedbackpunt.', 8.5, space_after=4)
    box(doc, 'Het oordeel zoals wij het lazen, en wat er moet gebeuren, door wie en wanneer:', 1.4)

    h(doc, 'Stap 2. De drie vragen')
    qt = doc.add_table(rows=1, cols=2); borders(qt); fixwidths(qt, [6.0, 11.0])
    for i, x in enumerate(['De vraag', 'Jullie antwoord']):
        celltext(qt.rows[0].cells[i], x, 9, True, color=INK); shade(qt.rows[0].cells[i], SAND)
    trPr = qt.rows[0]._tr.get_or_add_trPr(); th = OxmlElement('w:tblHeader'); th.set(qn('w:val'), 'true'); trPr.append(th)
    for n, (q, uitleg) in enumerate(QUESTIONS, 1):
        row = qt.add_row().cells
        cell = row[0]; cell.text = ''; p = cell.paragraphs[0]
        run(p, f'{n}. {q} ', 8.5, True, color=INK); run(p, uitleg, 8)
        shade(row[0], LIGHT); celltext(row[1], '', 9)
        minheight(qt.rows[-1], 1.6)

    h(doc, 'Stap 3. De checklist')
    ck = doc.add_table(rows=1 + len(CHECKS), cols=2); borders(ck); fixwidths(ck, [13.0, 4.0])
    for i, x in enumerate(['Controle', 'Ja / nee / deels']):
        celltext(ck.rows[0].cells[i], x, 9, True, color=INK); shade(ck.rows[0].cells[i], SAND)
    for r, c in enumerate(CHECKS, 1):
        celltext(ck.rows[r].cells[0], c, 8.5); celltext(ck.rows[r].cells[1], '☐ ja  ☐ nee  ☐ deels', 8)

    h(doc, 'Het belangrijkste dat jullie moeten aanpassen')
    box(doc, 'Eén of twee zinnen: wat moet de andere groep als eerste verbeteren, en waarom?', 1.5)
    para(doc, 'De groep die de feedback krijgt, zet elk punt in de verwerkingslijst (bijlage E), met als bron "Peergroep (9 maart)" en een besluit.',
         8, italic=True, color=GREY, space_after=0)

    path = os.path.join(OUT, 'ICT A-ET Peerfeedback.docx')
    doc.save(path); return path


if __name__ == '__main__':
    for f in (toestemming(), peerfeedback()):
        print('ok', f)
