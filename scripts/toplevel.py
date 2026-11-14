import re,sys,html
import xml.etree.ElementTree as ET
x=open(sys.argv[1]).read()
# make parseable: wrap
root=ET.fromstring(x)
prefix=None
for el in root:
    i=el.get('id'); 
    if i and not i.startswith('.'): prefix=i.split('.')[0]
    txt=''.join(el.itertext()).strip().replace('\n',' ')
    print(f"{el.tag[:4]} {i} {el.get('h')} {('H'+el.get('heading')) if el.get('heading') else ''} | {txt[:70]}")
