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
import timing from './timing_c4.json';

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

/* ---------- phone + chat ---------- */
const Bubble = ({ who, at, children, frame, stamp }) => {
  const s = spring({ frame: frame - at, fps: FPS, config: { damping: 16, stiffness: 140 } });
  const me = who === 'me';
  const typing = frame >= at - 18 && frame < at && !me;
  return (
    <div style={{ display: 'flex', justifyContent: me ? 'flex-end' : 'flex-start', marginTop: 14 }}>
      {typing ? (
        <div style={{ background: '#E6EEEA', borderRadius: 18, padding: '14px 20px', display: 'flex', gap: 6 }}>
          {[0, 1, 2].map((i) => <div key={i} style={{ width: 10, height: 10, borderRadius: 5, background: C.green, opacity: 0.4 + 0.6 * Math.abs(Math.sin((frame + i * 5) / 5)) }} />)}
        </div>
      ) : (
        <div style={{ position: 'relative', maxWidth: 420, background: me ? C.green : '#E6EEEA', color: me ? C.card : C.ink, borderRadius: me ? '20px 20px 6px 20px' : '20px 20px 20px 6px', padding: '14px 20px', fontFamily: SANS, fontSize: 25, lineHeight: 1.35, opacity: s, transform: `translateY(${(1 - s) * 16}px) scale(${0.9 + 0.1 * s})`, transformOrigin: me ? 'right bottom' : 'left bottom' }}>
          {children}
          {stamp}
        </div>
      )}
    </div>
  );
};
const Phone = ({ title, sub, children, style = {}, banner, h = 760 }) => (
  <div style={{ position: 'absolute', width: 540, height: h, borderRadius: 54, background: C.dark, padding: 16, boxShadow: '0 30px 60px rgba(18,49,42,.28)', ...style }}>
    <div style={{ width: '100%', height: '100%', borderRadius: 40, background: C.card, overflow: 'hidden', display: 'flex', flexDirection: 'column' }}>
      <div style={{ background: '#F0EBE1', padding: '28px 26px 16px', borderBottom: '2px solid #E2DACB' }}>
        <div style={{ fontFamily: SANS, fontWeight: 700, fontSize: 26, color: C.ink }}>{title}</div>
        <div style={{ fontFamily: SANS, fontSize: 20, color: C.mute }}>{sub}</div>
      </div>
      {banner}
      <div style={{ padding: '6px 22px', flex: 1 }}>{children}</div>
    </div>
  </div>
);
const QChips = ({ on, at }) => {
  const frame = useCurrentFrame();
  return (
    <div style={{ position: 'absolute', left: 128, top: 64, display: 'flex', gap: 14, opacity: interpolate(frame, [at, at + 12], [0, 1], clamp) }}>
      {['1 · Overtuigend fout?', '2 · Waar gaan de gegevens?', '3 · Weet je dat het AI is?', '4 · Iedereen even goed?'].map((n, i) => (
        <div key={n} style={{ fontFamily: SANS, fontSize: 22, fontWeight: 700, padding: '10px 22px', borderRadius: 999, background: i === on ? C.dark : C.sand, color: i === on ? C.amber : '#6B756F' }}>{n}</div>
      ))}
    </div>
  );
};

