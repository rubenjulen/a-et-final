#!/usr/bin/env python3
"""ICT A-ET Evidence card (sjabloon, Janssen-huisstijl). Uitvoer: lesmateriaal/instrumenten/Evidence_card.docx"""
import os
from janssen_docx import JanssenDoc
OUT = os.path.join(os.path.dirname(__file__), '..', 'lesmateriaal', 'instrumenten', 'Evidence_card.docx')
d = JanssenDoc()
d.heading('EVIDENCE CARD', 1)
d.label_table([['Naam', ''], ['Groep', ''], ['Evidence card nr.', '(1, 2, 3, 4 of 5)'], ['Practicum of test', ''], ['Datum', '']])
d.para('Vul na het practicum één kaart in, maximaal één pagina. De kaart kan als bijlage in het rapport terugkomen (A1 of A2). Lever in met je AI-verklaring onderaan.', italic=True, size=10)
d.table([['Vraag', 'Jouw antwoord'],
         ['Wat heb ik gedaan?', '\n\n'],
         ['Wat zag ik? Noem minstens twee getallen.', '\n\n'],
         ['Wat veranderde er toen ik iets aanpaste of vergeleek?', '\n\n'],
         ['Waarom gebeurde dat, denk ik?', '\n\n'],
         ['Wat betekent dit ethisch? Gebruik minstens één lens.', '\n\n'],
         ['Wat betekent dit voor onze eigen oplossing?', '\n\n']], header=True, widths=[6.0, 10.5], label_col=True, size=10)
d.heading('Veelgemaakte fouten', 2)
d.bullets(['Alleen getallen noemen. Een goede kaart zegt ook wie de fouten draagt, en welke lens laat zien waarom dat een probleem is.',
           'Eén uitleg voor iedereen. Vraag je af wat de aanvrager, de medewerker en een toezichthouder willen weten.',
           'Geen koppeling met de eigen oplossing. De laatste vraag is de belangrijkste: wat betekent dit voor jullie casus?'])
d.save(OUT)
print('ok', os.path.abspath(OUT))
