// Janssen-huisstijl voor nieuwe kennisclips (clip 5b en later): palet en lettertype van de collegedecks.
// Generieke animatiehulpen komen uit wk1_kit; hier alleen wat van kleur of lettertype afhangt.
import React, { useEffect, useState } from 'react';
import { AbsoluteFill, Audio, Sequence, staticFile, useCurrentFrame, interpolate, delayRender, continueRender } from 'remotion';
import { FPS, clamp, useSpring, Pop, Fade, interpolateColor } from './wk1_kit';

export const J = {
  navy: '#002060', blue: '#3F82BA', dblue: '#2E5597', ice: '#EAF0F8', bg: '#F5F8FC', card: '#FFFFFF',
  ink: '#25282A', slate: '#5B6B7F', gold: '#C8A24A', green: '#1F7A4D', red: '#B3261E', line: '#D6DFEB',
  onNavy: '#FFFFFF', onNavyMuted: '#C9D5E8',
};
export const FONT = "Carlito, Calibri, 'Public Sans', Arial, sans-serif";

export const JTitle = ({ at, children, top = 70, size = 60, kicker, kcol = J.blue, left = 128, width = 1664 }) => (
  <Pop at={at} style={{ left, top, width }}>
    {kicker && <div style={{ fontFamily: FONT, fontWeight: 700, fontSize: 26, letterSpacing: 2.5, color: kcol, marginBottom: 6, textTransform: 'uppercase' }}>{kicker}</div>}
    <div style={{ fontFamily: FONT, fontWeight: 700, fontSize: size, lineHeight: 1.08, color: J.navy }}>{children}</div>
  </Pop>
);
export const JBanner = ({ at, children, top = 760, left = 128, width = 1664, size = 44 }) => (
  <Pop at={at} style={{ left, top, width }}>
    <div style={{ background: J.navy, borderRadius: 18, padding: '22px 38px', fontFamily: FONT, fontWeight: 700, fontSize: size, color: J.onNavy, lineHeight: 1.2 }}>{children}</div>
  </Pop>
);

export const makeJKit = (timing) => {
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
      <div style={{ position: 'absolute', left: 0, right: 0, bottom: 40, display: 'flex', justifyContent: 'center', opacity: o }}>
        <div style={{ maxWidth: 1500, background: 'rgba(0,32,96,0.90)', color: J.onNavy, fontFamily: FONT, fontSize: 34, lineHeight: 1.3, padding: '12px 30px', borderRadius: 12, textAlign: 'center' }}>{cur.text}</div>
      </div>
    );
  };

  const QuizN = ({ n, q, a, question, options, good, note, secs = 8 }) => {
    const frame = useCurrentFrame();
    const tStart = end(q) + 3;
    const p = interpolate(frame, [tStart, tStart + secs * FPS], [0, 1], clamp);
    const ans = useSpring(F(a, 0));
    return (
      <AbsoluteFill style={{ background: J.bg }}>
        <Pop at={F(q, 0)} style={{ left: 128, top: 90 }}><div style={{ fontFamily: FONT, fontWeight: 700, fontSize: 28, letterSpacing: 2.5, color: J.blue }}>TUSSENVRAAG {n}</div></Pop>
        <Pop at={F(q, 0.3)} style={{ left: 128, top: 140, width: 1380 }}><div style={{ fontFamily: FONT, fontWeight: 700, fontSize: 52, lineHeight: 1.14, color: J.navy }}>{question}</div></Pop>
        <Pop at={F(q, 1.2)} style={{ left: 128, top: 400 }}>
          {options.map((o, i) => (
            <div key={o} style={{ fontFamily: FONT, fontSize: 38, padding: '16px 30px', borderRadius: 16, width: 1250, marginTop: 16, color: J.ink,
              background: i === good ? interpolateColor(ans, J.card, '#E2F1E8') : J.card,
              border: `3px solid ${i === good && ans > 0.5 ? J.green : J.line}`, opacity: i === good ? 1 : 1 - 0.55 * ans }}>{o}</div>
          ))}
        </Pop>
        <Pop at={F(q, 1.2)} style={{ left: 1560, top: 400 }}>
          <svg width="220" height="220"><circle cx="110" cy="110" r="90" fill="none" stroke={J.line} strokeWidth="18" />
            <circle cx="110" cy="110" r="90" fill="none" stroke={J.blue} strokeWidth="18" strokeLinecap="round" strokeDasharray={`${565 * (1 - p)} 1000`} transform="rotate(-90 110 110)" />
            <text x="110" y="128" textAnchor="middle" fontSize="58" fontWeight="700" fontFamily={FONT} fill={J.navy}>{p <= 0 ? secs : p < 1 ? Math.ceil(secs * (1 - p)) : '✓'}</text></svg>
          <div style={{ fontFamily: FONT, fontSize: 26, color: J.slate, textAlign: 'center', width: 220 }}>denktijd</div>
        </Pop>
        {note && <JBanner at={F(a, 1.0)} top={430 + options.length * 96} size={40}>{note}</JBanner>}
      </AbsoluteFill>
    );
  };

  const Root = ({ scenes }) => {
    const [handle] = useState(() => delayRender('fonts'));
    useEffect(() => { document.fonts.ready.then(() => continueRender(handle)); }, [handle]);
    const last = Math.ceil(timing.total * FPS);
    return (
      <AbsoluteFill style={{ background: J.bg }}>
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
