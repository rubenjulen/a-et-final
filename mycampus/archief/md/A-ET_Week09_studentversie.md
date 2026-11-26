## Deze week

**Leerdoelen.** Na week 9 kan de student:

1. Met dezelfde test als in week 4 laten zien of een ingebouwde maatregel werkt, werkt deels of niet werkt, en die uitkomst eerlijk gebruiken in het advies.
2. Maatregelen faseren in een uitvoerbaar implementatieplan met eigenaren en middelen.
3. Ethische signalen kiezen voor groepsverschillen, proces en mensen, elk met een grens, een actie en een eigenaar, en daarbij verwijzen naar de technische monitoring van A-AI2 en de datamonitoring van A-DG.
4. Uitleggen waarom een model na verloop van tijd slechter kan werken, en hoe monitoring dat opvangt.
5. Een eindoordeel formuleren in een beslismemo van één pagina: verantwoord inzetbaar, inzetbaar onder voorwaarden, of nu niet.

### Planning en deadlines

| Moment | Wat |
| --- | --- |
| Maandag 1 maart | Weekmodule 9 opent met feedforward op de Design Review |
| Maandag 1 tot en met woensdag 3 maart | Practicum 4b: de hertest, met de ingebouwde maatregelen |
| Woensdag 3 maart, 23:59 | Weekcheck met standpunt |
| Donderdag 4 maart | Online sessie: monitoring en het beslismemo (opent met de stelling); persoonlijke feedback aan twee groepen |
| \[datum, volgens A-AI2\] | AI Solutions Day: groepen laten een ingebouwde maatregel en de uitkomst van de hertest zien |
| Zondag 7 maart, 23:59 | Concept eindrapport (met hertest, K8 en beslismemo) naar de peergroep, docent in cc |
| Maandag 8 maart, 23:59 | Peerfeedback terug |
| Dinsdag 9 maart | Online vragenuur (week 10) |
| Donderdag 11 maart, 23:59 | Inleveren Assessment 2 |

### Tijdsbesteding

| Onderdeel | Uren |
| --- | --- |
| Clips 21 en 22 en weekcheck met standpunt | 1 |
| Online sessie | 1 |
| Practicum 4b: de hertest, in de groep | 1 |
| K8 implementatie- en monitoringplan in de groep | 2 |
| Beslismemo in de groep | 1 |
| Peerfeedback geven | 1 |
| Reflectie: eerste versie | 1 |
| **Totaal** | **8 SBU** |
| Practicum 5 (optioneel) | +1 |

## Voorbereiding

### Week 9: van ontwerp naar besluit

Jullie maatregelen zijn ingebouwd. Deze week beantwoorden jullie de laatste vragen: werken de maatregelen echt? Hoe weet de organisatie over een jaar nog of het goed gaat? En dan het belangrijkste: wat is jullie oordeel?

**Wat je oplevert (zondag 7 maart, 23:59, naar je peergroep)**

Het concept van het volledige eindrapport, met daarin:

1. De hertest (practicum 4b): week 4 en week 9 naast elkaar, met per maatregel de conclusie. Het testlogboek gaat als bijlage mee.
2. K8: implementatie- en monitoringplan (hoofdstuk 11): fasering, en ethische signalen met grens, actie en eigenaar.
3. Restrisico en conclusie (hoofdstuk 12).
4. Het beslismemo van één pagina, vooraan.

**Deze week ook**

- Practicum 4b: doe de test van week 4 opnieuw, met precies dezelfde vragen of paren, nu met de maatregelen erin. Klaar vóór woensdag 3 maart.
- Clip 21 en 22 (samen 15 minuten) en de weekcheck met je standpunt op woensdag.
- Donderdag 4 maart: online sessie over monitoring en het beslismemo. De sessie opent met de stelling.
- AI Solutions Day (\[datum\], A-AI2): laat een ingebouwde maatregel zien en wat de hertest liet zien.
- Maandag 8 maart: peerfeedback geven, de laatste keer.
- Schrijf een eerste versie van je reflectie. Lees daarvoor je logboekregels en je standpunten terug.
- **Optioneel:** practicum 5, het model een jaar later (ongeveer een uur). Wie het doet, heeft sterk materiaal voor hoofdstuk 11 en voor de reflectie.

## Kennisclips

