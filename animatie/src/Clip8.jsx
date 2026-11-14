/* Kennisclip 8 · Automation bias (week 2) */
import React from 'react';
import { AbsoluteFill, useCurrentFrame, interpolate, spring } from 'remotion';
import timing from './timing_c8.json';
import { C, SERIF, SANS, FPS, clamp, makeKit, Person } from './wk2_kit';

const K = makeKit(timing);
const { F, Pop, Card, Banner, Title, QuizN, Composition, TitleScene, Summary } = K;

/* Werkplek: medewerker, scherm met advies, klik op akkoord */
const Desk = ({ frame, advice = 'Advies: afwijzen', clicks = 0, flash = 0 }) => (
  <div style={{ position: 'relative', width: 760, height: 520 }}>
    <div style={{ position: 'absolute', left: 230, top: 20, width: 500, height: 320, background: C.dark, borderRadius: 18, padding: 18 }}>
      <div style={{ background: C.card, height: '100%', borderRadius: 10, padding: 24 }}>
        <div style={{ fontFamily: SANS, fontSize: 22, color: C.mute }}>Kredietaanvraag · dossier {1040 + clicks}</div>
        <div style={{ fontFamily: SERIF, fontWeight: 700, fontSize: 40, color: C.terra, marginTop: 14 }}>{advice}</div>
        <div style={{ fontFamily: SANS, fontSize: 22, color: C.mute, marginTop: 8 }}>score 41 / 100</div>
        <div style={{ marginTop: 22, display: 'inline-block', fontFamily: SANS, fontWeight: 700, fontSize: 28, padding: '12px 28px', borderRadius: 12, background: flash > 0 ? C.green : '#DDE7E1', color: flash > 0 ? C.card : C.green }}>Akkoord</div>
        <div style={{ marginLeft: 16, display: 'inline-block', fontFamily: SANS, fontSize: 24, color: '#9AA39E' }}>Afwijken…</div>
      </div>
    </div>

    <div style={{ position: 'absolute', left: 0, top: 160 }}><Person size={200} frame={frame} color="#3E6B8A" /></div>
    <div style={{ position: 'absolute', left: 120, top: 440, width: 640, height: 30, background: '#B88E66', borderRadius: 8 }} />
  </div>
);

/* D1 */
const Click = () => {
  const frame = useCurrentFrame();
  const t0 = F('d1a', 0.5);
  const period = 45;
  const n = Math.max(0, Math.floor((frame - t0) / period));
  const flash = (frame - t0) % period < 8 && frame > t0 ? 1 : 0;
  return (
    <AbsoluteFill style={{ background: C.light }}>
      <Title at={F('d1a', 0)} kicker="Wat is automation bias?">De neiging om de computer te volgen</Title>
      <Pop at={F('d1a', 0.3)} style={{ left: 160, top: 280 }}><Desk frame={frame} clicks={n} flash={flash} /></Pop>
      <Pop at={F('d1a', 2)} style={{ left: 1080, top: 320, width: 640 }}>
        <Card style={{ textAlign: 'center' }}>
          <div style={{ fontFamily: SANS, fontSize: 26, color: C.mute }}>Vandaag op "akkoord" geklikt</div>
          <div style={{ fontFamily: SERIF, fontWeight: 700, fontSize: 120, color: C.dark }}>{n}×</div>
          <div style={{ fontFamily: SANS, fontSize: 26, color: C.mute }}>afgeweken: <b style={{ color: C.terra }}>0×</b></div>
        </Card>
      </Pop>
      <Pop at={F('d1b', 0.5)} style={{ left: 1080, top: 640, width: 640 }}>
        <div style={{ fontFamily: SANS, fontSize: 28, color: C.ink }}>Fouten worden over het hoofd gezien. Advies wordt overgenomen zonder controle.</div>
      </Pop>
    </AbsoluteFill>
  );
};

/* D2: vier oorzaken */
const Why = () => {
  const frame = useCurrentFrame();
  const r = [
    ['⏱', 'Tijdsdruk', 'd2a', 1.5],
    ['🖥', 'Computer lijkt objectief', 'd2a', 3.2],
    ['✍', 'Afwijken moet je verantwoorden — meegaan nooit', 'd2b', 0.3],
    ['🤷', '"Het systeem is verantwoordelijk"', 'd2c', 0.3],
  ];
  const stack = Math.min(14, Math.max(0, Math.floor((frame - F('d2a', 0)) / 10)));
  return (
    <AbsoluteFill style={{ background: C.light }}>
      <Title at={F('d2a', 0)} kicker="Waarom gebeurt het?">Vier redenen om mee te gaan</Title>
      <div style={{ position: 'absolute', left: 1460, top: 300 }}>
        {Array.from({ length: stack }).map((_, i) => <div key={i} style={{ position: 'absolute', left: (i % 2) * 6, top: 360 - i * 24, width: 260, height: 22, background: i % 2 ? '#E9DFC9' : '#F3EAD6', border: '2px solid #D6C9AE', borderRadius: 4 }} />)}
        <div style={{ position: 'absolute', top: 400, left: 40, fontFamily: SANS, fontSize: 24, color: C.mute }}>dossiers wachten…</div>
      </div>
      <div style={{ position: 'absolute', left: 128, top: 280, width: 1240 }}>
        {r.map(([ic, t, k, o]) => (
          <Pop key={t} at={F(k, o)} style={{ position: 'relative', marginBottom: 20 }}>
            <Card style={{ display: 'flex', alignItems: 'center', gap: 24, padding: '20px 28px' }}>
              <span style={{ fontSize: 46, width: 60, textAlign: 'center' }}>{ic}</span>
              <span style={{ fontFamily: SANS, fontWeight: 700, fontSize: 32, color: C.ink }}>{t}</span>
            </Card>
          </Pop>
        ))}
      </div>
    </AbsoluteFill>
  );
};

