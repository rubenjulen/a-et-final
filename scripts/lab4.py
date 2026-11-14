import sys, warnings, numpy as np
warnings.filterwarnings('ignore')
from Orange.data import Table, Domain
from Orange.classification import LogisticRegressionLearner, TreeLearner
d = sys.argv[1]
def settarget(t, drop=()):
    attrs=[a for a in t.domain.attributes if a.name!='terugbetaald' and a.name not in drop]
    return t.transform(Domain(attrs, t.domain['terugbetaald'], t.domain.metas))
TE = Table(f'{d}/suribank_testset.csv')
reg = TE.get_column('regio'); rv = TE.domain['regio'].values
learners = {'LogReg': LogisticRegressionLearner(), 'Tree': TreeLearner(binarize=True, min_samples_leaf=2, min_samples_split=5, max_depth=100, sufficient_majority=0.95)}
for version in ['A','B']:
  for drop in [(), ('geslacht','district','regio')]:
    tr = settarget(Table(f'{d}/suribank_versie_{version}.csv'), drop)
    te = settarget(TE, drop)
    for ln, L in learners.items():
        m = L(tr); pred = m(te); act = te.Y
        for gi, g in enumerate(rv):
            mask = reg==gi; p=pred[mask]; a=act[mask]
            tp=int(((p==0)&(a==0)).sum()); fp=int(((p==0)&(a==1)).sum()); fn=int(((p==1)&(a==0)).sum()); tn=int(((p==1)&(a==1)).sum()); n=mask.sum()
            print(f'{version} {"zonder" if drop else "alles":6s} {ln:6s} {g:10s} n={n} CA={(tp+tn)/n:.3f} goedgek={(tp+fp)/n:.3f} TP={tp} FP={fp} FN={fn} TN={tn} onterecht_afgewezen={fn/(tp+fn):.3f} onterecht_goedgek={fp/(fp+tn):.3f}')
