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
import timing from './timing.json';

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
  const grow = interpolate(frame, [F('s7', 0), F('s7', 1.4)], [0, 1], { ...clamp, easing: Easing.inOut(Easing.cubic) });
  const shIn = useSpring(F('s7', 1.2));
  const txtIn = useSpring(F('s7', 1.8));
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

/* ---------- Composition ---------- */
const Fade = ({ from, to, children }) => {
  const frame = useCurrentFrame();
  const o = interpolate(frame, [from - 8, from + 8, to - 8, to + 8], [0, 1, 1, 0], clamp);
  return <AbsoluteFill style={{ opacity: o }}>{children}</AbsoluteFill>;
};

export const Clip = () => {
  const [handle] = useState(() => delayRender('fonts'));
  useEffect(() => { document.fonts.ready.then(() => continueRender(handle)); }, [handle]);
  const end = Math.ceil(timing.total * FPS);
  return (
    <AbsoluteFill style={{ background: C.light }}>
      <Fade from={0} to={F('s0', -0.4)}><Intro /></Fade>
      <Fade from={F('s0', -0.4)} to={F('s5', -0.3)}><Market /></Fade>
      <Fade from={F('s5', -0.3)} to={F('s7', -0.2)}><Dots /></Fade>
      <Fade from={F('s7', -0.2)} to={end + 20}><Person /></Fade>
      <Captions />
      {timing.cues.map((c) => (
        <Sequence key={c.key} from={Math.round(c.start * FPS)} durationInFrames={Math.ceil((c.dur + 0.2) * FPS)}>
          <Audio src={staticFile(`${timing.audioDir || "aud"}/${c.key}.mp3`)} />
        </Sequence>
      ))}
    </AbsoluteFill>
  );
};
