import numpy as np, pandas as pd, sys
out=sys.argv[1]; rng=np.random.default_rng(2028); N=1000
districts=['Paramaribo','Wanica','Nickerie','Commewijne','Para','Saramacca','Coronie','Marowijne','Brokopondo','Sipaliwini']
w=np.array([.34,.17,.06,.05,.04,.03,.01,.10,.08,.12]); w/=w.sum()
binnen={'Marowijne','Brokopondo','Sipaliwini'}
d=rng.choice(districts,N,p=w); regio=np.where(np.isin(d,list(binnen)),'binnenland','kust')
dv=np.array([rng.choice(['vast','tijdelijk','zelfstandig','informeel'],p=[.48,.20,.17,.15] if r=='kust' else [.22,.18,.20,.40]) for r in regio])
age=np.clip(rng.normal(37,10,N),21,65).round().astype(int); sex=rng.choice(['M','V'],N)
mult={'vast':1.15,'tijdelijk':0.9,'zelfstandig':1.0,'informeel':0.7}
INF=float(sys.argv[2]); SHOCK=float(sys.argv[3])
med=np.where(regio=='kust',16000,10000)
inc_real=med*np.array([mult[x] for x in dv])*np.exp(rng.normal(0,0.45,N)); inc_real=np.clip(inc_real,5000,80000)
inc=(np.clip(inc_real*INF,5000,120000)/100).round()*100
jaren=np.clip(np.minimum(age-20,rng.exponential(5,N)),0,25).round().astype(int)
jaren=np.where(dv=='informeel',np.clip(rng.exponential(3,N),0,15).round(),jaren).astype(int)
schuld=(inc*rng.gamma(1.2,1.5,N)/500).round()*500; schuld=np.where(rng.random(N)<0.35,0,schuld)
loopt=rng.choice([12,24,36,48,60],N,p=[.15,.25,.3,.15,.15])
gevr=(np.clip(inc*rng.uniform(2,14,N),10000,400000)/1000).round()*1000
achter=np.where(rng.random(N)<np.where(dv=='informeel',.22,.14),'ja','nee')
klant=np.clip(np.minimum(age-18,rng.exponential(6,N)),0,25).round().astype(int)
ratio=(gevr/loopt)/inc; dve={'vast':.4,'tijdelijk':0,'zelfstandig':-.1,'informeel':-.3}
z=1.3+0.9*np.log(inc/INF/15000)-1.6*(achter=='ja')-6*(ratio-0.15)+np.array([dve[x] for x in dv])-0.08*(schuld/inc)+0.02*klant-SHOCK
y=np.where(rng.random(N)<1/(1+np.exp(-z)),'ja','nee')
inc_obs=pd.array(inc.astype(int),dtype='Int64'); miss=rng.random(N)<np.where(dv=='informeel',.15,.02); inc_obs[miss]=pd.NA
df=pd.DataFrame({'aanvraag_id':[f'SK{i:04d}' for i in range(1,N+1)],'leeftijd':age,'geslacht':sex,'district':d,'regio':regio,'dienstverband':dv,'jaren_in_huidig_werk':jaren,'maandinkomen_srd':inc_obs,'bestaande_schulden_srd':schuld.astype(int),'gevraagd_bedrag_srd':gevr.astype(int),'looptijd_maanden':loopt,'eerdere_betalingsachterstand':achter,'klant_sinds_jaren':klant,'terugbetaald':y})
df.to_csv(f'{out}/suribank_2027.csv',index=False)
print('ja%',round((df.terugbetaald=='ja').mean()*100,1),'binnen%',round((regio=='binnenland').mean()*100,1),'inf%',round((dv=='informeel').mean()*100,1),'medinc',df.maandinkomen_srd.median(),'miss',int(miss.sum()))
print(df.groupby('regio').terugbetaald.apply(lambda s:round((s=='ja').mean()*100,1)).to_dict())
