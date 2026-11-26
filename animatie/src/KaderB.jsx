import React from 'react';
import { AbsoluteFill, useCurrentFrame, interpolate, spring } from 'remotion';
import timing from './timing_kB.json';
import {
  C, SERIF, SANS, FPS, clamp, makeF, useSpr, mix, Pop, Card, Banner, Heading, Dot,
  Quiz8, TitleScene, SummaryScene, ClipShell, Shanti, Person,
} from './wk3kit';

const tm = makeF(timing);
const { F } = tm;
const on = (frame, k, o = 0) => frame >= F(k, o);

const PARTS = [['Transparantie', 6, C.green], ['Verantwoording', 2, C.dark], ['Algoritmische bias', 5, C.terra], ['Privacy', 4, C.amber]];

/* ---------- seal ---------- */
const Seal = ({ size = 420, fill = [0, 0, 0, 0], rot = 0, labels = true }) => (
  <svg width={size} height={size} viewBox="0 0 420 420">
    <g transform={`rotate(${rot} 210 210)`}>
      {Array.from({ length: 24 }, (_, i) => <circle key={i} cx={210 + 196 * Math.cos(i * Math.PI / 12)} cy={210 + 196 * Math.sin(i * Math.PI / 12)} r="14" fill={C.amber} />)}
      <circle cx="210" cy="210" r="190" fill={C.amber} />
      <circle cx="210" cy="210" r="168" fill={C.card} />
    </g>
    {PARTS.map(([t, d, col], i) => {
      const a0 = -Math.PI / 2 + i * Math.PI / 2, a1 = a0 + Math.PI / 2;
      const r = 150, cx = 210, cy = 210;
      const p = `M${cx} ${cy} L${cx + r * Math.cos(a0)} ${cy + r * Math.sin(a0)} A${r} ${r} 0 0 1 ${cx + r * Math.cos(a1)} ${cy + r * Math.sin(a1)} Z`;
      return <path key={t} d={p} fill={mix(fill[i], C.sand, col)} stroke={C.card} strokeWidth="6" />;
    })}
    {labels && PARTS.map(([t], i) => {
      const am = -Math.PI / 2 + i * Math.PI / 2 + Math.PI / 4;
      return <text key={t} x={210 + 80 * Math.cos(am)} y={210 + 80 * Math.sin(am) + 6} textAnchor="middle" fontFamily={SANS} fontWeight="700" fontSize="14.5" fill={fill[i] > 0.5 ? C.card : 'transparent'}>{['Transparantie', 'Verantwoording', 'Bias', 'Privacy'][i]}</text>;
    })}
  </svg>
);

const Title = () => {
  const frame = useCurrentFrame();
  const rot = interpolate(frame, [0, F('B1a', 0)], [-40, 0], clamp);
  return (
    <TitleScene at={F('B0a', -0.3)} kicker="KADERCLIP B · AI &amp; ETHICS · BLOK 1" title="IEEE CertifAIEd">
      <div style={{ position: 'absolute', left: 140, top: 560, width: 900, fontFamily: SANS, fontSize: 38, color: '#C9D8D1' }}>transparantie en bias toetsen</div>
      <div style={{ position: 'absolute', left: 1280, top: 250 }}><Seal size={460} rot={rot} /></div>
    </TitleScene>
  );
};

