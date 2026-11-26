import React from 'react';
import timing from './timing_kA.json';
import {
  C, SERIF, SANS, FPS, clamp, Easing, interpolate, spring, useCurrentFrame, AbsoluteFill,
  useSpring, fade, Pop, Banner, Title, Shanti, MiniShanti, Bank, Figure, Bubble, Phone, makeKit,
} from './wk1_kit';

const { F, end, QuizN, Root } = makeKit(timing);

const LAYERS = [
  { k: 'WAT', q: 'Wat beoordeel je?', col: C.green },
  { k: 'HOE', q: 'Hoe pak je het aan?', col: '#1F5A6B' },
  { k: 'WAAROM', q: 'Waarom goed of fout?', col: '#7A4E86' },
  { k: 'WAAR', q: 'Welke regels gelden?', col: C.terra },
];
const DOMAINS = ['Doel en noodzaak', 'Governance', 'Stakeholders', 'Data en privacy', 'Fairness', 'Transparantie', 'Menselijke controle', 'Veiligheid', 'AI-geletterdheid', 'Duurzaamheid', 'Monitoring'];
const Chip = ({ children, on = false, col = C.green, size = 22, style = {} }) => (
  <div style={{ display: 'inline-block', fontFamily: SANS, fontWeight: 700, fontSize: size, padding: '7px 16px', borderRadius: 999, margin: '0 8px 8px 0',
    background: on ? col : C.sand, color: on ? C.card : C.ink, boxShadow: on ? '0 6px 16px rgba(0,0,0,.18)' : 'none', ...style }}>{children}</div>
);

/* ---------- 1. Intro ---------- */
const Intro = () => {
  const s = useSpring(F('A0', -0.4));
  const frame = useCurrentFrame();
  return (
    <AbsoluteFill style={{ background: `radial-gradient(1200px 800px at 75% 30%, #1B4A3E 0%, ${C.dark} 60%)` }}>
      <div style={{ position: 'absolute', left: 140, top: 300, fontFamily: SANS, fontSize: 30, fontWeight: 700, letterSpacing: 3, color: C.amber, opacity: s }}>KADERCLIP A · AI &amp; ETHICS · BLOK 1</div>
      <div style={{ position: 'absolute', left: 140, top: 360, width: 1100, fontFamily: SERIF, fontWeight: 700, fontSize: 124, lineHeight: 1.04, color: C.light, opacity: s, transform: `translateY(${(1 - s) * 50}px)` }}>Het kaderlandschap</div>
      {LAYERS.map((l, i) => {
        const a = spring({ frame: frame - F('A0', 0.4 + i * 0.25), fps: FPS, config: { damping: 16 } });
        return <div key={l.k} style={{ position: 'absolute', left: 1320, top: 300 + i * 92, width: 440, height: 74, borderRadius: 16, background: l.col, opacity: 0.85 * a, transform: `translateX(${(1 - a) * 120}px)`, fontFamily: SANS, fontWeight: 700, fontSize: 30, color: C.card, display: 'flex', alignItems: 'center', paddingLeft: 28, letterSpacing: 2 }}>{l.k}</div>;
      })}
    </AbsoluteFill>
  );
};

