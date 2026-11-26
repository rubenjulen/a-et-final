// Kennisclip 5c · Drie soorten black box (blok 1). Script: clip5c/build.py; timing: src/timing_c5c.json.
import React from 'react';
import { AbsoluteFill, useCurrentFrame, interpolate, Easing } from 'remotion';
import timing from './timing_c5c.json';
import { clamp, fade, Pop } from './wk1_kit';
import { J, FONT, JTitle, JBanner, makeJKit } from './janssen_kit';
import { sp, makeW, T, Kick, Panel, Person, Switch, Bub, PhoneFrame, IconDot } from './janssen_parts';

const { cue, F, QuizN, Root } = makeJKit(timing);
const W = makeW(cue, F);
const at = (k, o = -0.2) => F(k, o);

/* ---------- iconen ---------- */
const st = (c) => ({ fill: 'none', stroke: c, strokeWidth: 6, strokeLinecap: 'round', strokeLinejoin: 'round' });
const Ico = ({ k, size = 60, color = '#fff' }) => {
  const s = { width: size, height: size };
  if (k === 1) return (<svg viewBox="0 0 100 100" style={s}><g {...st(color)}><rect x="22" y="46" width="56" height="42" rx="6" /><path d="M34 46 V32 Q34 16 50 16 Q66 16 66 32 V46" /><line x1="50" y1="62" x2="50" y2="72" /></g></svg>);
  if (k === 2) return (<svg viewBox="0 0 100 100" style={s}><g {...st(color)}><path d="M24 12 H62 L78 28 V88 H24 Z" /><path d="M34 40 q6 -6 12 0 t12 0 t10 0" /><path d="M34 56 q6 -6 12 0 t12 0 t10 0" /><path d="M34 72 q6 -6 12 0 t12 0" /></g></svg>);
  return (<svg viewBox="0 0 100 100" style={s}><g {...st(color)}>{[[18, 30], [18, 70], [50, 20], [50, 50], [50, 80], [82, 35], [82, 65]].map(([x, y], i) => <circle key={i} cx={x} cy={y} r="6" />)}
    {[[18, 30, 50, 20], [18, 30, 50, 50], [18, 30, 50, 80], [18, 70, 50, 20], [18, 70, 50, 50], [18, 70, 50, 80], [50, 20, 82, 35], [50, 50, 82, 35], [50, 50, 82, 65], [50, 80, 82, 65], [50, 20, 82, 65], [50, 80, 82, 35]].map(([a, b, c, d], i) => <line key={i} x1={a} y1={b} x2={c} y2={d} strokeWidth="3" />)}</g></svg>);
};
const SO = [
  { n: 1, name: 'Bewust geheim', col: J.red, ans: 'Openheid, of een onafhankelijke audit' },
  { n: 2, name: 'Te ingewikkeld voor wie het raakt', col: J.gold, ans: 'Uitleg in gewone taal, en een loket' },
  { n: 3, name: 'Ook voor de makers onbekend', col: J.blue, ans: 'Een leesbaar model, of strenge menselijke controle' },
];

