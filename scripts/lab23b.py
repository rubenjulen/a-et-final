import sys, warnings, numpy as np
warnings.filterwarnings('ignore')
from Orange.data import Table, Domain
from Orange.classification import TreeLearner, LogisticRegressionLearner, MajorityLearner
from Orange.evaluation import TestOnTestData, CA, AUC
from Orange.widgets.data.owdatasampler import SampleRandomP, SampleRandomN
import inspect
t = Table(sys.argv[1]); dom = t.domain
attrs = [a for a in dom.attributes if a.name != 'terugbetaald']; cls = dom['terugbetaald']
t2 = t.transform(Domain(attrs, cls, dom.metas))
out = SampleRandomP(0.7, stratified=False, random_state=42)(t2)
print(type(out), [len(o) for o in out])
print(inspect.getsource(SampleRandomN.__call__)[:900])
