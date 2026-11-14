import sys, warnings, numpy as np, pandas as pd
warnings.filterwarnings('ignore')
from Orange.data import Table, Domain
from Orange.classification import LogisticRegressionLearner
d = sys.argv[1]
def settarget(t):
    attrs=[a for a in t.domain.attributes if a.name!='terugbetaald']
    return t.transform(Domain(attrs, t.domain['terugbetaald'], t.domain.metas))
tr = settarget(Table(f'{d}/suribank_versie_A.csv')); te = settarget(Table(f'{d}/suribank_testset.csv'))
m = LogisticRegressionLearner()(tr)
p1 = m(te, ret=1)[:,0]
# ground truth: concatenate in one file
a=pd.read_csv(f'{d}/suribank_versie_A.csv'); b=pd.read_csv(f'{d}/suribank_testset.csv')
c=pd.concat([a,b]); c['maandinkomen_srd']=c['maandinkomen_srd'].astype('Int64'); c.to_csv('/tmp/claude-0/-home-user-menssana/175e1d50-6875-5f56-acf6-23260f0c6b9a/scratchpad/combo.csv',index=False)
cc = settarget(Table('/tmp/claude-0/-home-user-menssana/175e1d50-6875-5f56-acf6-23260f0c6b9a/scratchpad/combo.csv'))
m2 = LogisticRegressionLearner()(cc[:len(a)])
p2 = m2(cc[len(a):], ret=1)[:,0]
print('max diff', float(np.abs(p1-p2).max()))
print('train district values', tr.domain['district'].values); print('test district values', te.domain['district'].values)
print('class values', tr.domain.class_var.values, te.domain.class_var.values)
