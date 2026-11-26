import React from 'react';
import { AbsoluteFill, useCurrentFrame, interpolate } from 'remotion';
import timing from './timing_kC.json';
import {
  C, SERIF, SANS, FPS, clamp, makeF, useSpr, mix, Pop, Card, Banner, Heading,
  Quiz8, TitleScene, ClipShell, Shanti, Person,
} from './wk3kit_j';
import { Bubble, Phone } from './wk3kit_j';

const tm = makeF(timing);
const { F, cue } = tm;
/* frame at a fraction of a sentence, so animations move along when the real audio is longer or shorter */
const Fr = (k, p = 0) => F(k, cue[k].dur * p);
const on = (frame, k, p = 0) => frame >= Fr(k, p);

const LAYERS = [
  { short: 'Onaanvaardbaar', name: 'Onaanvaardbaar risico', rule: 'Verboden · art. 5', ex: 'Sociale score voor burgers · kwetsbaarheid uitbuiten', col: C.terra, k: 'C2b' },
  { short: 'Hoog risico', name: 'Hoog risico', rule: 'Strenge eisen · bijlage III', ex: 'Kredietwaardigheid · werving · onderwijs · uitkeringen', col: '#A9852E', k: 'C2c' },
  { short: 'Beperkt risico', name: 'Beperkt risico', rule: 'Transparantieplicht · art. 50', ex: 'Chatbot · orderagent: "ik ben een AI"', col: C.amber, k: 'C2d' },
  { short: 'Minimaal risico', name: 'Minimaal risico', rule: 'Geen extra eisen', ex: 'Spamfilter · spellingscontrole', col: C.green, k: 'C2e' },
];

/* pyramid made of four trapezoid layers; active = index to highlight */
const Pyramid = ({ x, y, w = 760, h = 520, show = [1, 1, 1, 1], active = -1, labels = true, size = 1 }) => {
  const lh = h / 4;
  return (
    <svg width={w} height={h} style={{ position: 'absolute', left: x, top: y, overflow: 'visible' }}>
      {LAYERS.map((L, i) => {
        const top = i * lh, bot = top + lh - 8;
        const wt = (w * (i + 1.4)) / 5.4, wb = (w * (i + 2.4)) / 5.4;
        const cx = w / 2;
        const o = show[i];
        const dim = active >= 0 && active !== i ? 0.35 : 1;
        return (
          <g key={L.name} opacity={o * dim} transform={`translate(0 ${(1 - o) * 30})`}>
            <path d={`M${cx - wt / 2} ${top} L${cx + wt / 2} ${top} L${cx + wb / 2} ${bot} L${cx - wb / 2} ${bot} Z`} fill={L.col} />
            {labels && <text x={cx} y={top + lh / 2 + 8} textAnchor="middle" fontFamily={SANS} fontWeight="700" fontSize={(i === 0 ? 20 : 27) * size} fill={i === 2 ? C.ink : C.card}>{L.short}</text>}
          </g>
        );
      })}
    </svg>
  );
};

/* ---------- C0: title ---------- */
const Title = () => {
  const frame = useCurrentFrame();
  const s = useSpr(F('C0', 0.6));
  return (
    <TitleScene at={F('C0', -0.3)} kicker="KADERCLIP C · AI &amp; ETHICS · BLOK 1" title="De AI-verordening: risicoklasse en rol">
      <div style={{ position: 'absolute', left: 1240, top: 170, width: 420, height: 480, opacity: s }}><Shanti frame={frame} /></div>
      <div style={{ position: 'absolute', left: 1180, top: 690, width: 540, opacity: s, transform: `translateY(${(1 - s) * 30}px)` }}>
        <div style={{ background: C.card, borderRadius: 18, padding: '16px 22px', fontFamily: SANS, fontSize: 24, color: C.ink, boxShadow: '0 14px 30px rgba(0,0,0,.25)' }}>
          <b>Suribank</b> · kredietaanvraag Shanti
        </div>
        <div style={{ marginTop: 14, marginLeft: 60, background: '#EAF0F8', borderRadius: '20px 20px 20px 6px', padding: '14px 20px', fontFamily: SANS, fontSize: 24, color: C.ink, boxShadow: '0 14px 30px rgba(0,0,0,.25)' }}>
          <b>Frisco Installaties</b> · "Ik ben een AI-assistent."
        </div>
      </div>
    </TitleScene>
  );
};