Samen 15 minuten. Ze bouwen voort op het minicollege van college 3. De tekst van de clips staat achteraan om mee te lezen.

### Clip 21: Monitoren met grenzen en acties (8 minuten)

**Doel.** De student kan een monitoringplan opstellen dat signalen op tijd oppikt en tot een besluit leidt.

Video: [link volgt op MyCampus]

### Clip 22: Het beslismemo (7 minuten)

**Doel.** De student kan een eindoordeel geven dat een beslisser kan gebruiken.

Video: [link volgt op MyCampus]

## Practicum 4b: de hertest

In week 4 testten jullie je oplossing (practicum 4). Sindsdien hebben jullie via A-AI2 maatregelen ingebouwd. Nu doen jullie precies dezelfde test opnieuw. Zo laten jullie zien of de maatregelen werken, en niet alleen dat ze er zijn.

**Duur:** ongeveer een uur per student, in de groep, klaar vóór woensdag 3 maart. **Waar:** in het testlogboek van week 4 (practicum4\_testlogboek.xlsx). Daar is al plek voor week 9.

### Spelregels

- Dezelfde vragen of paren, in dezelfde volgorde en met dezelfde woorden. Laat niets weg, ook niet wat in week 4 goed ging.
- Leg de nieuwe versie van de oplossing en de datum vast in het tabblad Start.
- Dezelfde testomgeving en dezelfde regels als in week 4: alleen verzonnen personen, nooit echte gegevens.
- Scoor eerst zelf en laat daarna een ander groepslid nascoren, net als in week 4. Liefst dezelfde nascoorder per blok.
- Een nieuwe vraag die bij een maatregel hoort, bijvoorbeeld een test van de overdracht naar een mens, mag erbij als extra (X-nummer). Die telt niet mee in de vergelijking.

### Variant A: chatbot of agent

1. Open het tabblad A\_log. De rijen voor week 9 staan al klaar (Moment = week 9).
2. Stel elke vraag twee keer, elke keer in een nieuw gesprek, zoals in week 4. Plak het antwoord en scoor goed, matig of fout.
3. Laat nascoren. Bespreek elke rij waar "bespreken" staat.
4. Open Samenvatting. Daar staan week 4 en week 9 per blok naast elkaar.

### Variant B: voorspellend model

1. Draai de workflow of het notebook opnieuw, nu op de versie mét maatregelen. Voor Suribank is dat versie B uit practicum 2: zonder geslacht, district en regio.
2. Plak aanvraag\_id en de kansen in B\_import, in de kolommen voor week 9 (E tot en met G).
3. Kijk in Samenvatting naar het aantal paren met een ander besluit, week 4 tegen week 9.
4. Meet ook de fouten per groep opnieuw, zoals in practicum 2. Dit is de belangrijkste stap. Heb je een kenmerk weggelaten, dan kan een paar op dat kenmerk niet meer wisselen. Dat bewijst niets. Of een groep nog anders behandeld wordt, zie je aan de fouten per groep.
5. Doe de grensgevallen en de uitlegtest opnieuw. Begrijpt een afgewezen aanvrager de uitleg nu beter?

### Wat in het rapport komt

| Onderdeel | Wat erin staat |
| --- | --- |
| Vergelijking | Per blok (A), of per kenmerk en per groep (B): week 4 en week 9 naast elkaar |
| Per maatregel | Werkt, werkt deels of werkt niet, met het bewijs uit de vergelijking |
| Betekenis | Welk risico in K6 daalt, welk restrisico blijft (hoofdstuk 12), en wat dit doet met het oordeel in het beslismemo |
| Grenzen | Wat de hertest niet laat zien |

Het bijgewerkte testlogboek gaat als bijlage mee.

**Werkt een maatregel niet, of maar deels?** Dat is geen mislukking van de groep, maar een uitkomst. Zeg het eerlijk en trek de conclusie in het beslismemo: een extra voorwaarde, of "nu niet". Amsterdam deed precies dit met de Slimme Check (week 4, praktijkcasussen).

### AI Solutions Day (\[datum\], A-AI2)

Op de AI Solutions Day laten de groepen hun oplossing zien. Neem twee dingen mee uit A-ET:

- Eén ingebouwde maatregel, het liefst live. Bijvoorbeeld de AI-melding, de overdracht naar een mens of de uitleg bij een afwijzing.
- De uitkomst van de hertest op één dia: week 4, week 9, en wat dat betekent voor jullie advies.

