// Kennisclip 8b · Doel gehaald, bedoeling gemist (blok 1). Script: clip8b/build.py; timing: src/timing_c8b.json.
import React from 'react';
import { AbsoluteFill, useCurrentFrame, interpolate, Easing } from 'remotion';
import timing from './timing_c8b.json';
import { clamp, fade, Pop } from './wk1_kit';
import { J, FONT, JTitle, JBanner, makeJKit } from './janssen_kit';
import { sp, makeW, T, Kick, Panel, Person, Switch, Bub, PhoneFrame } from './janssen_parts';

const { cue, F, QuizN, Root } = makeJKit(timing);
const W = makeW(cue, F);
const at = (k, o = -0.2) => F(k, o);

const Intro = () => {
  const frame = useCurrentFrame(); const s = sp(frame, 4);
  const g = interpolate(frame, [20, 70], [0, 1], clamp);
  return (
    <AbsoluteFill style={{ background: `radial-gradient(1300px 900px at 78% 25%, #1A3D86 0%, ${J.navy} 62%)` }}>
      <div style={{ position: 'absolute', left: 140, top: 250, opacity: s }}><Kick color={J.gold} style={{ fontSize: 30 }}>Kennisclip 8b · AI &amp; Ethics · blok 1</Kick></div>
      <div style={{ position: 'absolute', left: 140, top: 300, fontFamily: FONT, fontWeight: 700, fontSize: 130, lineHeight: 1.02, color: '#fff', opacity: s, transform: `translateY(${(1 - s) * 40}px)` }}>Doel gehaald,<br />bedoeling gemist</div>
      <svg width="700" height="300" style={{ position: 'absolute', left: 1120, top: 320, opacity: fade(frame, 18, 30) }}>
        <path d={`M20 260 L${20 + 640 * g} ${260 - 230 * g}`} stroke={J.gold} strokeWidth="10" strokeLinecap="round" />
        <path d={`M20 260 L${20 + 640 * g} ${260 - 40 * g}`} stroke="#8FB3DE" strokeWidth="10" strokeLinecap="round" strokeDasharray="18 14" />
        <text x="20" y="40" fontFamily={FONT} fontWeight="700" fontSize="32" fill={J.gold} opacity={g}>— het getal</text>
        <text x="20" y="84" fontFamily={FONT} fontWeight="700" fontSize="32" fill="#8FB3DE" opacity={g}>- - het doel</text>
      </svg>
    </AbsoluteFill>
  );
};

const Dashboard = ({ k0, k1 }) => {
  const frame = useCurrentFrame();
  const v = Math.round(interpolate(frame, [F(k0, 2), F(k1, 3)], [12, 31], clamp));
  return (
    <div style={{ background: J.card, border: `2px solid ${J.line}`, borderRadius: 22, padding: '26px 32px', boxShadow: '0 12px 30px rgba(0,32,96,.07)' }}>
      <Kick color={J.slate}>Dashboard · klantenservice</Kick>
      <T size={34} weight={700} color={J.navy} style={{ marginTop: 8 }}>Afgehandelde gesprekken per uur</T>
      <div style={{ display: 'flex', alignItems: 'baseline', gap: 18, marginTop: 10 }}><div style={{ fontFamily: FONT, fontWeight: 700, fontSize: 130, color: J.blue, lineHeight: 1 }}>{v}</div><T size={44} weight={700} color={J.green}>▲</T></div>
    </div>
  );
};
const Bank = () => {
  const frame = useCurrentFrame();
  const verdict = sp(frame, W('V2', 'Het getal is gehaald'));
  return (
    <AbsoluteFill style={{ background: J.bg }}>
      <JTitle at={at('V1')} kicker="Denkvoorbeeld · een bankchatbot">Wat meet je eigenlijk?</JTitle>
      <PhoneFrame title="Bank · chat" sub="assistent" left={128} top={240} h={600}>
        <Bub at={F('V1', 0.6)} me size={24}>Ik heb een vraag over mijn lening en mijn salaris dat later komt.</Bub>
        <Bub at={W('V2', 'sluit', 0)} size={24}>Daarvoor verwijs ik u door naar het kantoor.</Bub>
        <Bub at={W('V2', 'verwijst', 0.6)} size={24} bg="#FBE9E7">Dit gesprek is beëindigd.</Bub>
      </PhoneFrame>
      <div style={{ position: 'absolute', left: 660, top: 250, width: 640 }}><Dashboard k0="V1" k1="V2" /></div>
      <svg viewBox="0 0 200 260" style={{ position: 'absolute', left: 1400, top: 260, width: 200, height: 260 }}><Person x={100} y={190} s={2.4} col={J.slate} />
        <text x="100" y="60" textAnchor="middle" fontFamily={FONT} fontWeight="700" fontSize="70" fill={J.red} opacity={sp(frame, W('V2', 'De klant'))}>?</text></svg>
      <div style={{ position: 'absolute', left: 660, top: 600, width: 1130, display: 'flex', gap: 20, opacity: verdict, transform: `translateY(${(1 - verdict) * 30}px)` }}>
        <div style={{ flex: 1, background: '#E2F1E8', border: `3px solid ${J.green}`, borderRadius: 16, padding: '18px 24px' }}><T size={36} weight={700} color={J.green}>Getal gehaald ✓</T></div>
        <div style={{ flex: 1, background: '#FBE9E7', border: `3px solid ${J.red}`, borderRadius: 16, padding: '18px 24px', opacity: sp(frame, W('V2', 'De klant')) }}><T size={36} weight={700} color={J.red}>Klant geholpen ✗</T></div>
      </div>
    </AbsoluteFill>
  );
};

