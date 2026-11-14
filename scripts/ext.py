import sys, pptx, openpyxl
for p in sys.argv[2:]:
    out = open(sys.argv[1] + '/' + p.split('/')[-1] + '.txt', 'w')
    if p.endswith('.pptx'):
        prs = pptx.Presentation(p)
        for i, s in enumerate(prs.slides, 1):
            out.write(f'\n=== SLIDE {i} ===\n')
            for sh in s.shapes:
                if sh.has_text_frame:
                    t = ' | '.join(par.text for par in sh.text_frame.paragraphs if par.text.strip())
                    if t: out.write(t + '\n')
                if sh.has_table:
                    for r in sh.table.rows:
                        out.write(' || '.join(c.text.replace('\n', ' / ') for c in r.cells) + '\n')
    else:
        wb = openpyxl.load_workbook(p, data_only=False)
        for ws in wb.worksheets:
            out.write(f'\n=== SHEET {ws.title} ({ws.max_row}x{ws.max_column}) ===\n')
            for row in ws.iter_rows(values_only=True):
                if any(v is not None for v in row):
                    out.write(' | '.join('' if v is None else str(v) for v in row) + '\n')