De Design Review in week 8 was de generale repetitie.

## K8: implementatie- en monitoringplan

K8 wordt hoofdstuk 11 van het eindrapport (ongeveer 1½ pagina). Vier delen; deel D bestaat uit twee vaste regels.

### Deel A: implementatieplan

Neem alle maatregelen uit K7 en zet ze in drie fasen. Wat jullie via A-AI2 al hebben ingebouwd en getest, zet je in fase direct, met "ingebouwd" en de uitkomst van de hertest.

| Fase | Wanneer | Wat erin hoort |
| --- | --- | --- |
| Direct | Binnen een maand | Maatregelen die schade nu stoppen, ook als ze tijdelijk zijn |
| Kort | Binnen drie maanden | Processen, documenten, training, de bezwaarroute |
| Structureel | Binnen een jaar | Hertraining, contracten, dashboards, onafhankelijke toets |

Per maatregel:

| Control ID | Fase | Wat er moet gebeuren | Eigenaar | Middelen | Klaar wanneer | Besluitmoment |
| --- | --- | --- | --- | --- | --- | --- |
| C-02 | Direct | Afwijzingen weer langs een medewerker; werkinstructie aanpassen | Hoofd kredietverlening | Ongeveer 85 uur per maand extra | 1 april | Directie keurt de extra capaciteit goed |

**Middelen** zijn uren, geld, mensen of medewerking van een leverancier. Een schatting is genoeg; zeg waar die op rust.

**Besluitmoment:** wie moet waarover beslissen voordat de volgende fase kan beginnen? Gebruik je RACI.

### Deel B: monitoringplan

Vijf tot acht ethische signalen.

| Indicator | Soort | Bron en meting | Hoe vaak | Wie meet | Grens | Actie bij overschrijding | Wie besluit |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Afwijzingspercentage per filiaal | Groepsverschil | Kernsysteem | Maandelijks | Data-analist IT | Verschil met Paramaribo groter dan de grens die de directie vaststelt | Review binnen twee weken; zo nodig meer afwijzingen naar een mens | Hoofd kredietverlening |

**Bij generatieve AI.** Ethische signalen voor een chatbot of agent zijn bijvoorbeeld: het aandeel fout of matig per blok als je de vaste testset van practicum 4 elke maand opnieuw afspeelt; verschillen in antwoorden tussen namen en talen (blok 1); het aantal overdrachten naar een mens, en hoe vaak een gebruiker daar vergeefs om vroeg; klachten over antwoorden; en pogingen tot misbruik die de chatbot niet tegenhield.

**Eisen**

- Alle drie de soorten: groepsverschillen, proces en mensen.
- Minstens twee indicatoren worden uitgesplitst naar de groepen die in jullie risicoanalyse kwetsbaar zijn.
- Minstens één vroeg signaal: iets wat je meteen ziet, zoals een verschil in afwijzingen of goedkeuringen tussen groepen. Wacht niet alleen op uitkomsten die pas na een jaar bekend zijn.
- Elke indicator heeft een grens, een actie en iemand die besluit.
- Minstens één indicator kan leiden tot stilzetten. Zeg welke grens dat is.
- Alleen ethische signalen. Technische monitoring (storingen, snelheid, nauwkeurigheid) staat in A-AI2, datamonitoring (kwaliteit van de data, veranderingen in wie er aanvraagt) in A-DG. Verwijs daarnaar in één zin, en zeg wie besluit als daar een alarm afgaat.
- Bij een chatbot of agent: minstens één signaal uit de vaste testset van practicum 4, en het aantal overdrachten naar een mens.

### Deel C: herbeoordeling

Wanneer gaat de hele toepassing opnieuw door een beoordeling zoals jullie die nu deden? Noem:

- een vast moment (bijvoorbeeld jaarlijks);
- en de gebeurtenissen die een extra herbeoordeling vereisen: een grote wijziging van het model of het proces, een nieuwe wet (zoals de privacywet in Suriname), een ernstig incident, of een indicator die herhaaldelijk de grens overschrijdt.

In het werkboek (ICT A-ET Werkboek instrumenten.xlsx) vul je dit in op het tabblad K8\_Monitoring: het moment in gebruik en het moment van een wijziging.

### Deel D: twee vaste regels