/* ---------- algemene kaarten ---------- */
const DefCard = ({ k, text, tags = [], t0 }) => {
  const frame = useCurrentFrame();
  return (<Panel><div style={{ position: 'absolute', left: 44, top: 40, right: 44 }}>
    <Kick color={J.slate}>Wat het is</Kick>
    <T size={46} weight={700} color={J.navy} style={{ marginTop: 14, lineHeight: 1.18 }}>{text}</T>
    <div style={{ display: 'flex', gap: 14, marginTop: 34, flexWrap: 'wrap' }}>
      {tags.map((t, i) => <div key={t} style={{ opacity: sp(frame, t0 + i * 12), background: J.ice, border: `2px solid ${SO[k].col}`, borderRadius: 999, padding: '10px 22px' }}><T size={30} weight={700} color={J.navy}>{t}</T></div>)}
    </div>
  </div></Panel>);
};
const CaseCard = ({ kick, title, lines }) => {
  const frame = useCurrentFrame();
  return (<Panel><div style={{ position: 'absolute', left: 44, top: 40, right: 44 }}>
    <Kick color={J.red}>{kick}</Kick>
    <T size={56} weight={700} color={J.navy} style={{ marginTop: 8 }}>{title}</T>
    <div style={{ marginTop: 24 }}>
      {lines.map(([t, w], i) => { const s = sp(frame, w); return (
        <div key={i} style={{ display: 'flex', gap: 16, alignItems: 'baseline', marginBottom: 18, opacity: s, transform: `translateX(${(1 - s) * 30}px)` }}>
          <div style={{ width: 14, height: 14, borderRadius: 7, background: J.red, flex: 'none', transform: 'translateY(-5px)' }} /><T size={34} color={J.ink}>{t}</T>
        </div>); })}
    </div>
  </div></Panel>);
};
const AnswerCard = ({ k, extra }) => (
  <Panel bg={J.navy} style={{ border: 'none' }}><div style={{ position: 'absolute', left: 44, top: 44, right: 44 }}>
    <Kick color={J.gold} style={{ fontSize: 28 }}>Het antwoord op soort {k + 1}</Kick>
    <T size={56} weight={700} color="#fff" style={{ marginTop: 24, lineHeight: 1.15 }}>{SO[k].ans}</T>
    {extra && <T size={30} color={J.onNavyMuted} style={{ marginTop: 30 }}>{extra}</T>}
  </div></Panel>
);
const InfoCard = ({ kick, title, children, col = J.blue }) => (
  <Panel><div style={{ position: 'absolute', left: 44, top: 40, right: 44 }}>
    <Kick color={col}>{kick}</Kick>
    <T size={46} weight={700} color={J.navy} style={{ marginTop: 12, lineHeight: 1.18 }}>{title}</T>
    <div style={{ marginTop: 26 }}>{children}</div>
  </div></Panel>
);
const Box = ({ children }) => <Panel><svg viewBox="0 0 780 560" width="100%" height="100%">{children}</svg></Panel>;

/* ---------- de zwarte doos ---------- */
const Cube = ({ x, y, s = 1, lid = 0, q = 1 }) => (
  <g transform={`translate(${x},${y}) scale(${s})`}>
    <polygon points="-110,-40 0,-95 110,-40 0,15" fill="#2B3445" transform={`rotate(${-lid * 28} -110 -40)`} />
    <polygon points="-110,-40 0,15 0,150 -110,95" fill="#1A1F2B" /><polygon points="110,-40 0,15 0,150 110,95" fill="#11151D" />
    <text x="-2" y="100" textAnchor="middle" fontFamily={FONT} fontWeight="700" fontSize="90" fill="#fff" opacity={q}>?</text>
  </g>
);

/* ---------- scènes ---------- */
const Intro = () => {
  const frame = useCurrentFrame(); const s = sp(frame, 4);
  return (
    <AbsoluteFill style={{ background: `radial-gradient(1300px 900px at 78% 25%, #1A3D86 0%, ${J.navy} 62%)` }}>
      <div style={{ position: 'absolute', left: 140, top: 250, opacity: s }}><Kick color={J.gold} style={{ fontSize: 30 }}>Kennisclip 5c · AI &amp; Ethics · blok 1</Kick></div>
      <div style={{ position: 'absolute', left: 140, top: 300, fontFamily: FONT, fontWeight: 700, fontSize: 140, lineHeight: 1.02, color: '#fff', opacity: s, transform: `translateY(${(1 - s) * 40}px)` }}>Drie soorten black box</div>
      <div style={{ position: 'absolute', left: 140, top: 470, fontFamily: FONT, fontSize: 40, color: J.onNavyMuted, opacity: fade(frame, 18, 34) }}>bewust geheim · te ingewikkeld · ook voor de makers onbekend</div>
      <div style={{ position: 'absolute', left: 140, top: 600, display: 'flex', gap: 34 }}>
        {SO.map((d, i) => { const a = sp(frame, 24 + i * 7, { damping: 14 }); return <div key={i} style={{ opacity: a, transform: `translateY(${(1 - a) * 60}px)` }}><IconDot col={d.col} size={130} ring="rgba(255,255,255,.55)"><Ico k={d.n} size={78} /></IconDot></div>; })}
      </div>
    </AbsoluteFill>
  );
};

