// Kennisclip 5b · Vijf ethische kaders (blok 1). Script: clip5b/build.py; timing: src/timing_c5b.json.
import React from 'react';
import { AbsoluteFill, useCurrentFrame, interpolate, spring, Easing } from 'remotion';
import timing from './timing_c5b.json';
import { FPS, clamp, fade, Pop } from './wk1_kit';
import { J, FONT, JTitle, JBanner, makeJKit } from './janssen_kit';

const { cue, F, QuizN, Root } = makeJKit(timing);
// Moment waarop een woord in de gesproken zin valt (benadering op tekstpositie).
const W = (key, word, off = 0) => {
  const c = cue[key]; const i = c.text.indexOf(word);
  if (i < 0) throw new Error(`woord "${word}" niet in ${key}`);
  return F(key, c.dur * i / c.text.length + off);
};
const sp = (frame, at, cfg = {}) => spring({ frame: frame - at, fps: FPS, config: { damping: 18, stiffness: 120, mass: 0.9, ...cfg } });
const T = ({ children, size = 30, color = J.ink, weight = 400, style = {} }) => <div style={{ fontFamily: FONT, fontSize: size, color, fontWeight: weight, lineHeight: 1.25, ...style }}>{children}</div>;

/* ---------- iconen ---------- */
const Icon = ({ k, size = 80, color = '#fff' }) => {
  const s = { width: size, height: size };
  const st = { fill: 'none', stroke: color, strokeWidth: 6, strokeLinecap: 'round', strokeLinejoin: 'round' };
  if (k === 0) return (<svg viewBox="0 0 100 100" style={s}><g {...st}><line x1="50" y1="18" x2="50" y2="84" /><line x1="18" y1="30" x2="82" y2="30" /><line x1="30" y1="84" x2="70" y2="84" />
    <path d="M18 30 L8 56 Q18 66 28 56 Z" /><path d="M82 30 L72 56 Q82 66 92 56 Z" /></g></svg>);
  if (k === 1) return (<svg viewBox="0 0 100 100" style={s}><g {...st}><line x1="20" y1="20" x2="20" y2="86" /><rect x="20" y="40" width="70" height="14" rx="4" /><line x1="40" y1="40" x2="48" y2="54" /><line x1="62" y1="40" x2="70" y2="54" /><line x1="10" y1="86" x2="30" y2="86" /></g></svg>);
  if (k === 2) return (<svg viewBox="0 0 100 100" style={s}><g {...st}><circle cx="50" cy="52" r="34" /><line x1="50" y1="52" x2="50" y2="18" /><line x1="50" y1="52" x2="80" y2="68" /><line x1="50" y1="52" x2="22" y2="72" /></g></svg>);
  if (k === 3) return (<svg viewBox="0 0 100 100" style={s}><polygon points="50,10 61,38 91,39 67,57 76,87 50,70 24,87 33,57 9,39 39,38" {...st} /></svg>);
  return (<svg viewBox="0 0 100 100" style={s}><g {...st}><path d="M50 52 C30 38 30 18 44 18 C50 18 50 26 50 26 C50 26 50 18 56 18 C70 18 70 38 50 52 Z" /><path d="M10 64 Q30 60 44 70 L66 70 Q74 70 74 78 L44 78" /><path d="M10 86 L58 86 Q72 86 92 66" /></g></svg>);
};
const IconDot = ({ k, col, size = 96, icon = 58, ring }) => (
  <div style={{ width: size, height: size, borderRadius: size / 2, background: col, border: ring ? `4px solid ${ring}` : 'none', boxSizing: 'border-box', display: 'flex', alignItems: 'center', justifyContent: 'center', boxShadow: '0 8px 20px rgba(0,32,96,.18)' }}><Icon k={k} size={icon} /></div>
);

/* ---------- inhoud van de vijf kaders ---------- */
const GOLD2 = '#A9852E';
const K = [
  { id: 'G', name: 'Gevolgen', theory: 'Utilitarisme', q: 'Wat levert het op, en voor wie?', col: J.blue,
    th: [['Jeremy Bentham', 1789, 'Engeland · Principles of Morals and Legislation'], ['John Stuart Mill', 1863, 'Engeland · Utilitarianism']],
    years: '1789 · 1863', idea: 'Kies wat de meeste baten en de minste schade oplevert, voor iedereen die geraakt wordt.', ideaW: ['G2', 'Kies wat'], thW: [['G2', 'Jeremy'], ['G2', 'John']],
    sterk: ['Praktisch en meetbaar', 'Past bij risicobeheer'], zwak: ['Kleine groepen worden weggemiddeld', 'Niet alles is meetbaar, zoals angst'], zwakW: 'kleine groepen',
    safe: 'Hoeveel minder straatroof, tegenover hoeveel foute treffers?' },
  { id: 'P', name: 'Plichten', theory: 'Deontologie', q: 'Wat mag nooit, ook niet als het veel oplevert?', col: J.dblue,
    th: [['Immanuel Kant', 1785, 'Duitsland · Grundlegung zur Metaphysik der Sitten']],
    years: '1785', idea: 'Behandel een mens nooit alleen als middel, maar altijd ook als doel.', ideaW: ['P2', 'Behandel'], thW: [['P2', 'Immanuel']],
    sterk: ['Heldere grenzen', 'Beschermt rechten en waardigheid'], zwak: ['Regels kunnen botsen', 'Star in grijze gevallen'], zwakW: 'Zwak',
    safe: 'De Grondwet beschermt in artikel 17 de persoonlijke levenssfeer. Mag een camera die zomaar doorbreken?' },
  { id: 'R', name: 'Rechtvaardigheid', theory: 'Rechtvaardigheidstheorie', q: 'Zijn de lasten eerlijk verdeeld?', col: J.navy,
    th: [['John Rawls', 1971, 'Verenigde Staten · A Theory of Justice']],
    years: '1971', idea: 'Kies de regels achter een sluier van onwetendheid: je weet niet welke plek je zelf krijgt.', ideaW: ['R2', 'Kies de regels'], thW: [['R2', 'John']],
    sterk: ['Je ziet wie de lasten draagt', 'Kijkt naar de zwakste positie'], zwak: ['Meerdere definities van eerlijk', 'Die gaan niet allemaal tegelijk'], zwakW: 'Zwak',
    safe: 'In welke wijken hangen de camera’s, en wie krijgt de foute treffers?' },
  { id: 'D', name: 'Deugd', theory: 'Deugdethiek', q: 'Wat zou een goede vakman hier doen?', col: J.gold,
    th: [['Aristoteles', -340, 'Griekenland · Ethica Nicomachea, ca. 340 v.Chr.']],
    years: 'ca. 340 v.Chr.', idea: 'Goed handelen komt uit karakter en praktische wijsheid: eerlijk, zorgvuldig en moedig.', ideaW: ['D2', 'Hij vroeg'], thW: [['D2', 'Aristoteles']],
    sterk: ['Gaat over karakter en cultuur', 'Beroepscodes maken het concreet (ACM, 2018)'], zwak: ['Zonder criteria blijft het vaag', 'Wiens deugden tellen?'], zwakW: 'Zwak',
    safe: 'Wat doet een goede politieleiding hier?' },
  { id: 'Z', name: 'Zorg', theory: 'Zorgethiek', q: 'Wie is afhankelijk, en wie kan zich niet verweren?', col: GOLD2,
    th: [['Carol Gilligan', 1982, 'In a Different Voice'], ['Nel Noddings', 1984, 'Caring'], ['Joan Tronto', 1993, 'Moral Boundaries']],
    years: '1982 – 1993', thW: [['Z2', 'Carol'], ['Z2', 'Nel'], ['Z2', 'Joan']],
    sterk: ['Kwetsbare mensen worden zichtbaar', 'Gevoelig voor context'], zwak: ['Moeilijk op grote schaal', 'Zorg alleen is geen verantwoording'], zwakW: 'Zwak',
    safe: 'Wie kan zich niet verweren als de camera zich vergist?' },
];
const ALLTH = [-340, 1785, 1789, 1863, 1971, 1982, 1984, 1993];

