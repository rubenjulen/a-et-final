import json
# Kennisclip 5c · Drie soorten black box (blok 1, bij college 1 deel 4 en kennispakket 1 "Uitleg: de black box openen")
# (sleutel, beeld, tekst, pauze)
R=[
("B0","Titelkaart op navy: 'Kennisclip 5c · Drie soorten black box'. Drie iconen: slot, document vol vaktaal, wirwar van verbindingen.","Drie soorten black box.",2.2),
("B1","Telefoon met een bericht van Suribank: 'Uw aanvraag is afgewezen.' Geen reden.","Een aanvrager bij Suribank krijgt een bericht: uw aanvraag is afgewezen. Waarom? Dat staat er niet.",0.5),
("B2","Schema: gegevens gaan een zwarte doos in, er komt 'afgewezen' uit. Op de doos een vraagteken.","Zo'n systeem heet een black box. Je ziet wat erin gaat en wat eruit komt, maar niet wat er binnenin gebeurt.",0.5),
("B3","Herkomst: kaart 'techniek: invoer en uitvoer', dan het boek 'The Black Box Society' (Pasquale, 2015).","Het begrip komt uit de techniek. In 2015 maakte Frank Pasquale er een maatschappelijk thema van, met zijn boek The Black Box Society.",0.5),
("B4","Kaart 'Burrell (2016)' met drie lege vakken die zich vullen: geheim, te ingewikkeld, onbekend.","Maar een black box is niet altijd hetzelfde. De onderzoeker Jenna Burrell onderscheidde in 2016 drie soorten. Elke soort vraagt een ander antwoord.",0.9),
# soort 1
("S1a","Soort 1 · Bewust geheim. Een doos met een hangslot.","Soort één: bewust geheim. Het model kan wel worden uitgelegd, maar de eigenaar wil het niet laten zien. Het is een bedrijfsgeheim, of een staatsgeheim.",0.4),
("S1b","Casuskaart SyRI: Nederland, rechtbank Den Haag, 5 februari 2020.","Een voorbeeld is SyRI, een Nederlands systeem dat fraude met uitkeringen moest opsporen. Het risicomodel was geheim. In februari 2020 oordeelde de rechter dat de wet het recht op privéleven schond, mede omdat niemand kon controleren hoe het werkte.",0.4),
("S1c","Casuskaart Loomis: Verenigde Staten, 2016, COMPAS-score.","In de Verenigde Staten gebruikte een rechter in de zaak Loomis een geheime risicoscore bij het bepalen van de straf. De verdachte kon die score niet controleren.",0.4),
("S1d","Een vergrootglas boven de open doos: 'openheid of audit'.","Het antwoord op deze soort: openheid, of een onafhankelijke audit. Iemand van buiten moet kunnen meekijken.",0.9),
# soort 2
("S2a","Soort 2 · Te ingewikkeld. Telefoon met vaktaal: score, drempel, kenmerken met gewichten.","Soort twee: te ingewikkeld voor wie het raakt. De uitleg bestaat wel, maar alleen in vaktaal.",0.4),
("S2b","Aanvrager met een vraagteken naast de telefoon.","De aanvrager krijgt bijvoorbeeld: score 42, drempel 50, belangrijkste kenmerken district, looptijd en inkomen. Wat moet ze daarmee?",0.4),
("S2c","Kaart 'geen begrip, geen bezwaar'; antwoordkaart 'gewone taal en een loket'.","Wie de uitleg niet begrijpt, kan ook geen bezwaar maken. Het antwoord: uitleg in gewone taal, en een loket waar je terecht kunt.",0.4),
("S2d","Telefoon met de uitleg in gewone taal: 'Met een looptijd van 24 in plaats van 12 maanden was uw aanvraag goedgekeurd.'","Bijvoorbeeld: met een looptijd van vierentwintig in plaats van twaalf maanden was uw aanvraag goedgekeurd. Dat heet een contrafactische uitleg: wat had er anders moeten zijn?",0.9),
# soort 3
("S3a","Soort 3 · Ook voor de makers onbekend. Een neuraal netwerk met flikkerende verbindingen.","Soort drie: ook voor de makers onbekend. Het model is zo groot dat zelfs de experts niet precies weten waarom een uitkomst zo uitvalt.",0.4),
("S3b","Getallen zweven uit het netwerk: 0,173; −1,02; 0,88.","Een groot taalmodel bestaat uit miljarden getallen, de gewichten. Je kunt ze allemaal bekijken, maar ze vertellen niet wat ze betekenen. De code lezen helpt dus niet.",0.4),
("S3c","Schema: jullie app stuurt een vraag naar een taalmodel van een externe aanbieder; op die dienst een slot en een netwerk.","Gebruiken jullie een taalmodel van een externe aanbieder? Dan heb je met soort één én soort drie te maken.",0.4),
("S3d","Een leesbare beslisboom naast het netwerk; kaart 'Rudin (2019)'.","Het antwoord: kies bij grote gevolgen een leesbaar model als dat even goed werkt, zoals Cynthia Rudin in 2019 bepleitte. Of zorg voor strenge menselijke controle.",0.9),
# tussenvraag 1
("Q1","Tussenvraag 1: A. Bewust geheim, B. Te ingewikkeld, C. Ook voor de makers onbekend. Aftelbalk 8 s.","Tussenvraag. Een gemeente gebruikt een risicomodel, maar de leverancier weigert te laten zien hoe het werkt. Welke soort is dat? A, bewust geheim. B, te ingewikkeld. C, ook voor de makers onbekend.",8),
("Q1b","Knop A licht groen op.","Het antwoord is A, bewust geheim. Het antwoord daarop is openheid, of een audit door iemand van buiten.",0.9),
# wanneer
("W1","Twee kolommen: 'Vaak wel' met muziekaanbevelingen, advies, een mens beslist.","Mag een black box dan nooit? Toch wel. Bij lage impact, als het systeem alleen adviseert en een mens echt beslist. Denk aan muziekaanbevelingen.",0.4),
("W2","Kolom 'Niet': rechten of vrijheid, geen bezwaar, niemand grijpt in. Navy balk met de vuistregel.","Niet als rechten of vrijheid op het spel staan, als er geen bezwaar mogelijk is, of als niemand echt ingrijpt. De vuistregel: hoe groter de impact op iemands leven, hoe zwaarder de eis aan uitleg.",0.9),
# tussenvraag 2
("Q2","Tussenvraag 2: dezelfde drie opties. Aftelbalk 8 s.","Tussenvraag. De aanvrager krijgt alleen: score 42, drempel 50. Welke soort black box is dat? A, bewust geheim. B, te ingewikkeld voor wie het raakt. C, ook voor de makers onbekend.",8),
("Q2b","Knop B licht groen op.","Het antwoord is B. De uitleg bestaat, maar niet in taal die de aanvrager begrijpt.",0.9),
# samenvatting en opdracht
("S9","Drie rijen: soort en antwoord.","Samengevat. Bewust geheim vraagt om openheid of een audit. Te ingewikkeld vraagt om uitleg in gewone taal. Ook voor de makers onbekend vraagt om een leesbaar model, of strenge menselijke controle.",0.9),
("N1","Eindkaart 'Nu jij' met drie stappen.","Nu jij. Welke soort black box zit er in jullie oplossing, en voor wie? Schrijf het op bij domein zes van de nulmeting: transparantie.",0.8),
]
n=sum(len(t) for _,_,t,_ in R)
json.dump([[k,t,p] for k,_,t,p in R],open('zinnen.json','w'),ensure_ascii=False,indent=0)
md=["## Kennisclip 5c · Drie soorten black box (ongeveer 5 minuten, blok 1)","",
"Na deze clip kan de student uitleggen wat een black box is en waar het begrip vandaan komt, de drie soorten ondoorzichtigheid van Burrell herkennen met een voorbeeld, per soort het passende antwoord noemen, en uitleggen wanneer een black box wel of niet aanvaardbaar is.","",
"Bronnen: Pasquale, F. (2015), The Black Box Society, Harvard University Press; Burrell, J. (2016), How the machine 'thinks', Big Data & Society 3(1); Rechtbank Den Haag 5 februari 2020, ECLI:NL:RBDHA:2020:865 (SyRI); State v. Loomis, Wisconsin Supreme Court 2016; Wachter, Mittelstadt & Russell (2018), counterfactual explanations, Harvard Journal of Law & Technology 31(2); Rudin, C. (2019), Nature Machine Intelligence 1, 206–215.","",
"| Sleutel | Beeld | Gesproken tekst |","| --- | --- | --- |"]
for k,b,t,p in R:
    md.append(f"| {k} | {b.replace('|','/')} | {t} |")
md+=["",f"Gesproken tekst: {n:,} tekens".replace(',','.')]
open('script.md','w').write("\n".join(md)+"\n")
print(n,len(R))
