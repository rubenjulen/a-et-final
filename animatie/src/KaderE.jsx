import React from 'react';
import { AbsoluteFill, useCurrentFrame, interpolate } from 'remotion';
import timing from './timing_kE.json';
import {
  C, SERIF, SANS, FPS, clamp, makeF, useSpr, mix, Pop, Card, Banner, Heading,
  Quiz8, TitleScene, ClipShell, Person,
} from './wk3kit';

const tm = makeF(timing);
const { F } = tm;

const Chip = ({ children, bg = C.dark, fg = C.light, size = 28, style = {} }) => (
  <span style={{ display: 'inline-block', background: bg, color: fg, fontFamily: SANS, fontWeight: 700, fontSize: size, padding: '10px 22px', borderRadius: 40, ...style }}>{children}</span>
);

/* ---------- E0: title ---------- */
const Intro = () => {
  const frame = useCurrentFrame();
  const leave = interpolate(frame, [F('E0.3', 0.4), F('E0.3', 2.6)], [0, 1], clamp);
  return (
    <TitleScene at={F('E0.1', 0)} kicker="KADERCLIP E · WEEK 8" title="Van maatregel naar managementsysteem">
      <Pop at={F('E0.4', 0.6)} style={{ left: 140, top: 600 }}>
        <Chip bg={C.amber} fg={C.dark} size={34}>ISO/IEC 42001</Chip>
      </Pop>
      <div style={{ position: 'absolute', left: 1240, top: 300, width: 560, height: 420 }}>
        {[0, 1, 2].map((i) => (
          <div key={i} style={{ position: 'absolute', left: 40 + i * 150 + leave * (520 + i * 60), top: 120, opacity: 1 - leave }}>
            <Person size={130} frame={frame + i * 9} body={[C.green, C.terra, C.amber][i]} />
            <div style={{ fontFamily: SANS, fontSize: 20, color: C.sand, textAlign: 'center' }}>bouwteam</div>
          </div>
        ))}
        <Pop at={F('E0.3', 1.2)} style={{ left: 0, top: 20, width: 560 }}>
          <div style={{ background: C.card, borderRadius: 22, padding: '22px 28px', fontFamily: SERIF, fontWeight: 600, fontSize: 34, color: C.ink, lineHeight: 1.2 }}>
            Hoe houden we dit vol, ook als het team weg is?
          </div>
        </Pop>
      </div>
    </TitleScene>
  );
};