/* ---------- gedeelde bouwstenen ---------- */
// Wisselt tussen inhoud op de momenten van de sleutels.
const Switch = ({ items, style }) => {
  const frame = useCurrentFrame();
  return (
    <div style={{ position: 'absolute', ...style }}>
      {items.map(([k, el], i) => {
        const a = typeof k === 'number' ? k : F(k, -0.2);
        const nk = items[i + 1] && items[i + 1][0];
        const b = nk === undefined ? 1e9 : (typeof nk === 'number' ? nk : F(nk, -0.2));
        if (frame < a - 2 || frame > b + 12) return null;
        const o = interpolate(frame, [a, a + 10, b, b + 10], [0, 1, 1, 0], clamp);
        const y = (1 - interpolate(frame, [a, a + 14], [0, 1], clamp)) * 26;
        return <div key={i} style={{ position: 'absolute', inset: 0, opacity: o, transform: `translateY(${y}px)` }}>{el}</div>;
      })}
    </div>
  );
};
const Panel = ({ children, bg = J.card, style = {} }) => (
  <div style={{ position: 'absolute', inset: 0, background: bg, border: `2px solid ${J.line}`, borderRadius: 22, boxShadow: '0 12px 30px rgba(0,32,96,.07)', overflow: 'hidden', ...style }}>{children}</div>
);
const Kick = ({ children, color = J.blue, style = {} }) => <div style={{ fontFamily: FONT, fontWeight: 700, fontSize: 24, letterSpacing: 2.5, color, textTransform: 'uppercase', ...style }}>{children}</div>;
const Person = ({ x, y, s = 1, col = J.blue }) => (
  <g transform={`translate(${x},${y}) scale(${s})`}><circle cx="0" cy="-34" r="14" fill={col} /><path d="M-20 14 Q-20 -14 0 -16 Q20 -14 20 14 Z" fill={col} /></g>
);

/* ---------- herkomst ---------- */
const TX = (y) => (y < 0 ? 70 : 200 + (y - 1750) / 250 * 520);
const Herkomst = ({ k }) => {
  const frame = useCurrentFrame();
  const d = K[k]; const key = d.thW[0][0];
  const xs = d.th.map(([, y]) => TX(y)); const mx = xs.reduce((a, b) => a + b, 0) / xs.length;
  const pulse = 1 + 0.12 * Math.sin(frame / 6);
  return (
    <Panel>
      <div style={{ position: 'absolute', left: 40, top: 30, right: 40 }}>
        <Kick>Herkomst</Kick>
        <svg width="752" height="120" style={{ marginTop: 10 }}>
          <line x1="20" y1="80" x2="130" y2="80" stroke={J.line} strokeWidth="6" strokeLinecap="round" />
          <line x1="146" y1="92" x2="160" y2="68" stroke={J.slate} strokeWidth="4" /><line x1="160" y1="92" x2="174" y2="68" stroke={J.slate} strokeWidth="4" />
          <line x1="190" y1="80" x2="730" y2="80" stroke={J.line} strokeWidth="6" strokeLinecap="round" />
          {[1800, 1900, 2000].map((y) => <g key={y}><line x1={TX(y)} y1="88" x2={TX(y)} y2="98" stroke={J.slate} strokeWidth="3" /><text x={TX(y)} y="116" textAnchor="middle" fontFamily={FONT} fontSize="20" fill={J.slate}>{y}</text></g>)}
          <text x="70" y="116" textAnchor="middle" fontFamily={FONT} fontSize="20" fill={J.slate}>oudheid</text>
          {ALLTH.map((y) => <circle key={y} cx={TX(y)} cy="80" r="7" fill="#B7C3D4" />)}
          {d.th.map(([, y], i) => { const s = sp(frame, W(...d.thW[i])); return <circle key={y} cx={TX(y)} cy="80" r={13 * s * pulse} fill={d.col} stroke="#fff" strokeWidth="3" />; })}
          <text x={Math.min(640, Math.max(80, mx))} y="44" textAnchor="middle" fontFamily={FONT} fontWeight="700" fontSize="30" fill={J.navy} opacity={fade(frame, W(...d.thW[0]), W(...d.thW[0]) + 12)}>{d.years}</text>
        </svg>
        <div style={{ marginTop: 16 }}>
          {d.th.map(([n, y, w], i) => {
            const s = sp(frame, W(...d.thW[i]));
            return (
              <div key={n} style={{ display: 'flex', alignItems: 'baseline', gap: 16, marginBottom: d.id === 'Z' ? 2 : 10, opacity: s, transform: `translateX(${(1 - s) * 40}px)` }}>
                <div style={{ width: 12, height: 12, borderRadius: 6, background: d.col, flex: 'none', transform: 'translateY(-4px)' }} />
                <T size={d.id === 'Z' ? 30 : 34} weight={700} color={J.navy} style={{ whiteSpace: 'nowrap' }}>{n}</T>
                <T size={d.id === 'Z' ? 24 : 26} color={J.slate}>{y < 0 ? '' : y + ' · '}{w}</T>
              </div>
            );
          })}
        </div>
      </div>
      {d.idea && (
        <div style={{ position: 'absolute', left: 40, right: 40, bottom: 36, opacity: sp(frame, W(...d.ideaW)), background: J.ice, borderLeft: `8px solid ${d.col}`, borderRadius: 14, padding: '22px 28px' }}>
          <T size={34} weight={700} color={J.navy}>{d.idea}</T>
        </div>
      )}
      {d.id === 'Z' && <Tronto />}
    </Panel>
  );
};
const Tronto = () => {
  const frame = useCurrentFrame();
  const steps = [['1', 'Zorg opmerken', 'zorg opmerken'], ['2', 'Verantwoordelijkheid', 'verantwoordelijkheid'], ['3', 'Zorg geven', 'zorg geven'], ['4', 'Nagaan hoe het aankomt', 'nagaan']];
  return (
    <div style={{ position: 'absolute', left: 40, right: 40, bottom: 24 }}>
      <Kick color={J.slate} style={{ fontSize: 22, marginBottom: 8, opacity: fade(frame, W('Z2', 'vier stappen'), W('Z2', 'vier stappen') + 10) }}>Tronto: vier stappen van zorg</Kick>
      <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 12 }}>
        {steps.map(([n, t, w]) => { const s = sp(frame, W('Z2', w)); return (
          <div key={n} style={{ opacity: s, transform: `scale(${0.9 + 0.1 * s})`, background: J.ice, borderRadius: 12, padding: '8px 16px', display: 'flex', gap: 12, alignItems: 'center' }}>
            <div style={{ width: 40, height: 40, borderRadius: 20, background: GOLD2, color: J.navy, fontFamily: FONT, fontWeight: 700, fontSize: 26, display: 'flex', alignItems: 'center', justifyContent: 'center', flex: 'none' }}>{n}</div>
            <T size={25} weight={700} color={J.navy} style={{ whiteSpace: 'nowrap' }}>{t}</T>
          </div>); })}
      </div>
    </div>
  );
};

