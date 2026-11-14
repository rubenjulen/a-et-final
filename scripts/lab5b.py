import sys, warnings, numpy as np
warnings.filterwarnings('ignore')
from Orange.data import Table, Domain
from Orange.classification import LogisticRegressionLearner, TreeLearner
d=sys.argv[1]
def st(t, drop=()):
    a=[x for x in t.domain.attributes if x.name!='terugbetaald' and x.name not in drop]
    return t.transform(Domain(a, t.domain['terugbetaald'], t.domain.metas))
drop=('geslacht','district','regio')
tr=st(Table(f'{d}/suribank_versie_A.csv'),drop); TE=st(Table(f'{d}/suribank_testset.csv'))
ms={'kort':TreeLearner(binarize=True,min_samples_leaf=2,min_samples_split=5,max_depth=3,sufficient_majority=0.95)(tr),
    'lang':TreeLearner(binarize=True,min_samples_leaf=2,min_samples_split=5,max_depth=100,sufficient_majority=0.95)(tr),
    'lr':LogisticRegressionLearner()(tr)}
ids=list(TE.metas[:,0]); i=ids.index('TB0046')
for k,m in ms.items():
    pr=m(TE[i:i+1],ret=2)
    print(k, 'pred', m.domain.class_var.values[int(pr[0][0])], 'p_ja', round(float(pr[1][0][0]),2))
print('actual', TE[i].get_class())