/* ---------- E1: what is the norm ---------- */
const Norm = () => {
  const frame = useCurrentFrame();
  const cross = interpolate(frame, [F('E1.2', 0.3), F('E1.2', 1.0)], [0, 1], clamp);
  const pillars = ['beleid', 'rollen', "risico's", 'controle', 'verbetering'];
  const certOn = frame >= F('E1.4', 0);
  return (
    <AbsoluteFill style={{ background: C.light }}>
      <Heading at={F('E1.1', 0)} kicker="WAT IS HET?">Een norm voor het besturen van AI</Heading>
      {/* document */}
      <Pop at={F('E1.1', 0.6)} style={{ left: 128, top: 280 }}>
        <div style={{ width: 340, height: 440, background: C.card, border: `3px solid ${C.dark}`, borderRadius: 14, padding: 30, boxShadow: '0 18px 40px rgba(18,49,42,.14)' }}>
          <div style={{ fontFamily: SANS, fontWeight: 700, fontSize: 22, color: C.terra, letterSpacing: 2 }}>NORM · 2023</div>
          <div style={{ fontFamily: SERIF, fontWeight: 700, fontSize: 48, color: C.dark, marginTop: 10 }}>ISO/IEC 42001</div>
          <div style={{ fontFamily: SANS, fontSize: 26, color: C.mute, marginTop: 8 }}>AI-managementsysteem</div>
          {[0, 1, 2, 3, 4].map((i) => <div key={i} style={{ height: 14, background: C.sand, borderRadius: 7, marginTop: i ? 16 : 40, width: `${90 - i * 9}%` }} />)}
          {frame >= F('E1.7', 0) && (
            <Pop at={F('E1.7', 0.2)} style={{ left: 200, top: 300 }}>
              <div style={{ background: C.terra, color: C.card, fontFamily: SANS, fontWeight: 700, fontSize: 22, padding: '8px 16px', borderRadius: 10, transform: 'rotate(-6deg)' }}>betaald</div>
            </Pop>
          )}
        </div>
      </Pop>
      {/* not one model */}
      <Pop at={F('E1.2', 0)} style={{ left: 560, top: 300 }}>
        <div style={{ position: 'relative' }}>
          <Card style={{ width: 300, padding: '20px 26px' }}>
            <div style={{ fontFamily: SANS, fontSize: 24, color: C.mute }}>checklist voor</div>
            <div style={{ fontFamily: SERIF, fontWeight: 700, fontSize: 38, color: C.ink }}>één model</div>
          </Card>
          <svg width="360" height="130" style={{ position: 'absolute', left: -10, top: 0 }}>
            <line x1="10" y1="120" x2={10 + 340 * cross} y2={120 - 110 * cross} stroke={C.terra} strokeWidth="10" strokeLinecap="round" />
          </svg>
        </div>
      </Pop>
      {/* pillars: the organisation */}
      <Pop at={F('E1.3', 0)} style={{ left: 560, top: 470, width: 620 }}>
        <div style={{ fontFamily: SANS, fontWeight: 700, fontSize: 26, color: C.green, marginBottom: 12 }}>maar afspraken voor de hele organisatie</div>
        <div style={{ display: 'flex', flexWrap: 'wrap', gap: 14 }}>
          {pillars.map((p, i) => (
            <Pop key={p} at={F('E1.3', 1.2 + i * 0.7)} style={{ position: 'relative' }}>
              <Chip bg={C.green} size={30}>{p}</Chip>
            </Pop>
          ))}
        </div>
      </Pop>
      {/* certificates */}
      {certOn && (
        <div style={{ position: 'absolute', left: 1260, top: 270, width: 560 }}>
          {[['ISO 9001', 'kwaliteit'], ['ISO 27001', 'informatiebeveiliging'], ['ISO/IEC 42001', 'AI']].map(([n, w], i) => (
            <Pop key={n} at={F('E1.4', 0.6 + i * 1.0)} style={{ position: 'relative', marginBottom: 18 }}>
              <div style={{ display: 'flex', alignItems: 'center', gap: 20, background: i === 2 ? C.dark : C.card, border: `2px solid ${i === 2 ? C.dark : C.line}`, borderRadius: 18, padding: '18px 24px' }}>
                <svg width="56" height="56" viewBox="0 0 56 56"><circle cx="28" cy="28" r="24" fill={C.amber} /><path d="M17 29 L25 37 L40 20" stroke={C.dark} strokeWidth="5" fill="none" strokeLinecap="round" /></svg>
                <div>
                  <div style={{ fontFamily: SERIF, fontWeight: 700, fontSize: 32, color: i === 2 ? C.light : C.ink }}>{n}</div>
                  <div style={{ fontFamily: SANS, fontSize: 22, color: i === 2 ? C.sand : C.mute }}>{w}</div>
                </div>
              </div>
            </Pop>
          ))}
          <Pop at={F('E1.5', 0.2)} style={{ position: 'relative', marginTop: 6 }}>
            <div style={{ display: 'flex', alignItems: 'center', gap: 16 }}>
              <Person size={90} frame={frame} body={C.dark} glasses />
              <div style={{ fontFamily: SANS, fontSize: 26, color: C.ink, lineHeight: 1.3 }}>klant of toezichthouder:<br /><b>"hier is AI geregeld"</b></div>
            </div>
          </Pop>
        </div>
      )}
      <Banner at={F('E1.8', 0.1)} top={790} size={40}>Lees de tekst niet. Ken de <span style={{ color: C.amber }}>opbouw</span>, en waar jullie werk past.</Banner>
    </AbsoluteFill>
  );
};

