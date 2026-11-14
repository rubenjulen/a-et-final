import json, copy
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.section import WD_ORIENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

OUT='out/feedback/'
INK=RGBColor(0x12,0x31,0x2A); GREY=RGBColor(0x6B,0x6B,0x6B); AMBER='E3A92B'; SAND='EDE7DA'; LIGHT='F6F3EC'
C=json.load(open(OUT+'criteria.json'))

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

RULES=[('Wijs aan','noem hoofdstuk, tabel of zin.'),('Over het werk, niet over de persoon',''),('Gebruik de woorden van de rubric','van het niveau erboven.'),('Kies en rangschik','hoogstens drie moet-punten, belangrijkste eerst.'),('Lof alleen als hij specifiek is','zeg wat werkt en waarom.'),('Geef de opdracht, niet de oplossing',''),('Scheid wat je ziet van wat je vindt','"ik zie geen grens" in plaats van "dit is fout".'),('Gewone taal','korte zinnen, jullie-vorm, begrippen uit de module.')]
CHAIN_G=['Bewijs','Gap','Dilemma','Risico','Eis','Maatregel met eigenaar','Monitoring','Oordeel']
CHAIN_I=['Beslisvraag','Feiten','Waarden','Opties','Lenzen','Oordeel']

def build(kind, fill=None):
    # kind: A1G, A1I, A2G, A2R
    key={'A1G':'A1 Groep','A1I':'A1 Individueel','A2G':'A2 Groep','A2R':'A2 Reflectie'}[kind]
    d=C[key]; group=kind in ('A1G','A2G'); a1=kind.startswith('A1')
    doc=Document()
    st=doc.styles['Normal']; st.font.name='Arial'; st.font.size=Pt(10); st.element.rPr.rFonts.set(qn('w:eastAsia'),'Arial')
    s=doc.sections[0]; s.page_width=Cm(21); s.page_height=Cm(29.7)
    for m in ('left_margin','right_margin'): setattr(s,m,Cm(2))
    s.top_margin=Cm(1.8); s.bottom_margin=Cm(1.8)
    fp=s.footer.paragraphs[0]; run(fp,'AI & Ethics (A-ET) · feedbackformulier · '+d['title'].split(' · ',1)[1],8,color=GREY)
    title=d['title'].split(' · ',1)[1]
    p=para(doc,'',space_after=0); run(p,'Feedback · '+title,18,True,False,INK,'Georgia')
    para(doc,'AI & Ethics (A-ET) · minor AI · Janssen University · 2026-2027',9,color=GREY,space_after=8)
    # header table
    lab1='Groep' if group else 'Student'
    t=doc.add_table(rows=3,cols=4); borders(t)
    labels=[(lab1,'Casus (oplossing, partner)'),('Beoordelaar','Datum'),('Toets','Weging')]
    vals=fill['head'] if fill else [('',''),('',''),(title, d['share'].split('. ')[0])]
    if not fill: vals=[('',''),('',''),(title,d['share'].split('. ')[0])]
    for r,((l1,l2),(v1,v2)) in enumerate(zip(labels,vals)):
        cs=t.rows[r].cells
        celltext(cs[0],l1,9,True,color=INK); shade(cs[0],SAND); celltext(cs[1],v1,9)
        celltext(cs[2],l2,9,True,color=INK); shade(cs[2],SAND); celltext(cs[3],v2,9)
    fixwidths(t,[3.2,5.3,3.2,5.3])
    # rules box
    para(doc,'',space_after=2)
    rb=doc.add_table(rows=1,cols=1); borders(rb,'E3A92B'); fixwidths(rb,[17]); c=rb.rows[0].cells[0]; shade(c,LIGHT)
    celltext(c,'Schrijfregels',9,True,color=INK)
    for a,b in RULES:
        pp=c.add_paragraph(); pp.paragraph_format.space_after=Pt(0); run(pp,'• '+a,8,True); 
        if b: run(pp,': '+b,8)
    pp=c.add_paragraph(); pp.paragraph_format.space_after=Pt(2)
    run(pp,'Volgorde: eerst begrijpen, dan het detail, dan wat je gaat doen; het cijfer pas aan het eind.',8,italic=True,color=GREY)
    # 1 Kernboodschap
    h(doc,'1. Kernboodschap')
    if group: hint='Hoogstens vijf zinnen. Eén zin: wat jullie adviseren en of het overtuigt. Het sterkste punt, met vindplaats. De één tot drie belangrijkste verbeterpunten, op volgorde van invloed op het oordeel. Geen cijfer.'
    else: hint='Twee of drie zinnen: wat het sterkst is (met vindplaats) en wat het belangrijkste verbeterpunt is. Geen cijfer.'
    box(doc,hint,3.2 if group else 2.2,text=fill['kern'] if fill else None)
    # 2 Per criterium
    h(doc,'2. Per criterium')
    para(doc,'Niveau: onvoldoende, voldoende, goed of excellent. Bij excellent: wat dit sterk maakt, zodat het wordt vastgehouden.',8,italic=True,color=GREY)
    t=table(doc,['Criterium (weging)','Niveau','Waarom (met vindplaats)','Naar het volgende niveau'],[4.4,1.9,5.35,5.35],rows=len(d['crit']))
    for i,(nm,w) in enumerate(d['crit']):
        cs=t.rows[i+1].cells; celltext(cs[0],f'{nm} ({int(round(w*100))}%)',9,True)
        if fill:
            f=fill['crit'][i]; celltext(cs[1],f[0]); celltext(cs[2],f[1]); celltext(cs[3],f[2])
        else: minheight(t.rows[i+1],1.6 if group else 1.3)
    # 3 Keten
    if kind!='A2R':
        h(doc,'3. Redeneerketen-check'+(' · risico [R-xx]' if group and not fill else (' · '+fill['ketentitel'] if fill else '')))
        para(doc,('Volg het belangrijkste risico door de acht schakels. Een breuk is bijna altijd actiepunt 1.' if group else 'Volg de opbouw van het canvas. Waar breekt de redenering?'),8,italic=True,color=GREY)
        chain=CHAIN_G if group else CHAIN_I
        t=table(doc,['Schakel','✓ / breuk / deels','Waar in het '+('rapport' if group else 'canvas')],[4.0,2.6,10.4],rows=len(chain))
        for i,sk in enumerate(chain):
            cs=t.rows[i+1].cells; celltext(cs[0],sk,9,True)
            if fill: celltext(cs[2],fill['keten'][i][0]); celltext(cs[1],fill['keten'][i][1])
            else: minheight(t.rows[i+1],0.6)
        if fill and fill.get('ketennoot'): para(doc,fill['ketennoot'],9,space_after=4).paragraph_format.space_before=Pt(4)
    n3=4 if kind!='A2R' else 3
    # 4 Actiepunten
    h(doc,f'{n3}. Actiepunten')
    mx=5 if group else 2
    para(doc,(f'Hoogstens {mx}' + (', hoogstens drie keer moet.' if group else '.')) + (' Elk actiepunt komt bij A2 in de verwerkingslijst (bijlage E): overgenomen (waar), deels overgenomen (waar en waarom niet helemaal) of niet overgenomen (waarom).' if kind=='A1G' else ' Neem ze mee in je reflectie bij A2: wat deed je ermee?' if kind=='A1I' else ' Na A2 gaan de actiepunten over de overdracht aan de partner en het volgende project.' if group else ' Voor je volgende project of stage.'),8,italic=True,color=GREY)
    pref='A1' if a1 else 'A2'
    rows=fill['acties'] if fill else [[f'{pref}-{i+1}','','','',''] for i in range(mx)]
    t=table(doc,['Nr.','Moet / kan','Wat','Waarom','Zo laat je zien dat het verwerkt is'],[1.4,1.6,5.0,4.2,4.8],rows=len(rows))
    for i,rw in enumerate(rows):
        cs=t.rows[i+1].cells
        for j,v in enumerate(rw): celltext(cs[j],v,9,bold=(j==0))
        if not fill: minheight(t.rows[i+1],1.2)
    # 5 Cijfer
    h(doc,f'{n3+1}. Cijfer en voorwaarden')
    para(doc,'Over te nemen uit de rubric-werkmap (Beoordelingsrubric_AI_en_Ethics_A-ET_2026-2027.xlsx).',8,italic=True,color=GREY)
    if fill:
        para(doc,fill['cijfer'],10)
    else:
        t=table(doc,['Voorwaarde','Ingevuld','Gevolg'],[8.5,2.5,6.0],rows=len(d['conds']))
        for i,q in enumerate(d['conds']):
            celltext(t.rows[i+1].cells[0],q,9)
        para(doc,'',space_after=2)
        t2=doc.add_table(rows=3 if group else 2,cols=2); borders(t2)
        labs=['Niveau per criterium','Groepscijfer (gewogen, één decimaal)','Peercorrectie (geen, of wie, hoeveel en waarom)'] if group else ['Niveau per criterium','Cijfer (gewogen, één decimaal)']
        for i,lab in enumerate(labs):
            cs=t2.rows[i].cells; celltext(cs[0],lab,9,True,color=INK); shade(cs[0],SAND)
        fixwidths(t2,[6.5,10.5])
    # 6 Expertblik
    if group:
        h(doc,f'{n3+2}. Expertblik (optioneel, telt niet mee)')
        para(doc,'Alleen als de groep op de meeste criteria goed of excellent scoort. Een uitnodiging, geen eis: komt niet in de verwerkingslijst. Elke uitdaging begint bij iets wat de groep zelf al vond.',8,italic=True,color=GREY)
        box(doc,'Wat dit rapport al professioneel maakt: één specifieke zin.',1.2,text=fill['expert_zin'] if fill else None)
        para(doc,'',space_after=2)
        rows=fill['expert'] if fill else [[str(i+1),'','','',''] for i in range(3)]
        t=table(doc,['Uitdaging','Wat een expert ziet','De vraag','Probeer dit','Meer leren'],[2.3,4.0,3.0,4.9,2.8],rows=len(rows),size=8.5)
        for i,rw in enumerate(rows):
            cs=t.rows[i+1].cells
            for j,v in enumerate(rw): celltext(cs[j],v,8.5,bold=(j==0))
            if not fill: minheight(t.rows[i+1],2.0)
    return doc

if __name__=='__main__':
    names={'A1G':'Feedbackformulier_A1_groep','A1I':'Feedbackformulier_A1_individueel','A2G':'Feedbackformulier_A2_groep','A2R':'Feedbackformulier_A2_reflectie'}
    for k,nm in names.items():
        build(k).save(OUT+nm+'.docx'); print(nm)
    import example_claimwacht as ex
    build('A2G',ex.FILL).save(OUT+'Feedbackformulier_A2_groep_voorbeeld_ClaimWacht.docx'); print('voorbeeld')
