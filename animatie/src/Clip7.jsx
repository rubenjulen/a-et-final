/* Kennisclip 7 · Privacy als ethische vraag (blok 1) */
import React from 'react';
import { AbsoluteFill, useCurrentFrame, interpolate, spring } from 'remotion';
import timing from './timing_c7.json';
import { C, SERIF, SANS, FPS, clamp, makeKit, Person, Phone, Bubble } from './wk2_kit';

const K = makeKit(timing);
const { F, Pop, Card, Banner, Title, QuizN, Composition, TitleScene, Summary } = K;

/* D1: de A-DG-beginselen als iconen die naar de hoek schuiven */
const Rules = () => {
  const frame = useCurrentFrame();
  const mv = interpolate(frame, [F('d1b', 0), F('d1b', 1.2)], [0, 1], clamp);
  const icons = [['👤', 'persoonsgegevens'], ['🔒', 'gevoelige gegevens'], ['🎯', 'doelbinding'], ['✂️', 'dataminimalisatie'], ['⏳', 'bewaartermijn'], ['🛡️', 'rechten']];
  return (
    <AbsoluteFill style={{ background: C.light }}>
      <Pop at={F('d1a', 0)} style={{ left: 128, top: 96 }}><div style={{ fontFamily: SANS, fontWeight: 700, fontSize: 24, letterSpacing: 2, color: C.terra }}>WAT JE UIT A-DG AL KENT</div></Pop>
      {icons.map(([ic, t], i) => {
        const x0 = 160 + (i % 3) * 540, y0 = 220 + Math.floor(i / 3) * 210;
        const x1 = 1060 + (i % 3) * 250, y1 = 60 + Math.floor(i / 3) * 70;
        const o = interpolate(frame, [F('d1a', 0.5 + i * 0.5), F('d1a', 0.9 + i * 0.5)], [0, 1], clamp);
        return (
          <div key={t} style={{ position: 'absolute', left: x0 + (x1 - x0) * mv, top: y0 + (y1 - y0) * mv, opacity: o, transform: `scale(${1 - 0.5 * mv})`, transformOrigin: 'top left' }}>
            <div style={{ display: 'flex', alignItems: 'center', gap: 16, background: C.card, border: `2px solid ${C.line}`, borderRadius: 20, padding: '20px 28px', width: 460 }}>
              <span style={{ fontSize: 46 }}>{ic}</span><span style={{ fontFamily: SANS, fontWeight: 700, fontSize: 30, color: C.ink }}>{t}</span>
            </div>
          </div>
        );
      })}
      <Pop at={F('d1c', 0)} style={{ left: 128, top: 430, width: 1500 }}>
        <div style={{ fontFamily: SANS, fontSize: 28, color: C.mute }}>In AI &amp; Ethics gaat het om de vraag erachter:</div>
        <div style={{ fontFamily: SERIF, fontWeight: 700, fontSize: 70, color: C.ink, lineHeight: 1.08, marginTop: 10 }}>Wat doet het met mensen?<br /><span style={{ color: C.green }}>En is het verantwoord?</span></div>
      </Pop>
    </AbsoluteFill>
  );
};

