import csv, random
random.seed(2030)
rows=list(csv.DictReader(open('out/week3/suribank_testset.csv')))
cols=list(rows[0].keys())
kust=['Paramaribo','Wanica','Nickerie','Commewijne','Para','Saramacca']; kw=[267,155,56,54,37,26]
binnen=['Sipaliwini','Marowijne','Brokopondo']; bw=[174,115,111]
out=[]
sample=random.sample(rows,200)
for i,r in enumerate(sample[:100]):
    a=dict(r); b=dict(r)
    if r['regio']=='kust':
        b['district']=random.choices(binnen,bw)[0]; b['regio']='binnenland'
    else:
        b['district']=random.choices(kust,kw)[0]; b['regio']='kust'
    pid=f'R{i+1:03d}'
    a['aanvraag_id']=pid+'-orig'; b['aanvraag_id']=pid+'-wijz'
    out+= [a,b]
for i,r in enumerate(sample[100:]):
    a=dict(r); b=dict(r); b['geslacht']='V' if r['geslacht']=='M' else 'M'
    pid=f'G{i+1:03d}'
    a['aanvraag_id']=pid+'-orig'; b['aanvraag_id']=pid+'-wijz'
    out+=[a,b]
w=csv.DictWriter(open('out/week4/suribank_paren.csv','w',newline=''),fieldnames=cols); w.writeheader(); w.writerows(out)
print(len(out))
