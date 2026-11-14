from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter as L
from openpyxl.worksheet.datavalidation import DataValidation
wb=Workbook()
H=Font(bold=True); HF=PatternFill('solid',fgColor='DCE6F1'); IN=PatternFill('solid',fgColor='FFF2CC'); OUT=PatternFill('solid',fgColor='E2EFDA')
thin=Side(style='thin',color='BFBFBF'); B=Border(left=thin,right=thin,top=thin,bottom=thin)
# Uitleg
u=wb.active; u.title='Uitleg'
lines=['Cijferbestand AI & Ethics (A-ET) 2026-2027',
'',
'Zo werkt het',
'1. Vul op het blad Groepen per groep de criteriumscores in (gele cellen), schaal 1 tot 10: onvoldoende 4, voldoende 6, goed 8, excellent 10, tussenscores toegestaan.',
'2. Vul op het blad Studenten per student de groep, de scores voor het individuele deel en de reflectie in, en zo nodig een peercorrectie (0, 10, 20 of 30 procent) of aftrek voor te laat inleveren.',
'3. Groene cellen rekenen zichzelf uit. Niets invullen in groene cellen.',
'',
'Formules (uit de rubrics van week 5 en week 8)',
'Groepscijfer A1 = (C1 x 20 + C2 x 25 + C3 x 10 + C4 x 30 + C5 x 15) / 100',
'Individueel A1 = (A x 15 + B x 20 + C x 10 + D x 30 + E x 20 + F x 5) / 100',
'Groepscijfer A2 = (C1 x 5 + C2 x 10 + C4 x 10 + C5 x 15 + C6 x 30 + C7 x 15 + C8 x 15) / 100',
'Reflectie A2 = (A x 20 + B x 20 + C x 20 + D x 20 + E x 10 + F x 10) / 100',
'Groepscijfer na peercorrectie = groepscijfer x (1 - correctie), minimaal 1,0. Bij vrijwel geen bijdrage: correctie 100 procent geeft 1,0.',
'Cijfer A1 = 0,6 x groep (na correctie en aftrek) + 0,4 x individueel (na aftrek)',
'Cijfer A2 = 0,6 x groep (na correctie en aftrek) + 0,4 x reflectie (na aftrek)',
'Eindcijfer = 0,3 x A1 + 0,7 x A2, afgerond op 1 decimaal; voldoende vanaf 5,5.',
'',
'Let op',
'- Tussenresultaten worden niet afgerond; alleen het eindcijfer.',
'- Afronding en de grens van 5,5: controleer de onderwijs- en examenregeling van Janssen.',
'- De voorbeeldrijen (groep G0 en studenten S0) laten zien dat het werkt. Verwijder ze voor gebruik.']
for i,t in enumerate(lines,1):
    c=u.cell(i,1,t)
    if i in (1,3,8,18): c.font=Font(bold=True, size=13 if i==1 else 11)
u.column_dimensions['A'].width=130
# Groepen
g=wb.create_sheet('Groepen')
hdr=['Groep','Toepassing / route','A1 C1 afbakening','A1 C2 bewijs','A1 C3 dilemma\'s','A1 C4 risico\'s','A1 C5 oordeel en plan','A1 aftrek te laat (punten)','A1 groepscijfer',
     'A2 C1 afbakening','A2 C2 bewijs','A2 C4 risico\'s','A2 C5 gewenste situatie','A2 C6 maatregelen','A2 C7 monitoring','A2 C8 eindoordeel','A2 aftrek te laat (punten)','A2 groepscijfer']
w1=[20,25,10,30,15]; w2=[5,10,10,15,30,15,15]
g.append(['Weging (%)','']+w1+['','']+w2+['',''])
g.append(hdr)
for c in range(1,len(hdr)+1):
    for r in (1,2):
        cell=g.cell(r,c); cell.font=H; cell.fill=HF; cell.border=B; cell.alignment=Alignment(wrap_text=True,vertical='top')
g.row_dimensions[2].height=45
rows=[('G0','Voorbeeld, verwijderen',[8,6,8,6,7],0,[7,7,7,8,6,7,8],0)]+[(f'G{i}','',None,None,None,None) for i in range(1,11)]
for i,(gid,name,a1,af1,a2,af2) in enumerate(rows):
    r=3+i
    g.cell(r,1,gid); g.cell(r,2,name)
    for j in range(5): g.cell(r,3+j, a1[j] if a1 else None)
    g.cell(r,8, af1 if a1 else None)
    g.cell(r,9, f'=IF(COUNT(C{r}:G{r})<5,"",MAX(1,SUMPRODUCT(C{r}:G{r},$C$1:$G$1)/100-N(H{r})))')
    for j in range(7): g.cell(r,10+j, a2[j] if a2 else None)
    g.cell(r,17, af2 if a2 else None)
    g.cell(r,18, f'=IF(COUNT(J{r}:P{r})<7,"",MAX(1,SUMPRODUCT(J{r}:P{r},$J$1:$P$1)/100-N(Q{r})))')
    for c in range(1,19):
        cell=g.cell(r,c); cell.border=B
        cell.fill = OUT if c in (9,18) else (IN if c>=3 else PatternFill())
        if c in (9,18): cell.number_format='0.00'
