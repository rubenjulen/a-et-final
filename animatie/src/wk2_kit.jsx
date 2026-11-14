/* Gedeelde bouwstenen voor kennisclips 6-8 (week 2). Kopie van de stijl van Clip3/Clip4,
   als factory zodat elke clip zijn eigen timing gebruikt. */
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
export const ease = Easing.bezier(0.33, 1, 0.68, 1);
export const QUIZ_SECONDS = 8;

export const interpolateColor = (p, a, b) => {
  const h = (s) => [1, 3, 5].map((i) => parseInt(s.slice(i, i + 2), 16));
  const [x, y] = [h(a), h(b)];
  return `rgb(${x.map((v, i) => Math.round(v + (y[i] - v) * Math.min(1, Math.max(0, p)))).join(',')})`;
};

export const useSpring = (startFrame, cfg = {}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  return spring({ frame: frame - startFrame, fps, config: { damping: 18, stiffness: 120, mass: 0.9, ...cfg } });
};

/* Persoon (generiek, in de stijl van Shanti) */
export const Person = ({ color = C.green, skin = '#7A4A2E', hair = C.ink, size = 160, frame = 0, glow = false }) => {
  const b = 1 + 0.012 * Math.sin(frame / 18);
  return (
    <svg viewBox="-80 -10 160 230" width={size} height={size * 1.44}>
      {glow && <circle cx="0" cy="110" r="78" fill={C.amber} opacity="0.35" />}
      <g transform={`scale(1,${b})`} style={{ transformOrigin: '0px 220px' }}>
        <path d="M-62 220 Q-62 130 0 124 Q62 130 62 220 Z" fill={color} />
        <rect x="-11" y="96" width="22" height="30" fill={skin} />
        <circle cx="0" cy="64" r="42" fill={skin} />
        <path d="M-44 58 Q-40 14 0 16 Q40 14 44 58 Q32 36 0 38 Q-32 36 -44 58Z" fill={hair} />
        <circle cx="-14" cy="66" r="4.5" fill={C.ink} /><circle cx="14" cy="66" r="4.5" fill={C.ink} />
        <path d="M-12 84 Q0 92 12 84" stroke={C.ink} strokeWidth="3.5" fill="none" strokeLinecap="round" />
      </g>
    </svg>
  );
};

export const Phone = ({ title, sub, children, style = {}, h = 700 }) => (
  <div style={{ position: 'absolute', width: 540, height: h, borderRadius: 54, background: C.dark, padding: 16, boxShadow: '0 30px 60px rgba(18,49,42,.28)', ...style }}>
    <div style={{ width: '100%', height: '100%', borderRadius: 40, background: C.card, overflow: 'hidden', display: 'flex', flexDirection: 'column' }}>
      <div style={{ background: '#F0EBE1', padding: '28px 26px 16px', borderBottom: '2px solid #E2DACB' }}>
        <div style={{ fontFamily: SANS, fontWeight: 700, fontSize: 26, color: C.ink }}>{title}</div>
        <div style={{ fontFamily: SANS, fontSize: 20, color: C.mute }}>{sub}</div>
      </div>
      <div style={{ padding: '6px 22px', flex: 1 }}>{children}</div>
    </div>
  </div>
);
export const Bubble = ({ who, at, children, frame }) => {
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
        <div style={{ maxWidth: 430, background: me ? C.green : '#E6EEEA', color: me ? C.card : C.ink, borderRadius: me ? '20px 20px 6px 20px' : '20px 20px 20px 6px', padding: '14px 20px', fontFamily: SANS, fontSize: 24, lineHeight: 1.35, opacity: s, transform: `translateY(${(1 - s) * 16}px) scale(${0.9 + 0.1 * s})`, transformOrigin: me ? 'right bottom' : 'left bottom' }}>
          {children}
        </div>
      )}
    </div>
  );
};