const Alignment = () => {
  const frame = useCurrentFrame(); const q = sp(frame, F('V4', 0.2));
  return (
    <AbsoluteFill style={{ background: J.bg }}>
      <JTitle at={at('V3')} kicker="Waar hebben we het over?">Het alignment-probleem</JTitle>
      <Pop at={F('V3', 1)} style={{ left: 128, top: 260, width: 1664 }}>
        <div style={{ background: J.card, border: `2px solid ${J.line}`, borderLeft: `10px solid ${J.blue}`, borderRadius: 18, padding: '28px 36px' }}>
          <Kick>Alignment</Kick><T size={44} weight={700} color={J.navy} style={{ marginTop: 8 }}>Het doel en het gedrag van een systeem sluiten aan bij wat mensen werkelijk bedoelen.</T>
        </div>
      </Pop>
      <div style={{ position: 'absolute', left: 128, top: 520, width: 1664, opacity: q, transform: `translateY(${(1 - q) * 30}px)`, background: J.navy, borderRadius: 18, padding: '30px 40px' }}>
        <Kick color={J.gold}>Norbert Wiener · Science · 1960</Kick>
        <T size={40} weight={700} color="#fff" style={{ marginTop: 10 }}>“We had better be quite sure that the purpose put into the machine is the purpose which we really desire.”</T>
        <T size={28} color={J.onNavyMuted} style={{ marginTop: 10 }}>Weet zeker dat het doel in de machine het doel is dat je echt wilt.</T>
      </div>
    </AbsoluteFill>
  );
};