const BlackBox = () => {
  const frame = useCurrentFrame();
  const why = sp(frame, W('B1', 'Waarom'));
  const d = sp(frame, F('B2', 0.2));
  const ins = ['inkomen', 'district', 'looptijd', 'leeftijd'];
  const out = sp(frame, W('B2', 'eruit komt'));
  return (
    <AbsoluteFill style={{ background: J.bg }}>
      <JTitle at={at('B1')} kicker="Suribank · kredietaanvraag">Afgewezen. Maar waarom?</JTitle>
      <PhoneFrame title="Suribank" sub="berichten" left={128} top={250} h={560}>
        <Bub at={F('B1', 0.8)}>Uw aanvraag is afgewezen.</Bub>
        <div style={{ marginTop: 26, opacity: why }}><T size={30} color={J.slate}>Reden: <b style={{ color: J.red }}>—</b></T></div>
      </PhoneFrame>
      <div style={{ position: 'absolute', left: 640, top: 360, opacity: why * (1 - d), fontFamily: FONT, fontWeight: 700, fontSize: 120, color: J.red }}>Waarom?</div>
      <svg width="1180" height="600" style={{ position: 'absolute', left: 640, top: 240, opacity: d }}>
        {ins.map((t, i) => { const a = sp(frame, F('B2', 0.6 + i * 0.25)); return (
          <g key={t} opacity={a}><rect x="0" y={60 + i * 110} width="200" height="64" rx="32" fill="#fff" stroke={J.blue} strokeWidth="3" />
            <text x="100" y={102 + i * 110} textAnchor="middle" fontFamily={FONT} fontWeight="700" fontSize="30" fill={J.navy}>{t}</text>
            <line x1="210" y1={92 + i * 110} x2={360} y2={92 + 165 * 0 + (i - 1.5) * 30 + 190} stroke={J.slate} strokeWidth="4" strokeDasharray="10 8" strokeDashoffset={-frame * 2} /></g>); })}
        <Cube x={500} y={230} s={1.25} />
        <g opacity={out}><line x1="660" y1="300" x2="830" y2="300" stroke={J.slate} strokeWidth="5" /><polygon points="830,286 856,300 830,314" fill={J.slate} />
          <rect x="870" y="262" width="250" height="76" rx="38" fill={J.red} /><text x="995" y="312" textAnchor="middle" fontFamily={FONT} fontWeight="700" fontSize="34" fill="#fff">afgewezen</text></g>
        <text x="500" y="560" textAnchor="middle" fontFamily={FONT} fontWeight="700" fontSize="34" fill={J.navy} opacity={sp(frame, W('B2', 'maar niet'))}>wat gebeurt hier binnenin?</text>
      </svg>
    </AbsoluteFill>
  );
};

const Origin = () => {
  const frame = useCurrentFrame();
  const cards = [
    ['Uit de techniek', 'Een systeem dat je alleen kent aan invoer en uitvoer.', W('B3', 'techniek')],
    ['Frank Pasquale · 2015', 'The Black Box Society: geheime algoritmen bepalen de kansen van mensen.', W('B3', 'In 2015')],
    ['Jenna Burrell · 2016', 'Drie soorten ondoorzichtigheid, elk met een eigen antwoord.', W('B4', 'Jenna')],
  ];
  return (
    <AbsoluteFill style={{ background: J.bg }}>
      <JTitle at={at('B3')} kicker="Herkomst">Waar komt het begrip vandaan?</JTitle>
      <div style={{ position: 'absolute', left: 128, top: 240, width: 1664, display: 'flex', gap: 28 }}>
        {cards.map(([h, t, w], i) => { const a = sp(frame, w); return (
          <div key={h} style={{ flex: 1, opacity: a, transform: `translateY(${(1 - a) * 40}px)`, background: J.card, border: `2px solid ${J.line}`, borderTop: `10px solid ${i === 2 ? J.gold : J.blue}`, borderRadius: 20, padding: '28px 32px', minHeight: 250 }}>
            <T size={38} weight={700} color={J.navy}>{h}</T><T size={30} color={J.ink} style={{ marginTop: 12 }}>{t}</T>
          </div>); })}
      </div>
      <div style={{ position: 'absolute', left: 128, top: 560, width: 1664, display: 'flex', gap: 28 }}>
        {SO.map((d, i) => { const a = sp(frame, W('B4', 'drie soorten', 0.3 + i * 0.5)); return (
          <div key={d.n} style={{ flex: 1, opacity: a, transform: `scale(${0.9 + 0.1 * a})`, background: d.col, borderRadius: 20, padding: '22px 28px', display: 'flex', alignItems: 'center', gap: 22 }}>
            <Ico k={d.n} size={70} /><div><T size={24} weight={700} color="rgba(255,255,255,.85)">SOORT {d.n}</T><T size={34} weight={700} color="#fff">{d.name}</T></div>
          </div>); })}
      </div>
    </AbsoluteFill>
  );
};