/* ---------- E2: clauses 4–10 as steps ---------- */
const CLAUSES = [
  ['4', 'Context', 'E2.2'], ['5', 'Leiderschap', 'E2.3'], ['6', 'Planning', 'E2.4'], ['7', 'Ondersteuning', 'E2.6'],
  ['8', 'Uitvoering', 'E2.7'], ['9', 'Evaluatie', 'E2.8'], ['10', 'Verbetering', 'E2.9'],
];
const Steps = () => {
  const frame = useCurrentFrame();
  return (
    <AbsoluteFill style={{ background: C.light }}>
      <Heading at={F('E2.1', 0)} kicker="DE OPBOUW">Zeven hoofdstukken: clausule 4 tot en met 10</Heading>
      {CLAUSES.map(([n, t, k], i) => {
        const on = frame >= F(k, 0);
        const s = interpolate(frame, [F('E2.1', 0.6 + i * 0.25), F('E2.1', 1.2 + i * 0.25)], [0, 1], clamp);
        const h = 110 + i * 62;
        return (
          <div key={n} style={{ position: 'absolute', left: 128 + i * 236, top: 840 - h * s, width: 222, height: h * s, overflow: 'hidden',
            background: on ? (n === '6' ? C.terra : C.dark) : C.sand, borderRadius: '16px 16px 0 0', transition: 'none' }}>
            <div style={{ padding: '16px 18px' }}>
              <div style={{ fontFamily: SERIF, fontWeight: 700, fontSize: 56, color: on ? C.amber : C.mute }}>{n}</div>
              <div style={{ fontFamily: SANS, fontWeight: 700, fontSize: 25, color: on ? C.light : C.mute }}>{t}</div>
            </div>
          </div>
        );
      })}
      <Pop at={F('E2.4', 3.2)} style={{ left: 600, top: 250, width: 560 }}>
        <Card style={{ borderColor: C.terra }}>
          <div style={{ fontFamily: SANS, fontWeight: 700, fontSize: 22, color: C.terra, letterSpacing: 1 }}>CLAUSULE 6.1.4</div>
          <div style={{ fontFamily: SERIF, fontWeight: 700, fontSize: 36, color: C.ink }}>Impactbeoordeling</div>
          {frame >= F('E2.5', 0) && <Pop at={F('E2.5', 0.3)} style={{ position: 'relative' }}><div style={{ fontFamily: SANS, fontSize: 28, color: C.green, fontWeight: 700, marginTop: 8 }}>= K2 + nulmeting: jullie AI-impactbeoordeling</div></Pop>}
        </Card>
      </Pop>
      <svg width="1920" height="1080" style={{ position: 'absolute', left: 0, top: 0, pointerEvents: 'none' }}>
        <line x1="128" y1="842" x2="1792" y2="842" stroke={C.dark} strokeWidth="4" />
      </svg>
    </AbsoluteFill>
  );
};

/* ---------- E3: PDCA wheel ---------- */
const Q = [
  ['Plan', C.dark, 'E3.2', ['K2', 'K4', 'K6', 'K7']],
  ['Do', C.green, 'E3.3', ['inbouwen via A-AI2']],
  ['Check', C.amber, 'E3.4', ['hertest', 'K8', 'Design Review']],
  ['Act', C.terra, 'E3.5', ['corrigeren', 'verbeteren']],
];
const Wheel = ({ frame, size = 560, rot = 0, active = -1, labels = true }) => {
  const r = size / 2 - 10, c = size / 2;
  return (
    <svg width={size} height={size} viewBox={`0 0 ${size} ${size}`}>
      <g transform={`rotate(${rot} ${c} ${c})`}>
        {Q.map(([t, col], i) => {
          const a0 = -Math.PI / 2 + i * Math.PI / 2 + 0.03, a1 = a0 + Math.PI / 2 - 0.06;
          const p = `M${c} ${c} L${c + r * Math.cos(a0)} ${c + r * Math.sin(a0)} A${r} ${r} 0 0 1 ${c + r * Math.cos(a1)} ${c + r * Math.sin(a1)} Z`;
          return <path key={t} d={p} fill={col} opacity={active < 0 || active === i ? 1 : 0.35} />;
        })}
        <circle cx={c} cy={c} r={r * 0.36} fill={C.light} />
        {labels && Q.map(([t], i) => {
          const am = -Math.PI / 2 + i * Math.PI / 2 + Math.PI / 4;
          return <text key={t} x={c + r * 0.68 * Math.cos(am)} y={c + r * 0.68 * Math.sin(am) + 14} textAnchor="middle" fontFamily={SERIF} fontWeight="700" fontSize={size / 12} fill={i === 2 ? C.dark : C.light} transform={`rotate(${-rot} ${c + r * 0.68 * Math.cos(am)} ${c + r * 0.68 * Math.sin(am)})`}>{t}</text>;
        })}
      </g>
    </svg>
  );
};
const Cycle = () => {
  const frame = useCurrentFrame();
  const s = useSpr(F('E3.1', 0.2));
  const spin = interpolate(frame, [F('E3.6', 0), F('E3.6', 3.0)], [0, 360], { ...clamp });
  let active = -1;
  Q.forEach((q, i) => { if (frame >= F(q[2], 0) && frame < F('E3.6', 0)) active = i; });
  return (
    <AbsoluteFill style={{ background: C.light }}>
      <Heading at={F('E3.1', 0)} kicker="SAMEN EEN CIRKEL">Plan · do · check · act</Heading>
      <div style={{ position: 'absolute', left: 150, top: 250, transform: `scale(${0.6 + 0.4 * s})`, transformOrigin: '280px 280px', opacity: s }}>
        <Wheel frame={frame} active={active} rot={spin} />
      </div>
      {/* arrow around */}
      {frame >= F('E3.6', 0) && (
        <Pop at={F('E3.6', 0.2)} style={{ left: 150, top: 830, width: 560 }}>
          <div style={{ textAlign: 'center', fontFamily: SERIF, fontWeight: 700, fontSize: 40, color: C.terra }}>↻ opnieuw, ook na de livegang</div>
        </Pop>
      )}
      <div style={{ position: 'absolute', left: 820, top: 250, width: 980 }}>
        {Q.map(([t, col, k, items], i) => (
          <Pop key={t} at={F(k, 0.2)} style={{ position: 'relative', marginBottom: 20 }}>
            <div style={{ display: 'flex', alignItems: 'center', gap: 22, background: C.card, border: `3px solid ${active === i ? col : C.line}`, borderRadius: 20, padding: '16px 24px' }}>
              <div style={{ width: 150, fontFamily: SERIF, fontWeight: 700, fontSize: 40, color: col === C.amber ? '#A87A12' : col }}>{t}</div>
              <div style={{ display: 'flex', flexWrap: 'wrap', gap: 10 }}>
                {items.map((it, j) => (
                  <Pop key={it} at={F(k, 1.0 + j * 0.6)} style={{ position: 'relative' }}>
                    <Chip bg={col} fg={col === C.amber ? C.dark : C.light} size={26}>{it}</Chip>
                  </Pop>
                ))}
              </div>
            </div>
          </Pop>
        ))}
      </div>
    </AbsoluteFill>
  );
};

