import re, copy
from openpyxl import load_workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
P='/tmp/claude-0/-home-user-menssana/175e1d50-6875-5f56-acf6-23260f0c6b9a/scratchpad/out/Beoordelingsrubric_AI_en_Ethics_A-ET_2026-2027.xlsx'
wb=load_workbook(P)
HF=PatternFill('solid',fgColor='12312A'); SF=PatternFill('solid',fgColor='EDE7DA'); IN=PatternFill('solid',fgColor='FFF6DD')
WH=Font(bold=True,color='FFFFFF'); B=Font(bold=True); WR=Alignment(wrap_text=True,vertical='top')
thin=Side(style='thin',color='BBBBBB'); BD=Border(left=thin,right=thin,top=thin,bottom=thin)
NAMES={'TC1':'Analyseren','TC2':'Adviseren','TC3':'Ontwerpen','TC4':'Realiseren','TC5':'Manage & Control',
'GC1':'Toekomstgericht organiseren','GC2':'Onderzoekend probleemoplossen','GC3':'Persoonlijk leiderschap','GC4':'Doelgericht interacteren','GC5':'Creativiteit'}
DESC={'TC1':'Ethische vraagstukken in AI identificeren en analyseren, zoals bias, privacy en de maatschappelijke impact van AI-oplossingen.',
'TC2':'Organisaties adviseren over het implementeren van ethische richtlijnen en normen voor AI-systemen, en zorgen voor naleving van wet- en regelgeving.',
'TC3':'AI-oplossingen ontwerpen die voldoen aan ethische normen en richtlijnen, en tegelijk de effectiviteit van de oplossing waarborgen.',
'TC4':'De ethische componenten van AI-oplossingen implementeren en testen, en zorgen dat ze voldoen aan de ethische en juridische eisen.',
'TC5':'De ethische uitvoering van AI-projecten beheren, inclusief het controleren van de impact op ethische vraagstukken en het implementeren van verbeteringen.',
'GC1':'De ethische implicaties van AI-oplossingen beoordelen en integreren in strategische besluitvorming over toekomstige toepassingen van AI.',
'GC2':'Met een kritische en onderzoekende benadering ethische dilemma\'s in AI identificeren, oplossingen analyseren en implementeren in de praktijk.',
'GC3':'Leiderschap tonen in het integreren van ethische normen in AI-projecten, verantwoordelijkheid nemen en actief pleiten voor ethische AI-principes.',
'GC4':'Effectief en ethisch communiceren met verschillende stakeholders, intern en extern, over de ethische implicaties van AI-oplossingen.',
'GC5':'Creatief en innovatief denken: AI-oplossingen ontwerpen die technisch effectief en ethisch verantwoord zijn, en ethische frameworks aanpassen aan nieuwe AI-uitdagingen.'}
ORDER=['TC1','TC2','TC3','TC4','TC5','GC1','GC2','GC3','GC4','GC5']
TABS={'A1 Groep':(range(6,11),'J11'),'A1 Individueel':(range(6,12),'J12'),'A2 Groep':(range(6,13),'J13'),'A2 Reflectie':(range(6,12),'J12')}
FIXED={'A1 Individueel':['TC1','GC2'],'A2 Reflectie':['GC3']}
cover={}
for t,(rows,cij) in TABS.items():
    ws=wb[t]
    m={}
    for r in rows:
        txt=str(ws.cell(r,1).value or '')
        codes=re.findall(r'\b(TC[1-5]|GC[1-5])\b',txt) or FIXED.get(t,[])
        crit=txt.split('/')[0].strip()
        for c in codes: m.setdefault(c,[]).append((r,crit.split('.')[0].strip()))
    cover[t]=m
    start=ws.max_row+2
    ws.cell(start,1,'Score per competentie (vakbeschrijving A-ET, niveau 3)').font=B
    ws.cell(start,1).fill=SF
    for c in range(2,13): ws.cell(start,c).fill=SF
    ws.merge_cells(start_row=start,start_column=1,end_row=start,end_column=12)
    h=start+1
    for col,txt in [(1,'Competentie'),(3,'Beoordeeld via criterium'),(7,'Score (gemiddelde van die criteria)'),(9,'Toelichting voor de student')]:
        c=ws.cell(h,col,txt); c.font=WH; c.fill=HF; c.alignment=WR
    for col in range(1,13): ws.cell(h,col).fill=HF
    ws.merge_cells(start_row=h,start_column=1,end_row=h,end_column=2); ws.merge_cells(start_row=h,start_column=3,end_row=h,end_column=6)
    ws.merge_cells(start_row=h,start_column=7,end_row=h,end_column=8); ws.merge_cells(start_row=h,start_column=9,end_row=h,end_column=12)
    r=h+1
    for code in ORDER:
        if code not in m: continue
        refs=[f'J{rr}' for rr,_ in m[code]]
        crits=', '.join(sorted({n for _,n in m[code]}, key=lambda s:(len(s),s)))
        ws.cell(r,1,f'{code}: {NAMES[code]}').alignment=WR
        ws.cell(r,3,crits if t not in FIXED else ('alle criteria (A tot en met F)' if t=='A2 Reflectie' else 'alle criteria (A tot en met F); het canvas werkt criterium 3 van het lesplan individueel uit')).alignment=WR
        if t=='A2 Reflectie':
            f=f'=IF(ISNUMBER({cij}),{cij},"")'
        else:
            f=f'=IF(COUNT({",".join(refs)})={len(refs)},ROUND(AVERAGE({",".join(refs)})+0.000001,1),"")'
        ws.cell(r,7,f); ws.cell(r,7).number_format='0.0'
        ws.cell(r,9).fill=IN; ws.cell(r,9).alignment=WR
        ws.merge_cells(start_row=r,start_column=1,end_row=r,end_column=2); ws.merge_cells(start_row=r,start_column=3,end_row=r,end_column=6)
        ws.merge_cells(start_row=r,start_column=7,end_row=r,end_column=8); ws.merge_cells(start_row=r,start_column=9,end_row=r,end_column=12)
        for col in range(1,13): ws.cell(r,col).border=BD
        ws.row_dimensions[r].height=30
        r+=1
    note=ws.cell(r,1,'Het cijfer van dit formulier blijft het gewogen gemiddelde van de criteria hierboven. De score per competentie is informatief: voor de feedback en voor registratie per competentie.')
    note.font=Font(italic=True,color='555555'); note.alignment=WR
    ws.merge_cells(start_row=r,start_column=1,end_row=r,end_column=12); ws.row_dimensions[r].height=30
    r+=2
    ws.cell(r,1,'Ondertekening').font=B; ws.cell(r,1).fill=SF
    for c in range(2,13): ws.cell(r,c).fill=SF
    ws.merge_cells(start_row=r,start_column=1,end_row=r,end_column=12)
    for lab in ['Examinator (eerste beoordelaar)','Tweede lezer (bij twijfel rond 5,5 of een steekproef)','Datum vastgesteld','Paraaf of handtekening examinator']:
        r+=1
        ws.cell(r,1,lab).alignment=WR
        ws.merge_cells(start_row=r,start_column=1,end_row=r,end_column=2)
        for col in range(3,8): ws.cell(r,col).fill=IN
        ws.merge_cells(start_row=r,start_column=3,end_row=r,end_column=7)
        for col in range(1,8): ws.cell(r,col).border=BD
    ws.print_area=f'A1:L{r}'
