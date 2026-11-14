import sys, warnings, numpy as np, pandas as pd
warnings.filterwarnings('ignore')
from Orange.data import Table, Domain
from Orange.classification import LogisticRegressionLearner
def st(t):
    attrs=[a for a in t.domain.attributes if a.name!='terugbetaald']
    return t.transform(Domain(attrs, t.domain['terugbetaald'], t.domain.metas))
tr=st(Table('out/week0/suribank_kredietaanvragen.csv'))
m=LogisticRegressionLearner()(tr)
for f in ['out/week3/suribank_testset.csv','out/week9/suribank_2025_controle.csv','out/week9/suribank_2027.csv']:
    te=Table(f); te=te.transform(tr.domain) if False else st(te)
    # align domain via combined approach: transform to training domain
    te2=te.transform(tr.domain)
    pred=m(te2); act=te2.Y
    reg=pd.read_csv(f).regio.values
    for g in ['alle','kust','binnenland']:
        mask=np.ones(len(act),bool) if g=='alle' else reg==g
        p=pred[mask]; a=act[mask]
        tp=((p==0)&(a==0)).sum(); fp=((p==0)&(a==1)).sum(); fn=((p==1)&(a==0)).sum(); tn=((p==1)&(a==1)).sum(); n=mask.sum()
        print(f.split('/')[-1][:20], g, 'n',n,'CA',round((tp+tn)/n*100,1),'voorspeld_ja%',round((tp+fp)/n*100,1),'werkelijk_ja%',round((tp+fn)/n*100,1),'TP',tp,'FP',fp,'FN',fn,'TN',tn,'ont_goedgek',round(fp/(fp+tn)*100,1),'ont_afgew',round(fn/(tp+fn)*100,1))