const Hard = () => {
  const frame = useCurrentFrame();
  const col = (t, items, c, at0) => (<div style={{ flex: 1, background: J.card, border: `2px solid ${J.line}`, borderTop: `10px solid ${c}`, borderRadius: 18, padding: '22px 28px' }}>
    <T size={34} weight={700} color={J.navy}>{t}</T>{items.map((x, i) => <T key={x} size={30} color={J.ink} style={{ marginTop: 8, opacity: sp(frame, at0 + i * 12) }}>• {x}</T>)}</div>);
  const pairs = [['klikken', 'tevredenheid'], ['afgehandelde gesprekken', 'geholpen klanten']];
  const g = interpolate(frame, [W('V7', 'Hoe beter'), W('V7', 'Hoe beter') + 90], [0, 1], clamp);
  return (
    <AbsoluteFill style={{ background: J.bg }}>
      <JTitle at={at('V5')} kicker="Waarom is het zo moeilijk?">Waarden zijn vaag, systemen willen een getal</JTitle>
      <Switch style={{ left: 128, top: 240, width: 1664, height: 600 }} items={[
        [at('V5'), <div style={{ display: 'flex', gap: 28 }}>{col('Wat mensen willen', ['vaag', 'afhankelijk van de context', 'soms botsend'], J.gold, W('V5', 'vaag'))}{col('Wat AI nodig heeft', ['een expliciet doel', 'een precies getal'], J.blue, W('V5', 'Een AI-systeem'))}</div>],
        [at('V6'), <div><Kick>Proxy</Kick><T size={40} weight={700} color={J.navy} style={{ marginTop: 6 }}>We meten iets anders dan wat we willen</T>
          {pairs.map(([a, b], i) => { const s = sp(frame, W('V6', i ? 'Afgehandelde' : 'Klikken')); return (
            <div key={a} style={{ display: 'flex', gap: 24, alignItems: 'center', marginTop: 26, opacity: s, transform: `translateX(${(1 - s) * 40}px)` }}>
              <div style={{ background: J.blue, color: '#fff', borderRadius: 14, padding: '16px 26px', fontFamily: FONT, fontWeight: 700, fontSize: 36 }}>{a}</div><T size={34} color={J.slate}>in plaats van</T>
              <div style={{ background: J.ice, border: `3px dashed ${J.gold}`, borderRadius: 14, padding: '14px 26px', fontFamily: FONT, fontWeight: 700, fontSize: 36, color: J.navy }}>{b}</div></div>); })}</div>],
        [at('V7'), <div style={{ display: 'flex', gap: 30, alignItems: 'center' }}>
          <div style={{ flex: 1, background: J.navy, borderRadius: 18, padding: '30px 36px' }}><Kick color={J.gold}>Wet van Goodhart</Kick><T size={40} weight={700} color="#fff" style={{ marginTop: 10 }}>Als een maat een doel wordt, is het geen goede maat meer.</T></div>
          <svg width="760" height="420"><line x1="40" y1="380" x2="740" y2="380" stroke={J.line} strokeWidth="4" /><line x1="40" y1="380" x2="40" y2="20" stroke={J.line} strokeWidth="4" />
            <path d={`M40 360 L${40 + 680 * g} ${360 - 320 * g}`} stroke={J.blue} strokeWidth="10" strokeLinecap="round" />
            <path d={`M40 360 Q ${40 + 300 * g} ${360 - 120 * g} ${40 + 680 * g} ${360 - 60 * g}`} stroke={J.gold} strokeWidth="10" fill="none" strokeLinecap="round" strokeDasharray="20 14" />
            <text x="70" y="40" fontFamily={FONT} fontWeight="700" fontSize="30" fill={J.blue} opacity={g}>— het getal</text>
            <text x="70" y="80" fontFamily={FONT} fontWeight="700" fontSize="30" fill="#9C7A28" opacity={g}>- - het echte doel</text>
            <text x="390" y="410" textAnchor="middle" fontFamily={FONT} fontSize="24" fill={J.slate}>hoe beter het systeem optimaliseert →</text></svg></div>],
      ]} />
    </AbsoluteFill>
  );
};

const Coast = () => {
  const frame = useCurrentFrame();
  const t = Math.max(0, frame - F('V9', 1)) / 24;
  const bx = 600 + 180 * Math.cos(t), by = 330 + 110 * Math.sin(t);
  const score = Math.round(interpolate(frame, [F('V9', 2), F('V9', 14)], [0, 2400], clamp));
  const fire = frame > W('V9', 'vloog') ? 1 : 0;
  return (
    <AbsoluteFill style={{ background: J.bg }}>
      <JTitle at={at('V8')} kicker="Specification gaming">Het doel halen via een maas in de opdracht</JTitle>
      <svg width="1664" height="600" style={{ position: 'absolute', left: 128, top: 240 }}>
        <rect x="0" y="0" width="1100" height="600" rx="24" fill="#CFE2F5" />
        <ellipse cx="600" cy="330" rx="230" ry="150" fill="#B6D2EE" stroke="#fff" strokeWidth="6" strokeDasharray="14 12" />
        {[[420, 250], [780, 260], [600, 470], [600, 190]].map(([x, y], i) => <g key={i}><circle cx={x} cy={y} r="22" fill={J.gold} stroke="#fff" strokeWidth="4" /><text x={x} y={y + 9} textAnchor="middle" fontFamily={FONT} fontWeight="700" fontSize="24" fill={J.navy}>+</text></g>)}
        <g transform={`translate(${bx},${by}) rotate(${(t * 180 / Math.PI + 90) % 360})`}><path d="M-16 -34 L16 -34 L22 26 L0 40 L-22 26 Z" fill={J.navy} />
          {fire ? <g>{[0, 1, 2].map((i) => <circle key={i} cx={-10 + i * 10} cy={30 + 8 * Math.sin(frame / 3 + i)} r={10 + 3 * Math.sin(frame / 2 + i)} fill={i === 1 ? J.red : J.gold} opacity="0.85" />)}</g> : null}</g>
        <g transform="translate(1000,80)"><line x1="0" y1="0" x2="0" y2="120" stroke={J.navy} strokeWidth="6" />{[0, 1, 2, 3].map((r) => [0, 1, 2].map((c) => <rect key={`${r}${c}`} x={c * 18} y={r * 18} width="18" height="18" fill={(r + c) % 2 ? '#fff' : J.navy} />))}
          <text x="-10" y="160" textAnchor="middle" fontFamily={FONT} fontWeight="700" fontSize="26" fill={J.navy}>finish</text><text x="-10" y="190" textAnchor="middle" fontFamily={FONT} fontSize="24" fill={J.red}>nooit bereikt</text></g>
        <g transform="translate(1160,40)"><rect width="500" height="200" rx="20" fill={J.navy} /><text x="30" y="58" fontFamily={FONT} fontWeight="700" fontSize="24" fill={J.gold}>SCORE</text>
          <text x="30" y="150" fontFamily={FONT} fontWeight="700" fontSize="90" fill="#fff">{score}</text></g>
        <g transform="translate(1160,270)" opacity={sp(frame, W('V9', 'Toch scoorde'))}><rect width="500" height="130" rx="20" fill={J.card} stroke={J.line} strokeWidth="2" /><text x="30" y="58" fontFamily={FONT} fontWeight="700" fontSize="30" fill={J.navy}>Hoger dan mensen,</text><text x="30" y="100" fontFamily={FONT} fontWeight="700" fontSize="30" fill={J.red}>zonder de race te varen</text></g>
        <text x="1160" y="470" fontFamily={FONT} fontSize="26" fill={J.slate}>CoastRunners · OpenAI, 2016</text>
      </svg>
    </AbsoluteFill>
  );
};