/* ---------- soort 1 ---------- */
const LockBox = () => {
  const frame = useCurrentFrame();
  const sh = interpolate(frame, [F('S1a', 0.8), F('S1a', 1.6)], [-40, 0], { ...clamp, easing: Easing.out(Easing.back(2)) });
  const tags = [['bedrijfsgeheim', 120, 120, W('S1a', 'bedrijfsgeheim')], ['staatsgeheim', 650, 140, W('S1a', 'staatsgeheim')]];
  return (<Box>
    <Cube x={390} y={250} s={1.3} q={0} />
    <g transform="translate(390,330)"><path d={`M-40 0 V${-40 + sh} Q-40 ${-90 + sh} 0 ${-90 + sh} Q40 ${-90 + sh} 40 ${-40 + sh} V0`} fill="none" stroke={J.gold} strokeWidth="16" />
      <rect x="-70" y="-10" width="140" height="110" rx="14" fill={J.gold} /><circle cx="0" cy="38" r="14" fill={J.navy} /><rect x="-5" y="40" width="10" height="34" fill={J.navy} /></g>
    {tags.map(([t, x, y, w]) => <g key={t} opacity={sp(frame, w)}><rect x={x - 110} y={y - 40} width="220" height="58" rx="29" fill="#fff" stroke={J.red} strokeWidth="3" /><text x={x} y={y} textAnchor="middle" fontFamily={FONT} fontWeight="700" fontSize="28" fill={J.red}>{t}</text></g>)}
  </Box>);
};
const AuditIll = () => {
  const frame = useCurrentFrame();
  const lid = interpolate(frame, [F('S1d', 0.5), F('S1d', 1.8)], [0, 1], { ...clamp, easing: Easing.inOut(Easing.cubic) });
  const mx = 470 + 40 * Math.sin(frame / 14);
  return (<Box>
    <Cube x={390} y={290} s={1.3} lid={lid} q={0} />
    <g transform={`translate(${mx},150)`} opacity={sp(frame, F('S1d', 1.6))}><circle cx="0" cy="0" r="70" fill="rgba(234,240,248,.6)" stroke={J.navy} strokeWidth="14" /><line x1="50" y1="50" x2="120" y2="120" stroke={J.navy} strokeWidth="22" strokeLinecap="round" /></g>
    <text x="390" y="530" textAnchor="middle" fontFamily={FONT} fontWeight="700" fontSize="34" fill={J.navy} opacity={sp(frame, W('S1d', 'Iemand van buiten'))}>iemand van buiten kijkt mee</text>
  </Box>);
};