/* ---------- sterk en zwak, Safe City ---------- */
const SterkZwak = ({ k, keyName }) => {
  const frame = useCurrentFrame();
  const d = K[k]; const zw = W(keyName, d.zwakW);
  const box = (title, items, col, t0, step) => (
    <div style={{ background: J.card, border: `2px solid ${J.line}`, borderLeft: `10px solid ${col}`, borderRadius: 16, padding: '22px 28px', marginBottom: 22 }}>
      <Kick color={col} style={{ marginBottom: 10 }}>{title}</Kick>
      {items.map((t, i) => { const s = sp(frame, t0 + i * step); return <T key={t} size={34} weight={700} color={J.navy} style={{ opacity: s, transform: `translateX(${(1 - s) * 30}px)`, marginBottom: 6 }}>{t}</T>; })}
    </div>
  );
  return (
    <div style={{ position: 'absolute', inset: 0 }}>
      {box('Sterk', d.sterk, J.green, F(keyName, 0.1), 10)}
      {box('Zwak', d.zwak, J.red, zw, 40)}
    </div>
  );
};
const Camera = ({ size = 120 }) => (
  <svg viewBox="0 0 120 120" width={size} height={size}>
    <rect x="18" y="40" width="70" height="40" rx="8" fill="#fff" /><polygon points="88,50 108,40 108,80 88,70" fill="#fff" />
    <circle cx="40" cy="60" r="10" fill={J.navy} /><line x1="53" y1="80" x2="53" y2="106" stroke="#fff" strokeWidth="8" /><line x1="30" y1="106" x2="76" y2="106" stroke="#fff" strokeWidth="8" strokeLinecap="round" />
  </svg>
);
const SafeCard = ({ k }) => (
  <Panel bg={J.navy} style={{ border: 'none' }}>
    <div style={{ position: 'absolute', left: 44, top: 40, right: 44 }}>
      <div style={{ display: 'flex', alignItems: 'center', gap: 20 }}><Camera size={96} /><Kick color={J.gold} style={{ fontSize: 28 }}>Bij Safe City vraagt dit kader</Kick></div>
      <T size={48} weight={700} color={J.onNavy} style={{ marginTop: 34, lineHeight: 1.18 }}>{K[k].safe}</T>
      <T size={24} color={J.onNavyMuted} style={{ marginTop: 30 }}>Stel dat de camera’s gezichten gaan herkennen.</T>
    </div>
  </Panel>
);