/* ---------- E4: Annex A ---------- */
const ANNEX = [
  ['A.2', 'Beleid rond AI'], ['A.3', 'Interne organisatie'], ['A.4', 'Middelen'], ['A.5', 'Impactbeoordeling'],
  ['A.6', 'Levenscyclus'], ['A.7', 'Data'], ['A.8', 'Informatie voor belanghebbenden'], ['A.9', 'Gebruik van AI'], ['A.10', 'Derde partijen'],
];
const HL = { 'A.2': 0.6, 'A.5': 2.2, 'A.6': 3.6, 'A.8': 5.0, 'A.10': 7.2 };
const Annex = () => {
  const frame = useCurrentFrame();
  const chosen = ['A.2', 'A.5', 'A.6', 'A.8', 'A.10'];
  const flow = interpolate(frame, [F('E4.5', 1.0), F('E4.5', 3.0)], [0, 1], clamp);
  return (
    <AbsoluteFill style={{ background: C.light }}>
      <Heading at={F('E4.1', 0)} kicker="ANNEX A">Een keuzelijst: 38 maatregelen in 9 gebieden</Heading>
      <div style={{ position: 'absolute', left: 128, top: 250, width: 760 }}>
        {ANNEX.map(([c, t], i) => {
          const hl = HL[c] !== undefined && frame >= F('E4.2', HL[c]);
          const tick = frame >= F('E4.3', 0.6 + i * 0.15) && chosen.includes(c);
          const isA10 = c === 'A.10' && frame >= F('E4.6', 0);
          return (
            <Pop key={c} at={F('E4.1', 0.8 + i * 0.18)} style={{ position: 'relative', marginBottom: 8 }}>
              <div style={{ display: 'flex', alignItems: 'center', gap: 18, background: isA10 ? C.dark : hl ? '#F4EAD3' : C.card, border: `2px solid ${hl ? C.amber : C.line}`, borderRadius: 14, padding: '9px 18px' }}>
                <div style={{ width: 34, height: 34, borderRadius: 8, border: `3px solid ${C.green}`, background: tick ? C.green : 'transparent', display: 'flex', alignItems: 'center', justifyContent: 'center', color: C.card, fontWeight: 700, fontSize: 24 }}>{tick ? '✓' : ''}</div>
                <div style={{ width: 80, fontFamily: SANS, fontWeight: 700, fontSize: 26, color: isA10 ? C.amber : C.terra }}>{c}</div>
                <div style={{ fontFamily: SANS, fontSize: 27, color: isA10 ? C.light : C.ink }}>{t}</div>
              </div>
            </Pop>
          );
        })}
      </div>
      <Pop at={F('E4.3', 2.2)} style={{ left: 940, top: 250, width: 850 }}>
        <div style={{ fontFamily: SERIF, fontWeight: 600, fontSize: 38, color: C.ink, lineHeight: 1.2 }}>Kies wat past bij je risico's, <span style={{ color: C.terra }}>en leg uit waarom</span>.</div>
      </Pop>
      {/* K7 row with Kader column */}
      <Pop at={F('E4.4', 0.3)} style={{ left: 940, top: 380, width: 850 }}>
        <div style={{ background: C.card, border: `2px solid ${C.line}`, borderRadius: 16, overflow: 'hidden', fontFamily: SANS, fontSize: 24 }}>
          <div style={{ display: 'flex', background: C.sand, fontWeight: 700, color: C.dark }}>
            {['K7 · maatregel', 'eigenaar', 'Kader'].map((h, i) => <div key={h} style={{ padding: '10px 16px', width: [420, 190, 240][i], background: i === 2 ? '#F4EAD3' : 'transparent' }}>{h}</div>)}
          </div>
          <div style={{ display: 'flex', color: C.ink }}>
            {['Leverancierscheck taalmodel-API', 'IT-beheer', frame >= F('E4.6', 0.4) ? 'ISO/IEC 42001 A.10' : '…'].map((h, i) => <div key={i} style={{ padding: '12px 16px', width: [420, 190, 240][i], fontWeight: i === 2 ? 700 : 400, color: i === 2 ? C.green : C.ink }}>{h}</div>)}
          </div>
        </div>
      </Pop>
      {/* Frisco agent schema */}
      <Pop at={F('E4.5', 0.2)} style={{ left: 940, top: 540, width: 850 }}>
        <div style={{ position: 'relative', height: 220 }}>
          <div style={{ position: 'absolute', left: 0, top: 50, width: 270 }}><Card style={{ padding: '16px 20px', borderColor: C.green }}>
            <div style={{ fontFamily: SANS, fontSize: 20, color: C.mute }}>Frisco Installaties</div>
            <div style={{ fontFamily: SERIF, fontWeight: 700, fontSize: 30, color: C.ink }}>orderagent</div></Card></div>
          {[['n8n', 0], ['taalmodel (andere partij)', 1]].map(([t, i]) => (
            <div key={t} style={{ position: 'absolute', left: 520, top: 10 + i * 110, width: 330 }}>
              <div style={{ background: C.card, border: `2px dashed ${C.terra}`, borderRadius: 14, padding: '14px 18px', fontFamily: SANS, fontWeight: 700, fontSize: 24, color: C.terra }}>{t}</div>
            </div>
          ))}
          <svg width="850" height="220" style={{ position: 'absolute', left: 0, top: 0 }}>
            {[40, 150].map((y, i) => (
              <line key={i} x1="280" y1="105" x2={280 + 236 * flow} y2={105 + (y - 105) * flow} stroke={C.terra} strokeWidth="5" strokeDasharray="10 8" />
            ))}
          </svg>
        </div>
      </Pop>
      <Banner at={F('E4.6', 0.2)} top={790} size={38}>Leverancierscheck uit week 6 → <span style={{ color: C.amber }}>A.10, derde partijen</span></Banner>
    </AbsoluteFill>
  );
};