/* ---------- C0b/C0c: register vs law, goals ---------- */
const Goal = () => {
  const frame = useCurrentFrame();
  const goals = ['Jullie oplossing indelen in een risicoklasse', 'De rol van jullie partner benoemen', 'Uitleggen waarom de klasse geen eindoordeel is'];
  return (
    <AbsoluteFill style={{ background: C.light }}>
      <Heading at={F('C0b', 0)} kicker="WAT JE AL HEBT, EN WAT ERBIJ KOMT">Twee vragen over hetzelfde systeem</Heading>
      <Pop at={Fr('C0b', 0.05)} style={{ left: 128, top: 300, width: 800 }}>
        <Card style={{ borderLeft: `10px solid ${C.green}` }}>
          <div style={{ fontFamily: SANS, fontWeight: 700, fontSize: 24, color: C.green, letterSpacing: 1 }}>JULLIE RISICOREGISTER (K6)</div>
          <div style={{ fontFamily: SERIF, fontWeight: 600, fontSize: 44, color: C.ink, marginTop: 8 }}>Wat kan er misgaan?</div>
        </Card>
      </Pop>
      <Pop at={Fr('C0b', 0.5)} style={{ left: 990, top: 300, width: 800 }}>
        <Card style={{ borderLeft: `10px solid ${C.terra}` }}>
          <div style={{ fontFamily: SANS, fontWeight: 700, fontSize: 24, color: C.terra, letterSpacing: 1 }}>DE AI-VERORDENING (EU)</div>
          <div style={{ fontFamily: SERIF, fontWeight: 600, fontSize: 44, color: C.ink, marginTop: 8 }}>Hoe zwaar weegt de wet het?</div>
        </Card>
      </Pop>
      {goals.map((g, i) => (
        <Pop key={g} at={Fr('C0c', 0.12 + i * 0.27)} style={{ left: 128 + i * 560, top: 560, width: 520 }}>
          <div style={{ background: C.dark, color: C.light, borderRadius: 20, padding: '22px 26px', fontFamily: SANS, fontWeight: 600, fontSize: 28, lineHeight: 1.3, minHeight: 120, display: 'flex', gap: 16 }}>
            <span style={{ fontFamily: SERIF, fontSize: 48, color: C.amber, lineHeight: 1 }}>{i + 1}</span><span>{g}</span>
          </div>
        </Pop>
      ))}
    </AbsoluteFill>
  );
};

/* ---------- C1: why look at an EU law from Suriname ---------- */
const Why = () => {
  const frame = useCurrentFrame();
  const arrow = interpolate(frame, [Fr('C1b', 0.25), Fr('C1b', 0.7)], [0, 1], clamp);
  const green = on(frame, 'C1b', 0.7);
  const tl = [['2024', 'Wet van kracht', 'C1d', 0.1], ['feb. 2025', 'Verboden + AI-geletterdheid', 'C1d', 0.45], ['daarna', 'Stap voor stap meer regels', 'C1d', 0.75]];
  return (
    <AbsoluteFill style={{ background: C.light }}>
      <Heading at={F('C1', 0)} kicker="WAAROM DEZE WET?">Geldt niet in Suriname. Toch kijken we ernaar.</Heading>
      {/* Suriname */}
      <Pop at={Fr('C1', 0.2)} style={{ left: 170, top: 300 }}>
        <svg width="330" height="300"><path d="M60 40 L250 20 L300 120 L270 250 L120 280 L40 200 Z" fill="#C3CEDC" stroke="#A9B5C6" strokeWidth="4" />
          <text x="165" y="150" textAnchor="middle" fontFamily={SANS} fontWeight="700" fontSize="34" fill={C.mute}>Suriname</text>
          <text x="165" y="190" textAnchor="middle" fontFamily={SANS} fontSize="22" fill={C.mute}>wet geldt niet</text></svg>
      </Pop>
      {/* Europe */}
      <Pop at={Fr('C1', 0.4)} style={{ left: 1330, top: 270 }}>
        <svg width="420" height="340"><path d="M70 60 L220 20 L360 70 L400 200 L300 310 L140 300 L40 190 Z" fill={C.green} />
          {Array.from({ length: 12 }, (_, i) => <text key={i} x={220 + 70 * Math.cos(i * Math.PI / 6)} y={168 + 70 * Math.sin(i * Math.PI / 6)} textAnchor="middle" fontSize="22" fill={C.amber}>★</text>)}
          <text x="220" y="175" textAnchor="middle" fontFamily={SANS} fontWeight="700" fontSize="34" fill={C.card}>EU</text></svg>
      </Pop>
      {/* arrow */}
      <svg width="900" height="120" style={{ position: 'absolute', left: 480, top: 400 }}>
        <path d={`M20 60 L${20 + 820 * arrow} 60`} stroke={green ? C.green : C.terra} strokeWidth="10" strokeLinecap="round" />
        {arrow > 0.98 && <path d="M830 30 L870 60 L830 90 Z" fill={C.green} />}
      </svg>
      <Pop at={Fr('C1b', 0.3)} style={{ left: 560, top: 300, width: 720 }}>
        <div style={{ textAlign: 'center', fontFamily: SANS, fontWeight: 700, fontSize: 30, color: C.ink }}>Surinaams bedrijf met Europese klanten of data</div>
      </Pop>
      <Pop at={Fr('C1b', 0.75)} style={{ left: 640, top: 500, width: 560 }}>
        <div style={{ textAlign: 'center', fontFamily: SANS, fontWeight: 700, fontSize: 30, color: C.green }}>✓ dan geldt de wet wél</div>
      </Pop>
      <Pop at={Fr('C1c', 0.15)} style={{ left: 128, top: 620, width: 760 }}>
        <Card><span style={{ fontFamily: SERIF, fontWeight: 600, fontSize: 34, color: C.ink }}>Het bekendste voorbeeld van hoe een wetgever AI indeelt: een meetlat.</span></Card>
      </Pop>
      {tl.map(([d, t, k, p], i) => (
        <Pop key={d} at={Fr(k, p)} style={{ left: 980 + i * 300, top: 640, width: 280 }}>
          <div style={{ borderTop: `6px solid ${C.amber}`, paddingTop: 12 }}>
            <div style={{ fontFamily: SERIF, fontWeight: 700, fontSize: 34, color: C.dark }}>{d}</div>
            <div style={{ fontFamily: SANS, fontSize: 24, color: C.ink, lineHeight: 1.25 }}>{t}</div>
          </div>
        </Pop>
      ))}
    </AbsoluteFill>
  );
};

