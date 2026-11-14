import sys, numpy as np
import Orange
from Orange.data import Table, Domain
from Orange.classification import TreeLearner, LogisticRegressionLearner, MajorityLearner
from Orange.evaluation import CrossValidation, TestOnTestData, CA, AUC, Precision, Recall
t = Table(sys.argv[1])
dom = t.domain
print('attrs', [(a.name, 'D' if a.is_discrete else 'C' if a.is_continuous else 'S') for a in dom.attributes])
print('class', dom.class_var, 'metas', [m.name for m in dom.metas])
# set target
attrs = [a for a in dom.attributes if a.name != 'terugbetaald']
cls = dom['terugbetaald']
d2 = Domain(attrs, cls, dom.metas)
t2 = t.transform(d2)
print('class values', cls.values)
learners = [TreeLearner(binarize=True, min_samples_leaf=2, min_samples_split=5, max_depth=100, sufficient_majority=0.95), LogisticRegressionLearner(), MajorityLearner()]
names = ['Tree','LogReg','Constant']
def report(res, label):
    print('==', label)
    ja = cls.values.index('ja')
    for i,n in enumerate(names):
        ca = CA(res)[i]; auc = AUC(res)[i]
        pred = res.predicted[i]; act = res.actual
        tp = int(((pred==ja)&(act==ja)).sum()); fp=int(((pred==ja)&(act!=ja)).sum()); fn=int(((pred!=ja)&(act==ja)).sum()); tn=int(((pred!=ja)&(act!=ja)).sum())
        prec = tp/(tp+fp) if tp+fp else float('nan'); rec = tp/(tp+fn)
        print(f'{n:9s} CA={ca:.3f} AUC={auc:.3f} TP={tp} FP={fp} FN={fn} TN={tn} prec_ja={prec:.3f} rec_ja={rec:.3f}')
cv = CrossValidation(k=10, stratified=True, random_state=42)
report(cv(t2, learners), 'CV10 all features')
# holdout 70/30 several seeds
rng = np.random.default_rng(0)
for seed in [1,2,3]:
    idx = np.random.default_rng(seed).permutation(len(t2)); cut = int(0.7*len(t2))
    res = TestOnTestData()(t2[idx[:cut]], t2[idx[cut:]], learners)
    report(res, f'holdout seed {seed}')
# without geslacht, district, regio
keep = [a for a in attrs if a.name not in ('geslacht','district','regio')]
t3 = t.transform(Domain(keep, cls, dom.metas))
report(cv(t3, learners), 'CV10 zonder geslacht/district/regio')
# per regio error rates for logreg (CV, all features)
res = cv(t2, learners)
reg = t2.get_column('regio')
regvals = t2.domain['regio'].values
ja = cls.values.index('ja')
for i,n in enumerate(names[:2]):
    for rv in range(len(regvals)):
        m = reg==rv; pred=res.predicted[i][m]; act=res.actual[m]
        fn = ((pred!=ja)&(act==ja)).sum()/max((act==ja).sum(),1); fp=((pred==ja)&(act!=ja)).sum()/max((act!=ja).sum(),1)
        print(n, regvals[rv], 'n',m.sum(),'acc',round((pred==act).mean(),3),'onterecht_afgewezen_rate',round(fn,3),'onterecht_goedgekeurd_rate',round(fp,3))
# tree root
model = learners[0](t2)
print('tree nodes', model.node_count(), 'leaves', model.leaf_count(), 'depth', model.depth())
print(model.print_tree()[:1500] if hasattr(model,'print_tree') else '')