/* ---------- Intro ---------- */
const Intro4 = () => {
  const frame = useCurrentFrame();
  const s = useSpring(F('i0', -0.4));
  const a = useSpring(F('i1', 3.0)), b = useSpring(F('i1', 5.5));
  return (
    <AbsoluteFill style={{ background: `radial-gradient(1200px 800px at 75% 30%, #1B4A3E 0%, ${C.dark} 60%)` }}>
      <div style={{ position: 'absolute', left: 140, top: 250, fontFamily: SANS, fontSize: 30, fontWeight: 700, letterSpacing: 3, color: C.amber, opacity: s }}>KENNISCLIP 4 · AI &amp; ETHICS · WEEK 0</div>
      <div style={{ position: 'absolute', left: 140, top: 310, width: 1000, fontFamily: SERIF, fontWeight: 700, fontSize: 116, lineHeight: 1.04, color: C.light, opacity: s, transform: `translateY(${(1 - s) * 50}px)` }}>Wat is anders bij generatieve AI?</div>
      <div style={{ position: 'absolute', left: 1240, top: 280, width: 520, opacity: a, transform: `translateY(${(1 - a) * 30}px)` }}>
        <div style={{ fontFamily: SANS, fontWeight: 700, fontSize: 24, color: '#C9D8D1', letterSpacing: 2 }}>VOORSPELLEND</div>
        <div style={{ background: 'rgba(246,243,236,.1)', borderRadius: 20, padding: '20px 28px', marginTop: 10, fontFamily: SERIF, fontWeight: 700, fontSize: 70, color: C.light }}>72% <span style={{ fontFamily: SANS, fontSize: 26, fontWeight: 400, color: '#C9D8D1' }}>kans op terugbetalen</span></div>
      </div>
      <div style={{ position: 'absolute', left: 1240, top: 560, width: 520, opacity: b, transform: `translateY(${(1 - b) * 30}px)` }}>
        <div style={{ fontFamily: SANS, fontWeight: 700, fontSize: 24, color: C.amber, letterSpacing: 2 }}>GENERATIEF</div>
        <div style={{ background: C.card, borderRadius: '22px 22px 22px 6px', padding: '18px 24px', marginTop: 10, fontFamily: SANS, fontSize: 28, color: C.ink, lineHeight: 1.35 }}>Natuurlijk! Uw bestelling staat klaar. Wilt u ook een onderhoudscontract?</div>
      </div>
    </AbsoluteFill>
  );
};

/* ---------- Chat: order + confident error ---------- */
const OrderChat = () => {
  const frame = useCurrentFrame();
  const order = useSpring(F('c2', 0.8));
  const wrong = spring({ frame: frame - F('v1b', 4.2), fps: FPS, config: { damping: 10, stiffness: 200 } });
  const showLater = frame > F('v1b', -0.2);
  return (
    <AbsoluteFill style={{ background: C.light }}>
      <QChips on={frame > F('v1', 0) ? 0 : -1} at={F('c2', 3.0)} />
      <div style={{ position: 'absolute', left: 110, top: 330, width: 420, height: 500 }}><Shanti frame={frame} /></div>
      <Phone title="Frisco Installaties" sub="online · meestal direct antwoord" style={{ left: 640, top: 140 }} h={760}>
        <Bubble who="me" at={F('c1', 0.6)} frame={frame}>Goedemiddag, ik wil een koelinstallatie voor mijn marktkraam in Nickerie.</Bubble>
        <Bubble who="bot" at={F('c1', 3.0)} frame={frame}>Prima! Welke lengte heeft uw kraam?</Bubble>
        <Bubble who="me" at={F('c1', 4.6)} frame={frame}>Ongeveer 2 meter.</Bubble>
        {showLater && <Bubble who="me" at={F('v1b', 0.3)} frame={frame}>Wanneer is het klaar?</Bubble>}
        {showLater && (
          <Bubble who="bot" at={F('v1b', 2.4)} frame={frame} stamp={
            <div style={{ position: 'absolute', right: -30, bottom: -34, border: `5px solid ${C.terra}`, color: C.terra, fontWeight: 800, fontSize: 22, padding: '2px 12px', background: C.card, transform: `rotate(-8deg) scale(${2 - Math.min(1, wrong)})`, opacity: Math.min(1, wrong) }}>NIET AFGESPROKEN</div>}>
            Morgen al! En plaatsen is gratis. ✓
          </Bubble>
        )}
      </Phone>
      <div style={{ position: 'absolute', left: 1260, top: 250, width: 540, opacity: order * (1 - interpolate(frame, [F('v1', 0), F('v1', 0.6)], [0, 1], clamp)), transform: `translateX(${(1 - order) * 80}px)` }}>
        <div style={{ fontFamily: SANS, fontWeight: 700, fontSize: 24, letterSpacing: 2, color: C.green }}>GESPREK → BESTELLING</div>
        <div style={{ background: C.card, border: '2px solid #E2DACB', borderRadius: 22, padding: '26px 30px', marginTop: 12, fontFamily: SANS, fontSize: 28, lineHeight: 1.6, color: C.ink, boxShadow: '0 14px 34px rgba(18,49,42,.10)' }}>
          <b>Order #1042</b><br />Koelinstallatie · 2 meter<br />Plaats: marktkraam, Nickerie<br />Klant: Shanti
        </div>
      </div>
      <Pop at={F('v1', 0.4)} style={{ left: 1260, top: 260, width: 540 }}>
        <div style={{ fontFamily: SERIF, fontWeight: 700, fontSize: 56, color: C.ink, lineHeight: 1.1 }}>Kan het overtuigend fout zijn?</div>
        <div style={{ fontFamily: SANS, fontSize: 30, color: C.mute, marginTop: 18, lineHeight: 1.4 }}>Een taalmodel weet niet wat waar is. Het klinkt alleen zo.</div>
      </Pop>
    </AbsoluteFill>
  );
};

