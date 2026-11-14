import sys, json, base64, re
raw = open(sys.argv[1]).read()
print(raw[:300])
try:
    obj = json.loads(raw)
except Exception:
    obj = None
def find_b64(o):
    if isinstance(o, dict):
        for k, v in o.items():
            r = find_b64(v)
            if r: return r
    elif isinstance(o, list):
        for v in o:
            r = find_b64(v)
            if r: return r
    elif isinstance(o, str) and len(o) > 10000:
        return o
if obj is not None:
    b = find_b64(obj)
else:
    b = max(re.findall(r'[A-Za-z0-9+/=]{10000,}', raw), key=len)
open(sys.argv[2], 'wb').write(base64.b64decode(b))