/* ---------- 2. De stapel ---------- */
const NORMS = ['UNESCO-aanbeveling', 'NIST AI RMF', 'AI-verordening (EU)', 'ISO/IEC 42001', 'IEEE CertifAIEd', 'OECD AI-principes', 'AIGP', 'Surinaamse wet', 'CEET'];
const Pile = () => {
  const frame = useCurrentFrame();
  const sh = useSpring(F('A1', 0));
  const sort = interpolate(frame, [F('A3', 1.2), F('A3', 3.2)], [0, 1], { ...clamp, easing: Easing.inOut(Easing.cubic) });
  const frameIn = useSpring(F('A3', 2.6));
  return (
    <AbsoluteFill style={{ background: C.light }}>
      <div style={{ position: 'absolute', left: 110, top: 200, width: 400, height: 460, opacity: sh * (1 - 0.6 * sort) }}><Shanti frame={frame} /></div>
      <Pop at={F('A1', 1.6)} style={{ left: 520, top: 300, width: 220 }}><div style={{ width: 200, height: 215, opacity: 1 - 0.6 * sort }}><Bank /></div></Pop>
      <Pop at={F('A1', 2.6)} style={{ left: 520, top: 230 }}>
        <div style={{ fontFamily: SANS, fontWeight: 700, fontSize: 26, color: C.terra, background: C.card, border: `2px solid ${C.terra}`, borderRadius: 14, padding: '8px 16px', opacity: 1 - sort }}>model beslist mee</div>
      </Pop>
      <Pop at={F('A2', 0)} style={{ left: 820, top: 110, width: 960 }}><div style={{ fontFamily: SERIF, fontWeight: 700, fontSize: 56, color: C.ink, opacity: 1 - sort }}>Is dat verantwoord?</div></Pop>
      {NORMS.map((n, i) => {
        const d = spring({ frame: frame - F('A2', 1.4 + i * 0.32), fps: FPS, config: { damping: 13, stiffness: 120 } });
        const rot = [-6, 4, -3, 7, -5, 2, -8, 5, -2][i];
        const x0 = 900 + ((i * 97) % 330), y0 = 720 - i * 62;
        const tx = 1060, ty = 300 + (i % 4) * 120;
        const x = x0 + (tx - x0) * sort, y = y0 + (ty - y0) * sort;
        return (
          <div key={n} style={{ position: 'absolute', left: x, top: y - (1 - d) * 500, width: 480, opacity: d * (1 - sort), transform: `rotate(${rot * (1 - sort)}deg)`, background: C.card, border: `2px solid ${C.line}`, borderRadius: 12, padding: '16px 22px', fontFamily: SANS, fontWeight: 700, fontSize: 28, color: C.ink, boxShadow: '0 10px 24px rgba(18,49,42,.12)' }}>{n}</div>
        );
      })}
      <div style={{ position: 'absolute', left: 820, top: 230, width: 960, opacity: frameIn, transform: `scale(${0.9 + 0.1 * frameIn})` }}>
        <div style={{ fontFamily: SERIF, fontWeight: 700, fontSize: 56, color: C.ink, marginBottom: 22 }}>Eén kader, vier lagen</div>
        {LAYERS.map((l) => <div key={l.k} style={{ height: 96, borderRadius: 16, background: l.col, marginBottom: 16, display: 'flex', alignItems: 'center', paddingLeft: 30, fontFamily: SANS, fontWeight: 700, fontSize: 34, color: C.card, letterSpacing: 2 }}>{l.k}</div>)}
      </div>
    </AbsoluteFill>
  );
};