/* ---------- illustraties ---------- */
const Box = ({ children }) => <Panel><svg viewBox="0 0 780 560" width="100%" height="100%">{children}</svg></Panel>;
const ScaleIll = () => {
  const frame = useCurrentFrame();
  const ang = interpolate(frame, [F('G1', 1.5), F('G1', 3)], [0, -7], { ...clamp, easing: Easing.inOut(Easing.cubic) }) + Math.sin(frame / 22) * 1.2;
  const ppl = fade(frame, W('G2', 'voor iedereen'), W('G2', 'voor iedereen') + 12);
  const r = (ang * Math.PI) / 180; const L = 230;
  const lx = 390 - L * Math.cos(r), ly = 170 - L * Math.sin(r), rx = 390 + L * Math.cos(r), ry = 170 + L * Math.sin(r);
  const pan = (x, y, col, sym, label) => (<g>
    <line x1={x} y1={y} x2={x - 60} y2={y + 120} stroke={J.slate} strokeWidth="3" /><line x1={x} y1={y} x2={x + 60} y2={y + 120} stroke={J.slate} strokeWidth="3" />
    <path d={`M${x - 80} ${y + 120} Q${x} ${y + 175} ${x + 80} ${y + 120} Z`} fill={J.ice} stroke={J.slate} strokeWidth="3" />
    {[-36, 0, 36].map((dx, i) => <g key={i}><circle cx={x + dx} cy={y + 104 - (i === 1 ? 18 : 0)} r="20" fill={col} /><text x={x + dx} y={y + 113 - (i === 1 ? 18 : 0)} textAnchor="middle" fontFamily={FONT} fontWeight="700" fontSize="28" fill="#fff">{sym}</text></g>)}
    <text x={x} y={y + 210} textAnchor="middle" fontFamily={FONT} fontWeight="700" fontSize="34" fill={J.navy}>{label}</text>
  </g>);
  return (<Box>
    <polygon points="390,170 350,470 430,470" fill={J.navy} /><rect x="300" y="470" width="180" height="22" rx="6" fill={J.navy} />
    <line x1={lx} y1={ly} x2={rx} y2={ry} stroke={J.navy} strokeWidth="12" strokeLinecap="round" /><circle cx="390" cy="170" r="14" fill={J.gold} />
    {pan(lx, ly, J.green, '+', 'baten')}{pan(rx, ry, J.red, '−', 'schade')}
    <g opacity={ppl}>{[90, 140, 640, 690].map((x, i) => <Person key={i} x={x} y={520} s={0.9} col={J.slate} />)}</g>
  </Box>);
};
const DotsIll = () => {
  const frame = useCurrentFrame();
  const red = sp(frame, W('G4', 'vijf procent benadeelt'));
  const avg = sp(frame, W('G4', 'scoort goed'));
  const you = sp(frame, W('G4', 'Tenzij'));
  const bad = [17, 43, 58, 76, 91];
  return (<Box>
    {Array.from({ length: 100 }).map((_, i) => {
      const x = 120 + (i % 20) * 28, y = 150 + Math.floor(i / 20) * 64; const isBad = bad.includes(i);
      return <g key={i}><Person x={x} y={y + 30} s={0.55} col={isBad ? interpolateCol(red, J.blue, J.red) : J.blue} /></g>;
    })}
    <circle cx={120 + (91 % 20) * 28} cy={150 + 4 * 64 + 18} r={34 + 4 * Math.sin(frame / 5)} fill="none" stroke={J.red} strokeWidth="5" opacity={you} />
    <g opacity={you}><rect x={120 + (91 % 20) * 28 + 40} y={150 + 4 * 64 - 70} width="80" height="48" rx="10" fill="#fff" stroke={J.red} strokeWidth="3" /><text x={120 + (91 % 20) * 28 + 80} y={150 + 4 * 64 - 36} textAnchor="middle" fontFamily={FONT} fontWeight="700" fontSize="32" fill={J.red}>jij?</text></g>
    <g opacity={avg}><rect x="120" y="40" width="300" height="58" rx="29" fill={J.blue} /><text x="270" y="79" textAnchor="middle" fontFamily={FONT} fontWeight="700" fontSize="30" fill="#fff">gemiddeld: goed</text></g>
    <text x="120" y="510" fontFamily={FONT} fontWeight="700" fontSize="32" fill={J.blue}>95% geholpen</text>
    <text x="420" y="510" fontFamily={FONT} fontWeight="700" fontSize="32" fill={J.red} opacity={red}>5% benadeeld</text>
  </Box>);
};
const interpolateCol = (p, a, b) => { const h = (s) => [1, 3, 5].map((i) => parseInt(s.slice(i, i + 2), 16)); const [x, y] = [h(a), h(b)]; return `rgb(${x.map((v, i) => Math.round(v + (y[i] - v) * Math.min(1, Math.max(0, p)))).join(',')})`; };
const RiskCard = () => {
  const frame = useCurrentFrame();
  const c = (t, at, col = J.navy) => <div style={{ opacity: sp(frame, at), fontFamily: FONT, fontWeight: 700, fontSize: 72, color: col }}>{t}</div>;
  return (<Panel><div style={{ position: 'absolute', left: 44, top: 40, right: 44 }}>
    <Kick>Bij AI ken je dit al</Kick>
    <T size={44} weight={700} color={J.navy} style={{ marginTop: 10 }}>Het risicoregister</T>
    <div style={{ display: 'flex', gap: 26, alignItems: 'center', marginTop: 50 }}>
      <div style={{ textAlign: 'center' }}>{c('4', F('G3', 2))}<T size={26} color={J.slate}>kans</T></div>{c('×', F('G3', 2.4), J.slate)}
      <div style={{ textAlign: 'center' }}>{c('3', F('G3', 2.8))}<T size={26} color={J.slate}>impact</T></div>{c('=', F('G3', 3.2), J.slate)}
      <div style={{ textAlign: 'center' }}>{c('12', F('G3', 3.6), J.blue)}<T size={26} color={J.slate}>risico</T></div>
    </div>
    <div style={{ marginTop: 50, opacity: sp(frame, W('G3', 'gevolgenberekening')), background: J.ice, borderRadius: 14, padding: '20px 26px' }}><T size={34} weight={700} color={J.navy}>Dat is een gevolgenberekening.</T></div>
  </div></Panel>);
};
const BarrierIll = () => {
  const frame = useCurrentFrame();
  const a = interpolate(frame, [F('P1', 1.2), F('P1', 2.4)], [-80, 0], { ...clamp, easing: Easing.out(Easing.back(1.4)) });
  const ook = fade(frame, W('P1', 'ook niet'), W('P1', 'ook niet') + 12);
  return (<Box>
    <line x1="40" y1="440" x2="740" y2="440" stroke={J.line} strokeWidth="8" />
    <rect x="150" y="230" width="34" height="210" rx="6" fill={J.navy} />
    <g transform={`rotate(${a} 167 250)`}>
      <rect x="167" y="236" width="440" height="30" rx="8" fill="#fff" stroke={J.red} strokeWidth="4" />
      {[0, 1, 2, 3, 4].map((i) => <rect key={i} x={190 + i * 84} y="238" width="40" height="26" fill={J.red} />)}
    </g>
    <g transform="translate(360,90)"><rect x="-110" y="0" width="220" height="80" rx="12" fill={J.navy} /><text x="0" y="54" textAnchor="middle" fontFamily={FONT} fontWeight="700" fontSize="44" fill="#fff">GRENS</text></g>
    <g opacity={ook}>
      {[0, 1, 2].map((i) => <ellipse key={i} cx="640" cy={420 - i * 18} rx="48" ry="14" fill={J.gold} stroke={J.navy} strokeWidth="3" />)}
      <text x="640" y="490" textAnchor="middle" fontFamily={FONT} fontWeight="700" fontSize="30" fill={J.navy}>veel opbrengst</text>
      <text x="390" y="520" textAnchor="middle" fontFamily={FONT} fontWeight="700" fontSize="34" fill={J.red}>ook dan niet</text>
    </g>
  </Box>);
};
const MeansEnd = () => {
  const frame = useCurrentFrame();
  const a = sp(frame, W('P2', 'nooit alleen')); const b = sp(frame, W('P2', 'altijd ook'));
  return (<Box>
    <Person x={390} y={300} s={3} col={J.dblue} />
    <g opacity={a}><rect x="40" y="380" width="300" height="80" rx="14" fill="#FBE9E7" stroke={J.red} strokeWidth="3" /><text x="190" y="432" textAnchor="middle" fontFamily={FONT} fontWeight="700" fontSize="32" fill={J.red}>alleen een middel ✗</text></g>
    <g opacity={b}><rect x="440" y="380" width="300" height="80" rx="14" fill="#E2F1E8" stroke={J.green} strokeWidth="3" /><text x="590" y="432" textAnchor="middle" fontFamily={FONT} fontWeight="700" fontSize="32" fill={J.green}>ook een doel ✓</text></g>
    <text x="390" y="80" textAnchor="middle" fontFamily={FONT} fontWeight="700" fontSize="34" fill={J.navy}>Een mens is geen datapunt</text>
  </Box>);
};
const Bub = ({ at, children, me = false }) => {
  const frame = useCurrentFrame(); const s = sp(frame, at, { damping: 16, stiffness: 140 });
  return (<div style={{ display: 'flex', justifyContent: me ? 'flex-end' : 'flex-start', marginTop: 14, opacity: s, transform: `translateY(${(1 - s) * 16}px)` }}>
    <div style={{ maxWidth: 400, background: me ? J.dblue : J.ice, color: me ? '#fff' : J.ink, borderRadius: me ? '20px 20px 6px 20px' : '20px 20px 20px 6px', padding: '14px 20px', fontFamily: FONT, fontSize: 28, lineHeight: 1.3 }}>{children}</div>
  </div>);
};
const PhoneFrame = ({ title, sub, children, left = 170, top = 30, h = 500 }) => (
  <div style={{ position: 'absolute', left, top, width: 440, height: h, borderRadius: 44, background: J.navy, padding: 14 }}>
    <div style={{ width: '100%', height: '100%', borderRadius: 32, background: '#fff', overflow: 'hidden' }}>
      <div style={{ background: J.ice, padding: '20px 22px 12px', borderBottom: `2px solid ${J.line}` }}><T size={28} weight={700} color={J.navy}>{title}</T><T size={20} color={J.slate}>{sub}</T></div>
      <div style={{ padding: '4px 18px' }}>{children}</div>
    </div>
  </div>
);
const ChatIll = () => {
  const frame = useCurrentFrame(); const st = sp(frame, W('P3', 'fout'));
  return (<Panel>
    <PhoneFrame title="ShopBot" sub="verkoopassistent">
      <Bub at={F('P3', 0.3)}>Nog maar 1 over in jouw maat!</Bub>
      <Bub at={F('P3', 1.4)}>37 mensen kijken nu mee. Beslis binnen 2 minuten!</Bub>
      <Bub at={F('P3', 2.6)} me>Oké, dan koop ik hem maar…</Bub>
    </PhoneFrame>
    <div style={{ position: 'absolute', left: 20, top: 40, opacity: sp(frame, W('P3', 'omzet')) }}><T size={30} weight={700} color={J.green}>omzet ↑</T></div>
    <div style={{ position: 'absolute', left: 430, top: 380, opacity: st, transform: `rotate(-12deg) scale(${2 - st})`, border: `6px solid ${J.red}`, borderRadius: 12, padding: '6px 18px', background: 'rgba(255,255,255,.9)' }}><T size={44} weight={700} color={J.red}>MANIPULATIE</T></div>
  </Panel>);
};
const ClashIll = () => {
  const frame = useCurrentFrame(); const t0 = W('P4', 'regels kunnen botsen');
  const m = interpolate(frame, [t0, t0 + 18], [0, 1], { ...clamp, easing: Easing.out(Easing.cubic) });
  const bolt = fade(frame, t0 + 16, t0 + 22) * (0.7 + 0.3 * Math.sin(frame / 2));
  return (<Box>
    <g transform={`translate(${-120 + 150 * m},0)`}><rect x="40" y="200" width="300" height="140" rx="18" fill={J.dblue} /><text x="190" y="262" textAnchor="middle" fontFamily={FONT} fontWeight="700" fontSize="32" fill="#fff">Recht op</text><text x="190" y="302" textAnchor="middle" fontFamily={FONT} fontWeight="700" fontSize="32" fill="#fff">privacy</text></g>
    <g transform={`translate(${120 - 150 * m},0)`}><rect x="440" y="200" width="300" height="140" rx="18" fill={J.blue} /><text x="590" y="262" textAnchor="middle" fontFamily={FONT} fontWeight="700" fontSize="32" fill="#fff">Plicht: burgers</text><text x="590" y="302" textAnchor="middle" fontFamily={FONT} fontWeight="700" fontSize="32" fill="#fff">beschermen</text></g>
    <polygon points="400,150 370,260 400,255 375,380 430,240 400,245 425,150" fill={J.gold} opacity={bolt} />
    <text x="390" y="470" textAnchor="middle" fontFamily={FONT} fontWeight="700" fontSize="38" fill={J.red} opacity={bolt > 0 ? 1 : 0}>regels kunnen botsen</text>
  </Box>);
};
const PieIll = () => {
  const frame = useCurrentFrame();
  const sl = [[0, 110], [110, 200], [200, 280], [280, 345], [345, 360]];
  const arc = (a0, a1, r = 170, cx = 390, cy = 270) => { const p = (a) => [cx + r * Math.sin(a * Math.PI / 180), cy - r * Math.cos(a * Math.PI / 180)]; const [x0, y0] = p(a0), [x1, y1] = p(a1); return `M${cx} ${cy} L${x0} ${y0} A${r} ${r} 0 ${a1 - a0 > 180 ? 1 : 0} 1 ${x1} ${y1} Z`; };
  const q = fade(frame, W('R1', 'eerlijk'), W('R1', 'eerlijk') + 12);
  return (<Box>
    {sl.map(([a0, a1], i) => { const s = sp(frame, F('R1', 0.3 + i * 0.3)); const mid = ((a0 + a1) / 2) * Math.PI / 180; const off = i === 4 ? 28 * q : 6;
      return <path key={i} d={arc(a0, a1)} fill={[J.blue, J.dblue, J.navy, '#6C9BCB', J.gold][i]} stroke="#fff" strokeWidth="5" opacity={s} transform={`translate(${off * Math.sin(mid)},${-off * Math.cos(mid)})`} />; })}
    <text x="390" y="520" textAnchor="middle" fontFamily={FONT} fontWeight="700" fontSize="36" fill={J.navy} opacity={q}>Eerlijk verdeeld?</text>
  </Box>);
};
const VeilIll = ({ choice = false }) => {
  const frame = useCurrentFrame();
  const v = choice ? 1 : interpolate(frame, [W('R2', 'alsof'), W('R2', 'alsof') + 24], [0, 1], { ...clamp, easing: Easing.out(Easing.cubic) });
  const qm = choice ? 1 : fade(frame, W('R2', 'sluier'), W('R2', 'sluier') + 10);
  const flip = Math.floor(frame / 24) % 2;
  return (<Box>
    <Person x={390} y={300} s={3} col={J.navy} />
    <g opacity={0.82}><path d={`M200 40 L580 40 L580 ${40 + 380 * v} Q490 ${20 + 400 * v} 390 ${40 + 380 * v} Q290 ${20 + 400 * v} 200 ${40 + 380 * v} Z`} fill={J.ice} stroke={J.line} strokeWidth="3" />
      {[260, 330, 450, 520].map((x) => <line key={x} x1={x} y1="44" x2={x} y2={40 + 360 * v} stroke="#C9D6E8" strokeWidth="4" />)}</g>
    <text x="390" y="250" textAnchor="middle" fontFamily={FONT} fontWeight="700" fontSize="130" fill={J.blue} opacity={qm}>?</text>
    {!choice && <text x="390" y="480" textAnchor="middle" fontFamily={FONT} fontWeight="700" fontSize="34" fill={J.navy} opacity={qm}>de sluier van onwetendheid</text>}
    {choice && <g>
      <rect x="40" y="500" width="700" height="0" />
      {[['kust', 118], ['binnenland', 662]].map(([t, x], i) => <g key={t}><rect x={x - 100} y="300" width="200" height="64" rx="32" fill={flip === i ? J.blue : '#fff'} stroke={J.blue} strokeWidth="3" /><text x={x} y="342" textAnchor="middle" fontFamily={FONT} fontWeight="700" fontSize="30" fill={flip === i ? '#fff' : J.blue}>{t}</text></g>)}
      <text x="390" y="530" textAnchor="middle" fontFamily={FONT} fontWeight="700" fontSize="32" fill={J.navy}>Accepteer je het model?</text>
      <rect x="250" y="452" width="280" height="50" rx="12" fill={J.navy} /><text x="390" y="486" textAnchor="middle" fontFamily={FONT} fontWeight="700" fontSize="28" fill="#fff">Suribank · kredietmodel</text>
    </g>}
  </Box>);
};
const RawlsRule = () => {
  const frame = useCurrentFrame();
  const bars = [['A', 60, 70], ['B', 30, 45]];
  return (<Panel><div style={{ position: 'absolute', left: 44, top: 40, right: 44 }}>
    <Kick>Rawls’ toets</Kick>
    <T size={44} weight={700} color={J.navy} style={{ marginTop: 10 }}>Ongelijkheid mag alleen als de zwakste er beter van wordt.</T>
    <svg width="700" height="230" style={{ marginTop: 30 }}>
      {bars.map(([n, v0, v1], i) => { const s = interpolate(frame, [F('R3', 1.2), F('R3', 3)], [0, 1], clamp); const v = v0 + (v1 - v0) * s; return (
        <g key={n}><text x="0" y={60 + i * 100} fontFamily={FONT} fontWeight="700" fontSize="28" fill={J.slate}>{i ? 'zwakste' : 'sterkste'}</text>
          <rect x="130" y={30 + i * 100} width={v * 7} height="44" rx="8" fill={i ? J.green : J.blue} /><text x={140 + v * 7} y={62 + i * 100} fontFamily={FONT} fontWeight="700" fontSize="28" fill={J.navy}>{i && s > 0.9 ? '↑ beter' : ''}</text></g>); })}
    </svg>
  </div></Panel>);
};
const StarDevIll = () => {
  const frame = useCurrentFrame(); const g = 0.8 + 0.2 * Math.sin(frame / 8);
  const words = [['eerlijk', 150, 150], ['zorgvuldig', 630, 150], ['moedig', 390, 70]];
  return (<Box>
    <g transform={`translate(390,200) scale(${g})`}><polygon points="0,-70 18,-22 70,-22 28,8 44,60 0,30 -44,60 -28,8 -70,-22 -18,-22" fill={J.gold} /></g>
    <Person x={390} y={430} s={2.4} col={J.navy} />
    <rect x="300" y="440" width="180" height="90" rx="8" fill={J.slate} /><rect x="280" y="528" width="220" height="14" rx="4" fill={J.navy} />
    {words.map(([w, x, y], i) => <text key={w} x={x} y={y} textAnchor="middle" fontFamily={FONT} fontWeight="700" fontSize="36" fill={J.dblue} opacity={fade(frame, F('D1', 2 + i * 0.8), F('D1', 2.4 + i * 0.8))}>{w}</text>)}
  </Box>);
};
const LaptopIll = () => {
  const frame = useCurrentFrame(); const m = sp(frame, W('D3', 'meldt')); const lv = sp(frame, W('D3', 'livegang'));
  return (<Panel><div style={{ position: 'absolute', left: 40, top: 34, right: 40 }}>
    <div style={{ background: J.navy, borderRadius: 18, padding: 14 }}>
      <div style={{ background: '#fff', borderRadius: 10, padding: '18px 22px' }}>
        <T size={24} weight={700} color={J.slate}>TESTRAPPORT · goed voorspeld per groep</T>
        {[['Groep A', 92, J.blue], ['Groep B', 71, J.red]].map(([n, v, c], i) => { const s = sp(frame, F('D3', 0.4 + i * 0.4)); return (
          <div key={n} style={{ display: 'flex', alignItems: 'center', gap: 14, marginTop: 14 }}><T size={26} style={{ width: 110 }}>{n}</T>
            <div style={{ height: 34, width: v * 5 * s, background: c, borderRadius: 6 }} /><T size={26} weight={700} color={c}>{v}%</T></div>); })}
        <div style={{ marginTop: 16, background: '#FBE9E7', borderRadius: 10, padding: '10px 16px', opacity: sp(frame, F('D3', 1.4)) }}><T size={26} weight={700} color={J.red}>⚠ Model werkt slechter voor groep B</T></div>
      </div>
    </div>
    <div style={{ display: 'flex', gap: 18, marginTop: 22, alignItems: 'center' }}>
      <div style={{ opacity: m, background: '#E2F1E8', border: `2px solid ${J.green}`, borderRadius: 999, padding: '10px 22px' }}><T size={28} weight={700} color={J.green}>Melding gedaan ✓</T></div>
      <div style={{ background: J.ice, borderRadius: 999, padding: '10px 22px', display: 'flex', gap: 10 }}><T size={28} color={J.navy}>Livegang:</T><T size={28} weight={700} color={lv > 0.5 ? J.red : J.navy}>{lv > 0.5 ? 'uitgesteld' : 'gepland'}</T></div>
    </div>
  </div></Panel>);
};
const CareIll = () => {
  const frame = useCurrentFrame();
  const others = [[150, 150], [630, 150], [150, 420], [630, 420]];
  const ln = fade(frame, W('Z1', 'afhankelijk'), W('Z1', 'afhankelijk') + 14);
  return (<Box>
    {others.map(([x, y], i) => <line key={i} x1="390" y1="270" x2={x} y2={y - 20} stroke={J.line} strokeWidth="5" strokeDasharray="10 10" opacity={ln} />)}
    {others.map(([x, y], i) => <Person key={i} x={x} y={y} s={1.3} col={J.slate} />)}
    <Person x={390} y={300} s={1.8} col={GOLD2} />
    <path d="M280 340 Q300 400 390 400 Q480 400 500 340" fill="none" stroke={J.navy} strokeWidth="14" strokeLinecap="round" opacity={sp(frame, F('Z1', 0.6))} />
    <text x="390" y="520" textAnchor="middle" fontFamily={FONT} fontWeight="700" fontSize="34" fill={J.navy} opacity={fade(frame, W('Z1', 'wie kan'), W('Z1', 'wie kan') + 12)}>Wie kan zich niet verweren?</text>
  </Box>);
};
const RejectIll = () => {
  const frame = useCurrentFrame();
  return (<Panel>
    <PhoneFrame title="Suribank" sub="berichten" left={40} top={30}>
      <Bub at={F('Z3', 0.4)}>Uw aanvraag is afgewezen.</Bub>
      <div style={{ marginTop: 22, opacity: sp(frame, W('Z3', 'zonder uitleg')) }}><T size={28} color={J.slate}>Uitleg: <b style={{ color: J.red }}>—</b></T></div>
      <div style={{ marginTop: 10, opacity: sp(frame, W('Z3', 'niemand')) }}><T size={28} color={J.slate}>Bellen: <b style={{ color: J.red }}>—</b></T></div>
    </PhoneFrame>
    <svg viewBox="0 0 280 400" style={{ position: 'absolute', left: 500, top: 90, width: 250, height: 360 }}><Person x={140} y={250} s={2.6} col={GOLD2} /><text x="140" y="110" textAnchor="middle" fontFamily={FONT} fontWeight="700" fontSize="80" fill={J.red} opacity={sp(frame, W('Z3', 'niemand'))}>?</text></svg>
    <div style={{ position: 'absolute', left: 500, top: 450, width: 250, textAlign: 'center' }}><T size={26} weight={700} color={J.navy}>aanvrager · binnenland</T></div>
  </Panel>);
};

