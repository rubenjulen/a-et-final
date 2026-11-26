import React from 'react';
import { AbsoluteFill, useCurrentFrame, interpolate } from 'remotion';
import timing from './timing_kD.json';
import {
  C, SERIF, SANS, FPS, clamp, makeF, useSpr, mix, Pop, Card, Banner, Heading,
  Quiz8, TitleScene, ClipShell, Person,
} from './wk3kit_j';

const tm = makeF(timing);
const { F } = tm;
const on = (frame, k, o = 0) => frame >= F(k, o);
const AMP = 'AI & ETHICS';

/* ---------- small building blocks ---------- */
const Chip = ({ children, bg = C.sand, color = C.dark, size = 26, style = {} }) => (
  <span style={{ display: 'inline-block', background: bg, color, fontFamily: SANS, fontWeight: 700, fontSize: size, padding: '8px 18px', borderRadius: 999, ...style }}>{children}</span>
);
const Icon = ({ kind, size = 64, color = C.dark }) => {
  const s = { width: size, height: size };
  if (kind === 'flow') return (<svg {...s} viewBox="0 0 64 64"><rect x="4" y="8" width="20" height="14" rx="4" fill={color} /><rect x="40" y="8" width="20" height="14" rx="4" fill={color} /><rect x="22" y="42" width="20" height="14" rx="4" fill={color} /><path d="M14 22 L32 42 M50 22 L32 42" stroke={color} strokeWidth="4" fill="none" /></svg>);
  if (kind === 'brain') return (<svg {...s} viewBox="0 0 64 64"><path d="M10 34 Q8 16 26 12 Q32 6 40 12 Q56 14 54 32 Q58 46 44 50 Q38 58 28 52 Q12 54 10 34Z" fill={color} /><path d="M24 20 Q30 28 24 38 M40 18 Q34 28 42 40" stroke={C.card} strokeWidth="3" fill="none" /></svg>);
  if (kind === 'db') return (<svg {...s} viewBox="0 0 64 64"><ellipse cx="32" cy="12" rx="22" ry="8" fill={color} /><path d="M10 12 V50 Q32 64 54 50 V12" fill={color} /><path d="M10 25 Q32 36 54 25 M10 38 Q32 49 54 38" stroke={C.card} strokeWidth="3" fill="none" /></svg>);
  if (kind === 'server') return (<svg {...s} viewBox="0 0 64 64"><rect x="8" y="6" width="48" height="16" rx="4" fill={color} /><rect x="8" y="26" width="48" height="16" rx="4" fill={color} /><rect x="8" y="46" width="48" height="14" rx="4" fill={color} /><circle cx="46" cy="14" r="3" fill={C.amber} /><circle cx="46" cy="34" r="3" fill={C.amber} /></svg>);
  if (kind === 'doc') return (<svg {...s} viewBox="0 0 64 64"><path d="M14 4 H40 L52 16 V60 H14Z" fill={C.card} stroke={color} strokeWidth="4" /><path d="M22 26 H44 M22 36 H44 M22 46 H36" stroke={color} strokeWidth="4" /></svg>);
  if (kind === 'eye') return (<svg {...s} viewBox="0 0 64 64"><path d="M4 32 Q32 6 60 32 Q32 58 4 32Z" fill="none" stroke={color} strokeWidth="5" /><circle cx="32" cy="32" r="9" fill={color} /></svg>);
  if (kind === 'pen') return (<svg {...s} viewBox="0 0 64 64"><path d="M8 52 Q20 30 30 44 Q38 54 56 24" stroke={color} strokeWidth="5" fill="none" strokeLinecap="round" /><path d="M8 58 H56" stroke={color} strokeWidth="3" /></svg>);
  return null;
};

