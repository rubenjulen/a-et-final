const { chromium } = require('playwright'); const fs=require('fs'); const path=require('path');
(async()=>{
  const [,, dir, mode, a, b] = process.argv;
  const timing = JSON.parse(fs.readFileSync(path.join(dir,'timing.json')));
  const browser = await chromium.launch(); const page = await browser.newPage({viewport:{width:1920,height:1080}});
  page.on('pageerror', e => console.log('PAGEERROR', e.message));
  await page.addInitScript(`window.TIMING=${JSON.stringify(timing)}`);
  await page.goto('file://'+path.resolve(dir,'scene.html'));
  const out = path.join(dir, mode==='check'?'check':'frames'); fs.mkdirSync(out,{recursive:true});
  if (mode==='check') {
    const keys = Object.keys(timing.starts);
    for (const k of keys){ await page.evaluate(t=>window.render(t), timing.starts[k]+3.5); await page.screenshot({path:path.join(out,`${k}.jpg`),type:'jpeg',quality:60}); }
  } else {
    const fps=25, N=Math.ceil(timing.total*fps); const s=+(a||0), e=Math.min(N, +(b||N));
    for (let k=s;k<e;k++){ await page.evaluate(t=>window.render(t), k/fps); await page.screenshot({path:path.join(out,`f${String(k).padStart(5,'0')}.jpg`),type:'jpeg',quality:88}); }
    console.log('done',s,e,N);
  }
  await browser.close();
})();