/* ---------- C2: the pyramid ---------- */
const PyramidScene = () => {
  const frame = useCurrentFrame();
  const show = LAYERS.map((L) => interpolate(frame, [F(L.k, 0), F(L.k, 0.5)], [0, 1], clamp));
  const active = LAYERS.reduce((a, L, i) => (on(frame, L.k) && !on(frame, 'C2f') ? i : a), -1);
  const up = interpolate(frame, [Fr('C2f', 0.05), Fr('C2f', 0.35)], [0, 1], clamp);
  return (
    <AbsoluteFill style={{ background: C.light }}>
      <Heading at={F('C2', 0)} kicker="DE AI-VERORDENING">Vier risicoklassen</Heading>
      <Pyramid x={128} y={250} w={760} h={500} show={show} active={active} />
      {/* arrow up: heavier requirements */}
      <svg width="80" height="500" style={{ position: 'absolute', left: 40, top: 250, opacity: up }}>
        <path d={`M40 ${490} L40 ${490 - 460 * up}`} stroke={C.dark} strokeWidth="8" />
        <path d="M18 40 L40 4 L62 40 Z" fill={C.dark} opacity={up > 0.95 ? 1 : 0} />
      </svg>
      {LAYERS.map((L, i) => (
        <Pop key={L.name} at={F(L.k, 0.4)} style={{ left: 960, top: 250 + i * 125, width: 840 }}>
          <div style={{ display: 'flex', gap: 18, alignItems: 'center', opacity: active >= 0 && active !== i ? 0.45 : 1 }}>
            <div style={{ width: 18, height: 96, borderRadius: 9, background: L.col }} />
            <div>
              <div style={{ fontFamily: SANS, fontWeight: 700, fontSize: 28, color: C.ink }}>{L.name} <span style={{ color: C.mute, fontWeight: 600 }}>· {L.rule}</span></div>
              <div style={{ fontFamily: SANS, fontSize: 25, color: C.mute, marginTop: 4 }}>{L.ex}</div>
            </div>
          </div>
        </Pop>
      ))}
      <Banner at={Fr('C2f', 0.45)} top={790} size={36}>Steeds de vraag: <span style={{ color: C.amber }}>waarvoor wordt het gebruikt, en wat staat er voor mensen op het spel?</span></Banner>
    </AbsoluteFill>
  );
};