Elk K8 heeft deze twee regels, ook als jullie oplossing klein is. Ze sluiten de verbetercyclus uit kaderclip E: ISO/IEC 42001 vraagt erom in clausule 10 (afwijkingen en corrigerende maatregelen).

**Incidentroute.** Wat is bij jullie een incident, wie meldt het aan wie, en binnen welke termijn? Een incident is meer dan een storing: een besluit of antwoord dat iemand schade doet of had kunnen doen. Denk aan een onterechte afwijzing die een klant aanvecht, of een chatbot die gegevens van een andere klant noemt. Leg vast wie mag melden (ook klanten en medewerkers), bij wie de melding binnenkomt, hoe snel er wordt gereageerd, en wie de getroffene informeert.

**Stopcriterium.** Wanneer gaat het systeem uit of terug naar handwerk, en wie beslist dat? Koppel het aan een grens uit deel B of aan een ernstig incident, en noem iemand die snel bereikbaar is. Zeg ook hoe het werk doorgaat zolang het systeem uit staat.

| Regel | Voorbeeld Suribank | Voorbeeld orderchatbot |
| --- | --- | --- |
| Incidentroute | Bezwaar tegen een afwijzing waarbij het model aantoonbaar fout zat: de medewerker meldt het dezelfde dag bij het hoofd kredietverlening, die binnen vijf werkdagen beoordeelt en de klant informeert. | Een antwoord met gegevens van een andere klant, of een order die de agent zonder akkoord plaatste: wie het ziet, meldt het direct bij de product owner; de klant hoort het binnen 48 uur. |
| Stopcriterium | Indicator 1 of 3 twee keer achter elkaar boven de grens: alle aanvragen terug naar handmatige beoordeling. Besluit: hoofd kredietverlening. | Eén datalek, of twee ernstige incidenten in één week: de agent gaat uit en klanten bellen of mailen weer met een medewerker. Besluit: operationeel manager. |

### Veelgemaakte fouten

- Alles in fase "direct". Dan is er geen plan, alleen een wensenlijst.
- Indicatoren die alleen het model meten. Of mensen bezwaar kunnen maken en of medewerkers afwijken, is net zo belangrijk.
- Een grens zonder onderbouwing ("maximaal 5%") of een grens die niemand vaststelt.
- Wachten op terugbetaling als enige signaal. Zie practicum 5.
- Technische indicatoren, zoals storingen of reactietijd. Die horen bij A-AI2; verwijs ernaar.
- Een maatregel in fase "direct" zonder uitkomst van de hertest. Ingebouwd is nog niet hetzelfde als werkend.

Werk K8 uit in het werkboek ICT A-ET Werkboek instrumenten.xlsx, tabblad K8\_Monitoring (delen A tot en met D) en tabblad Hertest.

## Het beslismemo

Het beslismemo staat vooraan in het eindrapport. Eén pagina, voor iemand die beslist en weinig tijd heeft: een directeur, een afdelingshoofd, een projectleider. In ISO/IEC 42001 heet zo'n terugblik met besluit een managementreview (9.3). Die kijkt terug en beslist vooruit: wat werkt, wat niet, wat is het besluit, en wanneer kijken we opnieuw? Het memo heeft daarom zeven onderdelen: het oordeel, waarom, wat het oplevert, de voorwaarden, het restrisico en wie het accepteert, wat het oordeel kan veranderen, en de managementreview met het stopcriterium en de datum van de volgende review. Het sjabloon hieronder volgt die opbouw.

### Welk oordeel?

| Oordeel | Wanneer |
| --- | --- |
| **Verantwoord inzetbaar** | Er zijn geen High-risico's of hoger meer na de maatregelen die er al zijn; restrisico's zijn bewust geaccepteerd; monitoring loopt. |
| **Inzetbaar onder voorwaarden** | Er zijn nog belangrijke risico's, maar ze zijn binnen redelijke tijd te beheersen met maatregelen die de organisatie kan uitvoeren. Gebruik mag doorgaan of starten, mits de voorwaarden op tijd worden gehaald. |
| **Nu niet** | Een of meer risico's zijn te ernstig of niet binnen redelijke tijd te beheersen, of de organisatie kan de maatregelen niet dragen. Stoppen, niet beginnen, of eerst herontwerpen. |

Kies het oordeel dat volgt uit jullie rapport, niet het oordeel dat de organisatie wil horen. "Nu niet" is een volwaardig advies.