const Hack = () => {
  const frame = useCurrentFrame();
  const posts = [['Koop nu goedkope pillen!!!', true], ['Fijne verjaardag, tante!', false], ['Bel dit nummer voor gratis geld', true], ['Foto’s van ons dorp in Brokopondo', false], ['Wie gaat mee naar de markt?', false]];
  const removed = Math.round(interpolate(frame, [F('V10', 3), F('V10', 12)], [120, 410], clamp));
  return (
    <AbsoluteFill style={{ background: J.bg }}>
      <JTitle at={at('V10')} kicker="Reward hacking">Beloning gehaald, bedoeling niet</JTitle>
      <Switch style={{ left: 128, top: 240, width: 1664, height: 600 }} items={[
        [at('V10'), <div style={{ display: 'flex', gap: 30 }}>
          <div style={{ flex: 1.3 }}>{posts.map(([p, bad], i) => { const x = sp(frame, F('V10', 4 + i * 1.2)); return (
            <div key={p} style={{ display: 'flex', alignItems: 'center', gap: 16, background: J.card, border: `2px solid ${J.line}`, borderRadius: 14, padding: '14px 22px', marginBottom: 12 }}>
              <T size={30} color={x > 0.5 ? J.slate : J.ink} style={{ flex: 1, textDecoration: x > 0.5 ? 'line-through' : 'none' }}>{p}</T>
              <div style={{ opacity: x, fontFamily: FONT, fontWeight: 700, fontSize: 26, color: '#fff', background: J.red, borderRadius: 999, padding: '4px 16px' }}>verwijderd</div>
              {!bad && <div style={{ opacity: x, fontFamily: FONT, fontWeight: 700, fontSize: 24, color: J.red }}>onschuldig!</div>}</div>); })}</div>
          <div style={{ flex: 0.8, background: J.navy, borderRadius: 18, padding: '28px 32px' }}><Kick color={J.gold}>Beloning</Kick><T size={30} color={J.onNavyMuted} style={{ marginTop: 6 }}>verwijderde berichten vandaag</T>
            <div style={{ fontFamily: FONT, fontWeight: 700, fontSize: 120, color: '#fff' }}>{removed}</div><T size={30} weight={700} color={J.gold}>Meer = beter?</T></div></div>],
        [at('V11'), <div style={{ display: 'flex', gap: 30, alignItems: 'center' }}>
          <div style={{ flex: 1, background: J.card, border: `2px solid ${J.line}`, borderRadius: 18, padding: '26px 32px' }}><Kick color={J.slate}>Testrapport</Kick>
            {['test_betaling', 'test_saldo', 'test_overschrijving', 'test_rente'].map((t, i) => <div key={t} style={{ display: 'flex', justifyContent: 'space-between', marginTop: 12, opacity: sp(frame, F('V11', 0.5 + i * 0.4)) }}><T size={30} color={J.ink}>{t}</T><T size={30} weight={700} color={J.green}>geslaagd ✓</T></div>)}</div>
          <div style={{ flex: 1, opacity: sp(frame, W('V11', 'zonder')), background: '#FBE9E7', border: `3px solid ${J.red}`, borderRadius: 18, padding: '26px 32px' }}><T size={40} weight={700} color={J.red}>Maar de code werkt niet</T><T size={28} color={J.ink} style={{ marginTop: 10 }}>Redeneermodellen lieten soms de tests slagen zonder het probleem op te lossen (OpenAI, 2025).</T></div></div>],
      ]} />
    </AbsoluteFill>
  );
};

