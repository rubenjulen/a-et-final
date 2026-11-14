import numpy as np, pandas as pd, sys
rng = np.random.default_rng(2027)
N = 1200
districts = ['Paramaribo','Wanica','Nickerie','Commewijne','Para','Saramacca','Coronie','Marowijne','Brokopondo','Sipaliwini']
w = [.40,.20,.07,.06,.05,.04,.01,.05,.05,.07]
binnen = {'Marowijne','Brokopondo','Sipaliwini'}
d = rng.choice(districts, N, p=w)
regio = np.where(np.isin(d, list(binnen)), 'binnenland', 'kust')
dv_opts = ['vast','tijdelijk','zelfstandig','informeel']
dv = np.array([rng.choice(dv_opts, p=[.55,.20,.15,.10] if r=='kust' else [.25,.20,.20,.35]) for r in regio])
age = np.clip(rng.normal(38,10,N),21,65).round().astype(int)
sex = rng.choice(['M','V'], N)
mult = {'vast':1.15,'tijdelijk':0.9,'zelfstandig':1.0,'informeel':0.7}
med = np.where(regio=='kust',16000,10000)
inc = med*np.array([mult[x] for x in dv])*np.exp(rng.normal(0,0.45,N))
inc = (np.clip(inc,5000,80000)/100).round()*100
jaren = np.clip(np.minimum(age-20, rng.exponential(5,N)),0,25).round().astype(int)
jaren = np.where(dv=='informeel', np.clip(rng.exponential(3,N),0,15).round(), jaren).astype(int)
schuld = (inc*rng.gamma(1.2,1.5,N)/500).round()*500
schuld = np.where(rng.random(N)<0.35,0,schuld)
loopt = rng.choice([12,24,36,48,60],N,p=[.15,.25,.3,.15,.15])
gevr = np.clip(inc*rng.uniform(2,14,N),10000,300000)
gevr = (gevr/1000).round()*1000
achter = np.where(rng.random(N) < np.where(dv=='informeel',.22,.14),'ja','nee')
klant = np.clip(np.minimum(age-18, rng.exponential(6,N)),0,25).round().astype(int)
ratio = (gevr/loopt)/inc
dve = {'vast':.4,'tijdelijk':0,'zelfstandig':-.1,'informeel':-.3}
z = 1.3 + 0.9*np.log(inc/15000) - 1.6*(achter=='ja') - 6*(ratio-0.15) + np.array([dve[x] for x in dv]) - 0.08*(schuld/inc) + 0.02*klant
p = 1/(1+np.exp(-z))
y = np.where(rng.random(N)<p,'ja','nee')
inc_obs = inc.astype(object)
miss = rng.random(N) < np.where(dv=='informeel',.15,.02)
inc_obs[miss] = np.nan
df = pd.DataFrame({'aanvraag_id':[f'SB{i:04d}' for i in range(1,N+1)],'leeftijd':age,'geslacht':sex,'district':d,'regio':regio,
 'dienstverband':dv,'jaren_in_huidig_werk':jaren,'maandinkomen_srd':inc_obs,'bestaande_schulden_srd':schuld.astype(int),
 'gevraagd_bedrag_srd':gevr.astype(int),'looptijd_maanden':loopt,'eerdere_betalingsachterstand':achter,'klant_sinds_jaren':klant,'terugbetaald':y})
df['maandinkomen_srd'] = pd.to_numeric(df['maandinkomen_srd']).astype('Int64')
df.to_csv(sys.argv[1], index=False)
# stats
print('N', len(df), 'cols', df.shape[1]); print('terugbetaald ja %', round((df.terugbetaald=='ja').mean()*100,1))
print('missing inkomen', df.maandinkomen_srd.isna().sum(), 'by dv', df[df.maandinkomen_srd.isna()].dienstverband.value_counts().to_dict())
print(df.groupby('regio').agg(n=('aanvraag_id','size'), ja=('terugbetaald',lambda s:round((s=='ja').mean()*100,1)), inkomen_med=('maandinkomen_srd','median')))
print(df.groupby('dienstverband').agg(n=('aanvraag_id','size'), ja=('terugbetaald',lambda s:round((s=='ja').mean()*100,1)), inkomen_med=('maandinkomen_srd','median')))
print(df.groupby('district').agg(n=('aanvraag_id','size'), ja=('terugbetaald',lambda s:round((s=='ja').mean()*100,1))).sort_values('n',ascending=False))
print(df.groupby('geslacht').terugbetaald.apply(lambda s:round((s=='ja').mean()*100,1)))
print(df.groupby('eerdere_betalingsachterstand').terugbetaald.apply(lambda s:round((s=='ja').mean()*100,1)))
def H(s):
    p=s.value_counts(normalize=True); return -(p*np.log2(p)).sum()
def ig(col):
    x=df[col]
    if x.dtype!=object and str(x.dtype)!='str': x=pd.qcut(x.astype(float),5,duplicates='drop').astype(str)
    return H(df.terugbetaald)-sum((x==v).mean()*H(df.terugbetaald[x==v]) for v in x.unique())
print({c:round(ig(c),4) for c in df.columns if c not in('aanvraag_id','terugbetaald')})
print(df.describe().round(0).to_string())
