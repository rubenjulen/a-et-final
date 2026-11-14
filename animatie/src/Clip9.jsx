import React from 'react';
import { AbsoluteFill, useCurrentFrame, interpolate, spring } from 'remotion';
import timing from './timing_c9.json';
import {
  C, SERIF, SANS, FPS, clamp, makeF, useSpr, mix, Pop, Card, Banner, Heading, Dot,
  Quiz8, TitleScene, SummaryScene, ClipShell, Shanti,
} from './wk3kit';

const tm = makeF(timing);
const { F } = tm;

/* ---------- Intro ---------- */
const Intro = () => {
  const frame = useCurrentFrame();
  const r = interpolate(frame, [F('i0', 0.3), F('i0', 2.2)], [0, 69], clamp);
  return (
    <TitleScene at={F('i0', -0.3)} kicker="KENNISCLIP 9 · AI &amp; ETHICS · WEEK 3" title="Fouten per groep">
      <div style={{ position: 'absolute', left: 1260, top: 250 }}>
        <svg width="460" height="460"><circle cx="230" cy="230" r="180" fill="none" stroke="rgba(246,243,236,.15)" strokeWidth="40" />
          <circle cx="230" cy="230" r="180" fill="none" stroke={C.amber} strokeWidth="40" strokeDasharray={`${1131 * r / 100} 2000`} transform="rotate(-90 230 230)" />
          <text x="230" y="250" textAnchor="middle" fontFamily={SERIF} fontWeight="700" fontSize="110" fill={C.light}>{Math.round(r)}%</text>
          <text x="230" y="305" textAnchor="middle" fontFamily={SANS} fontSize="30" fill="#C9D8D1">goed</text></svg>
      </div>
    </TitleScene>
  );
};

/* ---------- Dia 1: the average hides ---------- */
const Average = () => {
  const frame = useCurrentFrame();
  const n = interpolate(frame, [F('a1', 0.2), F('a1', 1.6)], [0, 69], clamp);
  const split = useSpr(F('a2', 0.6));
  const gs = useSpr(F('a3', 0.3));
  const gsBar = interpolate(frame, [F('a3', 2.0), F('a3', 3.6)], [0, 35], clamp);
  const bar = (label, pct, col, i) => (
    <div key={label} style={{ display: 'flex', alignItems: 'center', gap: 24, marginTop: 18 }}>
      <div style={{ width: 210, fontFamily: SANS, fontWeight: 700, fontSize: 30, color: C.ink }}>{label}</div>
      <div style={{ width: 640, height: 44, background: C.sand, borderRadius: 22, overflow: 'hidden' }}>
        <div style={{ width: `${pct * split}%`, height: '100%', background: col, borderRadius: 22 }} />
      </div>
    </div>
  );
  return (
    <AbsoluteFill style={{ background: C.light }}>
      <Pop at={F('a1', 0)} style={{ left: 128, top: 110 }}>
        <div style={{ fontFamily: SANS, fontWeight: 700, fontSize: 26, letterSpacing: 2, color: C.green }}>SURIBANK · HET HELE MODEL</div>
        <div style={{ fontFamily: SERIF, fontWeight: 700, fontSize: 150, color: C.dark, lineHeight: 1 }}>{Math.round(n)}% <span style={{ fontSize: 56, fontWeight: 600 }}>goed</span></div>
      </Pop>
      <Pop at={F('a2', 0.3)} style={{ left: 128, top: 360 }}>
        <div style={{ fontFamily: SANS, fontSize: 28, color: C.mute, marginBottom: 6 }}>Maar per groep?</div>
        {bar('Groep 1', 82, C.green, 0)}
        {bar('Groep 2', 51, C.terra, 1)}
        <div style={{ fontFamily: SANS, fontSize: 24, color: C.mute, marginTop: 12 }}>(voorbeeld)</div>
      </Pop>
      <Pop at={F('a3', 0)} style={{ left: 1150, top: 300, width: 640, opacity: gs }}>
        <Card>
          <div style={{ fontFamily: SANS, fontWeight: 700, fontSize: 24, letterSpacing: 2, color: C.terra }}>GENDER SHADES</div>
          <div style={{ fontFamily: SERIF, fontWeight: 600, fontSize: 40, color: C.ink, margin: '8px 0 18px' }}>Gemiddeld prima.</div>
          <div style={{ fontFamily: SANS, fontSize: 28, color: C.mute }}>Eén groep: foute uitkomsten</div>
          <div style={{ display: 'flex', alignItems: 'center', gap: 20, marginTop: 10 }}>
            <div style={{ width: 380, height: 40, background: C.sand, borderRadius: 20, overflow: 'hidden' }}>
              <div style={{ width: `${gsBar / 50 * 100}%`, height: '100%', background: C.terra }} />
            </div>
            <div style={{ fontFamily: SERIF, fontWeight: 700, fontSize: 56, color: C.terra }}>{Math.round(gsBar)}%</div>
          </div>
        </Card>
      </Pop>
      <Banner at={F('a4', 0)} top={720}>Daarom meet je <span style={{ color: C.amber }}>fouten per groep</span>.</Banner>
    </AbsoluteFill>
  );
};

