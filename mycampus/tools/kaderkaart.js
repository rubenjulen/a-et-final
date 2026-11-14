// Rendert de kaderkaart (één pagina A4 liggend) naar pdf.
// Gebruik: node kaderkaart.js [uitvoer.pdf]   (standaard: lesmateriaal/algemeen/ICT A-ET Kaderkaart.pdf)
const fs=require('fs'),path=require('path');const {chromium}=require('playwright');
const FONTS=process.env.AET_FONTS||path.resolve(__dirname,'../../animatie/node_modules/@fontsource');
const ff=(fam,dir,file,w,st='normal')=>`@font-face{font-family:'${fam}';src:url('file://${FONTS}/${dir}/files/${file}');font-weight:${w};font-style:${st}}`;
const faces=[ff('PS','public-sans','public-sans-latin-400-normal.woff2',400),ff('PS','public-sans','public-sans-latin-400-italic.woff2',400,'italic'),
 ff('PS','public-sans','public-sans-latin-700-normal.woff2',700),ff('SS','source-serif-4','source-serif-4-latin-600-normal.woff2',600),
 ff('SS','source-serif-4','source-serif-4-latin-700-normal.woff2',700)].join('\n');
(async()=>{
 const out=process.argv[2]||path.resolve(__dirname,'../../lesmateriaal/algemeen/ICT A-ET Kaderkaart.pdf');
 const html=fs.readFileSync(path.join(__dirname,'kaderkaart','kaderkaart.html'),'utf8').replace('__FONTFACES__',faces);
 const tmp=path.join(__dirname,'kaderkaart','_render.html');fs.writeFileSync(tmp,html);
 const b=await chromium.launch();const p=await b.newPage();await p.goto('file://'+tmp);await p.evaluate(()=>document.fonts.ready);
 await p.pdf({path:out,format:'A4',landscape:true,printBackground:true,margin:{top:0,bottom:0,left:0,right:0}});
 await b.close();fs.unlinkSync(tmp);console.log('ok',out);
})();