/* ---------- B1: four parts → domains ---------- */
const DOMAINS = ['Doel, noodzaak en proportionaliteit', 'Governance en verantwoording', 'Stakeholders en mensenrechten', 'Data en privacy', 'Fairness, bias en non-discriminatie', 'Transparantie en uitlegbaarheid', 'Menselijke controle en bezwaar', 'Veiligheid en robuustheid', 'AI-geletterdheid', 'Duurzaamheid', 'Monitoring en audit'];
const Parts = () => {
  const frame = useCurrentFrame();
  const fill = PARTS.map((_, i) => interpolate(frame, [F('B1d', 0.6 + i * 1.1), F('B1d', 1.0 + i * 1.1)], [0, 1], clamp));
  const listOn = useSpr(F('B1e', 0));
  const hl = (d) => {
    const idx = PARTS.findIndex((p) => p[1] === d);
    if (idx < 0) return 0;
    return interpolate(frame, [F('B1f', idx * 0.9), F('B1f', idx * 0.9 + 0.4)], [0, 1], clamp);
  };
  const privOff = on(frame, 'B1g', 0.3);
  return (
    <AbsoluteFill style={{ background: C.light }}>
      <Heading at={F('B1a', 0)} kicker="IEEE · GROOTSTE BEROEPSVERENIGING VAN INGENIEURS">CertifAIEd: een keurmerk voor ethische AI</Heading>
      <Pop at={F('B1b', 0)} style={{ left: 150, top: 300 }}>
        <Seal size={420} fill={fill} />
      </Pop>
      <Pop at={F('B1c', 0.2)} style={{ left: 150, top: 740 }}>
        <div style={{ display: 'flex', flexDirection: 'column', gap: 10, alignItems: 'flex-start', fontFamily: SANS, fontSize: 26, color: C.mute }}>
          <span style={{ background: C.sand, borderRadius: 999, padding: '8px 20px', fontWeight: 700, color: C.dark }}>keurmerk voor het systeem</span>
          <span style={{ background: C.sand, borderRadius: 999, padding: '8px 20px', fontWeight: 700, color: C.dark }}>certificaat voor de beoordelaar</span>
        </div>
      </Pop>
      <div style={{ position: 'absolute', left: 760, top: 270, width: 1030, opacity: listOn, transform: `translateX(${(1 - listOn) * 40}px)` }}>
        <div style={{ fontFamily: SANS, fontWeight: 700, fontSize: 24, letterSpacing: 2, color: C.green, marginBottom: 8 }}>ONS KADER · LAAG WAT · 11 DOMEINEN</div>
        {DOMAINS.map((d, i) => {
          const h = hl(i + 1);
          const part = PARTS.find((p) => p[1] === i + 1);
          const dim = part && part[1] === 4 && privOff;
          return (
            <div key={d} style={{ display: 'flex', alignItems: 'center', gap: 16, padding: '3px 14px', marginTop: 2, borderRadius: 12, background: h ? mix(h, C.light, dim ? C.sand : '#FFF6DD') : 'transparent', border: `2px solid ${h > 0.5 ? (part ? part[2] : C.line) : 'transparent'}` }}>
              <span style={{ fontFamily: SERIF, fontWeight: 700, fontSize: 26, width: 40, color: h > 0.5 ? part[2] : '#A9A296' }}>{i + 1}</span>
              <span style={{ fontFamily: SANS, fontSize: 25, color: h > 0.5 ? C.ink : C.mute, fontWeight: h > 0.5 ? 700 : 400 }}>{d}</span>
              {h > 0.5 && <span style={{ marginLeft: 'auto', fontFamily: SANS, fontWeight: 700, fontSize: 22, color: C.card, background: dim ? '#A9A296' : part[2], borderRadius: 999, padding: '4px 14px' }}>{dim ? 'privacy → A-DG' : part[0]}</span>}
            </div>
          );
        })}
      </div>
    </AbsoluteFill>
  );
};