const Sense = () => {
  const frame = useCurrentFrame();
  return (
    <AbsoluteFill style={{ background: J.bg }}>
      <JTitle at={at('V12')} kicker="Waarom zien wij het niet aankomen?">Wij vullen gezond verstand in. Het systeem niet.</JTitle>
      <svg width="1664" height="560" style={{ position: 'absolute', left: 128, top: 250 }}>
        <Person x={300} y={470} s={3.4} col={J.dblue} />
        <g opacity={sp(frame, F('V12', 1.5))}><ellipse cx="380" cy="150" rx="280" ry="120" fill={J.card} stroke={J.line} strokeWidth="3" />
          {['gezond verstand', 'normen', 'context', 'wat “natuurlijk” niet mag'].map((t, i) => <text key={t} x="380" y={105 + i * 34} textAnchor="middle" fontFamily={FONT} fontWeight="700" fontSize="28" fill={J.navy}>{t}</text>)}</g>
        <g transform="translate(1250,380)"><rect x="-120" y="-60" width="240" height="160" rx="20" fill={J.navy} /><circle cx="-40" cy="10" r="14" fill={J.blue} /><circle cx="40" cy="10" r="14" fill={J.blue} /></g>
        <g opacity={sp(frame, W('V12', 'Het kent'))}><ellipse cx="1250" cy="150" rx="200" ry="90" fill={J.card} stroke={J.line} strokeWidth="3" /><text x="1250" y="165" textAnchor="middle" fontFamily={FONT} fontWeight="700" fontSize="56" fill={J.blue}>het getal</text></g>
      </svg>
    </AbsoluteFill>
  );
};

const Suribank = () => {
  const frame = useCurrentFrame();
  const p = interpolate(frame, [F('V13', 4), F('V13', 14)], [0, 1], clamp);
  const bar = (lab, v, c, y) => (<g><text x="0" y={y + 40} fontFamily={FONT} fontWeight="700" fontSize="30" fill={J.navy}>{lab}</text><rect x="420" y={y} width={v * 10} height="56" rx="10" fill={c} /><text x={430 + v * 10} y={y + 40} fontFamily={FONT} fontWeight="700" fontSize="30" fill={c}>{Math.round(v)}%</text></g>);
  return (
    <AbsoluteFill style={{ background: J.bg }}>
      <JTitle at={at('V13')} kicker="Denkvoorbeeld · Suribank">Beloond voor terugbetaling</JTitle>
      <svg width="1664" height="420" style={{ position: 'absolute', left: 128, top: 280 }}>
        {bar('Terugbetaald', 78 + 18 * p, J.blue, 20)}{bar('Goedgekeurd, kust', 62 - 10 * p, J.dblue, 140)}{bar('Goedgekeurd, binnenland', 41 - 33 * p, J.red, 260)}
      </svg>
      <JBanner at={W('V13', 'Het binnenland')} top={740} size={40}>Het getal stijgt. Het binnenland valt weg.</JBanner>
    </AbsoluteFill>
  );
};

const Prefs = () => {
  const frame = useCurrentFrame();
  const pick = sp(frame, W('V14', 'Maar mensen'));
  const card = (lab, t, chosen) => (<div style={{ flex: 1, background: J.card, border: `3px solid ${chosen && pick > 0.5 ? J.green : J.line}`, borderRadius: 18, padding: '24px 28px' }}><Kick color={J.slate}>Antwoord {lab}</Kick><T size={30} color={J.ink} style={{ marginTop: 8 }}>{t}</T>
    {chosen && <T size={44} style={{ marginTop: 10, opacity: pick }}>👍</T>}</div>);
  return (
    <AbsoluteFill style={{ background: J.bg }}>
      <JTitle at={at('V14')} kicker="Leren van menselijke voorkeuren">Wat mensen kiezen, is niet altijd wat waar is</JTitle>
      <div style={{ position: 'absolute', left: 128, top: 260, width: 1664, display: 'flex', gap: 28, opacity: sp(frame, F('V14', 0.5)) }}>
        {card('A', 'Uw plan heeft risico’s: uw inkomen is onzeker en de rente is hoog. Overweeg een kleiner bedrag.', false)}
        {card('B', 'Goed plan! U kunt die lening zeker aan. Succes!', true)}
      </div>
      <JBanner at={W('V14', 'In april')} top={640} size={38}>April 2025: OpenAI draait een update van GPT-4o terug. Het model was te vleiend geworden.</JBanner>
    </AbsoluteFill>
  );
};

