import glob, sys
from PIL import Image, ImageDraw
B='/tmp/claude-0/-home-user-menssana/175e1d50-6875-5f56-acf6-23260f0c6b9a/scratchpad/'
for c in ('Clip6','Clip7','Clip8'):
    fs=sorted(glob.glob(B+f'remotion/stills_wk2/{c}_*.png'))
    ims=[Image.open(f) for f in fs]; w,h=ims[0].size; cols=3; rows=(len(ims)+cols-1)//cols
    sheet=Image.new('RGB',(cols*w+(cols+1)*10, rows*(h+28)+10),'#DDDDDD'); d=ImageDraw.Draw(sheet)
    for i,(im,f) in enumerate(zip(ims,fs)):
        x=10+(i%cols)*(w+10); y=10+(i//cols)*(h+28)
        sheet.paste(im,(x,y+18)); d.text((x,y+2),f.split('/')[-1],fill='black')
    sheet.save(B+f'out/preview/Kennisclip{c[4:]}_contactsheet.png'); print(c,len(ims),sheet.size)