/* ---------- B2: drivers vs inhibitors ---------- */
const Balance = () => {
  const frame = useCurrentFrame();
  const tilt = interpolate(frame, [F('B2b', 0), F('B2b', 1.5), F('B2c', 0), F('B2c', 1.5), F('B2e', 0), F('B2e', 1.5)], [0, -9, -9, 7, 7, 0], clamp);
  const up = useSpr(F('B2b', 0.3)), down = useSpr(F('B2c', 0.3));
  return (
    <AbsoluteFill style={{ background: C.light }}>
      <Heading at={F('B2a', 0)} kicker="PER ONDERDEEL">Wat helpt, en wat werkt tegen?</Heading>
      <div style={{ position: 'absolute', left: 560, top: 300 }}>
        <svg width="800" height="420" viewBox="0 0 800 420">
          <rect x="392" y="60" width="16" height="320" fill={C.dark} /><rect x="300" y="372" width="200" height="22" rx="11" fill={C.dark} />
          <g transform={`rotate(${tilt} 400 70)`}>
            <rect x="80" y="62" width="640" height="14" rx="7" fill={C.dark} />
            <path d="M140 76 L90 190 H190 Z" fill="none" stroke={C.green} strokeWidth="5" /><path d="M80 190 Q140 236 200 190Z" fill={C.green} />
            <path d="M660 76 L610 190 H710 Z" fill="none" stroke={C.terra} strokeWidth="5" /><path d="M600 190 Q660 236 720 190Z" fill={C.terra} />
            <g opacity={up}>{[0, 1, 2].map((i) => <text key={i} x={105 + i * 35} y={175 - 18 * Math.sin(frame / 8 + i)} fontSize="42" fill={C.green} fontWeight="700">↑</text>)}</g>
            <g opacity={down}>{[0, 1, 2].map((i) => <text key={i} x={625 + i * 35} y={160 + 18 * Math.sin(frame / 8 + i)} fontSize="42" fill={C.terra} fontWeight="700">↓</text>)}</g>
          </g>
          <circle cx="400" cy="68" r="16" fill={C.amber} />
        </svg>
      </div>
      <Pop at={F('B2b', 0)} style={{ left: 150, top: 330, width: 420 }}>
        <Card><div style={{ fontFamily: SERIF, fontWeight: 700, fontSize: 44, color: C.green }}>Drivers</div>
          <div style={{ fontFamily: SANS, fontSize: 28, color: C.mute }}>maken ethisch werken waarschijnlijker</div></Card>
      </Pop>
      <Pop at={F('B2c', 0)} style={{ left: 1360, top: 330, width: 420 }}>
        <Card><div style={{ fontFamily: SERIF, fontWeight: 700, fontSize: 44, color: C.terra }}>Inhibitors</div>
          <div style={{ fontFamily: SANS, fontSize: 28, color: C.mute }}>werken het tegen, om begrijpelijke redenen</div></Card>
      </Pop>
      <Pop at={F('B2d', 0.2)} style={{ left: 1360, top: 560, width: 420 }}>
        {['geen claims', 'idee niet weggeven'].map((t, i) => (
          <div key={t} style={{ opacity: on(frame, 'B2d', i * 1.6) ? 1 : 0, marginTop: 12, background: '#F6E2DC', border: `2px solid ${C.terra}`, borderRadius: '20px 20px 20px 6px', padding: '12px 20px', fontFamily: SANS, fontSize: 28, color: C.ink }}>💭 {t}</div>
        ))}
      </Pop>
      <Banner at={F('B2e', 0.6)} top={790} size={38}>Alleen drivers = goede bedoelingen. <span style={{ color: C.amber }}>Ook inhibitors = waarom het strandt.</span></Banner>
    </AbsoluteFill>
  );
};

