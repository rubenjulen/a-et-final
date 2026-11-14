import React, { useEffect, useState } from 'react';
import {
  AbsoluteFill, Audio, Sequence, staticFile, useCurrentFrame, useVideoConfig,
  interpolate, spring, Easing, delayRender, continueRender,
} from 'remotion';
import '@fontsource/source-serif-4/600.css';
import '@fontsource/source-serif-4/700.css';
import '@fontsource/public-sans/400.css';
import '@fontsource/public-sans/600.css';
import '@fontsource/public-sans/700.css';
import timing from './timing_c3.json';

const C = {
  dark: '#12312A', light: '#F6F3EC', sand: '#EDE7DA', card: '#FFFDF8',
  amber: '#E3A92B', green: '#2F6B4F', terra: '#A8432C', ink: '#1C2421', mute: '#44504B',
};
const SERIF = "'Source Serif 4', Georgia, serif";
const SANS = "'Public Sans', Arial, sans-serif";
const FPS = 30;
const cue = Object.fromEntries(timing.cues.map((c) => [c.key, c]));
const F = (key, off = 0) => Math.round((cue[key].start + off) * FPS);
const clamp = { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' };
const ease = Easing.bezier(0.33, 1, 0.68, 1);

const useSpring = (startFrame, cfg = {}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  return spring({ frame: frame - startFrame, fps, config: { damping: 18, stiffness: 120, mass: 0.9, ...cfg } });
};
const fadeIn = (frame, start, len = 15) => interpolate(frame, [start, start + len], [0, 1], clamp);

/* ---------- Shanti ---------- */
const Shanti = ({ frame, label = true }) => {
  const breathe = 1 + 0.012 * Math.sin(frame / 18);
  const blinkPhase = frame % 110;
  const eye = blinkPhase > 104 ? 0.15 : 1;
  const sway = Math.sin(frame / 25) * 2;
  return (
    <svg viewBox="0 0 560 640" width="100%" height="100%">
      <defs>
        <linearGradient id="table" x1="0" x2="0" y1="0" y2="1">
          <stop offset="0" stopColor="#D2AE87" /><stop offset="1" stopColor="#B88E66" />
        </linearGradient>
      </defs>
      {/* figure behind stall */}
      <g transform={`translate(280,${118}) scale(1,${breathe})`} style={{ transformOrigin: '280px 420px' }}>
        <path d="M-92 330 Q-92 196 0 186 Q92 196 92 330 Z" fill={C.green} />
        <path d="M-40 200 Q0 236 40 200" stroke="#25563F" strokeWidth="6" fill="none" />
        <rect x="-17" y="152" width="34" height="44" fill="#7A4A2E" />
        <circle cx="0" cy="112" r="64" fill="#7A4A2E" />
        <path d="M-66 104 Q-62 36 0 40 Q62 36 66 104 Q50 70 0 72 Q-50 70 -66 104Z" fill={C.ink} />
        <circle cx="46" cy="52" r="26" fill={C.ink} />
        <ellipse cx="-22" cy="114" rx="6.5" ry={6.5 * eye} fill={C.ink} />
        <ellipse cx="22" cy="114" rx="6.5" ry={6.5 * eye} fill={C.ink} />
        <path d="M-20 142 Q0 156 20 142" stroke={C.ink} strokeWidth="5" fill="none" strokeLinecap="round" />
        <circle cx="-38" cy="134" r="9" fill="#8E5638" opacity="0.6" />
        <circle cx="38" cy="134" r="9" fill="#8E5638" opacity="0.6" />
      </g>
      {/* awning */}
      <g transform={`translate(0,${sway * 0.3})`}>
        {[0, 1, 2, 3, 4, 5, 6].map((i) => (
          <rect key={i} x={20 + i * 74} y="300" width="74" height="58" fill={i % 2 ? C.card : C.amber} />
        ))}
        <path d="M20 358 Q57 388 94 358 Q131 388 168 358 Q205 388 242 358 Q279 388 316 358 Q353 388 390 358 Q427 388 464 358 Q501 388 538 358 L538 358 L20 358Z" fill={C.amber} />
      </g>
      <rect x="30" y="300" width="10" height="140" fill="#8A6A4A" />
      <rect x="520" y="300" width="10" height="140" fill="#8A6A4A" />
      <rect x="20" y="430" width="520" height="160" rx="12" fill="url(#table)" />
      <rect x="20" y="420" width="520" height="22" rx="4" fill="#8A6A4A" />
      <g fill={C.green}><circle cx="90" cy="410" r="27" /><circle cx="136" cy="414" r="22" /><circle cx="112" cy="392" r="18" /></g>
      <g fill={C.terra}><circle cx="420" cy="410" r="25" /><circle cx="463" cy="414" r="21" /><circle cx="441" cy="392" r="20" /></g>
      <g fill={C.amber}><ellipse cx="210" cy="412" rx="34" ry="16" /><ellipse cx="300" cy="414" rx="30" ry="14" /></g>
      {label && (
        <g transform="translate(280,0)">
          <rect x="-130" y="590" width="260" height="46" rx="23" fill={C.dark} />
          <text x="0" y="621" textAnchor="middle" fontSize="27" fontWeight="700" fill={C.light} fontFamily={SANS}>Shanti · Nickerie</text>
        </g>
      )}
    </svg>
  );
};

/* ---------- Captions ---------- */
const Captions = () => {
  const frame = useCurrentFrame();
  const t = frame / FPS;
  const cur = timing.cues.find((c) => t >= c.start - 0.1 && t <= c.start + c.dur + 0.25);
  if (!cur) return null;
  const o = interpolate(t, [cur.start - 0.1, cur.start + 0.15, cur.start + cur.dur + 0.05, cur.start + cur.dur + 0.25], [0, 1, 1, 0], clamp);
  return (
    <div style={{ position: 'absolute', left: 0, right: 0, bottom: 48, display: 'flex', justifyContent: 'center', opacity: o }}>
      <div style={{ maxWidth: 1400, background: 'rgba(18,49,42,0.86)', color: C.light, fontFamily: SANS, fontSize: 34, lineHeight: 1.35, padding: '14px 30px', borderRadius: 14, textAlign: 'center' }}>
        {cur.text}
      </div>
    </div>
  );
};

/* ---------- shared bits ---------- */
const Card = ({ style, children }) => (
  <div style={{ position: 'absolute', background: C.card, border: '2px solid #E2DACB', borderRadius: 22, padding: '30px 38px', boxShadow: '0 14px 34px rgba(18,49,42,.10)', ...style }}>{children}</div>
);
const Pop = ({ at, children, dy = 40, style = {} }) => {
  const s = useSpring(at);
  return <div style={{ position: 'absolute', opacity: s, transform: `translateY(${(1 - s) * dy}px) scale(${0.96 + 0.04 * s})`, ...style }}>{children}</div>;
};
const Chips = ({ on }) => (
  <div style={{ position: 'absolute', left: 128, top: 64, display: 'flex', gap: 14 }}>
    {['1 · Data', '2 · Label', '3 · Kenmerken', '4 · Gebruik'].map((n, i) => (
      <div key={n} style={{ fontFamily: SANS, fontSize: 24, fontWeight: 700, padding: '10px 24px', borderRadius: 999, background: i === on ? C.dark : C.sand, color: i === on ? C.amber : '#6B756F' }}>{n}</div>
    ))}
  </div>
);
const Banner = ({ at, children, top = 770 }) => (
  <Pop at={at} style={{ left: 128, top, width: 1664 }}>
    <div style={{ background: C.dark, borderRadius: 22, padding: '24px 40px', fontFamily: SERIF, fontWeight: 600, fontSize: 46, color: C.light }}>{children}</div>
  </Pop>
);

/* ---------- Scene: quiz ---------- */
const Quiz = ({ n, q, qb, a, a2, question, A, B, note, optOff = 0, C3 }) => {
  const frame = useCurrentFrame();
  const tStart = F(qb, 0) + Math.round(cue[qb].dur * FPS) + 3;
  const p = interpolate(frame, [tStart, tStart + 5 * FPS], [0, 1], clamp);
  const left = Math.ceil(5 * (1 - p));
  const ans = useSpring(F(a, 0));
  const optStyle = (good) => ({
    fontFamily: SANS, fontSize: 38, padding: '24px 34px', borderRadius: 18, width: 1250, marginTop: 20,
    background: good ? interpolateColor(ans, C.card, '#E3F0E8') : C.card,
    border: `3px solid ${good && ans > 0.5 ? C.green : '#E2DACB'}`, opacity: good ? 1 : 1 - 0.55 * ans, color: C.ink,
  });
  return (
    <AbsoluteFill style={{ background: C.light }}>
      <Pop at={F(q, 0)} style={{ left: 128, top: 110 }}><div style={{ fontFamily: SANS, fontWeight: 700, fontSize: 26, letterSpacing: 2, color: C.terra }}>TUSSENVRAAG {n}</div></Pop>
      <Pop at={F(q, 0.2)} style={{ left: 128, top: 170, width: 1560 }}><div style={{ fontFamily: SERIF, fontWeight: 600, fontSize: 60, lineHeight: 1.12, color: C.ink }}>{question}</div></Pop>
      <Pop at={F(qb, optOff)} style={{ left: 128, top: 450 }}>
        {C3 ? <div style={optStyle(false)}>{C3}</div> : null}
        <div style={optStyle(false)}>{A}</div>
        <div style={optStyle(true)}>{B}</div>
      </Pop>
      <Pop at={F(qb, optOff)} style={{ left: 1560, top: 500 }}>
        <svg width="220" height="220"><circle cx="110" cy="110" r="90" fill="none" stroke="#E2DACB" strokeWidth="18" />
          <circle cx="110" cy="110" r="90" fill="none" stroke={C.terra} strokeWidth="18" strokeLinecap="round" strokeDasharray={`${565 * (1 - p)} 1000`} transform="rotate(-90 110 110)" />
          <text x="110" y="128" textAnchor="middle" fontSize="54" fontWeight="700" fontFamily={SERIF} fill={C.dark}>{p < 1 ? left : '✓'}</text></svg>
        <div style={{ fontFamily: SANS, fontSize: 24, color: C.mute, textAlign: 'center', width: 220 }}>denktijd</div>
      </Pop>
      {note && <Banner at={F(a2 || a, 0.3)} top={740}>{note}</Banner>}
    </AbsoluteFill>
  );
};
const interpolateColor = (p, a, b) => {
  const h = (s) => [1, 3, 5].map((i) => parseInt(s.slice(i, i + 2), 16));
  const [x, y] = [h(a), h(b)];
  return `rgb(${x.map((v, i) => Math.round(v + (y[i] - v) * Math.min(1, Math.max(0, p)))).join(',')})`;
};


/* ---------- Quiz with any number of options ---------- */
const QuizN = ({ n, q, a, question, options, good, optOff = 0, note }) => {
  const frame = useCurrentFrame();
  const tStart = F(q, 0) + Math.round(cue[q].dur * FPS) + 3;
  const p = interpolate(frame, [tStart, tStart + 5 * FPS], [0, 1], clamp);
  const ans = useSpring(F(a, 0));
  return (
    <AbsoluteFill style={{ background: C.light }}>
      <Pop at={F(q, 0)} style={{ left: 128, top: 110 }}><div style={{ fontFamily: SANS, fontWeight: 700, fontSize: 26, letterSpacing: 2, color: C.terra }}>TUSSENVRAAG {n}</div></Pop>
      <Pop at={F(q, 0.3)} style={{ left: 128, top: 170, width: 1560 }}><div style={{ fontFamily: SERIF, fontWeight: 600, fontSize: 60, lineHeight: 1.12, color: C.ink }}>{question}</div></Pop>
      <Pop at={F(q, optOff)} style={{ left: 128, top: 430 }}>
        {options.map((o, i) => (
          <div key={o} style={{ fontFamily: SANS, fontSize: 38, padding: '22px 34px', borderRadius: 18, width: 1250, marginTop: 18, color: C.ink,
            background: i === good ? interpolateColor(ans, C.card, '#E3F0E8') : C.card,
            border: `3px solid ${i === good && ans > 0.5 ? C.green : '#E2DACB'}`, opacity: i === good ? 1 : 1 - 0.55 * ans }}>{o}</div>
        ))}
      </Pop>
      <Pop at={F(q, optOff)} style={{ left: 1560, top: 470 }}>
        <svg width="220" height="220"><circle cx="110" cy="110" r="90" fill="none" stroke="#E2DACB" strokeWidth="18" />
          <circle cx="110" cy="110" r="90" fill="none" stroke={C.terra} strokeWidth="18" strokeLinecap="round" strokeDasharray={`${565 * (1 - p)} 1000`} transform="rotate(-90 110 110)" />
          <text x="110" y="128" textAnchor="middle" fontSize="54" fontWeight="700" fontFamily={SERIF} fill={C.dark}>{p <= 0 ? 5 : p < 1 ? Math.ceil(5 * (1 - p)) : '✓'}</text></svg>
        <div style={{ fontFamily: SANS, fontSize: 24, color: C.mute, textAlign: 'center', width: 220 }}>denktijd</div>
      </Pop>
      {note && <Banner at={F(a, 1.0)} top={790}>{note}</Banner>}
    </AbsoluteFill>
  );
};

/* ---------- Intro ---------- */
const Intro3 = () => {
  const frame = useCurrentFrame();
  const s = useSpring(F('i0', -0.4));
  return (
    <AbsoluteFill style={{ background: `radial-gradient(1200px 800px at 75% 30%, #1B4A3E 0%, ${C.dark} 60%)` }}>
      <svg style={{ position: 'absolute', right: 150, top: 170, opacity: 0.55 * s }} width="420" height="420">
        {[0, 1, 2, 3].map((i) => <rect key={i} x={(i % 2) * 210 + 10} y={Math.floor(i / 2) * 210 + 10} width="190" height="190" rx="22" fill="none" stroke={i === 1 ? C.terra : i === 2 ? C.amber : C.green} strokeWidth="4" transform={`rotate(${Math.sin(frame / 40 + i) * 2} ${(i % 2) * 210 + 105} ${Math.floor(i / 2) * 210 + 105})`} />)}
      </svg>
      <div style={{ position: 'absolute', left: 140, top: 300, fontFamily: SANS, fontSize: 30, fontWeight: 700, letterSpacing: 3, color: C.amber, opacity: s }}>KENNISCLIP 3 · AI &amp; ETHICS · WEEK 0</div>
      <div style={{ position: 'absolute', left: 140, top: 360, fontFamily: SERIF, fontWeight: 700, fontSize: 140, lineHeight: 1.02, color: C.light, opacity: s, transform: `translateY(${(1 - s) * 50}px)` }}>Fouten tellen</div>
      <div style={{ position: 'absolute', left: 144, top: 540, fontFamily: SANS, fontSize: 40, color: '#C9D8D1', opacity: s }}>Welke fouten maakt een model, en hoe vaak?</div>
      <Pop at={F('i1', 0.3)} style={{ left: 140, top: 700, display: 'flex', gap: 22, alignItems: 'center' }}>
        {['AI maakt fouten', 'tel ze', 'wie krijgt ze?'].map((t, i) => (
          <React.Fragment key={t}>
            {i > 0 && <span style={{ fontSize: 44, color: C.amber }}>→</span>}
            <span style={{ fontFamily: SANS, fontWeight: 700, fontSize: 36, borderRadius: 999, padding: '14px 32px', background: i === 2 ? C.terra : 'rgba(246,243,236,.12)', color: C.light, opacity: interpolate(frame, [F('i1', 1 + i * 2.2), F('i1', 1.5 + i * 2.2)], [0, 1], clamp) }}>{t}</span>
          </React.Fragment>
        ))}
      </Pop>
    </AbsoluteFill>
  );
};

/* ---------- Matrix ---------- */
const MiniShanti = ({ frame, size = 150 }) => (
  <div style={{ width: size, height: size, borderRadius: '50%', overflow: 'hidden', background: C.sand, border: `4px solid ${C.card}`, boxShadow: '0 8px 20px rgba(0,0,0,.15)' }}>
    <div style={{ width: size * 2.1, height: size * 2.4, marginLeft: -size * 0.55, marginTop: -size * 0.15 }}><Shanti frame={frame} label={false} /></div>
  </div>
);
const Matrix = () => {
  const frame = useCurrentFrame();
  const at = (k, o = 0) => F(k, o);
  const vis = (k, o = 0, len = 12) => interpolate(frame, [at(k, o), at(k, o) + len], [0, 1], clamp);
  const X0 = 300, Y0 = 290, W = 360, H = 250, G = 16;
  const cells = [
    { r: 0, c: 0, k: 'v1', name: 'Terecht goedgekeurd', col: C.green, n: 50, nk: ['n2', 0.2] },
    { r: 1, c: 1, k: 'v2', name: 'Terecht afgewezen', col: C.green, n: 25, nk: ['n2', 1.6] },
    { r: 1, c: 0, k: 'v3', name: 'Onterecht goedgekeurd', col: '#B07A10', n: 15, nk: ['n2', 3.2] },
    { r: 0, c: 1, k: 'v4', name: 'Onterecht afgewezen', col: C.terra, n: 10, nk: ['n2', 4.8] },
  ];
  const grid = vis('m2', 0.3, 15);
  const heads = vis('m1', 0.4, 15);
  const colBank = vis('p1', 1.0, 15) * (1 - vis('r1', 0, 12));
  const rowApp = vis('r1', 0.8, 15) * (1 - vis('r2', 2.5, 15));
  const accGlow = vis('n3', 2.0, 12) * (1 - vis('q1', -0.5, 8));
  const shantiDim = vis('p2', 0.8, 15) * (1 - vis('r1', 0, 12));
  const pulseFN = frame > at('a1') && frame < at('p1') ? 1 + 0.04 * Math.sin((frame - at('a1')) / 4) : 1;
  return (
    <AbsoluteFill style={{ background: C.light }}>
      <Pop at={at('m1', 0)} style={{ left: 128, top: 90 }}><div style={{ fontFamily: SERIF, fontWeight: 700, fontSize: 60, color: C.ink, opacity: 1 - vis('m2', 0, 10) }}>Voorspelling naast werkelijkheid</div></Pop>
      <Pop at={at('m2', 0.2)} style={{ left: 128, top: 90 }}><div style={{ fontFamily: SERIF, fontWeight: 700, fontSize: 60, color: C.ink }}>De verwarringsmatrix</div></Pop>
      {/* headers */}
      <div style={{ position: 'absolute', left: X0, top: Y0 - 70, width: 2 * W + G, display: 'flex', gap: G, opacity: heads }}>
        {['Voorspeld: ja', 'Voorspeld: nee'].map((h, i) => <div key={h} style={{ width: W, textAlign: 'center', fontFamily: SANS, fontWeight: 700, fontSize: 30, color: i === 0 && colBank > 0.5 ? C.dark : C.mute, background: i === 0 ? `rgba(227,169,43,${0.35 * colBank})` : 'transparent', borderRadius: 12, padding: '8px 0' }}>{h}</div>)}
      </div>
      <div style={{ position: 'absolute', left: 60, top: Y0, width: 220, opacity: heads }}>
        {['Werkelijk: ja', 'Werkelijk: nee'].map((h, i) => <div key={h} style={{ height: H, marginBottom: G, display: 'flex', alignItems: 'center', fontFamily: SANS, fontWeight: 700, fontSize: 30, color: C.mute, background: i === 0 ? `rgba(227,169,43,${0.35 * rowApp})` : 'transparent', borderRadius: 12, padding: '0 14px' }}>{h}</div>)}
      </div>
      {/* bank column highlight + applicant row highlight */}
      <div style={{ position: 'absolute', left: X0 - 12, top: Y0 - 12, width: W + 24, height: 2 * H + G + 24, borderRadius: 26, border: `6px solid ${C.amber}`, opacity: colBank }} />
      <div style={{ position: 'absolute', left: X0 - 12, top: Y0 - 12, width: 2 * W + G + 24, height: H + 24, borderRadius: 26, border: `6px solid ${C.amber}`, opacity: rowApp }} />
      {cells.map((cl) => {
        const on = vis(cl.k, 0.2, 14);
        const num = Math.round(interpolate(frame, [at(...cl.nk), at(...cl.nk) + 18], [0, cl.n], clamp));
        const good = cl.col === C.green;
        const glow = good ? accGlow : 0;
        const dim = cl.k === 'v4' ? shantiDim : 0;
        return (
          <div key={cl.k} style={{ position: 'absolute', left: X0 + cl.c * (W + G), top: Y0 + cl.r * (H + G), width: W, height: H, borderRadius: 22, opacity: grid * (1 - 0.6 * dim),
            background: on > 0 ? interpolateColor(on, C.card, cl.col) : C.card, border: `3px solid ${on > 0.5 ? cl.col : '#E2DACB'}`,
            boxShadow: glow > 0 ? `0 0 0 ${8 * glow}px rgba(47,107,79,.25)` : '0 10px 24px rgba(18,49,42,.08)', transform: `scale(${cl.k === 'v4' ? pulseFN : 1})`, padding: 22, color: on > 0.5 ? C.card : C.mute }}>
            <div style={{ fontFamily: SANS, fontWeight: 700, fontSize: 28, opacity: on }}>{cl.name}</div>
            <div style={{ fontFamily: SERIF, fontWeight: 700, fontSize: 92, marginTop: 6 }}>{frame >= at(...cl.nk) ? num : (on > 0.5 ? '' : '?')}</div>
          </div>
        );
      })}
      {/* Shanti in the FN cell */}
      <div style={{ position: 'absolute', left: X0 + W + G + W - 170, top: Y0 + 80, opacity: vis('v4', 2.2, 12) * (1 - 0.7 * shantiDim), transform: `scale(${0.6 + 0.4 * useSpring(at('v4', 2.2))})` }}><MiniShanti frame={frame} size={150} /></div>
      {shantiDim > 0.05 && <div style={{ position: 'absolute', left: X0 + W + G + 30, top: Y0 + H - 60, fontFamily: SANS, fontWeight: 700, fontSize: 26, color: C.terra, opacity: shantiDim }}>onzichtbaar voor de bank</div>}
      {/* right panels */}
      <Pop at={at('n1', 0)} style={{ left: 1150, top: 230, width: 640 }}><div style={{ fontFamily: SANS, fontWeight: 700, fontSize: 34, color: C.ink, opacity: 1 - vis('p1', 0, 10) }}>100 aanvragen</div></Pop>
      <div style={{ position: 'absolute', left: 1150, top: 320, width: 640, opacity: vis('n3', 2.0, 14) * (1 - vis('q1', -0.5, 8)) }}>
        <div style={{ fontFamily: SANS, fontSize: 30, color: C.mute }}>Goed: <b style={{ color: C.green }}>50 + 25 = 75</b> van de 100</div>
        <div style={{ fontFamily: SERIF, fontWeight: 700, fontSize: 120, color: C.green, lineHeight: 1.1 }}>75%</div>
        <div style={{ fontFamily: SANS, fontWeight: 700, fontSize: 32, color: C.ink }}>accuracy</div>
        <div style={{ fontFamily: SANS, fontSize: 28, color: C.mute, marginTop: 10, opacity: vis('n3', 6.5, 12) }}>In Orange: <b>CA</b> (classification accuracy)</div>
      </div>
      <div style={{ position: 'absolute', left: 1150, top: 320, width: 640, opacity: vis('a1', 0.2, 12) * (1 - vis('p1', 0, 10)) }}>
        <div style={{ fontFamily: SERIF, fontWeight: 700, fontSize: 120, color: C.terra, lineHeight: 1.1 }}>10</div>
        <div style={{ fontFamily: SANS, fontSize: 32, color: C.ink, lineHeight: 1.35 }}>goede betalers onterecht afgewezen. Zoals Shanti.</div>
        <div style={{ fontFamily: SANS, fontSize: 28, color: C.mute, marginTop: 18, opacity: vis('a1', 5.0, 12) }}>De 15 is een andere fout: de bank lijdt verlies.</div>
      </div>
      <div style={{ position: 'absolute', left: 1150, top: 300, width: 640, opacity: vis('p1', 1.0, 14) }}>
        <div style={{ fontFamily: SANS, fontWeight: 700, fontSize: 26, letterSpacing: 2, color: '#B07A10' }}>DE BRIL VAN DE BANK</div>
        <div style={{ fontFamily: SANS, fontSize: 30, color: C.mute, marginTop: 8 }}>50 van de 65 goedkeuringen</div>
        <div style={{ fontFamily: SERIF, fontWeight: 700, fontSize: 96, color: C.dark, lineHeight: 1.1 }}>77% <span style={{ fontSize: 40 }}>precisie</span></div>
      </div>
      <div style={{ position: 'absolute', left: 1150, top: 560, width: 640, opacity: vis('r1', 0.8, 14) }}>
        <div style={{ fontFamily: SANS, fontWeight: 700, fontSize: 26, letterSpacing: 2, color: C.terra }}>DE BRIL VAN DE AANVRAGER</div>
        <div style={{ fontFamily: SANS, fontSize: 30, color: C.mute, marginTop: 8 }}>50 van de 60 goede betalers</div>
        <div style={{ fontFamily: SERIF, fontWeight: 700, fontSize: 96, color: C.dark, lineHeight: 1.1 }}>83% <span style={{ fontSize: 40 }}>recall</span></div>
      </div>
    </AbsoluteFill>
  );
};

/* ---------- Dumb model ---------- */
const Dumb = () => {
  const frame = useCurrentFrame();
  const stampN = Math.floor(interpolate(frame, [F('d1', 1.0), F('d1', 5.0)], [0, 24], clamp));
  const b1 = interpolate(frame, [F('d1', 7.0), F('d1', 8.5)], [0, 1], { ...clamp, easing: ease });
  const b2 = interpolate(frame, [F('d2', 0.2), F('d2', 1.7)], [0, 1], { ...clamp, easing: ease });
  const br = useSpring(F('d2', 3.0));
  return (
    <AbsoluteFill style={{ background: C.light }}>
      <Pop at={F('d1', 0)} style={{ left: 128, top: 90 }}><div style={{ fontFamily: SERIF, fontWeight: 700, fontSize: 60, color: C.ink }}>Vergelijk met een dom model</div></Pop>
      <Pop at={F('d1', 0.3)} style={{ left: 128, top: 210, width: 720 }}>
        <div style={{ background: C.dark, borderRadius: 24, padding: '26px 30px', color: C.light, fontFamily: SANS }}>
          <div style={{ fontWeight: 700, fontSize: 28, color: C.amber, letterSpacing: 2 }}>DOM MODEL · ZEGT ALTIJD JA</div>
          <div style={{ fontSize: 24, color: '#C9D8D1', marginTop: 6 }}>In Orange: de widget Constant</div>
          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(8, 1fr)', gap: 10, marginTop: 20 }}>
            {Array.from({ length: 24 }, (_, i) => (
              <div key={i} style={{ height: 54, borderRadius: 10, background: i < stampN ? C.green : 'rgba(246,243,236,.12)', color: C.card, fontWeight: 800, fontSize: 22, display: 'flex', alignItems: 'center', justifyContent: 'center', transform: `scale(${i === stampN - 1 ? 1.15 : 1})` }}>{i < stampN ? 'JA' : ''}</div>
            ))}
          </div>
        </div>
      </Pop>
      <div style={{ position: 'absolute', left: 1000, top: 200, width: 800, height: 600 }}>
        {[['Dom model', 59, b1, '#9FB3A9'], ['Kredietmodel', 69, b2, C.green]].map(([l, v, p, col], i) => (
          <div key={l} style={{ position: 'absolute', left: i * 300, bottom: 60, width: 220, textAlign: 'center', opacity: Math.min(1, p * 3) }}>
            <div style={{ fontFamily: SERIF, fontWeight: 700, fontSize: 56, color: C.ink }}>{Math.round(v * p)}%</div>
            <div style={{ height: v * 6 * p, background: col, borderRadius: '14px 14px 0 0' }} />
            <div style={{ fontFamily: SANS, fontSize: 30, marginTop: 10, color: C.ink }}>{l}</div>
          </div>
        ))}
        <div style={{ position: 'absolute', left: 560, top: 70, opacity: br, transform: `scale(${0.8 + 0.2 * br})` }}>
          <div style={{ fontFamily: SERIF, fontWeight: 700, fontSize: 84, color: C.terra }}>+10</div>
          <div style={{ fontFamily: SANS, fontSize: 28, color: C.ink }}>procentpunten</div>
        </div>
      </div>
      <Banner at={F('d2', 6.0)} top={790}>Vraag altijd: <span style={{ color: C.amber }}>vergeleken met wat?</span></Banner>
    </AbsoluteFill>
  );
};

/* ---------- Summary + what now ---------- */
const Summary3 = () => (
  <AbsoluteFill style={{ background: C.light }}>
    <Pop at={F('z1', 0)} style={{ left: 128, top: 110 }}><div style={{ fontFamily: SERIF, fontWeight: 700, fontSize: 68, color: C.ink }}>Samengevat</div></Pop>
    {[['Tel de fouten per soort', 0.8], ['Kijk met twee brillen: bank en aanvrager', 2.8], ['Vergelijk met het domme model', 6.2]].map(([t, o], i) => (
      <Pop key={t} at={F('z1', o)} style={{ left: 128 + i * 560, top: 280, width: 520 }}>
        <div style={{ background: C.card, border: '2px solid #E2DACB', borderRadius: 22, padding: '30px 32px', height: 260, boxShadow: '0 14px 34px rgba(18,49,42,.10)' }}>
          <div style={{ fontFamily: SERIF, fontWeight: 700, fontSize: 80, color: C.amber }}>{i + 1}</div>
          <div style={{ fontFamily: SANS, fontWeight: 700, fontSize: 34, color: C.ink, lineHeight: 1.25 }}>{t}</div>
        </div>
      </Pop>
    ))}
    <Banner at={F('z2', 0.5)} top={640}>Welke fout zwaarder telt, is <span style={{ color: C.amber }}>een ethische keuze</span>, geen rekensom.</Banner>
  </AbsoluteFill>
);
const WhatNow3 = () => (
  <AbsoluteFill style={{ background: C.light }}>
    <Pop at={F('e1', 0)} style={{ left: 128, top: 110 }}><div style={{ fontFamily: SERIF, fontWeight: 700, fontSize: 68, color: C.ink }}>Nu jij: practicum 1</div></Pop>
    {[['e1', 0.6, 'Maak de verwarringsmatrix van een echt model, met de Suribank-gegevens'], ['e1', 5.5, 'Bereken precisie en recall, en vergelijk met Constant'], ['e2', 0.3, 'Schrijf op evidence card 1 welke fout jij erger vindt, en waarom']].map(([k, o, t], i) => (
      <Pop key={t} at={F(k, o)} style={{ left: 128, top: 270 + i * 170, width: 1664 }}>
        <div style={{ background: C.card, border: '2px solid #E2DACB', borderRadius: 22, padding: '26px 38px', fontFamily: SANS, fontSize: 38, color: C.ink, display: 'flex', gap: 28, alignItems: 'center' }}>
          <span style={{ fontFamily: SERIF, fontWeight: 700, fontSize: 56, color: C.green }}>{i + 1}</span>{t}
        </div>
      </Pop>
    ))}
    <Pop at={F('e2', 4.0)} style={{ left: 128, top: 800 }}><div style={{ fontFamily: SANS, fontWeight: 700, fontSize: 34, color: C.green }}>In Orange of in Python · daarna clip 4</div></Pop>
  </AbsoluteFill>
);

/* ---------- Composition ---------- */
const Fade = ({ from, to, children }) => {
  const frame = useCurrentFrame();
  if (frame < from - 10 || frame > to + 10) return null;
  const o = interpolate(frame, [from - 8, from + 8, to - 8, to + 8], [0, 1, 1, 0], clamp);
  return <AbsoluteFill style={{ opacity: o }}>{children}</AbsoluteFill>;
};
export const Clip3 = () => {
  const [handle] = useState(() => delayRender('fonts'));
  useEffect(() => { document.fonts.ready.then(() => continueRender(handle)); }, [handle]);
  const end = Math.ceil(timing.total * FPS);
  const scenes = [
    ['i0', <Intro3 />], ['m1', <Matrix />],
    ['q1', <QuizN n={1} q="q1" a="a1" optOff={3.2} question="Hoeveel goede betalers worden onterecht afgewezen?" options={['A. 10', 'B. 15', 'C. 25']} good={0} />],
    ['a1', <Matrix />], ['d1', <Dumb />],
    ['q2', <QuizN n={2} q="q2" a="a2" optOff={6.0} question="Een model haalt 62%, terwijl 59% terugbetaalt. Wat zeg je?" options={['A. Uitstekend model', 'B. Nauwelijks beter dan altijd ja zeggen']} good={1} note={<>Maar <span style={{ color: C.amber }}>3 procentpunten</span> beter dan niets doen.</>} />],
    ['z1', <Summary3 />], ['e1', <WhatNow3 />],
  ];
  return (
    <AbsoluteFill style={{ background: C.light }}>
      {scenes.map(([k, el], i) => {
        const from = i === 0 ? 0 : F(k, -0.4);
        const to = i + 1 < scenes.length ? F(scenes[i + 1][0], -0.4) : end + 20;
        return <Fade key={k + i} from={from} to={to}>{el}</Fade>;
      })}
      <Captions />
      {timing.cues.map((c) => (
        <Sequence key={c.key} from={Math.round(c.start * FPS)} durationInFrames={Math.ceil((c.dur + 0.2) * FPS)}>
          <Audio src={staticFile(`${timing.audioDir}/${c.key}.mp3`)} />
        </Sequence>
      ))}
    </AbsoluteFill>
  );
};