/* ---------- soort 2 ---------- */
const JargonPhone = () => {
  const frame = useCurrentFrame(); const q = sp(frame, W('S2b', 'Wat moet'));
  return (<Panel>
    <PhoneFrame title="Suribank" sub="besluit kredietaanvraag" left={40} top={30} h={530}>
      <Bub at={F('S2a', 0.4)} size={25}>Besluit: afgewezen. Score 42 (drempel 50).</Bub>
      <Bub at={W('S2b', 'belangrijkste')} size={23}>Top-kenmerken (SHAP): district −0,31 · looptijd −0,18 · inkomen −0,12. Modelversie 3.2, AUC 0,81.</Bub>
    </PhoneFrame>
    <svg viewBox="0 0 280 400" style={{ position: 'absolute', left: 500, top: 90, width: 250, height: 360 }}><Person x={140} y={250} s={2.6} col={J.gold} />
      <text x="140" y="110" textAnchor="middle" fontFamily={FONT} fontWeight="700" fontSize="90" fill={J.red} opacity={q}>?</text></svg>
    <div style={{ position: 'absolute', left: 500, top: 460, width: 250, textAlign: 'center', opacity: q }}><T size={28} weight={700} color={J.navy}>Wat moet ik hiermee?</T></div>
  </Panel>);
};
const PlainPhone = () => (
  <Panel>
    <PhoneFrame title="Suribank" sub="besluit kredietaanvraag" left={170} top={30} h={530}>
      <Bub at={F('S2d', 0.2)} size={25}>Uw aanvraag is afgewezen.</Bub>
      <Bub at={F('S2d', 1.0)} size={25} bg="#E2F1E8">Met een looptijd van 24 in plaats van 12 maanden was uw aanvraag goedgekeurd.</Bub>
      <Bub at={F('S2d', 2.4)} size={25}>Vragen of bezwaar? Kies hieronder “Praat met een medewerker”.</Bub>
    </PhoneFrame>
  </Panel>
);
const NoObjection = () => {
  const frame = useCurrentFrame();
  const steps = ['Begrijpen', 'Bezwaar maken', 'Laten herstellen'];
  const x = sp(frame, F('S2c', 1.2));
  return (<InfoCard kick="Waarom dit telt" title="Geen begrip, dan ook geen bezwaar" col={J.gold}>
    <div style={{ display: 'flex', alignItems: 'center', gap: 14 }}>
      {steps.map((s, i) => <React.Fragment key={s}><div style={{ background: J.ice, borderRadius: 14, padding: '16px 18px', position: 'relative' }}><T size={28} weight={700} color={J.navy}>{s}</T>
        <div style={{ position: 'absolute', left: 10, right: 10, top: '50%', height: 5, background: J.red, transform: `scaleX(${x})`, transformOrigin: 'left' }} /></div>{i < 2 && <T size={34} color={J.slate}>→</T>}</React.Fragment>)}
    </div>
  </InfoCard>);
};
const ContraCard = () => {
  const frame = useCurrentFrame();
  return (<InfoCard kick="Contrafactische uitleg · Wachter e.a. (2018)" title="Wat had er anders moeten zijn?" col={J.green}>
    <div style={{ opacity: sp(frame, F('S2d', 1.2)), background: '#E2F1E8', borderLeft: `8px solid ${J.green}`, borderRadius: 14, padding: '20px 26px' }}>
      <T size={34} weight={700} color={J.navy}>“Met een looptijd van 24 in plaats van 12 maanden was uw aanvraag goedgekeurd.”</T></div>
    <T size={28} color={J.slate} style={{ marginTop: 20, opacity: sp(frame, W('S2d', 'Dat heet')) }}>De aanvrager weet wat ze kan doen, zonder het model te hoeven begrijpen.</T>
  </InfoCard>);
};