### Sjabloon

> **Aan:** \[functie van de beslisser\] · **Van:** \[groep\] · **Datum:** \[datum\] · **Onderwerp:** advies over \[toepassing\]
>
> **Ons oordeel:** \[verantwoord inzetbaar / inzetbaar onder voorwaarden / nu niet\], in één zin met de belangrijkste reden.
>
> **Waarom.** Drie redenen, elk in één of twee zinnen, met een verwijzing naar het rapport. Minstens één reden komt uit de hertest: werkt wat jullie hebben ingebouwd?
>
> **Wat het oplevert.** De baten van de toepassing, eerlijk benoemd.
>
> **Voorwaarden.**
>
> | Voorwaarde | Uiterlijk | Eigenaar | Als het niet lukt |
> | --- | --- | --- | --- |
> | ... | ... | ... | ... |
>
> **Restrisico.** Wat blijft er over, en wie moet dat bewust accepteren?
>
> **Wat ons oordeel kan veranderen.** De onzekerheden die het advies kunnen omdraaien.
>
> Managementreview. **Volgende herbeoordeling:** \[datum of gebeurtenis\]. Stopcriterium: \[wanneer gaat het systeem uit of terug naar handwerk, en wie beslist dat\].

Voorwaarden zijn er alleen bij "onder voorwaarden". Bij "nu niet" noem je in plaats daarvan wat er moet veranderen voordat een nieuw oordeel mogelijk is.

### Eisen

- Eén pagina, het oordeel in de eerste zin.
- Elke reden is terug te vinden in het rapport.
- Elke voorwaarde is toetsbaar, met een datum, een eigenaar en een gevolg als ze niet wordt gehaald.
- De baten staan erin.
- Het restrisico heeft een naam: wie accepteert het?
- Minstens één reden komt uit de hertest, en het oordeel past bij wat de hertest liet zien.
- De datum of gebeurtenis van de volgende review staat erin, zoals bij een managementreview.

### Leestest

Laat het memo lezen door iemand die het rapport niet kent. Vraag: wat moet er nu gebeuren, door wie, en wanneer? Kan die persoon dat niet zeggen, dan is het memo nog niet af.

### Veelgemaakte fouten

- Een samenvatting van het rapport in plaats van een advies.
- "Inzetbaar onder voorwaarden" met twaalf voorwaarden. Kies de drie tot vijf die het verschil maken.
- Voorwaarden zonder gevolg: wat gebeurt er als ze niet worden gehaald?
- Een oordeel dat niet volgt uit hoofdstuk 12: een Very high-restrisico en toch "verantwoord inzetbaar".

Gebruik het sjabloon voor het eindrapport (ICT A-ET Sjabloon eindrapport.docx); het beslismemo staat daar vooraan.

## Practicum 5 (optioneel): het model een jaar later

*Ongeveer een uur in Orange, of in Python met het notebook practicum5.ipynb uit ICT A-ET Practicum 5.zip (zelfde stappen, tabellen en vragen). Ethische vraag uit het lesplan: wie merkt het als het model ongemerkt slechter wordt?*

### Het scenario

> Dit scenario is verzonnen. Het is maart 2028. Snel Krediet draait sinds september 2026 op een logistisch regressiemodel zoals je dat in practicum 1 en 2 trainde, zonder hertraining. In de periode daarna stegen de prijzen in Suriname flink. Lonen stegen op papier mee, maar mensen konden er minder van kopen. Suribank is ook actiever klanten gaan werven in het binnenland. Inmiddels is bekend welke leningen uit die periode zijn terugbetaald.

### Bestanden

| Bestand | Wat het is |
| --- | --- |
| suribank\_kredietaanvragen.csv | De 1.200 aanvragen waarop het model is getraind (uit week 0) |
| suribank\_2025\_controle.csv | 1.000 andere aanvragen uit dezelfde periode als de trainingsdata; het model heeft ze nooit gezien |
| suribank\_2027.csv | 1.000 aanvragen uit de periode na de invoering |

### Deel 1: wat je meteen had kunnen zien (20 minuten)

In het echt weet je pas na een jaar of een lening is terugbetaald. Kijk daarom eerst alleen naar de invoer en de beslissingen.

