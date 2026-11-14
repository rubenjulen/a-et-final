// node decks2pdf.js <deckdir> <out.pdf> [notes]
const fs=require('fs'),path=require('path');const {chromium}=require('playwright');
const FS=process.env.AET_FONTS||require('path').resolve(__dirname,'../../animatie/node_modules/@fontsource');
const ff=(fam,dir,file,w,st)=>`@font-face{font-family:'${fam}';src:url('file://${FS}/${dir}/files/${file}-latin-${w}-${st}.woff2');font-weight:${w};font-style:${st}}`;
let faces="@font-face{font-family:'Carlito';src:local('Carlito'),url('file:///usr/share/fonts/truetype/crosextra/Carlito-Regular.ttf');font-weight:400}@font-face{font-family:'Carlito';src:local('Carlito Bold'),url('file:///usr/share/fonts/truetype/crosextra/Carlito-Bold.ttf');font-weight:700}";for(const w of [400,600,700])for(const st of ['normal','italic']){faces+=ff('Public Sans','public-sans','public-sans',w,st);faces+=ff('Source Serif 4','source-serif-4','source-serif-4',w,st);}
const ICON={CheckCircle:'✓',Database:'≡',Lightbulb:'!',Settings:'⚙'};
function fix(h){
  h=h.replace(/<x-shape kind="arrow-right" style="([^"]*)"\s*>(\s*<\/x-shape>)?/g,(m,st)=>`<div style="${st};clip-path:polygon(0 30%,60% 30%,60% 0,100% 50%,60% 100%,60% 70%,0 70%);flex:none"></div>`);
  h=h.replace(/<x-shape kind="([a-z-]+)" style="([^"]*)"\s*>(\s*<\/x-shape>)?/g,(m,k,st)=>`<div style="${st};${k==='ellipse'?'border-radius:50%;':k==='rounded'?'border-radius:16px;':''}flex:none"></div>`);
  h=h.replace(/<x-icon name="([A-Za-z]+)" style="([^"]*)"\s*>(\s*<\/x-icon>)?/g,(m,n,st)=>{const wm=st.match(/width:(\d+)px/);const s=wm?+wm[1]:72;return `<div style="${st};border:${Math.max(3,s/18)}px solid currentColor;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:${s*0.5}px;font-weight:700;flex:none;box-sizing:border-box">${ICON[n]||'•'}</div>`;});
  return h;}
(async()=>{
  const [,,dir,out,mode]=process.argv;const deck=JSON.parse(fs.readFileSync(path.join(dir,'project/deck.json')));
  const files=fs.readdirSync(path.join(dir,'project/slides')).map(f=>f.replace('.html',''));
  const order=[...deck.order.filter(i=>files.includes(i)),...files.filter(f=>!deck.order.includes(f))];
  let pages='';
  for(const id of order){
    let h=fs.readFileSync(path.join(dir,'project/slides',id+'.html'),'utf8');
    const am=h.match(/<aside>([\s\S]*?)<\/aside>/);const notes=am?am[1].trim():'';
    if(id==='docent-voorbereiding'&&mode!=='notes')continue;
    h=fix(h.replace(/<aside>[\s\S]*?<\/aside>/,''));
    {const bf=path.join(dir,'blobs.json');if(fs.existsSync(bf)){const B=JSON.parse(fs.readFileSync(bf));for(const k in B)h=h.split('/_blob/'+k).join('file://'+path.resolve(dir,B[k]));}}
    pages+=`<div class="page">${h}</div>`;
    if(mode==='notes'){const fs_=notes.length>2600?22:notes.length>1600?26:30;
      pages+=`<div class="page notes"><div class="nh">Sprekersnotitie · ${id}</div><div class="nt" style="font-size:${fs_}px">${notes||'<em>(geen notitie)</em>'}</div></div>`;}
  }
  const html=`<!doctype html><html><head><meta charset="utf-8"><style>${faces}
  @page{size:1920px 1080px;margin:0}html,body{margin:0;padding:0}
  .page{width:1920px;height:1080px;overflow:hidden;position:relative;break-after:page}
  .page>section{width:1920px;height:1080px;box-sizing:border-box;overflow:hidden;position:relative}
  section *{box-sizing:border-box;margin:0}section ul,section ol{padding-left:1.2em}section li{margin:0}
  section table{border-collapse:collapse;width:100%}section th{text-align:left;font-weight:700;padding:14px 18px;border-bottom:3px solid rgba(28,36,33,.35)}section td{padding:14px 18px;border-bottom:2px solid rgba(28,36,33,.15);vertical-align:top;height:1.4em}
  .notes{background:#FFFDF8;padding:96px 128px;box-sizing:border-box;font-family:'Public Sans',Arial,sans-serif;color:#1C2421}
  .nh{font-size:24px;font-weight:700;color:#2F6B4F;text-transform:uppercase;letter-spacing:2px;margin-bottom:28px}
  .nt{line-height:1.5;white-space:pre-wrap}
  </style></head><body>${pages}</body></html>`;
  const tmp=out.replace(/\.pdf$/,'.html');fs.writeFileSync(tmp,html);
  const b=await chromium.launch();const p=await b.newPage({viewport:{width:1920,height:1080}});
  await p.goto('file://'+path.resolve(tmp));await p.evaluate(()=>document.fonts.ready);
  const over=await p.evaluate(()=>{const r=[];for(const s of document.querySelectorAll('.page>section')){if(s.scrollHeight>s.clientHeight+4){const z=s.clientHeight/s.scrollHeight;s.style.overflow='visible';s.style.height='auto';s.style.width=(1920/z)+'px';s.style.zoom=z;const z2=1080/s.getBoundingClientRect().height;if(z2<1){s.style.zoom=z*z2;s.style.width=(1920/(z*z2))+'px';}r.push(s.id+'('+Math.round(s.style.zoom*100)+'%)');}}return r;});
  await p.pdf({path:out,width:'1920px',height:'1080px',printBackground:true,preferCSSPageSize:true});
  await b.close();fs.unlinkSync(tmp);console.log('ok',out,order.length,'overflow:',over.join(',')||'-');
})();