/* ---------- B3/B4: Frisco orderagent, transparency ---------- */
const Phone = ({ children, banner, footer }) => (
  <div style={{ width: 500, height: 700, borderRadius: 52, background: C.dark, padding: 15, boxShadow: '0 30px 60px rgba(18,49,42,.28)' }}>
    <div style={{ width: '100%', height: '100%', borderRadius: 40, background: C.card, overflow: 'hidden', display: 'flex', flexDirection: 'column' }}>
      <div style={{ background: '#F0EBE1', padding: '24px 24px 14px', borderBottom: `2px solid ${C.line}` }}>
        <div style={{ fontFamily: SANS, fontWeight: 700, fontSize: 26, color: C.ink }}>Frisco Installaties</div>
        <div style={{ fontFamily: SANS, fontSize: 20, color: C.mute }}>bestellingen en offertes</div>
      </div>
      {banner}
      <div style={{ padding: '6px 20px', flex: 1 }}>{children}</div>
      {footer}
    </div>
  </div>
);
const Msg = ({ me, children, show }) => (
  <div style={{ display: 'flex', justifyContent: me ? 'flex-end' : 'flex-start', marginTop: 12, opacity: show ? 1 : 0 }}>
    <div style={{ maxWidth: 380, background: me ? C.green : '#E6EEEA', color: me ? C.card : C.ink, borderRadius: me ? '20px 20px 6px 20px' : '20px 20px 20px 6px', padding: '12px 18px', fontFamily: SANS, fontSize: 24, lineHeight: 1.35 }}>{children}</div>
  </div>
);
const FriscoPhone = ({ frame, k0 }) => {
  const banner = on(frame, 'B3c', 0.5);
  const foot = on(frame, 'B3e', 0.3);
  return (
    <Phone
      banner={<div style={{ background: C.amber, color: C.dark, fontFamily: SANS, fontWeight: 700, fontSize: 22, padding: '10px 20px', opacity: banner ? 1 : 0 }}>🤖 U praat met een digitale assistent</div>}
      footer={<div style={{ display: 'flex', gap: 12, padding: '14px 20px', borderTop: `2px solid ${C.line}`, opacity: foot ? 1 : 0 }}>
        <span style={{ flex: 1, background: C.dark, color: C.card, borderRadius: 999, textAlign: 'center', padding: '10px 0', fontFamily: SANS, fontWeight: 700, fontSize: 22 }}>Medewerker</span>
        <span style={{ background: C.sand, borderRadius: 999, padding: '10px 18px', fontSize: 22 }}>👍</span><span style={{ background: C.sand, borderRadius: 999, padding: '10px 18px', fontSize: 22 }}>👎</span></div>}>
      <Msg me show={on(frame, k0, 0.4)}>Kunnen jullie volgende week een koelinstallatie plaatsen?</Msg>
      <Msg show={on(frame, k0, 1.6)}>Zeker! Levering dinsdag, prijs SRD 48.000.</Msg>
      <Msg me show={on(frame, 'B3b', 1.0)}>Top, dan reken ik daarop.</Msg>
    </Phone>
  );
};
const Drivers = () => {
  const frame = useCurrentFrame();
  const list = [['B3c', 'Weet dat je met AI praat'], ['B3d', 'Werking helder: wat kan de agent wel en niet'], ['B3e', 'Ingrijpen, feedback en een mens'], ['B3f', 'Voorspelbaar gedrag, van ontwerp tot gebruik']];
  return (
    <AbsoluteFill style={{ background: C.light }}>
      <Heading at={F('B3a', 0)} kicker="TRANSPARANTIE · DRIVERS">De orderagent van Frisco</Heading>
      <Pop at={F('B3a', 0.4)} style={{ left: 160, top: 250 }}><FriscoPhone frame={frame} k0="B3a" /></Pop>
      <div style={{ position: 'absolute', left: 820, top: 300, width: 960 }}>
        {list.map(([k, t]) => (
          <Pop key={k} at={F(k, 0.2)} style={{ position: 'relative' }}>
            <div style={{ display: 'flex', gap: 20, alignItems: 'center', marginBottom: 22, background: C.card, border: `2px solid ${C.line}`, borderRadius: 18, padding: '18px 26px' }}>
              <span style={{ width: 52, height: 52, borderRadius: 26, background: C.green, color: C.card, display: 'flex', alignItems: 'center', justifyContent: 'center', fontSize: 32, fontWeight: 700 }}>✓</span>
              <span style={{ fontFamily: SANS, fontWeight: 600, fontSize: 34, color: C.ink }}>{t}</span>
            </div>
          </Pop>
        ))}
      </div>
    </AbsoluteFill>
  );
};
const Inhibitors = () => {
  const frame = useCurrentFrame();
  const cards = [['B4b', 'Gedrag verhullen'], ['B4c', 'Angst voor aansprakelijkheid'], ['B4d', 'Bedrijfsgeheim']];
  const mgr = useSpr(F('B4f', 0));
  return (
    <AbsoluteFill style={{ background: C.light }}>
      <Heading at={F('B4a', 0)} kicker="TRANSPARANTIE · INHIBITORS">Drie redenen om te zwijgen</Heading>
      <div style={{ position: 'absolute', left: 160, top: 250, opacity: 0.55 }}><FriscoPhone frame={F('B3f', 2)} k0="B3a" /></div>
      {cards.map(([k, t], i) => {
        const s = spring({ frame: frame - F(k, 0), fps: FPS, config: { damping: 14, stiffness: 110 } });
        return (
          <div key={k} style={{ position: 'absolute', left: 120 + 40 * i + (1 - s) * -600, top: 330 + i * 130, opacity: s, transform: `rotate(${-4 + i * 3}deg)` }}>
            <div style={{ background: C.terra, color: C.card, fontFamily: SANS, fontWeight: 700, fontSize: 36, padding: '22px 34px', borderRadius: 18, boxShadow: '0 14px 30px rgba(168,67,44,.35)', width: 560 }}>✗ {t}</div>
          </div>
        );
      })}
      <Pop at={F('B4e', 0.3)} style={{ left: 820, top: 300, width: 520 }}>
        <Card style={{ borderColor: C.terra }}>
          <div style={{ fontFamily: SANS, fontWeight: 700, fontSize: 22, letterSpacing: 2, color: C.terra }}>CONTRACT LEVERANCIER</div>
          <div style={{ fontFamily: SERIF, fontWeight: 600, fontSize: 34, color: C.ink, marginTop: 8 }}>Naam van de taaldienst: geheim</div>
          <div style={{ fontFamily: SANS, fontSize: 26, color: C.mute, marginTop: 8 }}>De klant weet niet waar zijn gegevens heen gaan.</div>
        </Card>
      </Pop>
      <div style={{ position: 'absolute', left: 1400, top: 260, opacity: mgr, transform: `translateY(${(1 - mgr) * 30}px)` }}>
        <div style={{ background: C.card, border: `2px solid ${C.line}`, borderRadius: '24px 24px 6px 24px', padding: '16px 24px', fontFamily: SANS, fontSize: 30, color: C.ink, width: 360 }}>“Dat kunnen we niet vertellen.”</div>
        <div style={{ marginLeft: 150, marginTop: 10 }}><Person size={200} frame={frame} body={C.dark} tie skin="#A06A45" /></div>
      </div>
    </AbsoluteFill>
  );
};

