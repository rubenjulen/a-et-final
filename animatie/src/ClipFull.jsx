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
import timing from './timing_full.json';

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

/* ---------- Bank ---------- */
const Bank = () => (
  <svg viewBox="0 0 400 430" width="100%" height="100%">
    <polygon points="200,10 392,112 8,112" fill={C.dark} />
    <rect x="28" y="112" width="344" height="24" fill={C.green} />
    <g fill={C.sand}>{[55, 135, 231, 311].map((x) => <rect key={x} x={x} y="142" width="34" height="198" rx="4" />)}</g>
    <rect x="18" y="340" width="364" height="30" fill={C.dark} />
    <text x="200" y="412" textAnchor="middle" fontSize="42" fontWeight="700" fill={C.dark} fontFamily={SANS}>Suribank</text>
  </svg>
);

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

/* ---------- Scene: intro ---------- */
const Intro = () => {
  const frame = useCurrentFrame();
  const s = useSpring(F('i0', -0.4));
  const s2 = useSpring(F('i0', 0.6));
  return (
    <AbsoluteFill style={{ background: `radial-gradient(1200px 800px at 75% 30%, #1B4A3E 0%, ${C.dark} 60%)` }}>
      {[0, 1, 2].map((i) => (
        <div key={i} style={{ position: 'absolute', right: 160 + i * 90, top: 160 + i * 120, width: 260 - i * 60, height: 260 - i * 60, borderRadius: '50%', border: `3px solid ${i === 1 ? C.amber : '#2F6B4F'}`, opacity: 0.5 * s, transform: `scale(${0.6 + 0.4 * s}) rotate(${frame / 3}deg)` }} />
      ))}
      <div style={{ position: 'absolute', left: 140, top: 300, fontFamily: SANS, fontSize: 30, fontWeight: 700, letterSpacing: 3, color: C.amber, opacity: s, transform: `translateY(${(1 - s) * 30}px)` }}>
        KENNISCLIP 2 · AI &amp; ETHICS · WEEK 0
      </div>
      <div style={{ position: 'absolute', left: 140, top: 360, fontFamily: SERIF, fontWeight: 700, fontSize: 130, lineHeight: 1.02, color: C.light, opacity: s, transform: `translateY(${(1 - s) * 50}px)` }}>
        Waarom maakt<br />AI fouten?
      </div>
      <div style={{ position: 'absolute', left: 144, top: 670, fontFamily: SANS, fontSize: 40, color: '#C9D8D1', opacity: s2, transform: `translateX(${(1 - s2) * -40}px)` }}>
        Een verhaal over Shanti
      </div>
      <IntroExtra />
    </AbsoluteFill>
  );
};

