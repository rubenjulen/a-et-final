import glob, sys
from PIL import Image, ImageDraw
# usage: python3 wk6tools/sheet.py <out.png> [glob]
out = sys.argv[1]; pat = sys.argv[2] if len(sys.argv) > 2 else 'stills_wk6/KaderD_*.png'
fs = sorted(glob.glob(pat)); ims = [Image.open(f) for f in fs]; w, h = ims[0].size; cols = 3; rows = (len(ims) + cols - 1) // cols
sheet = Image.new('RGB', (cols * w + (cols + 1) * 10, rows * (h + 28) + 10), '#DDDDDD'); d = ImageDraw.Draw(sheet)
for i, (im, f) in enumerate(zip(ims, fs)):
    x = 10 + (i % cols) * (w + 10); y = 10 + (i // cols) * (h + 28)
    sheet.paste(im, (x, y + 18)); d.text((x, y + 2), f.split('/')[-1], fill='black')
sheet.save(out); print(out, len(ims), sheet.size)