/* ---------- 3. De vier lagen ---------- */
const LayerRow = ({ l, i, at, children, glow = 0, top }) => {
  const s = useSpring(at);
  return (
    <div style={{ position: 'absolute', left: 128, top, width: 1664, height: 140, opacity: s, transform: `translateX(${(1 - s) * -80}px)`, display: 'flex', borderRadius: 18, overflow: 'hidden', background: C.card, border: `2px solid ${C.line}`, boxShadow: glow > 0 ? `0 0 0 ${6 * glow}px ${l.col}55` : '0 10px 24px rgba(18,49,42,.08)' }}>
      <div style={{ width: 330, background: l.col, color: C.card, padding: '22px 28px' }}>
        <div style={{ fontFamily: SANS, fontWeight: 700, fontSize: 34, letterSpacing: 2 }}>{l.k}</div>
        <div style={{ fontFamily: SANS, fontSize: 24, opacity: 0.9, marginTop: 6 }}>{l.q}</div>
      </div>
      <div style={{ flex: 1, padding: '20px 26px', display: 'flex', flexWrap: 'wrap', alignContent: 'center' }}>{children}</div>
    </div>
  );
};
const Layers = () => {
  const frame = useCurrentFrame();
  const g = (i) => { const t0 = F('A8', 0.6 + i * 0.9); return interpolate(frame, [t0, t0 + 8, t0 + 24, t0 + 34], [0, 1, 1, 0], clamp); };
  const nist = ['Besturen', 'In kaart brengen', 'Meten', 'Beheersen'];
  const lenses = ['Gevolgen', 'Rechten en plichten', 'Rechtvaardigheid', 'Professionele integriteit'];
  return (
    <AbsoluteFill style={{ background: C.light }}>
      <Title at={F('A4', -0.3)} top={70} size={56}>Eén kader, vier lagen</Title>
      <LayerRow l={LAYERS[0]} i={0} top={180} at={F('A4', 0)} glow={g(0)}>
        {DOMAINS.map((d, j) => <Chip key={d} size={20} on={d === 'Fairness' || d === 'Data en privacy' || d === 'Menselijke controle' ? frame > F('A4', 3.4) : false}
          style={{ opacity: fade(frame, F('A4', 0.8 + j * 0.12), F('A4', 1.1 + j * 0.12)) }}>{d}</Chip>)}
      </LayerRow>
      <LayerRow l={LAYERS[1]} i={1} top={338} at={F('A5', 0)} glow={g(1)}>
        <Chip size={22} on col={LAYERS[1].col}>NIST AI RMF</Chip>
        {nist.map((n, j) => <React.Fragment key={n}><Chip size={22} style={{ opacity: fade(frame, F('A5', 3.0 + j * 0.5), F('A5', 3.3 + j * 0.5)) }}>{n}</Chip>{j < 3 && <span style={{ fontSize: 26, color: C.mute, margin: '0 10px 8px 0', opacity: fade(frame, F('A5', 3.2 + j * 0.5), F('A5', 3.5 + j * 0.5)) }}>→</span>}</React.Fragment>)}
      </LayerRow>
      <LayerRow l={LAYERS[2]} i={2} top={496} at={F('A6', 0)} glow={g(2)}>
        <Chip size={22} on col={LAYERS[2].col}>UNESCO-aanbeveling</Chip>
        {lenses.map((n, j) => <Chip key={n} size={22} style={{ opacity: fade(frame, F('A6', 3.0 + j * 0.4), F('A6', 3.3 + j * 0.4)) }}>{n}</Chip>)}
      </LayerRow>
      <LayerRow l={LAYERS[3]} i={3} top={654} at={F('A7', 0)} glow={g(3)}>
        <Chip size={22} on col={LAYERS[3].col}>Surinaamse wet en beleid</Chip>
        <Chip size={22} style={{ opacity: fade(frame, F('A7', 2.4), F('A7', 2.8)) }}>de sector</Chip>
        <Chip size={22} style={{ opacity: fade(frame, F('A7', 3.4), F('A7', 3.8)) }}>buitenlandse regels, als die nodig zijn</Chip>
      </LayerRow>
    </AbsoluteFill>
  );
};

/* ---------- 4. Voorbeeld Shanti ---------- */
const ShantiFair = () => {
  const frame = useCurrentFrame();
  const q = useSpring(F('A8b', 1.4));
  const hit = useSpring(F('A8b', 4.6));
  return (
    <AbsoluteFill style={{ background: C.light }}>
      <Title at={F('A8b', -0.2)} top={80} size={52} kicker="VOORBEELD">Een vraag in de laag wat</Title>
      <div style={{ position: 'absolute', left: 110, top: 250, width: 440, height: 500 }}><Shanti frame={frame} /></div>
      <div style={{ position: 'absolute', left: 580, top: 280, width: 560, opacity: q, transform: `translateY(${(1 - q) * 30}px)` }}>
        <div style={{ background: C.card, border: `3px solid ${C.terra}`, borderRadius: '24px 24px 24px 6px', padding: '26px 30px', fontFamily: SERIF, fontWeight: 600, fontSize: 40, lineHeight: 1.2, color: C.ink }}>Wordt ze vaker afgewezen omdat ze in Nickerie woont?</div>
      </div>
      <svg style={{ position: 'absolute', left: 1140, top: 380 }} width="140" height="80"><path d={`M10 40 L${10 + 110 * hit} 40`} stroke={C.dark} strokeWidth="8" strokeLinecap="round" />{hit > 0.9 && <polygon points="120,22 140,40 120,58" fill={C.dark} />}</svg>
      <div style={{ position: 'absolute', left: 1300, top: 250, width: 500, opacity: hit, transform: `scale(${0.9 + 0.1 * hit})` }}>
        <div style={{ background: LAYERS[0].col, color: C.card, borderRadius: '18px 18px 0 0', padding: '16px 24px', fontFamily: SANS, fontWeight: 700, fontSize: 32, letterSpacing: 2 }}>WAT</div>
        <div style={{ background: C.card, border: `2px solid ${C.line}`, borderTop: 'none', borderRadius: '0 0 18px 18px', padding: '22px 24px' }}>
          {['Data en privacy', 'Fairness', 'Transparantie', 'Menselijke controle'].map((d) => <Chip key={d} size={24} on={d === 'Fairness'} col={C.terra}>{d}</Chip>)}
          <div style={{ fontFamily: SANS, fontSize: 24, color: C.mute, marginTop: 8 }}>domein 5: fairness en non-discriminatie</div>
        </div>
      </div>
    </AbsoluteFill>
  );
};

