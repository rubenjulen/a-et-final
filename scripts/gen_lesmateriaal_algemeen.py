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
WEEKS = [
    ('Week 4', 'zo 31 jan → ma 1 feb', 'Concept K4 diep, K5, K6 en testverslag practicum 4',
     ['Wat is het sterkste punt? Wijs één plek aan waar de redenering overtuigt, en zeg waarom.',
      'Waar ontbreekt bewijs? Noem maximaal drie scores of beweringen zonder bron of met zwak bewijs.',
      'Welke stap in de keten mist? Volg één dilemma: is er een risico dat eruit volgt, en hangt dat risico samen met een gap? Waar breekt de lijn?']),
    ('Week 7', 'zo 21 feb → ma 22 feb', 'Concept K7 (deel 1 herzien en deel 2)',
     ['Wat is het sterkste punt? Welk onderdeel van het ontwerp overtuigt, en waarom?',
      'Waar ontbreekt bewijs? Welke maatregel heeft geen eigenaar, geen verificatie, of is niet uitvoerbaar?',
      'Welke stap in de keten mist? Volg één risico van de top 5: is er een eis, een maatregel, een eigenaar in de RACI, en komt het terug in de menselijke controle of de transparantieverklaring?']),
    ('Week 9', 'zo 7 mrt → ma 8 mrt', 'Concept eindrapport (hertest, K8, beslismemo)',
     ['Wat is het sterkste punt? Welk deel van het advies overtuigt het meest?',
      'Waar ontbreekt bewijs? Welke voorwaarde, indicator of restrisico hangt in de lucht?',
      'Welke stap in de keten mist? Volg één risico van begin tot eind, tot en met het beslismemo. Waar breekt de lijn?']),
]
CHAIN = ['Bewijs', 'Gap', 'Dilemma', 'Risico', 'Eis', 'Maatregel met eigenaar', 'Monitoring', 'Oordeel']


def peerfeedback():
    doc = new_doc('ICT A-ET Peerfeedback · AI & Ethics (A-ET) · peercheck week 4, 7 en 9')
    title(doc, 'Peerfeedback', 'AI & Ethics (A-ET) · peercheck in week 4, 7 en 9 · hoogstens één pagina terug')

    t = doc.add_table(rows=2, cols=4); borders(t); fixwidths(t, [3.6, 4.9, 3.6, 4.9])
    for r, ((a, av), (b, bv)) in enumerate([(('Feedback van groep', '[groep]'), ('Aan groep', '[groep]')),
                                            (('Week', '☐ 4   ☐ 7   ☐ 9'), ('Datum', '[datum]'))]):
        cs = t.rows[r].cells
        celltext(cs[0], a, 9, True, color=INK); shade(cs[0], SAND); celltext(cs[1], av, 9, hint=av.startswith('['))
        celltext(cs[2], b, 9, True, color=INK); shade(cs[2], SAND); celltext(cs[3], bv, 9, hint=bv.startswith('['))

    p = para(doc, '', 8.5, space_after=4); p.paragraph_format.space_before = Pt(6)
    run(p, 'Zo geef je goede feedback: ', 8.5, True, color=INK)
    run(p, 'wees specifiek en noem de vindplaats ("bij 7.2 staat score 3, maar de enige bron is een interview"); '
           'schrijf over het werk, niet over de mensen; scheid wat je ziet van wat je vindt; kies wat het belangrijkst is.', 8.5)

    p = para(doc, '', 8.5, space_after=2)
    run(p, 'Per week extra: ', 8.5, True, color=INK)
    run(p, 'vul ook de checklist van die week in (zie de weekmodule). Week 7: lees de transparantieverklaring als getroffene en '
           'zeg in twee zinnen of je weet wat er gebeurt en wat je kunt doen. Week 9: lees eerst alleen het beslismemo en schrijf op '
           'wat het oordeel is, wat er moet gebeuren, door wie en wanneer. De groep die feedback krijgt, schrijft in het logboek in '
           'twee zinnen wat ze ermee deed.', 8.5)
    h(doc, 'De drie vaste vragen')
    qt = doc.add_table(rows=1, cols=3); borders(qt); fixwidths(qt, [1.6, 9.6, 5.8])
    for i, x in enumerate(['Week', 'De vraag', 'Jullie antwoord']):
        celltext(qt.rows[0].cells[i], x, 9, True, color=INK); shade(qt.rows[0].cells[i], SAND)
    trPr = qt.rows[0]._tr.get_or_add_trPr(); th = OxmlElement('w:tblHeader'); th.set(qn('w:val'), 'true'); trPr.append(th)
    for n in range(3):
        row = qt.add_row().cells
        celltext(row[0], f'Vraag {n + 1}', 9, True, color=INK); shade(row[0], LIGHT)
        cell = row[1]; cell.text = ''
        for i, (wk, _, _, qs) in enumerate(WEEKS):
            p = cell.paragraphs[0] if i == 0 else cell.add_paragraph()
            p.paragraph_format.space_after = Pt(1)
            run(p, wk + ': ', 7.5, True, color=INK); run(p, qs[n], 7.5)
        celltext(row[2], '', 9)
        minheight(qt.rows[-1], 1.5)

    h(doc, 'Redeneerketen-check')
    para(doc, 'Kies één belangrijk risico van de andere groep en volg het door de acht schakels. Gekozen risico: ______________________', 9, space_after=4)
    ct = doc.add_table(rows=1 + len(CHAIN), cols=3); borders(ct); fixwidths(ct, [4.4, 2.6, 10.0])
    for i, x in enumerate(['Schakel', '✓ of breuk', 'Waar in het rapport, of wat ontbreekt']):
        celltext(ct.rows[0].cells[i], x, 9, True, color=INK); shade(ct.rows[0].cells[i], SAND)
    for r, s in enumerate(CHAIN, 1):
        celltext(ct.rows[r].cells[0], s, 9, True, color=INK); shade(ct.rows[r].cells[0], LIGHT)
        celltext(ct.rows[r].cells[1], '☐ ✓   ☐ breuk', 8.5); celltext(ct.rows[r].cells[2], '', 9)

    h(doc, 'Het belangrijkste dat jullie moeten aanpassen')
    box(doc, 'Eén of twee zinnen: wat moet de andere groep als eerste verbeteren, en waarom?', 1.5)

    path = os.path.join(OUT, 'ICT A-ET Peerfeedback.docx')
    doc.save(path); return path


if __name__ == '__main__':
    for f in (toestemming(), peerfeedback()):
        print('ok', f)
