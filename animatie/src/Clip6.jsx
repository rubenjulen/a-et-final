/* Kennisclip 6 · Waar komt bias vandaan? (week 2) */
import React from 'react';
import { AbsoluteFill, useCurrentFrame, interpolate, spring } from 'remotion';
import timing from './timing_c6.json';
import { C, SERIF, SANS, FPS, clamp, makeKit, Person, useSpring } from './wk2_kit';

const K = makeKit(timing);
const { F, endOf, Pop, Card, Banner, Title, Chips, QuizN, Composition, TitleScene, Summary } = K;
const SRC = ['1 · Historisch', '2 · Representatie', '3 · Meting', '4 · Label', '5 · Aggregatie', '6 · Gebruik'];

/* D1: weegschaal die steeds naar dezelfde kant doorslaat */
const Scale = () => {
  const frame = useCurrentFrame();
  const tilt = 9 + 4 * Math.sin(frame / 14);
  const drops = [0, 1, 2, 3, 4, 5].map((i) => {
    const t0 = F('d1a', 0.6 + i * 0.9);
    const y = interpolate(frame, [t0, t0 + 18], [-260, 0], clamp);
    return { y, o: frame > t0 ? 1 : 0 };
  });
  return (
    <AbsoluteFill style={{ background: C.light }}>
      <Title at={F('d1a', 0)} kicker="Wat is bias?">Een fout die steeds dezelfde kant op valt</Title>
      <svg style={{ position: 'absolute', left: 560, top: 260 }} width="800" height="460" viewBox="-400 -40 800 460">
        <rect x="-10" y="40" width="20" height="300" fill={C.dark} />
        <rect x="-120" y="330" width="240" height="26" rx="8" fill={C.dark} />
        <g transform={`rotate(${tilt} 0 40)`}>
          <rect x="-330" y="32" width="660" height="16" rx="8" fill={C.green} />
          <line x1="-300" y1="40" x2="-300" y2="150" stroke={C.mute} strokeWidth="4" />
          <line x1="300" y1="40" x2="300" y2="150" stroke={C.mute} strokeWidth="4" />
          <path d="M-380 150 Q-300 200 -220 150 Z" fill={C.sand} stroke={C.mute} strokeWidth="3" />
          <path d="M220 150 Q300 200 380 150 Z" fill={C.sand} stroke={C.mute} strokeWidth="3" />
          <g transform="translate(300,150)">
            {drops.map((d, i) => <rect key={i} x={-46 + (i % 3) * 30} y={-28 - Math.floor(i / 3) * 26 + d.y} width="26" height="22" rx="4" fill={C.terra} opacity={d.o} />)}
          </g>
        </g>
      </svg>
      <Pop at={F('d1c', 0)} style={{ left: 128, top: 290, width: 420 }}>
        {['de data', 'het label', 'de bouwer', 'het gebruik'].map((t, i) => (
          <div key={t} style={{ fontFamily: SANS, fontWeight: 700, fontSize: 30, color: C.ink, marginTop: 16, opacity: interpolate(frame, [F('d1c', 0.4 + i * 0.6), F('d1c', 0.8 + i * 0.6)], [0, 1], clamp) }}>→ {t}</div>
        ))}
      </Pop>
      <Pop at={F('d1d', 0)} style={{ left: 128, top: 760, width: 1664 }}>
        <div style={{ display: 'flex', gap: 14, flexWrap: 'wrap' }}>
          {SRC.map((s, i) => <div key={s} style={{ fontFamily: SANS, fontWeight: 700, fontSize: 26, padding: '12px 24px', borderRadius: 999, background: C.dark, color: C.amber, opacity: interpolate(frame, [F('d1d', i * 0.2), F('d1d', 0.3 + i * 0.2)], [0, 1], clamp) }}>{s}</div>)}
        </div>
      </Pop>
    </AbsoluteFill>
  );
};