/* ---------- D0: title + where a measure lands ---------- */
const Title = () => {
  const frame = useCurrentFrame();
  const drop = interpolate(frame, [F('D0a', 3.2), F('D0a', 5.2)], [0, 1], { ...clamp });
  const pads = ['Eigenaar', 'Proces', 'Leverancier'];
  const target = Math.min(2, Math.floor(interpolate(frame, [F('D0a', 4.2), F('D0a', 8.2)], [0, 2.99], clamp)));
  return (
    <TitleScene at={F('D0a', -0.3)} kicker={`KADERCLIP D · ${AMP} · BLOK 2`} title="Governance over de levenscyclus">
      <div style={{ position: 'absolute', left: 140, top: 560, width: 900, fontFamily: SANS, fontSize: 38, color: '#C9D6E8' }}>leveranciers en AI-agents (AIGP)</div>
      <div style={{ position: 'absolute', left: 1180, top: 210, width: 600, height: 500 }}>
        <div style={{ position: 'absolute', left: 140 + (target - 1) * 180 * drop, top: 20 + drop * 250, width: 320, background: C.amber, color: C.dark, fontFamily: SANS, fontWeight: 700, fontSize: 28, padding: '18px 22px', borderRadius: 16, textAlign: 'center', opacity: on(frame, 'D0a', 2.5) ? 1 : 0, boxShadow: '0 16px 30px rgba(0,0,0,.25)' }}>Maatregel</div>
        {pads.map((p, i) => {
          const lit = drop > 0.95 && target === i;
          return (
            <div key={p} style={{ position: 'absolute', left: i * 200, top: 380, width: 180, padding: '16px 0', textAlign: 'center', borderRadius: 14, fontFamily: SANS, fontWeight: 700, fontSize: 26, color: lit ? C.dark : '#C9D6E8', background: lit ? C.light : 'rgba(255,255,255,0.08)', border: '2px solid rgba(255,255,255,0.25)', opacity: on(frame, 'D0a', 1.0 + i * 0.4) ? 1 : 0 }}>{p}</div>
          );
        })}
      </div>
    </TitleScene>
  );
};

const Intro = () => {
  const frame = useCurrentFrame();
  const band = useSpr(F('D0b', 0.3));
  const badge = useSpr(F('D0c', 1.0));
  return (
    <AbsoluteFill style={{ background: C.light }}>
      <Heading at={F('D0b', 0)} kicker="GOVERNANCE">Wie beslist, en wie controleert?</Heading>
      <div style={{ position: 'absolute', left: 128, top: 330, width: 1664 * band, height: 26, borderRadius: 13, background: `linear-gradient(90deg, ${C.green}, ${C.dark})` }} />
      <div style={{ position: 'absolute', left: 128, top: 380, fontFamily: SANS, fontSize: 30, fontWeight: 700, color: C.green, opacity: band }}>eerste ontwerp</div>
      <div style={{ position: 'absolute', right: 128, top: 380, fontFamily: SANS, fontSize: 30, fontWeight: 700, color: C.dark, opacity: band }}>dagelijks gebruik</div>
      <Pop at={F('D0c', 1.0)} style={{ left: 128, top: 480 }}>
        <Card style={{ display: 'flex', gap: 28, alignItems: 'center', width: 900 }}>
          <div style={{ width: 120, height: 120, borderRadius: 60, background: C.dark, color: C.amber, fontFamily: SERIF, fontWeight: 700, fontSize: 40, display: 'flex', alignItems: 'center', justifyContent: 'center', transform: `rotate(${(1 - badge) * -30}deg)` }}>AIGP</div>
          <div>
            <div style={{ fontFamily: SANS, fontWeight: 700, fontSize: 32, color: C.ink }}>AI Governance Professional</div>
            <div style={{ fontFamily: SANS, fontSize: 28, color: C.mute, marginTop: 6 }}>certificering van de IAPP, beroepsvereniging voor privacy en AI</div>
          </div>
        </Card>
      </Pop>
      <Pop at={F('D0d', 0.8)} style={{ left: 1130, top: 500 }}>
        <div style={{ fontFamily: SANS, fontSize: 28, color: C.mute, marginBottom: 14 }}>Niet halen, wel gebruiken bij:</div>
        <div style={{ display: 'flex', gap: 16 }}><Chip bg={C.amber} size={34}>K3</Chip><Chip bg={C.amber} size={34}>K7</Chip></div>
      </Pop>
    </AbsoluteFill>
  );
};