/* D2: inferentie en herleidbaarheid */
const Inference = () => {
  const frame = useCurrentFrame();
  const items = ['foliumzuur', 'zwangerschapsvitamines', 'babykleertjes (cadeau?)'];
  const arrow = interpolate(frame, [F('d2a', 4), F('d2a', 5)], [0, 1], clamp);
  const crowd = Array.from({ length: 24 });
  const pick = interpolate(frame, [F('d2c', 1), F('d2c', 2.5)], [0, 1], clamp);
  return (
    <AbsoluteFill style={{ background: C.light }}>
      <Title at={F('d2a', 0)} kicker="Wat AI anders maakt">AI leidt af wat niemand heeft opgegeven</Title>
      <Pop at={F('d2a', 1)} style={{ left: 128, top: 300, width: 520 }}>
        <Card>
          <div style={{ fontFamily: SANS, fontWeight: 700, fontSize: 24, color: C.mute }}>Aankopen</div>
          {items.map((t, i) => <div key={t} style={{ fontFamily: SANS, fontSize: 30, color: C.ink, marginTop: 10, opacity: interpolate(frame, [F('d2a', 1.5 + i * 0.6), F('d2a', 1.8 + i * 0.6)], [0, 1], clamp) }}>🛒 {t}</div>)}
        </Card>
      </Pop>
      <svg style={{ position: 'absolute', left: 670, top: 400 }} width="220" height="60"><line x1="10" y1="30" x2={10 + 180 * arrow} y2="30" stroke={C.terra} strokeWidth="8" strokeLinecap="round" />{arrow > 0.95 && <path d="M180 10 L210 30 L180 50" fill="none" stroke={C.terra} strokeWidth="8" strokeLinecap="round" />}</svg>
      <Pop at={F('d2a', 5)} style={{ left: 910, top: 340, width: 420 }}>
        <Card style={{ background: '#F7E7E2', borderColor: C.terra }}>
          <div style={{ fontFamily: SANS, fontSize: 24, color: C.terra, fontWeight: 700 }}>Het model concludeert</div>
          <div style={{ fontFamily: SERIF, fontWeight: 700, fontSize: 44, color: C.ink, marginTop: 6 }}>"waarschijnlijk zwanger"</div>
        </Card>
      </Pop>
      <Pop at={F('d2b', 0)} style={{ left: 1400, top: 360 }}><div style={{ fontFamily: SERIF, fontWeight: 700, fontSize: 58, color: C.green }}>= inferentie</div></Pop>
      <Pop at={F('d2c', 0)} style={{ left: 128, top: 620, width: 1664 }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: 30 }}>
          <div style={{ display: 'flex', gap: 10 }}>
            {['34 jaar', 'Coronie', 'vroedvrouw'].map((t) => <span key={t} style={{ fontFamily: SANS, fontWeight: 700, fontSize: 26, padding: '10px 18px', borderRadius: 12, background: C.sand }}>{t}</span>)}
          </div>
          <div style={{ fontFamily: SERIF, fontSize: 50, color: C.mute }}>→</div>
          <div style={{ display: 'flex', flexWrap: 'wrap', width: 820, gap: 4 }}>
            {crowd.map((_, i) => <div key={i} style={{ opacity: i === 17 ? 1 : 1 - 0.75 * pick }}><Person size={56} frame={frame} color={i === 17 ? C.terra : C.green} glow={i === 17 && pick > 0.6} /></div>)}
          </div>
        </div>
      </Pop>
    </AbsoluteFill>
  );
};

/* D3: chatbot en een server ver weg */
const ChatOut = () => {
  const frame = useCurrentFrame();
  const fly = interpolate(frame, [F('d3b', 0.5), F('d3b', 3)], [0, 1], clamp);
  const qs = ['Waar gaat het naartoe?', 'Wie kan het lezen?', 'Wordt ermee getraind?', 'Weet de klant dit?'];
  return (
    <AbsoluteFill style={{ background: C.light }}>
      <Title at={F('d3a', 0)} kicker="Bij generatieve AI">Wat je in een chatbot typt, gaat vaak naar buiten</Title>
      <Phone title="Klantenservice-assistent" sub="medewerker plakt een brief" h={600} style={{ left: 160, top: 270, transform: 'scale(0.82)', transformOrigin: 'top left' }}>
        <Bubble who="me" at={F('d3a', 1)} frame={frame}>Schrijf een antwoord op deze brief: "Geachte heer, mijn naam is R. Kartodikromo, rekening 4417…, ik ben ziek en kan de termijn niet betalen…"</Bubble>
        <Bubble who="bot" at={F('d3a', 3)} frame={frame}>Hier is een conceptantwoord…</Bubble>
      </Phone>
      <svg style={{ position: 'absolute', left: 640, top: 330 }} width="760" height="200">
        <path d="M10 150 C 250 -20, 500 -20, 740 110" stroke={C.terra} strokeWidth="5" strokeDasharray="14 12" fill="none" opacity={fly} />
        <circle cx={10 + 730 * fly} cy={150 - Math.sin(Math.PI * fly) * 120 - 40 * fly} r="14" fill={C.terra} />
      </svg>
      <Pop at={F('d3b', 2.4)} style={{ left: 1420, top: 330, width: 340 }}>
        <Card style={{ textAlign: 'center' }}>
          <div style={{ fontSize: 70 }}>🖥️</div>
          <div style={{ fontFamily: SANS, fontWeight: 700, fontSize: 26, color: C.ink }}>externe dienst</div>
          <div style={{ fontFamily: SANS, fontSize: 22, color: C.mute }}>ergens anders, buiten de organisatie</div>
        </Card>
      </Pop>
      <div style={{ position: 'absolute', left: 820, top: 560, display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 14, width: 960 }}>
        {qs.map((q, i) => {
          const key = i < 3 ? 'd3c' : 'd3d';
          const off = i < 3 ? 1 + i * 2.2 : 0.3;
          return <Pop key={q} at={F(key, off)} style={{ position: 'relative' }}><div style={{ fontFamily: SANS, fontWeight: 700, fontSize: 28, padding: '16px 22px', borderRadius: 16, background: C.dark, color: C.amber }}>? {q}</div></Pop>;
        })}
      </div>
    </AbsoluteFill>
  );
};