1. Zet twee **File**-widgets neer: een met suribank\_2025\_controle.csv, een met suribank\_2027.csv. Zet in beide de rol van terugbetaald op target en die van aanvraag\_id op meta, zoals in eerdere practica.
2. Verbind beide met een **Concatenate**-widget (groep Transform). Vink **Append data source IDs** aan. Er komt een kolom *Source ID* bij die zegt uit welk bestand een rij komt.
3. Verbind Concatenate met een **Box Plot**. Kies maandinkomen\_srd en zet *Subgroups* op Source ID. Noteer de mediaan voor beide bestanden. Doe hetzelfde voor gevraagd\_bedrag\_srd.
4. Verbind Concatenate met **Distributions**. Kies regio en zet *Split by* op Source ID. Noteer het aandeel binnenland. Doe hetzelfde voor dienstverband (aandeel informeel).

*Lukt Concatenate niet? Open dan elk bestand in een eigen Box Plot en Distributions en vergelijk ze naast elkaar.*

|  | 2025 (controle) | 2027 |
| --- | --- | --- |
| Mediaan maandinkomen |  |  |
| Mediaan gevraagd bedrag |  |  |
| Aandeel binnenland |  |  |
| Aandeel informeel |  |  |

### Deel 2: wat er gebeurde (30 minuten)

Nu kijk je naar de uitkomsten.

5. Nieuwe **File**-widget met suribank\_kredietaanvragen.csv (rollen als hierboven). Verbind met **Test and Score** als *Data*.
6. Zet een **Logistic Regression**-widget neer en verbind die met Test and Score.
7. Verbind de File met suribank\_2025\_controle.csv met Test and Score als *Test Data*. Kies in Test and Score **Test on test data** en zet *Target class* op ja. Noteer CA.
8. Verbind Test and Score met een **Confusion Matrix** en kies *Number of instances*. Noteer de vier getallen.
9. Vervang in de File-widget het controlebestand door suribank\_2027.csv. Alles rekent opnieuw. Noteer opnieuw.
10. Wil je het per regio zien? Zet tussen de testbestanden en Test and Score een **Select Rows** met regio is binnenland, en daarna kust, zoals in practicum 2.

|  | 2025 (controle) | 2027 |
| --- | --- | --- |
| CA (nauwkeurigheid) |  |  |
| Voorspeld "ja" (percentage goedgekeurd) |  |  |
| Werkelijk "ja" (percentage terugbetaald) |  |  |
| Onterecht goedgekeurd: van wie niet terugbetaalde, het aandeel dat toch "ja" kreeg |  |  |
| Onterecht afgewezen: van wie wel terugbetaalde, het aandeel dat "nee" kreeg |  |  |
| Onterecht afgewezen in het binnenland |  |  |

### Vragen (één pagina, zoals bij elk practicum)

1. Welke veranderingen had Suribank in 2027 al kunnen zien, zonder te wachten op de uitkomsten? Welke indicator in jullie monitoringplan had dit opgemerkt?
2. Het model keurt in 2027 meer aanvragen goed, terwijl minder mensen hun lening terugbetalen. Hoe kan dat? Kijk naar het inkomen.
3. Het verschil in onterecht afwijzen tussen binnenland en kust is in 2027 bijna verdwenen. Is het model eerlijker geworden?
4. Wie draagt de schade als iemand onterecht een lening krijgt?
5. Je bent hoofd kredietverlening. Wat doe je, en wie moet daarover beslissen?

## Weekcheck 9

Sluit woensdag 3 maart om 23:59. Vijf vragen, twee pogingen. Daarna een logboekregel en een standpunt.

**Vraag 1.** Welke indicator is het best uitgewerkt?

- a. We monitoren de eerlijkheid van het model.
- b. Aantal klachten.
- c. Afwijzingspercentage per filiaal, maandelijks gemeten door de data-analist; bij meer dan de vastgestelde grens verschil met Paramaribo een review door het hoofd kredietverlening binnen twee weken.
- d. Het model moet minstens 70% nauwkeurig zijn.

**Vraag 2.** Een kredietmodel geeft een jaar na invoering duidelijk meer goedkeuringen, terwijl de uitkomsten van die leningen nog niet bekend zijn. Wat is de beste reactie?

- a. Goed nieuws: meer klanten geholpen.
- b. Wachten tot de uitkomsten bekend zijn.
- c. Onderzoeken waarom: is de groep aanvragers veranderd, of de economie? Dit is een signaal, ook zonder uitkomsten.
- d. Het model direct stilzetten.

