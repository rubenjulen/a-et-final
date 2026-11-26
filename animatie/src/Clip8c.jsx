// Kennisclip 8c · Aanvullen of overlaten? (blok 1). Script: clip8c/build.py; timing: src/timing_c8c.json.
import React from 'react';
import { AbsoluteFill, useCurrentFrame, interpolate, Easing } from 'remotion';
import timing from './timing_c8c.json';
import { clamp, fade, Pop } from './wk1_kit';
import { J, FONT, JTitle, JBanner, makeJKit } from './janssen_kit';
import { sp, makeW, T, Kick, Panel, Person, Switch, Bub } from './janssen_parts';

const { cue, F, QuizN, Root } = makeJKit(timing);
const W = makeW(cue, F);
const at = (k, o = -0.2) => F(k, o);
const GOLD2 = '#A9852E';

const Intro = () => {
  const frame = useCurrentFrame(); const s = sp(frame, 4);
  const k = interpolate(frame, [20, 80], [0, 1], { ...clamp, easing: Easing.inOut(Easing.cubic) });
  return (
    <AbsoluteFill style={{ background: `radial-gradient(1300px 900px at 78% 25%, #1A3D86 0%, ${J.navy} 62%)` }}>
      <div style={{ position: 'absolute', left: 140, top: 250, opacity: s }}><Kick color={J.gold} style={{ fontSize: 30 }}>Kennisclip 8c · AI &amp; Ethics · blok 1</Kick></div>
      <div style={{ position: 'absolute', left: 140, top: 300, fontFamily: FONT, fontWeight: 700, fontSize: 130, lineHeight: 1.02, color: '#fff', opacity: s, transform: `translateY(${(1 - s) * 40}px)` }}>Aanvullen<br />of overlaten?</div>
      <div style={{ position: 'absolute', left: 1150, top: 400, width: 620, opacity: fade(frame, 18, 30) }}>
        <div style={{ height: 16, borderRadius: 8, background: `linear-gradient(90deg, ${J.green}, ${J.gold}, ${J.red})` }} />
        <div style={{ position: 'relative', height: 0 }}><div style={{ position: 'absolute', left: 20 + 540 * k, top: -38, width: 60, height: 60, borderRadius: 30, background: '#fff', border: `6px solid ${J.navy}` }} /></div>
        <div style={{ display: 'flex', justifyContent: 'space-between', marginTop: 50 }}><T size={30} weight={700} color="#fff">aanvullen</T><T size={30} weight={700} color="#fff">overlaten</T></div>
      </div>
    </AbsoluteFill>
  );
};

const Callcenter = () => {
  const frame = useCurrentFrame();
  const q = sp(frame, W('W1', 'Is dat'));
  return (
    <AbsoluteFill style={{ background: J.bg }}>
      <JTitle at={at('W1')} kicker="Denkvoorbeeld · een callcenter in Paramaribo">Een AI-assistent naast je</JTitle>
      <svg viewBox="0 0 500 500" style={{ position: 'absolute', left: 128, top: 250, width: 520, height: 520 }}>
        <Person x={250} y={380} s={5} col={GOLD2} />
        <path d="M170 170 Q250 90 330 170" fill="none" stroke={J.navy} strokeWidth="14" /><rect x="150" y="160" width="34" height="56" rx="12" fill={J.navy} /><rect x="316" y="160" width="34" height="56" rx="12" fill={J.navy} />
        <path d="M168 210 Q170 260 220 262" fill="none" stroke={J.navy} strokeWidth="6" />
      </svg>
      <div style={{ position: 'absolute', left: 720, top: 260, width: 640, background: J.card, border: `2px solid ${J.line}`, borderRadius: 22, padding: '20px 26px' }}>
        <Kick color={J.blue}>AI-assistent</Kick>
        <Bub at={W('W1', 'Die vat')} size={27}>Samenvatting: klant belt over een dubbele afschrijving van 15 november.</Bub>
        <Bub at={W('W1', 'stelt antwoorden')} size={27} bg="#E2F1E8">Voorstel: “Ik zie de dubbele afschrijving. Ik zet de terugboeking voor u in gang.”</Bub>
      </div>
      <div style={{ position: 'absolute', left: 1400, top: 300, width: 400, opacity: q, transform: `scale(${0.85 + 0.15 * q})` }}>
        <div style={{ background: J.navy, borderRadius: 18, padding: '24px 28px' }}><T size={34} weight={700} color="#fff">Goed nieuws,</T><T size={34} weight={700} color={J.gold}>of het begin van het einde?</T></div>
      </div>
    </AbsoluteFill>
  );
};

