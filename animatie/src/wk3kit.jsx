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
export const makeF = (timing) => {
  const cue = Object.fromEntries(timing.cues.map((c) => [c.key, c]));
  const F = (key, off = 0) => {
    if (!cue[key]) throw new Error('missing cue ' + key);
    return Math.round((cue[key].start + off) * FPS);
  };
  const end = (key, off = 0) => Math.round((cue[key].start + cue[key].dur + off) * FPS);
  return { cue, F, end };
};
export const useSpr = (startFrame, cfg = {}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  return spring({ frame: frame - startFrame, fps, config: { damping: 18, stiffness: 120, mass: 0.9, ...cfg } });
};
export const fadeIn = (frame, start, len = 15) => interpolate(frame, [start, start + len], [0, 1], clamp);
export const mix = (p, a, b) => {
  const h = (s) => [1, 3, 5].map((i) => parseInt(s.slice(i, i + 2), 16));
  const [x, y] = [h(a), h(b)];
  const q = Math.min(1, Math.max(0, p));
  return `rgb(${x.map((v, i) => Math.round(v + (y[i] - v) * q)).join(',')})`;
};

export const Shanti = ({ frame, label = true }) => {
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


export const Pop = ({ at, children, dy = 40, style = {} }) => {
  const s = useSpr(at);
  return <div style={{ position: 'absolute', opacity: s, transform: `translateY(${(1 - s) * dy}px) scale(${0.96 + 0.04 * s})`, ...style }}>{children}</div>;
};
export const Card = ({ style = {}, children }) => (
  <div style={{ background: C.card, border: `2px solid ${C.line}`, borderRadius: 22, padding: '26px 34px', boxShadow: '0 14px 34px rgba(18,49,42,.10)', ...style }}>{children}</div>
);
export const Banner = ({ at, children, top = 770, left = 128, width = 1664, size = 44 }) => (
  <Pop at={at} style={{ left, top, width }}>
    <div style={{ background: C.dark, borderRadius: 22, padding: '22px 40px', fontFamily: SERIF, fontWeight: 600, fontSize: size, color: C.light, lineHeight: 1.2 }}>{children}</div>
  </Pop>
);
export const Heading = ({ at, kicker, children, top = 96, left = 128, width = 1660 }) => (
  <Pop at={at} style={{ left, top, width }}>
    {kicker && <div style={{ fontFamily: SANS, fontWeight: 700, fontSize: 24, letterSpacing: 2, color: C.terra, marginBottom: 8 }}>{kicker}</div>}
    <div style={{ fontFamily: SERIF, fontWeight: 700, fontSize: 60, lineHeight: 1.1, color: C.ink }}>{children}</div>
  </Pop>
);

/* simple person avatar */
export const Person = ({ size = 120, body = C.green, skin = '#7A4A2E', hair = C.ink, frame = 0, glasses = false, tie = false }) => {
  const b = 1 + 0.015 * Math.sin(frame / 17);
  return (
    <svg width={size} height={size * 1.15} viewBox="0 0 100 115">
      <g transform={`translate(50,0) scale(1,${b})`} style={{ transformOrigin: '50px 115px' }}>
        <path d="M-34 115 Q-34 70 0 66 Q34 70 34 115Z" fill={body} />
        {tie && <path d="M0 70 L-5 80 L0 104 L5 80Z" fill={C.amber} />}
        <circle cx="0" cy="40" r="22" fill={skin} />
        <path d="M-23 38 Q-21 12 0 14 Q21 12 23 38 Q17 26 0 26 Q-17 26 -23 38Z" fill={hair} />
        <circle cx="-8" cy="42" r="2.6" fill={C.ink} /><circle cx="8" cy="42" r="2.6" fill={C.ink} />
        {glasses && <g fill="none" stroke={C.ink} strokeWidth="1.6"><circle cx="-8" cy="42" r="6" /><circle cx="8" cy="42" r="6" /><path d="M-2 42 H2" /></g>}
        <path d="M-6 52 Q0 56 6 52" stroke={C.ink} strokeWidth="2" fill="none" strokeLinecap="round" />
      </g>
    </svg>
  );
};

/* a dot = one applicant. good: would repay; state: 'none' | 'ok' | 'rej' */
export const Dot = ({ size = 34, good = true, fill = null, ring = null, mark = null, o = 1 }) => (
  <div style={{ width: size, height: size, borderRadius: size / 2, opacity: o,
    background: fill || (good ? '#DCEBE2' : '#E6E1D6'),
    border: `${Math.max(2, size / 10)}px solid ${ring || (good ? C.green : '#A9A296')}`,
    display: 'flex', alignItems: 'center', justifyContent: 'center',
    fontFamily: SANS, fontWeight: 700, fontSize: size * 0.55, color: fill ? C.card : C.mute, boxSizing: 'border-box' }}>{mark}</div>
);

export const Captions = ({ timing }) => {
  const frame = useCurrentFrame();
  const t = frame / FPS;
  const cur = timing.cues.find((c) => t >= c.start - 0.1 && t <= c.start + c.dur + 0.25);
  if (!cur) return null;
  const o = interpolate(t, [cur.start - 0.1, cur.start + 0.15, cur.start + cur.dur + 0.05, cur.start + cur.dur + 0.25], [0, 1, 1, 0], clamp);
  return (
    <div style={{ position: 'absolute', left: 0, right: 0, bottom: 40, display: 'flex', justifyContent: 'center', opacity: o }}>
      <div style={{ maxWidth: 1480, background: 'rgba(18,49,42,0.88)', color: C.light, fontFamily: SANS, fontSize: 32, lineHeight: 1.35, padding: '12px 30px', borderRadius: 14, textAlign: 'center' }}>
        {cur.text}
      </div>
    </div>
  );
};

/* Question with 8 s countdown that starts after the spoken question */
export const Quiz8 = ({ tm, n, q, a, question, options, good, optAt = 0.45, note, secs = 8 }) => {
  const frame = useCurrentFrame();
  const { F, cue, end } = tm;
  const tStart = end(q, 0.1);
  const p = interpolate(frame, [tStart, tStart + secs * FPS], [0, 1], clamp);
  const ans = useSpr(F(a, 0));
  const oAt = F(q, cue[q].dur * optAt);
  return (
    <AbsoluteFill style={{ background: C.light }}>
      <Pop at={F(q, 0)} style={{ left: 128, top: 90 }}><div style={{ fontFamily: SANS, fontWeight: 700, fontSize: 26, letterSpacing: 2, color: C.terra }}>TUSSENVRAAG {n}</div></Pop>
      <Pop at={F(q, 0.3)} style={{ left: 128, top: 140, width: 1580 }}><div style={{ fontFamily: SERIF, fontWeight: 600, fontSize: 54, lineHeight: 1.14, color: C.ink }}>{question}</div></Pop>
      <Pop at={oAt} style={{ left: 128, top: 420 }}>
        {options.map((o, i) => (
          <div key={i} style={{ fontFamily: SANS, fontSize: 34, padding: '20px 32px', borderRadius: 18, width: 1280, marginTop: 16, color: C.ink, lineHeight: 1.3,
            background: i === good ? mix(ans, C.card, '#E3F0E8') : C.card,
            border: `3px solid ${i === good && ans > 0.5 ? C.green : C.line}`, opacity: i === good ? 1 : 1 - 0.55 * ans }}>{o}</div>
        ))}
      </Pop>
      <Pop at={oAt} style={{ left: 1560, top: 440 }}>
        <svg width="220" height="220"><circle cx="110" cy="110" r="90" fill="none" stroke={C.line} strokeWidth="18" />
          <circle cx="110" cy="110" r="90" fill="none" stroke={C.terra} strokeWidth="18" strokeLinecap="round" strokeDasharray={`${565 * (1 - p)} 1000`} transform="rotate(-90 110 110)" />
          <text x="110" y="128" textAnchor="middle" fontSize="54" fontWeight="700" fontFamily={SERIF} fill={C.dark}>{p <= 0 ? secs : p < 1 ? Math.ceil(secs * (1 - p)) : '✓'}</text></svg>
        <div style={{ fontFamily: SANS, fontSize: 24, color: C.mute, textAlign: 'center', width: 220 }}>denktijd</div>
      </Pop>
      {note && <Banner at={F(a, 0.8)} top={800} size={38}>{note}</Banner>}
    </AbsoluteFill>
  );
};

export const TitleScene = ({ at, kicker, title, children }) => {
  const s = useSpr(at);
  return (
    <AbsoluteFill style={{ background: `radial-gradient(1200px 800px at 75% 30%, #1B4A3E 0%, ${C.dark} 60%)` }}>
      <div style={{ position: 'absolute', left: 140, top: 260, fontFamily: SANS, fontSize: 30, fontWeight: 700, letterSpacing: 3, color: C.amber, opacity: s }}>{kicker}</div>
      <div style={{ position: 'absolute', left: 140, top: 320, width: 1000, fontFamily: SERIF, fontWeight: 700, fontSize: 112, lineHeight: 1.04, color: C.light, opacity: s, transform: `translateY(${(1 - s) * 50}px)` }}>{title}</div>
      {children}
    </AbsoluteFill>
  );
};

export const SummaryScene = ({ tm, keys, title = 'Samengevat', items }) => {
  const { F } = tm;
  return (
    <AbsoluteFill style={{ background: C.light }}>
      <Heading at={F(keys[0], 0)}>{title}</Heading>
      {items.map((t, i) => (
        <Pop key={i} at={F(keys[i + 1], 0.1)} style={{ left: 128, top: 250 + i * 170, width: 1664 }}>
          <Card style={{ display: 'flex', gap: 30, alignItems: 'center', padding: '24px 36px' }}>
            <span style={{ fontFamily: SERIF, fontWeight: 700, fontSize: 70, color: C.amber, width: 60 }}>{i + 1}</span>
            <span style={{ fontFamily: SANS, fontWeight: 600, fontSize: 38, color: C.ink, lineHeight: 1.25 }}>{t}</span>
          </Card>
        </Pop>
      ))}
    </AbsoluteFill>
  );
};

export const Fade = ({ from, to, children }) => {
  const frame = useCurrentFrame();
  if (frame < from - 10 || frame > to + 10) return null;
  const o = interpolate(frame, [from - 8, from + 8, to - 8, to + 8], [0, 1, 1, 0], clamp);
  return <AbsoluteFill style={{ opacity: o }}>{children}</AbsoluteFill>;
};

export const ClipShell = ({ timing, scenes }) => {
  const [handle] = useState(() => delayRender('fonts'));
  useEffect(() => { document.fonts.ready.then(() => continueRender(handle)); }, [handle]);
  const { F } = makeF(timing);
  const end = Math.ceil(timing.total * FPS);
  return (
    <AbsoluteFill style={{ background: C.light }}>
      {scenes.map(([k, el], i) => {
        const from = i === 0 ? 0 : F(k, -0.4);
        const to = i + 1 < scenes.length ? F(scenes[i + 1][0], -0.4) : end + 20;
        return <Fade key={k + i} from={from} to={to}>{el}</Fade>;
      })}
      <Captions timing={timing} />
      {timing.cues.filter((c) => c.audio).map((c) => (
        <Sequence key={c.key} from={Math.round(c.start * FPS)} durationInFrames={Math.ceil((c.dur + 0.2) * FPS)}>
          <Audio src={staticFile(`${timing.audioDir}/${c.key}.mp3`)} />
        </Sequence>
      ))}
    </AbsoluteFill>
  );
};