/* ---------- B5: bias drivers at Suribank ---------- */
const FEATURES = ['inkomen', 'looptijd', 'soort werk', 'district', 'afstand tot filiaal'];
const BiasScene = () => {
  const frame = useCurrentFrame();
  const glass = interpolate(frame, [F('B5b', 0), F('B5b', 3)], [0, 1], clamp);
  const struck = on(frame, 'B5c', 2.5);
  const proxy = on(frame, 'B5d', 1.0);
  const pay = on(frame, 'B5g', 1.5);
  const checks = [['B5b', 'Context van alle betrokkenen'], ['B5c', 'Beschermd kenmerk: gebruik of weglaten onderbouwen'], ['B5e', 'Gedrag per groep volgen, ook na livegang'], ['B5f', 'Biasprofiel bijhouden en corrigeren']];
  const grp = (good, n) => Array.from({ length: n }, (_, i) => good[i]);
  return (
    <AbsoluteFill style={{ background: C.light }}>
      <Heading at={F('B5a', 0)} kicker="ALGORITMISCHE BIAS · DRIVERS">Suribank, zoals in practicum 2</Heading>
      <Pop at={F('B5a', 0.5)} style={{ left: 128, top: 250 }}>
        <div style={{ display: 'flex', gap: 60 }}>
          {[['Paramaribo', false], ['Binnenland', true]].map(([n, inl]) => (
            <div key={n}>
              <div style={{ fontFamily: SANS, fontWeight: 700, fontSize: 28, color: C.ink, marginBottom: 10 }}>{n}</div>
              <div style={{ display: 'grid', gridTemplateColumns: 'repeat(4, 54px)', gap: 10 }}>
                {Array.from({ length: 12 }, (_, i) => {
                  const red = inl && pay && i % 3 !== 2;
                  return <Dot key={i} size={50} good fill={red ? C.terra : null} ring={red ? C.terra : null} />;
                })}
              </div>
            </div>
          ))}
        </div>
      </Pop>
      <div style={{ position: 'absolute', left: 420 + glass * 40, top: 300, opacity: glass > 0 && !pay ? 1 : 0 }}>
        <svg width="170" height="170"><circle cx="66" cy="66" r="52" fill="rgba(227,169,43,.18)" stroke={C.amber} strokeWidth="10" /><path d="M104 104 L156 156" stroke={C.amber} strokeWidth="18" strokeLinecap="round" /></svg>
      </div>
      <div style={{ position: 'absolute', left: 150, top: 470, width: 170, height: 200, opacity: interpolate(frame, [F('B5b', 1), F('B5b', 1.6)], [0, 1], clamp) }}><Shanti frame={frame} label={false} /></div>
      <Pop at={F('B5c', 0.5)} style={{ left: 360, top: 500, width: 440 }}>
        <Card style={{ padding: '16px 22px' }}>
          <div style={{ fontFamily: SANS, fontWeight: 700, fontSize: 20, letterSpacing: 2, color: C.mute }}>KENMERKEN MODEL</div>
          {FEATURES.map((f) => {
            const isD = f === 'district', isP = f === 'afstand tot filiaal';
            return <div key={f} style={{ fontFamily: SANS, fontSize: 25, marginTop: 6, color: isD && struck ? '#A9A296' : C.ink, textDecoration: isD && struck ? 'line-through' : 'none',
              background: isP && proxy ? '#FFF0C8' : 'transparent', borderRadius: 8, padding: '0 6px', fontWeight: isP && proxy ? 700 : 400 }}>{f}{isP && proxy ? ' ← verraadt het district' : ''}</div>;
          })}
        </Card>
      </Pop>
      <div style={{ position: 'absolute', left: 860, top: 280, width: 930 }}>
        {checks.map(([k, t]) => (
          <Pop key={k} at={F(k, 0.2)} style={{ position: 'relative' }}>
            <div style={{ display: 'flex', gap: 18, alignItems: 'center', marginBottom: 18, background: C.card, border: `2px solid ${C.line}`, borderRadius: 18, padding: '16px 24px' }}>
              <span style={{ width: 48, height: 48, borderRadius: 24, background: C.green, color: C.card, display: 'flex', alignItems: 'center', justifyContent: 'center', fontSize: 28, fontWeight: 700, flexShrink: 0 }}>✓</span>
              <span style={{ fontFamily: SANS, fontWeight: 600, fontSize: 31, color: C.ink }}>{t}</span>
            </div>
          </Pop>
        ))}
      </div>
      <Banner at={F('B5g', 0.4)} top={800} size={36}>Niemand doet het? <span style={{ color: C.amber }}>De goede betalers in het binnenland betalen de prijs.</span></Banner>
    </AbsoluteFill>
  );
};