/* ---------- C3: the two roles ---------- */
const Gear = ({ frame }) => (
  <svg width="120" height="120" viewBox="-60 -60 120 120"><g transform={`rotate(${frame * 0.8})`}>
    {Array.from({ length: 8 }, (_, i) => <rect key={i} x="-9" y="-56" width="18" height="22" rx="4" fill={C.green} transform={`rotate(${i * 45})`} />)}
    <circle r="38" fill={C.green} /><circle r="15" fill={C.card} /></g></svg>
);
const Roles = () => {
  const frame = useCurrentFrame();
  const arrow = interpolate(frame, [Fr('C3d', 0.35), Fr('C3d', 0.8)], [0, 1], clamp);
  return (
    <AbsoluteFill style={{ background: C.light }}>
      <Heading at={F('C3', 0)} kicker="NAAST DE KLASSE">Welke rol heb je?</Heading>
      <Pop at={Fr('C3b', 0.05)} style={{ left: 128, top: 250, width: 760 }}>
        <Card style={{ display: 'flex', gap: 28, alignItems: 'center' }}>
          <div style={{ flexShrink: 0 }}><Gear frame={frame} /></div>
          <div>
            <div style={{ fontFamily: SERIF, fontWeight: 700, fontSize: 44, color: C.dark }}>Aanbieder</div>
            <div style={{ fontFamily: SANS, fontSize: 26, color: C.ink, lineHeight: 1.3 }}>Ontwikkelt het systeem of laat het ontwikkelen, en brengt het onder eigen naam op de markt of in gebruik</div>
          </div>
        </Card>
      </Pop>
      <Pop at={Fr('C3c', 0.05)} style={{ left: 1030, top: 250, width: 760 }}>
        <Card style={{ display: 'flex', gap: 28, alignItems: 'center' }}>
          <div style={{ position: 'relative', width: 130, height: 130, flexShrink: 0 }}>
            <div style={{ position: 'absolute', left: 10, top: 0 }}><Person size={100} frame={frame} body={C.dark} tie /></div>
            <div style={{ position: 'absolute', left: 0, top: 96, width: 130, height: 24, borderRadius: 6, background: '#B88E66' }} />
          </div>
          <div>
            <div style={{ fontFamily: SERIF, fontWeight: 700, fontSize: 38, color: C.dark }}>Gebruiksverantwoordelijke</div>
            <div style={{ fontFamily: SANS, fontSize: 26, color: C.ink, lineHeight: 1.3 }}>Zet het systeem onder eigen verantwoordelijkheid in, bijvoorbeeld in het eigen kantoor</div>
          </div>
        </Card>
      </Pop>
      {/* supplier -> Suribank */}
      <Pop at={Fr('C3d', 0.2)} style={{ left: 128, top: 545, width: 1664 }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: 24 }}>
          <div style={{ background: C.sand, borderRadius: 16, padding: '14px 24px', fontFamily: SANS, fontWeight: 700, fontSize: 28, color: C.ink, width: 520 }}>Leverancier van het model <span style={{ color: C.green }}>· aanbieder</span></div>
          <svg width="260" height="40"><path d={`M6 20 L${6 + 220 * arrow} 20`} stroke={C.dark} strokeWidth="6" />{arrow > 0.97 && <path d="M226 6 L252 20 L226 34 Z" fill={C.dark} />}</svg>
          <div style={{ background: C.sand, borderRadius: 16, padding: '14px 24px', fontFamily: SANS, fontWeight: 700, fontSize: 28, color: C.ink, width: 600, opacity: arrow }}>Suribank <span style={{ color: C.green }}>· gebruiksverantwoordelijke</span></div>
        </div>
      </Pop>
      <Pop at={Fr('C3e', 0.4)} style={{ left: 128, top: 650, width: 760 }}>
        <div style={{ fontFamily: SANS, fontSize: 27, color: C.ink, borderLeft: `6px solid ${C.green}`, paddingLeft: 18 }}>Plicht: het systeem is <b>goed gebouwd en getest</b></div>
      </Pop>
      <Pop at={Fr('C3e', 0.7)} style={{ left: 1030, top: 650, width: 760 }}>
        <div style={{ fontFamily: SANS, fontSize: 27, color: C.ink, borderLeft: `6px solid ${C.green}`, paddingLeft: 18 }}>Plicht: het wordt <b>in de praktijk goed gebruikt</b></div>
      </Pop>
    </AbsoluteFill>
  );
};