/* ---------- 5. Andere kaders vinden hun plek ---------- */
const Badge = ({ at, children, col }) => {
  const frame = useCurrentFrame();
  const s = spring({ frame: frame - at, fps: FPS, config: { damping: 14, stiffness: 110 } });
  return <div style={{ display: 'inline-block', marginRight: 12, opacity: s, transform: `translateX(${(1 - s) * 700}px)`, background: col, color: C.card, fontFamily: SANS, fontWeight: 700, fontSize: 26, padding: '10px 20px', borderRadius: 12, boxShadow: '0 8px 20px rgba(0,0,0,.18)' }}>{children}</div>;
};
const Frameworks = () => {
  const frame = useCurrentFrame();
  const side = (k0, k1) => interpolate(frame, [F(k0, -0.2), F(k0, 0.3), F(k1, -0.5), F(k1, 0)], [0, 1, 1, 0], clamp);
  const rows = [
    [<Badge key="i" at={F('A10', 0.3)} col={LAYERS[0].col}>IEEE CertifAIEd</Badge>,
      <span key="s" style={{ fontFamily: SANS, fontSize: 22, color: C.mute, opacity: fade(frame, F('A10', 2.5), F('A10', 3.0)) }}>transparantie · verantwoording · bias · privacy</span>],
    [<Badge key="iso" at={F('A11', 0.3)} col={LAYERS[1].col}>ISO/IEC 42001</Badge>, <Badge key="aigp" at={F('A11', 1.0)} col={LAYERS[1].col}>AIGP</Badge>],
    [<span key="l" style={{ fontFamily: SANS, fontSize: 22, color: C.mute }}>vier lenzen met hun theorie</span>],
    [<Badge key="eu" at={F('A12', 0.3)} col={LAYERS[3].col}>AI-verordening (EU)</Badge>,
      <span key="n" style={{ fontFamily: SANS, fontWeight: 700, fontSize: 22, color: C.terra, opacity: fade(frame, F('A12', 2.0), F('A12', 2.5)) }}>geldt niet in Suriname · vergelijking</span>],
  ];
  const weeks = [['B', 'blok 1', 'IEEE CertifAIEd'], ['C', 'blok 1', 'AI-verordening'], ['D', 'blok 2', 'AIGP'], ['E', 'blok 2', 'ISO/IEC 42001']];
  return (
    <AbsoluteFill style={{ background: C.light }}>
      <Title at={F('A9', -0.2)} top={70} size={52}>Elk kader past in een laag</Title>
      {LAYERS.map((l, i) => (
        <div key={l.k} style={{ position: 'absolute', left: 128, top: 190 + i * 150, width: 1000, height: 126, display: 'flex', background: C.card, border: `2px solid ${C.line}`, borderRadius: 16, overflow: 'hidden', opacity: fade(frame, F('A9', 0.3 + i * 0.2), F('A9', 0.7 + i * 0.2)) }}>
          <div style={{ width: 200, background: l.col, color: C.card, fontFamily: SANS, fontWeight: 700, fontSize: 28, letterSpacing: 2, display: 'flex', alignItems: 'center', paddingLeft: 22 }}>{l.k}</div>
          <div style={{ flex: 1, padding: '0 20px', display: 'flex', alignItems: 'center', flexWrap: 'wrap', gap: 6 }}>{rows[i]}</div>
        </div>
      ))}
      {/* rechts: wisselende toelichting */}
      <div style={{ position: 'absolute', left: 1180, top: 160, opacity: side('A11b', 'A12') }}>
        <Phone title="Frisco Installaties" sub="orderagent" h={430} style={{ position: 'relative', width: 460 }}>
          <Bubble who="me" at={F('A11b', 0.3)} frame={frame}>Koelinstallatie, 2 meter, Nickerie.</Bubble>
          <Bubble who="bot" at={F('A11b', 1.2)} frame={frame}>Order #1042 is verwerkt. ✓</Bubble>
        </Phone>
        {['Wie mag de agent aanpassen?', 'Wie zet hem uit als het misgaat?'].map((t, i) => (
          <div key={t} style={{ marginTop: 14, fontFamily: SANS, fontWeight: 700, fontSize: 28, color: LAYERS[1].col, opacity: fade(frame, F('A11b', 2.2 + i * 1.8), F('A11b', 2.6 + i * 1.8)) }}>→ {t}</div>
        ))}
      </div>
      <div style={{ position: 'absolute', left: 1180, top: 200, width: 600, opacity: side('A13', 'A13b') }}>
        <div style={{ background: C.card, border: `3px dashed ${LAYERS[3].col}`, borderRadius: 18, padding: '26px 30px', fontFamily: SANS, fontSize: 32, lineHeight: 1.35, color: C.ink }}>
          Europese klanten of data?<br /><b style={{ color: LAYERS[3].col }}>Dan kan de verordening wél gelden.</b>
        </div>
      </div>
      <div style={{ position: 'absolute', left: 1180, top: 170, width: 600, opacity: side('A13b', 'A14') }}>
        <div style={{ width: 230, height: 248 }}><Bank /></div>
        <div style={{ marginTop: 14, background: C.terra, color: C.card, fontFamily: SANS, fontWeight: 700, fontSize: 30, padding: '14px 22px', borderRadius: 14, display: 'inline-block' }}>kredietwaardigheid = hoog risico</div>
        <div style={{ fontFamily: SANS, fontSize: 24, color: C.mute, marginTop: 10 }}>in de EU: strenge eisen</div>
      </div>
      <div style={{ position: 'absolute', left: 1180, top: 190, width: 620, opacity: fade(frame, F('A14', 0), F('A14', 0.5)) }}>
        <div style={{ fontFamily: SANS, fontWeight: 700, fontSize: 26, letterSpacing: 2, color: C.green, marginBottom: 14 }}>KADERCLIPS</div>
        {weeks.map(([l, w, n], i) => (
          <div key={l} style={{ display: 'flex', alignItems: 'center', gap: 18, marginBottom: 16, opacity: fade(frame, F('A14', 0.8 + i * 0.6), F('A14', 1.2 + i * 0.6)) }}>
            <div style={{ width: 64, height: 64, borderRadius: 32, background: C.dark, color: C.amber, fontFamily: SERIF, fontWeight: 700, fontSize: 36, display: 'flex', alignItems: 'center', justifyContent: 'center' }}>{l}</div>
            <div style={{ fontFamily: SANS, fontSize: 30, color: C.ink }}><b>{w}</b> · {n}</div>
          </div>
        ))}
        <div style={{ fontFamily: SANS, fontSize: 26, color: C.mute, marginTop: 8, opacity: fade(frame, F('A14', 4.2), F('A14', 4.6)) }}>Niet uit je hoofd leren.</div>
      </div>
    </AbsoluteFill>
  );
};

