const { chromium } = require('playwright'); const fs=require('fs'); const path=require('path');
(async()=>{
  const [,, dir, mode] = process.argv;
  const timing = JSON.parse(fs.readFileSync(path.join(dir,'timing.json')));
  const browser = await chromium.launch(); const page = await browser.newPage({viewport:{width:1920,height:1080}});
  await page.addInitScript(`window.TIMING=${JSON.stringify(timing)}`);
  await page.goto('file://'+path.resolve(dir,'scene.html'));
  const out = path.join(dir, mode==='check'?'check':'frames'); fs.mkdirSync(out,{recursive:true});
  if (mode==='check') {
    const ts = timing.starts.map(s=>s+3.2);
    for (let i=0;i<ts.length;i++){ await page.evaluate(t=>window.render(t), ts[i]); await page.screenshot({path:path.join(out,`c${String(i).padStart(2,'0')}.jpg`),type:'jpeg',quality:70}); }
  } else {
    const fps=25, N=Math.ceil(timing.total*fps);
    for (let k=0;k<N;k++){ await page.evaluate(t=>window.render(t), k/fps); await page.screenshot({path:path.join(out,`f${String(k).padStart(5,'0')}.jpg`),type:'jpeg',quality:88}); }
  }
  await browser.close();
})();