const Levels = () => {
  const frame = useCurrentFrame();
  const L = [['Taak', 'de baan blijft', 'AI vat gesprekken samen', 'W3', J.blue], ['Baan', 'het werk verdwijnt', 'een tolpoort die automatisch betaalt', 'W4', J.dblue], ['Sector', 'alles wordt anders', 'loketten worden apps, chatbots en zelfbediening', 'W5', J.navy]];
  return (
    <AbsoluteFill style={{ background: J.bg }}>
      <JTitle at={at('W2')} kicker="Wat neemt AI over?">Drie niveaus van automatisering</JTitle>
      {L.map(([t, s, vb, k, c], i) => { const on = sp(frame, F(k, 0)); const inn = sp(frame, F('W2', 1 + i * 0.4)); return (
        <div key={t} style={{ position: 'absolute', left: 128, top: 250 + i * 175, width: 1664, height: 150, display: 'flex', borderRadius: 18, overflow: 'hidden', opacity: inn, border: `2px solid ${J.line}`, boxShadow: on > 0.5 ? `0 0 0 ${6 * on}px ${c}55` : 'none' }}>
          <div style={{ width: 380, background: c, padding: '24px 30px', display: 'flex', flexDirection: 'column', justifyContent: 'center' }}><T size={44} weight={700} color="#fff">{i + 1} · {t}</T><T size={26} color="#DDE7F4">{s}</T></div>
          <div style={{ flex: 1, background: J.card, padding: '0 34px', display: 'flex', alignItems: 'center', opacity: 0.25 + 0.75 * on }}><T size={36} color={J.ink}>{vb}</T></div>
        </div>); })}
    </AbsoluteFill>
  );
};

const Exposure = () => {
  const frame = useCurrentFrame();
  const list = [['Routinewerk', 'routinewerk'], ['Administratie', 'administratie'], ['Klantcontact', 'klantcontact'], ['Instapfuncties', 'instapfuncties']];
  const big = (n, s, c, w) => { const a = sp(frame, w); return (<div style={{ flex: 1, opacity: a, transform: `translateY(${(1 - a) * 30}px)`, background: J.card, border: `2px solid ${J.line}`, borderTop: `10px solid ${c}`, borderRadius: 18, padding: '22px 28px' }}>
    <div style={{ fontFamily: FONT, fontWeight: 700, fontSize: 96, color: c, lineHeight: 1 }}>{n}</div><T size={28} color={J.ink} style={{ marginTop: 10 }}>{s}</T></div>); };
  return (
    <AbsoluteFill style={{ background: J.bg }}>
      <JTitle at={at('W6')} kicker="Wat het meest geraakt wordt">Blootgesteld is niet hetzelfde als vervangen</JTitle>
      <div style={{ position: 'absolute', left: 128, top: 250, width: 520 }}>
        {list.map(([t, w]) => { const a = sp(frame, W('W6', w)); return <div key={t} style={{ opacity: a, transform: `translateX(${(1 - a) * -30}px)`, background: J.ice, borderRadius: 14, padding: '18px 24px', marginBottom: 14 }}><T size={36} weight={700} color={J.navy}>{t}</T></div>; })}
        <T size={26} color={J.slate} style={{ opacity: sp(frame, W('W6', 'Volgens de ILO')) }}>ILO, 2023: administratief werk het meest; voor vrouwen meer dan twee keer zo groot.</T>
      </div>
      <div style={{ position: 'absolute', left: 720, top: 250, width: 1072, display: 'flex', gap: 24 }}>
        {big('40%', 'van het werk wereldwijd is blootgesteld aan AI (IMF, 2024)', J.blue, W('W7', 'Het IMF'))}
        {big('26–38%', 'van de banen in Latijns-Amerika en het Caribisch gebied (ILO en Wereldbank, 2024)', J.red, W('W7', 'In Latijns'))}
      </div>
    </AbsoluteFill>
  );
};

