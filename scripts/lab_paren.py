import sys,warnings; warnings.filterwarnings('ignore')
import numpy as np
from Orange.data import Table, Domain
from Orange.classification import LogisticRegressionLearner, TreeLearner
tr=Table('out/week3/suribank_versie_A.csv'); P=Table('out/week4/suribank_paren.csv')
def st(t):
    attrs=[a for a in t.domain.attributes if a.name!='terugbetaald']
    return t.transform(Domain(attrs, t.domain['terugbetaald'], t.domain.metas))
tr=st(tr); P=st(P)
ids=[str(x) for x in P.get_column('aanvraag_id')]
reg=P.get_column('regio'); rv=P.domain['regio'].values
yes=list(P.domain.class_var.values).index('ja')
for name,L in [('LogReg',LogisticRegressionLearner()),('Tree',TreeLearner(binarize=True, min_samples_leaf=2, min_samples_split=5, max_depth=100, sufficient_majority=0.95))]:
    m=L(tr); pr=m(P,m.Probs)[:,yes]; pc=(pr>=0.5)
    res={}
    for i in range(0,len(ids),2):
        pid=ids[i].split('-')[0]; o,wz=pc[i],pc[i+1]; d=pr[i+1]-pr[i]
        res[pid]=(o,wz,d,rv[int(reg[i])],rv[int(reg[i+1])])
    for kind in 'RG':
        ks=[k for k in res if k[0]==kind]
        ch=[k for k in ks if res[k][0]!=res[k][1]]
        print(name,kind,'pairs',len(ks),'changed',len(ch),'mean|dp|',round(float(np.mean([abs(res[k][2]) for k in ks])),3),'max|dp|',round(float(np.max([abs(res[k][2]) for k in ks])),3))
        if kind=='R':
            k2b=[k for k in ks if res[k][3]=='kust']; b2k=[k for k in ks if res[k][3]=='binnenland']
            print('  kust->binnen n',len(k2b),'ja->nee',sum(1 for k in k2b if res[k][0] and not res[k][1]),'nee->ja',sum(1 for k in k2b if not res[k][0] and res[k][1]),'mean dp',round(float(np.mean([res[k][2] for k in k2b])),3))
            print('  binnen->kust n',len(b2k),'nee->ja',sum(1 for k in b2k if not res[k][0] and res[k][1]),'ja->nee',sum(1 for k in b2k if res[k][0] and not res[k][1]),'mean dp',round(float(np.mean([res[k][2] for k in b2k])),3))
        else:
            print('  changed ids',ch[:6], 'mean dp', round(float(np.mean([res[k][2] for k in ks])),3))
        if kind=='R': print('  example changed', ch[:5])