/* ---------- één kader-scène ---------- */
const KaderScene = ({ k, left, right }) => {
  const frame = useCurrentFrame(); const d = K[k]; const k0 = d.id + '1';
  return (
    <AbsoluteFill style={{ background: J.bg }}>
      <Pop at={F(k0, -0.2)} style={{ left: 128, top: 60 }}><IconDot k={k} col={d.col} size={110} icon={66} /></Pop>
      <Pop at={F(k0, 0)} style={{ left: 268, top: 62, width: 1250 }}>
        <Kick color={J.slate}>Kader {k + 1} van 5 · {d.name} · {d.theory}</Kick>
        <div style={{ fontFamily: FONT, fontWeight: 700, fontSize: 58, lineHeight: 1.05, color: J.navy, marginTop: 6 }}>{d.q}</div>
      </Pop>
      <div style={{ position: 'absolute', left: 1580, top: 82, display: 'flex', gap: 12 }}>
        {K.map((x, i) => <div key={i} style={{ width: 34, height: 34, borderRadius: 17, background: i === k ? x.col : i < k ? '#B7C3D4' : J.line }} />)}
      </div>
      <Switch items={left} style={{ left: 128, top: 240, width: 780, height: 590 }} />
      <Switch items={right} style={{ left: 960, top: 240, width: 832, height: 590 }} />
    </AbsoluteFill>
  );
};