/* ---------- C4: Suribank is high risk ---------- */
const Stamp = ({ at, text, sub, x, y, rot = -6, col = C.terra }) => {
  const s = useSpr(at, { damping: 12, stiffness: 160 });
  return (
    <div style={{ position: 'absolute', left: x, top: y, opacity: s, transform: `rotate(${rot}deg) scale(${1.6 - 0.6 * s})`, border: `5px solid ${col}`, borderRadius: 14, padding: '10px 20px', background: 'rgba(255,253,248,.92)', color: col, fontFamily: SANS, fontWeight: 700, fontSize: 30, textAlign: 'center', lineHeight: 1.15 }}>
      {text}<div style={{ fontSize: 22, fontWeight: 600 }}>{sub}</div>
    </div>
  );
};
const Suribank = () => {
  const frame = useCurrentFrame();
  const slide = interpolate(frame, [F('C4', 0.2), Fr('C4', 0.75)], [0, 1], clamp);
  const morph = interpolate(frame, [F('C4d', 0), Fr('C4d', 0.4)], [0, 1], clamp);
  return (
    <AbsoluteFill style={{ background: C.light }}>
      <Heading at={F('C4', 0)} kicker="VOORBEELD 1 · SURIBANK">Kredietwaardigheid: hoog risico</Heading>
      <Pyramid x={128} y={250} w={620} h={440} active={1} size={0.85} />
      {/* application card sliding into the high-risk layer */}
      <div style={{ position: 'absolute', left: interpolate(slide, [0, 1], [820, 330]), top: interpolate(slide, [0, 1], [250, 360]), transform: `rotate(${(1 - slide) * 8}deg)` }}>
        <div style={{ background: C.card, border: `3px solid ${C.dark}`, borderRadius: 12, padding: '10px 16px', fontFamily: SANS, fontSize: 21, color: C.ink, boxShadow: '0 10px 24px rgba(0,0,0,.18)' }}>
          <b>Aanvraag Shanti</b><br />bijlage III · 5b
        </div>
      </div>
      <Stamp at={Fr('C4b', 0.25)} text="Risicobeheer" sub="art. 9" x={860} y={260} rot={-5} />
      <Stamp at={Fr('C4b', 0.55)} text="Data" sub="art. 10" x={1180} y={250} rot={4} />
      <Stamp at={Fr('C4b', 0.85)} text="Menselijk toezicht" sub="art. 14" x={1420} y={270} rot={-3} />
      <div style={{ position: 'absolute', left: 860, top: 440, width: 900, opacity: interpolate(frame, [F('C4c', 0), Fr('C4c', 0.2)], [0, 1], clamp) }}>
        <div style={{ background: mix(morph, '#F8E1DF', '#DCE6F5'), border: `4px solid ${mix(morph, C.terra, C.green)}`, borderRadius: 18, padding: '18px 26px' }}>
          <div style={{ fontFamily: SANS, fontWeight: 700, fontSize: 32, color: C.ink }}>
            {morph < 0.5 ? 'FRIA · art. 27' : 'K2 + nulmeting = jullie AI-impactbeoordeling'}
          </div>
          <div style={{ fontFamily: SANS, fontSize: 25, color: C.mute, marginTop: 6 }}>Wie wordt geraakt? Hoe ernstig? Wat doe je eraan?</div>
        </div>
      </div>
      <Pop at={Fr('C4e', 0.3)} style={{ left: 860, top: 610, width: 900 }}>
        <div style={{ display: 'flex', gap: 22, alignItems: 'center' }}>
          <Person size={90} frame={frame} body={C.green} glasses />
          <div style={{ fontFamily: SANS, fontSize: 28, color: C.ink, lineHeight: 1.3 }}>Onterecht afgewezen? Een mens kan <b>ingrijpen</b> en de bank kan <b>uitleggen</b> waarom. <span style={{ color: C.green, fontWeight: 700 }}>→ K7</span></div>
        </div>
      </Pop>
    </AbsoluteFill>
  );
};