/* D2: oud kredietdossier met stempel */
const History = () => {
  const frame = useCurrentFrame();
  const st = spring({ frame: frame - F('d2a', 1.2), fps: FPS, config: { damping: 9, stiffness: 160 } });
  const rows = [['2016', 'vaste baan', 'goedgekeurd'], ['2017', 'informeel werk', 'afgewezen'], ['2018', 'vaste baan', 'goedgekeurd'], ['2019', 'informeel werk', 'afgewezen'], ['2020', 'informeel werk', 'afgewezen']];
  return (
    <AbsoluteFill style={{ background: C.light }}>
      <Chips items={SRC} on={0} at={F('d2a', 0)} />
      <Title at={F('d2a', 0)} top={110}>Historische bias: het verleden zit in de data</Title>
      <Pop at={F('d2a', 0.4)} style={{ left: 200, top: 300, width: 820 }}>
        <Card style={{ background: '#F3EAD6', transform: 'rotate(-2deg)' }}>
          <div style={{ fontFamily: SERIF, fontWeight: 700, fontSize: 36, color: C.ink }}>Suribank · kredietdossiers</div>
          {rows.map(([y, w, r], i) => (
            <div key={y} style={{ display: 'flex', justifyContent: 'space-between', fontFamily: SANS, fontSize: 28, marginTop: 12, color: C.ink, opacity: interpolate(frame, [F('d2a', 0.6 + i * 0.3), F('d2a', 0.9 + i * 0.3)], [0, 1], clamp) }}>
              <span>{y}</span><span>{w}</span><span style={{ fontWeight: 700, color: r === 'afgewezen' ? C.terra : C.green }}>{r}</span>
            </div>
          ))}
        </Card>
      </Pop>
      <div style={{ position: 'absolute', left: 520, top: 640, transform: `rotate(-10deg) scale(${2.4 - 1.4 * st})`, opacity: Math.min(1, st * 1.4), border: `8px solid ${C.terra}`, color: C.terra, fontFamily: SANS, fontWeight: 700, fontSize: 52, padding: '6px 22px', borderRadius: 10, letterSpacing: 4 }}>AFGEWEZEN</div>
      <Pop at={F('d2b', 0.5)} style={{ left: 1120, top: 330, width: 640 }}>
        <Card>
          <div style={{ fontFamily: SANS, fontSize: 24, color: C.mute }}>Wat het model leert</div>
          <div style={{ fontFamily: SERIF, fontWeight: 600, fontSize: 40, color: C.ink, marginTop: 10, lineHeight: 1.2 }}>"Informeel werk = minder kredietwaardig"</div>
          <div style={{ fontFamily: SANS, fontSize: 26, color: C.terra, marginTop: 18, fontWeight: 700, opacity: interpolate(frame, [F('d2b', 6), F('d2b', 6.6)], [0, 1], clamp) }}>… terwijl het vooral een gevolg was van eerdere keuzes</div>
        </Card>
      </Pop>
    </AbsoluteFill>
  );
};