/* D4: Grondwet en ontwerpwet */
const Suriname = () => {
  const frame = useCurrentFrame();
  const regel = ['onafhankelijke toezichthouder', 'regels voor gegevens naar het buitenland', 'soms een functionaris gegevensbescherming'];
  return (
    <AbsoluteFill style={{ background: C.light }}>
      <Title at={F('d4a', 0)} kicker="De situatie in Suriname">Grondwet wel, privacywet nog niet</Title>
      <Pop at={F('d4a', 1)} style={{ left: 128, top: 300, width: 760 }}>
        <Card style={{ borderLeft: `10px solid ${C.green}` }}>
          <div style={{ fontFamily: SANS, fontWeight: 700, fontSize: 24, color: C.mute, letterSpacing: 1 }}>GRONDWET</div>
          <div style={{ fontFamily: SERIF, fontWeight: 600, fontSize: 40, color: C.ink, marginTop: 8 }}>beschermt de persoonlijke levenssfeer</div>
          <div style={{ fontFamily: SANS, fontWeight: 700, fontSize: 28, color: C.green, marginTop: 14 }}>✓ geldt nu</div>
        </Card>
      </Pop>
      <Pop at={F('d4b', 0)} style={{ left: 960, top: 300, width: 830 }}>
        <Card style={{ borderLeft: `10px solid ${C.amber}` }}>
          <div style={{ fontFamily: SANS, fontWeight: 700, fontSize: 24, color: C.mute, letterSpacing: 1 }}>ONTWERPWET BESCHERMING PRIVACY EN PERSOONSGEGEVENS</div>
          <div style={{ fontFamily: SERIF, fontWeight: 600, fontSize: 36, color: C.ink, marginTop: 8 }}>ligt bij De Nationale Assemblée</div>
          <div style={{ fontFamily: SANS, fontWeight: 700, fontSize: 28, color: C.amber, marginTop: 10 }}>⏳ nog niet in werking</div>
          {regel.map((r, i) => <div key={r} style={{ fontFamily: SANS, fontSize: 28, color: C.ink, marginTop: 12, opacity: interpolate(frame, [F('d4c', 2 + i * 2.5), F('d4c', 2.4 + i * 2.5)], [0, 1], clamp) }}>• {r}</div>)}
        </Card>
      </Pop>
    </AbsoluteFill>
  );
};

/* D5: Paramaribo -> server in Europa */
const Border = () => {
  const frame = useCurrentFrame();
  const fly = interpolate(frame, [F('d5b', 0), F('d5b', 3)], [0, 1], clamp);
  return (
    <AbsoluteFill style={{ background: C.light }}>
      <Title at={F('d5a', 0)} kicker="Gegevens over de grens">Veel AI draait bij buitenlandse leveranciers</Title>
      <svg style={{ position: 'absolute', left: 128, top: 270 }} width="1664" height="420" viewBox="0 0 1664 420">
        <rect x="0" y="0" width="1664" height="420" rx="24" fill="#E7EFE9" />
        <circle cx="300" cy="300" r="16" fill={C.green} />
        <text x="300" y="350" textAnchor="middle" fontFamily={SANS} fontWeight="700" fontSize="30" fill={C.ink}>Paramaribo</text>
        <text x="300" y="384" textAnchor="middle" fontFamily={SANS} fontSize="24" fill={C.mute}>Suribank · klantdata</text>
        <path d={`M300 300 Q 830 -40 1360 150`} stroke={C.terra} strokeWidth="6" strokeDasharray="16 12" fill="none" opacity={fly} />
        <circle cx={300 + 1060 * fly} cy={300 - Math.sin(Math.PI * fly) * 230 - 150 * fly} r="16" fill={C.terra} />
        <rect x="1290" y="110" width="140" height="90" rx="12" fill={C.dark} opacity={interpolate(frame, [F('d5b', 2.5), F('d5b', 3)], [0, 1], clamp)} />
        <text x="1360" y="240" textAnchor="middle" fontFamily={SANS} fontWeight="700" fontSize="30" fill={C.ink}>Leverancier in Europa</text>
        <text x="1360" y="274" textAnchor="middle" fontFamily={SANS} fontSize="24" fill={C.mute}>Europese privacyregels</text>
      </svg>
      <Pop at={F('d5c', 0)} style={{ left: 128, top: 720, width: 760 }}>
        <div style={{ fontFamily: SANS, fontSize: 28, color: C.ink }}>Ook een chatbot met een buitenlands taalmodel stuurt gegevens weg.</div>
      </Pop>
      <Pop at={F('d5d', 0.2)} style={{ left: 960, top: 715, width: 830 }}>
        <div style={{ fontFamily: SANS, fontSize: 26, color: C.mute, marginBottom: 10 }}>Welke afspraken zijn er gemaakt over…</div>
      </Pop>
      <div style={{ position: 'absolute', left: 960, top: 765, display: 'flex', gap: 14 }}>
        {['beveiliging?', 'bewaartermijn?', 'hergebruik?'].map((t, i) => <Pop key={t} at={F('d5d', 0.8 + i * 0.6)} style={{ position: 'relative' }}><div style={{ fontFamily: SANS, fontWeight: 700, fontSize: 28, padding: '14px 22px', borderRadius: 14, background: C.dark, color: C.amber }}>{t}</div></Pop>)}
      </div>
    </AbsoluteFill>
  );
};

