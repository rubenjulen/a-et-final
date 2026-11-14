# Peerbeoordelingsformulier A-ET (bron: week 5, Hoofdstukeigenaarschap en peerbeoordeling; week 10 signalen; rubric Toelichting)
import sys
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.formatting.rule import FormulaRule
from openpyxl.utils import get_column_letter as L
OUT=sys.argv[1] if len(sys.argv)>1 else 'out/instrumenten/Peerbeoordeling_A-ET.xlsx'
DARK='12312A'; SAND='EDE7DA'; INP='FFF6DD'; RED='A8432C'; CALC='F6F3EC'
H=Font(bold=True,color='FFFFFF'); HF=PatternFill('solid',fgColor=DARK); SF=PatternFill('solid',fgColor=SAND)
IF=PatternFill('solid',fgColor=INP); CF=PatternFill('solid',fgColor=CALC)
WR=Alignment(wrap_text=True,vertical='top'); CT=Alignment(horizontal='center',vertical='top',wrap_text=True)
th=Side(style='thin',color='CCCCCC'); B=Border(top=th,bottom=th,left=th,right=th)
def hdr(ws,row,cols):
    for i,c in enumerate(cols,1):
        x=ws.cell(row,i,c); x.font=H; x.fill=HF; x.alignment=Alignment(wrap_text=True,vertical='center'); x.border=B
    ws.row_dimensions[row].height=52
def dv(ws,opts,rng,prompt=None):
    d=DataValidation(type='list',formula1='"'+','.join(opts)+'"',allow_blank=True)
    if prompt: d.prompt=prompt; d.showInputMessage=True
    ws.add_data_validation(d); d.add(rng)
def page(ws,rows_repeat=None):
    ws.page_setup.orientation='landscape'; ws.page_setup.paperSize=ws.PAPERSIZE_A4
    ws.page_setup.fitToWidth=1; ws.page_setup.fitToHeight=0; ws.sheet_properties.pageSetUpPr.fitToPage=True
    ws.page_margins.left=ws.page_margins.right=0.5
    if rows_repeat: ws.print_title_rows=rows_repeat
def title(ws,t,sub):
    ws['A1']=t; ws['A1'].font=Font(bold=True,size=16,color=DARK)
    ws['A2']=sub; ws['A2'].font=Font(italic=True,color='44504B')

Q=['Leverde het afgesproken werk op tijd','Kwaliteit van de bijdrage','Was bereikbaar en deed mee aan overleg','Hielp anderen en gaf feedback']
SC=[['Bijna nooit','Soms','Meestal','Altijd'],['Moest overgedaan worden','Bruikbaar na veel werk','Goed','Tilde het rapport op'],
    ['Bijna nooit','Soms','Meestal','Altijd'],['Nooit','Soms','Regelmatig','Actief en opbouwend']]
wb=Workbook()