/* D3: kaart met veel stippen aan de kust, weinig in het binnenland */
const Representation = () => {
  const frame = useCurrentFrame();
  const dots = [];
  let seed = 7;
  const rnd = () => { seed = (seed * 9301 + 49297) % 233280; return seed / 233280; };
  for (let i = 0; i < 100; i++) {
    const coast = i < 83;
    dots.push({ x: 40 + rnd() * 620, y: coast ? 40 + rnd() * 110 : 200 + rnd() * 330, coast });
  }
  return (
    <AbsoluteFill style={{ background: C.light }}>
      <Chips items={SRC} on={1} at={F('d3a', 0)} />
      <Title at={F('d3a', 0)} top={110}>Representatiebias: een groep komt te weinig voor</Title>
      <Pop at={F('d3a', 0.5)} style={{ left: 200, top: 270 }}>
        <svg width="700" height="560" viewBox="0 0 700 560">
          <path d="M20 20 L680 20 L660 180 L620 300 L560 540 L120 540 L60 320 L30 180 Z" fill="#E7EFE9" stroke={C.green} strokeWidth="3" />
          <path d="M20 170 Q350 200 670 170" stroke={C.green} strokeWidth="2" strokeDasharray="8 8" fill="none" />
          <text x="40" y="200" fontFamily={SANS} fontSize="22" fill={C.mute}>kust</text>
          <text x="40" y="520" fontFamily={SANS} fontSize="22" fill={C.mute}>binnenland</text>
          {dots.map((d, i) => (
            <circle key={i} cx={d.x} cy={d.y} r="7" fill={d.coast ? C.green : C.terra} opacity={interpolate(frame, [F('d3a', 0.6 + i * 0.03), F('d3a', 0.8 + i * 0.03)], [0, 1], clamp)} />
          ))}
        </svg>
      </Pop>
      <Pop at={F('d3b', 0)} style={{ left: 1040, top: 320, width: 700 }}>
        <Card>
          <div style={{ display: 'flex', alignItems: 'baseline', gap: 20 }}>
            <span style={{ fontFamily: SERIF, fontWeight: 700, fontSize: 120, color: C.terra }}>17%</span>
            <span style={{ fontFamily: SANS, fontSize: 30, color: C.ink }}>van de aanvragen<br />komt uit het binnenland</span>
          </div>
        </Card>
      </Pop>
      <Pop at={F('d3c', 0)} style={{ left: 1040, top: 590, width: 700 }}>
        <div style={{ fontFamily: SERIF, fontWeight: 600, fontSize: 38, color: C.ink, lineHeight: 1.2 }}>Minder voorbeelden = het model weet minder.</div>
        <div style={{ fontFamily: SANS, fontSize: 26, color: C.mute, marginTop: 10, opacity: interpolate(frame, [F('d3c', 2.5), F('d3c', 3)], [0, 1], clamp) }}>Zo ging het ook bij Gender Shades (kernbron).</div>
      </Pop>
    </AbsoluteFill>
  );
};

/* D4: loonstrook naast handgeschreven briefje */
const Measure = () => {
  const frame = useCurrentFrame();
  const miss = interpolate(frame, [F('d4c', 1.5), F('d4c', 2.2)], [0, 1], clamp);
  return (
    <AbsoluteFill style={{ background: C.light }}>
      <Chips items={SRC} on={2} at={F('d4a', 0)} />
      <Title at={F('d4a', 0)} top={110}>Meetbias: niet iedereen wordt even goed gemeten</Title>
      <Pop at={F('d4b', 0)} style={{ left: 200, top: 290, width: 640 }}>
        <Card>
          <div style={{ fontFamily: SANS, fontWeight: 700, fontSize: 26, color: C.mute, letterSpacing: 1 }}>LOONSTROOK · OKTOBER</div>
          {[['Bruto', 'SRD 18.400'], ['Inhoudingen', 'SRD 2.150'], ['Netto', 'SRD 16.250']].map(([a, b]) => (
            <div key={a} style={{ display: 'flex', justifyContent: 'space-between', fontFamily: SANS, fontSize: 30, marginTop: 14, color: C.ink }}><span>{a}</span><span style={{ fontWeight: 700 }}>{b}</span></div>
          ))}
          <div style={{ marginTop: 22, fontFamily: SANS, fontWeight: 700, fontSize: 26, color: C.green }}>✓ inkomen aangetoond</div>
        </Card>
      </Pop>
      <Pop at={F('d4c', 0)} style={{ left: 1000, top: 300, width: 600 }}>
        <div style={{ background: '#FFF8D8', padding: '30px 36px', transform: 'rotate(3deg)', boxShadow: '0 12px 26px rgba(0,0,0,.12)', fontFamily: "'Comic Sans MS', 'Segoe Print', cursive", fontSize: 34, color: '#3A3A3A', lineHeight: 1.4 }}>
          groente markt<br />± 600 per week?<br />soms meer, soms minder
        </div>
        <div style={{ marginTop: 40, fontFamily: SANS, fontWeight: 700, fontSize: 28, color: C.terra, opacity: miss }}>inkomen in de data: <span style={{ background: C.terra, color: C.card, padding: '2px 12px', borderRadius: 8 }}>ontbreekt</span></div>
      </Pop>
      <Pop at={F('d4b', 0.6)} style={{ left: 870, top: 420 }}><div style={{ fontFamily: SERIF, fontSize: 60, color: C.mute }}>vs</div></Pop>
    </AbsoluteFill>
  );
};

