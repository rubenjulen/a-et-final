from xml.sax.saxutils import escape, quoteattr
Q={'File':'Orange.widgets.data.owfile.OWFile','LR':'Orange.widgets.model.owlogisticregression.OWLogisticRegression',
 'Tree':'Orange.widgets.model.owtree.OWTreeLearner','Pred':'Orange.widgets.evaluate.owpredictions.OWPredictions',
 'Table':'Orange.widgets.data.owtable.OWTable','Save':'Orange.widgets.data.owsave.OWSave',
 'Nomo':'Orange.widgets.visualize.ownomogram.OWNomogram','TV':'Orange.widgets.visualize.owtreeviewer.OWTreeGraph'}
NAME={'File':'File','LR':'Logistic Regression','Tree':'Tree','Pred':'Predictions','Table':'Data Table','Save':'Save Data','Nomo':'Nomogram','TV':'Tree Viewer'}
nodes=[('File','1 Leren: suribank_versie_A.csv',60,120),('LR','Logistic Regression',260,60),('Tree','Tree',260,200),
('File','2 Paren: suribank_paren.csv',60,360),('Pred','3 Voorspelling paren',480,360),('Table','4 Paren bekijken',680,300),('Save','5 Paren opslaan (Excel)',680,420),
('File','6 Grensgevallen: suribank_testset.csv',60,560),('Pred','7 Voorspelling testset',480,560),('Table','8 Sorteer op kans',680,560),
('Nomo','9 Uitleg: Nomogram',480,0),('TV','9 Uitleg: Tree Viewer',480,200)]
links=[(0,1,'Data','data','Data','data'),(0,2,'Data','data','Data','data'),
(3,4,'Data','data','Data','data'),(1,4,'Model','model','Predictors','predictors'),(2,4,'Model','model','Predictors','predictors'),
(4,5,'Predictions','annotated','Data','data'),(4,6,'Predictions','annotated','Data','data'),
(7,8,'Data','data','Data','data'),(1,8,'Model','model','Predictors','predictors'),(2,8,'Model','model','Predictors','predictors'),
(8,9,'Predictions','annotated','Data','data'),
(1,10,'Model','model','Classifier','classifier'),(2,11,'Model','model','Tree','tree')]
# fix: node 7 is File testset, 8 Predictions; reindex below
links=[(0,1,'Data','data','Data','data'),(0,2,'Data','data','Data','data'),
(3,4,'Data','data','Data','data'),(1,4,'Model','model','Predictors','predictors'),(2,4,'Model','model','Predictors','predictors'),
(4,5,'Predictions','annotated','Data','data'),(4,6,'Predictions','annotated','Data','data'),
(7,8,'Data','data','Data','data'),(1,8,'Model','model','Predictors','predictors'),(2,8,'Model','model','Predictors','predictors'),
(8,9,'Predictions','annotated','Data','data'),
(1,10,'Model','model','Classifier','classifier'),(2,11,'Model','model','Tree','tree')]
notes=[((20,640,420,120),"Stap 6 tot 8, grensgevallen: open 8 en klik op de kolomkop met de kans op ja. Kies 10 aanvragers met een kans tussen 0,45 en 0,55. Verander in Excel één gewoon kenmerk een klein beetje en laad ze opnieuw in 2."),
((20,0,400,90),"Practicum 4, Suribank. Dubbelklik op elke File en kies het bestand dat in de naam staat. Laat Logistic Regression en Tree op de standaardinstellingen."),
((720,120,330,150),"Stap 4 en 5: in 4 zie je per paar (R001-orig, R001-wijz) het besluit en de kans op ja. Sla in 5 op als Excel en plak aanvraag_id en de twee kansen in het tabblad B_import van het testlogboek."),
((700,0,330,100),"Stap 9, uitlegtest: gebruik Nomogram en Tree Viewer, net als in practicum 3.")]
out=["<?xml version='1.0' encoding='utf-8'?>",'<scheme version="2.0" title="Practicum 4 gepaarde test Suribank" description="A-ET week 4: gepaarde test, grensgevallen en uitlegtest.">','\t<nodes>']
for i,(k,t,x,y) in enumerate(nodes):
    out.append(f'\t\t<node id="{i}" name="{NAME[k]}" qualified_name="{Q[k]}" project_name="Orange3" version="" title={quoteattr(t)} position="({x}.0, {y}.0)" />')
out.append('\t</nodes>'); out.append('\t<links>')
for i,(s,d,sc,sid,dc,did) in enumerate(links):
    out.append(f'\t\t<link id="{i}" source_node_id="{s}" sink_node_id="{d}" source_channel="{sc}" sink_channel="{dc}" enabled="true" source_channel_id="{sid}" sink_channel_id="{did}" />')
out.append('\t</links>'); out.append('\t<annotations>')
for i,(r,txt) in enumerate(notes):
    out.append(f'\t\t<text id="{i}" type="text/plain" rect="({r[0]}.0, {r[1]}.0, {r[2]}.0, {r[3]}.0)" font-family="Helvetica" font-size="13">{escape(txt)}</text>')
out.append('\t</annotations>'); out.append('\t<node_properties />'); out.append('</scheme>')
open('out/week4/practicum4/practicum4_suribank.ows','w',encoding='utf-8').write('\n'.join(out)+'\n')