/* ---------- E5: what you already do ---------- */
const DONE = [
  ['E5.2', 'week 8', 'Design Review', 'peer-audit · 9.2', C.amber],
  ['E5.3', 'week 4 → 9', 'hertest, zelfde testset', 'check', C.amber],
  ['E5.4', 'week 9', 'beslismemo', 'managementreview · 9.3', C.terra],
  ['E5.6', 'K7', 'eigenaar per maatregel', 'rollen · 5', C.dark],
  ['E5.6', 'week 7', 'AI-beleidsregel', 'AI-beleid · A.2', C.dark],
];
const Already = () => {
  const frame = useCurrentFrame();
  return (
    <AbsoluteFill style={{ background: C.light }}>
      <Heading at={F('E5.1', 0)} kicker="GOED NIEUWS">Jullie doen al veel van wat de norm vraagt</Heading>
      {DONE.map(([k, w, what, iso, col], i) => {
        const off = i === 4 ? 2.6 : 0.2;
        return (
          <Pop key={i} at={F(k, off)} style={{ left: 128, top: 250 + i * 104, width: 1664 }}>
            <div style={{ display: 'flex', alignItems: 'center', gap: 26 }}>
              <div style={{ width: 170, fontFamily: SANS, fontWeight: 700, fontSize: 26, color: C.mute }}>{w}</div>
              <div style={{ width: 640 }}><Card style={{ padding: '16px 24px' }}><span style={{ fontFamily: SERIF, fontWeight: 700, fontSize: 34, color: C.ink }}>{what}</span></Card></div>
              <svg width="120" height="30"><path d="M0 15 H100 M84 3 L104 15 L84 27" stroke={C.green} strokeWidth="5" fill="none" /></svg>
              <Chip bg={col} fg={col === C.amber ? C.dark : C.light} size={30}>{iso}</Chip>
            </div>
          </Pop>
        );
      })}
      <Pop at={F('E5.5', 0.3)} style={{ left: 1330, top: 456 }}>
        <div style={{ background: C.card, border: `2px solid ${C.terra}`, borderRadius: 12, padding: '8px 14px', fontFamily: SANS, fontSize: 22, color: C.terra, fontWeight: 700 }}>+ datum volgende review</div>
      </Pop>
    </AbsoluteFill>
  );
};

