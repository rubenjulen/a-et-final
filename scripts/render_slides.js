const { chromium } = require('playwright');
const fs = require('fs'); const path = require('path');
(async () => {
  const [,, root, outdir] = process.argv;
  const deck = JSON.parse(fs.readFileSync(path.join(root,'project/deck.json'),'utf8'));
  fs.mkdirSync(outdir,{recursive:true});
  const browser = await chromium.launch();
  const page = await browser.newPage({viewport:{width:1920,height:1080}, deviceScaleFactor:1});
  for (const id of deck.order) {
    let html = fs.readFileSync(path.join(root,'project/slides',id+'.html'),'utf8');
    html = html.replace(/<aside>[\s\S]*?<\/aside>/g,'');
    const doc = `<!doctype html><html><head><meta charset="utf-8"><style>
      *{box-sizing:border-box;margin:0}html,body{width:1920px;height:1080px;overflow:hidden;background:#F6F3EC}
      section{width:1920px;height:1080px;overflow:hidden}ul,ol{padding-left:1.2em}
      </style></head><body>${html}</body></html>`;
    await page.setContent(doc,{waitUntil:'load'});
    await page.screenshot({path:path.join(outdir,id+'.png')});
  }
  await browser.close();
})();