/* D3: werkinstructie en de praktijk */
const Instruction = () => {
  const frame = useCurrentFrame();
  const g = interpolate(frame, [F('d3c', 0), F('d3c', 1.5)], [0, 1], clamp);
  return (
    <AbsoluteFill style={{ background: C.light }}>
      <Title at={F('d3a', 0)} kicker="Een voorbeeld">Formeel een mens, in de praktijk het model</Title>
      <Pop at={F('d3a', 1)} style={{ left: 128, top: 290, width: 760 }}>
        <Card style={{ background: '#F3EAD6' }}>
          <div style={{ fontFamily: SANS, fontWeight: 700, fontSize: 24, color: C.mute, letterSpacing: 1 }}>WERKINSTRUCTIE KREDIET</div>
          <div style={{ fontFamily: SANS, fontSize: 32, color: C.ink, marginTop: 14 }}>⏱ 15 minuten per dossier</div>
          <div style={{ fontFamily: SANS, fontSize: 32, color: C.ink, marginTop: 10, opacity: interpolate(frame, [F('d3a', 4), F('d3a', 4.6)], [0, 1], clamp) }}>✍ Afwijken van het advies alleen met schriftelijk akkoord van het afdelingshoofd</div>
        </Card>
      </Pop>
      <Pop at={F('d3b', 0)} style={{ left: 960, top: 300, width: 820 }}>
        <div style={{ fontFamily: SERIF, fontWeight: 700, fontSize: 64, color: C.dark }}>Hoe vaak wijkt deze medewerker af?</div>
      </Pop>
      <Pop at={F('d3c', 0)} style={{ left: 960, top: 520, width: 820 }}>
        <div style={{ display: 'flex', gap: 20 }}>
          <Card style={{ flex: 1, textAlign: 'center', opacity: 1 - 0.5 * g }}>
            <div style={{ fontFamily: SANS, fontSize: 24, color: C.mute }}>formeel</div>
            <div style={{ fontFamily: SERIF, fontWeight: 700, fontSize: 44, color: C.green }}>de mens</div>
          </Card>
          <Card style={{ flex: 1, textAlign: 'center', borderColor: C.terra, transform: `scale(${1 + 0.06 * g})` }}>
            <div style={{ fontFamily: SANS, fontSize: 24, color: C.mute }}>in de praktijk</div>
            <div style={{ fontFamily: SERIF, fontWeight: 700, fontSize: 44, color: C.terra }}>het model</div>
          </Card>
        </div>
      </Pop>
    </AbsoluteFill>
  );
};

/* D4: krantenkoppen (generiek, geen echte krantennamen) */
const Headlines = () => {
  const frame = useCurrentFrame();
  const heads = [
    ['Duizenden ouders onterecht als fraudeur behandeld', 'd4a', 1.5, -3],
    ['Risicomodel en medewerkers versterkten elkaar', 'd4b', 0.3, 2],
    ['Getroffenen konden zich nauwelijks verweren', 'd4b', 2.5, -1.5],
    ['Parlementaire commissie (2020): "ongekend onrecht"', 'd4c', 0.4, 1.5],
  ];
  return (
    <AbsoluteFill style={{ background: C.light }}>
      <Title at={F('d4a', 0)} kicker="De toeslagenaffaire">Wanneer mens en systeem elkaar versterken</Title>
      {heads.map(([h, k, o, rot], i) => {
        const s = spring({ frame: frame - F(k, o), fps: FPS, config: { damping: 14 } });
        return (
          <div key={h} style={{ position: 'absolute', left: 170 + (i % 2) * 820, top: 300 + Math.floor(i / 2) * 210, width: 760, opacity: s, transform: `rotate(${rot}deg) scale(${0.85 + 0.15 * s})` }}>
            <div style={{ background: C.card, borderTop: `8px solid ${C.ink}`, padding: '20px 26px', boxShadow: '0 12px 26px rgba(0,0,0,.12)' }}>
              <div style={{ fontFamily: SANS, fontSize: 18, color: C.mute, letterSpacing: 2 }}>NIEUWS · NEDERLAND</div>
              <div style={{ fontFamily: SERIF, fontWeight: 700, fontSize: 38, color: C.ink, lineHeight: 1.12, marginTop: 6 }}>{h}</div>
            </div>
          </div>
        );
      })}
    </AbsoluteFill>
  );
};