/* ---------- E6a: clause 10 incidents ---------- */
const Incident = () => {
  const frame = useCurrentFrame();
  const qs = ['Wat is een incident?', 'Wie meldt het, aan wie?', 'Binnen welke termijn?'];
  const sw = interpolate(frame, [F('E6.3', 0.8), F('E6.3', 1.6)], [0, 1], clamp);
  const wrong = frame >= F('E6.6', 2.2);
  return (
    <AbsoluteFill style={{ background: C.light }}>
      <Heading at={F('E6.1', 0)} kicker="WAT ER NOG BIJ MOET · CLAUSULE 10">Afwijkingen en incidenten</Heading>
      <div style={{ position: 'absolute', left: 128, top: 250, width: 720 }}>
        {qs.map((q, i) => (
          <Pop key={q} at={F('E6.2', 0.3 + i * 1.3)} style={{ position: 'relative', marginBottom: 14 }}>
            <Card style={{ padding: '14px 24px' }}><span style={{ fontFamily: SANS, fontWeight: 700, fontSize: 30, color: C.ink }}>{q}</span></Card>
          </Pop>
        ))}
        <Pop at={F('E6.3', 0.2)} style={{ position: 'relative', marginTop: 10 }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: 22 }}>
            <svg width="120" height="64" viewBox="0 0 120 64">
              <rect x="2" y="2" width="116" height="60" rx="30" fill={mix(sw, C.green, C.terra)} />
              <circle cx={32 + 56 * sw} cy="32" r="24" fill={C.card} />
            </svg>
            <span style={{ fontFamily: SANS, fontWeight: 700, fontSize: 30, color: C.ink }}>Wanneer gaat het uit, en wie beslist?</span>
          </div>
        </Pop>
      </div>
      <Pop at={F('E6.4', 0.2)} style={{ left: 940, top: 250, width: 850 }}>
        <Card style={{ borderColor: C.dark }}>
          <div style={{ fontFamily: SANS, fontWeight: 700, fontSize: 24, color: C.terra, letterSpacing: 1 }}>K8 · TWEE VASTE REGELS</div>
          <div style={{ fontFamily: SERIF, fontWeight: 700, fontSize: 38, color: C.ink, marginTop: 8 }}>1. Incidentroute</div>
          <div style={{ fontFamily: SERIF, fontWeight: 700, fontSize: 38, color: C.ink }}>2. Stopcriterium</div>
          {frame >= F('E6.5', 0) && <Pop at={F('E6.5', 0.2)} style={{ position: 'relative' }}><div style={{ marginTop: 12 }}><Chip bg={C.terra} size={26}>verplicht voor een voldoende</Chip></div></Pop>}
        </Card>
      </Pop>
      {/* Frisco wrong price */}
      <Pop at={F('E6.6', 0.3)} style={{ left: 940, top: 560, width: 850 }}>
        <div style={{ display: 'flex', gap: 20, alignItems: 'flex-start' }}>
          <div style={{ width: 520, background: '#E6EEEA', borderRadius: '20px 20px 20px 6px', padding: '16px 22px', fontFamily: SANS, fontSize: 26, color: C.ink, lineHeight: 1.35 }}>
            <div style={{ fontSize: 20, color: C.mute, fontWeight: 700 }}>Frisco orderagent</div>
            Order #1042 bevestigd: koelinstallatie voor <span style={{ background: wrong ? '#F6D9D1' : 'transparent', color: wrong ? C.terra : C.ink, fontWeight: 700, padding: '0 6px', borderRadius: 6 }}>SRD 4.500</span>
          </div>
          {wrong && <Pop at={F('E6.6', 2.2)} style={{ position: 'relative' }}><div style={{ fontFamily: SANS, fontWeight: 700, fontSize: 26, color: C.terra, lineHeight: 1.3 }}>verkeerde prijs:<br />wie ziet het,<br />wie hoort het?</div></Pop>}
        </div>
      </Pop>
    </AbsoluteFill>
  );
};