/* ---------- D1: two phases ---------- */
const Phases = () => {
  const frame = useCurrentFrame();
  const dev = ['Use case', 'Wie wordt geraakt?', 'Eisen', 'Getest vóór livegang?'];
  const use = ['Monitoring', 'Incidenten', 'Instructie voor medewerkers', 'Besluit om uit te zetten'];
  const live = interpolate(frame, [F('D1e', 0.5), F('D1e', 5.5)], [0, 1], clamp);
  const Col = ({ x, title, items, key0, color, kLabel, kAt }) => (
    <div style={{ position: 'absolute', left: x, top: 250, width: 790 }}>
      <Pop at={F(key0, 0)} style={{ left: 0, top: 0, width: 790 }}>
        <div style={{ background: color, color: C.light, fontFamily: SERIF, fontWeight: 700, fontSize: 44, padding: '18px 30px', borderRadius: '20px 20px 0 0' }}>{title}</div>
      </Pop>
      {items.map((t, i) => (
        <Pop key={t} at={F(key0, 1.2 + i * 1.6)} style={{ left: 0, top: 96 + i * 78, width: 790 }}>
          <div style={{ background: C.card, border: `2px solid ${C.line}`, borderTop: 'none', fontFamily: SANS, fontSize: 32, color: C.ink, padding: '16px 30px' }}>{t}</div>
        </Pop>
      ))}
      <Pop at={F('D1d', kAt)} style={{ left: 0, top: 430, width: 790 }}>
        <div style={{ border: `3px dashed ${color}`, borderRadius: 16, padding: '14px 24px', fontFamily: SANS, fontWeight: 700, fontSize: 30, color }}>{kLabel}</div>
      </Pop>
    </div>
  );
  return (
    <AbsoluteFill style={{ background: C.light }}>
      <Heading at={F('D1a', 0)} kicker="AIGP: TWEE FASEN">Ontwikkeling en gebruik</Heading>
      <Col x={128} title="1 · Ontwikkeling" items={dev} key0="D1b" color={C.green} kLabel="Jullie rapport: K1 t/m K7" kAt={2.2} />
      <Col x={1002} title="2 · Gebruik" items={use} key0="D1c" color={C.dark} kLabel="Jullie rapport: K8 en beslismemo" kAt={5.0} />
      {on(frame, 'D1e', 0) && (
        <div style={{ position: 'absolute', left: 128, top: 800, width: 1664, height: 70 }}>
          <div style={{ position: 'absolute', left: 0, top: 30, width: 1664, height: 8, background: C.line, borderRadius: 4 }} />
          <div style={{ position: 'absolute', left: 860, top: -6, fontFamily: SANS, fontWeight: 700, fontSize: 24, color: C.terra }}>livegang ▼</div>
          {[1, 2, 3, 4, 5].map((m) => {
            const o = interpolate(live, [(m - 1) / 5, m / 5], [0, 1], clamp);
            return <div key={m} style={{ position: 'absolute', left: 880 + m * 150, top: 22, width: 24, height: 24, borderRadius: 12, background: m >= 4 ? C.terra : C.green, opacity: o }} />;
          })}
          <div style={{ position: 'absolute', left: 1250, top: -34, whiteSpace: 'nowrap', fontFamily: SANS, fontWeight: 700, fontSize: 24, color: C.terra, opacity: live > 0.75 ? 1 : 0 }}>problemen na een paar maanden</div>
        </div>
      )}
    </AbsoluteFill>
  );
};

/* ---------- D2: roles ---------- */
const ROLES = [
  ['Ontwikkelaar', 'bouwt het systeem', 'team A-AI2', 'D2b', C.green],
  ['Aanbieder', 'brengt het onder eigen naam in gebruik', 'Frisco', 'D2c', C.dark],
  ['Gebruiksverantwoordelijke', 'zet het in, in de eigen organisatie', 'Frisco', 'D2c', C.dark],
  ['Gebruiker', 'medewerker en klant', 'medewerker · klant', 'D2d', C.terra],
];
const Roles = () => {
  const frame = useCurrentFrame();
  return (
    <AbsoluteFill style={{ background: C.light }}>
      <Heading at={F('D2a', 0)} kicker="ROLLEN">Wie beslist er? Dat hangt af van de rol</Heading>
      {ROLES.map(([r, d, who, k, col], i) => {
        const offs = i === 2 ? 4.5 : 0.3;
        const s = interpolate(frame, [F(k, offs), F(k, offs + 0.8)], [0, 1], clamp);
        const frisco = who === 'Frisco' && on(frame, 'D2e', 3.2 + (i === 2 ? 0 : 3.0));
        const tag = i === 0 ? on(frame, 'D2b', 2.0) : i === 3 ? on(frame, 'D2d', 1.5) : frisco;
        return (
          <div key={r} style={{ position: 'absolute', left: 128 + i * 420, top: 290, width: 390, opacity: s, transform: `translateY(${(1 - s) * -120}px)` }}>
            <div style={{ background: C.card, border: `3px solid ${col}`, borderRadius: 22, padding: '24px 26px', height: 250, boxSizing: 'border-box' }}>
              <div style={{ fontFamily: SERIF, fontWeight: 700, fontSize: r.length > 15 ? 25 : 38, color: col }}>{r}</div>
              <div style={{ fontFamily: SANS, fontSize: 27, color: C.mute, marginTop: 10, lineHeight: 1.3 }}>{d}</div>
            </div>
            <div style={{ marginTop: 18, display: 'flex', justifyContent: 'center', opacity: tag ? 1 : 0, transform: `scale(${tag ? 1 : 0.8})` }}>
              <Chip bg={who === 'Frisco' ? C.amber : C.sand} size={28}>{who === 'Frisco' ? 'Frisco Installaties' : who}</Chip>
            </div>
          </div>
        );
      })}
      <Pop at={F('D2c', 8.0)} style={{ left: 820, top: 640 }}><div style={{ fontFamily: SANS, fontSize: 26, color: C.mute }}>bekend uit kaderclip C</div></Pop>
      <Banner at={F('D2f', 1.5)} top={730} size={42}>Een maatregel zonder rol is <span style={{ color: C.amber }}>een wens</span>.</Banner>
    </AbsoluteFill>
  );
};

