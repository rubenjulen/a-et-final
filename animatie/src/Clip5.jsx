import React from 'react';
import timing from './timing_c5.json';
import {
  C, SERIF, SANS, FPS, clamp, Easing, interpolate, spring, useCurrentFrame, AbsoluteFill,
  useSpring, fade, Pop, Banner, Title, Shanti, MiniShanti, Figure, Bubble, Phone, makeKit,
} from './wk1_kit';

const { F, QuizN, Root } = makeKit(timing);

const BOX = [
  ['Uitkomst', 'wat het systeem maakt', C.green],
  ['Beslissing', 'wat er daarna mee gebeurt', '#1F5A6B'],
  ['Gevolg', 'wat mensen ervan merken', C.terra],
];
const Boxes = ({ at, top = 260, scale = 1, shake = 0 }) => {
  const frame = useCurrentFrame();
  return (
    <>
      {BOX.map(([t, s, col], i) => {
        const a = spring({ frame: frame - at - i * 14, fps: FPS, config: { damping: 15 } });
        const jx = shake * Math.sin(frame / 2 + i * 2) * 14, jy = shake * Math.cos(frame / 3 + i) * 10;
        return (
          <div key={t} style={{ position: 'absolute', left: 128 + i * 590 * scale + jx, top: top + jy, width: 480 * scale, opacity: a, transform: `translateY(${(1 - a) * 40}px)`, background: C.card, border: `3px solid ${col}`, borderRadius: 22, padding: `${26 * scale}px ${30 * scale}px`, boxShadow: '0 12px 28px rgba(18,49,42,.10)' }}>
            <div style={{ fontFamily: SERIF, fontWeight: 700, fontSize: 50 * scale, color: col }}>{t}</div>
            <div style={{ fontFamily: SANS, fontSize: 28 * scale, color: C.ink, marginTop: 6 }}>{s}</div>
          </div>
        );
      })}
      {[0, 1].map((i) => {
        const d = interpolate(frame, [at + 20 + i * 14, at + 36 + i * 14], [0, 1], clamp);
        return <svg key={i} style={{ position: 'absolute', left: 128 + (480 + i * 590) * scale, top: top + 70 * scale }} width={110 * scale} height="60"><path d={`M8 30 L${8 + 80 * d * scale} 30`} stroke={C.dark} strokeWidth="7" strokeLinecap="round" />{d > 0.95 && <polygon points={`${88 * scale},14 ${104 * scale},30 ${88 * scale},46`} fill={C.dark} />}</svg>;
      })}
    </>
  );
};

/* 1. Intro */
const Intro5 = () => {
  const s = useSpring(F('p0', -0.4));
  return (
    <AbsoluteFill style={{ background: `radial-gradient(1200px 800px at 75% 30%, #1B4A3E 0%, ${C.dark} 60%)` }}>
      <div style={{ position: 'absolute', left: 140, top: 300, fontFamily: SANS, fontSize: 30, fontWeight: 700, letterSpacing: 3, color: C.amber, opacity: s }}>KENNISCLIP 5 · AI &amp; ETHICS · BLOK 1</div>
      <div style={{ position: 'absolute', left: 140, top: 360, width: 1200, fontFamily: SERIF, fontWeight: 700, fontSize: 124, lineHeight: 1.04, color: C.light, opacity: s, transform: `translateY(${(1 - s) * 50}px)` }}>Wie beslist er eigenlijk?</div>
    </AbsoluteFill>
  );
};