const Ring = () => {
  const frame = useCurrentFrame();
  const steps = [['Een bank sluit een kantoor in een district', 'Sluit een bank', J.navy], ['De winkel en het eethuis ernaast verliezen klanten', 'de winkel', GOLD2], ['Wie geen smartphone heeft, verliest toegang', 'geen smartphone', J.red]];
  return (
    <AbsoluteFill style={{ background: J.bg }}>
      <JTitle at={at('W8')} kicker="De tweede kring">Het effect stopt niet bij de baan</JTitle>
      <div style={{ position: 'absolute', left: 128, top: 300, width: 1664, display: 'flex', gap: 16, alignItems: 'stretch' }}>
        {steps.map(([t, w, c], i) => { const a = sp(frame, W('W8', w)); return (<React.Fragment key={t}>
          <div style={{ flex: 1, opacity: a, transform: `translateY(${(1 - a) * 30}px)`, background: J.card, border: `2px solid ${J.line}`, borderTop: `10px solid ${c}`, borderRadius: 18, padding: '26px 28px' }}><T size={36} weight={700} color={J.navy}>{t}</T></div>
          {i < 2 && <div style={{ alignSelf: 'center', fontFamily: FONT, fontWeight: 700, fontSize: 56, color: J.blue, opacity: a }}>→</div>}</React.Fragment>); })}
      </div>
      <JBanner at={W('W8', 'Dat is de tweede kring')} top={640} size={40}>De tweede kring hoort in K2, bij de stakeholders.</JBanner>
    </AbsoluteFill>
  );
};

const Slider = () => {
  const frame = useCurrentFrame();
  const causes = [['Het klinkt zeker', 'klinkt zeker'], ['Geen tijd om te controleren', 'geen tijd'], ['De schuldcultuur', 'wie afwijkt']];
  const pos = interpolate(frame, [W('W10', 'klinkt zeker'), W('W10', 'wie afwijkt') + 40], [0.12, 0.88], clamp);
  return (
    <AbsoluteFill style={{ background: J.bg }}>
      <JTitle at={at('W9')} kicker="Augmentatie en delegatie">Van aanvullen naar overlaten</JTitle>
      <div style={{ position: 'absolute', left: 128, top: 260, width: 1664 }}>
        <div style={{ display: 'flex', justifyContent: 'space-between', opacity: sp(frame, F('W9', 0.5)) }}>
          <div style={{ background: J.green, borderRadius: 16, padding: '16px 24px', width: 520 }}><T size={36} weight={700} color="#fff">Augmentatie</T><T size={26} color="#fff">AI ondersteunt, de mens beslist</T></div>
          <div style={{ background: J.red, borderRadius: 16, padding: '16px 24px', width: 520, opacity: sp(frame, W('W9', 'Bij delegatie')) }}><T size={36} weight={700} color="#fff">Delegatie</T><T size={26} color="#fff">AI beslist, de mens kijkt op papier mee</T></div>
        </div>
        <div style={{ position: 'relative', marginTop: 40, height: 18, borderRadius: 9, background: `linear-gradient(90deg, ${J.green}, ${J.gold}, ${J.red})` }}>
          <div style={{ position: 'absolute', left: `calc(${pos * 100}% - 34px)`, top: -25, width: 68, height: 68, borderRadius: 34, background: '#fff', border: `8px solid ${J.navy}` }} /></div>
        <div style={{ display: 'flex', gap: 20, marginTop: 60 }}>
          {causes.map(([t, w], i) => { const a = sp(frame, W('W10', w)); return <div key={t} style={{ flex: 1, opacity: a, transform: `translateY(${(1 - a) * 30}px)`, background: J.card, border: `2px solid ${J.line}`, borderTop: `8px solid ${[J.blue, J.gold, J.red][i]}`, borderRadius: 16, padding: '22px 26px' }}><T size={24} weight={700} color={J.slate}>OORZAAK {i + 1}</T><T size={34} weight={700} color={J.navy}>{t}</T></div>; })}
        </div>
      </div>
    </AbsoluteFill>
  );
};

