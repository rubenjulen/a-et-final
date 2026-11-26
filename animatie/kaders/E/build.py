import json
S=[
("E0","Titel: \"Van maatregel naar managementsysteem\". Shanti's dossier en de Frisco-orderagent schuiven als kaarten op tafel; een klok tikt jaren verder, het bouwteam loopt het beeld uit.",[
"Jullie hebben maatregelen ontworpen, en een deel zit al in jullie oplossing.",
"Maar een organisatie wil nog iets weten.",
"Hoe houden we dit vol, ook als het team dat het bouwde allang weg is?",
"Daarover gaat deze clip: ISO/IEC 42001, van maatregel naar managementsysteem."]),
("E1","Normboek met \"ISO/IEC 42001:2023\" op de rug; één model krimpt weg, een organisatieschema met beleid, rollen, risico's, controle en verbetering groeit eromheen. Slotje op het boek: \"normtekst is betaald\".",[
"ISO/IEC 42001 is een internationale norm uit 2023, voor een AI-managementsysteem.",
"Dat is geen checklist voor één model.",
"Het zijn afspraken over hoe een organisatie al haar AI bestuurt: beleid, rollen, risico's, controle en verbetering.",
"Een organisatie kan zich ertegen laten certificeren, zoals bij ISO 9001 voor kwaliteit of ISO 27001 voor informatiebeveiliging.",
"Een klant of toezichthouder ziet dan in één oogopslag: hier is AI geen los experiment, hier is het geregeld.",
"Ook buiten Europa gebruiken organisaties de norm als houvast, bijvoorbeeld als hun klanten erom vragen.",
"De normtekst zelf is betaald. Je hoeft hem niet te lezen.",
"Je moet wel de opbouw kennen, en weten waar jullie werk daarin past."]),
("E2","Zeven tegels 4 tot en met 10 vallen één voor één in een rij, elk met een icoon: kaart (context), leider (leiderschap), checklist (planning), gereedschap (ondersteuning), tandwiel (uitvoering), meetlat (evaluatie), pijl omhoog (verbetering). Bij 6 licht \"6.1.4 impactbeoordeling\" op.",[
"De eisen staan in zeven hoofdstukken: clausule 4 tot en met 10.",
"Vier is de context: welke AI gebruikt de organisatie, en voor wie?",
"Vijf is leiderschap: de leiding stelt een AI-beleid vast en verdeelt de rollen.",
"Zes is planning: risico's beoordelen, maatregelen kiezen, en beoordelen wat het systeem met mensen doet. Dat laatste is de impactbeoordeling, clausule 6.1.4.",
"Die kennen jullie al: K2 en de nulmeting vormen samen jullie AI-impactbeoordeling.",
"Zeven is ondersteuning, zoals mensen, kennis en documentatie.",
"Acht is uitvoering: de plannen echt doen.",
"Negen is evaluatie: meten, een interne audit, en een managementreview.",
"Tien is verbetering: afwijkingen herstellen en ervan leren."]),
("E3","De tegels rollen op tot een draaiend PDCA-wiel. Bij elk kwart vallen kaartjes uit het rapport op hun plek: Plan (K2, K4, K6, K7), Do (\"inbouwen via A-AI2\"), Check (hertest, K8, Design Review), Act (leeg vak met vraagteken). Het wiel draait één slag door: \"opnieuw\".",[
"Samen vormen die hoofdstukken een cirkel: plan, do, check, act.",
"Plan: risico's en impact beoordelen en maatregelen kiezen. Bij jullie zijn dat K2, K4, K6 en K7.",
"Do: de maatregelen invoeren. Bij jullie is dat het inbouwen via A-AI2.",
"Check: meten, auditen en terugkijken. Bij jullie zijn dat de hertest, K8 en de Design Review.",
"Act: corrigeren en verbeteren. En dan begint de cirkel opnieuw.",
"Dat woord telt: opnieuw. Een managementsysteem stopt niet na de livegang."]),
("EQ1","Vraagkaart op het wiel. Pauze 8 s met aftelbalk.",[
"Vraag één. Welke stap van plan, do, check en act is in jullie ontwerp het zwakst, en waarom? Zet de video even op pauze."]),
("EQ1b","Het vak Act knippert; tekst \"meten zonder gevolg\".",[
"Bij veel groepen is dat act. Ze meten wel, maar zeggen niet wat er gebeurt als een meting slecht uitvalt.",
"Daar komen we zo op terug, want juist daar vraagt de norm het meest."]),
("E4","Een la schuift open: \"Annex A, 38 beheersmaatregelen, 9 gebieden\". Vijf kaartjes springen eruit: A.2 AI-beleid, A.5 impactbeoordeling, A.6 levenscyclus, A.8 informatie voor belanghebbenden, A.10 derde partijen. Eén kaartje vliegt in de kolom Kader van een K7-tabel.",[
"Achter in de norm staat Annex A, een keuzelijst met 38 beheersmaatregelen in negen gebieden.",
"Bijvoorbeeld AI-beleid, A.2. De impactbeoordeling, A.5. De levenscyclus van het systeem, A.6. Informatie voor belanghebbenden, A.8. En derde partijen, zoals leveranciers, A.10.",
"Een organisatie hoeft niet alles te doen. Ze kiest wat past bij haar risico's, en legt uit waarom.",
"Daarom heeft K7 een kolom Kader. Daar kun je bijvoorbeeld naar een gebied uit Annex A verwijzen.",
"Neem de orderagent van Frisco Installaties. Die gebruikt n8n en een taalmodel van een andere partij.",
"De leverancierscheck uit H6 hoort dan bij A.10, derde partijen."]),
("E5","Terug naar het wiel. Drie groene vinkjes verschijnen: Design Review bij Check (label \"9.2 interne audit\"), beslismemo bij Act/Check (label \"9.3 managementreview\", met een kalenderblad \"volgende review\"), AI-beleidsregel bij Plan (label \"A.2\").",[
"Het goede nieuws: jullie doen al veel van wat de norm vraagt.",
"De Design Review in college 3 is een vorm van audit, zoals de interne audit uit clausule 9.2.",
"Ook de hertest in blok 3 is check: dezelfde testset als bij practicum 4, zodat je ziet wat de maatregelen echt veranderden.",
"Het beslismemo in blok 3 is een managementreview, clausule 9.3. Die kijkt terug en beslist vooruit.",
"Daarom vraagt het memo ook om de datum van de volgende review.",
"Elke maatregel in K7 heeft een eigenaar. En de AI-beleidsregel uit H7 is een klein stukje AI-beleid, A.2."]),
("E6","Het lege vak Act vult zich. Links een kaart \"Incidentroute: wat, wie, aan wie, wanneer\"; rechts een grote schakelaar \"Stopcriterium\". Daarna het ClaimWacht-dashboard van Tamarinde: indicator 1 kleurt twee maanden rood, de schakelaar voor één regio springt om naar \"steekproefcontrole\", de Manager Declaraties zet een paraaf. Kalenderblad: \"volgende review maart 2028\".",[
"Wat er nog bij moet, zit in clausule 10: afwijkingen en incidenten.",
"Wat is een incident? Wie meldt het, aan wie, en binnen welke termijn?",
"En wanneer gaat het systeem uit, en wie beslist dat?",
"In blok 3 worden dat twee vaste regels in K8: de incidentroute en het stopcriterium.",
"Voor een voldoende op monitoring in het eindrapport zijn ze allebei verplicht.",
"Bij de orderagent van Frisco kan een incident zijn: de agent bevestigt een order met een verkeerde prijs. Wie ziet dat, en wie hoort het?",
"Kijk naar ClaimWacht van verzekeraar Tamarinde, uit het voorbeeldrapport.",
"Gaan indicator 1 of 3 twee maanden achter elkaar over de grens? Dan gaat ClaimWacht uit voor dat kanaal of die regio, en geldt weer steekproefcontrole.",
"De Manager Declaraties beslist dat, zonder op de directie te wachten.",
"En de volgende managementreview staat al vast: maart 2028."]),
("EQ2","Vraagkaart. Pauze 8 s met aftelbalk.",[
"Vraag twee. Wie bij jullie partner zou de managementreview moeten doen, en hoe vaak? Zet de video even op pauze."]),
("EQ2b","Twee kaartjes: \"mag bijsturen of stoppen\" en \"vast ritme: jaarlijks, eerder na een incident\".",[
"Kies iemand die het systeem mag bijsturen of stoppen, niet alleen iemand die het bouwde.",
"En spreek een vast ritme af: bijvoorbeeld elk jaar, en eerder na een incident."]),
("E7","\"Nu jij, met je groep\": een leeg PDCA-wiel en een stapel K7-kaartjes die de kijker zelf moet plaatsen. Onderin: \"college 3, daarna K8 in blok 3\".",[
"Nu jij, met je groep.",
"Teken de cirkel van plan, do, check en act, en zet elke maatregel uit K7 op zijn plek.",
"Waar de cirkel open blijft, zit jullie gat.",
"Een gat is geen ramp. Een gat dat je niet ziet, wel.",
"Dat werk je uit in college 3, en daarna in K8."]),
]
z=[];tot=0;rows=[]
for k,beeld,zs in S:
    for i,t in enumerate(zs):
        key=k if len(zs)==1 else f"{k}.{i+1}"
        last=i==len(zs)-1
        p=8 if (k.startswith('EQ') and not k.endswith('b')) else (0.9 if last else 0.5)
        z.append([key,t,p]); tot+=len(t)
    rows.append((k,beeld," ".join(zs)))
json.dump(z,open('zinnen.json','w'),ensure_ascii=False,indent=0)
print('tekens',tot,'zinnen',len(z))
md="## Kaderclip E · ISO/IEC 42001: van maatregel naar managementsysteem (7 minuten, blok 2)\n\n"
md+="**Doel.** De student kan het eigen ontwerp plaatsen in de verbetercyclus van ISO/IEC 42001 en ziet welke stappen nog ontbreken.\n\n"
md+="| Sleutel | Beeld | Gesproken tekst |\n| --- | --- | --- |\n"
for k,b,t in rows:
    if k.startswith('EQ') and not k.endswith('b'): b=b
    md+=f"| {k} | {b.replace('|','/')} | {t.replace('|','/')} |\n"
md+=f"\nGesproken tekst: {tot:,} tekens (budget 5.300).".replace(',','.')
open('script.md','w').write(md)