/* ---------- Scene: market, bank, model ---------- */
const Market = () => {
  const frame = useCurrentFrame();
  // camera: start zoomed on Shanti, pull back when the bank appears
  const zoom = interpolate(frame, [F('s0'), F('s2', 0.2), F('s2', 1.6)], [1.35, 1.35, 1], { ...clamp, easing: ease });
  const panX = interpolate(frame, [F('s2', 0.2), F('s2', 1.6)], [420, 0], { ...clamp, easing: ease });
  const shIn = useSpring(F('s0', -0.3), { damping: 16 });
  const formIn = useSpring(F('s1', 0.1));
  const bankIn = useSpring(F('s2', 0.3), { damping: 15 });
  const modelIn = useSpring(F('s3', 0.2), { damping: 15 });
  // form flight: from beside Shanti to the bank door, then down into the model
  const fly = interpolate(frame, [F('s2', 1.2), F('s2', 2.4)], [0, 1], { ...clamp, easing: Easing.inOut(Easing.cubic) });
  const drop = interpolate(frame, [F('s3', 1.0), F('s3', 2.0)], [0, 1], { ...clamp, easing: Easing.inOut(Easing.cubic) });
  const fx = 650 + fly * 820 + drop * 20;
  const fy = 340 - Math.sin(fly * Math.PI) * 160 + fly * 40 + drop * 360;
  const fScale = 1 - 0.55 * fly - 0.1 * drop;
  const fOpacity = formIn * interpolate(frame, [F('s3', 1.8), F('s3', 2.2)], [1, 0], clamp);
  // scanning bar in the model
  const scan = ((frame - F('s3')) % 45) / 45;
  const scanOn = frame > F('s3', 1.6) ? 1 : 0;
  // accuracy ring
  const ringP = interpolate(frame, [F('s4', 0.3), F('s4', 2.6)], [0, 1], { ...clamp, easing: ease });
  const ringIn = useSpring(F('s4', 0));
  const R = 100, CIRC = 2 * Math.PI * R;
  return (
    <AbsoluteFill style={{ background: `linear-gradient(180deg, ${C.light} 0%, #EFE9DD 100%)` }}>
      <AbsoluteFill style={{ transform: `translate(${panX}px, ${-170 * (zoom - 1) / 0.35}px) scale(${zoom})`, transformOrigin: '430px 620px' }}>
        <div style={{ position: 'absolute', left: 150, top: 300, width: 560, height: 640, transform: `translateY(${(1 - shIn) * 80}px)`, opacity: shIn }}>
          <Shanti frame={frame} />
        </div>
        {/* bank */}
        <div style={{ position: 'absolute', left: 1400, top: 200, width: 400, height: 430, opacity: bankIn, transform: `translateX(${(1 - bankIn) * 200}px)` }}>
          <Bank />
        </div>
        {/* model box */}
        <div style={{ position: 'absolute', left: 1385, top: 680, width: 430, height: 170, borderRadius: 24, background: C.dark, opacity: modelIn, transform: `scale(${0.8 + 0.2 * modelIn})`, overflow: 'hidden', boxShadow: '0 20px 40px rgba(18,49,42,.25)' }}>
          <div style={{ fontFamily: SANS, fontSize: 30, fontWeight: 700, letterSpacing: 2, color: C.amber, textAlign: 'center', marginTop: 38 }}>COMPUTERMODEL</div>
          <div style={{ fontFamily: SANS, fontSize: 25, color: '#C9D8D1', textAlign: 'center', marginTop: 8 }}>beoordeelt elke aanvraag</div>
          <div style={{ position: 'absolute', left: 0, top: 0, bottom: 0, width: 120, transform: `translateX(${scan * 560 - 120}px)`, background: 'linear-gradient(90deg, rgba(227,169,43,0) 0%, rgba(227,169,43,.35) 50%, rgba(227,169,43,0) 100%)', opacity: scanOn }} />
        </div>
        {/* dashed path */}
        <svg style={{ position: 'absolute', left: 0, top: 0 }} width="1920" height="1080">
          <path d="M 860 420 Q 1150 200 1420 410" fill="none" stroke={C.green} strokeWidth="5" strokeDasharray="14 12"
            strokeDashoffset={-frame * 1.5} opacity={interpolate(frame, [F('s2', 0.8), F('s2', 1.2), F('s3', 2.2), F('s3', 2.6)], [0, 0.8, 0.8, 0], clamp)} />
        </svg>
        {/* application form */}
        <div style={{ position: 'absolute', left: fx, top: fy, width: 400, padding: '30px 36px', background: C.card, borderRadius: 22, border: `2px solid #E2DACB`, boxShadow: '0 16px 36px rgba(18,49,42,.14)', transform: `scale(${fScale * (0.7 + 0.3 * formIn)}) rotate(${(1 - formIn) * -6 + fly * 4}deg)`, transformOrigin: 'top left', opacity: fOpacity }}>
          <div style={{ fontFamily: SANS, fontSize: 21, fontWeight: 700, letterSpacing: 2, color: C.terra }}>AANVRAAG LENING</div>
          <div style={{ fontFamily: SERIF, fontWeight: 700, fontSize: 56, color: C.ink, marginTop: 8 }}>SRD 40.000</div>
          <div style={{ fontFamily: SANS, fontSize: 27, color: C.mute, marginTop: 6 }}>Eigen kraam met koeling</div>
        </div>
        {/* accuracy ring */}
        <div style={{ position: 'absolute', left: 760, top: 650, display: 'flex', alignItems: 'center', gap: 34, opacity: ringIn, transform: `translateY(${(1 - ringIn) * 40}px)` }}>
          <svg width="240" height="240" viewBox="0 0 240 240">
            <circle cx="120" cy="120" r={R} fill="none" stroke="#E2DACB" strokeWidth="26" />
            <circle cx="120" cy="120" r={R} fill="none" stroke={C.green} strokeWidth="26" strokeLinecap="round" transform="rotate(-90 120 120)" strokeDasharray={`${CIRC * 0.9 * ringP} ${CIRC}`} />
            <text x="120" y="140" textAnchor="middle" fontSize="58" fontWeight="700" fill={C.dark} fontFamily={SERIF}>{Math.round(90 * ringP)}%</text>
          </svg>
          <div style={{ fontFamily: SERIF, fontWeight: 600, fontSize: 46, lineHeight: 1.15, color: C.ink }}>9 van de 10<br />goed advies</div>
        </div>
      </AbsoluteFill>
    </AbsoluteFill>
  );
};