/* ---------- Data ---------- */
const DataFlow = () => {
  const frame = useCurrentFrame();
  const items = [['Naam', 'Shanti R.', 'v2', 3.2], ['Adres', 'Markt, Nickerie', 'v2', 4.0], ['Telefoon', '+597 …', 'v2', 4.8], ['Borstomvang', '92 cm', 'v2b', 0.8], ['Taille', '78 cm', 'v2b', 1.4], ['Schouderbreedte', '41 cm', 'v2b', 2.0]];
  const cloud = useSpring(F('v2', 5.5));
  return (
    <AbsoluteFill style={{ background: C.light }}>
      <QChips on={1} at={F('v2', -0.3)} />
      <Pop at={F('v2', 0)} style={{ left: 128, top: 140 }}><div style={{ fontFamily: SERIF, fontWeight: 700, fontSize: 60, color: C.ink }}>Waar gaan de gegevens heen?</div></Pop>
      {items.map(([l, v, k, o], i) => {
        const appear = spring({ frame: frame - F(k, o), fps: FPS, config: { damping: 16 } });
        const travel = interpolate(frame, [F(k, o + 3.0), F(k, o + 4.8)], [0, 1], { ...clamp, easing: Easing.inOut(Easing.cubic) });
        const x = 128 + travel * 1040, y = 290 + i * 92 - travel * (i * 92 - 180);
        const isBody = k === 'v2b';
        return (
          <div key={l} style={{ position: 'absolute', left: x, top: y, opacity: appear * (1 - 0.85 * travel), transform: `scale(${1 - 0.5 * travel})`, transformOrigin: 'left center', background: isBody ? '#F6E7C8' : C.card, border: `2px solid ${isBody ? C.amber : '#E2DACB'}`, borderRadius: 14, padding: '12px 22px', fontFamily: SANS, fontSize: 28, color: C.ink, width: 470 }}>
            <span style={{ color: C.mute }}>{l}:</span> <b>{v}</b>
          </div>
        );
      })}
      <Pop at={F('v2b', 0)} style={{ left: 640, top: 600 }}><div style={{ fontFamily: SANS, fontWeight: 700, fontSize: 26, color: '#B07A10', letterSpacing: 2 }}>BIJ MAATKLEDING</div></Pop>
      <div style={{ position: 'absolute', left: 1180, top: 300, width: 600, opacity: cloud, transform: `scale(${0.85 + 0.15 * cloud})` }}>
        <svg width="600" height="330" viewBox="0 0 600 330">
          <path d="M150 280 Q60 280 60 210 Q60 140 140 135 Q150 60 240 60 Q300 20 370 60 Q470 50 480 140 Q560 150 550 220 Q540 280 460 280 Z" fill={C.dark} />
          <text x="300" y="185" textAnchor="middle" fontFamily={SANS} fontWeight="700" fontSize="34" fill={C.amber}>externe dienst</text>
          <text x="300" y="228" textAnchor="middle" fontFamily={SANS} fontSize="26" fill="#C9D8D1">vaak in het buitenland</text>
        </svg>
        {['Bewaard?', 'Gebruikt om te trainen?', 'Wie kan het lezen?'].map((q, i) => (
          <div key={q} style={{ fontFamily: SANS, fontWeight: 700, fontSize: 30, color: C.terra, marginTop: 10, opacity: interpolate(frame, [F('v2b', 3.6 + i * 1.3), F('v2b', 4.0 + i * 1.3)], [0, 1], clamp) }}>{q}</div>
        ))}
      </div>
    </AbsoluteFill>
  );
};