/* D5: zes vinkjes */
const Six = () => {
  const frame = useCurrentFrame();
  const items = [['informatie', 'd5a', 3.5], ['tijd', 'd5a', 5.0], ['kennis', 'd5a', 6.2], ['bevoegdheid om af te wijken', 'd5b', 0.3], ['cultuur waarin afwijken mag', 'd5b', 2.4], ['registratie van afwijkingen', 'd5c', 1.0]];
  return (
    <AbsoluteFill style={{ background: C.light }}>
      <Title at={F('d5a', 0)} kicker="Betekenisvolle menselijke controle">Een mens heeft pas echt controle met…</Title>
      <div style={{ position: 'absolute', left: 128, top: 290, width: 1664, display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 22 }}>
        {items.map(([t, k, o], i) => {
          const s = spring({ frame: frame - F(k, o), fps: FPS, config: { damping: 12 } });
          return (
            <div key={t} style={{ display: 'flex', alignItems: 'center', gap: 22, background: C.card, border: `2px solid ${s > 0.5 ? C.green : C.line}`, borderRadius: 20, padding: '20px 28px' }}>
              <div style={{ width: 56, height: 56, borderRadius: 28, background: s > 0.5 ? C.green : C.sand, color: C.card, fontSize: 36, fontWeight: 700, display: 'flex', alignItems: 'center', justifyContent: 'center', transform: `scale(${0.6 + 0.4 * s})`, fontFamily: SANS }}>✓</div>
              <span style={{ fontFamily: SANS, fontWeight: 700, fontSize: 32, color: C.ink, opacity: 0.35 + 0.65 * s }}>{t}</span>
            </div>
          );
        })}
      </div>
    </AbsoluteFill>
  );
};

/* D6: chatbot-antwoord met één fout */
const GenAI = () => {
  const frame = useCurrentFrame();
  const mark = interpolate(frame, [F('d6b', 0.5), F('d6b', 1.5)], [0, 1], clamp);
  return (
    <AbsoluteFill style={{ background: C.light }}>
      <Title at={F('d6a', 0)} kicker="Bij generatieve AI">Vloeiend en zelfverzekerd, ook als het niet klopt</Title>
      <Pop at={F('d6a', 1)} style={{ left: 128, top: 290, width: 1080 }}>
        <Card>
          <div style={{ fontFamily: SANS, fontSize: 22, color: C.mute }}>Conceptbrief door de assistent</div>
          <div style={{ fontFamily: SERIF, fontSize: 32, color: C.ink, lineHeight: 1.45, marginTop: 12 }}>
            Geachte mevrouw Ramdin,<br />
            Hartelijk dank voor uw aanvraag. Wij hebben uw dossier zorgvuldig bekeken.{' '}
            <span style={{ background: `rgba(168,67,44,${0.25 * mark})`, borderBottom: `4px solid rgba(168,67,44,${mark})` }}>U kunt binnen 30 dagen opnieuw een aanvraag doen zonder nieuwe documenten.</span>{' '}
            Wij wensen u veel succes.
          </div>
        </Card>
      </Pop>
      <Pop at={F('d6b', 1.6)} style={{ left: 1260, top: 380, width: 520 }}>
        <div style={{ fontFamily: SANS, fontWeight: 700, fontSize: 30, color: C.terra }}>← klopt niet met de regels van de bank</div>
        <div style={{ fontFamily: SANS, fontSize: 26, color: C.mute, marginTop: 14 }}>Hoe overtuigender het klinkt, hoe minder we controleren.</div>
      </Pop>
      <Banner at={F('d6c', 0.6)} top={720} size={38}>Wie de brief verstuurt, <span style={{ color: C.amber }}>blijft verantwoordelijk</span> voor de inhoud.</Banner>
    </AbsoluteFill>
  );
};

export const Clip8 = () => {
  const scenes = [
    ['t0', <TitleScene n={8} title="Automation bias" sub="Waarom een mens in het proces nog geen controle is" />],
    ['d1a', <Click />],
    ['d2a', <Why />],
    ['d3a', <Instruction />],
    ['d4a', <Headlines />],
    ['d5a', <Six />],
    ['q1', <QuizN n={null} q="q1" a="a1" question="Een medewerker mag afwijken, maar alleen met schriftelijk akkoord, en heeft 15 minuten per dossier. Is er betekenisvolle menselijke controle?" options={['A. Ja, er zit een mens tussen.', 'B. Twijfelachtig; de drempel om af te wijken is hoog en de tijd kort.']} good={1} note={<>Een mens in het proces is <span style={{ color: C.amber }}>nog geen controle</span>.</>} />],
    ['d6a', <GenAI />],
    ['d7a', <Summary k="d7a" cols={3} title="Een mens in het proces is nog geen controle" items={['Informatie', 'Tijd', 'Kennis', 'Bevoegdheid', 'Cultuur', 'Registratie']} bannerKey="d7c" banner={<>Hoe overtuigender het antwoord, <span style={{ color: C.amber }}>hoe belangrijker de controle</span>.</>} />],
  ];
  return <Composition scenes={scenes} />;
};
