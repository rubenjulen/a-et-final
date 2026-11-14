import sys, warnings, numpy as np
warnings.filterwarnings('ignore')
from Orange.data import Table, Domain
from Orange.classification import LogisticRegressionLearner
from Orange.evaluation import TestOnTestData
d=sys.argv[1]
def st(t, drop=()):
    a=[x for x in t.domain.attributes if x.name!='terugbetald' and x.name!='terugbetaald' and x.name not in drop]
    return t.transform(Domain(a, t.domain['terugbetaald'], t.domain.metas))
tr=st(Table(f'{d}/suribank_versie_B.csv'),('geslacht','district','regio')); te=st(Table(f'{d}/suribank_testset.csv'))
b = te[te.get_column('regio')==te.domain['regio'].values.index('binnenland')]
res=TestOnTestData()(tr, b, [LogisticRegressionLearner()])
p=res.predicted[0]; a=res.actual
print('n',len(b),'FN rate', round(((p==1)&(a==0)).sum()/(a==0).sum(),3))