/* 2. Drie vakjes */
const Three = () => {
  const frame = useCurrentFrame();
  const k1 = useSpring(F('p1b', 0.2));
  const shake = interpolate(frame, [F('p1c', 0.2), F('p1c', 0.6), F('p1c', 2.6), F('p1c', 3.2)], [0, 1, 1, 0], clamp);
  return (
    <AbsoluteFill style={{ background: C.light }}>
      <Title at={F('p1', -0.2)} top={90} size={56}>Drie dingen, apart</Title>
      <Boxes at={F('p1', 1.0)} top={250} shake={shake} />
      <div style={{ position: 'absolute', left: 128, top: 520, width: 900, opacity: k1, transform: `translateY(${(1 - k1) * 30}px)`, background: C.card, border: `2px solid ${C.line}`, borderRadius: 16, padding: '20px 28px', fontFamily: SANS, fontSize: 28, color: C.ink }}>
        <div style={{ fontWeight: 700, fontSize: 22, letterSpacing: 2, color: C.green }}>K1 AI USE CASE &amp; SCOPE CANVAS</div>
        <div style={{ marginTop: 8 }}>Uitkomst: … · Beslissing: … · Gevolg: …</div>
      </div>
      <Pop at={F('p1c', 1.4)} style={{ left: 1100, top: 530, width: 690 }}>
        <div style={{ fontFamily: SERIF, fontWeight: 700, fontSize: 44, lineHeight: 1.15, color: C.terra }}>Door elkaar? Dan zie je niet waar het misgaat.</div>
      </Pop>
    </AbsoluteFill>
  );
};

/* 3. Voorspellend model */
const Predict = () => {
  const frame = useCurrentFrame();
  const g = useSpring(F('p2', 0.2));
  const kans = Math.round(72 * interpolate(frame, [F('p2', 0.4), F('p2', 1.6)], [0, 1], clamp));
  const thr = useSpring(F('p2b', 0.2));
  const paths = useSpring(F('p2c', 0.3));
  const human = useSpring(F('p2c', 2.0));
  return (
    <AbsoluteFill style={{ background: C.light }}>
      <Title at={F('p2', -0.3)} top={80} size={52} kicker="BIJ EEN VOORSPELLEND MODEL">Wie beslist er bij Suribank?</Title>
      <div style={{ position: 'absolute', left: 130, top: 300 }}><MiniShanti frame={frame} size={170} /></div>
      <div style={{ position: 'absolute', left: 110, top: 490, width: 220, fontFamily: SANS, fontWeight: 700, fontSize: 24, color: C.mute, textAlign: 'center' }}>aanvraag</div>
      <div style={{ position: 'absolute', left: 420, top: 250, width: 420, opacity: g, transform: `scale(${0.9 + 0.1 * g})`, background: C.card, border: `3px solid ${C.green}`, borderRadius: 22, padding: '26px 30px' }}>
        <div style={{ fontFamily: SANS, fontWeight: 700, fontSize: 24, letterSpacing: 2, color: C.green }}>MODEL · UITKOMST</div>
        <div style={{ fontFamily: SERIF, fontWeight: 700, fontSize: 96, color: C.ink }}>{kans}%</div>
        <div style={{ fontFamily: SANS, fontSize: 26, color: C.mute }}>kans op terugbetalen</div>
        <div style={{ position: 'relative', height: 26, background: C.sand, borderRadius: 13, marginTop: 20 }}>
          <div style={{ width: `${kans}%`, height: '100%', background: C.green, borderRadius: 13 }} />
          <div style={{ position: 'absolute', left: '60%', top: -14, width: 6, height: 54, background: C.terra, opacity: thr }} />
          <div style={{ position: 'absolute', left: 'calc(60% - 70px)', top: 46, width: 140, textAlign: 'center', fontFamily: SANS, fontWeight: 700, fontSize: 22, color: C.terra, opacity: thr }}>drempel 60%</div>
        </div>
      </div>
      <Pop at={F('p2b', 1.2)} style={{ left: 420, top: 640, width: 420 }}><div style={{ fontFamily: SANS, fontWeight: 700, fontSize: 26, color: '#1F5A6B' }}>De organisatie kiest de drempel.</div></Pop>
      <svg style={{ position: 'absolute', left: 860, top: 260, opacity: paths }} width="220" height="380">
        <path d="M10 160 C 100 160, 110 60, 200 60" stroke={C.dark} strokeWidth="6" fill="none" strokeDasharray="10 8" />
        <path d="M10 200 C 100 200, 110 300, 200 300" stroke={C.dark} strokeWidth="6" fill="none" />
      </svg>
      <div style={{ position: 'absolute', left: 1090, top: 250, opacity: paths, display: 'flex', alignItems: 'center', gap: 20 }}>
        <div style={{ background: C.green, color: C.card, fontFamily: SANS, fontWeight: 700, fontSize: 28, padding: '14px 24px', borderRadius: 14 }}>automatisch goedgekeurd</div>
      </div>
      <div style={{ position: 'absolute', left: 1090, top: 470, opacity: human, display: 'flex', alignItems: 'center', gap: 20 }}>
        <Figure size={90} color="#1F5A6B" badge />
        <div style={{ fontFamily: SANS, fontWeight: 700, fontSize: 28, color: C.ink }}>een medewerker beslist</div>
      </div>
      <Banner at={F('p2d', 0.2)} top={700} size={42}>De beslissing is van <span style={{ color: C.amber }}>de organisatie</span>, ook als niemand meer kijkt.</Banner>
    </AbsoluteFill>
  );
};

