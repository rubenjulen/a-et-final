# Huisstijl-hulpfuncties voor Word-bestanden (uit gen_feedbackforms.py)
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
INK=RGBColor(0x12,0x31,0x2A); GREY=RGBColor(0x6B,0x6B,0x6B); AMBER='E3A92B'; SAND='EDE7DA'; LIGHT='F6F3EC'

def shade(cell,hexc):
    tcPr=cell._tc.get_or_add_tcPr(); s=OxmlElement('w:shd'); s.set(qn('w:val'),'clear'); s.set(qn('w:color'),'auto'); s.set(qn('w:fill'),hexc); tcPr.append(s)
def borders(table,color='BFB6A3'):
    tbl=table._tbl; tblPr=tbl.tblPr; b=OxmlElement('w:tblBorders')
    for e in ('top','left','bottom','right','insideH','insideV'):
        el=OxmlElement(f'w:{e}'); el.set(qn('w:val'),'single'); el.set(qn('w:sz'),'4'); el.set(qn('w:color'),color); b.append(el)
    tblPr.append(b)
def leftbar(par,color=AMBER):
    pPr=par._p.get_or_add_pPr(); bd=OxmlElement('w:pBdr'); l=OxmlElement('w:left')
    l.set(qn('w:val'),'single'); l.set(qn('w:sz'),'24'); l.set(qn('w:space'),'6'); l.set(qn('w:color'),color); bd.append(l); pPr.append(bd)
def run(p,text,size=10,bold=False,italic=False,color=None,font=None):
    r=p.add_run(text); r.font.size=Pt(size); r.bold=bold; r.italic=italic
    if color is not None: r.font.color.rgb=color
    if font: r.font.name=font; r._element.rPr.rFonts.set(qn('w:eastAsia'),font)
    return r
def para(doc_or_cell,text='',size=10,bold=False,italic=False,color=None,font=None,space_after=4,align=None):
    p=doc_or_cell.add_paragraph()
    p.paragraph_format.space_after=Pt(space_after); p.paragraph_format.space_before=Pt(0)
    if text: run(p,text,size,bold,italic,color,font)
    if align: p.alignment=align
    return p
def celltext(cell,text,size=9,bold=False,italic=False,color=None,hint=False):
    cell.text=''
    p=cell.paragraphs[0]; p.paragraph_format.space_after=Pt(2)
    if hint: run(p,text,size,False,True,GREY)
    else: run(p,text,size,bold,italic,color)
def h(doc,text):
    p=doc.add_paragraph(); p.paragraph_format.space_before=Pt(12); p.paragraph_format.space_after=Pt(4); p.paragraph_format.keep_with_next=True
    leftbar(p); run(p,text,13,True,False,INK,'Georgia'); return p
def table(doc,headers,widths,rows=0,head_fill=SAND,size=9):
    t=doc.add_table(rows=1+rows,cols=len(headers)); t.alignment=WD_TABLE_ALIGNMENT.CENTER; borders(t); t.autofit=False
    for i,(hd,w) in enumerate(zip(headers,widths)):
        c=t.rows[0].cells[i]; celltext(c,hd,size,True,color=INK); shade(c,head_fill)
    for row in t.rows:
        for i,w in enumerate(widths): row.cells[i].width=Cm(w)
    # repeat header
    trPr=t.rows[0]._tr.get_or_add_trPr(); th=OxmlElement('w:tblHeader'); th.set(qn('w:val'),'true'); trPr.append(th)
    fixwidths(t,widths)
    return t

def fixwidths(t,widths):
    tbl=t._tbl; tblPr=tbl.tblPr
    lay=OxmlElement('w:tblLayout'); lay.set(qn('w:type'),'fixed'); tblPr.append(lay)
    tw=OxmlElement('w:tblW'); tw.set(qn('w:w'),str(int(sum(widths)*567))); tw.set(qn('w:type'),'dxa')
    for old in tblPr.findall(qn('w:tblW')): tblPr.remove(old)
    tblPr.append(tw)
    grid=tbl.tblGrid
    for gc,w in zip(grid.findall(qn('w:gridCol')),widths): gc.set(qn('w:w'),str(int(w*567)))
    for row in t.rows:
        for c,w in zip(row.cells,widths): c.width=Cm(w)

def minheight(row,cm):
    trPr=row._tr.get_or_add_trPr(); hgt=OxmlElement('w:trHeight'); hgt.set(qn('w:val'),str(int(cm*567))); hgt.set(qn('w:hRule'),'atLeast'); trPr.append(hgt)
def box(doc,hint,height=3.0,text=None):
    t=doc.add_table(rows=1,cols=1); borders(t); fixwidths(t,[17])
    c=t.rows[0].cells[0]
    if text: celltext(c,text,10)
    else: celltext(c,hint,9,hint=True)
    minheight(t.rows[0],height); return t