/* ---------- Dia 2: three questions per group ---------- */
// 20 applicants: good payers (repay) and not; model decision
const crowd = Array.from({ length: 20 }, (_, i) => {
  const good = [0, 1, 2, 3, 5, 6, 8, 9, 11, 12, 14, 17].includes(i);
  const approved = [0, 1, 3, 5, 8, 9, 12, 14, 4, 15].includes(i);
  return { good, approved };
});
const ThreeQ = () => {
  const frame = useCurrentFrame();
  const stage = frame >= F('b4', 0) ? 3 : frame >= F('b3', 0) ? 2 : frame >= F('b2', 0) ? 1 : 0;
  const cards = [
    ['b2', '1', 'Welk deel wordt goedgekeurd?', C.green],
    ['b3', '2', 'Goede betalers: welk deel onterecht afgewezen?', C.terra],
    ['b4', '3', 'Geen betalers: welk deel onterecht goedgekeurd?', C.amber],
  ];
  return (
    <AbsoluteFill style={{ background: C.light }}>
      <Heading at={F('b1', 0)} kicker="PER GROEP">Stel drie vragen</Heading>
      <Pop at={F('b1', 0.4)} style={{ left: 128, top: 270 }}>
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(5, 92px)', gap: 18 }}>
          {crowd.map((p, i) => {
            const hl = (stage === 1 && p.approved) || (stage === 2 && p.good && !p.approved) || (stage === 3 && !p.good && p.approved);
            const col = stage === 1 ? C.green : stage === 2 ? C.terra : C.amber;
            const o = stage === 0 || hl ? 1 : 0.3;
            return <Dot key={i} size={80} good={p.good} o={o} fill={hl ? col : null} ring={hl ? col : null} mark={stage > 0 ? (p.approved ? '✓' : '✗') : null} />;
          })}
        </div>
        <div style={{ display: 'flex', flexDirection: 'column', gap: 6, marginTop: 22, fontFamily: SANS, fontSize: 24, color: C.mute }}>
          <span><b style={{ color: C.green }}>●</b> zou terugbetalen</span><span><b style={{ color: '#A9A296' }}>●</b> zou niet terugbetalen</span><span>✓ / ✗ besluit model</span>
        </div>
      </Pop>
      {cards.map(([k, n, t, col]) => (
        <Pop key={k} at={F(k, 0.1)} style={{ left: 760, top: 300 + (Number(n) - 1) * 150, width: 1030 }}>
          <Card style={{ display: 'flex', gap: 26, alignItems: 'center', padding: '20px 30px', borderColor: frame >= F(k, 0) ? col : C.line }}>
            <span style={{ fontFamily: SERIF, fontWeight: 700, fontSize: 60, color: col, width: 44 }}>{n}</span>
            <span style={{ fontFamily: SANS, fontWeight: 600, fontSize: 34, color: C.ink }}>{t}</span>
          </Card>
        </Pop>
      ))}
    </AbsoluteFill>
  );
};

