// usage: node render.js in.md out.pdf "Week 2" "Titel" 
const {execFileSync}=require('child_process');const fs=require('fs');const path=require('path');
const {chromium}=require('playwright') ;
(async()=>{
 const [,,inp,out,kicker,title]=process.argv;
 const body=execFileSync('pandoc',['-f','gfm','-t','html5',inp]).toString();
 const FONTS=process.env.AET_FONTS||path.resolve(__dirname,'../../animatie/node_modules/@fontsource');
 const css=fs.readFileSync(path.join(__dirname,'style.css'),'utf8').split('__FONTS__').join(FONTS);
 const html=`<!doctype html><html lang="nl"><head><meta charset="utf-8"><style>${css}</style></head><body><div class="cover"><div class="kicker">AI &amp; Ethics (A-ET) · ${kicker} · studentversie</div><h1>${title}</h1></div>${body}</body></html>`;
 const tmp=out.replace(/\.pdf$/,'.html'); fs.writeFileSync(tmp,html);
 const b=await chromium.launch(); const p=await b.newPage();
 await p.goto('file://'+path.resolve(tmp)); await p.evaluate(()=>document.fonts.ready);
 await p.pdf({path:out,format:'A4',margin:{top:'18mm',bottom:'18mm',left:'18mm',right:'18mm'},displayHeaderFooter:true,
  headerTemplate:'<div></div>',
  footerTemplate:`<div style="font-size:7.5pt;color:#6a7179;width:100%;padding:0 18mm;display:flex;justify-content:space-between;font-family:Arial"><span>A-ET 2026-2027 · ${kicker}</span><span>pagina <span class="pageNumber"></span> van <span class="totalPages"></span></span></div>`,printBackground:true});
 await b.close(); fs.unlinkSync(tmp); console.log('ok',out);
})();