/* ---------- D3: the order agent and its services ---------- */
const SERVICES = [
  ['n8n', 'workflow', 'flow', 360, 0.0],
  ['Taalmodel-API', 'externe aanbieder schrijft antwoorden', 'brain', 1460, 2.6],
  ['Vectordatabase', 'productinformatie', 'db', 360, 6.3],
  ['Hosting', 'server', 'server', 1460, 9.4],
];
const Agent = () => {
  const frame = useCurrentFrame();
  const cx = 960, cy = 520;
  const pos = (i) => ({ x: SERVICES[i][3], y: i < 2 ? 330 : 700 });
  const lit = (i) => interpolate(frame, [F('D3b', SERVICES[i][4]), F('D3b', SERVICES[i][4] + 0.6)], [0, 1], clamp);
  const flow = interpolate(frame, [F('D3d', 3.0), F('D3d', 7.5)], [0, 1], clamp);
  const data = ['Naam', 'Adres', 'Foto koelinstallatie'];
  return (
    <AbsoluteFill style={{ background: C.light }}>
      <Heading at={F('D3a', 0)} kicker="EEN ORDERAGENT, VAN DICHTBIJ">Het lijkt één systeem. Het zijn er meer.</Heading>
      <svg width="1920" height="1080" style={{ position: 'absolute', left: 0, top: 0 }}>
        {SERVICES.map((s, i) => {
          const p = pos(i); const l = lit(i);
          return <line key={i} x1={cx} y1={cy} x2={p.x} y2={p.y} stroke={mix(l, C.line, C.amber)} strokeWidth={4 + 6 * l} strokeDasharray={l > 0.5 ? '0' : '10 10'} />;
        })}
        {flow > 0 && flow < 1 && SERVICES.map((s, i) => {
          const p = pos(i);
          return [0, 0.33, 0.66].map((o, j) => {
            const q = (flow * 2 + o) % 1;
            return <circle key={i + '-' + j} cx={cx + (p.x - cx) * q} cy={cy + (p.y - cy) * q} r="11" fill={j === 2 ? C.terra : C.green} />;
          });
        })}
      </svg>
      <Pop at={F('D3a', 1.0)} style={{ left: cx - 190, top: cy - 90, width: 380 }}>
        <div style={{ background: C.dark, color: C.light, borderRadius: 24, padding: '24px 28px', textAlign: 'center', boxShadow: '0 18px 40px rgba(0,32,96,.3)' }}>
          <div style={{ fontFamily: SANS, fontWeight: 700, fontSize: 22, letterSpacing: 2, color: C.amber }}>FRISCO INSTALLATIES</div>
          <div style={{ fontFamily: SERIF, fontWeight: 700, fontSize: 44 }}>Orderagent</div>
        </div>
      </Pop>
      {SERVICES.map(([n, d, ic], i) => {
        const p = pos(i); const l = lit(i);
        const docOn = on(frame, 'D3c', 0.4 + i * 0.4);
        return (
          <div key={n} style={{ position: 'absolute', left: p.x - 200, top: p.y - 80, width: 400, opacity: 0.25 + 0.75 * l, transform: `scale(${0.92 + 0.08 * l})` }}>
            <Card style={{ display: 'flex', gap: 20, alignItems: 'center', padding: '18px 24px', border: `3px solid ${mix(l, C.line, C.amber)}` }}>
              <Icon kind={ic} size={70} color={C.dark} />
              <div>
                <div style={{ fontFamily: SANS, fontWeight: 700, fontSize: 32, color: C.ink }}>{n}</div>
                <div style={{ fontFamily: SANS, fontSize: 22, color: C.mute }}>{d}</div>
              </div>
            </Card>
            <div style={{ position: 'absolute', right: -24, top: -30, opacity: docOn ? 1 : 0, transform: `rotate(${docOn ? 8 : 0}deg)` }}>
              <div style={{ background: C.card, border: `2px solid ${C.terra}`, borderRadius: 10, padding: '4px 12px', fontFamily: SANS, fontWeight: 700, fontSize: 20, color: C.terra }}>voorwaarden</div>
            </div>
          </div>
        );
      })}
      <Pop at={F('D3d', 0.3)} style={{ left: 700, top: 660, width: 520 }}>
        <div style={{ background: C.green, color: C.card, borderRadius: '20px 20px 20px 6px', padding: '14px 22px', fontFamily: SANS, fontSize: 26 }}>
          Klant stuurt:
          <div style={{ display: 'flex', gap: 10, marginTop: 8, flexWrap: 'wrap' }}>{data.map((d) => <Chip key={d} bg={C.card} color={C.dark} size={22}>{d}</Chip>)}</div>
        </div>
      </Pop>
      <Pop at={F('D3e', 0.5)} style={{ left: 128, top: 815, width: 1664 }}>
        <div style={{ background: '#F7F0DD', border: `2px solid ${C.amber}`, borderRadius: 16, padding: '12px 26px', fontFamily: SANS, fontWeight: 700, fontSize: 30, color: C.dark }}>
          Teken het in K3: welke gegevens gaan erheen, en waar worden ze opgeslagen?
        </div>
      </Pop>
    </AbsoluteFill>
  );
};