/* ---------- soort 3 ---------- */
const LAY = [[4, 110], [6, 300], [6, 490], [3, 670]];
const NetIll = () => {
  const frame = useCurrentFrame();
  const nodes = LAY.map(([n, x]) => Array.from({ length: n }).map((_, i) => [x, 280 + (i - (n - 1) / 2) * 72]));
  const nums = ['0,173', '−1,02', '0,88', '2,4·10⁻³', '−0,57', '1,316', '−0,09'];
  const t0 = F('S3b', 0.3);
  return (<Box>
    {nodes.slice(0, -1).map((col, l) => col.map(([x1, y1], i) => nodes[l + 1].map(([x2, y2], j) => {
      const o = 0.15 + 0.55 * Math.abs(Math.sin(frame / 9 + i * 1.7 + j * 2.3 + l));
      return <line key={`${l}${i}${j}`} x1={x1} y1={y1} x2={x2} y2={y2} stroke={J.blue} strokeWidth="2.5" opacity={o} />;
    })))}
    {nodes.flat().map(([x, y], i) => <circle key={i} cx={x} cy={y} r="18" fill={J.navy} stroke="#fff" strokeWidth="3" />)}
    {nums.map((n, i) => { const p = interpolate(frame, [t0 + i * 14, t0 + i * 14 + 90], [0, 1], clamp); return (
      <text key={n} x={150 + i * 80} y={420 - p * 340} fontFamily={FONT} fontWeight="700" fontSize="32" fill={J.dblue} opacity={p > 0 && p < 1 ? Math.sin(p * Math.PI) : 0}>{n}</text>); })}
    <text x="390" y="530" textAnchor="middle" fontFamily={FONT} fontWeight="700" fontSize="32" fill={J.navy} opacity={sp(frame, W('S3b', 'de gewichten'))}>miljarden gewichten, zonder betekenis</text>
  </Box>);
};
const ApiIll = () => {
  const frame = useCurrentFrame(); const a1 = sp(frame, W('S3c', 'soort één')); const a3 = sp(frame, W('S3c', 'soort drie'));
  return (<Box>
    <rect x="40" y="200" width="230" height="140" rx="20" fill={J.ice} stroke={J.blue} strokeWidth="4" /><text x="155" y="280" textAnchor="middle" fontFamily={FONT} fontWeight="700" fontSize="34" fill={J.navy}>Jullie app</text>
    <line x1="280" y1="270" x2="410" y2="270" stroke={J.slate} strokeWidth="5" strokeDasharray="12 8" strokeDashoffset={-frame * 2} /><polygon points="410,256 436,270 410,284" fill={J.slate} />
    <g fill="#1A1F2B"><rect x="450" y="200" width="300" height="140" rx="40" /><circle cx="530" cy="200" r="50" /><circle cx="630" cy="185" r="62" /></g>
    <text x="600" y="262" textAnchor="middle" fontFamily={FONT} fontWeight="700" fontSize="28" fill="#fff">taalmodel van</text><text x="600" y="298" textAnchor="middle" fontFamily={FONT} fontWeight="700" fontSize="28" fill="#fff">een aanbieder</text>
    <g opacity={a1} transform="translate(470,400)"><circle r="46" fill={J.red} /><g transform="translate(-30,-30)"><svg width="60" height="60" viewBox="0 0 100 100"><g {...st('#fff')}><rect x="22" y="46" width="56" height="42" rx="6" /><path d="M34 46 V32 Q34 16 50 16 Q66 16 66 32 V46" /></g></svg></g>
      <text x="0" y="86" textAnchor="middle" fontFamily={FONT} fontWeight="700" fontSize="26" fill={J.red}>soort 1</text></g>
    <g opacity={a3} transform="translate(690,400)"><circle r="46" fill={J.blue} /><text x="0" y="86" textAnchor="middle" fontFamily={FONT} fontWeight="700" fontSize="26" fill={J.blue}>soort 3</text>
      {[[-20, -14], [-20, 14], [0, -22], [0, 0], [0, 22], [20, -12], [20, 12]].map(([x, y], i) => <circle key={i} cx={x} cy={y} r="5" fill="#fff" />)}</g>
  </Box>);
};
const TreeIll = () => {
  const frame = useCurrentFrame();
  const N = ({ x, y, w = 260, t, col = J.navy, fill = '#fff', tc = J.navy, a }) => (<g opacity={a}><rect x={x - w / 2} y={y - 34} width={w} height="68" rx="14" fill={fill} stroke={col} strokeWidth="3" /><text x={x} y={y + 10} textAnchor="middle" fontFamily={FONT} fontWeight="700" fontSize="26" fill={tc}>{t}</text></g>);
  const a = (o) => sp(frame, F('S3d', o));
  return (<Box>
    <text x="390" y="56" textAnchor="middle" fontFamily={FONT} fontWeight="700" fontSize="32" fill={J.green}>Een leesbaar model</text>
    <g stroke={J.slate} strokeWidth="4" opacity={a(1.2)}><line x1="390" y1="150" x2="220" y2="260" /><line x1="390" y1="150" x2="600" y2="260" /><line x1="220" y1="320" x2="120" y2="420" /><line x1="220" y1="320" x2="365" y2="420" /></g>
    <N x={390} y={130} w={330} t="Inkomen voldoende?" a={a(0.6)} />
    <N x={220} y={290} w={330} t="Schuld onder 30%?" a={a(1.4)} /><N x={600} y={290} w={300} t="Medewerker kijkt" fill={J.ice} a={a(1.6)} />
    <N x={120} y={450} w={200} t="Goedkeuren" fill="#E2F1E8" col={J.green} a={a(2.0)} /><N x={370} y={450} w={240} t="Medewerker kijkt" fill={J.ice} a={a(2.2)} />
    <text x="390" y="540" textAnchor="middle" fontFamily={FONT} fontSize="26" fill={J.slate} opacity={a(2.6)}>ja links, nee rechts · elke stap is te volgen</text>
  </Box>);
};

/* ---------- één soort-scène ---------- */
const SoortScene = ({ k, k0, left, right }) => {
  const d = SO[k];
  return (
    <AbsoluteFill style={{ background: J.bg }}>
      <Pop at={F(k0, -0.2)} style={{ left: 128, top: 60 }}><IconDot col={d.col} size={110}><Ico k={d.n} size={66} /></IconDot></Pop>
      <Pop at={F(k0, 0)} style={{ left: 268, top: 62, width: 1250 }}>
        <Kick color={J.slate}>Soort {d.n} van 3 · Burrell (2016)</Kick>
        <div style={{ fontFamily: FONT, fontWeight: 700, fontSize: 60, lineHeight: 1.05, color: J.navy, marginTop: 6 }}>{d.name}</div>
      </Pop>
      <div style={{ position: 'absolute', left: 1640, top: 82, display: 'flex', gap: 12 }}>
        {SO.map((x, i) => <div key={i} style={{ width: 34, height: 34, borderRadius: 17, background: i === k ? x.col : i < k ? '#B7C3D4' : J.line }} />)}
      </div>
      <Switch items={left} style={{ left: 128, top: 240, width: 780, height: 590 }} />
      <Switch items={right} style={{ left: 960, top: 240, width: 832, height: 590 }} />
    </AbsoluteFill>
  );
};