/* ---------- AI notice ---------- */
const Notice = () => {
  const frame = useCurrentFrame();
  const good = useSpring(F('v3b', 0.3));
  return (
    <AbsoluteFill style={{ background: C.light }}>
      <QChips on={2} at={F('v3', -0.3)} />
      <Pop at={F('v3', 0)} style={{ left: 128, top: 140 }}><div style={{ fontFamily: SERIF, fontWeight: 700, fontSize: 60, color: C.ink }}>Weet de gebruiker dat het AI is?</div></Pop>
      <Phone title="Frisco Installaties" h={690} sub="Sandra · klantenservice" style={{ left: 160, top: 250, transform: 'scale(0.85)', transformOrigin: 'top left' }}>
        <Bubble who="bot" at={F('v3', 0.8)} frame={frame}>Hoi! Ik ben Sandra. Waarmee kan ik u helpen?</Bubble>
        <Bubble who="me" at={F('v3', 2.4)} frame={frame}>Fijn dat ik een mens spreek!</Bubble>
      </Phone>
      <Pop at={F('v3', 3.0)} style={{ left: 660, top: 430 }}><div style={{ fontFamily: SANS, fontWeight: 700, fontSize: 26, color: C.terra }}>✗ Geen melding</div></Pop>
      <Phone title="Frisco Installaties" h={690} sub="digitale assistent" style={{ left: 1060, top: 250, transform: `scale(0.85) translateY(${(1 - good) * 60}px)`, transformOrigin: 'top left', opacity: good }}
        banner={<div style={{ background: '#F6E7C8', padding: '12px 22px', fontFamily: SANS, fontSize: 21, color: C.ink, borderBottom: `2px solid ${C.amber}` }}>🤖 Je praat met een <b>digitale assistent (AI)</b>. Ik kan fouten maken. Typ <b>‘medewerker’</b> om een mens te spreken.</div>}>
        <Bubble who="me" at={F('v3b', 2.2)} frame={frame}>medewerker</Bubble>
        <Bubble who="bot" at={F('v3b', 3.6)} frame={frame}>Ik verbind u door met een collega. Uw gesprek gaat mee.</Bubble>
      </Phone>
      <div style={{ position: 'absolute', left: 1580, top: 360, width: 300 }}>
        {['Zegt dat het AI is', 'Zegt wat het kan', 'Een mens is bereikbaar'].map((t, i) => (
          <div key={t} style={{ fontFamily: SANS, fontWeight: 700, fontSize: 26, color: C.green, marginBottom: 26, opacity: interpolate(frame, [F('v3b', 1.0 + i * 1.6), F('v3b', 1.4 + i * 1.6)], [0, 1], clamp) }}>✓ {t}</div>
        ))}
      </div>
    </AbsoluteFill>
  );
};