**Vraag 3.** Wat hoort **niet** in het beslismemo?

- a. Het oordeel
- b. De voorwaarden
- c. Het restrisico en wie het accepteert
- d. De volledige risicoanalyse met alle scores

**Vraag 4.** Een groep adviseert "inzetbaar onder voorwaarden". Wat maakt dat oordeel sterk?

- a. Veel voorwaarden.
- b. Voorwaarden die toetsbaar zijn, met een termijn en een eigenaar, en wat er gebeurt als ze niet worden gehaald.
- c. Voorwaarden die de organisatie makkelijk kan halen.
- d. Geen voorwaarden noemen, zodat de organisatie zelf kiest.

**Vraag 5.** Een groep haalde geslacht en district uit het model. In de hertest wisselt bij de gepaarde test geen enkel paar meer van besluit. Wat concludeer je?

- a. De maatregel werkt: het model behandelt iedereen gelijk.
- b. Dat zegt weinig: de kenmerken zitten er niet meer in, dus een paar kan niet meer wisselen. Kijk ook naar de fouten per groep.
- c. De hertest is mislukt.
- d. Een hertest was niet nodig.

**Logboekregel.** Maximaal 60 woorden: *"Als ik nu de directeur was, zou ik ... besluiten, omdat ... Wat mij nog laat twijfelen, is ..."*

**Standpunt,** hoogstens 100 woorden. De stelling van de online sessie: *"Als de hertest niet beter uitpakt dan de eerste test, mag de oplossing niet live."* Ben je het eens of oneens? Geef één argument met een bron, en noem één tegenargument dat je serieus neemt.

## Online sessie donderdag 4 maart: monitoring en het beslismemo

60 minuten, opgenomen. De sessie opent met de stelling: *"Als de hertest niet beter uitpakt dan de eerste test, mag de oplossing niet live."* Twee studenten verdedigen en bestrijden de stelling, daarna volgt een peiling. Bereid je standpunt voor (zie de weekcheck).

Neem het concept van jullie beslismemo mee. In een breakout lezen twee groepen elkaar de eerste drie zinnen van hun memo voor, met de uitkomst van de hertest, en stelt de andere groep als directeur drie vragen: wat moet ik nu doen, wat kost het, en wat gebeurt er als het niet lukt? Denk ook na over jullie incidentroute en stopcriterium (K8, deel D).

## Laatste peercheck: zondag 7 en maandag 8 maart

De derde en laatste peercheck, nu op het hele eindrapport. Andere koppels dan in week 4 en 7. De peergroep heeft weinig tijd, dus de check is gericht: het memo, de keten en het plan.

**Wat de groep stuurt (zondag 7 maart, 23:59):** het concept van het volledige eindrapport. De docent in de cc.

**Wat de peergroep teruggeeft (maandag 8 maart, 23:59):** maximaal één pagina.

### Stap 1: lees eerst alleen het beslismemo (5 minuten)

Schrijf op, zonder het rapport te lezen: wat is het oordeel, wat moet er gebeuren, door wie, en wanneer? Lukt dat niet, dan is dat je eerste feedbackpunt.

### Stap 2: de drie vragen

1. **Wat is het sterkste punt?** Welk deel van het advies overtuigt het meest?
2. **Waar ontbreekt bewijs?** Welke voorwaarde, indicator of restrisico hangt in de lucht?
3. **Welke stap in de keten mist?** Volg één risico van begin tot eind: dilemma, risico, eis, maatregel, hertest, eigenaar, indicator, restrisico, en terug in het memo. Waar breekt de lijn?

### Stap 3: checklist

| Controle | Ja / nee / deels |
| --- | --- |
| Beslismemo: één pagina, oordeel in de eerste zin |  |
| Beslismemo: voorwaarden met datum, eigenaar en gevolg |  |
| Beslismemo: baten en restrisico benoemd |  |
| Hertest: week 4 en week 9 naast elkaar, met dezelfde vragen of paren |  |
| Hertest: per maatregel werkt, werkt deels of werkt niet, met bewijs |  |
| K8: drie fasen, met eigenaar en middelen per maatregel |  |
| K8: vijf tot acht ethische signalen, alle drie de soorten, met grens, actie en wie besluit |  |
| K8: minstens één vroeg signaal en één indicator die tot stilzetten kan leiden |  |
| K8: techniek en data verwezen naar A-AI2 en A-DG, niet overgeschreven |  |
| Hoofdstuk 12: restrisico per top 5 risico, en wie het accepteert |  |
| Het oordeel in het memo volgt uit hoofdstuk 12 en de hertest |  |
| Maximaal 12 pagina's |  |
| Verwerkingslijst aanwezig (bijlage E) |  |