for c in range(1,19): g.column_dimensions[L(c)].width=14
g.column_dimensions['B'].width=26
g.freeze_panes='C3'
dv=DataValidation(type='decimal',operator='between',formula1='1',formula2='10',showErrorMessage=True,error='Score tussen 1 en 10')
g.add_data_validation(dv); dv.add('C3:G13'); dv.add('J3:P13')
# Studenten
s=wb.create_sheet('Studenten')
sh=['Studentnummer','Naam','Groep',
 'A1 peercorrectie (0-1)','A1 groep na correctie',
 'A1 ind A beslisvraag','A1 ind B feiten','A1 ind C alternatieven','A1 ind D lenzen','A1 ind E oordeel','A1 ind F risico','A1 ind aftrek te laat','A1 individueel','Cijfer A1',
 'A2 peercorrectie (0-1)','A2 groep na correctie',
 'Refl A dilemma','Refl B aanname','Refl C feedback','Refl D rol','Refl E diepgang','Refl F onderbouwing','Refl aftrek te laat','Reflectie','Cijfer A2',
 'Eindcijfer','Resultaat']
wi=[15,20,10,30,20,5]; wr=[20,20,20,20,10,10]
s.append(['Weging (%)','','','','']+wi+['','','','','']+wr+['','','','',''])
s.append(sh)
for c in range(1,len(sh)+1):
    for r in (1,2):
        cell=s.cell(r,c); cell.font=H; cell.fill=HF; cell.border=B; cell.alignment=Alignment(wrap_text=True,vertical='top')
s.row_dimensions[2].height=45
ex=[('S0-1','Voorbeeld A','G0',0,[7,8,7,8,7,6],0,0,[7,6,7,6,6,7],0),
    ('S0-2','Voorbeeld B','G0',0.1,[6,6,6,5,6,6],0,0,[6,6,5,6,6,6],0)]
N=40
for i in range(N):
    r=3+i
    if i<len(ex):
        sid,nm,gr,c1,i1,a1,c2,rf,a2=ex[i]
        vals={1:sid,2:nm,3:gr,4:c1,12:a1,15:c2,23:a2}
        for j in range(6): vals[6+j]=i1[j]; vals[17+j]=rf[j]
        for k,v in vals.items(): s.cell(r,k,v)
    s.cell(r,5, f'=IF(OR(C{r}="",IFERROR(VLOOKUP(C{r},Groepen!$A$3:$I$13,9,FALSE),"")=""),"",MAX(1,VLOOKUP(C{r},Groepen!$A$3:$I$13,9,FALSE)*(1-N(D{r}))))')
    s.cell(r,13, f'=IF(COUNT(F{r}:K{r})<6,"",MAX(1,SUMPRODUCT(F{r}:K{r},$F$1:$K$1)/100-N(L{r})))')
    s.cell(r,14, f'=IF(OR(E{r}="",M{r}=""),"",0.6*E{r}+0.4*M{r})')
    s.cell(r,16, f'=IF(OR(C{r}="",IFERROR(VLOOKUP(C{r},Groepen!$A$3:$R$13,18,FALSE),"")=""),"",MAX(1,VLOOKUP(C{r},Groepen!$A$3:$R$13,18,FALSE)*(1-N(O{r}))))')
    s.cell(r,24, f'=IF(COUNT(Q{r}:V{r})<6,"",MAX(1,SUMPRODUCT(Q{r}:V{r},$Q$1:$V$1)/100-N(W{r})))')
    s.cell(r,25, f'=IF(OR(P{r}="",X{r}=""),"",0.6*P{r}+0.4*X{r})')
    s.cell(r,26, f'=IF(OR(N{r}="",Y{r}=""),"",ROUND(0.3*N{r}+0.7*Y{r},1))')
    s.cell(r,27, f'=IF(Z{r}="","",IF(Z{r}>=5.5,"voldoende","onvoldoende"))')
    for c in range(1,28):
        cell=s.cell(r,c); cell.border=B
        if c in (5,13,14,16,24,25,26,27): cell.fill=OUT; cell.number_format='0.00' if c!=26 else '0.0'
        elif c>=3: cell.fill=IN
for c in range(1,28): s.column_dimensions[L(c)].width=12
s.column_dimensions['B'].width=22
s.freeze_panes='D3'
dv2=DataValidation(type='decimal',operator='between',formula1='0',formula2='1',showErrorMessage=True,error='Correctie tussen 0 en 1 (0,1 = 10%)')
s.add_data_validation(dv2); dv2.add(f'D3:D{N+2}'); dv2.add(f'O3:O{N+2}')
dv3=DataValidation(type='decimal',operator='between',formula1='1',formula2='10',showErrorMessage=True,error='Score tussen 1 en 10')
s.add_data_validation(dv3); dv3.add(f'F3:K{N+2}'); dv3.add(f'Q3:V{N+2}')
wb.save('out/week10/Cijferbestand_A-ET_2026-2027.xlsx')