/* D6: twee overlappende cirkels */
const Circles = () => {
  const frame = useCurrentFrame();
  const sl = interpolate(frame, [F('d6a', 0.5), F('d6a', 2.5)], [0, 1], clamp);
  return (
    <AbsoluteFill style={{ background: C.light }}>
      <Title at={F('d6a', 0)} kicker="Wettelijk is niet hetzelfde als verantwoord">Waar de wet zwijgt, blijft de ethische vraag</Title>
      <svg style={{ position: 'absolute', left: 360, top: 260 }} width="1200" height="460">
        <circle cx={600 - 180 * sl} cy="230" r="210" fill={C.green} opacity="0.22" stroke={C.green} strokeWidth="4" />
        <circle cx={600 + 180 * sl} cy="230" r="210" fill={C.amber} opacity="0.28" stroke={C.amber} strokeWidth="4" />
        <text x={600 - 260 * sl} y="236" textAnchor="middle" fontFamily={SERIF} fontWeight="700" fontSize="44" fill={C.ink} opacity={sl}>wettelijk</text>
        <text x={600 + 260 * sl} y="236" textAnchor="middle" fontFamily={SERIF} fontWeight="700" fontSize="44" fill={C.ink} opacity={sl}>verantwoord</text>
      </svg>
      <Banner at={F('d6b', 1)} top={740} size={38}>Zou je klanten recht in de ogen kunnen kijken als zij wisten <span style={{ color: C.amber }}>wat er met hun gegevens gebeurt?</span></Banner>
    </AbsoluteFill>
  );
};

export const Clip7 = () => {
  const scenes = [
    ['t0', <TitleScene n={7} title="Privacy als ethische vraag" sub="Niet de regels, maar wat het met mensen doet" />],
    ['d1a', <Rules />],
    ['d2a', <Inference />],
    ['q1', <QuizN n={1} q="q1" a="a1" question="Een dataset bevat geen namen, wel leeftijd, district en beroep. Is dat anoniem?" options={['A. Ja.', 'B. Niet per se; de combinatie kan naar een persoon te herleiden zijn.']} good={1} note={<>Samen kunnen leeftijd, district en beroep naar <span style={{ color: C.amber }}>één persoon</span> wijzen.</>} />],
    ['d3a', <ChatOut />],
    ['d4a', <Suriname />],
    ['d5a', <Border />],
    ['q2', <QuizN n={2} q="q2" a="a2" question="Een medewerker plakt een klantbrief in een gratis online chatbot om snel een antwoord te laten schrijven. Wat is het grootste ethische probleem?" options={['A. Het antwoord kan te lang zijn.', 'B. De gegevens van de klant gaan, zonder dat die het weet, naar een externe dienst.']} good={1} note={<>De klant weet niet dat zijn gegevens <span style={{ color: C.amber }}>naar buiten</span> gaan.</>} />],
    ['d6a', <Circles />],
    ['d7a', <Summary k="d7a" cols={3} title="Privacy is meer dan regels volgen" items={['AI leidt af wat niemand opgaf', 'Gegevens gaan vaak naar buiten', 'Regels in A-DG, de afweging hier']} bannerKey="d7c" banner={<>Vraag steeds: is het verantwoord voor <span style={{ color: C.amber }}>de mensen om wie het gaat?</span></>} />],
  ];
  return <Composition scenes={scenes} />;
};