const Conditions = () => {
  const frame = useCurrentFrame();
  const conds = ['Informatie', 'Tijd', 'Kennis', 'Bevoegdheid', 'Cultuur'];
  return (
    <AbsoluteFill style={{ background: J.bg }}>
      <JTitle at={at('W11')} kicker="Wat er misgaat, en wat er nodig is">Echte samenwerking</JTitle>
      <Switch style={{ left: 128, top: 250, width: 1664, height: 560 }} items={[
        [at('W11'), <div style={{ background: J.card, border: `2px solid ${J.line}`, borderLeft: `10px solid ${J.red}`, borderRadius: 18, padding: '30px 38px' }}>
          <Kick color={J.red}>Echte casus · New York, 2023</Kick><T size={48} weight={700} color={J.navy} style={{ marginTop: 10 }}>Mata v. Avianca</T>
          <T size={34} color={J.ink} style={{ marginTop: 14 }}>Advocaten dienden een pleitnota in met uitspraken die ChatGPT had verzonnen.</T>
          <div style={{ display: 'inline-block', marginTop: 20, background: J.red, color: '#fff', fontFamily: FONT, fontWeight: 700, fontSize: 40, borderRadius: 14, padding: '10px 24px', opacity: sp(frame, W('W11', 'Ze kregen')) }}>Boete: 5.000 dollar</div></div>],
        [at('W12'), <div>
          <div style={{ display: 'flex', gap: 16 }}>{conds.map((c, i) => { const a = sp(frame, F('W12', 1 + i * 0.8)); return <div key={c} style={{ flex: 1, opacity: a, background: J.ice, borderRadius: 14, padding: '22px 18px', textAlign: 'center' }}><T size={34} weight={700} color={J.navy}>{c}</T></div>; })}</div>
          <div style={{ marginTop: 40, background: J.navy, borderRadius: 18, padding: '28px 36px', opacity: sp(frame, W('W12', 'Samenwerken met AI')) }}><T size={40} weight={700} color="#fff">Alleen ethisch als <span style={{ color: J.gold }}>macht, begrip en verantwoording</span> bij elkaar horen.</T></div></div>],
      ]} />
    </AbsoluteFill>
  );
};

const Suriname = () => {
  const frame = useCurrentFrame();
  const c = (k, t, b, col, w) => { const a = sp(frame, W('W13', w)); return (<div style={{ flex: 1, opacity: a, transform: `translateY(${(1 - a) * 30}px)`, background: J.card, border: `2px solid ${J.line}`, borderLeft: `10px solid ${col}`, borderRadius: 18, padding: '24px 30px' }}>
    <Kick color={J.slate}>{k}</Kick><T size={36} weight={700} color={J.navy} style={{ marginTop: 6 }}>{t}</T><T size={24} color={J.slate} style={{ marginTop: 8 }}>{b}</T></div>); };
  return (
    <AbsoluteFill style={{ background: J.bg }}>
      <JTitle at={at('W13')} kicker="Dichtbij">Ook in Suriname</JTitle>
      <div style={{ position: 'absolute', left: 128, top: 260, width: 1664, display: 'flex', gap: 24 }}>
        {c('Callcenters', 'Een bloeiende sector, onder druk door AI', 'Dagblad Suriname, 2025 en 2026', J.red, 'Callcenters')}
        {c('Banken', 'AI-assistenten voor klantvragen', 'onder meer DSB Buddy via WhatsApp', J.blue, 'Banken')}
        {c('Finabank', '“Human in the loop”: medewerkers blijven verantwoordelijk', 'Suriname Herald, 12 november 2026', J.green, 'Finabank')}
      </div>
      <JBanner at={W('W13', 'De vraag is')} top={620} size={40}>Hoe ziet die controle er in de praktijk uit: aanvullen of overlaten?</JBanner>
    </AbsoluteFill>
  );
};