/* ---------- D4: supplier check ---------- */
const QUESTIONS = [
  ['D4b', 'Wat doet de leverancier met onze gegevens? Ook training?'],
  ['D4c', 'Waar staan de gegevens?'],
  ['D4d', 'Wat wordt gelogd, en wie kan daarbij?'],
  ['D4e', 'Wat mag de agent zelf doen, zonder mens?'],
];
const Check = () => {
  const frame = useCurrentFrame();
  const unknown = on(frame, 'D4f', 5.0);
  const toReg = interpolate(frame, [F('D4f', 7.5), F('D4f', 9.5)], [0, 1], clamp);
  return (
    <AbsoluteFill style={{ background: C.light }}>
      <Heading at={F('D4a', 0)} kicker="VOOR ELKE EXTERNE DIENST">De leverancierscheck</Heading>
      <Pop at={F('D4a', 1.2)} style={{ left: 128, top: 250, width: 1060 }}>
        <div style={{ background: C.card, border: `2px solid ${C.line}`, borderRadius: 22, padding: '20px 30px', boxShadow: '0 14px 34px rgba(0,32,96,.10)' }}>
          <div style={{ fontFamily: SANS, fontWeight: 700, fontSize: 22, letterSpacing: 2, color: C.green, marginBottom: 6 }}>K7 · LEVERANCIERSCHECK · TAALMODEL-API</div>
          {QUESTIONS.map(([k, q], i) => {
            const s = interpolate(frame, [F(k, 0.1), F(k, 0.6)], [0, 1], clamp);
            const ans = i === 1 ? (unknown ? 'onbekend' : '') : on(frame, 'D4f', 1.5 + i * 0.5) ? 'ingevuld' : '';
            return (
              <div key={k} style={{ display: 'flex', alignItems: 'center', gap: 22, padding: '14px 0', borderTop: i ? `2px solid ${C.line}` : 'none', opacity: s, transform: `translateX(${(1 - s) * 30}px)` }}>
                <span style={{ fontFamily: SERIF, fontWeight: 700, fontSize: 48, color: C.amber, width: 40 }}>{i + 1}</span>
                <span style={{ flex: 1, fontFamily: SANS, fontSize: 31, color: C.ink, lineHeight: 1.25 }}>{q}</span>
                <span style={{ width: 160, textAlign: 'center', fontFamily: SANS, fontWeight: 700, fontSize: 24, padding: '6px 0', borderRadius: 10, color: ans === 'onbekend' ? C.card : C.green, background: ans === 'onbekend' ? C.terra : ans ? '#E2F1E8' : 'transparent' }}>{ans}</span>
              </div>
            );
          })}
        </div>
      </Pop>
      <Pop at={F('D4f', 0.4)} style={{ left: 1260, top: 260, width: 530 }}>
        <Card style={{ display: 'flex', gap: 18, alignItems: 'center' }}>
          <Icon kind="doc" size={70} color={C.dark} />
          <div style={{ fontFamily: SANS, fontSize: 27, color: C.ink, lineHeight: 1.3 }}>Antwoord in de voorwaarden of de accountinstellingen</div>
        </Card>
      </Pop>
      <div style={{ position: 'absolute', left: 1260, top: 470, width: 530, opacity: toReg }}>
        <div style={{ fontFamily: SANS, fontWeight: 700, fontSize: 40, color: C.terra, textAlign: 'center' }}>↓</div>
        <div style={{ background: C.dark, borderRadius: 20, padding: '20px 26px', color: C.light }}>
          <div style={{ fontFamily: SANS, fontWeight: 700, fontSize: 22, letterSpacing: 2, color: C.amber }}>RISICOREGISTER</div>
          <div style={{ fontFamily: SANS, fontSize: 28, marginTop: 6 }}>R-xx: onbekend waar klantgegevens staan</div>
        </div>
      </div>
      <Banner at={F('D4f', 7.0)} top={760} size={38}>Onbekend is geen fout in je rapport. <span style={{ color: C.amber }}>Het is een risico.</span></Banner>
    </AbsoluteFill>
  );
};

