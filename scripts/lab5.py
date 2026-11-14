import sys, warnings, numpy as np
warnings.filterwarnings('ignore')
from Orange.data import Table, Domain
from Orange.classification import LogisticRegressionLearner, TreeLearner
d = sys.argv[1]
def settarget(t, drop=()):
    attrs=[a for a in t.domain.attributes if a.name!='terugbetaald' and a.name not in drop]
    return t.transform(Domain(attrs, t.domain['terugbetaald'], t.domain.metas))
drop=('geslacht','district','regio')
tr = settarget(Table(f'{d}/suribank_versie_A.csv'), drop); te = settarget(Table(f'{d}/suribank_testset.csv'), drop)
def ca(m): return float((m(te)==te.Y).mean())
t3 = TreeLearner(binarize=True, min_samples_leaf=2, min_samples_split=5, max_depth=3, sufficient_majority=0.95)(tr)
tf = TreeLearner(binarize=True, min_samples_leaf=2, min_samples_split=5, max_depth=100, sufficient_majority=0.95)(tr)
lr = LogisticRegressionLearner()(tr)
print('CA depth3', round(ca(t3),3), 'leaves', t3.leaf_count(), '| full', round(ca(tf),3), 'leaves', tf.leaf_count(), '| LR', round(ca(lr),3))
print(t3.print_tree())
# LR coefficients (for class ja vs nee): Orange LR coef on continuized/normalized?
sk = lr.skl_model
names = [a.name for a in lr.domain.attributes]
coef = sk.coef_[0]
order = np.argsort(-np.abs(coef))
print('LR coef (positive -> class index 1 = nee):')
for i in order[:10]: print(f'  {names[i]:40s} {coef[i]:+.3f}')
# example rejected applicant in testset: pick a ja-actual predicted nee from binnenland
p = lr(te, ret=1)[:,0]
TE = Table(f'{d}/suribank_testset.csv')
reg = TE.get_column('regio'); ids = TE.metas[:,0]
cand = [i for i in range(len(te)) if te.Y[i]==0 and p[i]<0.5 and TE.domain['regio'].values[int(reg[i])]=='binnenland']
for i in cand[:3]:
    r = TE[i]
    print(ids[i], round(p[i],2), {a.name: str(r[a]) for a in TE.domain.attributes if a.name in ('dienstverband','maandinkomen_srd','gevraagd_bedrag_srd','looptijd_maanden','eerdere_betalingsachterstand','bestaande_schulden_srd','leeftijd')})
