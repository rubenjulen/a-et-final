import React from 'react';
import { AbsoluteFill, useCurrentFrame, interpolate } from 'remotion';
import timing from './timing_c10.json';
import {
  C, SERIF, SANS, FPS, clamp, makeF, useSpr, mix, Pop, Card, Banner, Heading,
  Quiz8, TitleScene, SummaryScene, ClipShell, Shanti, Person,
} from './wk3kit';

const tm = makeF(timing);
const { F } = tm;

/* ---------- Intro ---------- */
const Intro = () => {
  const a = useSpr(F('i0', 0.8));
  return (
    <TitleScene at={F('i0', -0.3)} kicker="KENNISCLIP 10 · AI &amp; ETHICS · BLOK 1" title="Uitleg die werkt">
      <div style={{ position: 'absolute', left: 1220, top: 300, width: 560, opacity: a, transform: `translateY(${(1 - a) * 30}px)` }}>
        <div style={{ background: C.card, borderRadius: 22, padding: '26px 30px', fontFamily: SANS, fontSize: 30, color: C.ink, lineHeight: 1.35 }}>
          <div style={{ fontWeight: 700, color: C.terra, marginBottom: 8 }}>Suribank</div>
          Uw aanvraag is afgewezen.
          <div style={{ fontFamily: SERIF, fontWeight: 700, fontSize: 90, color: C.amber, textAlign: 'right', lineHeight: 1 }}>Waarom?</div>
        </div>
      </div>
    </TitleScene>
  );
};

/* ---------- Dia 1: three concepts ---------- */
const Sign = () => (
  <svg width="200" height="170" viewBox="0 0 200 170"><rect x="92" y="90" width="16" height="80" fill={C.dark} />
    <rect x="10" y="10" width="180" height="90" rx="14" fill={C.amber} /><text x="100" y="50" textAnchor="middle" fontFamily={SANS} fontWeight="700" fontSize="24" fill={C.dark}>AI IN</text>
    <text x="100" y="80" textAnchor="middle" fontFamily={SANS} fontWeight="700" fontSize="24" fill={C.dark}>GEBRUIK</text></svg>
);
const Qmark = () => (
  <svg width="200" height="170" viewBox="0 0 200 170"><circle cx="100" cy="85" r="78" fill={C.green} />
    <text x="100" y="122" textAnchor="middle" fontFamily={SERIF} fontWeight="700" fontSize="110" fill={C.card}>?</text></svg>
);
const Log = ({ frame, at }) => {
  const n = Math.floor(interpolate(frame, [at, at + 60], [0, 5], clamp));
  return (
    <svg width="200" height="170" viewBox="0 0 200 170"><rect x="30" y="8" width="140" height="156" rx="12" fill={C.card} stroke={C.dark} strokeWidth="5" />
      {[0, 1, 2, 3, 4].map((i) => <g key={i} opacity={i < n ? 1 : 0.15}><rect x="48" y={30 + i * 26} width="22" height="12" rx="3" fill={C.terra} /><rect x="78" y={32 + i * 26} width="74" height="8" rx="4" fill={C.mute} /></g>)}
    </svg>
  );
};
const Concepts = () => {
  const frame = useCurrentFrame();
  const tiles = [
    ['a1', 'Transparantie', 'Mensen weten dát AI wordt gebruikt, en waarvoor', <Sign />],
    ['a2', 'Uitlegbaarheid', 'Je kunt uitleggen waaróm deze uitkomst', <Qmark />],
    ['a3', 'Traceerbaarheid', 'Achteraf nagaan: welke gegevens, welke versie', <Log frame={frame} at={F('a3', 1.0)} />],
  ];
  return (
    <AbsoluteFill style={{ background: C.light }}>
      <Heading at={F('a1', -0.2)} kicker="DRIE BEGRIPPEN">Niet hetzelfde</Heading>
      {tiles.map(([k, t, d, icon], i) => (
        <Pop key={k} at={F(k, 0)} style={{ left: 128 + i * 560, top: 270, width: 520 }}>
          <Card style={{ height: 470, display: 'flex', flexDirection: 'column', alignItems: 'center', textAlign: 'center' }}>
            {icon}
            <div style={{ fontFamily: SERIF, fontWeight: 700, fontSize: 46, color: C.dark, marginTop: 18 }}>{t}</div>
            <div style={{ fontFamily: SANS, fontSize: 30, color: C.mute, marginTop: 12, lineHeight: 1.3 }}>{d}</div>
          </Card>
        </Pop>
      ))}
    </AbsoluteFill>
  );
};