/* ---------- D5: what an agent may do ---------- */
const ACTIONS = ['Offerte maken', 'Mail sturen', 'Monteur inplannen', 'Bestelling plaatsen'];
const AgentLimits = () => {
  const frame = useCurrentFrame();
  const auto = interpolate(frame, [F('D5c', 0), F('D5c', 3.0)], [0.2, 0.95], clamp);
  const lanes = on(frame, 'D5d', 0);
  const logs = ['10:02 offerte #1042 opgesteld', '10:03 medewerker keurt goed', '10:05 mail verstuurd', '10:09 bestelling wacht op bevestiging'];
  const contract = on(frame, 'D5g', 1.5);
  const stay = on(frame, 'D5g', 7.0);
  return (
    <AbsoluteFill style={{ background: C.light }}>
      <Heading at={F('D5a', 0)} kicker="HET BIJZONDERE VAN EEN AI-AGENT">Een chatbot antwoordt. Een agent doet.</Heading>
      {!lanes && (
        <>
          <Pop at={F('D5a', 1.5)} style={{ left: 128, top: 280, width: 560 }}>
            <Card><div style={{ fontFamily: SANS, fontWeight: 700, fontSize: 24, color: C.mute }}>CHATBOT</div>
              <div style={{ marginTop: 12, background: '#EAF0F8', borderRadius: '18px 18px 18px 6px', padding: '14px 20px', fontFamily: SANS, fontSize: 28 }}>De installatie kost ongeveer…</div></Card>
          </Pop>
          <Pop at={F('D5a', 3.2)} style={{ left: 760, top: 280, width: 1030 }}>
            <Card><div style={{ fontFamily: SANS, fontWeight: 700, fontSize: 24, color: C.terra }}>AGENT</div>
              <div style={{ display: 'flex', flexWrap: 'wrap', gap: 14, marginTop: 14 }}>
                {ACTIONS.map((a, i) => <div key={a} style={{ opacity: on(frame, 'D5b', 0.4 + i * 1.2) ? 1 : 0.15 }}><Chip bg={i === 3 ? C.terra : C.green} color={C.card} size={28}>{a}</Chip></div>)}
              </div></Card>
          </Pop>
          <Pop at={F('D5c', 0)} style={{ left: 128, top: 560, width: 1660 }}>
            <div style={{ fontFamily: SANS, fontWeight: 700, fontSize: 28, color: C.ink, marginBottom: 12 }}>Hoe meer de agent zelf mag…</div>
            <div style={{ height: 30, borderRadius: 15, background: C.line, overflow: 'hidden' }}><div style={{ width: `${auto * 100}%`, height: '100%', background: `linear-gradient(90deg, ${C.green}, ${C.terra})` }} /></div>
            <div style={{ fontFamily: SANS, fontWeight: 700, fontSize: 28, color: C.terra, marginTop: 12, textAlign: 'right', opacity: auto > 0.8 ? 1 : 0 }}>…hoe belangrijker de grenzen</div>
          </Pop>
        </>
      )}
      {lanes && !contract && (
        <>
          <Pop at={F('D5d', 0.2)} style={{ left: 128, top: 270, width: 800 }}>
            <Card style={{ borderLeft: `10px solid ${C.green}` }}>
              <div style={{ display: 'flex', gap: 20, alignItems: 'center' }}><Icon kind="eye" size={64} color={C.green} />
                <div><div style={{ fontFamily: SERIF, fontWeight: 700, fontSize: 38, color: C.green }}>Offerte opstellen</div>
                  <div style={{ fontFamily: SANS, fontSize: 27, color: C.mute }}>mag de agent zelf, een medewerker kijkt mee</div></div></div>
            </Card>
          </Pop>
          <Pop at={F('D5d', 5.5)} style={{ left: 990, top: 270, width: 800 }}>
            <Card style={{ borderLeft: `10px solid ${C.terra}` }}>
              <div style={{ display: 'flex', gap: 20, alignItems: 'center' }}><Icon kind="pen" size={64} color={C.terra} />
                <div><div style={{ fontFamily: SERIF, fontWeight: 700, fontSize: 38, color: C.terra }}>Bestellen of betalen</div>
                  <div style={{ fontFamily: SANS, fontSize: 27, color: C.mute }}>daar tekent een mens</div></div></div>
            </Card>
          </Pop>
          <Pop at={F('D5e', 0.3)} style={{ left: 128, top: 490, width: 800 }}>
            <Card>
              <div style={{ fontFamily: SANS, fontWeight: 700, fontSize: 22, letterSpacing: 2, color: C.dark }}>LEG VAST</div>
              {['Welke acties na bevestiging door een mens', 'Tot welk bedrag', 'Voor welke klanten'].map((t, i) => (
                <div key={t} style={{ fontFamily: SANS, fontSize: 29, color: C.ink, marginTop: 10, opacity: on(frame, 'D5e', 1.0 + i * 1.6) ? 1 : 0 }}>✓ {t}</div>
              ))}
            </Card>
          </Pop>
          <Pop at={F('D5f', 0.2)} style={{ left: 990, top: 490, width: 800 }}>
            <div style={{ background: C.dark, borderRadius: 20, padding: '20px 26px', fontFamily: "'Courier New', monospace", fontSize: 25, color: '#C9D6E8' }}>
              <div style={{ fontFamily: SANS, fontWeight: 700, fontSize: 22, letterSpacing: 2, color: C.amber, marginBottom: 8 }}>LOGBOEK VAN DE AGENT</div>
              {logs.map((l, i) => <div key={l} style={{ opacity: on(frame, 'D5f', 0.8 + i * 0.9) ? 1 : 0, marginTop: 4 }}>{l}</div>)}
            </div>
          </Pop>
        </>
      )}
      {contract && (
        <>
          <Pop at={F('D5g', 1.5)} style={{ left: 128, top: 290, width: 520 }}>
            <Card style={{ display: 'flex', gap: 18, alignItems: 'center' }}><Icon kind="doc" size={80} />
              <div style={{ fontFamily: SERIF, fontWeight: 700, fontSize: 36, color: C.dark }}>Contract met de leverancier</div></Card>
          </Pop>
          <Pop at={F('D5g', 3.0)} style={{ left: 760, top: 290, width: 1030 }}>
            <Card>
              <div style={{ fontFamily: SANS, fontSize: 30, color: C.ink }}>Een deel van de <b>gevolgen</b> → leverancier</div>
              <div style={{ fontFamily: SANS, fontSize: 30, color: C.terra, marginTop: 14, opacity: stay ? 1 : 0 }}>De <b>schade voor de klant</b> blijft</div>
            </Card>
          </Pop>
          <Banner at={F('D5g', 8.5)} top={600} size={42}>Wie de agent inzet, <span style={{ color: C.amber }}>blijft verantwoordelijk</span>.</Banner>
        </>
      )}
    </AbsoluteFill>
  );
};