/* ---------- C5: Frisco orderagent ---------- */
const Frisco = () => {
  const frame = useCurrentFrame();
  const both = useSpr(Fr('C5d', 0.4));
  return (
    <AbsoluteFill style={{ background: C.light }}>
      <Heading at={F('C5', 0)} kicker="VOORBEELD 2 · FRISCO INSTALLATIES">Orderagent: meestal beperkt risico</Heading>
      <Phone title="Frisco Installaties" sub="orderassistent" h={640} style={{ left: 128, top: 240, transform: 'scale(0.9)', transformOrigin: 'top left' }}>
        <Bubble who="bot" at={Fr('C5c', 0.12)} frame={frame}>Hallo, ik ben de digitale assistent van Frisco. Ik ben een AI.</Bubble>
        <Bubble who="me" at={Fr('C5c', 0.48)} frame={frame}>Praat ik met een mens?</Bubble>
        <Bubble who="bot" at={Fr('C5c', 0.66)} frame={frame}>Nee, ik ben een AI. Wilt u een medewerker spreken?</Bubble>
      </Phone>
      <Pop at={Fr('C5b', 0.1)} style={{ left: 720, top: 250, width: 1070 }}>
        <Card style={{ display: 'flex', gap: 22, alignItems: 'center' }}>
          <span style={{ fontFamily: SERIF, fontSize: 52, color: C.mute }}>✕</span>
          <span style={{ fontFamily: SANS, fontSize: 30, color: C.ink }}>Niet in bijlage III → meestal <b>beperkt risico</b></span>
        </Card>
      </Pop>
      <Pop at={Fr('C5c', 0.2)} style={{ left: 720, top: 400, width: 1070 }}>
        <Card style={{ display: 'flex', gap: 22, alignItems: 'center', borderColor: C.green }}>
          <span style={{ fontFamily: SERIF, fontSize: 52, color: C.green }}>✓</span>
          <span style={{ fontFamily: SANS, fontSize: 30, color: C.ink }}><b>Artikel 50:</b> klanten weten dat ze met AI praten</span>
        </Card>
      </Pop>
      <div style={{ position: 'absolute', left: 720, top: 550, display: 'flex', gap: 20, opacity: both, transform: `translateY(${(1 - both) * 20}px)` }}>
        {['Aanbieder', 'Gebruiksverantwoordelijke'].map((r) => (
          <div key={r} style={{ background: C.dark, color: C.light, borderRadius: 16, padding: '14px 24px', fontFamily: SANS, fontWeight: 700, fontSize: 28 }}><span style={{ color: C.amber }}>✓</span> {r}</div>
        ))}
        <div style={{ alignSelf: 'center', fontFamily: SANS, fontSize: 26, color: C.mute }}>Frisco is allebei</div>
      </div>
      <Pop at={Fr('C5e', 0.2)} style={{ left: 720, top: 660, width: 1070 }}>
        <div style={{ background: '#F8E1DF', border: `3px solid ${C.terra}`, borderRadius: 16, padding: '16px 24px', fontFamily: SANS, fontSize: 27, color: C.ink, lineHeight: 1.3 }}>
          <b style={{ color: C.terra }}>Let op:</b> beslist de agent over krediet, of over wie wel en niet geholpen wordt? Deel dan opnieuw in.
        </div>
      </Pop>
    </AbsoluteFill>
  );
};

/* ---------- C6: four articles ---------- */
const ARTS = [
  ['10', 'Data en datagovernance', 'C6b', 'A-DG'],
  ['13', 'Informatie voor wie het systeem gebruikt', 'C6c', null],
  ['26', 'Plichten van de gebruiksverantwoordelijke', 'C6d', null],
  ['86', 'Recht op uitleg bij een besluit', 'C6e', null],
];
const Articles = () => (
  <AbsoluteFill style={{ background: C.light }}>
    <Heading at={F('C6', 0)} kicker="BIJ HOOG RISICO">Nog vier artikelen</Heading>
    {ARTS.map(([n, t, k, tag], i) => (
      <Pop key={n} at={F(k, 0.1)} dy={0} style={{ left: 128 + i * 420, top: 300, width: 390 }}>
        <Card style={{ minHeight: 330, position: 'relative' }}>
          <div style={{ fontFamily: SANS, fontWeight: 700, fontSize: 24, color: C.mute, letterSpacing: 1 }}>ARTIKEL</div>
          <div style={{ fontFamily: SERIF, fontWeight: 700, fontSize: 110, color: C.dark, lineHeight: 1 }}>{n}</div>
          <div style={{ fontFamily: SANS, fontWeight: 600, fontSize: 30, color: C.ink, marginTop: 14, lineHeight: 1.25 }}>{t}</div>
          {tag && <div style={{ position: 'absolute', right: 20, top: 20, background: C.amber, borderRadius: 12, padding: '6px 14px', fontFamily: SANS, fontWeight: 700, fontSize: 22, color: C.dark }}>{tag}</div>}
        </Card>
      </Pop>
    ))}
  </AbsoluteFill>
);

