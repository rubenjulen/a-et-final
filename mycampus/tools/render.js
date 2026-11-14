// usage: node render.js in.md out.pdf "Week 2" "Titel" 
const {execFileSync}=require('child_process');const fs=require('fs');const path=require('path');
const {chromium}=require('playwright') ;
(async()=>{
 const [,,inp,out,kicker,title]=process.argv;
 const body=execFileSync('pandoc',['-f','gfm','-t','html5',inp]).toString();
 const FONTS=process.env.AET_FONTS||path.resolve(__dirname,'../../animatie/node_modules/@fontsource');
 const css=fs.readFileSync(path.join(__dirname,'style.css'),'utf8').split('__FONTS__').join(FONTS);
 const LOGO=fs.readFileSync(path.resolve(__dirname,'../../lesmateriaal/huisstijl/janssen_logo.png')).toString('base64');
 const html=`<!doctype html><html lang="nl"><head><meta charset="utf-8"><style>${css}</style></head><body><div class="cover"><div class="kicker">AI &amp; Ethics (A-ET) · ${kicker} · studentversie</div><h1>${title}</h1></div>${body}</body></html>`;
 const tmp=out.replace(/\.pdf$/,'.html'); fs.writeFileSync(tmp,html);
 const b=await chromium.launch(); const p=await b.newPage();
 await p.goto('file://'+path.resolve(tmp)); await p.evaluate(()=>document.fonts.ready);
 await p.pdf({path:out,format:'Letter',margin:{top:'24mm',bottom:'18mm',left:'20mm',right:'20mm'},displayHeaderFooter:true,
  headerTemplate:`<div style="width:100%;padding:0 20mm;display:flex;justify-content:flex-end"><img style="height:7mm" src="data:image/png;base64,${LOGO}"></div>`,
  footerTemplate:`<div style="font-size:8pt;color:#25282A;width:100%;padding:0 20mm;display:flex;justify-content:space-between;font-family:'Times New Roman',serif"><span>Collegejaar 2026-2027 · ICT A-ET ${kicker}</span><span>Pagina <span class="pageNumber"></span> van <span class="totalPages"></span></span></div>`,printBackground:true});
 await b.close(); fs.unlinkSync(tmp); console.log('ok',out);
})();