const Winst = () => {
  const frame = useCurrentFrame();
  const items = [['Data', 'Data'], ['Rekenkracht', 'rekenkracht'], ['Talent', 'talent']];
  return (
    <AbsoluteFill style={{ background: J.bg }}>
      <JTitle at={at('W14')} kicker="Wie vangt de winst?">Meer welvaart, maar voor wie?</JTitle>
      <svg width="900" height="430" style={{ position: 'absolute', left: 128, top: 250 }}>
        <polygon points="0,0 900,0 560,320 340,320" fill={J.ice} />
        {items.map(([t, w], i) => <text key={t} x={150 + i * 300} y="80" textAnchor="middle" fontFamily={FONT} fontWeight="700" fontSize="40" fill={J.navy} opacity={sp(frame, W('W14', w))}>{t}</text>)}
        <rect x="330" y="320" width="240" height="90" rx="16" fill={J.navy} opacity={sp(frame, W('W14', 'handvol'))} />
        <text x="450" y="375" textAnchor="middle" fontFamily={FONT} fontWeight="700" fontSize="30" fill="#fff" opacity={sp(frame, W('W14', 'handvol'))}>weinig bedrijven</text>
      </svg>
      <div style={{ position: 'absolute', left: 1100, top: 260, width: 690, opacity: sp(frame, W('W14', 'Wie hun')) }}>
        <div style={{ background: J.card, border: `2px solid ${J.line}`, borderRadius: 18, padding: '24px 30px' }}><T size={34} weight={700} color={J.navy}>AI-afhankelijk of AI-sterk?</T><T size={28} color={J.ink} style={{ marginTop: 8 }}>Wie hun modellen gebruikt, betaalt en levert data, maar bouwt weinig zelf op.</T></div>
      </div>
      <JBanner at={F('W15', 0.2)} top={720} size={40}>Geen natuurwet, maar een keuze van bedrijven en overheden.</JBanner>
    </AbsoluteFill>
  );
};

const NowYou = () => {
  const frame = useCurrentFrame();
  const st = [['Vult jullie oplossing werk aan, of neemt ze het over?', 'Vult'], ['Wie verliest taken, inkomen of zeggenschap, ook in de tweede kring?', 'Wie verliest'], ['Schrijf het op bij domein 10 van de nulmeting.', 'Schrijf']];
  return (
    <AbsoluteFill style={{ background: J.bg }}>
      <JTitle at={at('N1')} kicker="Opdracht" size={68}>Nu jij</JTitle>
      {st.map(([t, w], i) => { const a = sp(frame, W('N1', w)); return (
        <div key={i} style={{ position: 'absolute', left: 128, top: 250 + i * 170, width: 1664, opacity: a, transform: `translateY(${(1 - a) * 40}px)`, background: J.card, border: `2px solid ${J.line}`, borderRadius: 20, padding: '28px 38px', display: 'flex', gap: 30, alignItems: 'center' }}>
          <div style={{ fontFamily: FONT, fontWeight: 700, fontSize: 64, color: J.blue, width: 50 }}>{i + 1}</div><T size={42} color={J.navy} weight={700}>{t}</T></div>); })}
    </AbsoluteFill>
  );
};

export const Clip8c = () => (
  <Root scenes={[
    ['W0', <Intro />], ['W1', <Callcenter />], ['W2', <Levels />], ['W6', <Exposure />], ['W8', <Ring />],
    ['Q1', <QuizN n={1} q="Q1" a="Q1b" question="Een bankmedewerker laat AI elke ochtend de klachten van gisteren samenvatten. Haar baan blijft bestaan. Welk niveau is dit?" options={['A. Taak', 'B. Baan', 'C. Sector']} good={0} note={<>A: <span style={{ color: J.gold }}>de baan blijft, de inhoud verandert</span></>} />],
    ['W9', <Slider />], ['W11', <Conditions />], ['W13', <Suriname />], ['W14', <Winst />],
    ['Q2', <QuizN n={2} q="Q2" a="Q2b" question="Wie afwijkt van het AI-advies en fout zit, krijgt een berisping. Wat gebeurt er?" options={['A. De medewerker blijft echt beslissen', 'B. Aanvullen wordt overlaten: iedereen volgt het advies']} good={1} note={<>B: <span style={{ color: J.gold }}>een schuldcultuur maakt augmentatie tot delegatie</span></>} />],
    ['N1', <NowYou />],
  ]} />
);