/* ---------- Dia 2: two roads ---------- */
const Tree = ({ frame, at }) => {
  const step = (k) => interpolate(frame, [at + k * 25, at + k * 25 + 15], [0, 1], clamp);
  const node = (x, y, w, t, on) => (
    <g><rect x={x - w / 2} y={y - 32} width={w} height="64" rx="16" fill={on ? C.green : C.card} stroke={C.green} strokeWidth="4" />
      <text x={x} y={y + 10} textAnchor="middle" fontFamily={SANS} fontWeight="700" fontSize="26" fill={on ? C.card : C.ink}>{t}</text></g>
  );
  return (
    <svg width="700" height="420" viewBox="0 0 700 420">
      <path d="M350 70 L190 200 M350 70 L510 200 M190 200 L100 340 M190 200 L280 340" stroke={C.line} strokeWidth="6" />
      <path d="M350 70 L190 200" stroke={C.amber} strokeWidth="8" strokeDasharray="210" strokeDashoffset={210 * (1 - step(1))} />
      <path d="M190 200 L280 340" stroke={C.amber} strokeWidth="8" strokeDasharray="170" strokeDashoffset={170 * (1 - step(2))} />
      {node(350, 70, 340, 'Inkomen ≥ 15.000?', step(0) > 0.5)}
      {node(190, 200, 300, 'Looptijd ≤ 24 mnd?', step(1) > 0.5)}
      {node(510, 200, 160, 'Ja', false)}
      {node(100, 340, 150, 'Ja', false)}
      {node(280, 340, 150, 'Nee', step(2) > 0.5)}
      <text x="150" y="140" fontFamily={SANS} fontSize="22" fill={C.mute}>nee</text><text x="460" y="140" fontFamily={SANS} fontSize="22" fill={C.mute}>ja</text>
    </svg>
  );
};
const BlackBox = ({ frame, at }) => {
  const s = interpolate(frame, [at, at + 30], [0, 1], clamp);
  const jit = (i) => 0.75 + 0.25 * Math.sin(frame / 7 + i * 1.7);
  return (
    <div style={{ position: 'relative', width: 640, height: 420 }}>
      <div style={{ position: 'absolute', left: 30, top: 20, width: 300, height: 300, background: C.ink, borderRadius: 26, boxShadow: '0 20px 40px rgba(0,0,0,.25)', display: 'flex', alignItems: 'flex-start', justifyContent: 'center', paddingTop: 34, boxSizing: 'border-box', color: '#8A958F', fontFamily: SANS, fontSize: 26 }}>complex model</div>
      <svg style={{ position: 'absolute', left: 230, top: 160 }} width="140" height="140"><circle cx="55" cy="55" r="42" fill="rgba(246,243,236,.25)" stroke={C.amber} strokeWidth="10" /><path d="M86 86 L130 130" stroke={C.amber} strokeWidth="16" strokeLinecap="round" /></svg>
      <div style={{ position: 'absolute', left: 380, top: 40, width: 260, opacity: s }}>
        <div style={{ fontFamily: SANS, fontWeight: 700, fontSize: 22, color: C.mute, marginBottom: 8 }}>Belangrijkste factoren</div>
        {['inkomen', 'looptijd', 'werk', 'district'].map((f, i) => (
          <div key={f} style={{ marginTop: 12 }}>
            <div style={{ fontFamily: SANS, fontSize: 22, color: C.ink }}>{f}</div>
            <div style={{ height: 18, width: `${(90 - i * 18) * jit(i)}%`, background: C.terra, borderRadius: 9, opacity: 0.85, filter: 'blur(0.6px)' }} />
          </div>
        ))}
      </div>
    </div>
  );
};
const Roads = () => {
  const frame = useCurrentFrame();
  return (
    <AbsoluteFill style={{ background: C.light }}>
      <Heading at={F('b1', -0.2)} kicker="TWEE WEGEN NAAR UITLEG">Zelf te begrijpen, of achteraf uitgelegd</Heading>
      <Pop at={F('b1', 0.2)} style={{ left: 110, top: 260 }}>
        <div style={{ fontFamily: SANS, fontWeight: 700, fontSize: 28, color: C.green, marginBottom: 6 }}>1 · Beslisboom of puntentelling</div>
        <Tree frame={frame} at={F('b1', 2.5)} />
      </Pop>
      <Pop at={F('b2', 0)} style={{ left: 1040, top: 260 }}>
        <div style={{ fontFamily: SANS, fontWeight: 700, fontSize: 28, color: C.terra, marginBottom: 6 }}>2 · Complex model + uitleg achteraf</div>
        <BlackBox frame={frame} at={F('b2', 1.5)} />
      </Pop>
      <Pop at={F('b3', 0)} style={{ left: 1420, top: 650 }}>
        <div style={{ background: C.terra, color: C.card, fontFamily: SANS, fontWeight: 700, fontSize: 28, padding: '10px 24px', borderRadius: 999 }}>≈ een benadering</div>
      </Pop>
      <Banner at={F('b4', 0.2)} top={760} size={40}>Rudin: bij grote gevolgen <span style={{ color: C.amber }}>een model dat zelf te begrijpen is</span>.</Banner>
    </AbsoluteFill>
  );
};