/* ---------- intro ---------- */
const Intro = () => {
  const frame = useCurrentFrame(); const s = sp(frame, 4);
  return (
    <AbsoluteFill style={{ background: `radial-gradient(1300px 900px at 78% 25%, #1A3D86 0%, ${J.navy} 62%)` }}>
      <div style={{ position: 'absolute', left: 140, top: 250, opacity: s }}><Kick color={J.gold} style={{ fontSize: 30 }}>Kennisclip 5b · AI &amp; Ethics · blok 1</Kick></div>
      <div style={{ position: 'absolute', left: 140, top: 300, fontFamily: FONT, fontWeight: 700, fontSize: 140, lineHeight: 1.02, color: '#fff', opacity: s, transform: `translateY(${(1 - s) * 40}px)` }}>Vijf ethische kaders</div>
      <div style={{ position: 'absolute', left: 140, top: 470, fontFamily: FONT, fontSize: 40, color: J.onNavyMuted, opacity: fade(frame, 18, 34) }}>gevolgen · plichten · rechtvaardigheid · deugd · zorg</div>
      <div style={{ position: 'absolute', left: 140, top: 600, display: 'flex', gap: 34 }}>
        {K.map((d, i) => { const a = sp(frame, 24 + i * 7, { damping: 14 }); return <div key={i} style={{ opacity: a, transform: `translateY(${(1 - a) * 60}px)` }}><IconDot k={i} col={d.col} size={130} icon={78} ring="rgba(255,255,255,.55)" /></div>; })}
      </div>
    </AbsoluteFill>
  );
};