/* Factory met timing-afhankelijke onderdelen */
export const makeKit = (timing) => {
  const cue = Object.fromEntries(timing.cues.map((c) => [c.key, c]));
  const F = (key, off = 0) => Math.round((cue[key].start + off) * FPS);
  const endOf = (key, off = 0) => Math.round((cue[key].start + cue[key].dur + off) * FPS);

  const Pop = ({ at, children, dy = 40, style = {} }) => {
    const s = useSpring(at);
    return <div style={{ position: 'absolute', opacity: s, transform: `translateY(${(1 - s) * dy}px) scale(${0.96 + 0.04 * s})`, ...style }}>{children}</div>;
  };
  const Card = ({ style, children }) => (
    <div style={{ background: C.card, border: `2px solid ${C.line}`, borderRadius: 22, padding: '26px 34px', boxShadow: '0 14px 34px rgba(18,49,42,.10)', ...style }}>{children}</div>
  );
  const Banner = ({ at, children, top = 740, size = 44 }) => (
    <Pop at={at} style={{ left: 128, top, width: 1664 }}>
      <div style={{ background: C.dark, borderRadius: 22, padding: '22px 40px', fontFamily: SERIF, fontWeight: 600, fontSize: size, color: C.light, lineHeight: 1.2 }}>{children}</div>
    </Pop>
  );
  const Title = ({ at, kicker, children, top = 96 }) => (
    <>
      {kicker && <Pop at={at} style={{ left: 128, top }}><div style={{ fontFamily: SANS, fontWeight: 700, fontSize: 24, letterSpacing: 2, color: C.terra, textTransform: 'uppercase' }}>{kicker}</div></Pop>}
      <Pop at={at + 4} style={{ left: 128, top: top + (kicker ? 40 : 0), width: 1660 }}><div style={{ fontFamily: SERIF, fontWeight: 700, fontSize: 62, lineHeight: 1.08, color: C.ink }}>{children}</div></Pop>
    </>
  );
  const Chips = ({ items, on, at = 0 }) => {
    const frame = useCurrentFrame();
    return (
      <div style={{ position: 'absolute', left: 128, top: 34, display: 'flex', gap: 12, opacity: interpolate(frame, [at, at + 12], [0, 1], clamp) }}>
        {items.map((n, i) => (
          <div key={n} style={{ fontFamily: SANS, fontSize: 21, fontWeight: 700, padding: '8px 20px', borderRadius: 999, background: i === on ? C.dark : C.sand, color: i === on ? C.amber : '#6B756F' }}>{n}</div>
        ))}
      </div>
    );
  };

  /* Tussenvraag: opties verschijnen met de gesproken vraag; aftelbalk start NA de vraag */
  const QuizN = ({ n, q, a, question, options, good, note }) => {
    const frame = useCurrentFrame();
    const tStart = endOf(q, 0.1);
    const p = interpolate(frame, [tStart, tStart + QUIZ_SECONDS * FPS], [0, 1], clamp);
    const ans = useSpring(F(a, 0));
    return (
      <AbsoluteFill style={{ background: C.light }}>
        <Pop at={F(q, 0)} style={{ left: 128, top: 96 }}><div style={{ fontFamily: SANS, fontWeight: 700, fontSize: 26, letterSpacing: 2, color: C.terra }}>{n ? `TUSSENVRAAG ${n}` : 'TUSSENVRAAG'}</div></Pop>
        <Pop at={F(q, 0.3)} style={{ left: 128, top: 150, width: 1360 }}><div style={{ fontFamily: SERIF, fontWeight: 600, fontSize: 52, lineHeight: 1.14, color: C.ink }}>{question}</div></Pop>
        <Pop at={F(q, 3)} style={{ left: 128, top: 470 }}>
          {options.map((o, i) => (
            <div key={o} style={{ fontFamily: SANS, fontSize: 32, lineHeight: 1.3, padding: '20px 30px', borderRadius: 18, width: 1300, marginTop: 16, color: C.ink,
              background: i === good ? interpolateColor(ans, C.card, '#E3F0E8') : C.card,
              border: `3px solid ${i === good && ans > 0.5 ? C.green : C.line}`, opacity: i === good ? 1 : 1 - 0.55 * ans }}>{o}</div>
          ))}
        </Pop>
        <Pop at={F(q, 3)} style={{ left: 1560, top: 470 }}>
          <svg width="220" height="220"><circle cx="110" cy="110" r="90" fill="none" stroke={C.line} strokeWidth="18" />
            <circle cx="110" cy="110" r="90" fill="none" stroke={C.terra} strokeWidth="18" strokeLinecap="round" strokeDasharray={`${565 * (1 - p)} 1000`} transform="rotate(-90 110 110)" />
            <text x="110" y="128" textAnchor="middle" fontSize="54" fontWeight="700" fontFamily={SERIF} fill={C.dark}>{p <= 0 ? QUIZ_SECONDS : p < 1 ? Math.ceil(QUIZ_SECONDS * (1 - p)) : '✓'}</text></svg>
          <div style={{ fontFamily: SANS, fontSize: 24, color: C.mute, textAlign: 'center', width: 220 }}>{p > 0 && p < 1 ? 'zet stil of denk na' : 'denktijd'}</div>
        </Pop>
        {note && <Banner at={F(a, 1.0)} top={800} size={36}>{note}</Banner>}
      </AbsoluteFill>
    );
  };

  /* Ondertitels; bij tussenvragen staat de vraag al groot in beeld */
  const Captions = () => {
    const frame = useCurrentFrame();
    const t = frame / FPS;
    const cur = timing.cues.find((c) => t >= c.start - 0.1 && t <= c.start + c.dur + 0.25);
    if (!cur || cur.key.startsWith('q')) return null;
    const o = interpolate(t, [cur.start - 0.1, cur.start + 0.15, cur.start + cur.dur + 0.05, cur.start + cur.dur + 0.25], [0, 1, 1, 0], clamp);
    return (
      <div style={{ position: 'absolute', left: 0, right: 0, bottom: 40, display: 'flex', justifyContent: 'center', opacity: o }}>
        <div style={{ maxWidth: 1500, background: 'rgba(18,49,42,0.88)', color: C.light, fontFamily: SANS, fontSize: cur.text.length > 150 ? 30 : 33, lineHeight: 1.34, padding: '12px 28px', borderRadius: 14, textAlign: 'center' }}>
          {cur.text}
        </div>
      </div>
    );
  };

  const Fade = ({ from, to, children }) => {
    const frame = useCurrentFrame();
    if (frame < from - 10 || frame > to + 10) return null;
    const o = interpolate(frame, [from - 8, from + 8, to - 8, to + 8], [0, 1, 1, 0], clamp);
    return <AbsoluteFill style={{ opacity: o }}>{children}</AbsoluteFill>;
  };

  const Composition = ({ scenes }) => {
    const [handle] = useState(() => delayRender('fonts'));
    useEffect(() => { document.fonts.ready.then(() => continueRender(handle)); }, [handle]);
    const end = Math.ceil(timing.total * FPS);
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

  /* Openings- en slotscène */
  const TitleScene = ({ n, title, sub, k = 't0' }) => {
    const frame = useCurrentFrame();
    const s = useSpring(F(k, 0));
    return (
      <AbsoluteFill style={{ background: C.dark }}>
        <div style={{ position: 'absolute', left: 128, top: 330, opacity: s, transform: `translateY(${(1 - s) * 30}px)` }}>
          <div style={{ fontFamily: SANS, fontWeight: 700, fontSize: 28, letterSpacing: 3, color: C.amber }}>KENNISCLIP {n} · WEEK 2</div>
          <div style={{ fontFamily: SERIF, fontWeight: 700, fontSize: 96, color: C.light, marginTop: 14, maxWidth: 1500, lineHeight: 1.05 }}>{title}</div>
          <div style={{ fontFamily: SANS, fontSize: 34, color: '#C9D6CF', marginTop: 22 }}>{sub}</div>
        </div>
        <div style={{ position: 'absolute', left: 128, top: 300, width: 8, height: 330 * Math.min(1, s), background: C.amber, marginLeft: -40 }} />
        <div style={{ position: 'absolute', right: 120, bottom: 110, fontFamily: SANS, fontSize: 24, color: '#9FB3A9', opacity: interpolate(frame, [20, 40], [0, 1], clamp) }}>AI &amp; Ethics (A-ET)</div>
      </AbsoluteFill>
    );
  };
  const Summary = ({ k, title, items, banner, bannerKey, cols = 3 }) => (
    <AbsoluteFill style={{ background: C.light }}>
      <Title at={F(k, 0)} kicker="Samengevat">{title}</Title>
      <div style={{ position: 'absolute', left: 128, top: 280, width: 1664, display: 'grid', gridTemplateColumns: `repeat(${cols}, 1fr)`, gap: 22 }}>
        {items.map((t, i) => (
          <Pop key={t} at={F(k, 0.8 + i * 0.45)} style={{ position: 'relative' }}>
            <Card style={{ display: 'flex', gap: 18, alignItems: 'center', padding: '22px 28px' }}>
              <span style={{ fontFamily: SERIF, fontWeight: 700, fontSize: 52, color: C.amber }}>{i + 1}</span>
              <span style={{ fontFamily: SANS, fontWeight: 700, fontSize: 30, color: C.ink }}>{t}</span>
            </Card>
          </Pop>
        ))}
      </div>
      {banner && <Banner at={F(bannerKey, 0.2)} top={700} size={40}>{banner}</Banner>}
    </AbsoluteFill>
  );

  return { cue, F, endOf, Pop, Card, Banner, Title, Chips, QuizN, Captions, Fade, Composition, TitleScene, Summary };
};