/* D5: labelkolom die alleen gevuld is voor wie een lening kreeg */
const Label = () => {
  const frame = useCurrentFrame();
  const rows = [['A-101', 'goedgekeurd', 'ja'], ['A-102', 'afgewezen', '?'], ['A-103', 'goedgekeurd', 'nee'], ['A-104', 'afgewezen', '?'], ['A-105', 'goedgekeurd', 'ja'], ['A-106', 'afgewezen', '?']];
  const hi = interpolate(frame, [F('d5c', 0), F('d5c', 0.6)], [0, 1], clamp);
  return (
    <AbsoluteFill style={{ background: C.light }}>
      <Chips items={SRC} on={3} at={F('d5a', 0)} />
      <Title at={F('d5a', 0)} top={110}>Labelbias: het label zelf is scheef</Title>
      <Pop at={F('d5a', 0.6)} style={{ left: 260, top: 290, width: 1000 }}>
        <Card style={{ padding: 0, overflow: 'hidden' }}>
          <div style={{ display: 'grid', gridTemplateColumns: '1fr 1.4fr 1.4fr', background: C.sand, fontFamily: SANS, fontWeight: 700, fontSize: 26, color: C.ink }}>
            {['Aanvraag', 'Besluit toen', 'Terugbetaald?'].map((h) => <div key={h} style={{ padding: '16px 24px' }}>{h}</div>)}
          </div>
          {rows.map(([id, b, l], i) => (
            <div key={id} style={{ display: 'grid', gridTemplateColumns: '1fr 1.4fr 1.4fr', fontFamily: SANS, fontSize: 26, color: C.ink, borderTop: `2px solid ${C.line}`, opacity: b === 'afgewezen' ? 1 - 0.55 * hi : 1, background: b === 'afgewezen' ? `rgba(168,67,44,${0.08 * hi})` : 'transparent' }}>
              <div style={{ padding: '12px 24px' }}>{id}</div>
              <div style={{ padding: '12px 24px' }}>{b}</div>
              <div style={{ padding: '12px 24px', fontWeight: 700, color: l === '?' ? C.terra : C.green, opacity: interpolate(frame, [F('d5b', 0.5 + i * 0.3), F('d5b', 0.8 + i * 0.3)], [0, 1], clamp) }}>{l === '?' ? 'onbekend' : l}</div>
            </div>
          ))}
        </Card>
      </Pop>
      <Pop at={F('d5c', 1.2)} style={{ left: 1330, top: 330, width: 460 }}>
        <Card>
          <div style={{ fontFamily: SERIF, fontWeight: 600, fontSize: 36, color: C.ink, lineHeight: 1.2 }}>Wie werd afgewezen, ontbreekt.</div>
          <div style={{ fontFamily: SANS, fontSize: 26, color: C.mute, marginTop: 12 }}>Het model leert van een voorselectie.</div>
        </Card>
      </Pop>
    </AbsoluteFill>
  );
};