/* ---------- C7: floor, not ceiling ---------- */
const LENZEN = ['Gevolgen', 'Rechten en plichten', 'Rechtvaardigheid', 'Professionele integriteit'];
const Floor = () => {
  const frame = useCurrentFrame();
  const shrink = interpolate(frame, [F('C7', 0), Fr('C7', 0.9)], [0, 1], clamp);
  const ex = on(frame, 'C7e', 0.05);
  return (
    <AbsoluteFill style={{ background: C.light }}>
      <Heading at={F('C7', 0)} kicker="DE KLASSE IS NIET HET HELE VERHAAL">Een ondergrens, geen eindoordeel</Heading>
      <div style={{ position: 'absolute', left: 128, top: 0, width: 560, height: 1080, transform: `scale(${1 - 0.15 * shrink})`, transformOrigin: '280px 600px' }}>
        <Pyramid x={90} y={430} w={380} h={240} labels={false} />
        <div style={{ position: 'absolute', left: 40, top: 680, width: 480, background: C.dark, color: C.amber, borderRadius: 10, padding: '12px 0', textAlign: 'center', fontFamily: SANS, fontWeight: 700, fontSize: 30, letterSpacing: 3 }}>ONDERGRENS</div>
        {LENZEN.map((l, i) => (
          <Pop key={l} at={Fr('C7d', 0.35 + i * 0.1)} style={{ left: 10 + (i % 2) * 270, top: 250 + Math.floor(i / 2) * 82, width: 255 }}>
            <div style={{ background: C.card, border: `2px solid ${C.green}`, borderRadius: 14, padding: '12px 10px', textAlign: 'center', fontFamily: SANS, fontWeight: 700, fontSize: 21, color: C.green }}>{l}</div>
          </Pop>
        ))}
      </div>
      {!ex && <>
        <Pop at={Fr('C7b', 0.1)} style={{ left: 760, top: 260, width: 1030 }}>
          <Card><span style={{ fontFamily: SANS, fontSize: 30, color: C.ink }}><b>Artikel 4:</b> AI-geletterdheid voor iedereen die ermee werkt, <b>in elke klasse</b></span></Card>
        </Pop>
        <Pop at={Fr('C7c', 0.1)} style={{ left: 760, top: 400, width: 1030 }}>
          <div style={{ display: 'flex', gap: 18 }}>
            {['Clip 18 · menselijk toezicht', 'Clip 20 · transparantie'].map((t) => <div key={t} style={{ background: C.sand, borderRadius: 14, padding: '14px 22px', fontFamily: SANS, fontWeight: 700, fontSize: 26, color: C.ink }}>{t}</div>)}
          </div>
        </Pop>
        <Banner at={Fr('C7d', 0.15)} left={760} width={1030} top={530} size={36}>Wat de wet toestaat, is niet altijd verantwoord. <span style={{ color: C.amber }}>En waar de wet zwijgt, zoals in Suriname, blijft de ethische vraag staan.</span></Banner>
      </>}
      {ex && <>
        <Pop at={Fr('C7e', 0.08)} style={{ left: 760, top: 260, width: 1030 }}>
          <Card style={{ display: 'flex', gap: 20, alignItems: 'center' }}>
            <span style={{ background: C.amber, borderRadius: 12, padding: '6px 14px', fontFamily: SANS, fontWeight: 700, fontSize: 24, color: C.dark }}>beperkt risico</span>
            <span style={{ fontFamily: SANS, fontSize: 30, color: C.ink }}>Orderagent van Frisco</span>
          </Card>
        </Pop>
        <Pop at={Fr('C7e', 0.3)} style={{ left: 760, top: 400, width: 1030 }}>
          <div style={{ display: 'flex', gap: 20 }}>
            {['Klant met een andere naam', 'Klant die een spraakbericht stuurt'].map((t) => (
              <div key={t} style={{ flex: 1, background: '#F8E1DF', border: `3px solid ${C.terra}`, borderRadius: 16, padding: '16px 20px', fontFamily: SANS, fontSize: 27, color: C.ink }}>{t} <b style={{ color: C.terra }}>→ slechter geholpen?</b></div>
            ))}
          </div>
        </Pop>
        <Banner at={Fr('C7e', 0.75)} left={760} width={1030} top={560} size={36}>De wet vraagt hier weinig. <span style={{ color: C.amber }}>Jullie test in practicum 4 vraagt het wel.</span></Banner>
      </>}
    </AbsoluteFill>
  );
};

/* ---------- C7f: summary (three items inside one sentence) ---------- */
const Summary = () => {
  const items = ['Vier klassen, van verboden tot minimaal risico', 'Je rol bepaalt je plichten: aanbieder of gebruiksverantwoordelijke', 'De klasse is een ondergrens, geen eindoordeel'];
  return (
    <AbsoluteFill style={{ background: C.light }}>
      <Heading at={F('C7f', 0)}>Samengevat</Heading>
      {items.map((t, i) => (
        <Pop key={t} at={Fr('C7f', 0.08 + i * 0.3)} style={{ left: 128, top: 250 + i * 170, width: 1664 }}>
          <Card style={{ display: 'flex', gap: 30, alignItems: 'center', padding: '24px 36px' }}>
            <span style={{ fontFamily: SERIF, fontWeight: 700, fontSize: 70, color: C.amber, width: 60 }}>{i + 1}</span>
            <span style={{ fontFamily: SANS, fontWeight: 600, fontSize: 38, color: C.ink, lineHeight: 1.25 }}>{t}</span>
          </Card>
        </Pop>
      ))}
    </AbsoluteFill>
  );
};

