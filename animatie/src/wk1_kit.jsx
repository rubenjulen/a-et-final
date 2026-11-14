// Gedeelde onderdelen voor de week 1-clips (kaderclip A, clip 5).
// Kopie van de vaste stijl uit Clip4.jsx, maar als fabriek: makeKit(timing) geeft F, Captions, QuizN, Audio.
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

export const C = {
  dark: '#12312A', light: '#F6F3EC', sand: '#EDE7DA', card: '#FFFDF8',
  amber: '#E3A92B', green: '#2F6B4F', terra: '#A8432C', ink: '#1C2421', mute: '#44504B', line: '#E2DACB',
};
export const SERIF = "'Source Serif 4', Georgia, serif";
export const SANS = "'Public Sans', Arial, sans-serif";
export const FPS = 30;
export const clamp = { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' };
export { Easing, interpolate, spring, useCurrentFrame, AbsoluteFill };

export const useSpring = (startFrame, cfg = {}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  return spring({ frame: frame - startFrame, fps, config: { damping: 18, stiffness: 120, mass: 0.9, ...cfg } });
};
export const fade = (frame, a, b) => interpolate(frame, [a, b], [0, 1], clamp);

export const Pop = ({ at, children, dy = 40, style = {} }) => {
  const s = useSpring(at);
  return <div style={{ position: 'absolute', opacity: s, transform: `translateY(${(1 - s) * dy}px) scale(${0.96 + 0.04 * s})`, ...style }}>{children}</div>;
};
export const Banner = ({ at, children, top = 770, left = 128, width = 1664, size = 46 }) => (
  <Pop at={at} style={{ left, top, width }}>
    <div style={{ background: C.dark, borderRadius: 22, padding: '22px 38px', fontFamily: SERIF, fontWeight: 600, fontSize: size, color: C.light, lineHeight: 1.2 }}>{children}</div>
  </Pop>
);
export const Title = ({ at, children, top = 110, size = 64, kicker }) => (
  <Pop at={at} style={{ left: 128, top, width: 1664 }}>
    {kicker && <div style={{ fontFamily: SANS, fontWeight: 700, fontSize: 24, letterSpacing: 2.5, color: C.terra, marginBottom: 8 }}>{kicker}</div>}
    <div style={{ fontFamily: SERIF, fontWeight: 700, fontSize: size, lineHeight: 1.1, color: C.ink }}>{children}</div>
  </Pop>
);

/* ---------- Shanti (zelfde figuur als clip 2–4) ---------- */
export const Shanti = ({ frame, label = true }) => {
  const breathe = 1 + 0.012 * Math.sin(frame / 18);
  const eye = frame % 110 > 104 ? 0.15 : 1;
  const sway = Math.sin(frame / 25) * 2;
  return (
    <svg viewBox="0 0 560 640" width="100%" height="100%">
      <defs><linearGradient id="table" x1="0" x2="0" y1="0" y2="1"><stop offset="0" stopColor="#D2AE87" /><stop offset="1" stopColor="#B88E66" /></linearGradient></defs>
      <g transform={`translate(280,118) scale(1,${breathe})`} style={{ transformOrigin: '280px 420px' }}>
        <path d="M-92 330 Q-92 196 0 186 Q92 196 92 330 Z" fill={C.green} />
        <path d="M-40 200 Q0 236 40 200" stroke="#25563F" strokeWidth="6" fill="none" />
        <rect x="-17" y="152" width="34" height="44" fill="#7A4A2E" />
        <circle cx="0" cy="112" r="64" fill="#7A4A2E" />
        <path d="M-66 104 Q-62 36 0 40 Q62 36 66 104 Q50 70 0 72 Q-50 70 -66 104Z" fill={C.ink} />
        <circle cx="46" cy="52" r="26" fill={C.ink} />
        <ellipse cx="-22" cy="114" rx="6.5" ry={6.5 * eye} fill={C.ink} />
        <ellipse cx="22" cy="114" rx="6.5" ry={6.5 * eye} fill={C.ink} />
        <path d="M-20 142 Q0 156 20 142" stroke={C.ink} strokeWidth="5" fill="none" strokeLinecap="round" />
        <circle cx="-38" cy="134" r="9" fill="#8E5638" opacity="0.6" /><circle cx="38" cy="134" r="9" fill="#8E5638" opacity="0.6" />
      </g>
      <g transform={`translate(0,${sway * 0.3})`}>
        {[0, 1, 2, 3, 4, 5, 6].map((i) => <rect key={i} x={20 + i * 74} y="300" width="74" height="58" fill={i % 2 ? C.card : C.amber} />)}
        <path d="M20 358 Q57 388 94 358 Q131 388 168 358 Q205 388 242 358 Q279 388 316 358 Q353 388 390 358 Q427 388 464 358 Q501 388 538 358 L538 358 L20 358Z" fill={C.amber} />
      </g>
      <rect x="30" y="300" width="10" height="140" fill="#8A6A4A" /><rect x="520" y="300" width="10" height="140" fill="#8A6A4A" />
      <rect x="20" y="430" width="520" height="160" rx="12" fill="url(#table)" /><rect x="20" y="420" width="520" height="22" rx="4" fill="#8A6A4A" />
      <g fill={C.green}><circle cx="90" cy="410" r="27" /><circle cx="136" cy="414" r="22" /><circle cx="112" cy="392" r="18" /></g>
      <g fill={C.terra}><circle cx="420" cy="410" r="25" /><circle cx="463" cy="414" r="21" /><circle cx="441" cy="392" r="20" /></g>
      <g fill={C.amber}><ellipse cx="210" cy="412" rx="34" ry="16" /><ellipse cx="300" cy="414" rx="30" ry="14" /></g>
      {label && <g transform="translate(280,0)"><rect x="-130" y="590" width="260" height="46" rx="23" fill={C.dark} /><text x="0" y="621" textAnchor="middle" fontSize="27" fontWeight="700" fill={C.light} fontFamily={SANS}>Shanti · Nickerie</text></g>}
    </svg>
  );
};
export const MiniShanti = ({ frame, size = 150 }) => (
  <div style={{ width: size, height: size, borderRadius: '50%', overflow: 'hidden', background: C.sand, border: `4px solid ${C.card}`, boxShadow: '0 8px 20px rgba(0,0,0,.15)' }}>
    <div style={{ width: size * 2.1, height: size * 2.4, marginLeft: -size * 0.55, marginTop: -size * 0.15 }}><Shanti frame={frame} label={false} /></div>
  </div>
);
export const Bank = () => (
  <svg viewBox="0 0 400 430" width="100%" height="100%">
    <polygon points="200,10 392,112 8,112" fill={C.dark} />
    <rect x="28" y="112" width="344" height="24" fill={C.green} />
    <g fill={C.sand}>{[55, 135, 231, 311].map((x) => <rect key={x} x={x} y="142" width="34" height="198" rx="4" />)}</g>
    <rect x="18" y="340" width="364" height="30" fill={C.dark} />
    <text x="200" y="412" textAnchor="middle" fontSize="42" fontWeight="700" fill={C.dark} fontFamily={SANS}>Suribank</text>
  </svg>
);
/* Eenvoudig persoontje (medewerker, klant) */
export const Figure = ({ color = C.green, skin = '#7A4A2E', size = 120, badge }) => (
  <svg viewBox="0 0 120 150" width={size} height={size * 1.25}>
    <circle cx="60" cy="38" r="26" fill={skin} />
    <path d="M14 146 Q14 78 60 74 Q106 78 106 146 Z" fill={color} />
    {badge && <rect x="38" y="104" width="44" height="16" rx="4" fill={C.card} />}
  </svg>
);

/* ---------- telefoon + chat (uit clip 4) ---------- */
export const Bubble = ({ who, at, children, frame, stamp }) => {
  const s = spring({ frame: frame - at, fps: FPS, config: { damping: 16, stiffness: 140 } });
  const me = who === 'me';
  const typing = frame >= at - 18 && frame < at && !me;
  if (frame < at - 18) return null;
  return (
    <div style={{ display: 'flex', justifyContent: me ? 'flex-end' : 'flex-start', marginTop: 14 }}>
      {typing ? (
        <div style={{ background: '#E6EEEA', borderRadius: 18, padding: '14px 20px', display: 'flex', gap: 6 }}>
          {[0, 1, 2].map((i) => <div key={i} style={{ width: 10, height: 10, borderRadius: 5, background: C.green, opacity: 0.4 + 0.6 * Math.abs(Math.sin((frame + i * 5) / 5)) }} />)}
        </div>
      ) : (
        <div style={{ position: 'relative', maxWidth: 420, background: me ? C.green : '#E6EEEA', color: me ? C.card : C.ink, borderRadius: me ? '20px 20px 6px 20px' : '20px 20px 20px 6px', padding: '14px 20px', fontFamily: SANS, fontSize: 25, lineHeight: 1.35, opacity: s, transform: `translateY(${(1 - s) * 16}px) scale(${0.9 + 0.1 * s})`, transformOrigin: me ? 'right bottom' : 'left bottom' }}>
          {children}{stamp}
        </div>
      )}
    </div>
  );
};
export const Phone = ({ title, sub, children, style = {}, h = 700 }) => (
  <div style={{ position: 'absolute', width: 540, height: h, borderRadius: 54, background: C.dark, padding: 16, boxShadow: '0 30px 60px rgba(18,49,42,.28)', ...style }}>
    <div style={{ width: '100%', height: '100%', borderRadius: 40, background: C.card, overflow: 'hidden', display: 'flex', flexDirection: 'column' }}>
      <div style={{ background: '#F0EBE1', padding: '28px 26px 16px', borderBottom: `2px solid ${C.line}` }}>
        <div style={{ fontFamily: SANS, fontWeight: 700, fontSize: 26, color: C.ink }}>{title}</div>
        <div style={{ fontFamily: SANS, fontSize: 20, color: C.mute }}>{sub}</div>
      </div>
      <div style={{ padding: '6px 22px', flex: 1 }}>{children}</div>
    </div>
  </div>
);

export const interpolateColor = (p, a, b) => {
  const h = (s) => [1, 3, 5].map((i) => parseInt(s.slice(i, i + 2), 16));
  const [x, y] = [h(a), h(b)];
  return `rgb(${x.map((v, i) => Math.round(v + (y[i] - v) * Math.min(1, Math.max(0, p)))).join(',')})`;
};

export const Fade = ({ from, to, children }) => {
  const frame = useCurrentFrame();
  if (frame < from - 10 || frame > to + 10) return null;
  const o = interpolate(frame, [from - 8, from + 8, to - 8, to + 8], [0, 1, 1, 0], clamp);
  return <AbsoluteFill style={{ opacity: o }}>{children}</AbsoluteFill>;
};

/* ---------- fabriek per clip ---------- */
export const makeKit = (timing) => {
  const cue = Object.fromEntries(timing.cues.map((c) => [c.key, c]));
  const F = (key, off = 0) => Math.round((cue[key].start + off) * FPS);
  const end = (key) => Math.round((cue[key].start + cue[key].dur) * FPS);

  const Captions = () => {
    const frame = useCurrentFrame();
    const t = frame / FPS;
    const cur = timing.cues.find((c) => t >= c.start - 0.1 && t <= c.start + c.dur + 0.25);
    if (!cur) return null;
    const o = interpolate(t, [cur.start - 0.1, cur.start + 0.15, cur.start + cur.dur + 0.05, cur.start + cur.dur + 0.25], [0, 1, 1, 0], clamp);
    return (
      <div style={{ position: 'absolute', left: 0, right: 0, bottom: 44, display: 'flex', justifyContent: 'center', opacity: o }}>
        <div style={{ maxWidth: 1460, background: 'rgba(18,49,42,0.88)', color: C.light, fontFamily: SANS, fontSize: 32, lineHeight: 1.35, padding: '12px 30px', borderRadius: 14, textAlign: 'center' }}>{cur.text}</div>
      </div>
    );
  };

  // Tussenvraag: opties verschijnen tijdens de vraag; de aftelbalk loopt NA de gesproken vraag (secs seconden).
  const QuizN = ({ n, q, a, question, options, good, note, secs = 8 }) => {
    const frame = useCurrentFrame();
    const tStart = end(q) + 3;
    const p = interpolate(frame, [tStart, tStart + secs * FPS], [0, 1], clamp);
    const ans = useSpring(F(a, 0));
    return (
      <AbsoluteFill style={{ background: C.light }}>
        <Pop at={F(q, 0)} style={{ left: 128, top: 100 }}><div style={{ fontFamily: SANS, fontWeight: 700, fontSize: 26, letterSpacing: 2, color: C.terra }}>TUSSENVRAAG {n}</div></Pop>
        <Pop at={F(q, 0.3)} style={{ left: 128, top: 155, width: 1380 }}><div style={{ fontFamily: SERIF, fontWeight: 600, fontSize: 52, lineHeight: 1.14, color: C.ink }}>{question}</div></Pop>
        <Pop at={F(q, 1.2)} style={{ left: 128, top: 430 }}>
          {options.map((o, i) => (
            <div key={o} style={{ fontFamily: SANS, fontSize: 34, padding: '18px 30px', borderRadius: 18, width: 1250, marginTop: 16, color: C.ink,
              background: i === good ? interpolateColor(ans, C.card, '#E3F0E8') : C.card,
              border: `3px solid ${i === good && ans > 0.5 ? C.green : C.line}`, opacity: i === good ? 1 : 1 - 0.55 * ans }}>{o}</div>
          ))}
        </Pop>
        <Pop at={F(q, 1.2)} style={{ left: 1560, top: 430 }}>
          <svg width="220" height="220"><circle cx="110" cy="110" r="90" fill="none" stroke={C.line} strokeWidth="18" />
            <circle cx="110" cy="110" r="90" fill="none" stroke={C.terra} strokeWidth="18" strokeLinecap="round" strokeDasharray={`${565 * (1 - p)} 1000`} transform="rotate(-90 110 110)" />
            <text x="110" y="128" textAnchor="middle" fontSize="54" fontWeight="700" fontFamily={SERIF} fill={C.dark}>{p <= 0 ? secs : p < 1 ? Math.ceil(secs * (1 - p)) : '✓'}</text></svg>
          <div style={{ fontFamily: SANS, fontSize: 24, color: C.mute, textAlign: 'center', width: 220 }}>denktijd</div>
        </Pop>
        {note && <Banner at={F(a, 1.0)} top={460 + options.length * 100} size={40}>{note}</Banner>}
      </AbsoluteFill>
    );
  };

  const Root = ({ scenes }) => {
    const [handle] = useState(() => delayRender('fonts'));
    useEffect(() => { document.fonts.ready.then(() => continueRender(handle)); }, [handle]);
    const last = Math.ceil(timing.total * FPS);
    return (
      <AbsoluteFill style={{ background: C.light }}>
        {scenes.map(([k, el], i) => {
          const from = i === 0 ? 0 : F(k, -0.4);
          const to = i + 1 < scenes.length ? F(scenes[i + 1][0], -0.4) : last + 20;
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
  return { cue, F, end, Captions, QuizN, Root };
};