/* ---------- 6. Lenzen met theorienaam ---------- */
const LENS = [
  ['Gevolgen', 'Utilitarisme', 'Baten en schade, voor iedereen die geraakt wordt', 'A16'],
  ['Rechten en plichten', 'Deontologie', 'Sommige grenzen gelden altijd', 'A17'],
  ['Rechtvaardigheid', 'Rawls', 'Eerlijke verdeling, ook voor wie het zwakst staat', 'A18'],
  ['Professionele integriteit', 'Deugdethiek en beroepscodes', 'Wat doet een goede vakman?', 'A19'],
];
const Lenses = () => {
  const frame = useCurrentFrame();
  const canvas = useSpring(F('A20', 0.2));
  const type = (s, k, o) => s.slice(0, Math.max(0, Math.floor((frame - F(k, o)) / 2)));
  return (
    <AbsoluteFill style={{ background: C.light }}>
      <Title at={F('A15', -0.2)} top={70} size={52} kicker="DE LAAG WAAROM">Elke lens heeft een naam</Title>
      {LENS.map(([lens, th, line, k], i) => {
        const flip = interpolate(frame, [F(k, 0.2), F(k, 0.9)], [0, 1], { ...clamp, easing: Easing.inOut(Easing.cubic) });
        const showBack = flip > 0.5;
        const sx = Math.abs(Math.cos(flip * Math.PI));
        const inn = useSpring(F('A15', 1.0 + i * 0.3));
        return (
          <div key={lens} style={{ position: 'absolute', left: 128 + i * 420, top: 240, width: 390, height: 360, opacity: inn, transform: `translateY(${(1 - inn) * 40}px) scaleX(${Math.max(0.02, sx)})`, background: showBack ? LAYERS[2].col : C.card, border: `2px solid ${showBack ? LAYERS[2].col : C.line}`, borderRadius: 22, padding: '30px 28px', boxShadow: '0 12px 28px rgba(18,49,42,.10)' }}>
            <div style={{ fontFamily: SANS, fontWeight: 700, fontSize: 22, letterSpacing: 2, color: showBack ? '#E9DDF0' : C.mute }}>LENS {i + 1}</div>
            <div style={{ fontFamily: SERIF, fontWeight: 700, fontSize: 38, lineHeight: 1.12, marginTop: 10, color: showBack ? C.card : C.ink }}>{lens}</div>
            {showBack && <>
              <div style={{ fontFamily: SANS, fontWeight: 700, fontSize: 30, color: C.amber, marginTop: 22 }}>{th}</div>
              <div style={{ fontFamily: SANS, fontSize: 25, lineHeight: 1.35, color: C.card, marginTop: 12 }}>{line}</div>
            </>}
          </div>
        );
      })}
      <div style={{ position: 'absolute', left: 128, top: 640, width: 1100, opacity: canvas, transform: `translateY(${(1 - canvas) * 30}px)`, background: C.card, border: `2px solid ${C.line}`, borderRadius: 16, padding: '18px 26px', fontFamily: SANS, fontSize: 28, color: C.ink, boxShadow: '0 10px 24px rgba(18,49,42,.08)' }}>
        <div style={{ fontWeight: 700, fontSize: 22, letterSpacing: 2, color: C.green }}>K5 DILEMMA-CANVAS</div>
        <div style={{ marginTop: 6 }}>Lens: <b>{type('Rechtvaardigheid', 'A20', 1.0)}</b>  ·  Theorie: <b>{type('Rawls', 'A20', 2.2)}</b></div>
      </div>
    </AbsoluteFill>
  );
};

