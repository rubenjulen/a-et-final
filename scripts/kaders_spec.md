# Spec: vijf kaders inbouwen in A-ET (bron: kruistabel https://claude.ai/artifact/JoNqBfntw1E1JuiCBfpK8n)

Geldt voor lesplan en alle weekdocumenten. Gebruik exact deze namen en woorden.

## Uitgangspunt
- Geen vijf losse kaders naast het bestaande kader. Elk kader hangt in een bestaande laag. Studenten houden één kader in vier lagen.
- De vijf certificeringen (CEET, IEEE CertifAIEd, AIGP, AICP, ISO/IEC 42001) gebruikt de docent als toets op dekking. Studenten krijgen ze in week 10 als "verder na de minor"; de module is geen examentraining.
- Geen nieuw instrument, geen nieuw rapporthoofdstuk, geen andere weging, stellingen blijven zoals ze zijn.

## Vier lagen (lesplan §3), aanvulling per laag
| Laag | Bestaand | Erbij |
|---|---|---|
| Wat | 11 beoordelingsdomeinen | IEEE CertifAIEd: vier ontologieën. Transparantie hoort bij domein 6, verantwoording bij domein 2, algoritmische bias bij domein 5, privacy bij domein 4. Drivers en inhibitors als checklist bij de nulmeting |
| Hoe | NIST AI RMF (Govern, Map, Measure, Manage) | ISO/IEC 42001: managementsysteem met plan-do-check-act. AIGP: governance bij ontwikkeling en bij gebruik, inclusief leveranciers en AI-agents |
| Waarom | UNESCO-aanbeveling en vier ethische lenzen | De lenzen krijgen hun theorienaam (CEET): gevolgen (utilitarisme), rechten en plichten (deontologie), rechtvaardigheid (rechtvaardigheidstheorie, Rawls), professionele integriteit (deugdethiek en beroepscodes) |
| Waar | Surinaamse wet, beleid en sector; buitenlandse regels waar relevant | AI-verordening (EU) 2024/1689: risicoklassen (onaanvaardbaar, hoog, beperkt, minimaal), rollen (aanbieder, gebruiksverantwoordelijke), art. 4 AI-geletterdheid, art. 14 menselijk toezicht, art. 27 FRIA, art. 50 transparantie. Blijft vergelijking, en eis bij Europese klanten of data |

## Kaderclips (aparte reeks, clips 1–22 houden hun nummer)
| Clip | Titel | Week | Duur |
|---|---|---|---|
| A | Het kaderlandschap | 1 | 5 min |
| B | IEEE CertifAIEd: transparantie en bias toetsen | 3 | 7 min |
| C | De AI-verordening: risicoklasse en rol | 4 | 8 min |
| D | Governance over de levenscyclus: leveranciers en AI-agents (AIGP) | 6 | 7 min |
| E | ISO/IEC 42001: van maatregel naar managementsysteem | 8 | 7 min |
Inhoud kort:
- A: de vier lagen, waar elk kader hangt, CEET als toets op het geheel, de lenzen met theorienaam.
- B: vier ontologieën; drivers (o.a. weten dat je met AI praat, toegankelijke controle en feedback, biasprofiel bijhouden) en inhibitors (gedrag verhullen, angst voor aansprakelijkheid, bedrijfsgeheim; bij bias: gebrek aan procestransparantie). Bewijs per doel, score 1-5, zoals K4.
- C: indelen in risicoklasse; rollen; Suribank-kredietmodel = hoog risico (bijlage III, punt 5b) met FRIA (art. 27); orderagents A-AI2 meestal beperkt risico met transparantieplicht (art. 50); art. 14 komt terug in clip 18, art. 50 in clip 20.
- D: governance bij ontwikkeling en bij gebruik; rollen; externe diensten (n8n, taalmodel-API, vectordatabase): voorwaarden, waar data staat, logging; wat een AI-agent zelf mag doen.
- E: plan-do-check-act; risicobeoordeling, behandeling en impactbeoordeling (6.1.4); monitoring, interne audit, managementreview (9); corrigerende actie en incidenten (10); Annex A als keuzelijst. Design Review = peer-audit, beslismemo = managementreview.
Clip 13 (week 4) gaat van 7 naar 4 minuten (escaleren kort), zodat week 4 niet zwaarder wordt dan nodig.