/* ---------- Dia 3: explanation per audience ---------- */
const Audience = () => {
  const frame = useCurrentFrame();
  const people = [
    ['c1', 'Aanvrager', 'Welke factoren gaven de doorslag? Wat kan ik zelf doen?', 'shanti'],
    ['c2', 'Medewerker', 'Hoe zeker is het model? Wanneer wijk ik af?', { body: C.dark, tie: true }],
    ['c3', 'Toezichthouder', 'Hoe werkt het, hoe is het getest, werkt het voor alle groepen?', { body: C.terra, glasses: true, skin: '#A06A45' }],
  ];
  return (
    <AbsoluteFill style={{ background: C.light }}>
      <Heading at={F('c1', -0.2)} kicker="UITLEG PER DOELGROEP">Wie wil wat weten?</Heading>
      {people.map(([k, role, q, p], i) => (
        <Pop key={k} at={F(k, 0)} style={{ left: 128 + i * 560, top: 250, width: 520 }}>
          <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
            <div style={{ background: C.card, border: `2px solid ${C.line}`, borderRadius: '24px 24px 24px 6px', padding: '20px 26px', fontFamily: SANS, fontSize: 29, lineHeight: 1.3, color: C.ink, minHeight: 130, width: 460 }}>{q}</div>
            <div style={{ width: 230, height: 250, marginTop: 14 }}>
              {p === 'shanti' ? <div style={{ width: 230, height: 260 }}><Shanti frame={frame} label={false} /></div> : <Person size={210} frame={frame} {...p} />}
            </div>
            <div style={{ fontFamily: SERIF, fontWeight: 700, fontSize: 40, color: C.dark }}>{role}</div>
          </div>
        </Pop>
      ))}
      <Banner at={F('c4', 0.1)} top={770} size={42}>Eén uitleg voor iedereen <span style={{ color: C.amber }}>werkt niet</span>.</Banner>
    </AbsoluteFill>
  );
};

/* ---------- Dia 4: counterfactual ---------- */
const Letter = ({ head, body, tone, stamp }) => (
  <div style={{ width: 760, background: C.card, borderRadius: 18, border: `3px solid ${tone}`, padding: '26px 32px', boxShadow: '0 16px 36px rgba(18,49,42,.12)', position: 'relative' }}>
    <div style={{ fontFamily: SANS, fontWeight: 700, fontSize: 22, letterSpacing: 2, color: C.mute }}>SURIBANK · BESLUIT</div>
    <div style={{ fontFamily: SANS, fontSize: 30, color: C.ink, margin: '8px 0 12px' }}>{head}</div>
    <div style={{ fontFamily: SERIF, fontWeight: 600, fontSize: 36, color: C.ink, lineHeight: 1.25, background: mix(1, C.card, tone === C.terra ? '#F6E2DC' : '#E3F0E8'), padding: '10px 14px', borderRadius: 10 }}>{body}</div>
    {stamp}
  </div>
);
const Counter = () => {
  const frame = useCurrentFrame();
  const warn = useSpr(F('d4', 2.0));
  return (
    <AbsoluteFill style={{ background: C.light }}>
      <Heading at={F('d1', -0.2)} kicker="UITLEG MET EEN ALS-DAN">Wat had anders moeten zijn?</Heading>
      <Pop at={F('d1', 0.6)} style={{ left: 128, top: 260 }}>
        <Letter head="Uw aanvraag is afgewezen." tone={C.green} body="Als u een looptijd van 36 maanden had gekozen, was uw aanvraag goedgekeurd." />
      </Pop>
      <Pop at={F('d2', 0)} style={{ left: 128, top: 590 }}>
        <div style={{ display: 'flex', gap: 16 }}>
          {['contrafactisch', 'begrijpelijk', 'iets om mee te doen'].map((t, i) => (
            <span key={t} style={{ opacity: frame >= F(i === 0 ? 'd2' : 'd3', i * 0.8) ? 1 : 0, background: C.green, color: C.card, fontFamily: SANS, fontWeight: 700, fontSize: 28, padding: '10px 22px', borderRadius: 999 }}>✓ {t}</span>
          ))}
        </div>
      </Pop>
      <Pop at={F('d4', 0.6)} style={{ left: 1000, top: 330 }}>
        <Letter head="Uw aanvraag is afgewezen." tone={C.terra} body="Als u in Paramaribo had gewoond, was uw aanvraag goedgekeurd."
          stamp={<div style={{ position: 'absolute', right: -20, top: -30, transform: `rotate(8deg) scale(${0.6 + 0.4 * warn})`, opacity: warn, background: C.terra, color: C.card, fontFamily: SANS, fontWeight: 700, fontSize: 24, padding: '10px 18px', borderRadius: 12 }}>zegt iets over de eerlijkheid</div>} />
      </Pop>
    </AbsoluteFill>
  );
};

