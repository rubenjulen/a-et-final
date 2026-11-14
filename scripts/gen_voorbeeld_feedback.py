#!/usr/bin/env python3
"""Maakt 'ICT A-ET Voorbeeld feedback.pdf' uit het ingevulde ClaimWacht-feedbackformulier,
met bovenaan een korte uitleg voor studenten. Draaien vanuit de repository."""
import copy, os, subprocess, sys, tempfile
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from docx_kit import *  # noqa: F401,F403
REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(REPO, 'lesmateriaal', 'feedback', 'Feedbackformulier_A2_groep_voorbeeld_ClaimWacht.docx')
OUT = os.path.join(REPO, 'lesmateriaal', 'algemeen')
d = Document(SRC)
# docentnaam en datum invullen
for t in d.tables:
    for r in t.rows:
        for c in r.cells:
            for p in c.paragraphs:
                for rn in p.runs:
                    rn.text = rn.text.replace('[naam docent]', 'Docent A-ET').replace('[datum]', 'maart 2027')
# uitlegkader bovenaan (na titel en ondertitel)
anchor = d.paragraphs[1]
box_t = d.add_table(rows=1, cols=1); borders(box_t, 'E3A92B'); fixwidths(box_t, [17])
c = box_t.rows[0].cells[0]; shade(c, LIGHT); c.text = ''
p = c.paragraphs[0]; p.paragraph_format.space_after = Pt(3)
run(p, 'Zo ziet de feedback op jullie rapport eruit. ', 9.5, True, color=INK)
run(p, 'Dit is de feedback op het voorbeeldrapport ClaimWacht (een fictieve zorgverzekeraar), dat een 8,2 kreeg. '
       'Na Assessment 1 en Assessment 2 krijgen jullie feedback in precies deze vorm: eerst de kernboodschap, dan per criterium '
       'waarom jullie op dat niveau zitten en wat nodig is voor het volgende niveau, een redeneerketen-check van één risico, '
       'hoogstens vijf actiepunten en het cijfer onderaan.', 9.5)
p2 = c.add_paragraph(); p2.paragraph_format.space_after = Pt(2)
run(p2, 'Na Assessment 1 verwerken jullie elk actiepunt in de verwerkingslijst (bijlage E van het eindrapport): overgenomen, deels overgenomen of niet overgenomen, met waar of waarom.', 9.5)
anchor._p.addnext(box_t._tbl)
spacer = copy.deepcopy(anchor._p); anchor._p.addnext(spacer)
for r in list(spacer):
    if r.tag.endswith('}r'): spacer.remove(r)
spacer2 = copy.deepcopy(spacer); box_t._tbl.addnext(spacer2)
with tempfile.TemporaryDirectory() as tmp:
    tmpdocx = os.path.join(tmp, 'ICT A-ET Voorbeeld feedback.docx')
    d.save(tmpdocx)
    subprocess.run(['soffice', '--headless', '--convert-to', 'pdf', '--outdir', OUT, tmpdocx], check=True,
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
print('ok', os.path.join(OUT, 'ICT A-ET Voorbeeld feedback.pdf'))