/* ---------- D6: Kader column ---------- */
const KROWS = [
  ['Bestelling boven een vast bedrag: eerst bevestiging door een medewerker', 'AI-verordening, art. 14 (menselijk toezicht)', 'D6b', 'plicht bij hoog risico; hier goed ontwerp'],
  ['Leverancierscheck voor elke externe dienst', 'ISO/IEC 42001 · derde partijen', 'D6c', ''],
  ['Elke actie van de agent wordt gelogd', 'ISO/IEC 42001 · levenscyclus', 'D6c', ''],
];
const Kader = () => {
  const frame = useCurrentFrame();
  return (
    <AbsoluteFill style={{ background: C.light }}>
      <Heading at={F('D6a', 0)} kicker="K7 · DE KOLOM KADER">Elke maatregel een verwijzing</Heading>
      <Pop at={F('D6a', 1.0)} style={{ left: 128, top: 260, width: 1664 }}>
        <div style={{ background: C.card, border: `2px solid ${C.line}`, borderRadius: 20, overflow: 'hidden' }}>
          <div style={{ display: 'grid', gridTemplateColumns: '1.25fr 1fr', background: C.sand, fontFamily: SANS, fontWeight: 700, fontSize: 26, color: C.dark, padding: '14px 26px' }}><span>Maatregel</span><span>Kader</span></div>
          {KROWS.map(([m, k, key, note], i) => {
            const off = key === 'D6c' ? (i === 1 ? 0.3 : 5.0) : 0.3;
            const show = on(frame, key, off);
            const kOn = on(frame, key, off + 1.4);
            return (
              <div key={m} style={{ display: 'grid', gridTemplateColumns: '1.25fr 1fr', padding: '18px 26px', borderTop: `2px solid ${C.line}`, fontFamily: SANS, fontSize: 28, color: C.ink, opacity: show ? 1 : 0.15 }}>
                <span style={{ paddingRight: 24 }}>{m}</span>
                <span style={{ opacity: kOn ? 1 : 0 }}><Chip bg="#E2F1E8" color={C.green} size={25}>{k}</Chip>
                  {note && <div style={{ fontFamily: SANS, fontSize: 22, color: C.mute, marginTop: 8, opacity: on(frame, 'D6b', 7.0) ? 1 : 0 }}>{note}</div>}</span>
              </div>
            );
          })}
        </div>
      </Pop>
      <Banner at={F('D6d', 0.3)} top={770} size={40}>Zo komt een maatregel niet <span style={{ color: C.amber }}>uit de lucht vallen</span>.</Banner>
    </AbsoluteFill>
  );
};