/* ---------- wanneer, samenvatting, opdracht ---------- */
const When = () => {
  const frame = useCurrentFrame();
  const col = (title, c, items, ws) => (
    <div style={{ flex: 1, background: J.card, border: `2px solid ${J.line}`, borderTop: `10px solid ${c}`, borderRadius: 20, padding: '26px 32px', minHeight: 420 }}>
      <Kick color={c} style={{ fontSize: 28 }}>{title}</Kick>
      {items.map((t, i) => { const a = sp(frame, ws[i]); return <T key={t} size={36} weight={700} color={J.navy} style={{ marginTop: 18, opacity: a, transform: `translateX(${(1 - a) * 30}px)` }}>{t}</T>; })}
    </div>
  );
  return (
    <AbsoluteFill style={{ background: J.bg }}>
      <JTitle at={at('W1')} kicker="Aanvaardbaar of niet">Mag een black box?</JTitle>
      <div style={{ position: 'absolute', left: 128, top: 240, width: 1664, display: 'flex', gap: 32 }}>
        {col('Vaak wel', J.green, ['Lage impact', 'Het systeem adviseert alleen', 'Een mens beslist echt', 'Zoals muziekaanbevelingen'], [W('W1', 'lage impact'), W('W1', 'alleen adviseert'), W('W1', 'een mens'), W('W1', 'Denk aan')])}
        {col('Niet', J.red, ['Rechten of vrijheid op het spel', 'Geen bezwaar mogelijk', 'Niemand grijpt echt in'], [W('W2', 'rechten'), W('W2', 'geen bezwaar'), W('W2', 'niemand')])}
      </div>
      <JBanner at={W('W2', 'De vuistregel')} top={740} size={42}>Hoe groter de impact op iemands leven, hoe zwaarder de eis aan uitleg.</JBanner>
    </AbsoluteFill>
  );
};
const Summary = () => {
  const frame = useCurrentFrame(); const ws = ['Bewust', 'Te ingewikkeld', 'Ook voor'];
  return (
    <AbsoluteFill style={{ background: J.bg }}>
      <JTitle at={at('S9')}>Samengevat</JTitle>
      {SO.map((d, i) => { const a = sp(frame, W('S9', ws[i])); return (
        <div key={d.n} style={{ position: 'absolute', left: 128, top: 220 + i * 175, width: 1664, height: 150, display: 'flex', alignItems: 'center', gap: 30, background: J.card, border: `2px solid ${J.line}`, borderRadius: 20, padding: '0 30px', opacity: a, transform: `translateX(${(1 - a) * -60}px)` }}>
          <IconDot col={d.col} size={96}><Ico k={d.n} size={58} /></IconDot>
          <T size={40} weight={700} color={J.navy} style={{ width: 640 }}>{d.name}</T><T size={44} color={J.slate}>→</T><T size={38} color={J.ink}>{d.ans}</T>
        </div>); })}
    </AbsoluteFill>
  );
};
const NowYou = () => {
  const frame = useCurrentFrame();
  const st2 = [['Welke soort black box zit er in jullie oplossing?', 'Welke soort'], ['Voor wie is het een black box: jullie, de partner, de klant?', 'en voor wie'], ['Schrijf het op bij domein 6 van de nulmeting: transparantie.', 'Schrijf']];
  return (
    <AbsoluteFill style={{ background: J.bg }}>
      <JTitle at={at('N1')} kicker="Opdracht" size={68}>Nu jij</JTitle>
      {st2.map(([t, w], i) => { const a = sp(frame, W('N1', w)); return (
        <div key={i} style={{ position: 'absolute', left: 128, top: 250 + i * 170, width: 1664, opacity: a, transform: `translateY(${(1 - a) * 40}px)`, background: J.card, border: `2px solid ${J.line}`, borderRadius: 20, padding: '28px 38px', display: 'flex', gap: 30, alignItems: 'center' }}>
          <div style={{ fontFamily: FONT, fontWeight: 700, fontSize: 64, color: J.blue, width: 50 }}>{i + 1}</div><T size={42} color={J.navy} weight={700}>{t}</T>
        </div>); })}
    </AbsoluteFill>
  );
};