/* ---------- Safe City-straat ---------- */
const Street = () => {
  const frame = useCurrentFrame();
  const stop = F('E2', 0);
  const tt = Math.min(frame, stop);
  const beamX = 900 + 450 * Math.sin(frame / 40);
  const walkers = [[180, 1], [460, 1], [740, 1], [1020, 1], [1300, 1]];
  const opinions = ['Ja', 'Nee', 'Onder voorwaarden', 'Eerst een wet', 'Wie controleert?'];
  const cols = [J.blue, J.dblue, J.navy, GOLD2, J.slate];
  return (
    <AbsoluteFill style={{ background: `linear-gradient(${J.ice}, #fff 70%)` }}>
      <svg width="1920" height="1080" style={{ position: 'absolute', inset: 0 }}>
        {[[140, 500, 220], [380, 470, 180], [600, 520, 260], [900, 460, 200], [1140, 500, 240], [1420, 480, 200], [1660, 510, 220]].map(([x, y, w], i) => (
          <g key={i}><rect x={x} y={y} width={w} height={790 - y} fill="#fff" stroke={J.navy} strokeWidth="4" /><polygon points={`${x - 14},${y} ${x + w / 2},${y - 80} ${x + w + 14},${y}`} fill={i % 2 ? J.dblue : J.navy} />
            {[0, 1].map((r) => [0, 1, 2].map((c) => <rect key={`${r}${c}`} x={x + 24 + c * (w - 48) / 3} y={y + 40 + r * 110} width={(w - 48) / 3 - 18} height="64" fill={J.ice} stroke={J.navy} strokeWidth="2" />))}</g>))}
        <rect x="0" y="790" width="1920" height="290" fill="#DCE3EC" /><rect x="0" y="790" width="1920" height="10" fill={J.slate} />
        <polygon points={`1700,330 ${beamX - 200},860 ${beamX + 200},860`} fill={J.blue} opacity={0.16 * fade(frame, F('E1', 0.8), F('E1', 1.6))} />
        <rect x="1730" y="320" width="20" height="480" fill={J.navy} /><g transform="translate(1650,290)"><rect x="0" y="0" width="110" height="56" rx="10" fill={J.navy} /><circle cx="24" cy="28" r="14" fill={J.blue} /></g>
        {walkers.map(([x0, v], i) => {
          const x = x0 + tt * v * 0.5; const near = frame < stop && Math.abs(x - beamX) < 170 && frame > F('E1', 2);
          return (<g key={i}><Person x={x} y={830} s={2.2} col={cols[i]} />
            {near && <g><rect x={x - 40} y={720} width="80" height="80" fill="none" stroke={J.red} strokeWidth="4" /><text x={x} y={710} textAnchor="middle" fontFamily={FONT} fontWeight="700" fontSize="24" fill={J.red}>gezicht herkend</text></g>}</g>);
        })}
      </svg>
      {walkers.map(([x0, v], i) => { const x = x0 + stop * v * 0.5; const s = sp(frame, W('E2', 'vijf antwoorden', i * 0.35)); return (
        <div key={i} style={{ position: 'absolute', left: x - 135, top: 560, width: 270, display: 'flex', justifyContent: 'center', opacity: s, transform: `translateY(${(1 - s) * 30}px) scale(${0.8 + 0.2 * s})` }}>
          <div style={{ background: '#fff', border: `3px solid ${cols[i]}`, borderRadius: 20, padding: '12px 18px', fontFamily: FONT, fontWeight: 700, fontSize: 30, color: J.navy, textAlign: 'center', whiteSpace: 'nowrap', boxShadow: '0 8px 18px rgba(0,32,96,.15)' }}>{opinions[i]}</div>
        </div>); })}
      <div style={{ position: 'absolute', left: 128, top: 60, width: 1500 }}>
        <Pop at={F('E1', -0.2)} style={{ position: 'relative' }}><Kick>Stel dat · Surinaamse casus</Kick>
          <div style={{ fontFamily: FONT, fontWeight: 700, fontSize: 64, color: J.navy, marginTop: 6 }}>Safe City met gezichtsherkenning?</div></Pop>
        <div style={{ position: 'relative', marginTop: 12, opacity: fade(frame, F('E2', 0), F('E2', 0.4)) }}><T size={44} weight={700} color={J.blue}>Goed of fout?</T></div>
      </div>
    </AbsoluteFill>
  );
};

/* ---------- waarom kaders ---------- */
const Why = () => {
  const frame = useCurrentFrame();
  const three = [['Structuur', 'Je weegt stap voor stap, niet op gevoel.', 'structuur'], ['Consequent', 'Vergelijkbare gevallen, hetzelfde oordeel.', 'consequent'], ['Onderbouwd', 'Je kunt uitleggen waarom.', 'uitleggen']];
  return (
    <AbsoluteFill style={{ background: J.bg }}>
      <JTitle at={F('E3', -0.2)} kicker="Ethiek is geen mening">Wat een ethisch kader je geeft</JTitle>
      <Switch style={{ left: 128, top: 270, width: 1664, height: 560 }} items={[
        ['E3', <div style={{ display: 'flex', gap: 32 }}>{three.map(([t, s, w], i) => { const a = sp(frame, W('E3', w)); return (
          <div key={t} style={{ flex: 1, opacity: a, transform: `translateY(${(1 - a) * 40}px)`, background: J.card, border: `2px solid ${J.line}`, borderTop: `10px solid ${J.blue}`, borderRadius: 20, padding: '36px 36px', minHeight: 300 }}>
            <div style={{ fontFamily: FONT, fontWeight: 700, fontSize: 80, color: J.blue, lineHeight: 1 }}>{i + 1}</div>
            <T size={48} weight={700} color={J.navy} style={{ marginTop: 16 }}>{t}</T><T size={34} color={J.ink} style={{ marginTop: 10 }}>{s}</T>
          </div>); })}</div>],
        ['E4', <div style={{ display: 'flex', gap: 22 }}>{K.map((d, i) => { const a = sp(frame, F('E4', 0.3 + i * 0.35)); return (
          <div key={d.id} style={{ flex: 1, opacity: a, transform: `translateY(${(1 - a) * 40}px)`, background: J.card, border: `2px solid ${J.line}`, borderRadius: 20, padding: '28px 26px', minHeight: 440, display: 'flex', flexDirection: 'column', gap: 18 }}>
            <IconDot k={i} col={d.col} size={100} icon={60} /><T size={40} weight={700} color={J.navy}>{d.name}</T><T size={30} color={J.ink}>{d.q}</T>
          </div>); })}</div>],
      ]} />
    </AbsoluteFill>
  );
};

/* ---------- tegenspraak ---------- */
const Conflict = () => {
  const frame = useCurrentFrame();
  const rows = [
    [0, 'Ja', J.green, 'Het levert veiligheid op.', ['T1', 'Gevolgen'], ['T1', 'ja,']],
    [1, 'Nee', J.red, 'Niet zonder een privacywet.', ['T1', 'Plichten'], ['T1', 'niet zonder']],
    [2, 'Onder voorwaarden', J.blue, 'Alleen als de fouten eerlijk verdeeld zijn.', ['T2', 'Rechtvaardigheid'], ['T2', 'alleen als']],
    [3, 'Vraag', J.slate, 'Wat doet dit met het vertrouwen in de politie?', ['T2', 'Deugd en zorg'], ['T2', 'vertrouwen']],
    [4, 'Vraag', J.slate, 'Wat doet dit met het vertrouwen in de politie?', ['T2', 'Deugd en zorg'], ['T2', 'vertrouwen', 0.3]],
  ];
  return (
    <AbsoluteFill style={{ background: J.bg }}>
      <JTitle at={F('T1', -0.2)} kicker="Safe City door vijf kaders">De kaders spreken elkaar tegen</JTitle>
      <div style={{ position: 'absolute', left: 128, top: 240, width: 1664 }}>
        {rows.map(([k, v, c, arg, kw, vw]) => { const a = sp(frame, F('T1', 0.2 + k * 0.15)); const on = sp(frame, W(...kw)); const vv = sp(frame, W(...vw));
          return (
            <div key={k} style={{ display: 'flex', alignItems: 'center', gap: 26, height: 92, marginBottom: 10, background: J.card, border: `2px solid ${on > 0.5 ? K[k].col : J.line}`, borderRadius: 16, padding: '0 24px', opacity: 0.35 + 0.65 * Math.max(on, 0.0) * a + 0.0 }}>
              <IconDot k={k} col={K[k].col} size={64} icon={40} />
              <T size={36} weight={700} color={J.navy} style={{ width: 330 }}>{K[k].name}</T>
              <div style={{ width: 340, opacity: vv, transform: `scale(${0.8 + 0.2 * vv})` }}><span style={{ display: 'inline-block', background: c, color: '#fff', fontFamily: FONT, fontWeight: 700, fontSize: 30, padding: '8px 22px', borderRadius: 999 }}>{v}</span></div>
              <T size={32} color={J.ink} style={{ opacity: vv }}>{arg}</T>
            </div>); })}
      </div>
      <JBanner at={F('T3', 0.2)} top={790} size={40}>Geen kader heeft alle antwoorden. Gebruik ze samen, en zeg eerlijk wat je opgeeft.</JBanner>
    </AbsoluteFill>
  );
};

