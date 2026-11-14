import sys, warnings, math, numpy as np
warnings.filterwarnings('ignore')
import sklearn.model_selection as skl
from Orange.data import Table, Domain
from Orange.classification import TreeLearner, LogisticRegressionLearner, MajorityLearner
from Orange.evaluation import TestOnTestData, CA, AUC
t = Table(sys.argv[1]); dom = t.domain
attrs = [a for a in dom.attributes if a.name != 'terugbetaald']; cls = dom['terugbetaald']
t2 = t.transform(Domain(attrs, cls, dom.metas))
n = int(math.ceil(len(t2)*0.7))
others, sample = next(iter(skl.ShuffleSplit(n_splits=1, test_size=n, random_state=42).split(t2)))
train, test = t2[sample], t2[others]
print('train', len(train), 'test', len(test), 'ja in test', int((test.Y==0).sum()))
L = [TreeLearner(binarize=True, min_samples_leaf=2, min_samples_split=5, max_depth=100, sufficient_majority=0.95), LogisticRegressionLearner(), MajorityLearner()]
names = ['Tree','Logistic Regression','Constant']
def rep(tr, te, label):
    res = TestOnTestData()(tr, te, L)
    print('==', label)
    for i,nm in enumerate(names):
        p=res.predicted[i]; a=res.actual
        tp=int(((p==0)&(a==0)).sum()); fp=int(((p==0)&(a==1)).sum()); fn=int(((p==1)&(a==0)).sum()); tn=int(((p==1)&(a==1)).sum())
        prec=tp/(tp+fp) if tp+fp else float('nan'); rec=tp/(tp+fn)
        print(f'{nm:20s} CA={CA(res)[i]:.3f} AUC={AUC(res)[i]:.3f} TP={tp} FP={fp} FN={fn} TN={tn} Prec(ja)={prec:.3f} Recall(ja)={rec:.3f}')
    return res
res = rep(train, test, 'alle kenmerken')
keep = [a for a in attrs if a.name not in ('geslacht','district','regio')]
d3 = Domain(keep, cls, dom.metas)
rep(train.transform(d3), test.transform(d3), 'zonder geslacht, district, regio')
tree = L[0](train)
print('nodes', tree.node_count(), 'leaves', tree.leaf_count(), 'depth', tree.depth())
txt = tree.print_tree()
print('\n'.join(txt.splitlines()[:12]))
# where does district appear: count nodes splitting on district by depth
import re
lines = txt.splitlines()
for nm in ['district','regio','geslacht','leeftijd']:
    depths=[ (len(l)-len(l.lstrip()))//4 for l in lines if re.search(r'\b'+nm+r'\b', l)]
    print(nm, 'count', len(depths), 'min depth', min(depths) if depths else None)
# root var
print('root var:', tree.root.attr.name if tree.root.attr else None)
# logistic predictions near 0.5
lr = L[1](train)
probs = lr(test, ret=1)  # probabilities
pja = probs[:,0]
ids = test.metas[:,0]
order = np.argsort(np.abs(pja-0.5))[:3]
for k in order:
    row = test[k]
    print(ids[k], round(pja[k],2), 'werkelijk', row.get_class(), {a.name: row[a] for a in attrs if a.name in ('district','dienstverband','maandinkomen_srd','gevraagd_bedrag_srd','looptijd_maanden','eerdere_betalingsachterstand')})
hi = np.argsort(-pja)[:1]; lo=np.argsort(pja)[:1]
for k in list(hi)+list(lo): print('extreme', ids[k], round(pja[k],2), test[k].get_class())