/* ---------- Scene: 1000 requests, 100 errors ---------- */
const RED = (() => {
  let r = 12345; const rnd = () => { r = (r * 16807) % 2147483647; return r / 2147483647; };
  const all = [...Array(1000).keys()];
  for (let i = 999; i > 0; i--) { const j = Math.floor(rnd() * (i + 1)); [all[i], all[j]] = [all[j], all[i]]; }
  const m = new Map(); all.slice(0, 100).forEach((k, i) => m.set(k, i)); return m;
})();
const Dots = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const head = useSpring(F('s5', 0));
  const start = F('s5', 1.6);
  const redStart = F('s6', 0.2);
  const count = Math.round(interpolate(frame, [redStart, redStart + 2.8 * FPS], [0, 100], { ...clamp, easing: ease }));
  const numIn = useSpring(redStart);
  const cols = 50, cell = 26;
  const dots = [];
  for (let k = 0; k < 1000; k++) {
    const c = k % cols, rr = Math.floor(k / cols);
    const appear = spring({ frame: frame - start - (c + rr) * 0.6, fps, config: { damping: 14, stiffness: 160 } });
    const rank = RED.get(k);
    let fill = C.green, op = 0.5 * appear, sc = appear;
    if (rank !== undefined) {
      const rp = spring({ frame: frame - redStart - rank * 0.8, fps, config: { damping: 9, stiffness: 180 } });
      if (rp > 0.01) { fill = C.terra; op = 0.5 + 0.5 * Math.min(1, rp); sc = 1 + 0.35 * rp * (rp > 1 ? 1 : 1 - Math.abs(1 - rp)); }
    }
    dots.push(<circle key={k} cx={c * cell + 13} cy={rr * cell + 13} r={9 * sc} fill={fill} opacity={op} />);
  }
  return (
    <AbsoluteFill style={{ background: C.light }}>
      <div style={{ position: 'absolute', left: 128, top: 90, fontFamily: SANS, fontSize: 26, fontWeight: 700, letterSpacing: 2, color: C.green, opacity: head }}>ELKE MAAND BIJ SURIBANK</div>
      <div style={{ position: 'absolute', left: 128, top: 140, fontFamily: SERIF, fontWeight: 700, fontSize: 80, color: C.ink, opacity: head, transform: `translateY(${(1 - head) * 30}px)` }}>1.000 aanvragen</div>
      <svg style={{ position: 'absolute', left: 128, top: 300 }} width={cols * cell} height={20 * cell}>{dots}</svg>
      <div style={{ position: 'absolute', left: 1490, top: 330, width: 340, opacity: numIn, transform: `translateY(${(1 - numIn) * 40}px)` }}>
        <div style={{ fontFamily: SERIF, fontWeight: 700, fontSize: 160, lineHeight: 1, color: C.terra }}>{count}</div>
        <div style={{ fontFamily: SANS, fontSize: 36, lineHeight: 1.3, marginTop: 12, color: C.ink }}>keer vergist het model zich.</div>
        <div style={{ fontFamily: SANS, fontSize: 30, marginTop: 22, color: C.mute }}>Elke maand weer.</div>
      </div>
    </AbsoluteFill>
  );
};