/* ---------- Bias: language ---------- */
const Language = () => {
  const frame = useCurrentFrame();
  return (
    <AbsoluteFill style={{ background: C.light }}>
      <QChips on={3} at={F('v4', -0.3)} />
      <Pop at={F('v4', 0)} style={{ left: 128, top: 140 }}><div style={{ fontFamily: SERIF, fontWeight: 700, fontSize: 60, color: C.ink }}>Helpt het iedereen even goed?</div></Pop>
      <Phone title="Frisco Installaties" h={690} sub="getypt, in het Nederlands" style={{ left: 200, top: 250, transform: 'scale(0.85)', transformOrigin: 'top left' }}>
        <Bubble who="me" at={F('v4', 2.0)} frame={frame}>Ik wil een koelinstallatie voor mijn kraam. Wanneer kan dat?</Bubble>
        <Bubble who="bot" at={F('v4', 3.3)} frame={frame}>Graag! Een monteur kan volgende week komen. Ik stuur u een offerte met de prijs en de mogelijke dagen.</Bubble>
      </Phone>
      <Phone title="Frisco Installaties" h={690} sub="ingesproken, in het Sranantongo" style={{ left: 1020, top: 250, transform: 'scale(0.85)', transformOrigin: 'top left' }}>
        <Bubble who="me" at={F('v4', 5.2)} frame={frame}>
          <div style={{ display: 'flex', alignItems: 'center', gap: 14 }}>
            <span style={{ fontSize: 30 }}>▶</span>
            <div style={{ display: 'flex', alignItems: 'center', gap: 4, height: 40 }}>
              {[14, 26, 34, 20, 38, 28, 16, 30, 36, 22, 12, 26, 32, 18, 10].map((h, i) => (
                <div key={i} style={{ width: 6, borderRadius: 3, background: C.card, height: h * (0.55 + 0.45 * Math.abs(Math.sin((frame + i * 7) / 9))) }} />
              ))}
            </div>
            <span style={{ fontSize: 22 }}>0:07</span>
          </div>
        </Bubble>
        <div style={{ margin: '10px 0 0 auto', maxWidth: 420, fontFamily: SANS, fontSize: 21, color: '#5C6862', fontStyle: 'italic', opacity: interpolate(frame, [F('v4', 8.6), F('v4', 9.2)], [0, 1], clamp) }}>
          Omgezet naar tekst: “▮▮▮ koel ▮▮▮ installatie ▮▮▮ ▮▮▮?”
        </div>
        <Bubble who="bot" at={F('v4', 11.6)} frame={frame}>Sorry, ik begrijp uw vraag niet.</Bubble>
      </Phone>
      <Banner at={F('v4b', 4.6)} top={800}>Spraak in jullie oplossing? Test het in <span style={{ color: C.amber }}>practicum 4</span>.</Banner>
    </AbsoluteFill>
  );
};