const OPT = ['A. Bewust geheim', 'B. Te ingewikkeld voor wie het raakt', 'C. Ook voor de makers onbekend'];
export const Clip5c = () => (
  <Root scenes={[
    ['B0', <Intro />], ['B1', <BlackBox />], ['B3', <Origin />],
    ['S1a', <SoortScene k={0} k0="S1a" left={[[at('S1a'), <LockBox />], [at('S1d'), <AuditIll />]]} right={[
      [at('S1a'), <DefCard k={0} text="Het model kan worden uitgelegd, maar de eigenaar wil het niet laten zien." tags={['bedrijfsgeheim', 'staatsgeheim']} t0={W('S1a', 'bedrijfsgeheim')} />],
      [at('S1b'), <CaseCard kick="Echte casus · Nederland, 2020" title="SyRI" lines={[['Risicomodel om fraude met uitkeringen op te sporen', W('S1b', 'een Nederlands')], ['Het model en de indicatoren waren geheim', W('S1b', 'Het risicomodel')], ['Rechtbank Den Haag, 5 februari 2020: in strijd met het recht op privéleven (art. 8 EVRM)', W('S1b', 'In februari')]]} />],
      [at('S1c'), <CaseCard kick="Echte casus · Verenigde Staten, 2016" title="State v. Loomis" lines={[['Een rechter gebruikte de COMPAS-risicoscore bij de strafmaat', W('S1c', 'gebruikte')], ['Het model is een bedrijfsgeheim', W('S1c', 'geheime')], ['De verdachte kon de score niet controleren', W('S1c', 'De verdachte')]]} />],
      [at('S1d'), <AnswerCard k={0} extra="Iemand van buiten moet kunnen meekijken." />]]} />],
    ['S2a', <SoortScene k={1} k0="S2a" left={[[at('S2a'), <JargonPhone />], [at('S2d'), <PlainPhone />]]} right={[
      [at('S2a'), <DefCard k={1} text="De uitleg bestaat wel, maar alleen in vaktaal." tags={['score', 'drempel', 'gewichten']} t0={F('S2a', 3)} />],
      [at('S2c'), <NoObjection />], [W('S2c', 'Het antwoord', -0.2), <AnswerCard k={1} />], [at('S2d'), <ContraCard />]]} />],
    ['S3a', <SoortScene k={2} k0="S3a" left={[[at('S3a'), <NetIll />], [at('S3c'), <ApiIll />], [at('S3d'), <TreeIll />]]} right={[
      [at('S3a'), <DefCard k={2} text="Zelfs de experts weten niet precies waarom een uitkomst zo uitvalt." tags={['deep learning', 'grote taalmodellen']} t0={F('S3a', 4)} />],
      [at('S3b'), <InfoCard kick="Waarom de code lezen niet helpt" title="Je kunt de gewichten zien, maar ze vertellen niet wat ze betekenen."><T size={30} color={J.slate}>Een groot taalmodel heeft miljarden gewichten. De kennis zit in die getallen, niet in de code.</T></InfoCard>],
      [at('S3c'), <InfoCard kick="Bij jullie oplossing" title="Een taalmodel van een externe aanbieder is soort 1 én soort 3." col={J.red}><T size={30} color={J.slate}>Geheim voor jullie, en ook voor de makers niet helemaal te verklaren.</T></InfoCard>],
      [at('S3d'), <AnswerCard k={2} extra="Bij grote gevolgen een leesbaar model als dat even goed werkt (Rudin, 2019)." />]]} />],
    ['Q1', <QuizN n={1} q="Q1" a="Q1b" question="Een gemeente gebruikt een risicomodel, maar de leverancier weigert te laten zien hoe het werkt. Welke soort is dat?" options={OPT} good={0} note={<>A, bewust geheim: <span style={{ color: J.gold }}>openheid of een audit</span></>} />],
    ['W1', <When />],
    ['Q2', <QuizN n={2} q="Q2" a="Q2b" question="De aanvrager krijgt alleen: “score 42, drempel 50”. Welke soort black box is dat?" options={OPT} good={1} note={<>B: <span style={{ color: J.gold }}>de uitleg bestaat, maar niet in gewone taal</span></>} />],
    ['S9', <Summary />], ['N1', <NowYou />],
  ]} />
);