/* ---------- Dia 3: X vs Y ---------- */
const Grid100 = ({ red, at, label, color }) => {
  const frame = useCurrentFrame();
  const k = Math.round(interpolate(frame, [at, at + 40], [0, red], clamp));
  return (
    <div>
      <div style={{ fontFamily: SANS, fontWeight: 700, fontSize: 32, color: C.ink, marginBottom: 12 }}>{label} <span style={{ fontWeight: 400, color: C.mute, fontSize: 26 }}>· 100 goede betalers</span></div>
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(10, 34px)', gap: 8 }}>
        {Array.from({ length: 100 }, (_, i) => <Dot key={i} size={34} good fill={i < k ? color : null} ring={i < k ? color : null} />)}
      </div>
      <div style={{ fontFamily: SERIF, fontWeight: 700, fontSize: 72, color: k ? color : C.mute, marginTop: 12 }}>{k}% <span style={{ fontFamily: SANS, fontWeight: 400, fontSize: 28 }}>onterecht afgewezen</span></div>
    </div>
  );
};
const XY = () => {
  const frame = useCurrentFrame();
  const badge = useSpr(F('c3', 0.4));
  return (
    <AbsoluteFill style={{ background: C.light }}>
      <Heading at={F('c1', -0.2)} kicker="REKENVOORBEELD">Twee groepen, elk 100 goede betalers</Heading>
      <Pop at={F('c1', 0.2)} style={{ left: 160, top: 270 }}><Grid100 red={20} at={F('c1', 1.0)} label="Groep X" color={C.amber} /></Pop>
      <Pop at={F('c1', 0.5)} style={{ left: 1100, top: 270 }}><Grid100 red={40} at={F('c2', 0.3)} label="Groep Y" color={C.terra} /></Pop>
      <div style={{ position: 'absolute', left: 735, top: 420, width: 300, textAlign: 'center', opacity: badge, transform: `scale(${0.7 + 0.3 * badge})` }}>
        <div style={{ background: C.dark, color: C.amber, fontFamily: SERIF, fontWeight: 700, fontSize: 64, borderRadius: 24, padding: '16px 0' }}>2×</div>
        <div style={{ fontFamily: SANS, fontSize: 26, color: C.ink, marginTop: 10 }}>zoveel kans op een onterecht nee</div>
      </div>
      <Banner at={F('c4', 0.2)} top={830} size={40}><span style={{ color: C.amber }}>Gelijke kansen:</span> goede betalers hebben in elke groep dezelfde kans.</Banner>
    </AbsoluteFill>
  );
};

/* ---------- Dia 4: three scales ---------- */
const Scale = ({ tilt, color }) => (
  <svg width="300" height="230" viewBox="0 0 300 230">
    <rect x="144" y="40" width="12" height="160" fill={C.dark} /><rect x="95" y="196" width="110" height="16" rx="8" fill={C.dark} />
    <g transform={`rotate(${tilt} 150 46)`}>
      <rect x="30" y="40" width="240" height="10" rx="5" fill={color} />
      <path d="M50 50 L20 120 H80 Z" fill="none" stroke={color} strokeWidth="4" /><path d="M14 120 Q50 150 86 120Z" fill={color} />
      <path d="M250 50 L220 120 H280 Z" fill="none" stroke={color} strokeWidth="4" /><path d="M214 120 Q250 150 286 120Z" fill={color} />
    </g>
    <circle cx="150" cy="44" r="12" fill={C.amber} />
  </svg>
);
const Scales = () => {
  const frame = useCurrentFrame();
  const wob = frame >= F('d5', 0) ? Math.sin((frame - F('d5', 0)) / 4) * 9 * interpolate(frame, [F('d5', 0), F('d5', 4)], [1, 0.4], clamp) : 0;
  const items = [['d2', 'Elke groep even vaak goedgekeurd'], ['d3', 'Goede betalers even weinig onterecht afgewezen'], ['d4', 'Een goedkeuring overal even betrouwbaar']];
  const no = useSpr(F('d5', 1.5));
  return (
    <AbsoluteFill style={{ background: C.light }}>
      <Heading at={F('d1', 0)} kicker="WELKE EERLIJKHEID?">Meerdere definities van eerlijk</Heading>
      {items.map(([k, t], i) => (
        <Pop key={k} at={F(k, 0)} style={{ left: 150 + i * 560, top: 270, width: 480 }}>
          <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
            <Scale tilt={wob * (i === 1 ? -1 : 1)} color={[C.green, C.terra, C.amber][i]} />
            <div style={{ fontFamily: SANS, fontWeight: 600, fontSize: 32, textAlign: 'center', color: C.ink, marginTop: 10 }}>{t}</div>
          </div>
        </Pop>
      ))}
      <div style={{ position: 'absolute', left: 460, top: 650, width: 1000, textAlign: 'center', opacity: no, transform: `scale(${0.8 + 0.2 * no})` }}>
        <span style={{ display: 'inline-block', background: C.terra, color: C.card, fontFamily: SANS, fontWeight: 700, fontSize: 34, borderRadius: 999, padding: '12px 34px' }}>✗ Niet alle drie tegelijk, als groepen verschillen</span>
      </div>
      <Banner at={F('d6', 0.2)} top={780} size={42}>Kiezen en onderbouwen: <span style={{ color: C.amber }}>een ethische keuze</span>, geen technische.</Banner>
    </AbsoluteFill>
  );
};