/* ---------- 7. Samengevat ---------- */
const Summary = () => {
  const frame = useCurrentFrame();
  const drop = interpolate(frame, [F('A21b', 0.4), F('A21b', 1.4)], [0, 1], { ...clamp, easing: Easing.out(Easing.cubic) });
  const slot = interpolate(frame, [F('A21b', 3.4), F('A21b', 4.6)], [0, 1], { ...clamp, easing: Easing.inOut(Easing.cubic) });
  const landed = frame > F('A21b', 4.5);
  const comp = useSpring(F('A22', 0.2));
  const w10 = useSpring(F('A23', 0.2));
  return (
    <AbsoluteFill style={{ background: C.light }}>
      <Title at={F('A21', -0.2)} top={70} size={52}>Samengevat</Title>
      {LAYERS.map((l, i) => (
        <div key={l.k} style={{ position: 'absolute', left: 128, top: 200 + i * 150, width: 860, height: 128, borderRadius: 18, background: l.col, color: C.card, display: 'flex', alignItems: 'center', justifyContent: 'space-between', padding: '0 30px', fontFamily: SANS, fontWeight: 700, fontSize: 36, letterSpacing: 2, opacity: fade(frame, F('A21', 0.2 + i * 0.2), F('A21', 0.6 + i * 0.2)), boxShadow: landed && i === 1 ? `0 0 0 8px ${l.col}55` : 'none' }}>
          <span>{l.k}<span style={{ fontWeight: 400, fontSize: 24, letterSpacing: 0, marginLeft: 18, opacity: 0.9 }}>{l.q}</span></span>
          {landed && i === 1 && <span style={{ background: C.amber, color: C.ink, fontSize: 22, letterSpacing: 0, padding: '6px 14px', borderRadius: 10 }}>+ nieuwe norm</span>}
        </div>
      ))}
      <div style={{ position: 'absolute', left: 1080 - slot * 300, top: -140 + drop * 380 + slot * 140, opacity: drop * (1 - slot), transform: `rotate(${(1 - drop) * -10}deg) scale(${1 - slot * 0.5})`, background: C.card, border: `3px solid ${C.amber}`, borderRadius: 14, padding: '18px 26px', fontFamily: SANS, fontWeight: 700, fontSize: 32, color: C.ink, boxShadow: '0 12px 26px rgba(0,0,0,.15)' }}>
        Nieuwe norm? <span style={{ color: C.terra }}>In welke laag?</span>
      </div>
      <div style={{ position: 'absolute', left: 1080, top: 430, width: 720, opacity: comp, transform: `translateY(${(1 - comp) * 30}px)`, display: 'flex', gap: 26, alignItems: 'center' }}>
        <svg width="150" height="150" viewBox="0 0 150 150">
          <circle cx="75" cy="75" r="66" fill={C.card} stroke={C.dark} strokeWidth="8" />
          <g transform={`rotate(${20 + Math.sin(frame / 12) * 8} 75 75)`}><polygon points="75,22 88,75 75,128 62,75" fill={C.terra} /><polygon points="75,75 88,75 75,128 62,75" fill={C.dark} /></g>
          <circle cx="75" cy="75" r="8" fill={C.amber} />
        </svg>
        <div style={{ fontFamily: SANS, fontSize: 32, color: C.ink, lineHeight: 1.35 }}><b>CEET</b> en andere certificeringen:<br />een kompas, geen examenstof</div>
      </div>
      <div style={{ position: 'absolute', left: 1080, top: 640, width: 720, opacity: w10, transform: `translateY(${(1 - w10) * 30}px)`, background: C.dark, color: C.light, borderRadius: 18, padding: '22px 28px', fontFamily: SANS, fontSize: 32 }}>
        <b style={{ color: C.amber }}>Kennispakket 3</b> · verder na de minor
      </div>
    </AbsoluteFill>
  );
};