## Instrumenten (kleine aanpassingen)
- AI-impactbeoordeling: K2 plus de nulmeting (K4) heten samen "AI-impactbeoordeling". Eén zin: dit is wat de AI-verordening een FRIA noemt (art. 27) en ISO/IEC 42005 een impactbeoordeling. Geen extra werk.
- K3: elke externe dienst (n8n, taalmodel-API, vectordatabase, hosting) krijgt een markering: welke gegevens gaan erheen en waar staan ze.
- K6: bovenaan één regel "EU-risicoklasse en rol": klasse, onderbouwing (artikel of bijlage), rol van de partner (aanbieder of gebruiksverantwoordelijke).
- K7: (1) maatregelentabel krijgt kolom "Kader": AI-verordening (artikel), ISO/IEC 42001 (Annex A-gebied), IEEE CertifAIEd (ontologie) of NIST AI RMF (functie). (2) Leverancierscheck per externe dienst, vier vragen: wat doet de leverancier met onze gegevens (ook training)? waar staan de gegevens? wat wordt gelogd en wie kan erbij? wat mag de agent zelf doen zonder mens? (3) Eén AI-beleidsregel van hoogstens 100 woorden die de partner kan overnemen.
- K8: twee vaste regels: incidentroute (wat is een incident, wie meldt aan wie, binnen welke termijn) en stopcriterium (wanneer gaat het systeem uit of terug naar handwerk, en wie beslist dat).
- Beslismemo = managementreview (ISO/IEC 42001, 9.3): wat werkt, wat niet, besluit, datum van de volgende review.
- K5: per lens ook de theorienaam.

## Lessen
- College 1 (wk1): lenzendia met theorienamen; blok 1:25-1:55 krijgt 5 minuten kaderlandschap.
- Online sessies wk3, wk4, wk6, wk9: 5 van de 20 minuten uitleg over het kader van die week (wk9: ISO-cyclus, incidentroute en stopcriterium).
- College 3 (wk8): minicollege implementatie en monitoring (1:55-2:35) gebruikt de ISO/IEC 42001-cyclus; Design Review wordt benoemd als peer-audit.
- Weekcheck: één kennisvraag per kader in weken 1, 3, 4, 6 en 8 (vervangt geen bestaande vraag als er al vijf zijn: maak er dan één van de vijf).
- Reserve-stelling voor de docent, week 3 (alleen als alternatief): "Een bedrijf mag de werking van zijn AI geheimhouden."

## Rubric
Geen nieuw criterium, geen andere weging. Op niveau goed en excellent van de criteria over risico's (A1 en A2), maatregelen (A2) en monitoring (A2) komt de zin: "herleidbaar naar een erkend kader (AI-verordening, ISO/IEC 42001, IEEE CertifAIEd of NIST AI RMF)".

## Week 10: "Verder na de minor"
Kort blok: CEET (CertNexus), IEEE CertifAIEd, AIGP (IAPP), AICP (EXIN), ISO/IEC 42001 Lead Implementer. Eén regel per certificering wat het toetst. Geen prijzen.

## Bronnen (lesplan)
ISO/IEC 42001:2023; ISO/IEC 42005:2025; ISO/IEC 23894:2023; Verordening (EU) 2024/1689; IEEE CertifAIEd ontologische specificaties (2022); IAPP AIGP Body of Knowledge v2.1 (2026); CertNexus CET-110 blueprint v1.5; EXIN AICP Preparation Guide (2026).

## Stijl
Nederlands, korte zinnen, zelfde toon als bestaande docs. Bestaande tekst die niet geraakt wordt blijft letterlijk staan. Studielast per week bijwerken waar clipminuten staan.