/* ---------- E6b: ClaimWacht stop rule ---------- */
const Stop = () => {
  const frame = useCurrentFrame();
  const draw = interpolate(frame, [F('E6.8', 0.2), F('E6.8', 4.5)], [0, 1], clamp);
  const off = frame >= F('E6.8', 5.2);
  const pts = [[0, 120], [1, 112], [2, 125], [3, 108], [4, 60], [5, 48]]; // y in chart px (lower = higher value)
  const W = 760, H = 260, x = (i) => 40 + i * 130;
  const path = pts.map(([i, y], j) => `${j ? 'L' : 'M'}${x(i)} ${y + 20}`).join(' ');
  const len = 900;
  return (
    <AbsoluteFill style={{ background: C.light }}>
      <Heading at={F('E6.7', 0)} kicker="VOORBEELDRAPPORT · TAMARINDE">ClaimWacht: het stopcriterium</Heading>
      <Pop at={F('E6.8', 0)} style={{ left: 128, top: 260 }}>
        <Card style={{ width: W, padding: '20px 24px' }}>
          <div style={{ fontFamily: SANS, fontWeight: 700, fontSize: 24, color: C.mute }}>Indicator 1 · per maand</div>
          <svg width={W - 48} height={H}>
            <line x1="20" y1="90" x2={W - 60} y2="90" stroke={C.terra} strokeWidth="3" strokeDasharray="10 8" />
            <text x={W - 64} y="80" textAnchor="end" fontFamily={SANS} fontSize="20" fill={C.terra} fontWeight="700">grens</text>
            <path d={path} fill="none" stroke={C.dark} strokeWidth="6" strokeDasharray={len} strokeDashoffset={len * (1 - draw)} strokeLinecap="round" strokeLinejoin="round" />
            {draw > 0.95 && [4, 5].map((i) => <circle key={i} cx={x(i)} cy={pts[i][1] + 20} r="12" fill={C.terra} />)}
            {['jan', 'feb', 'mrt', 'apr', 'mei', 'jun'].map((m, i) => <text key={m} x={x(i)} y={H - 6} textAnchor="middle" fontFamily={SANS} fontSize="20" fill={C.mute}>{m}</text>)}
          </svg>
          {draw > 0.95 && <div style={{ fontFamily: SANS, fontWeight: 700, fontSize: 24, color: C.terra }}>twee maanden achter elkaar boven de grens</div>}
        </Card>
      </Pop>
      <Pop at={F('E6.8', 5.0)} style={{ left: 980, top: 260, width: 810 }}>
        <Card style={{ background: off ? C.dark : C.card, borderColor: C.dark }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: 20 }}>
            <svg width="120" height="64" viewBox="0 0 120 64"><rect x="2" y="2" width="116" height="60" rx="30" fill={off ? C.terra : C.green} /><circle cx={off ? 88 : 32} cy="32" r="24" fill={C.card} /></svg>
            <div style={{ fontFamily: SERIF, fontWeight: 700, fontSize: 34, color: off ? C.light : C.ink }}>ClaimWacht uit voor dat kanaal of die regio</div>
          </div>
          <div style={{ fontFamily: SANS, fontSize: 26, color: off ? C.sand : C.mute, marginTop: 12 }}>→ weer steekproefcontrole</div>
        </Card>
      </Pop>
      <Pop at={F('E6.9', 0.2)} style={{ left: 980, top: 520, width: 810 }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: 22 }}>
          <Person size={110} frame={frame} body={C.dark} tie />
          <div><div style={{ fontFamily: SERIF, fontWeight: 700, fontSize: 34, color: C.ink }}>Manager Declaraties beslist</div>
            <div style={{ fontFamily: SANS, fontSize: 26, color: C.mute }}>zonder op de directie te wachten</div></div>
        </div>
      </Pop>
      <Pop at={F('E6.10', 0.2)} style={{ left: 980, top: 700 }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: 22 }}>
          <div style={{ width: 120, background: C.card, border: `3px solid ${C.dark}`, borderRadius: 14, overflow: 'hidden', textAlign: 'center' }}>
            <div style={{ background: C.terra, color: C.card, fontFamily: SANS, fontWeight: 700, fontSize: 22, padding: 4 }}>maart</div>
            <div style={{ fontFamily: SERIF, fontWeight: 700, fontSize: 40, color: C.ink, padding: 6 }}>2028</div>
          </div>
          <div style={{ fontFamily: SERIF, fontWeight: 700, fontSize: 34, color: C.ink }}>volgende managementreview</div>
        </div>
      </Pop>
    </AbsoluteFill>
  );
};