/* ---------- C8: now you, the K6 line ---------- */
const typed = (frame, from, to, text) => text.slice(0, Math.round(interpolate(frame, [from, to], [0, text.length], clamp)));
const Now = () => {
  const frame = useCurrentFrame();
  const vals = [
    ['Klasse', 'Hoog risico', 'C8b', 0.05],
    ['Onderbouwing', 'Bijlage III, punt 5b: kredietwaardigheid', 'C8b', 0.3],
    ['Rol van de partner', 'Leverancier = aanbieder · Suribank = gebruiksverantwoordelijke', 'C8b', 0.6],
  ];
  return (
    <AbsoluteFill style={{ background: C.light }}>
      <Heading at={F('C8', 0)} kicker="NU JIJ · BOVEN JULLIE RISICOREGISTER (K6)">EU-risicoklasse en rol</Heading>
      <Pop at={Fr('C8', 0.3)} style={{ left: 128, top: 250, width: 1664 }}>
        <div style={{ background: C.card, border: `2px solid ${C.line}`, borderRadius: 18, overflow: 'hidden', boxShadow: '0 14px 34px rgba(0,32,96,.10)' }}>
          <div style={{ background: C.dark, color: C.light, fontFamily: SANS, fontWeight: 700, fontSize: 26, padding: '14px 26px' }}>EU-risicoklasse en rol · voorbeeld Suribank</div>
          {vals.map(([l, v, k, p]) => (
            <div key={l} style={{ display: 'flex', borderTop: `2px solid ${C.line}` }}>
              <div style={{ width: 380, padding: '20px 26px', background: C.sand, fontFamily: SANS, fontWeight: 700, fontSize: 28, color: C.ink }}>{l}</div>
              <div style={{ flex: 1, padding: '20px 26px', fontFamily: SANS, fontSize: 28, color: C.ink, background: '#F7F0DD' }}>{typed(frame, Fr(k, p), Fr(k, p + 0.3), v)}</div>
            </div>
          ))}
          <div style={{ display: 'flex', borderTop: `2px solid ${C.line}` }}>
            <div style={{ width: 380, padding: '16px 26px', background: C.sand, fontFamily: SANS, fontWeight: 700, fontSize: 28, color: C.ink }}>Risicoregister</div>
            <div style={{ flex: 1, padding: '16px 26px', fontFamily: SANS, fontSize: 26, color: C.mute }}>R-01 · R-02 · R-03 …</div>
          </div>
        </div>
      </Pop>
      <Banner at={Fr('C8c', 0.1)} top={720} size={36}>Twijfel je? Schrijf op tussen welke klassen, en waarom. <span style={{ color: C.amber }}>Ook dat is een goed antwoord.</span></Banner>
    </AbsoluteFill>
  );
};

export const KaderC = () => (
  <ClipShell timing={timing} scenes={[
    ['C0', <Title />], ['C0b', <Goal />], ['C1', <Why />], ['C2', <PyramidScene />], ['C3', <Roles />],
    ['CQ1', <Quiz8 tm={tm} n={1} q="CQ1" a="CQ1b" optAt={0.6} question="Een bank gebruikt een model dat beslist of iemand een persoonlijke lening krijgt. In welke risicoklasse valt dit model?" options={['A. Minimaal risico', 'B. Beperkt risico', 'C. Hoog risico']} good={2} note={<>Hoog risico: bijlage III, punt 5b. <span style={{ color: C.amber }}>De bank doet ook een FRIA.</span></>} />],
    ['C4', <Suribank />], ['C5', <Frisco />],
    ['CQ2', <Quiz8 tm={tm} n={2} q="CQ2" a="CQ2b" optAt={0.55} question="Een maatkledingzaak laat een orderchatbot bouwen en zet die onder eigen naam op haar website. Welke rol heeft de zaak, en welke plicht geldt in elk geval?" options={['A. Alleen gebruiksverantwoordelijke; geen extra plicht', 'B. Aanbieder én gebruiksverantwoordelijke; transparantieplicht (art. 50)', 'C. Geen rol: de bouwer is verantwoordelijk']} good={1} />],
    ['C6', <Articles />], ['C7', <Floor />], ['C7f', <Summary />], ['C8', <Now />],
  ]} />
);
