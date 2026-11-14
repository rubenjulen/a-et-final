import warnings; warnings.filterwarnings('ignore')
from Orange.data import Table, Domain
from Orange.classification import LogisticRegressionLearner, TreeLearner
from openpyxl import load_workbook
tr=Table('out/week3/suribank_versie_A.csv'); P=Table('out/week4/suribank_paren.csv')
def st(t):
    attrs=[a for a in t.domain.attributes if a.name!='terugbetaald']
    return t.transform(Domain(attrs, t.domain['terugbetaald'], t.domain.metas))
tr=st(tr); P=st(P); yes=list(P.domain.class_var.values).index('ja')
ids=[str(x) for x in P.get_column('aanvraag_id')]
pr={}
for n,Lr in [('LR',LogisticRegressionLearner()),('T',TreeLearner(binarize=True, min_samples_leaf=2, min_samples_split=5, max_depth=100, sufficient_majority=0.95))]:
    m=Lr(tr); pr[n]=m(P,m.Probs)[:,yes]
wb=load_workbook('out/week4/practicum4/practicum4_testlogboek.xlsx')
ws=wb['B_import']
# shuffle order to test MATCH: reverse
for r,k in enumerate(reversed(range(len(ids))),2):
    ws.cell(r,1,ids[k]); ws.cell(r,2,float(pr['LR'][k])); ws.cell(r,3,float(pr['T'][k]))
a=wb['A_log']; a['H2']='goed'; a['K2']='fout'; a['H3']='fout'; a['K3']='fout'; a['H62']='matig'
wb.save('check/logboek_test.xlsx')