**Spelregels** zoals in week 4 en 7. Groepen schrijven in hun logboek in twee zinnen wat ze met de feedback deden. Dat kan direct in de verwerkingslijst.

## Bijlage: tekst van de kennisclips (meelezen)

### Clip 21: Monitoren met grenzen en acties

Een model dat vandaag goed werkt, werkt over een jaar misschien niet meer. Hoe merk je dat?

De wereld verandert: andere klanten, inflatie, een nieuwe wet, een nieuw filiaal. Het model kent alleen het verleden waarvan het leerde. Twee soorten verandering: in **wie** er aanvraagt (de invoer), en in **wat** er gebeurt (de uitkomst).

Uitkomsten, zoals of een lening wordt terugbetaald, zie je pas na maanden of jaren. Invoer en beslissingen zie je meteen: het aandeel aanvragers uit het binnenland, het mediane inkomen, het percentage goedkeuringen per groep. Monitor allebei. Veranderingen in de invoer meet A-DG; jullie zorgen dat iemand besluit als daar een alarm afgaat. Practicum 5 laat zien waarom.

**Groepsverschillen:** fouten en afwijzingen per groep, goedkeuringen per groep. **Proces:** aandeel afwijkingen door medewerkers, bezwaren binnen de termijn afgehandeld, bij een chatbot de overdrachten naar een mens. **Mensen:** klachten, gegronde bezwaren, signalen van medewerkers. Nauwkeurigheid en storingen meet A-AI2, de kwaliteit van de data A-DG.

Wat meet je, hoe vaak, wie meet het, wat is de grens, en wat gebeurt er als die wordt overschreden, door wie? Zonder grens is het een getal; zonder actie een alarm dat niemand hoort.

Een grens is een bestuurlijke keuze. Stel er een voor met een reden ("het verschil dat we in practicum 2 en 4 zagen", "het niveau van vóór de invoering"), en zeg wie hem vaststelt. Begin streng en versoepel als je meer weet.

Drie niveaus: onderzoeken, bijsturen (drempel aanpassen, meer gevallen naar een mens), stilzetten en terug naar handmatig. De RACI zegt wie wat besluit.

Vijf tot acht ethische signalen, uit alle drie de soorten, elk met de vijf onderdelen.

### Clip 22: Het beslismemo

Een directeur leest jullie rapport van 12 pagina's niet. Wel één pagina. Wat moet daar staan?

**Verantwoord inzetbaar:** de risico's zijn beheerst; doorgaan met monitoring. **Inzetbaar onder voorwaarden:** doorgaan mag, mits bepaalde maatregelen er op tijd zijn; zo niet, dan stoppen of terugschalen. **Nu niet:** de risico's zijn te groot of niet te beheersen binnen redelijke tijd; stoppen, herontwerpen of niet beginnen.

Zeven vaste onderdelen. Het oordeel in de eerste zin. Dan: waarom (drie redenen, waarvan minstens één uit de hertest), wat het oplevert, de voorwaarden (toetsbaar, met termijn en eigenaar), het restrisico en wie het accepteert, wat het oordeel kan veranderen, en de managementreview met het stopcriterium en de datum van de volgende review.

De bezwaarroute werkt binnen drie maanden" is beter dan "er komt een bezwaarroute". Nog beter: "Werkt de bezwaarroute op 1 juli niet, dan gaan alle afwijzingen weer handmatig.

Noem ook de baten. Een memo dat alleen risico's noemt, overtuigt geen directeur. Bij Suribank: de doorlooptijd ging van 14 naar 1,6 werkdagen, en dat is voor klanten echt iets waard.

Het memo herhaalt niet het rapport. Het verwijst ernaar: "zie hoofdstuk 8".

Eén pagina. Lees hem voor aan iemand die het rapport niet kent. Begrijpt die wat er moet gebeuren?