/* ---------- Dia 5: explanation enables control and objection ---------- */
const Control = () => {
  const frame = useCurrentFrame();
  const r = useSpr(F('e1', 0.8));
  return (
    <AbsoluteFill style={{ background: C.light }}>
      <Heading at={F('e1', -0.2)} kicker="UITLEG EN MENSELIJKE CONTROLE">Zonder uitleg geen controle</Heading>
      <Pop at={F('e1', 0.3)} style={{ left: 128, top: 260 }}>
        <div style={{ display: 'flex', gap: 24, alignItems: 'flex-end' }}>
          <Person size={180} frame={frame} body={C.dark} tie />
          <div style={{ width: 560, background: C.dark, borderRadius: 18, padding: '22px 28px', color: C.light, fontFamily: SANS }}>
            <div style={{ fontSize: 22, color: '#C9D8D1', letterSpacing: 2, fontWeight: 700 }}>SCHERM MEDEWERKER</div>
            <div style={{ fontFamily: SERIF, fontWeight: 700, fontSize: 64 }}>41% <span style={{ fontSize: 28, fontFamily: SANS, fontWeight: 400 }}>kans op terugbetalen</span></div>
            {['Kort dienstverband', 'Hoog bedrag t.o.v. inkomen', 'Eerdere achterstand'].map((t, i) => (
              <div key={t} style={{ fontSize: 28, marginTop: 8, opacity: interpolate(frame, [F('e1', 1.2 + i * 0.6), F('e1', 1.5 + i * 0.6)], [0, 1], clamp) }}>• {t}</div>
            ))}
          </div>
        </div>
      </Pop>
      <Pop at={F('e1', 2.6)} style={{ left: 1000, top: 300 }}>
        <div style={{ background: C.green, color: C.card, fontFamily: SANS, fontWeight: 700, fontSize: 34, padding: '20px 30px', borderRadius: 18 }}>↺ Medewerker wijkt bewust af</div>
      </Pop>
      <Pop at={F('e2', 0.2)} style={{ left: 1000, top: 440 }}>
        <div style={{ background: C.amber, color: C.dark, fontFamily: SANS, fontWeight: 700, fontSize: 34, padding: '20px 30px', borderRadius: 18 }}>✉ Aanvrager maakt bezwaar</div>
      </Pop>
      <Banner at={F('e3', 0.1)} top={760} size={40}>Uitleg is een <span style={{ color: C.amber }}>voorwaarde</span> voor menselijke controle en bezwaar.</Banner>
    </AbsoluteFill>
  );
};

export const Clip10 = () => (
  <ClipShell timing={timing} scenes={[
    ['i0', <Intro />], ['a1', <Concepts />], ['b1', <Roads />], ['c1', <Audience />], ['d1', <Counter />],
    ['q1', <Quiz8 tm={tm} n={1} q="q1" a="q1b" optAt={0.35} question="Welke uitleg is contrafactisch?" options={['A. “Uw score was 41%.”', 'B. “Met een looptijd van 24 in plaats van 12 maanden was uw aanvraag goedgekeurd.”']} good={1} />],
    ['e1', <Control />],
    ['q2', <Quiz8 tm={tm} n={2} q="q2" a="q2b" optAt={0.45} question="Een aanvrager hoort: “Uw woonplaats verlaagde uw score.” Wat is het probleem?" options={['A. Geen; het is eerlijke uitleg.', 'B. De aanvrager kan er niets aan doen, en het wijst op mogelijke ongelijke behandeling.']} good={1} />],
    ['z1', <SummaryScene tm={tm} keys={['z1', 'z2', 'z3', 'z4']} items={['Transparantie, uitlegbaarheid en traceerbaarheid zijn drie verschillende dingen', 'Bij grote gevolgen: liever een begrijpelijk model', 'Pas de uitleg aan de doelgroep aan; gebruik waar het kan een als-dan']} />],
  ]} />
);