/* ---------- Scene: one dot becomes a person ---------- */
const Person = () => {
  const frame = useCurrentFrame();
  const grow = interpolate(frame, [F('z4', 0), F('z4', 1.4)], [0, 1], { ...clamp, easing: Easing.inOut(Easing.cubic) });
  const shIn = useSpring(F('z4', 1.2));
  const txtIn = useSpring(F('z4', 1.8));
  const size = 18 + grow * 3300;
  return (
    <AbsoluteFill style={{ background: C.light, overflow: 'hidden' }}>
      <div style={{ position: 'absolute', left: 640 - size / 2, top: 560 - size / 2, width: size, height: size, borderRadius: '50%', background: grow < 0.98 ? C.terra : C.dark, transition: 'none' }} />
      <div style={{ position: 'absolute', left: 260, top: 250, width: 520, height: 600, opacity: shIn, transform: `scale(${0.85 + 0.15 * shIn})` }}>
        <Shanti frame={frame} />
      </div>
      <div style={{ position: 'absolute', left: 860, top: 360, width: 960, fontFamily: SERIF, fontWeight: 700, fontSize: 88, lineHeight: 1.08, color: C.light, opacity: txtIn, transform: `translateY(${(1 - txtIn) * 40}px)` }}>
        Achter elk percentage staan <span style={{ color: C.amber }}>mensen</span>.
      </div>
    </AbsoluteFill>
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

/* ---------- Intro extras ---------- */
const IntroExtra = () => (
  <>
    <Pop at={F('i2', 0.2)} style={{ left: 140, top: 780, display: 'flex', gap: 26 }}>
      <div style={{ fontFamily: SANS, fontWeight: 700, fontSize: 38, background: C.terra, color: C.card, borderRadius: 999, padding: '16px 36px' }}>2 soorten fouten</div>
      <div style={{ fontFamily: SANS, fontWeight: 700, fontSize: 38, background: C.amber, color: C.dark, borderRadius: 999, padding: '16px 36px' }}>4 plekken waar ze ontstaan</div>
    </Pop>
    <Pop at={F('i3', 0.2)} style={{ left: 1180, top: 300, width: 600 }}>
      <div style={{ background: 'rgba(246,243,236,.08)', border: '2px solid rgba(201,216,209,.35)', borderRadius: 22, padding: '30px 36px' }}>
        <div style={{ width: 220, height: 230 }}><Bank /></div>
        <div style={{ fontFamily: SANS, fontSize: 30, color: '#C9D8D1', marginTop: 12, lineHeight: 1.35 }}>Een verzonnen bank met verzonnen gegevens. Dezelfde gegevens gebruik je in practicum 1.</div>
      </div>
    </Pop>
  </>
);

/* ---------- Scene: letter + two errors ---------- */
const Letter = () => {
  const frame = useCurrentFrame();
  const letterIn = useSpring(F('s7', 0.1), { damping: 14 });
  const stamp = spring({ frame: frame - F('s7', 2.3), fps: FPS, config: { damping: 10, stiffness: 200 } });
  return (
    <AbsoluteFill style={{ background: C.light }}>
      <div style={{ position: 'absolute', left: 100, top: 300, width: 480, height: 550 }}><Shanti frame={frame} /></div>
      <div style={{ position: 'absolute', left: 560, top: 150, width: 480, opacity: letterIn, transform: `translate(${(1 - letterIn) * 300}px, ${(1 - letterIn) * -120}px) rotate(${-4 + (1 - letterIn) * 20}deg)` }}>
        <div style={{ background: C.card, border: '2px solid #E2DACB', borderRadius: 18, padding: '30px 36px', boxShadow: '0 18px 40px rgba(18,49,42,.14)' }}>
          <div style={{ fontFamily: SANS, fontSize: 22, color: C.mute }}>Suribank · uw aanvraag</div>
          <div style={{ fontFamily: SANS, fontSize: 26, lineHeight: 1.4, marginTop: 12, color: C.ink }}>Geachte mevrouw, na beoordeling kunnen wij u helaas geen lening aanbieden.</div>
          <div style={{ display: 'inline-block', marginTop: 22, border: `6px solid ${C.terra}`, color: C.terra, fontFamily: SANS, fontWeight: 800, fontSize: 46, letterSpacing: 3, padding: '4px 22px', opacity: Math.min(1, stamp), transform: `rotate(-8deg) scale(${2.2 - 1.2 * Math.min(1, stamp)})` }}>AFGEWEZEN</div>
        </div>
      </div>
      <Pop at={F('s8', 0.3)} style={{ left: 560, top: 600, width: 480 }}>
        <div style={{ background: C.sand, borderRadius: 18, padding: '26px 32px', fontFamily: SANS, fontSize: 30, lineHeight: 1.4, color: C.ink }}>Genoeg inkomen uit de markt.<br /><b style={{ color: C.terra }}>Geen loonstrook.</b></div>
      </Pop>
      <Pop at={F('s9', 0)} style={{ left: 1110, top: 190, width: 700 }}>
        <div style={{ display: 'inline-block', background: C.terra, color: C.card, fontFamily: SANS, fontWeight: 700, fontSize: 44, borderRadius: 999, padding: '16px 38px' }}>Onterecht afgewezen</div>
        <div style={{ fontFamily: SANS, fontSize: 30, color: C.mute, marginTop: 16 }}>Had terugbetaald, kreeg geen lening.</div>
      </Pop>
      <Pop at={F('s10', 1.2)} style={{ left: 1110, top: 520, width: 700 }}>
        <div style={{ display: 'inline-block', background: C.amber, color: C.dark, fontFamily: SANS, fontWeight: 700, fontSize: 44, borderRadius: 999, padding: '16px 38px' }}>Onterecht goedgekeurd</div>
        <div style={{ fontFamily: SANS, fontSize: 30, color: C.mute, marginTop: 16 }}>Kreeg een lening, kan niet terugbetalen.</div>
      </Pop>
      <Pop at={F('s11', 0)} style={{ left: 1110, top: 380 }}><div style={{ fontFamily: SANS, fontSize: 32, fontWeight: 700, color: C.terra }}>→ raakt vooral de aanvrager</div></Pop>
      <Pop at={F('s11', 1.6)} style={{ left: 1110, top: 710 }}><div style={{ fontFamily: SANS, fontSize: 32, fontWeight: 700, color: '#8A6410' }}>→ raakt vooral de bank</div></Pop>
    </AbsoluteFill>
  );
};

/* ---------- Scene: quiz ---------- */
const Quiz = ({ n, q, qb, a, a2, question, A, B, note }) => {
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
      <Pop at={F(qb, 0)} style={{ left: 128, top: 450 }}>
        <div style={optStyle(false)}>{A}</div>
        <div style={optStyle(true)}>{B}</div>
      </Pop>
      <Pop at={F(qb, 0)} style={{ left: 1560, top: 500 }}>
        <svg width="220" height="220"><circle cx="110" cy="110" r="90" fill="none" stroke="#E2DACB" strokeWidth="18" />
          <circle cx="110" cy="110" r="90" fill="none" stroke={C.terra} strokeWidth="18" strokeLinecap="round" strokeDasharray={`${565 * (1 - p)} 1000`} transform="rotate(-90 110 110)" />
          <text x="110" y="128" textAnchor="middle" fontSize="54" fontWeight="700" fontFamily={SERIF} fill={C.dark}>{p <= 0 ? 5 : p < 1 ? left : '✓'}</text></svg>
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

/* ---------- Scene: four places ---------- */
const Four = ({ at, stagger = 0.35, size = 380 }) => (
  <div style={{ position: 'absolute', left: 128, top: 0, width: 1664, height: 1080 }}>
    {['Data', 'Label', 'Kenmerken', 'Gebruik'].map((n, i) => (
      <Pop key={n} at={at + Math.round(i * stagger * FPS)} style={{ left: i * (size + 46), top: 360 }}>
        <div style={{ width: size, background: C.card, border: '2px solid #E2DACB', borderRadius: 24, padding: '34px 0', textAlign: 'center', boxShadow: '0 14px 34px rgba(18,49,42,.10)' }}>
          <div style={{ fontFamily: SERIF, fontWeight: 700, fontSize: 96, color: C.amber }}>{i + 1}</div>
          <div style={{ fontFamily: SANS, fontWeight: 700, fontSize: 40, color: C.ink }}>{n}</div>
        </div>
      </Pop>
    ))}
  </div>
);
const Places = () => (
  <AbsoluteFill style={{ background: C.light }}>
    <Pop at={F('v1', 0)} style={{ left: 128, top: 150 }}><div style={{ fontFamily: SERIF, fontWeight: 700, fontSize: 72, color: C.ink }}>Vier plekken waar fouten ontstaan</div></Pop>
    <Four at={F('v1', 3.2)} stagger={0.9} />
  </AbsoluteFill>
);

/* ---------- Scene: data ---------- */
const DataScene = () => {
  const frame = useCurrentFrame();
  const rows = [['Marlon · Paramaribo', 'vaste baan', 'SRD 18.400', 'ja'], ['Wiwin · Commewijne', 'vaste baan', 'SRD 15.900', 'ja'], ['Shanti · Nickerie', 'informeel', '?', 'nee'], ['Desiree · Brokopondo', 'informeel', '?', 'nee']];
  const b1 = interpolate(frame, [F('d2', 0.6), F('d2', 2.6)], [0, 1], { ...clamp, easing: ease });
  const b2 = interpolate(frame, [F('d2', 5.0), F('d2', 6.2)], [0, 1], { ...clamp, easing: ease });
  const sq = interpolate(frame, [F('d3', 0.3), F('d3', 2.6)], [0, 1200], clamp);
  const bin = frame > F('d3', 4.2);
  return (
    <AbsoluteFill style={{ background: C.light }}>
      <Chips on={0} />
      <Pop at={F('d1', 0.2)} style={{ left: 128, top: 160, width: 1000 }}>
        <div style={{ background: C.card, border: '2px solid #E2DACB', borderRadius: 22, overflow: 'hidden', fontFamily: SANS, fontSize: 29 }}>
          <div style={{ display: 'flex', background: C.dark, color: C.light, padding: '16px 26px' }}>{['Aanvrager', 'Werk', 'Inkomen', 'Advies'].map((h, i) => <div key={h} style={{ flex: i ? 1 : 1.6 }}>{h}</div>)}</div>
          {rows.map((r, j) => (
            <div key={j} style={{ display: 'flex', padding: '14px 26px', background: j % 2 ? C.sand : C.card, fontWeight: j === 2 ? 700 : 400 }}>
              <div style={{ flex: 1.6 }}>{r[0]}</div><div style={{ flex: 1 }}>{r[1]}</div>
              <div style={{ flex: 1, color: r[2] === '?' ? C.terra : C.ink, fontWeight: r[2] === '?' ? 800 : 400, fontSize: r[2] === '?' ? 40 : 29, transform: r[2] === '?' ? `scale(${1 + 0.15 * Math.sin(frame / 5)})` : 'none', transformOrigin: 'left center' }}>{r[2]}</div>
              <div style={{ flex: 1, fontWeight: 700, color: r[3] === 'ja' ? C.green : C.terra }}>{r[3]}</div>
            </div>
          ))}
        </div>
      </Pop>
      <Pop at={F('d2', 0)} style={{ left: 1220, top: 170, width: 570 }}>
        <div style={{ fontFamily: SANS, fontWeight: 700, fontSize: 30, marginBottom: 22, color: C.ink }}>Inkomen ontbreekt</div>
        {[['Informeel werk', b1 * 0.95, C.terra, '14%'], ['Vaste baan', b2 * (2 / 14) * 0.95, C.green, '<2%']].map(([l, w, col, v]) => (
          <div key={l} style={{ marginBottom: 26 }}>
            <div style={{ fontFamily: SANS, fontSize: 27, marginBottom: 8, color: C.ink }}>{l}</div>
            <div style={{ position: 'relative', height: 54, borderRadius: 12, background: '#E2DACB' }}>
              <div style={{ width: `${w * 100}%`, height: 54, borderRadius: 12, background: col }} />
              <div style={{ position: 'absolute', right: 16, top: 9, fontFamily: SANS, fontWeight: 700, fontSize: 30 }}>{v}</div>
            </div>
          </div>
        ))}
      </Pop>
      <Pop at={F('d3', 0)} style={{ left: 128, top: 620, width: 1664 }}>
        <div style={{ fontFamily: SANS, fontWeight: 700, fontSize: 30, marginBottom: 14, color: C.ink }}>1.200 aanvragen · <span style={{ color: '#B07A10' }}>204 uit het binnenland</span></div>
        <svg width="1664" height="130">{Array.from({ length: Math.floor(sq) }, (_, k) => (
          <rect key={k} x={(k % 120) * 13.8} y={Math.floor(k / 120) * 13} width="10.5" height="10" rx="2" fill={bin && k >= 996 ? '#B07A10' : '#9FB3A9'} />
        ))}</svg>
      </Pop>
      <Banner at={F('d4', 0.2)}>Wat het model niet goed kent, voorspelt het minder goed.</Banner>
    </AbsoluteFill>
  );
};

/* ---------- Scene: label ---------- */
const LabelScene = () => {
  const frame = useCurrentFrame();
  const rows = [['A · 2019', 'vaste baan', 'goedgekeurd', 'ja'], ['B · 2019', 'informeel', 'afgewezen', '?'], ['C · 2020', 'vaste baan', 'goedgekeurd', 'ja'], ['D · 2020', 'vaste baan', 'goedgekeurd', 'nee'], ['E · 2021', 'informeel', 'afgewezen', '?'], ['F · 2021', 'vaste baan', 'goedgekeurd', 'ja'], ['G · 2022', 'informeel', 'goedgekeurd', 'ja'], ['H · 2022', 'informeel', 'afgewezen', '?'], ['I · 2023', 'vaste baan', 'goedgekeurd', 'ja']];
  const grey = interpolate(frame, [F('l3', 0), F('l3', 0.8)], [0, 1], clamp);
  const hl = frame > F('l1', 4.5);
  return (
    <AbsoluteFill style={{ background: C.light }}>
      <Chips on={1} />
      <Pop at={F('l1', 0.2)} style={{ left: 128, top: 150, width: 1060 }}>
        <div style={{ background: C.card, border: '2px solid #E2DACB', borderRadius: 22, overflow: 'hidden', fontFamily: SANS, fontSize: 28 }}>
          <div style={{ display: 'flex', background: C.dark, color: C.light, padding: '14px 26px' }}>
            {['Aanvraag (vroeger)', 'Werk', 'Besluit toen', 'terugbetaald'].map((h, i) => <div key={h} style={{ flex: i ? 1 : 1.5, color: i === 3 ? C.amber : C.light, textDecoration: i === 3 && hl ? 'underline' : 'none' }}>{h}</div>)}
          </div>
          {rows.map((r, j) => {
            const rowIn = spring({ frame: frame - F('l1', 1.2) - j * 7, fps: FPS, config: { damping: 18 } });
            const rej = r[2] === 'afgewezen';
            const valShown = rej ? grey : interpolate(frame, [F('l2', 0), F('l2', 0.6)], [0.25, 1], clamp);
            return (
              <div key={j} style={{ display: 'flex', padding: '11px 26px', background: j % 2 ? C.sand : C.card, opacity: rowIn * (rej ? 1 - 0.45 * grey : 1), transform: `translateX(${(1 - rowIn) * -40}px)` }}>
                <div style={{ flex: 1.5 }}>{r[0]}</div><div style={{ flex: 1 }}>{r[1]}</div><div style={{ flex: 1 }}>{r[2]}</div>
                <div style={{ flex: 1, fontWeight: 800, fontSize: 32, opacity: valShown, color: r[3] === '?' ? C.terra : r[3] === 'ja' ? C.green : '#B07A10' }}>{r[3]}</div>
              </div>
            );
          })}
        </div>
      </Pop>
      <Pop at={F('l4', 0.3)} style={{ left: 1260, top: 190, width: 530 }}>
        <div style={{ fontFamily: SANS, fontWeight: 700, fontSize: 30, marginBottom: 16, color: C.ink }}>Waar leert het model van?</div>
        <div style={{ background: C.card, border: '2px solid #E2DACB', borderRadius: 22, padding: '24px 30px', fontFamily: SANS, fontSize: 27, lineHeight: 1.6, color: C.ink }}>
          Goedgekeurd, vaste baan: <span style={{ fontFamily: SERIF, fontWeight: 700, fontSize: 52, color: C.green }}>5</span><br />
          Goedgekeurd, informeel: <span style={{ fontFamily: SERIF, fontWeight: 700, fontSize: 52, color: C.terra }}>1</span>
        </div>
      </Pop>
      <Banner at={F('l5', 0.2)}>Het label is geen objectieve waarheid, maar het gevolg van <span style={{ color: C.amber }}>eerdere keuzes</span>.</Banner>
    </AbsoluteFill>
  );
};

/* ---------- Scene: proxy ---------- */
const ProxyScene = () => {
  const frame = useCurrentFrame();
  const h1 = interpolate(frame, [F('p1', 4.0), F('p1', 5.5)], [0, 1], { ...clamp, easing: ease });
  const h2 = interpolate(frame, [F('p1', 7.2), F('p1', 8.7)], [0, 1], { ...clamp, easing: ease });
  const hid = interpolate(frame, [F('p3', 0.6), F('p3', 1.6)], [0, 1], clamp);
  const lineIn = interpolate(frame, [F('p2', 0.2), F('p2', 1.4)], [0, 1], clamp);
  return (
    <AbsoluteFill style={{ background: C.light }}>
      <Chips on={2} />
      <Pop at={F('p1', 0)} style={{ left: 128, top: 170, width: 640 }}>
        <div style={{ fontFamily: SANS, fontWeight: 700, fontSize: 30, color: C.ink }}>Terugbetaald</div>
        <div style={{ display: 'flex', alignItems: 'flex-end', gap: 70, height: 470 }}>
          {[['Binnenland', 49, h1, '#B07A10'], ['Kust', 61, h2, C.green]].map(([l, v, h, col]) => (
            <div key={l} style={{ textAlign: 'center' }}>
              <div style={{ fontFamily: SERIF, fontWeight: 700, fontSize: 50, color: C.ink, opacity: h }}>{Math.round(v * h)}%</div>
              <div style={{ width: 190, height: v * 6 * h, background: col, borderRadius: '14px 14px 0 0' }} />
              <div style={{ fontFamily: SANS, fontSize: 30, marginTop: 12, color: C.ink }}>{l}</div>
            </div>
          ))}
        </div>
      </Pop>
      <svg style={{ position: 'absolute', left: 860, top: 170 }} width="980" height="700" viewBox="0 0 980 700">
        <g opacity={useSpring(F('p2', 0))} fontFamily={SANS} fontSize="34" fontWeight="700" textAnchor="middle">
          <rect x="340" y="20" width="300" height="90" rx="45" fill={C.dark} /><text x="490" y="78" fill={C.amber}>district</text>
          <line x1="430" y1="110" x2={430 - 200 * lineIn} y2={110 + 190 * lineIn} stroke={C.green} strokeWidth="5" />
          <line x1="550" y1="110" x2={550 + 200 * lineIn} y2={110 + 190 * lineIn} stroke={C.green} strokeWidth="5" />
          <g opacity={lineIn}>
            <rect x="80" y="300" width="300" height="90" rx="45" fill={C.card} stroke={C.green} strokeWidth="4" /><text x="230" y="358" fill={C.ink}>inkomen</text>
            <rect x="600" y="300" width="300" height="90" rx="45" fill={C.card} stroke={C.green} strokeWidth="4" /><text x="750" y="358" fill={C.ink}>soort werk</text>
          </g>
          <g opacity={hid}>
            <line x1="460" y1="110" x2="330" y2="540" stroke={C.terra} strokeWidth="5" strokeDasharray="14 10" strokeDashoffset={-frame} />
            <line x1="520" y1="110" x2="650" y2="540" stroke={C.terra} strokeWidth="5" strokeDasharray="14 10" strokeDashoffset={-frame} />
            <rect x="190" y="540" width="280" height="90" rx="45" fill={C.terra} /><text x="330" y="598" fill={C.card}>afkomst</text>
            <rect x="510" y="540" width="280" height="90" rx="45" fill={C.terra} /><text x="650" y="598" fill={C.card}>armoede</text>
          </g>
        </g>
      </svg>
      <Pop at={F('p4', 0.1)} style={{ left: 880, top: 800 }}>
        <span style={{ display: 'inline-block', background: C.terra, color: C.card, fontFamily: SANS, fontWeight: 700, fontSize: 40, borderRadius: 999, padding: '12px 34px' }}>proxy</span>
        <span style={{ fontFamily: SANS, fontSize: 32, marginLeft: 20, color: C.ink }}>meet via een omweg iets gevoeligs</span>
      </Pop>
    </AbsoluteFill>
  );
};

/* ---------- Scene: use ---------- */
const UseScene = () => {
  const frame = useCurrentFrame();
  const cp = interpolate(frame, [F('g3', 1.0), F('g3', 2.2)], [0, 1], { ...clamp, easing: ease });
  const clickT = (frame - F('g3', 2.4)) % 48;
  const click = frame > F('g3', 2.4) && clickT < 8;
  const sw = interpolate(frame, [F('g4', 1.8), F('g4', 2.6)], [0, 1], clamp);
  const box = { width: 520, height: 520 };
  return (
    <AbsoluteFill style={{ background: C.light }}>
      <Chips on={3} />
      <Pop at={F('g1', 0)} style={{ left: 128, top: 150 }}><div style={{ fontFamily: SERIF, fontWeight: 700, fontSize: 68, color: C.ink }}>Een goed model, verkeerd gebruikt</div></Pop>
      <Pop at={F('g2', 0)} style={{ left: 128, top: 320 }}>
        <div style={{ ...box, background: C.card, border: '2px solid #E2DACB', borderRadius: 24, padding: 34, fontFamily: SANS, color: C.ink }}>
          <div style={{ fontWeight: 700, fontSize: 24, letterSpacing: 2, color: '#B07A10' }}>VERKEERDE GROEP</div>
          <div style={{ fontSize: 30, marginTop: 28 }}>Geleerd van</div>
          <div style={{ display: 'inline-block', background: C.sand, borderRadius: 999, padding: '10px 26px', fontSize: 32, marginTop: 10 }}>particulieren</div>
          <div style={{ fontSize: 60, color: C.terra, margin: '10px 0' }}>↓</div>
          <div style={{ fontSize: 30 }}>Gebruikt voor</div>
          <div style={{ display: 'inline-block', background: C.terra, color: C.card, borderRadius: 999, padding: '10px 26px', fontSize: 32, marginTop: 10 }}>kleine bedrijven</div>
        </div>
      </Pop>
      <Pop at={F('g3', 0)} style={{ left: 700, top: 320 }}>
        <div style={{ ...box, position: 'relative', background: C.card, border: '2px solid #E2DACB', borderRadius: 24, padding: 34, fontFamily: SANS, color: C.ink }}>
          <div style={{ fontWeight: 700, fontSize: 24, letterSpacing: 2, color: '#B07A10' }}>BLIND VOLGEN</div>
          <div style={{ fontSize: 30, marginTop: 28, color: C.mute }}>Advies: afwijzen</div>
          <div style={{ marginTop: 40, width: 320, padding: 24, borderRadius: 16, background: click ? C.amber : C.green, color: C.card, fontSize: 40, fontWeight: 700, textAlign: 'center', transform: `scale(${click ? 0.96 : 1})` }}>Akkoord</div>
          <div style={{ fontSize: 28, marginTop: 40, color: C.mute }}>Weinig tijd · de computer lijkt objectief</div>
          <svg width="60" height="60" style={{ position: 'absolute', left: 430 - 210 * cp, top: 470 - 230 * cp }}><polygon points="5,5 5,50 18,38 28,58 36,54 26,34 44,34" fill={C.ink} stroke={C.card} strokeWidth="3" /></svg>
        </div>
      </Pop>
      <Pop at={F('g4', 0)} style={{ left: 1272, top: 320 }}>
        <div style={{ ...box, background: C.card, border: '2px solid #E2DACB', borderRadius: 24, padding: 34, fontFamily: SANS, color: C.ink }}>
          <div style={{ fontWeight: 700, fontSize: 24, letterSpacing: 2, color: '#B07A10' }}>HULPMIDDEL WORDT BESLUIT</div>
          <div style={{ position: 'relative', height: 200, marginTop: 70 }}>
            <div style={{ position: 'absolute', fontFamily: SERIF, fontWeight: 700, fontSize: 84, color: C.green, opacity: 1 - sw, transform: `translateY(${-30 * sw}px)` }}>advies</div>
            <div style={{ position: 'absolute', fontFamily: SERIF, fontWeight: 700, fontSize: 84, color: C.terra, opacity: sw, transform: `translateY(${30 * (1 - sw)}px)` }}>besluit</div>
          </div>
          <div style={{ fontSize: 30, color: C.mute }}>Niemand kijkt meer mee.</div>
        </div>
      </Pop>
    </AbsoluteFill>
  );
};

/* ---------- Scene: summary ---------- */
const Summary = () => (
  <AbsoluteFill style={{ background: C.light }}>
    <Pop at={F('z1', 0)} style={{ left: 128, top: 150, width: 1660 }}><div style={{ fontFamily: SERIF, fontWeight: 700, fontSize: 72, color: C.ink }}>AI geeft voorspellingen, geen zekerheden.</div></Pop>
    <Four at={F('z2', 0.2)} stagger={0.7} size={370} />
    <Banner at={F('z3', 0.6)} top={690}>Welke fout is erger, en voor wie? <span style={{ color: C.amber }}>Dat is een ethische vraag.</span></Banner>
  </AbsoluteFill>
);

/* ---------- Scene: what now ---------- */
const WhatNow = () => (
  <AbsoluteFill style={{ background: C.light }}>
    <Pop at={F('e1', 0)} style={{ left: 128, top: 130 }}><div style={{ fontFamily: SERIF, fontWeight: 700, fontSize: 72, color: C.ink }}>Wat je nu doet</div></Pop>
    {[['e1', 'Bekijk clip 3: Fouten tellen'], ['e2', 'Denk na: welke fout vind jij erger, en waarom?'], ['e3', 'Practicum 1: zelf werken met de gegevens van Suribank']].map(([k, t], i) => (
      <Pop key={k} at={F(k, 0.4)} style={{ left: 128, top: 300 + i * 170, width: 1664 }}>
        <div style={{ background: C.card, border: '2px solid #E2DACB', borderRadius: 22, padding: '28px 38px', fontFamily: SANS, fontSize: 40, color: C.ink, display: 'flex', gap: 28, alignItems: 'center' }}>
          <span style={{ fontFamily: SERIF, fontWeight: 700, fontSize: 56, color: C.green }}>{i + 1}</span>{t}
        </div>
      </Pop>
    ))}
    <Pop at={F('e3', 4.5)} style={{ left: 128, top: 840 }}><div style={{ fontFamily: SANS, fontWeight: 700, fontSize: 34, color: C.terra }}>Deadline week 0: woensdag 6 januari, 23:59</div></Pop>
  </AbsoluteFill>
);

/* ---------- Composition ---------- */
const Fade = ({ from, to, children }) => {
  const frame = useCurrentFrame();
  const o = interpolate(frame, [from - 8, from + 8, to - 8, to + 8], [0, 1, 1, 0], clamp);
  if (frame < from - 10 || frame > to + 10) return null;
  return <AbsoluteFill style={{ opacity: o }}>{children}</AbsoluteFill>;
};

export const ClipFull = () => {
  const [handle] = useState(() => delayRender('fonts'));
  useEffect(() => { document.fonts.ready.then(() => continueRender(handle)); }, [handle]);
  const end = Math.ceil(timing.total * FPS);
  const scenes = [
    ['i0', <Intro />], ['s0', <Market />], ['s5', <Dots />], ['s7', <Letter />],
    ['q1', <Quiz n={1} q="q1" qb="q1b" a="a1" question="Het model wijst iemand af die de lening wél had terugbetaald. Welke fout is dit?" A="A. Onterecht goedgekeurd" B="B. Onterecht afgewezen" note="Het model wees af, en dat was niet terecht." />],
    ['v1', <Places />], ['d1', <DataScene />], ['l1', <LabelScene />], ['p1', <ProxyScene />],
    ['q2', <Quiz n={2} q="q2" qb="q2b" a="a2" a2="a2b" question="De bank haalt de kolom district uit het model. Is het risico op ongelijke behandeling naar woonplaats nu weg?" A="A. Ja, het model kan de woonplaats niet meer zien." B="B. Nee, andere kenmerken hangen samen met de woonplaats." note={<>Kenmerk weglaten ≠ effect weghalen. <span style={{ color: C.amber }}>Blijf controleren per groep.</span></>} />],
    ['g1', <UseScene />], ['z1', <Summary />], ['z4', <Person />], ['e1', <WhatNow />],
  ];
  return (
    <AbsoluteFill style={{ background: C.light }}>
      {scenes.map(([k, el], i) => {
        const from = i === 0 ? 0 : F(k, -0.4);
        const to = i + 1 < scenes.length ? F(scenes[i + 1][0], -0.4) : end + 20;
        return <Fade key={k} from={from} to={to}>{el}</Fade>;
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