/* ---------- B6: lack of process transparency ---------- */
const Fog = () => {
  const frame = useCurrentFrame();
  const fog = interpolate(frame, [F('B6a', 0.5), F('B6b', 1.5)], [0, 0.82], clamp);
  const shake = Math.sin(frame / 2) * 6 * interpolate(frame, [F('B6b', 2), F('B6b', 3), F('B6c', 0)], [0, 1, 0], clamp);
  const clear = interpolate(frame, [F('B6c', 0.5), F('B6c', 2)], [0, 1], clamp);
  const sources = ['Bron data?', 'Wie besloot?', 'Welke versie?', 'Waarom zo?'];
  return (
    <AbsoluteFill style={{ background: C.light }}>
      <Heading at={F('B6a', 0)} kicker="ALGORITMISCHE BIAS · INHIBITOR">Gebrek aan procestransparantie</Heading>
      <div style={{ position: 'absolute', left: 150, top: 280, display: 'flex', gap: 30 }}>
        {sources.map((s, i) => (
          <Card key={s} style={{ width: 340, textAlign: 'center', padding: '28px 20px' }}>
            <div style={{ fontFamily: SERIF, fontWeight: 700, fontSize: 70, color: C.terra }}>?</div>
            <div style={{ fontFamily: SANS, fontWeight: 600, fontSize: 30, color: C.ink }}>{s}</div>
          </Card>
        ))}
      </div>
      <div style={{ position: 'absolute', left: 0, top: 240, width: 1920, height: 330, background: `linear-gradient(90deg, rgba(246,243,236,${fog * (1 - clear)}) 0%, rgba(214,208,196,${fog * (1 - clear)}) 50%, rgba(246,243,236,${fog * (1 - clear)}) 100%)`, filter: 'blur(8px)' }} />
      <Pop at={F('B6b', 1.8)} style={{ left: 150, top: 620 }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: 24, transform: `translateX(${shake}px)` }}>
          <svg width="520" height="70"><rect x="0" y="10" width="520" height="50" rx="8" fill={C.amber} />{Array.from({ length: 26 }, (_, i) => <rect key={i} x={10 + i * 20} y="10" width="3" height={i % 5 === 0 ? 30 : 18} fill={C.dark} />)}</svg>
          <span style={{ fontFamily: SANS, fontWeight: 700, fontSize: 32, color: clear > 0.5 ? C.green : C.terra }}>{clear > 0.5 ? 'per groep gemeten: verschil zichtbaar' : 'bias meten lukt niet'}</span>
        </div>
      </Pop>
      <Banner at={F('B6d', 0.3)} top={790} size={36}>Ook bij de orderagent: <span style={{ color: C.amber }}>zonder logboek</span> weet je niet of de districten slechter geholpen worden.</Banner>
    </AbsoluteFill>
  );
};