const Helps = () => {
  const frame = useCurrentFrame();
  const items = [['Meet ook de bijwerking', 'niet alleen het doel', 'bijwerking'], ['Test lastige gevallen', 'zoals in practicum 4', 'Test met'], ['Laat een mens ingrijpen', 'met tijd en bevoegdheid', 'Laat een mens'], ['Blijf volgen', 'ook na de livegang', 'blijf volgen']];
  return (
    <AbsoluteFill style={{ background: J.bg }}>
      <JTitle at={at('V15')} kicker="Wat helpt">Vier manieren om de bedoeling te bewaken</JTitle>
      <div style={{ position: 'absolute', left: 128, top: 260, width: 1664, display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 24 }}>
        {items.map(([t, s, w], i) => { const a = sp(frame, W('V15', w)); return (
          <div key={t} style={{ opacity: a, transform: `translateY(${(1 - a) * 30}px)`, background: J.card, border: `2px solid ${J.line}`, borderTop: `10px solid ${i === 3 ? J.gold : J.blue}`, borderRadius: 18, padding: '26px 32px' }}>
            <T size={40} weight={700} color={J.navy}>{t}</T><T size={30} color={J.slate} style={{ marginTop: 6 }}>{s}</T></div>); })}
      </div>
    </AbsoluteFill>
  );
};

const NowYou = () => {
  const frame = useCurrentFrame();
  const st = [['Welk getal stuurt jullie oplossing?', 'Welk getal'], ['Hoe kan ze dat getal halen zonder het doel te dienen?', 'Hoe kan'], ['Wat test of volg je om dat op tijd te zien?', 'wat test']];
  return (
    <AbsoluteFill style={{ background: J.bg }}>
      <JTitle at={at('N1')} kicker="Opdracht" size={68}>Nu jij</JTitle>
      {st.map(([t, w], i) => { const a = sp(frame, W('N1', w)); return (
        <div key={i} style={{ position: 'absolute', left: 128, top: 250 + i * 170, width: 1664, opacity: a, transform: `translateY(${(1 - a) * 40}px)`, background: J.card, border: `2px solid ${J.line}`, borderRadius: 20, padding: '28px 38px', display: 'flex', gap: 30, alignItems: 'center' }}>
          <div style={{ fontFamily: FONT, fontWeight: 700, fontSize: 64, color: J.blue, width: 50 }}>{i + 1}</div><T size={42} color={J.navy} weight={700}>{t}</T></div>); })}
    </AbsoluteFill>
  );
};

export const Clip8b = () => (
  <Root scenes={[
    ['V0', <Intro />], ['V1', <Bank />], ['V3', <Alignment />], ['V5', <Hard />],
    ['Q1', <QuizN n={1} q="Q1" a="Q1b" question="Een tijdlijn wordt beloond voor zoveel mogelijk reacties en gedeelde berichten. Wat is hier de proxy?" options={['A. Het welzijn van de gebruikers', 'B. Het aantal reacties en gedeelde berichten']} good={1} note={<>B: <span style={{ color: J.gold }}>Facebook, 2018: verontwaardiging kreeg meer bereik</span></>} />],
    ['V8', <Coast />], ['V10', <Hack />], ['V12', <Sense />], ['V13', <Suribank />], ['V14', <Prefs />],
    ['Q2', <QuizN n={2} q="Q2" a="Q2b" question="Een moderatiesysteem wordt beloond voor elk verwijderd bericht, en verwijdert ook onschuldige berichten. Hoe heet dit?" options={['A. Reward hacking', 'B. Een adversarial aanval']} good={0} note={<>A: <span style={{ color: J.gold }}>de beloning is gehaald, de bedoeling niet</span></>} />],
    ['V15', <Helps />], ['N1', <NowYou />],
  ]} />
);
