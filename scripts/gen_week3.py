import numpy as np, pandas as pd, sys
out = sys.argv[1]
districts = ['Paramaribo','Wanica','Nickerie','Commewijne','Para','Saramacca','Coronie','Marowijne','Brokopondo','Sipaliwini']
kust_d = districts[:7]; kust_w = np.array([.40,.20,.07,.06,.05,.04,.01]); kust_w/=kust_w.sum()
binn_d = districts[7:]; binn_w = np.array([.05,.05,.07]); binn_w/=binn_w.sum()
def gen(n, regio_fixed, seed, prefix):
    rng = np.random.default_rng(seed)
    if regio_fixed=='kust': d = rng.choice(kust_d, n, p=kust_w)
    else: d = rng.choice(binn_d, n, p=binn_w)
    regio = np.array([regio_fixed]*n)
    dv = np.array([rng.choice(['vast','tijdelijk','zelfstandig','informeel'], p=[.55,.20,.15,.10] if r=='kust' else [.25,.20,.20,.35]) for r in regio])
    age = np.clip(rng.normal(38,10,n),21,65).round().astype(int)
    sex = rng.choice(['M','V'], n)
    mult = {'vast':1.15,'tijdelijk':0.9,'zelfstandig':1.0,'informeel':0.7}
    med = np.where(regio=='kust',16000,10000)
    inc = med*np.array([mult[x] for x in dv])*np.exp(rng.normal(0,0.45,n)); inc=(np.clip(inc,5000,80000)/100).round()*100
    jaren = np.clip(np.minimum(age-20, rng.exponential(5,n)),0,25).round().astype(int)
    jaren = np.where(dv=='informeel', np.clip(rng.exponential(3,n),0,15).round(), jaren).astype(int)
    schuld = (inc*rng.gamma(1.2,1.5,n)/500).round()*500; schuld=np.where(rng.random(n)<0.35,0,schuld)
    loopt = rng.choice([12,24,36,48,60],n,p=[.15,.25,.3,.15,.15])
    gevr = (np.clip(inc*rng.uniform(2,14,n),10000,300000)/1000).round()*1000
    achter = np.where(rng.random(n) < np.where(dv=='informeel',.22,.14),'ja','nee')
    klant = np.clip(np.minimum(age-18, rng.exponential(6,n)),0,25).round().astype(int)
    ratio=(gevr/loopt)/inc; dve={'vast':.4,'tijdelijk':0,'zelfstandig':-.1,'informeel':-.3}
    z = 1.3+0.9*np.log(inc/15000)-1.6*(achter=='ja')-6*(ratio-0.15)+np.array([dve[x] for x in dv])-0.08*(schuld/inc)+0.02*klant
    y = np.where(rng.random(n)<1/(1+np.exp(-z)),'ja','nee')
    inc_obs = pd.array(inc.astype(int), dtype='Int64'); miss = rng.random(n) < np.where(dv=='informeel',.15,.02); inc_obs[miss]=pd.NA
    return pd.DataFrame({'aanvraag_id':[f'{prefix}{i:04d}' for i in range(1,n+1)],'leeftijd':age,'geslacht':sex,'district':d,'regio':regio,'dienstverband':dv,'jaren_in_huidig_werk':jaren,'maandinkomen_srd':inc_obs,'bestaande_schulden_srd':schuld.astype(int),'gevraagd_bedrag_srd':gevr.astype(int),'looptijd_maanden':loopt,'eerdere_betalingsachterstand':achter,'klant_sinds_jaren':klant,'terugbetaald':y})
gen(600,'kust',3101,'TK').to_csv(f'{out}/suribank_test_kust.csv', index=False)
gen(400,'binnenland',3102,'TB').to_csv(f'{out}/suribank_test_binnenland.csv', index=False)
base = pd.read_csv(sys.argv[2])
base.to_csv(f'{out}/suribank_versie_A.csv', index=False)
B = base.copy(); rng = np.random.default_rng(3103)
flip = (B.regio=='binnenland') & (B.terugbetaald=='ja') & (rng.random(len(B)) < float(sys.argv[3]))
B.loc[flip,'terugbetaald']='nee'
B['maandinkomen_srd']=B['maandinkomen_srd'].astype('Int64')
B.to_csv(f'{out}/suribank_versie_B.csv', index=False)
print('flipped', int(flip.sum()), 'binnenland ja A', int(((base.regio=='binnenland')&(base.terugbetaald=='ja')).sum()))
for f in ['suribank_test_kust','suribank_test_binnenland']:
    t=pd.read_csv(f'{out}/{f}.csv'); print(f, len(t), 'ja%', round((t.terugbetaald=='ja').mean()*100,1))
for nm,df in [('A',base),('B',B)]:
    print(nm, df.groupby('regio').terugbetaald.apply(lambda s: round((s=='ja').mean()*100,1)).to_dict())