/* ---------- E7: now you ---------- */
const Now = () => {
  const frame = useCurrentFrame();
  const gap = frame >= F('E7.3', 0);
  return (
    <AbsoluteFill style={{ background: C.light }}>
      <Heading at={F('E7.1', 0)}>Nu jij, met je groep</Heading>
      <div style={{ position: 'absolute', left: 128, top: 240 }}>
        <svg width="460" height="460" viewBox="0 0 460 460">
          {Q.map(([t, col], i) => {
            const c = 230, r = 200, a0 = -Math.PI / 2 + i * Math.PI / 2 + 0.05, a1 = a0 + Math.PI / 2 - 0.1;
            const isGap = gap && i === 3;
            const p = `M${c + r * Math.cos(a0)} ${c + r * Math.sin(a0)} A${r} ${r} 0 0 1 ${c + r * Math.cos(a1)} ${c + r * Math.sin(a1)}`;
            const shown = frame >= F('E7.2', 0.5 + i * 0.6);
            return shown ? <path key={t} d={p} fill="none" stroke={isGap ? C.line : col} strokeWidth="34" strokeDasharray={isGap ? '14 14' : 'none'} strokeLinecap="butt" /> : null;
          })}
          {Q.map(([t], i) => {
            const am = -Math.PI / 2 + i * Math.PI / 2 + Math.PI / 4;
            return frame >= F('E7.2', 0.5 + i * 0.6) ? <text key={t} x={230 + 120 * Math.cos(am)} y={230 + 120 * Math.sin(am) + 12} textAnchor="middle" fontFamily={SERIF} fontWeight="700" fontSize="34" fill={C.ink}>{t}</text> : null;
          })}
          {gap && <text x="230" y="244" textAnchor="middle" fontFamily={SANS} fontWeight="700" fontSize="30" fill={C.terra}>gat?</text>}
        </svg>
      </div>
      {[['E7.2', 'Teken de cirkel en zet elke K7-maatregel op zijn plek'], ['E7.3', 'Waar de cirkel open blijft, zit jullie gat'], ['E7.5', 'Donderdag: minicollege · volgende week: K8']].map(([k, t], i) => (
        <Pop key={k} at={F(k, 0.2)} style={{ left: 700, top: 270 + i * 150, width: 1090 }}>
          <Card style={{ display: 'flex', gap: 26, alignItems: 'center', padding: '22px 32px' }}>
            <span style={{ fontFamily: SERIF, fontWeight: 700, fontSize: 56, color: C.green }}>{i + 1}</span>
            <span style={{ fontFamily: SANS, fontWeight: 600, fontSize: 34, color: C.ink, lineHeight: 1.25 }}>{t}</span>
          </Card>
        </Pop>
      ))}
      <Banner at={F('E7.4', 0.1)} top={760} left={700} width={1090} size={38}>Een gat is geen ramp. <span style={{ color: C.amber }}>Een gat dat je niet ziet, wel.</span></Banner>
    </AbsoluteFill>
  );
};

export const KaderE = () => (
  <ClipShell timing={timing} scenes={[
    ['E0.1', <Intro />],
    ['E1.1', <Norm />],
    ['E2.1', <Steps />],
    ['E3.1', <Cycle />],
    ['EQ1', <Quiz8 tm={tm} n={1} q="EQ1" a="EQ1b.1" optAt={0.55} question="Welke stap van plan, do, check en act is in jullie ontwerp het zwakst, en waarom?" options={['Plan', 'Do', 'Check', 'Act']} good={3} />],
    ['E4.1', <Annex />],
    ['E5.1', <Already />],
    ['E6.1', <Incident />],
    ['E6.7', <Stop />],
    ['EQ2', <Quiz8 tm={tm} n={2} q="EQ2" a="EQ2b.1" optAt={0.55} question="Wie bij jullie partner zou de managementreview moeten doen, en hoe vaak?" options={['De bouwer uit A-AI2, één keer bij de livegang', 'Iemand die mag bijsturen of stoppen, met een vast ritme: elk jaar en na een incident']} good={1} />],
    ['E7.1', <Now />],
  ]} />
);