/* 4. Generatieve AI */
const Generative = () => {
  const frame = useCurrentFrame();
  const emp = useSpring(F('p3b', 0.2));
  const look = interpolate(frame, [F('p3b', 1.6), F('p3b', 2.2)], [1, 0.25], clamp);
  const acts = ['Formulier B-12 ingevuld', 'Betaling gedaan', 'Klacht laten vallen'];
  return (
    <AbsoluteFill style={{ background: C.light }}>
      <Title at={F('p3', -0.3)} top={70} size={52} kicker="BIJ GENERATIEVE AI">Een chatbot maakt een antwoord</Title>
      <Phone title="Klantenservice" sub="assistent" h={470} style={{ left: 128, top: 190, width: 500 }}>
        <Bubble who="me" at={F('p3', 0.4)} frame={frame}>Hoe vraag ik een vergoeding aan?</Bubble>
        <Bubble who="bot" at={F('p3', 1.6)} frame={frame}>Vul formulier B-12 in en betaal SRD 50 administratiekosten. Dan is het binnen 5 dagen geregeld.</Bubble>
      </Phone>
      <div style={{ position: 'absolute', left: 690, top: 240, opacity: emp * look, display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
        <Figure size={100} color="#1F5A6B" badge />
        <div style={{ fontFamily: SANS, fontWeight: 700, fontSize: 22, color: C.mute, marginTop: 6 }}>medewerker</div>
      </div>
      <Pop at={F('p3b', 1.8)} style={{ left: 640, top: 440, width: 280 }}><div style={{ fontFamily: SANS, fontWeight: 700, fontSize: 26, color: C.terra, textAlign: 'center' }}>leest vaak niet mee</div></Pop>
      <div style={{ position: 'absolute', left: 1000, top: 210 }}><MiniShanti frame={frame} size={140} /></div>
      <Pop at={F('p3c', 0)} style={{ left: 1170, top: 220, width: 640 }}><div style={{ fontFamily: SANS, fontWeight: 700, fontSize: 26, letterSpacing: 2, color: C.green }}>DE KLANT DOET ER IETS MEE</div></Pop>
      {acts.map((t, i) => (
        <Pop key={t} at={F('p3c', 1.2 + i * 1.3)} style={{ left: 1170, top: 290 + i * 96, width: 600 }}>
          <div style={{ background: C.card, border: `2px solid ${C.line}`, borderRadius: 14, padding: '16px 22px', fontFamily: SANS, fontSize: 30, color: C.ink }}><span style={{ color: C.green, fontWeight: 700 }}>✓</span> {t}</div>
        </Pop>
      ))}
      <Banner at={F('p3d', 0.3)} top={710} size={40}>Daar valt de beslissing: <span style={{ color: C.amber }}>bij de klant</span>, op basis van wat de organisatie liet zeggen.</Banner>
    </AbsoluteFill>
  );
};

/* 6. Gebruikers en betrokkenen */
const People = () => {
  const frame = useCurrentFrame();
  const ring = useSpring(F('p4', 0.2));
  const others = [['een aanvrager', 1150, 240], ['een klant over wie een samenvatting wordt gemaakt', 1150, 410], ['een medewerker die een rooster krijgt', 1150, 580]];
  return (
    <AbsoluteFill style={{ background: C.light }}>
      <Title at={F('p4', -0.3)} top={70} size={52}>Wie merkt de gevolgen?</Title>
      <div style={{ position: 'absolute', left: 170, top: 190, width: 600, height: 600, borderRadius: '50%', border: `5px solid ${C.green}`, background: '#E3F0E8', opacity: ring, transform: `scale(${0.85 + 0.15 * ring})` }} />
      <div style={{ position: 'absolute', left: 370, top: 300, width: 200, padding: '20px 0', borderRadius: 18, background: C.dark, color: C.amber, fontFamily: SANS, fontWeight: 700, fontSize: 30, textAlign: 'center', opacity: ring }}>AI-systeem</div>
      <div style={{ position: 'absolute', left: 300, top: 430, display: 'flex', gap: 60, opacity: ring }}><Figure size={90} color="#1F5A6B" badge /><Figure size={90} color="#1F5A6B" badge /></div>
      <div style={{ position: 'absolute', left: 320, top: 650, width: 300, textAlign: 'center', fontFamily: SANS, fontWeight: 700, fontSize: 30, color: C.green, opacity: ring }}>gebruikers</div>
      <Pop at={F('p4b', 0.2)} style={{ left: 860, top: 180 }}><div style={{ fontFamily: SANS, fontWeight: 700, fontSize: 30, color: C.terra }}>betrokkenen</div></Pop>
      {others.map(([t, x, y], i) => (
        <Pop key={t} at={F('p4b', 2.6 + i * 1.8)} style={{ left: x - 300, top: y, width: 900 }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: 20, background: C.card, border: `2px solid ${C.terra}`, borderRadius: 16, padding: '12px 22px' }}>
            <Figure size={56} color={C.terra} /><span style={{ fontFamily: SANS, fontSize: 28, color: C.ink }}>{t}</span>
          </div>
        </Pop>
      ))}
      <Banner at={F('p4c', 0.2)} top={760} left={850} width={940} size={36}>In K1: altijd <span style={{ color: C.amber }}>beide groepen</span></Banner>
    </AbsoluteFill>
  );
};

/* 7. Wat gaat erin, waar gaat het heen */
const Input = () => {
  const frame = useCurrentFrame();
  const docs = ['Instructies', 'Documenten', 'Vraag van de klant', 'Klantgegevens'];
  const cloud = useSpring(F('p5', 0.4));
  return (
    <AbsoluteFill style={{ background: C.light }}>
      <Title at={F('p5', -0.3)} top={70} size={52} kicker="BIJ GENERATIEVE AI">Wat gaat erin, en waar gaat het heen?</Title>
      {docs.map((t, i) => {
        const o = 1.2 + i * 1.4;
        const a = spring({ frame: frame - F('p5', o), fps: FPS, config: { damping: 16 } });
        const tr = (frame - F('p5', o + 0.6)) / (1.6 * FPS);
        const y = 250 + i * 110;
        const px = 560 + (((tr % 1) + 1) % 1) * 600, py = y + 30 + (((tr % 1) + 1) % 1) * (400 - y - 30);
        return (
          <React.Fragment key={t}>
            <div style={{ position: 'absolute', left: 128, top: y, opacity: a, transform: `translateX(${(1 - a) * -60}px)`, width: 420, background: i === 3 ? '#F6E7C8' : C.card, border: `2px solid ${i === 3 ? C.amber : C.line}`, borderRadius: 14, padding: '16px 22px', fontFamily: SANS, fontWeight: 700, fontSize: 30, color: C.ink }}>📄 {t}</div>
            {tr > 0 && <div style={{ position: 'absolute', left: px, top: py, width: 22, height: 22, borderRadius: 11, background: i === 3 ? C.amber : C.green, opacity: 0.85 }} />}
          </React.Fragment>
        );
      })}
      <div style={{ position: 'absolute', left: 1130, top: 250, width: 620, opacity: cloud, transform: `scale(${0.85 + 0.15 * cloud})` }}>
        <svg width="620" height="330" viewBox="0 0 600 330">
          <path d="M150 280 Q60 280 60 210 Q60 140 140 135 Q150 60 240 60 Q300 20 370 60 Q470 50 480 140 Q560 150 550 220 Q540 280 460 280 Z" fill={C.dark} />
          <text x="300" y="185" textAnchor="middle" fontFamily={SANS} fontWeight="700" fontSize="34" fill={C.amber}>externe dienst</text>
          <text x="300" y="228" textAnchor="middle" fontFamily={SANS} fontSize="26" fill="#C9D8D1">taalmodel van een leverancier</text>
        </svg>
      </div>
      <Banner at={F('p5b', 0.2)} top={700} left={980} width={810} size={38}>Dit bepaalt later <span style={{ color: C.amber }}>veel van je risico's</span>.</Banner>
    </AbsoluteFill>
  );
};

/* 9. Samengevat */
const Sum5 = () => {
  const frame = useCurrentFrame();
  const qs = ['Wat gaat erin?', 'Waar gaat het heen?', 'Wat doet iemand met het antwoord?'];
  return (
    <AbsoluteFill style={{ background: C.light }}>
      <Title at={F('p6', -0.3)} top={70} size={52}>Samengevat</Title>
      <Boxes at={F('p6', 0.3)} top={190} scale={0.92} />
      <Pop at={F('p6b', 0.2)} style={{ left: 128, top: 420, width: 1664 }}>
        <div style={{ display: 'flex', gap: 24 }}>
          <div style={{ flex: 1, background: '#E3F0E8', border: `3px solid ${C.green}`, borderRadius: 18, padding: '18px 26px', fontFamily: SANS, fontWeight: 700, fontSize: 32, color: C.green }}>gebruikers</div>
          <div style={{ flex: 1, background: '#F6E2DC', border: `3px solid ${C.terra}`, borderRadius: 18, padding: '18px 26px', fontFamily: SANS, fontWeight: 700, fontSize: 32, color: C.terra }}>én betrokkenen</div>
        </div>
      </Pop>
      <Pop at={F('p6c', 0.1)} style={{ left: 128, top: 560 }}><div style={{ fontFamily: SANS, fontWeight: 700, fontSize: 24, letterSpacing: 2, color: C.mute }}>BIJ GENERATIEVE AI</div></Pop>
      {qs.map((q, i) => (
        <Pop key={q} at={F('p6c', 0.8 + i * 1.3)} style={{ left: 128 + i * 560, top: 610, width: 530 }}>
          <div style={{ background: C.card, border: `2px solid ${C.line}`, borderRadius: 16, padding: '18px 24px', fontFamily: SANS, fontSize: 30, color: C.ink }}>{q}</div>
        </Pop>
      ))}
    </AbsoluteFill>
  );
};

export const Clip5 = () => (
  <Root scenes={[
    ['p0', <Intro5 />], ['p1', <Three />], ['p2', <Predict />], ['p3', <Generative />],
    ['q1', <QuizN n={1} q="q1" a="a1" question="Een medewerker laat een assistent een antwoord op een klachtbrief schrijven en stuurt dat ongewijzigd door. Wie heeft beslist wat de klant leest?" options={['A. De assistent', 'B. De medewerker en de organisatie']} good={1} note={<>B: <span style={{ color: C.amber }}>de medewerker en de organisatie</span></>} />],
    ['p4', <People />], ['p5', <Input />],
    ['q2', <QuizN n={2} q="q2" a="a2" question="Welke informatie hoort in K1 bij een chatbot?" options={['A. Alleen welke dienst wordt gebruikt', 'B. Ook welke gegevens naar die dienst gaan, wie het antwoord ziet en wat er daarna mee gebeurt']} good={1} />],
    ['p6', <Sum5 />],
  ]} />
);