# Competenties sheet
if 'Competenties' in wb.sheetnames: del wb['Competenties']
cs=wb.create_sheet('Competenties', index=1)
cs['A1']='Competenties uit de vakbeschrijving en waar ze worden beoordeeld'; cs['A1'].font=Font(bold=True,size=14,color='12312A')
cs['A2']='Alle competenties zijn op niveau 3. Elke competentie komt minstens één keer terug in Assessment 1 of 2. Bron: vakbeschrijving A-ET 2026-2027 en het lesplan (beoordelingscriteria).'
cs['A2'].alignment=WR; cs.merge_cells('A2:G2'); cs.row_dimensions[2].height=32
hdr=['Code','Competentie','Wat de student laat zien (vakbeschrijving)','A1 groep','A1 individueel','A2 groep','A2 reflectie']
for i,hx in enumerate(hdr,1):
    c=cs.cell(4,i,hx); c.font=WH; c.fill=HF; c.alignment=WR
for i,code in enumerate(ORDER,5):
    vals=[code,NAMES[code],DESC[code]]
    for t in ['A1 Groep','A1 Individueel','A2 Groep','A2 Reflectie']:
        lst=cover[t].get(code,[])
        vals.append(('criterium '+', '.join(sorted({n for _,n in lst},key=lambda s:(len(s),s)))) if lst and t not in FIXED else ('alle criteria' if lst else '–'))
    for j,v in enumerate(vals,1):
        c=cs.cell(i,j,v); c.alignment=WR; c.border=BD
    cs.row_dimensions[i].height=45
for col,w in zip('ABCDEFG',[7,26,70,16,16,16,14]): cs.column_dimensions[col].width=w
cs.freeze_panes='A5'
cs.page_setup.orientation='landscape'; cs.page_setup.paperSize=9; cs.page_setup.fitToWidth=1; cs.page_setup.fitToHeight=0; cs.sheet_properties.pageSetUpPr.fitToPage=True
r=16
cs.cell(r,1,'Verschil met de beoordeling van 2025-2026').font=B
cs.cell(r+1,1,'Vroeger kreeg elke competentie een cijfer en was het toetscijfer het gewone gemiddelde daarvan. Het groepscijfer gold voor iedereen in de groep; in Assessment 2 telde alleen persoonlijk leiderschap (GC3) per student. Nu wordt per criterium beoordeeld met beschreven niveaus en een weging, telt per toets een individueel deel van 40% mee, en laat het overzicht per competentie zien hoe de student op elke competentie scoort. De weging 30% (A1) en 70% (A2) is gelijk gebleven.').alignment=WR
cs.merge_cells(start_row=r+1,start_column=1,end_row=r+1,end_column=7); cs.row_dimensions[r+1].height=75
# Toelichting addition
ts=wb['Toelichting']
n=ts.max_row+1
for lab,txt in [('Score per competentie','Onder elke rubric staat de score per competentie (TC1 tot en met TC5, GC1 tot en met GC5): het gemiddelde van de criteria die die competentie toetsen. Het tabblad Competenties laat zien welke criteria bij welke competentie horen. Het cijfer zelf blijft het gewogen gemiddelde van de criteria.'),
                ('Ondertekening','Elk formulier eindigt met de examinator, de tweede lezer (bij twijfel rond 5,5 of een steekproef), de datum en een paraaf. Vul die in voordat het cijfer wordt geregistreerd.')]:
    ts.cell(n,1,lab).font=B; ts.cell(n,1).alignment=WR
    ts.cell(n,2,txt).alignment=WR; ts.row_dimensions[n].height=48; n+=1
wb.save(P)
print({t:{k:[x[1] for x in v] for k,v in m.items()} for t,m in cover.items()})