/* ---------- Dia 5: more accurate and less fair ---------- */
// group of 20: 8 would repay (<half)
const grp = Array.from({ length: 20 }, (_, i) => ({ good: [1, 4, 6, 9, 11, 14, 16, 19].includes(i) }));
const Meter = ({ label, value, color, at }) => {
  const frame = useCurrentFrame();
  const v = interpolate(frame, [at, at + 45], [0, value], clamp);
  return (
    <div style={{ marginTop: 26 }}>
      <div style={{ display: 'flex', justifyContent: 'space-between', fontFamily: SANS, fontSize: 30, fontWeight: 700, color: C.ink, width: 700 }}><span>{label} ↑</span><span style={{ color }}>{Math.round(v)}%</span></div>
      <div style={{ width: 700, height: 40, background: C.sand, borderRadius: 20, overflow: 'hidden', marginTop: 8 }}><div style={{ width: `${v}%`, height: '100%', background: color }} /></div>
    </div>
  );
};
const Paradox = () => {
  const frame = useCurrentFrame();
  const rejAll = frame >= F('e2', 0.8);
  const pay = frame >= F('e3', 0.2);
  return (
    <AbsoluteFill style={{ background: C.light }}>
      <Heading at={F('e1', 0)} kicker="NAUWKEURIGER EN ONEERLIJKER">Minder dan de helft betaalt terug</Heading>
      <Pop at={F('e1', 0.5)} style={{ left: 128, top: 290 }}>
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(5, 92px)', gap: 18 }}>
          {grp.map((p, i) => <Dot key={i} size={80} good={p.good} fill={pay && p.good ? C.terra : null} ring={pay && p.good ? C.terra : null} mark={rejAll ? '✗' : null} />)}
        </div>
        <div style={{ fontFamily: SANS, fontSize: 24, color: C.mute, marginTop: 18 }}>8 van de 20 zouden terugbetalen · het model wijst iedereen af</div>
      </Pop>
      <Pop at={F('e2', 1.4)} style={{ left: 900, top: 300 }}>
        <Meter label="Nauwkeurigheid voor deze groep" value={60} color={C.green} at={F('e2', 1.6)} />
        <Meter label="Goede betalers onterecht afgewezen" value={100} color={C.terra} at={F('e3', 0.4)} />
      </Pop>
      <Banner at={F('e4', 0.2)} top={760} size={42}>Nauwkeuriger ≠ eerlijker. <span style={{ color: C.amber }}>In practicum 2 zie je het zelf.</span></Banner>
    </AbsoluteFill>
  );
};

export const Clip9 = () => (
  <ClipShell timing={timing} scenes={[
    ['i0', <Intro />], ['a1', <Average />], ['b1', <ThreeQ />], ['c1', <XY />],
    ['q1', <Quiz8 tm={tm} n={1} q="q1" a="q1b" optAt={0.62} question="In het binnenland zijn er 50 goede betalers. Het model wijst er 15 af. Hoeveel procent is onterecht afgewezen?" options={['A. 15%', 'B. 30%', 'C. 50%']} good={1} note={<>15 van de 50 = <span style={{ color: C.amber }}>30%</span></>} />],
    ['d1', <Scales />], ['e1', <Paradox />],
    ['q2', <Quiz8 tm={tm} n={2} q="q2" a="q2b" optAt={0.55} question="Een nieuw model is nauwkeuriger dan het oude. Is het daarmee ook eerlijker?" options={['A. Ja', 'B. Niet per se: kijk naar de fouten per groep']} good={1} />],
    ['z1', <SummaryScene tm={tm} keys={['z1', 'z2', 'z3', 'z4']} items={['Meet per groep: goedgekeurd, onterecht afgewezen, onterecht goedgekeurd', 'Er zijn meerdere definities van eerlijk: kies en onderbouw', 'Nauwkeuriger is niet hetzelfde als eerlijker']} />],
  ]} />
);