/* ---------- B7: evidence per goal ---------- */
const Evidence = () => {
  const frame = useCurrentFrame();
  const rows = [['Klant weet dat het AI is', 'Begroeting agent + test practicum 4', 4, true], ['Werking helder beschreven', 'Productpagina', 3, true], ['Toegankelijke controle', '(geen bewijs)', 3, false]];
  const struck = on(frame, 'B7c', 0.3);
  const scan = useSpr(F('B7d', 0.3));
  return (
    <AbsoluteFill style={{ background: C.light }}>
      <Heading at={F('B7a', 0)} kicker="ZO KOMT EEN BEOORDELAAR TOT EEN OORDEEL">Bewijs per doel, score 1 tot 5</Heading>
      <Pop at={F('B7b', 0)} style={{ left: 128, top: 260, width: 1100 }}>
        <div style={{ background: C.card, border: `2px solid ${C.line}`, borderRadius: 20, overflow: 'hidden' }}>
          <div style={{ display: 'grid', gridTemplateColumns: '1.3fr 1.6fr 0.5fr', background: C.sand, fontFamily: SANS, fontWeight: 700, fontSize: 26, color: C.dark, padding: '14px 24px' }}><span>Doel</span><span>Bewijs</span><span>Score</span></div>
          {rows.map(([d, b, s, ok], i) => {
            const show = on(frame, 'B7b', 1.5 + i * 0.9);
            const x = !ok && struck;
            return (
              <div key={d} style={{ display: 'grid', gridTemplateColumns: '1.3fr 1.6fr 0.5fr', padding: '16px 24px', borderTop: `2px solid ${C.line}`, fontFamily: SANS, fontSize: 27, color: C.ink, opacity: show ? 1 : 0, background: x ? '#F6E2DC' : 'transparent' }}>
                <span>{d}</span><span style={{ color: ok ? C.ink : C.terra }}>{b}</span>
                <span style={{ fontFamily: SERIF, fontWeight: 700, fontSize: 36, color: x ? C.terra : C.green, textDecoration: x ? 'line-through' : 'none' }}>{s}</span>
              </div>
            );
          })}
        </div>
        <div style={{ fontFamily: SANS, fontWeight: 700, fontSize: 30, color: C.terra, marginTop: 14, opacity: struck ? 1 : 0 }}>Een score zonder bewijs telt niet.</div>
      </Pop>
      <div style={{ position: 'absolute', left: 1290, top: 260, width: 500, opacity: scan, transform: `translateX(${(1 - scan) * 40}px)` }}>
        <Card>
          <div style={{ fontFamily: SANS, fontWeight: 700, fontSize: 22, letterSpacing: 2, color: C.green }}>JULLIE SNELLE SCAN (K4)</div>
          {[1, 2, 3, 4, 5, 6, 7].map((d) => {
            const h = d === 5 || d === 6;
            return <div key={d} style={{ display: 'flex', justifyContent: 'space-between', fontFamily: SANS, fontSize: 26, marginTop: 8, padding: '4px 10px', borderRadius: 8, background: h && on(frame, 'B7g', 0.3) ? '#FFF0C8' : 'transparent', fontWeight: h ? 700 : 400, color: C.ink }}>
              <span>Domein {d}</span><span>{d === 6 && on(frame, 'B7e', 1.5) ? '3 · bewijs ✓' : '…'}</span></div>;
          })}
        </Card>
      </div>
      <Banner at={F('B7f', 0.3)} top={790} size={36}>Bedrijfsgeheim houdt de score laag? <span style={{ color: C.amber }}>Noem die inhibitor als reden.</span></Banner>
    </AbsoluteFill>
  );
};

