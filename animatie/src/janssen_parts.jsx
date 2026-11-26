// Gedeelde bouwstenen voor kennisclips in Janssen-huisstijl (vanaf clip 5c).
import React from 'react';
import { useCurrentFrame, interpolate, spring } from 'remotion';
import { FPS, clamp } from './wk1_kit';
import { J, FONT } from './janssen_kit';

export const sp = (frame, at, cfg = {}) => spring({ frame: frame - at, fps: FPS, config: { damping: 18, stiffness: 120, mass: 0.9, ...cfg } });
// Moment waarop een woord in de gesproken zin valt (benadering op tekstpositie).
export const makeW = (cue, F) => (key, word, off = 0) => {
  const c = cue[key]; const i = c.text.indexOf(word);
  if (i < 0) throw new Error(`woord "${word}" niet in ${key}`);
  return F(key, c.dur * i / c.text.length + off);
};
export const T = ({ children, size = 30, color = J.ink, weight = 400, style = {} }) => <div style={{ fontFamily: FONT, fontSize: size, color, fontWeight: weight, lineHeight: 1.25, ...style }}>{children}</div>;
export const Kick = ({ children, color = J.blue, style = {} }) => <div style={{ fontFamily: FONT, fontWeight: 700, fontSize: 24, letterSpacing: 2.5, color, textTransform: 'uppercase', ...style }}>{children}</div>;
export const Panel = ({ children, bg = J.card, style = {} }) => (
  <div style={{ position: 'absolute', inset: 0, background: bg, border: `2px solid ${J.line}`, borderRadius: 22, boxShadow: '0 12px 30px rgba(0,32,96,.07)', overflow: 'hidden', ...style }}>{children}</div>
);
export const Person = ({ x, y, s = 1, col = J.blue }) => (
  <g transform={`translate(${x},${y}) scale(${s})`}><circle cx="0" cy="-34" r="14" fill={col} /><path d="M-20 14 Q-20 -14 0 -16 Q20 -14 20 14 Z" fill={col} /></g>
);
// Wisselt tussen inhoud; items: [[startFrame, element], ...]
export const Switch = ({ items, style }) => {
  const frame = useCurrentFrame();
  return (
    <div style={{ position: 'absolute', ...style }}>
      {items.map(([a, el], i) => {
        const b = items[i + 1] ? items[i + 1][0] : 1e9;
        if (frame < a - 2 || frame > b + 12) return null;
        const o = interpolate(frame, [a, a + 10, b, b + 10], [0, 1, 1, 0], clamp);
        const y = (1 - interpolate(frame, [a, a + 14], [0, 1], clamp)) * 26;
        return <div key={i} style={{ position: 'absolute', inset: 0, opacity: o, transform: `translateY(${y}px)` }}>{el}</div>;
      })}
    </div>
  );
};
export const Bub = ({ at, children, me = false, size = 28, bg }) => {
  const frame = useCurrentFrame(); const s = sp(frame, at, { damping: 16, stiffness: 140 });
  return (<div style={{ display: 'flex', justifyContent: me ? 'flex-end' : 'flex-start', marginTop: 14, opacity: s, transform: `translateY(${(1 - s) * 16}px)` }}>
    <div style={{ maxWidth: 400, background: bg || (me ? J.dblue : J.ice), color: me ? '#fff' : J.ink, borderRadius: me ? '20px 20px 6px 20px' : '20px 20px 20px 6px', padding: '14px 20px', fontFamily: FONT, fontSize: size, lineHeight: 1.3 }}>{children}</div>
  </div>);
};
export const PhoneFrame = ({ title, sub, children, left = 170, top = 30, h = 500 }) => (
  <div style={{ position: 'absolute', left, top, width: 440, height: h, borderRadius: 44, background: J.navy, padding: 14 }}>
    <div style={{ width: '100%', height: '100%', borderRadius: 32, background: '#fff', overflow: 'hidden' }}>
      <div style={{ background: J.ice, padding: '20px 22px 12px', borderBottom: `2px solid ${J.line}` }}><T size={28} weight={700} color={J.navy}>{title}</T><T size={20} color={J.slate}>{sub}</T></div>
      <div style={{ padding: '4px 18px' }}>{children}</div>
    </div>
  </div>
);
export const IconDot = ({ children, col, size = 96, ring }) => (
  <div style={{ width: size, height: size, borderRadius: size / 2, background: col, border: ring ? `4px solid ${ring}` : 'none', boxSizing: 'border-box', display: 'flex', alignItems: 'center', justifyContent: 'center', boxShadow: '0 8px 20px rgba(0,32,96,.18)' }}>{children}</div>
);