# ---------- Uitleg ----------
ws=wb.active; ws.title='Uitleg'
title(ws,'Peerbeoordeling A-ET','AI & Ethics (A-ET) 2026-2027 · bij Assessment 1 (week 5) en Assessment 2 (week 10)')
ws.column_dimensions['A'].width=26; ws.column_dimensions['B'].width=100
rows=[
('Wanneer','Bij het inleveren van Assessment 1 (vóór donderdag 4 februari, 23:59) en van Assessment 2 (vóór donderdag 11 maart, 23:59). Bij Assessment 2 gaat het over de periode sinds Assessment 1.'),
('Over wie','Over elk groepslid, niet over jezelf.'),
('Hoe','Ga naar het tabblad Invullen. Vul je naam, groep en de toets in. Geef per groepslid op vier vragen een score van 1 tot 4 en beantwoord de open vraag: Wat was de belangrijkste bijdrage van deze persoon? Die open vraag is verplicht, minimaal één zin. Lever het bestand in bij het inleverpunt peerbeoordeling op MyCampus.'),
('Vertrouwelijk','Alleen de docent ziet het formulier. Groepsgenoten zien je scores en antwoorden niet.'),
('Wat de docent ermee doet','De docent berekent per student het gemiddelde dat die van de anderen kreeg. Een signaal is: een gemiddelde onder de 2,0; of een gemiddelde dat 1,0 of meer onder het groepsgemiddelde ligt; of twee of meer groepsleden die in de open vraag aangeven dat iemand weinig of niets heeft bijgedragen.'),
('Bij een signaal','1. Controleren: de docent bekijkt logboek, weekchecks, de versiegeschiedenis van het gedeelde document en het hoofdstuk van de student. 2. Gesprek: kort apart gesprek met de student; de student hoort wat er speelt en kan reageren. 3. Besluit: geen correctie, of een correctie op het groepscijfer van die student: 10%, 20% of 30% lager. Bij vrijwel geen bijdrage krijgt de student voor het groepsdeel een 1,0. De docent legt het besluit en de reden vast.'),
('Nooit alleen het formulier','Een correctie gebeurt nooit alleen op basis van het formulier: er moet ook ander bewijs zijn. Andersom: een student die veel meer deed dan de rest krijgt geen hoger groepscijfer. Dat zie je terug in het individuele deel en in de reflectie van Assessment 2.'),
('Hoofdstukeigenaar','Elk hoofdstuk heeft één eigenaar, genoemd op het voorblad. Zonder hoofdstukeigenaren op het voorblad is een correctie op basis van de peerbeoordeling niet mogelijk zonder gesprek.'),
('Spanningen in de groep','Meld problemen vóór de deadline, niet erna. Een groep die vastloopt, kan bij de docent terecht voor een kort gesprek van 15 minuten.'),
('Tabblad Docent_samenvatting','Alleen voor de docent: daar worden de formulieren van één groep samengevoegd. Studenten laten dit tabblad leeg.'),
]
for i,(a,b) in enumerate(rows,4):
    x=ws.cell(i,1,a); x.font=Font(bold=True,color=DARK); x.fill=SF; x.alignment=WR; x.border=B
    y=ws.cell(i,2,b); y.alignment=WR; y.border=B
    ws.row_dimensions[i].height=max(30,15*(len(b)//95+1))
r=len(rows)+5
ws.cell(r,1,'De vier vragen en de schaal').font=Font(bold=True,size=12,color=DARK)
hdr(ws,r+1,['Vraag','1 · 2 · 3 · 4'])
for j,(q,s) in enumerate(zip(Q,SC)):
    ws.cell(r+2+j,1,q).alignment=WR; ws.cell(r+2+j,1).border=B
    ws.cell(r+2+j,2,'  ·  '.join(f'{k+1} = {t}' for k,t in enumerate(s))).alignment=WR; ws.cell(r+2+j,2).border=B
    ws.row_dimensions[r+2+j].height=30
page(ws)

# ---------- Invullen ----------
ws=wb.create_sheet('Invullen')
title(ws,'Peerbeoordeling: invullen','Gele cellen vul je zelf in. Beoordeel elk groepslid, niet jezelf. Vertrouwelijk: alleen de docent ziet dit.')
info=[('Jouw naam',''),('Studentnummer',''),('Groep / casus',''),('Toets','')]
for i,(a,b) in enumerate(info,4):
    ws.cell(i,1,a).font=Font(bold=True); c=ws.cell(i,2,b); c.fill=IF; c.border=B
    ws.merge_cells(start_row=i,start_column=2,end_row=i,end_column=4)
dv(ws,['Assessment 1 (week 5)','Assessment 2 (week 10)'],'B7')
cols=['Groepslid (naam)']+[f'{k+1}. {q}' for k,q in enumerate(Q)]+['Gemiddelde','Wat was de belangrijkste bijdrage van deze persoon? (verplicht, minimaal één zin)','Controle']
HR=9; hdr(ws,HR,cols)
widths=[22,15,15,15,15,11,60,30]
for i,w in enumerate(widths,1): ws.column_dimensions[L(i)].width=w
ws.cell(HR-1,1,'Scores: typ 1, 2, 3 of 4 (zie de schaal op het tabblad Uitleg).').font=Font(italic=True,color='44504B')
for k in range(5):
    r=HR+1+k
    for c in range(1,8):
        x=ws.cell(r,c); x.border=B; x.alignment=WR if c in (1,7) else CT
        if c!=6: x.fill=IF
    ws.cell(r,6,f'=IF(COUNT(B{r}:E{r})=4,ROUND(AVERAGE(B{r}:E{r}),2),"")').fill=CF
    ws.cell(r,8,f'=IF(A{r}="","",IF(COUNT(B{r}:E{r})<4,"Vul alle vier scores in",IF(LEN(TRIM(G{r}))<10,"Open vraag is verplicht",IF(F{r}<2,"Gemiddelde onder 2,0: licht toe in de open vraag","OK"))))').alignment=WR
    ws.cell(r,8).border=B
    ws.row_dimensions[r].height=60
dv(ws,['1','2','3','4'],f'B{HR+1}:E{HR+5}','Score 1 tot 4')
# integers via list are text in some apps -> use whole-number validation instead
ws.data_validations.dataValidation=[d for d in ws.data_validations.dataValidation if 'Score' not in (d.prompt or '')]
dw=DataValidation(type='whole',operator='between',formula1='1',formula2='4',allow_blank=True); dw.prompt='Score 1 tot 4'; dw.showInputMessage=True; dw.error='Kies een geheel getal van 1 tot 4'; dw.showErrorMessage=True
ws.add_data_validation(dw); dw.add(f'B{HR+1}:E{HR+5}')
rng=f'A{HR+1}:H{HR+5}'
ws.conditional_formatting.add(f'F{HR+1}:F{HR+5}',FormulaRule(formula=[f'AND(F{HR+1}<>"",F{HR+1}<2)'],fill=PatternFill('solid',fgColor='F3D9D2'),font=Font(bold=True,color=RED)))
ws.conditional_formatting.add(f'H{HR+1}:H{HR+5}',FormulaRule(formula=[f'AND(H{HR+1}<>"",H{HR+1}<>"OK")'],font=Font(bold=True,color=RED)))
ws.cell(HR+7,1,'Voorbeeld (niet invullen, alleen ter illustratie):').font=Font(italic=True,color='777777')
ex=['Student B',4,3,3,2,3.0,'Schreef hoofdstuk 4 (nulmeting) en vond het bewijs voor domein 5 in het testverslag.','OK']
for i,v in enumerate(ex,1):
    c=ws.cell(HR+8,i,v); c.font=Font(italic=True,color='777777'); c.alignment=WR; c.border=B
ws.row_dimensions[HR+8].height=32
ws.freeze_panes=f'A{HR+1}'; page(ws,f'{HR}:{HR}')

# ---------- Docent_samenvatting ----------
ws=wb.create_sheet('Docent_samenvatting')
title(ws,'Peerbeoordeling: docentsamenvatting per groep','Alleen voor de docent. Neem per groep de formulieren over (één regel per beoordelaar en beoordeelde). Een correctie gebeurt nooit alleen op basis van het formulier.')
for i,(a,b) in enumerate([('Groep / casus',''),('Toets',''),('Groepscijfer (vóór correctie)','')],4):
    ws.cell(i,1,a).font=Font(bold=True); c=ws.cell(i,2,b); c.fill=IF; c.border=B
dv(ws,['Assessment 1 (week 5)','Assessment 2 (week 10)'],'B5')
# Block 1: ingevoerde formulieren
R1=8
ws.cell(R1-1,1,'1. Ingevoerde formulieren (tot 5 groepsleden: 20 regels)').font=Font(bold=True,size=12,color=DARK)
hdr(ws,R1,['Beoordelaar','Beoordeelde','V1 op tijd','V2 kwaliteit','V3 overleg','V4 hulp','Gemiddelde','Belangrijkste bijdrage (open vraag)','Meldt weinig of niets? (docent)'])
N=20
for k in range(N):
    r=R1+1+k
    for c in range(1,10):
        x=ws.cell(r,c); x.border=B; x.alignment=WR if c in (1,2,8) else CT
        if c!=7: x.fill=IF
    ws.cell(r,7,f'=IF(COUNT(C{r}:F{r})=4,ROUND(AVERAGE(C{r}:F{r}),2),"")').fill=CF
dw2=DataValidation(type='whole',operator='between',formula1='1',formula2='4',allow_blank=True); ws.add_data_validation(dw2); dw2.add(f'C{R1+1}:F{R1+N}')
dv(ws,['ja','nee'],f'I{R1+1}:I{R1+N}','Geeft de open vraag aan dat deze persoon weinig of niets bijdroeg?')
first,last=R1+1,R1+N
# Block 2: per student
R2=last+3
ws.cell(R2-1,1,'2. Per student: signaal, ander bewijs en besluit').font=Font(bold=True,size=12,color=DARK)
cols2=['Student','Aantal formulieren','Ontvangen gemiddelde','Groepsgemiddelde','Verschil met groep','Meldingen weinig/niets','Signaal',
       'Logboek en weekchecks','Versiegeschiedenis','Hoofdstuk (eigenaar)','Gesprek (datum)','Besluit','Reden (verplicht bij correctie)','Groepscijfer na correctie','Controle']
hdr(ws,R2,cols2)
for k in range(5):
    r=R2+1+k; A=f'$A${R2+1}:$A${R2+5}'
    ws.cell(r,1).fill=IF
    ws.cell(r,2,f'=IF(A{r}="","",COUNTIFS($B${first}:$B${last},A{r},$G${first}:$G${last},"<>"))')
    ws.cell(r,3,f'=IF(OR(A{r}="",B{r}=0),"",ROUND(AVERAGEIFS($G${first}:$G${last},$B${first}:$B${last},A{r}),2))')
    ws.cell(r,4,f'=IF(C{r}="","",ROUND(AVERAGE($C${R2+1}:$C${R2+5}),2))')
    ws.cell(r,5,f'=IF(C{r}="","",ROUND(C{r}-D{r},2))')
    ws.cell(r,6,f'=IF(A{r}="","",COUNTIFS($B${first}:$B${last},A{r},$I${first}:$I${last},"ja"))')
    ws.cell(r,7,f'=IF(A{r}="","",IF(OR(AND(C{r}<>"",C{r}<2),AND(E{r}<>"",E{r}<=-1),F{r}>=2),"SIGNAAL: "&IF(AND(C{r}<>"",C{r}<2),"onder 2,0; ","")&IF(AND(E{r}<>"",E{r}<=-1),"1,0 of meer onder groep; ","")&IF(F{r}>=2,"2+ meldingen","" ),"geen signaal"))')
    for c in (8,9,10,11,12,13): ws.cell(r,c).fill=IF
    ws.cell(r,14,f'=IF(OR(A{r}="",$B$6=""),"",IF(L{r}="1,0 (vrijwel geen bijdrage)",1,IF(L{r}="20% lager",MAX(1,ROUND($B$6*0.8,1)),IF(L{r}="30% lager",MAX(1,ROUND($B$6*0.7,1)),IF(L{r}="10% lager",MAX(1,ROUND($B$6*0.9,1)),ROUND($B$6,1))))))')
    ws.cell(r,15,f'=IF(OR(A{r}="",L{r}="",L{r}="Geen correctie"),"",IF(OR(K{r}="",M{r}="",AND(H{r}="",I{r}="",J{r}="")),"Niet toegestaan: ander bewijs, gesprek en reden zijn nodig","OK"))')
    for c in range(1,16):
        x=ws.cell(r,c); x.border=B; x.alignment=WR if c in (1,7,8,9,10,13,15) else CT
        if c in (2,3,4,5,6,7,14): x.fill=CF
    ws.row_dimensions[r].height=48
dv(ws,['Geen correctie','10% lager','20% lager','30% lager','1,0 (vrijwel geen bijdrage)'],f'L{R2+1}:L{R2+5}')
ws.conditional_formatting.add(f'G{R2+1}:G{R2+5}',FormulaRule(formula=[f'LEFT(G{R2+1},7)="SIGNAAL"'],fill=PatternFill('solid',fgColor='F3D9D2'),font=Font(bold=True,color=RED)))
ws.conditional_formatting.add(f'O{R2+1}:O{R2+5}',FormulaRule(formula=[f'LEFT(O{R2+1},4)="Niet"'],font=Font(bold=True,color=RED)))
ws.cell(R2+7,1,'Groepscijfer na correctie = groepscijfer × (1 − correctie), minimaal 1,0; bij vrijwel geen bijdrage 1,0. Signaalgrenzen en stappen: week 5 (Wanneer de docent ingrijpt) en week 10 (Signalen uit de peerbeoordeling).').font=Font(italic=True,color='44504B')
w2=[18,16,13,13,13,13,26,24,20,20,14,22,30,14,30]
for i,w in enumerate(w2,1): ws.column_dimensions[L(i)].width=max(w,ws.column_dimensions[L(i)].width or 0)
ws.column_dimensions['H'].width=40; ws.column_dimensions['I'].width=20
ws.freeze_panes=f'A{R1+1}'; page(ws)
wb.save(OUT); print('saved',OUT)