/* ---------- B9: now you ---------- */
const Now = () => (
  <AbsoluteFill style={{ background: C.light }}>
    <Heading at={F('B9a', 0)}>Nu jij, met je groep</Heading>
    {[['B9a', 'Pak jullie snelle scan erbij'], ['B9b', 'Welke inhibitor herken je bij jullie partner of leverancier?'], ['B9c', 'Wat betekent dat voor jullie score op domein 6? Gebruik het in je nulmeting']].map(([k, t], i) => (
      <Pop key={k} at={F(k, 0.3)} style={{ left: 128, top: 250 + i * 170, width: 1664 }}>
        <Card style={{ display: 'flex', gap: 30, alignItems: 'center', padding: '24px 36px' }}>
          <span style={{ fontFamily: SERIF, fontWeight: 700, fontSize: 64, color: C.green, width: 50 }}>{i + 1}</span>
          <span style={{ fontFamily: SANS, fontWeight: 600, fontSize: 36, color: C.ink }}>{t}</span>
        </Card>
      </Pop>
    ))}
  </AbsoluteFill>
);

export const KaderB = () => (
  <ClipShell timing={timing} scenes={[
    ['B0a', <Title />], ['B1a', <Parts />], ['B2a', <Balance />], ['B3a', <Drivers />], ['B4a', <Inhibitors />],
    ['BQ1', <Quiz8 tm={tm} n={1} q="BQ1" a="BQ1b" optAt={0.62} question="Een bedrijf vertelt klanten niet dat een chatbot hun vragen beantwoordt, uit angst voor claims. Wat is dit volgens CertifAIEd?" options={['A. Een driver van transparantie', 'B. Een inhibitor: angst voor aansprakelijkheid']} good={1} />],
    ['B5a', <BiasScene />], ['B6a', <Fog />],
    ['BQ2', <Quiz8 tm={tm} n={2} q="BQ2" a="BQ2b" optAt={0.6} question="Een bank laat district weg uit het model, maar legt niet vast waarom en meet de uitkomsten per regio niet. Welke drivers ontbreken vooral?" options={['A. Weten dat je met AI praat', 'B. Gebruik van beschermde kenmerken onderbouwen, en gedrag per groep volgen']} good={1} />],
    ['B7a', <Evidence />],
    ['B8a', <SummaryScene tm={tm} keys={['B8a', 'B8b', 'B8c', 'B8d']} items={['Vier onderdelen: domein 2, 4, 5 en 6', 'Kijk naar wat helpt én naar wat tegenwerkt', 'Onderbouw elke score met bewijs']} />],
    ['B9a', <Now />],
  ]} />
);