/* ---------- 8. Nu jij ---------- */
const NowA = () => (
  <AbsoluteFill style={{ background: C.light }}>
    <Pop at={F('A24', 0)} style={{ left: 128, top: 110 }}><div style={{ fontFamily: SERIF, fontWeight: 700, fontSize: 64, color: C.ink }}>Nu jij, met je groep</div></Pop>
    {['Pak jullie eigen oplossing erbij', 'Bij welke laag liggen jullie grootste vragen?', 'Schrijf er één op voor het college'].map((t, i) => (
      <Pop key={t} at={F('A24', 0.6 + i * 2.2)} style={{ left: 128, top: 270 + i * 160, width: 1664 }}>
        <div style={{ background: C.card, border: `2px solid ${C.line}`, borderRadius: 22, padding: '24px 38px', fontFamily: SANS, fontSize: 38, color: C.ink, display: 'flex', gap: 28, alignItems: 'center' }}>
          <span style={{ fontFamily: SERIF, fontWeight: 700, fontSize: 56, color: C.green }}>{i + 1}</span>{t}
        </div>
      </Pop>
    ))}
  </AbsoluteFill>
);

export const KaderA = () => (
  <Root scenes={[
    ['A0', <Intro />], ['A1', <Pile />], ['A4', <Layers />], ['A8b', <ShantiFair />], ['A9', <Frameworks />],
    ['AQ1', <QuizN n={1} q="AQ1" a="AQ1b" question="Een organisatie wil weten hoe ze AI stap voor stap bestuurt, van ontwikkeling tot gebruik. In welke laag zoek je?" options={['A. Wat', 'B. Hoe', 'C. Waarom']} good={1} note={<>B, hoe: <span style={{ color: C.amber }}>NIST, ISO/IEC 42001 en AIGP</span></>} />],
    ['A15', <Lenses />],
    ['AQ2', <QuizN n={2} q="AQ2" a="AQ2b" question="Welke theorie hoort bij de lens rechten en plichten?" options={['A. Utilitarisme', 'B. Deontologie', 'C. Deugdethiek']} good={1} note={<>Deontologie: <span style={{ color: C.amber }}>grenzen die gelden, ongeacht het nut</span></>} />],
    ['A21', <Summary />], ['A24', <NowA />],
  ]} />
);