/* ---------- Summary + now ---------- */
const Summary4 = () => (
  <AbsoluteFill style={{ background: C.light }}>
    <Pop at={F('z1', 0)} style={{ left: 128, top: 110 }}><div style={{ fontFamily: SERIF, fontWeight: 700, fontSize: 64, color: C.ink }}>Vier vragen bij generatieve AI</div></Pop>
    {['Kan het overtuigend fout zijn?', 'Waar gaan de gegevens heen?', 'Weet de gebruiker dat het AI is?', 'Helpt het iedereen even goed?'].map((t, i) => (
      <Pop key={t} at={F('z1', 2.6 + i * 2.4)} style={{ left: 128 + (i % 2) * 840, top: 280 + Math.floor(i / 2) * 260, width: 800 }}>
        <div style={{ background: C.card, border: '2px solid #E2DACB', borderRadius: 22, padding: '28px 34px', display: 'flex', gap: 26, alignItems: 'center', boxShadow: '0 14px 34px rgba(18,49,42,.10)' }}>
          <span style={{ fontFamily: SERIF, fontWeight: 700, fontSize: 80, color: C.amber }}>{i + 1}</span>
          <span style={{ fontFamily: SANS, fontWeight: 700, fontSize: 36, color: C.ink }}>{t}</span>
        </div>
      </Pop>
    ))}
  </AbsoluteFill>
);
const Now4 = () => (
  <AbsoluteFill style={{ background: C.light }}>
    <Pop at={F('e1', 0)} style={{ left: 128, top: 110 }}><div style={{ fontFamily: SERIF, fontWeight: 700, fontSize: 64, color: C.ink }}>Nu jij, met je groep</div></Pop>
    {[['e1', 0.4, 'Pak jullie eigen oplossing erbij'], ['e1', 3.0, 'Welke van de vier vragen spelen bij jullie?'], ['e1', 5.6, 'Schrijf bij elke vraag één voorbeeld op']].map(([k, o, t], i) => (
      <Pop key={t} at={F(k, o)} style={{ left: 128, top: 270 + i * 160, width: 1664 }}>
        <div style={{ background: C.card, border: '2px solid #E2DACB', borderRadius: 22, padding: '24px 38px', fontFamily: SANS, fontSize: 38, color: C.ink, display: 'flex', gap: 28, alignItems: 'center' }}>
          <span style={{ fontFamily: SERIF, fontWeight: 700, fontSize: 56, color: C.green }}>{i + 1}</span>{t}
        </div>
      </Pop>
    ))}
    <Pop at={F('e2', 0.3)} style={{ left: 128, top: 790 }}><div style={{ fontFamily: SANS, fontWeight: 700, fontSize: 32, color: C.green }}>Opdracht in week 0: “De eigen oplossing klaarzetten” · verder in week 1</div></Pop>
  </AbsoluteFill>
);

/* ---------- Composition ---------- */
const Fade = ({ from, to, children }) => {
  const frame = useCurrentFrame();
  if (frame < from - 10 || frame > to + 10) return null;
  const o = interpolate(frame, [from - 8, from + 8, to - 8, to + 8], [0, 1, 1, 0], clamp);
  return <AbsoluteFill style={{ opacity: o }}>{children}</AbsoluteFill>;
};
export const Clip4 = () => {
  const [handle] = useState(() => delayRender('fonts'));
  useEffect(() => { document.fonts.ready.then(() => continueRender(handle)); }, [handle]);
  const end = Math.ceil(timing.total * FPS);
  const scenes = [
    ['i0', <Intro4 />], ['c1', <OrderChat />],
    ['q1', <QuizN n={1} q="q1" a="a1" optOff={5.5} question="De chatbot gaf een verkeerd antwoord. Wie is verantwoordelijk?" options={['A. Het taalmodel', 'B. Het bedrijf dat de chatbot inzet']} good={1} note={<>Een model kan geen verantwoordelijkheid dragen. <span style={{ color: C.amber }}>Het bedrijf wel.</span></>} />],
    ['v2', <DataFlow />], ['v3', <Notice />], ['v4', <Language />], ['z1', <Summary4 />], ['e1', <Now4 />],
  ];
  return (
    <AbsoluteFill style={{ background: C.light }}>
      {scenes.map(([k, el], i) => {
        const from = i === 0 ? 0 : F(k, -0.4);
        const to = i + 1 < scenes.length ? F(scenes[i + 1][0], -0.4) : end + 20;
        return <Fade key={k + i} from={from} to={to}>{el}</Fade>;
      })}
      <Captions />
      {timing.cues.filter((c) => c.audio).map((c) => (
        <Sequence key={c.key} from={Math.round(c.start * FPS)} durationInFrames={Math.ceil((c.dur + 0.2) * FPS)}>
          <Audio src={staticFile(`${timing.audioDir}/${c.key}.mp3`)} />
        </Sequence>
      ))}
    </AbsoluteFill>
  );
};