/* D6: één gemiddelde, drie groepen */
const Aggregate = () => {
  const frame = useCurrentFrame();
  const split = interpolate(frame, [F('d6a', 4), F('d6a', 5.5)], [0, 1], clamp);
  const groups = [['Paramaribo', 0.90, C.green], ['Kustdistricten', 0.87, C.green], ['Binnenland', 0.61, C.terra]];
  return (
    <AbsoluteFill style={{ background: C.light }}>
      <Chips items={SRC} on={4} at={F('d6a', 0)} />
      <Title at={F('d6a', 0)} top={110}>Aggregatiebias: het gemiddelde verbergt een groep</Title>
      <Pop at={F('d6a', 0.6)} style={{ left: 200, top: 300, width: 1500 }}>
        <div style={{ fontFamily: SANS, fontSize: 28, color: C.mute }}>Goed beoordeeld (fictieve cijfers)</div>
        <div style={{ position: 'relative', height: 90, marginTop: 14, background: C.sand, borderRadius: 14, width: 1400, opacity: 1 - 0.6 * split }}>
          <div style={{ width: 1400 * 0.86, height: '100%', background: C.dark, borderRadius: 14 }} />
          <div style={{ position: 'absolute', left: 30, top: 18, fontFamily: SERIF, fontWeight: 700, fontSize: 44, color: C.light }}>Gemiddeld 86%</div>
        </div>
        {groups.map(([g, v, col], i) => (
          <div key={g} style={{ display: 'flex', alignItems: 'center', gap: 24, marginTop: 26, opacity: split, transform: `translateY(${(1 - split) * -40 * (i + 1)}px)` }}>
            <div style={{ width: 280, fontFamily: SANS, fontWeight: 700, fontSize: 30, color: C.ink }}>{g}</div>
            <div style={{ width: 1100, height: 56, background: C.sand, borderRadius: 12 }}>
              <div style={{ width: 1100 * v, height: '100%', background: col, borderRadius: 12 }} />
            </div>
            <div style={{ fontFamily: SERIF, fontWeight: 700, fontSize: 40, color: col }}>{Math.round(v * 100)}%</div>
          </div>
        ))}
      </Pop>
      <Banner at={F('d6b', 1.5)} top={760} size={40}>Meet daarom altijd <span style={{ color: C.amber }}>per groep</span>.</Banner>
    </AbsoluteFill>
  );
};

/* D7: model met etiket wordt elders ingezet */
const Use = () => {
  const frame = useCurrentFrame();
  const mv = interpolate(frame, [F('d7b', 0.5), F('d7b', 3)], [0, 1], clamp);
  const warn = spring({ frame: frame - F('d7b', 3), fps: FPS, config: { damping: 10 } });
  return (
    <AbsoluteFill style={{ background: C.light }}>
      <Chips items={SRC} on={5} at={F('d7a', 0)} />
      <Title at={F('d7a', 0)} top={110}>Gebruiksbias: ingezet waar het niet voor gemaakt is</Title>
      <Pop at={F('d7a', 0.4)} style={{ left: 200, top: 320, width: 520 }}>
        <Card style={{ textAlign: 'center' }}>
          <div style={{ fontFamily: SANS, fontSize: 24, color: C.mute }}>getraind op</div>
          <div style={{ fontFamily: SERIF, fontWeight: 700, fontSize: 52, color: C.green }}>de stad</div>
        </Card>
      </Pop>
      <Pop at={F('d7a', 0.8)} style={{ left: 1200, top: 320, width: 520 }}>
        <Card style={{ textAlign: 'center' }}>
          <div style={{ fontFamily: SANS, fontSize: 24, color: C.mute }}>ingezet in</div>
          <div style={{ fontFamily: SERIF, fontWeight: 700, fontSize: 52, color: C.terra }}>het binnenland</div>
        </Card>
      </Pop>
      <div style={{ position: 'absolute', left: 380 + 840 * mv, top: 540, transform: `rotate(${-6 + 12 * mv}deg)` }}>
        <div style={{ background: C.dark, color: C.amber, fontFamily: SANS, fontWeight: 700, fontSize: 30, padding: '20px 30px', borderRadius: 18, boxShadow: '0 16px 30px rgba(18,49,42,.25)' }}>Kredietmodel</div>
      </div>
      <div style={{ position: 'absolute', left: 1240, top: 640, opacity: warn, transform: `scale(${0.7 + 0.3 * warn})`, fontFamily: SANS, fontWeight: 700, fontSize: 30, color: C.terra }}>⚠ andere mensen, andere situatie</div>
      <Pop at={F('d7a', 3)} style={{ left: 200, top: 700, width: 700 }}>
        <div style={{ fontFamily: SANS, fontSize: 26, color: C.mute }}>Ook: een model voor <b>consumptief</b> krediet dat wordt gebruikt voor <b>zakelijk</b> krediet.</div>
      </Pop>
    </AbsoluteFill>
  );
};