/* ---------- van vijf kaders naar vier lenzen ---------- */
const Canvas = () => {
  const frame = useCurrentFrame();
  const m = interpolate(frame, [W('K1', 'deugd en zorg'), W('K1', 'deugd en zorg') + 30], [0, 1], { ...clamp, easing: Easing.inOut(Easing.cubic) });
  const lbl = fade(frame, W('K1', 'professionele'), W('K1', 'professionele') + 10);
  const cv = sp(frame, W('K1', 'Noem'));
  const type = (s, off) => s.slice(0, Math.max(0, Math.floor((frame - W('K1', 'Noem', off)) / 2)));
  const x = (i) => (i < 3 ? 128 + i * 340 : 1148 + (i - 3) * 330 * (1 - m));
  return (
    <AbsoluteFill style={{ background: J.bg }}>
      <JTitle at={F('K1', -0.2)} kicker="In het dilemma-canvas (K5)">Vijf kaders, vier lenzen</JTitle>
      {K.map((d, i) => (
        <div key={d.id} style={{ position: 'absolute', left: x(i), top: 250, width: 310, height: 250, background: J.card, border: `2px solid ${J.line}`, borderTop: `10px solid ${d.col}`, borderRadius: 18, padding: 24, opacity: i === 4 ? 1 - m * 0.9 : 1 }}>
          <IconDot k={i} col={d.col} size={72} icon={44} /><T size={36} weight={700} color={J.navy} style={{ marginTop: 14 }}>{d.name}</T><T size={26} color={J.slate}>{d.theory}</T>
        </div>
      ))}
      <div style={{ position: 'absolute', left: 1148, top: 520, width: 640, opacity: lbl, background: J.navy, borderRadius: 14, padding: '14px 22px' }}><T size={32} weight={700} color="#fff">Lens 4 · Professionele integriteit</T><T size={24} color={J.onNavyMuted}>deugdethiek, zorgethiek en beroepscodes</T></div>
      {[0, 1, 2].map((i) => <div key={i} style={{ position: 'absolute', left: 128 + i * 340, top: 520, width: 310, opacity: lbl }}><T size={28} weight={700} color={J.slate}>Lens {i + 1}</T></div>)}
      <div style={{ position: 'absolute', left: 128, top: 650, width: 1100, opacity: cv, transform: `translateY(${(1 - cv) * 30}px)`, background: J.card, border: `2px solid ${J.line}`, borderRadius: 16, padding: '18px 28px' }}>
        <Kick color={J.blue} style={{ fontSize: 22 }}>K5 dilemma-canvas</Kick>
        <T size={36} color={J.ink} style={{ marginTop: 6 }}>Lens: <b style={{ color: J.navy }}>{type('Rechtvaardigheid', 0.4)}</b>  ·  Theorie: <b style={{ color: J.navy }}>{type('Rawls', 1.6)}</b></T>
      </div>
    </AbsoluteFill>
  );
};

/* ---------- samenvatting en opdracht ---------- */
const Summary = () => {
  const frame = useCurrentFrame();
  const w = ['Gevolgen', 'Plichten', 'Rechtvaardigheid', 'Deugd', 'zorg vraagt'];
  return (
    <AbsoluteFill style={{ background: J.bg }}>
      <JTitle at={F('S1', -0.2)}>Samengevat</JTitle>
      {K.map((d, i) => { const a = sp(frame, W('S1', w[i])); return (
        <div key={d.id} style={{ position: 'absolute', left: 128, top: 200 + i * 128, width: 1664, height: 110, display: 'flex', alignItems: 'center', gap: 28, background: J.card, border: `2px solid ${J.line}`, borderRadius: 18, padding: '0 26px', opacity: a, transform: `translateX(${(1 - a) * -60}px)` }}>
          <IconDot k={i} col={d.col} size={78} icon={48} /><T size={40} weight={700} color={J.navy} style={{ width: 380 }}>{d.name}</T><T size={36} color={J.ink}>{d.q}</T>
        </div>); })}
    </AbsoluteFill>
  );
};
const NowYou = () => {
  const frame = useCurrentFrame();
  const st = [['Kies één dilemma uit jullie eigen oplossing.', 'Kies'], ['Welk kader gebruik je als eerste? Welk kader spreekt het het meest tegen?', 'Welk kader'], ['Schrijf het op voor je dilemma-canvas (K5).', 'Schrijf']];
  return (
    <AbsoluteFill style={{ background: J.bg }}>
      <JTitle at={F('N1', -0.2)} kicker="Opdracht" size={68}>Nu jij</JTitle>
      {st.map(([t, w], i) => { const a = sp(frame, W('N1', w)); return (
        <div key={i} style={{ position: 'absolute', left: 128, top: 250 + i * 170, width: 1664, opacity: a, transform: `translateY(${(1 - a) * 40}px)`, background: J.card, border: `2px solid ${J.line}`, borderRadius: 20, padding: '28px 38px', display: 'flex', gap: 30, alignItems: 'center' }}>
          <div style={{ fontFamily: FONT, fontWeight: 700, fontSize: 64, color: J.blue, width: 50 }}>{i + 1}</div><T size={42} color={J.navy} weight={700}>{t}</T>
        </div>); })}
    </AbsoluteFill>
  );
};

export const Clip5b = () => (
  <Root scenes={[
    ['E0', <Intro />], ['E1', <Street />], ['E3', <Why />],
    ['G1', <KaderScene k={0} left={[['G1', <ScaleIll />], ['G4', <DotsIll />]]} right={[['G2', <Herkomst k={0} />], ['G3', <RiskCard />], ['G5', <SterkZwak k={0} keyName="G5" />], ['G6', <SafeCard k={0} />]]} />],
    ['P1', <KaderScene k={1} left={[['P1', <BarrierIll />], ['P2', <MeansEnd />], ['P3', <ChatIll />], ['P4', <ClashIll />]]} right={[['P2', <Herkomst k={1} />], ['P4', <SterkZwak k={1} keyName="P4" />], ['P5', <SafeCard k={1} />]]} />],
    ['R1', <KaderScene k={2} left={[['R1', <PieIll />], ['R2', <VeilIll />], ['R4', <VeilIll choice />]]} right={[['R2', <Herkomst k={2} />], ['R3', <RawlsRule />], ['R5', <SterkZwak k={2} keyName="R5" />], ['R6', <SafeCard k={2} />]]} />],
    ['Q1', <QuizN n={1} q="Q1" a="Q1b" question="“Het model helpt duizend klanten sneller, dus een paar foute afwijzingen nemen we voor lief.” Welk kader is dat?" options={['A. Gevolgen', 'B. Plichten', 'C. Rechtvaardigheid']} good={0} note={<>A, gevolgen: <span style={{ color: J.gold }}>baten tegen schade</span></>} />],
    ['D1', <KaderScene k={3} left={[['D1', <StarDevIll />], ['D3', <LaptopIll />]]} right={[['D2', <Herkomst k={3} />], ['D4', <SterkZwak k={3} keyName="D4" />], ['D5', <SafeCard k={3} />]]} />],
    ['Z1', <KaderScene k={4} left={[['Z1', <CareIll />], ['Z3', <RejectIll />]]} right={[['Z2', <Herkomst k={4} />], ['Z4', <SterkZwak k={4} keyName="Z4" />], ['Z5', <SafeCard k={4} />]]} />],
    ['T1', <Conflict />], ['K1', <Canvas />],
    ['Q2', <QuizN n={2} q="Q2" a="Q2b" question="“Hoeveel het ook oplevert, een aanvrager heeft altijd recht op uitleg.” Welk kader is dat?" options={['A. Gevolgen', 'B. Plichten', 'C. Zorg']} good={1} note={<>B, plichten: <span style={{ color: J.gold }}>een recht dat geldt, ongeacht het nut</span></>} />],
    ['S1', <Summary />], ['N1', <NowYou />],
  ]} />
);
