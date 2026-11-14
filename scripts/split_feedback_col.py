import openpyxl, copy, sys
from openpyxl.worksheet.cell_range import CellRange
p=sys.argv[1]
wb=openpyxl.load_workbook(p)
for name in ['A1 Groep','A1 Individueel','A2 Groep','A2 Reflectie']:
    ws=wb[name]
    # extend merges ending at K to L
    for m in list(ws.merged_cells.ranges):
        if m.max_col==11:
            rng=str(m); ws.unmerge_cells(rng)
            for r in range(m.min_row,m.max_row+1):
                src=ws.cell(r,11); dst=ws.cell(r,12); dst._style=copy.copy(src._style)
            ws.merge_cells(start_row=m.min_row,start_column=m.min_col,end_row=m.max_row,end_column=12)
    # copy column K style to L for rows 1..max_row where L empty and not merged
    for r in range(1,ws.max_row+1):
        k=ws.cell(r,11); l=ws.cell(r,12)
        if l.coordinate in ws.merged_cells: continue
        if k.has_style and not l.has_style: l._style=copy.copy(k._style)
    ws['K4'].value='Waarom (met vindplaats)'
    ws['L4'].value='Naar het volgende niveau'
    ws['K5'].value='wat je zag, met hoofdstuk, tabel of zin'
    ws['L5'].value='wat ontbreekt, in de woorden van de rubric'
    ws.column_dimensions['K'].width=40; ws.column_dimensions['L'].width=40
    # criterion rows: those with weight in B and formula in J
    for r in range(6,ws.max_row+1):
        b=ws.cell(r,2).value; j=ws.cell(r,10).value
        if isinstance(b,(int,float)) and isinstance(j,str) and j.startswith('=IF(IF('):
            ws.cell(r,12)._style=copy.copy(ws.cell(r,11)._style); ws.cell(r,12).value=None
    pa=ws.print_area
    if isinstance(pa,list): pa=pa[0]
    ws.print_area=str(pa).split('!')[-1].replace('$K$','$L$')
wb.save(p)
print('ok')