/* D8: Grondwet artikel 8 */
const Law = () => {
  const frame = useCurrentFrame();
  const words = ['geboorte', 'geslacht', 'ras', 'godsdienst', '…', 'economische positie', 'sociale omstandigheden'];
  return (
    <AbsoluteFill style={{ background: C.light }}>
      <Title at={F('d8a', 0)} kicker="Bias en discriminatie">Technisch begrip, of ongerechtvaardigd onderscheid?</Title>
      <Pop at={F('d8b', 0)} style={{ left: 128, top: 300, width: 980 }}>
        <Card style={{ borderLeft: `10px solid ${C.dark}` }}>
          <div style={{ fontFamily: SANS, fontWeight: 700, fontSize: 24, color: C.mute, letterSpacing: 1 }}>GRONDWET VAN SURINAME · ARTIKEL 8 LID 2</div>
          <div style={{ fontFamily: SERIF, fontSize: 32, color: C.ink, marginTop: 12, lineHeight: 1.3 }}>Verbiedt discriminatie op grond van onder meer:</div>
          <div style={{ display: 'flex', flexWrap: 'wrap', gap: 10, marginTop: 14 }}>
            {words.map((w, i) => {
              const hot = i >= 5;
              const on = interpolate(frame, [F('d8b', 1 + i * 0.6), F('d8b', 1.3 + i * 0.6)], [0, 1], clamp);
              return <span key={w} style={{ fontFamily: SANS, fontWeight: 700, fontSize: 26, padding: '8px 16px', borderRadius: 10, opacity: on, background: hot ? C.amber : C.sand, color: C.ink }}>{w}</span>;
            })}
          </div>
        </Card>
      </Pop>
      <Pop at={F('d8c', 0)} style={{ left: 1180, top: 300, width: 610 }}>
        <Card>
          <div style={{ fontFamily: SANS, fontSize: 24, color: C.mute }}>Kredietmodel</div>
          <div style={{ fontFamily: SERIF, fontWeight: 600, fontSize: 36, color: C.ink, marginTop: 8, lineHeight: 1.2 }}>Rekening houden met inkomen is nodig: kan iemand terugbetalen?</div>
        </Card>
      </Pop>
      <Banner at={F('d8d', 0.4)} top={720} size={42}>Niet óf er onderscheid is, maar of het <span style={{ color: C.amber }}>gerechtvaardigd en proportioneel</span> is.</Banner>
    </AbsoluteFill>
  );
};

export const Clip6 = () => {
  const scenes = [
    ['t0', <TitleScene n={6} title="Waar komt bias vandaan?" sub="Zes bronnen van scheefheid, met Suribank als voorbeeld" />],
    ['d1a', <Scale />],
    ['d2a', <History />],
    ['d3a', <Representation />],
    ['d4a', <Measure />],
    ['q1', <QuizN n={1} q="q1" a="a1" question="Bij mensen met informeel werk ontbreekt vaker het inkomen in de data. Welke bron van bias is dit?" options={['A. Meetbias', 'B. Gebruiksbias']} good={0} note={<>Meetbias: het inkomen wordt voor die groep <span style={{ color: C.amber }}>slechter gemeten</span>.</>} />],
    ['d5a', <Label />],
    ['d6a', <Aggregate />],
    ['d7a', <Use />],
    ['d8a', <Law />],
    ['q2', <QuizN n={2} q="q2" a="a2" question="Een kredietmodel houdt rekening met inkomen. Is dat discriminatie op grond van economische positie?" options={['A. Ja, altijd.', 'B. Niet zonder meer: terugbetaalcapaciteit is een legitiem doel, maar het onderscheid moet proportioneel zijn en niet verder gaan dan nodig.']} good={1} note={<>Onderscheid is niet altijd discriminatie: <span style={{ color: C.amber }}>gerechtvaardigd en proportioneel?</span></>} />],
    ['d9a', <Summary k="d9a" title="Zes bronnen van bias" items={['Historisch', 'Representatie', 'Meting', 'Label', 'Aggregatie', 'Gebruik']} bannerKey="d9b" banner={<>Bias is technisch. Of het <span style={{ color: C.amber }}>discriminatie</span> is, vraagt om een ethische en juridische afweging.</>} />],
  ];
  return <Composition scenes={scenes} />;
};