/* ---------- D7: now you ---------- */
const Now = () => (
  <AbsoluteFill style={{ background: C.light }}>
    <Heading at={F('D7a', 0)}>Nu jij, met je groep</Heading>
    {[['D7b', 'K3: zet bij elke externe dienst wat erheen gaat en waar het staat'], ['D7c', 'K7: vul voor elke dienst de leverancierscheck in'], ['D7d', 'K7: geef elke maatregel een verwijzing in de kolom Kader']].map(([k, t], i) => (
      <Pop key={k} at={F(k, 0.3)} style={{ left: 128, top: 250 + i * 160, width: 1664 }}>
        <Card style={{ display: 'flex', gap: 30, alignItems: 'center', padding: '22px 36px' }}>
          <span style={{ fontFamily: SERIF, fontWeight: 700, fontSize: 64, color: C.green, width: 50 }}>{i + 1}</span>
          <span style={{ fontFamily: SANS, fontWeight: 600, fontSize: 36, color: C.ink }}>{t}</span>
        </Card>
      </Pop>
    ))}
    <Pop at={F('D7e', 0.5)} style={{ left: 128, top: 760 }}>
      <div style={{ fontFamily: SANS, fontWeight: 700, fontSize: 30, color: C.green }}>Bespreek met je groep: welke stap mag jullie agent zelf zetten, zonder mens?</div>
    </Pop>
  </AbsoluteFill>
);

export const KaderD = () => (
  <ClipShell timing={timing} scenes={[
    ['D0a', <Title />], ['D0b', <Intro />], ['D1a', <Phases />], ['D2a', <Roles />], ['D3a', <Agent />], ['D4a', <Check />],
    ['DQ1', <Quiz8 tm={tm} n={1} q="DQ1" a="DQ1b" optAt={0.55}
      question="Een groep laat een taalmodel-API e-mails van klanten samenvatten. Welke vraag uit de leverancierscheck is hier het belangrijkst?"
      options={['A. Wat doet de leverancier met de gegevens, ook voor training?', 'B. Wat mag de agent zelf doen, zonder mens?', 'C. Wat wordt gelogd?']} good={0}
      note="De e-mails bevatten persoonsgegevens. Waar ze staan, volgt direct daarna." />],
    ['D5a', <AgentLimits />],
    ['DQ2', <Quiz8 tm={tm} n={2} q="DQ2" a="DQ2b" optAt={0.6}
      question="Een orderagent mag zelf bestellingen plaatsen, tot elk bedrag. Welke maatregelen passen het best?"
      options={['A. Niets: de agent werkt snel en goedkoop', 'B. Een grens met bevestiging door een medewerker, en logging van elke actie', 'C. Alleen een goed contract met de leverancier']} good={1} />],
    ['D6a', <Kader />], ['D7a', <Now />],
  ]} />
);
