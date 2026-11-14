## Deze week

**Leerdoelen.** Na week 3 kan de student:

1. Fouten van een model per groep meten en vergelijken: het aandeel goedgekeurd, onterecht afgewezen en onterecht goedgekeurd.
2. Uitleggen waarom een model nauwkeuriger kan lijken en tegelijk oneerlijker kan worden.
3. Uitleggen waarom het weglaten van gevoelige kenmerken ongelijke behandeling niet vanzelf oplost.
4. Een uitkomst van een model in begrijpelijke taal uitleggen aan drie doelgroepen.
5. Benoemen welke ethische vragen erbij komen bij generatieve AI, en die toepassen op de eigen oplossing.
6. Voor de eigen oplossing alle 11 domeinen een eerste score geven, met het werk uit A-AI1, A-AI2 en A-DG als bewijs, en bepalen welk bewijs nog nodig is.

**Planning en deadlines.**

| Moment | Wat |
| --- | --- |
| Maandag 18 januari | Weekmodule 3 opent; feedforward op week 2 |
| Woensdag 20 januari, 23:59 | Weekcheck met standpunt, met de eigen uitkomsten van practicum 2; practicum 2 moet dus af zijn |
| Donderdag 21 januari | Online sessie van een uur: wat lieten de practica zien, en wat is anders bij generatieve AI? |
| Zondag 24 januari, 23:59 | Inleveren: practicum 3, evidence card 2 en 3 (individueel); K4 snelle scan (groep) |
| Maandag 25 januari | Feedforward-bericht; uiterste dag om van casus te wisselen |

**Tijdsbesteding voor de student.**

| Onderdeel | Uren |
| --- | --- |
| Clip 9 en 10, kaderclip B, studietekst generatieve AI, kernbron en weekcheck | 1,5 |
| Online sessie | 1 |
| Practicum 2 en 3 met evidence cards | 2 |
| K4 snelle scan en eerste gesprekken, in de groep | 3,5 |
| **Totaal** | **8 SBU** |

**Bestanden in de leeromgeving.**

| Bestand | Inhoud |
| --- | --- |
| suribank\_versie\_A.csv | De oefendata uit week 0: 1.200 aanvragen |
| suribank\_versie\_B.csv | Dezelfde aanvragen, maar met scheve historische labels voor het binnenland |
| suribank\_testset.csv | 1.000 nieuwe aanvragen met de juiste uitkomst: 600 van de kust, 400 uit het binnenland |
| practicum2\_3.ipynb | De Python-versie van practicum 2 en 3 |

Alle bestanden zitten samen in BK-ICT A-ET Practicum 2 en 3.zip op MyCampus.

## Voorbereiding

> **Week 3. Eerlijk voor wie, en wat is anders bij generatieve AI?**
>
> In week 0 zag je hoe vaak een model zich vergist. Deze week kijk je voor wie het zich vergist. Je ontdekt dat een model nauwkeuriger kan lijken en tegelijk oneerlijker kan worden. Je oefent met het uitleggen van een uitkomst, en je leest wat er anders is bij generatieve AI. Met je groep start je de nulmeting van jullie eigen oplossing.
>
> **Vóór donderdag:**
>
> 1. Bekijk clip 9: Fouten per groep. *6 minuten*
> 2. Maak practicum 2: het bias-experiment. *75 minuten*
> 3. Doe de weekcheck, met je eigen uitkomsten van practicum 2 en je standpunt, vóór woensdag 23:59. *20 minuten*
>
> **Donderdag 21 januari:** online sessie van een uur.
>
> **Vóór zondag 23:59:**
>
> 1. Bekijk clip 10: Uitleg die werkt. Lees de kernbron en de studietekst over generatieve AI. *37 minuten*
> 2. Bekijk kaderclip B: IEEE CertifAIEd, transparantie en bias toetsen. Beantwoord de vragen in de clip. 10 minuten
> 3. Maak practicum 3 en vul evidence card 2 en 3 in. *45 minuten*
> 4. Maak met je groep de snelle scan (K4) van jullie eigen oplossing. *3,5 uur, inclusief eerste gesprekken*

**Kernbron: Rudin (2019).** Samenvatting.

> Cynthia Rudin, Stop explaining black box machine learning models for high stakes decisions and use interpretable models instead. Nature Machine Intelligence, 2019.
>
> Rudin stelt dat organisaties voor beslissingen met grote gevolgen, zoals in rechtspraak, zorg en kredietverlening, geen ondoorzichtige modellen moeten gebruiken die ze achteraf proberen uit te leggen. Zo'n uitleg achteraf is een benadering en kan misleidend zijn. Gebruik in plaats daarvan een model dat zelf te begrijpen is, zoals een korte beslisboom of een eenvoudige puntentelling. Volgens Rudin kost dat vaak nauwelijks nauwkeurigheid, zeker bij gestructureerde gegevens zoals in een tabel. De vraag is dus niet alleen hoe goed een model is, maar ook of de mensen die ermee werken en de mensen over wie het beslist, kunnen begrijpen waarom het iets zegt.

## Kennisclips

### Clip 9. Fouten per groep (3 minuten)

Video: [link volgt op MyCampus]

Vragen in de clip:

- **Tussenvraag 1.** In het binnenland zijn er 50 goede betalers, van wie het model er 15 afwijst. Hoeveel procent is onterecht afgewezen? A. 15%. B. 30%. C. 50%.
- **Tussenvraag 2.** Een nieuw model is nauwkeuriger dan het oude. Is het daarmee ook eerlijker? A. Ja. B. Niet per se; kijk naar de fouten per groep.

### Clip 10. Uitleg die werkt (4 minuten)

Video: [link volgt op MyCampus]

Vragen in de clip:

- **Tussenvraag 1.** Welke uitleg is contrafactisch? A. "Uw score was 41%." B. "Met een looptijd van 24 in plaats van 12 maanden was uw aanvraag goedgekeurd."
- **Tussenvraag 2.** Een aanvrager hoort: "Uw woonplaats verlaagde uw score." Wat is het probleem? A. Geen; het is eerlijke uitleg. B. De aanvrager kan er niets aan doen, en het wijst op mogelijke ongelijke behandeling.

### Kaderclip B. IEEE CertifAIEd: transparantie en bias toetsen (7 minuten)

Video: [link volgt op MyCampus]

Vragen in de clip:

- **Tussenvraag 1.** Een bedrijf vertelt klanten niet dat een chatbot hun vragen beantwoordt, uit angst voor claims als het misgaat. Wat is dit volgens CertifAIEd? A. Een driver van transparantie. B. Een inhibitor: angst voor aansprakelijkheid.
- **Tussenvraag 2.** Een bank laat district weg uit het model, maar legt niet vast waarom, en meet de uitkomsten per regio niet. Welke drivers ontbreken vooral? A. Weten dat je met AI praat. B. Het gebruik van beschermde kenmerken onderbouwen en het gedrag per groep volgen.

## Studietekst: vier vragen bij generatieve AI

*Leestijd ongeveer 15 minuten. Kijk clip 4 uit week 0 terug als je die niet meer scherp hebt.*

Clip 9 en 10 gaan over een kredietmodel. Veel van jullie oplossingen zijn chatbots, assistenten of agents. Daarvoor gelden dezelfde vragen over fouten, eerlijkheid en uitleg, maar ze zien er anders uit. Deze vier vragen helpen bij de snelle scan van jullie eigen oplossing.

| Vraag | Wat er mis kan gaan | Waar je op let in de nulmeting | Domein |
| --- | --- | --- | --- |
| Kan het overtuigend fout zijn? | De assistent verzint een regel, een bedrag of een bron. Gebruikers geloven het, omdat het zeker klinkt | Wordt de kwaliteit van de antwoorden getest? Is vastgelegd wat de assistent niet mag beantwoorden? Weten gebruikers dat antwoorden fout kunnen zijn? | 8, 9, 11 |
| Waar gaan de gegevens heen? | Wat gebruikers typen of uploaden, gaat naar een externe dienst en wordt daar bewaard of gebruikt | Welke gegevens gaan erheen, en wat staat er in de afspraken met de aanbieder? Gebruik het werk uit A-DG | 4 |
| Weet de gebruiker dat het AI is? | Gebruikers denken met een mens te praten, of weten niet wat de assistent wel en niet kan | Is er een duidelijke melding, met uitleg over wat de assistent kan en hoe je een mens spreekt? | 6 |
| Helpt het iedereen even goed? | Wie in een andere taal schrijft, een ongebruikelijke naam heeft of een vraag anders formuleert, krijgt slechtere antwoorden | Is getest of verschillende gebruikers even goede antwoorden krijgen? | 5 |

Twee vragen spelen bij elke oplossing, maar bij generatieve AI net anders:

- **Kan een mens ingrijpen?** Kan een gebruiker eenvoudig een medewerker spreken? Leest iemand mee bij antwoorden met grote gevolgen? (domein 7)
- **Kan iemand het systeem misbruiken?** Kan een gebruiker de assistent met slimme vragen laten doen wat niet de bedoeling is, of er gevoelige informatie uit halen? Dat heet prompt injection. (domein 8)

In week 4 test je jullie eigen oplossing op deze punten, in practicum 4.

## Practicum 2: het bias-experiment

**Doel.** Je traint hetzelfde model op twee versies van de Suribank-data en meet de fouten apart voor de kust en het binnenland. Werk je in Python, gebruik dan practicum2\_3.ipynb; de stappen en vragen zijn hetzelfde. *Tijd: ongeveer 75 minuten. Af vóór woensdag 20 januari.*

**Het verhaal achter versie B.** Tot 2022 werden betalingen van klanten uit het binnenland via het kantoor in Albina met de hand ingeboekt. Betalingen kwamen daardoor vaak weken te laat in het systeem. Een deel van de klanten die gewoon betaalden, staat daardoor in de historische data als wanbetaler. Versie B bevat die scheve labels. De testset bevat de echte uitkomsten.

**Stap 1. Twee bestanden inladen.**

1. Start een nieuwe workflow. Sleep twee keer File naar het werkblad.
2. Laad in de eerste suribank\_versie\_A.csv en in de tweede suribank\_testset.csv.
3. Zet in allebei terugbetaald op target, en controleer dat aanvraag\_id op meta staat.

**Stap 2. De testset splitsen per regio.**

1. Sleep twee keer Select Rows (groep Transform) naar het werkblad en verbind de File met de testset met allebei.
2. Stel de eerste in op regio is kust, en de tweede op regio is binnenland.

**Stap 3. Testen per regio.**

1. Sleep Logistic Regression en twee keer Test and Score naar het werkblad.
2. Verbind voor elke Test and Score: File met versie A naar Data, de Select Rows van één regio naar Test Data, en Logistic Regression.
3. Kies in beide Test and Score de optie Test on test data en zet Target class op ja.
4. Verbind elke Test and Score met een eigen Confusion Matrix en kies bij Show de optie Number of instances.

**Stap 4. Noteren.** Reken per regio uit en vul de tabel in:

- **Goedgekeurd:** voorspeld ja, gedeeld door het totaal.
- **Onterecht afgewezen:** goede betalers met voorspelling nee, gedeeld door alle goede betalers.
- **Onterecht goedgekeurd:** slechte betalers met voorspelling ja, gedeeld door alle slechte betalers.

| Versie | Regio | CA | Goedgekeurd | Onterecht afgewezen | Onterecht goedgekeurd |
| --- | --- | --- | --- | --- | --- |
| A | Kust |  |  |  |  |
| A | Binnenland |  |  |  |  |
| B | Kust |  |  |  |  |
| B | Binnenland |  |  |  |  |
| B zonder gevoelige kenmerken | Kust |  |  |  |  |
| B zonder gevoelige kenmerken | Binnenland |  |  |  |  |

**Stap 5. Versie B.** Laad in de eerste File het bestand suribank\_versie\_B.csv. Alles werkt automatisch bij. Noteer opnieuw.

**Stap 6. Zonder gevoelige kenmerken.** Zet tussen de File met versie B en de twee Test and Score een Select Columns (groep Transform). Zet geslacht, district en regio op Ignored. Noteer opnieuw.

**Stap 7. Opslaan** als practicum2\_jouwnaam.ows.

**Vragen.**

1. Versie A: hoe groot is het verschil in onterecht afwijzen tussen kust en binnenland? Waar komt dat verschil vandaan, als woonplaats in deze data geen directe rol speelt bij terugbetalen?
2. Versie B: wat gebeurt er met goede betalers uit het binnenland? Wat gebeurt er met de CA voor het binnenland? Hoe kan dat?
3. Zonder gevoelige kenmerken: wat verandert er? Waarom kom je niet terug op het niveau van versie A?
4. Wie is verantwoordelijk voor het verschil: de bank die de data vastlegde, de leverancier die alle velden gebruikte, of de bank die niet per groep testte? Gebruik minstens één ethische lens.
5. Wat zou jij van Suribank eisen voordat zo'n model live mag? Formuleer één eis die je kunt controleren.

Vul na afloop evidence card 2 in. Het sjabloon staat in de leeromgeving.

## Practicum 3: uitlegbaarheid

**Doel.** Je vergelijkt een korte, leesbare beslisboom met een grote boom en met logistische regressie, en je legt de uitkomst voor één aanvrager uit aan drie doelgroepen. In Python staat dit practicum in hetzelfde notebook als practicum 2. *Tijd: ongeveer 45 minuten.*

**Stap 1. Drie modellen.**

1. Start een nieuwe workflow. Laad in een File suribank\_versie\_A.csv en in een tweede File suribank\_testset.csv. Zet in beide terugbetaald op target.
2. Zet na de File met versie A een Select Columns en zet geslacht, district en regio op Ignored.
3. Sleep twee keer Tree en één keer Logistic Regression naar het werkblad, en verbind Select Columns met alle drie.
4. Dubbelklik op de eerste Tree. Zet Limit the maximal tree depth to op 3. Geef de widget de naam Korte boom; de tweede noem je Lange boom.

**Stap 2. Vergelijken.** Sleep Test and Score naar het werkblad. Verbind Select Columns naar Data, de File met de testset naar Test Data, en de drie modellen. Kies Test on test data en Target class ja.

**Stap 3. In de korte boom kijken.** Verbind de Korte boom met een Tree Viewer. Lees de regels van boven naar beneden.

**Stap 4. In logistische regressie kijken.** Sleep Nomogram (groep Visualize) naar het werkblad en verbind Logistic Regression ermee. De lengte van elke balk laat zien hoeveel een kenmerk kan bijdragen aan de uitkomst.

**Stap 5. Eén aanvrager.** Sleep Predictions naar het werkblad. Verbind de File met de testset en de drie modellen. Zoek aanvraag TB0046 op.

**Stap 6. Opslaan** als practicum3\_jouwnaam.ows.

**Vragen.**

1. Welke CA hebben de drie modellen op de testset? Welk model is het best? Verrast je dat?
2. Schrijf de korte boom op als drie of vier regels in gewone taal, zoals: "Bij een looptijd van meer dan 24 maanden en geen eerdere achterstand …"
3. Welke drie kenmerken wegen in het Nomogram het zwaarst? Vind je dat redelijk?
4. Wat voorspelt elk model voor aanvraag TB0046, en met welke kans? Wat gebeurde er werkelijk?
5. Leg de uitkomst van de korte boom voor TB0046 uit aan drie doelgroepen, elk in hooguit 60 woorden: de aanvrager, de kredietmedewerker en een toezichthouder.
6. Rudin zegt: kies bij grote gevolgen een model dat zelf te begrijpen is. Ben je het daarmee eens voor Suribank? Wanneer zou je toch een complexer model kiezen?

Vul na afloop evidence card 3 in.

## K4 snelle scan

De snelle scan geeft alle 11 domeinen een eerste score, en bepaalt welke 4 tot 6 domeinen de groep in week 4 diep onderzoekt. Het is een eerste beeld, geen eindoordeel. *Omvang: één tabel van één tot twee pagina's.*

**Bewijs uit andere vakken.** Begin bij wat er al is. De ethische evaluatie uit A-AI1 geeft een eerste beeld. Voor domein 4 (data en privacy) en domein 11 (monitoring) gebruik je wat A-DG oplevert, voor de werking van de oplossing (domein 6 en 8) de documentatie uit A-AI2. Noem bij elke score de bron, ook als die uit een ander vak komt.

**Bij generatieve AI.** Gebruik de studietekst hierboven: de vier vragen horen bij domein 4, 5, 6, 8, 9 en 11. Kijk bij domein 7 ook of een gebruiker eenvoudig een mens kan spreken.

**Checklist uit IEEE CertifAIEd.** Gebruik bij domein 5 en 6 de drivers en inhibitors uit kaderclip B. Domein 6: weet de gebruiker dat die met AI te maken heeft, is de werking helder beschreven, en kan de gebruiker ingrijpen, feedback geven of een alternatief kiezen? Wordt er informatie achtergehouden uit angst voor aansprakelijkheid of om een bedrijfsgeheim te beschermen? Domein 5: is het gebruik of weglaten van beschermde kenmerken onderbouwd, wordt het gedrag per groep gevolgd, en kan de organisatie bias corrigeren? Is het proces zo onduidelijk dat niemand bias kan meten?

**Zo werkt ook een certificering.** De snelle scan lijkt op een beoordeling voor IEEE CertifAIEd: per doel bewijs, en een score die zegt hoe aantoonbaar iets geregeld is.

**AI-impactbeoordeling.** K2 uit week 2 en de nulmeting (snelle scan en diepe nulmeting) vormen samen jullie AI-impactbeoordeling. De AI-verordening noemt dat een grondrechteneffectbeoordeling (FRIA, artikel 27), ISO/IEC 42005 een impactbeoordeling.

**De schaal.** Een score zegt hoe aantoonbaar de organisatie iets geregeld heeft, niet hoe goed de bedoelingen zijn.

| Score | Betekenis | Herken je aan |
| --- | --- | --- |
| 0 | Niet aanwezig of onbekend | Niemand weet ervan, of er is geen enkel spoor van |
| 1 | Ad hoc | Er gebeurt iets, maar informeel en afhankelijk van personen |
| 2 | Gedeeltelijk beheerst | Er zijn afspraken of maatregelen, maar de uitvoering of het bewijs is onvolledig |
| 3 | Aantoonbaar beheerst | Er is beleid of een proces, verantwoordelijkheden zijn duidelijk, de uitvoering is aan te tonen en wordt gecontroleerd |

Een score zonder bewijs telt niet. Weet je het nog niet, noteer dan onbekend, met welk bewijs je nodig hebt.

**Twee kernvragen per domein.**

| # | Domein | Kernvragen |
| --- | --- | --- |
| 1 | Doel, noodzaak en proportionaliteit | Is vastgelegd welk probleem AI oplost en waarom AI nodig is? Zijn alternatieven en de verhouding tussen nut en risico afgewogen? |
| 2 | Governance en accountability | Is er een eigenaar die verantwoordelijk is en het systeem kan stopzetten? Is er beleid voor AI, ook voor afspraken met leveranciers? |
| 3 | Stakeholders, mensenrechten en impact | Zijn de gevolgen voor betrokkenen en kwetsbare groepen onderzocht? Worden betrokkenen gehoord bij ontwerp of evaluatie? |
| 4 | Data en privacy | Is vastgelegd welke gegevens worden gebruikt, waarvoor en hoe lang? Zijn privacyrisico's beoordeeld, ook bij doorgifte en hergebruik? |
| 5 | Fairness, bias en non-discriminatie | Is getest of het systeem voor relevante groepen even goed werkt? Is vastgelegd welke verschillen acceptabel zijn en wat er gebeurt als die worden overschreden? |
| 6 | Transparantie, uitlegbaarheid en traceerbaarheid | Weten betrokkenen dat AI wordt gebruikt en waarvoor? Kan een uitkomst worden uitgelegd en achteraf worden nagegaan? |
| 7 | Menselijke controle, bezwaar en herstel | Kan een bevoegde mens met genoeg tijd en informatie ingrijpen en afwijken? Kunnen betrokkenen bezwaar maken en een herbeoordeling krijgen? |
| 8 | Veiligheid, security en robuustheid | Zijn toegang, beveiliging en logging geregeld? Is bekend wat er gebeurt bij fouten, misbruik of veranderende omstandigheden? |
| 9 | AI-geletterdheid en competenties | Weten gebruikers en beslissers wat het systeem wel en niet kan? Weten ze wanneer ze moeten escaleren? |
| 10 | Duurzaamheid en bredere impact | Zijn sociale, economische en ecologische gevolgen overwogen? Ook voor mensen buiten de directe gebruikers? |
| 11 | Monitoring, audit en verbetering | Worden prestaties, fouten, klachten en verschillen tussen groepen regelmatig gemeten? Leidt een afwijking tot actie? |

**Sjabloon.** Per domein één rij met deze kolommen: domein, eerste score (0 tot 3 of onbekend), waarop die is gebaseerd, welk bewijs nog nodig is, en diep onderzoeken ja of nee.

**Voorbeeld: een handelsbedrijf dat cv's laat rangschikken door AI.** Een fictieve casus; niet de Suribank-casus.

| Domein | Eerste score | Waarop gebaseerd | Bewijs nog nodig | Diep? |
| --- | --- | --- | --- | --- |
| 1. Doel | 2 | HR-notitie noemt tijdwinst als doel | Zijn alternatieven overwogen? | Nee |
| 2. Governance | 1 | HR-manager noemt zich eigenaar, maar er is geen beleid | Wie mag het stopzetten? | Ja |
| 3. Stakeholders | 0 | Kandidaten zijn nergens genoemd | Gesprek met recruiter | Ja |
| 4. Data en privacy | 1 | Cv's gaan naar een buitenlandse leverancier | Contract met de leverancier | Nee |
| 5. Fairness | Onbekend | Geen informatie over testen per groep | Testrapport, gesprek met IT | Ja |
| 6. Transparantie | 1 | Vacaturetekst noemt geen AI | Afwijzingsmail | Nee |
| 7. Menselijke controle | 1 | Recruiters zien alleen de top 20 | Werkinstructie, aantal afwijkingen | Ja |
| 8. Veiligheid | 2 | Toegang is beperkt tot HR | Logging | Nee |
| 9. AI-geletterdheid | 1 | Korte instructie door de leverancier | Trainingsmateriaal | Nee |
| 10. Duurzaamheid | 0 | Niet overwogen | Geen; weinig relevant voor deze casus | Nee |
| 11. Monitoring | 0 | Alleen aantal vacatures bijgehouden | Rapportages | Ja |

**Welke domeinen diep?** Kies er 4 tot 6, met deze regels:

1. Domeinen die de meest kwetsbare stakeholder uit K2 het hardst raken.
2. Domeinen met een score van 0, 1 of onbekend.
3. Domeinen waar in K3 een risicopunt zit.
4. Gaat het om beslissingen over mensen, neem dan altijd fairness (5) en menselijke controle (7) mee.
5. Is de oplossing een chatbot, assistent of agent, neem dan ook transparantie (6) mee.

**Inleveren.** Uiterlijk zondag 24 januari, 23:59, met een AI-verklaring. In week 4 werken jullie de gekozen domeinen uit met bewijs.

## Online sessie donderdag 21 januari

Een uur, online, met opname; camera is optioneel.

| Tijd | Onderdeel |
| --- | --- |
| 0:00 tot 0:08 | Stelling: twee studenten verdedigen en bestrijden de stelling uit de weekcheck, daarna een peiling in de chat |
| 0:08 tot 0:25 | Wat lieten de practica zien, wat is anders bij generatieve AI, en wat toetst IEEE CertifAIEd? |
| 0:25 tot 0:50 | Wie draagt de fouten in jullie oplossing? Groepswerk in aparte kamers |
| 0:50 tot 1:00 | Vragen en uitleg snelle scan |

**Neem mee:** je eigen uitkomsten van practicum 2 (uit de weekcheck) en je standpunt over de stelling: *"Een bank mag een model gebruiken dat nauwkeuriger is dan medewerkers, ook als het één groep vaker onterecht afwijst."*

**Groepswerk.** Elke groep beantwoordt drie vragen voor de eigen oplossing. Welke gebruikers of betrokkenen lopen het risico dat de fouten bij hen terechtkomen? Hoe zou je dat kunnen meten of testen? Welke score krijgen domein 5 en 7 nu in jullie snelle scan, en waarop baseren jullie die? Groepen met een chatbot of agent nemen bij de eerste vraag ook de vier vragen uit de studietekst mee.

## Weekcheck

Sluit woensdag 20 januari om 23:59.

 Vijf vragen, een logboekregel en een standpunt.

1. **Practicum 2, versie A.** Welk percentage van de goede betalers werd onterecht afgewezen, aan de kust en in het binnenland? *Open, twee getallen.*
2. **Practicum 2, versie B.** Dezelfde vraag voor versie B. *Open, twee getallen.*
3. **In versie B steeg de nauwkeurigheid voor het binnenland, terwijl meer goede betalers werden afgewezen. Hoe kan dat?** A. Het model werd echt beter. B. In het binnenland betaalt minder dan de helft terug; vaker afwijzen is dan vaker goed, terwijl de goede betalers de prijs betalen.
4. **Wat zegt Rudin?** A. Leg een ondoorzichtig model altijd achteraf uit. B. Kies bij beslissingen met grote gevolgen een model dat zelf te begrijpen is.
5. **Een bedrijf vertelt klanten niet dat een chatbot hun vragen beantwoordt, uit angst voor claims als het misgaat. Wat is dit volgens IEEE CertifAIEd?** A. Een driver van transparantie. B. Een inhibitor: angst voor aansprakelijkheid.

**Logboekregel.** Wat verraste je in practicum 2, en wat heb ik deze week aan de snelle scan bijgedragen?

**Standpunt,** hoogstens 100 woorden. De stelling van de online sessie: *"Een bank mag een model gebruiken dat nauwkeuriger is dan medewerkers, ook als het één groep vaker onterecht afwijst."* Ben je het eens of oneens? Geef één argument, en noem één tegenargument dat je serieus neemt.

## Bijlage: tekst van de kennisclips (meelezen)

### Clip 9. Fouten per groep (3 minuten)

**Dia 1. Het gemiddelde verbergt.** Het Suribank-model heeft 69% goed. Dat zegt niets over de vraag of het voor iedereen even goed werkt. Bij Gender Shades was het gemiddelde ook prima, terwijl één groep tot 35% foute uitkomsten kreeg. Daarom meet je fouten per groep.

**Dia 2. Drie vragen per groep.** Stel per groep drie vragen. Welk deel wordt goedgekeurd? Van de mensen die wél zouden terugbetalen: welk deel wordt onterecht afgewezen? En van de mensen die niet zouden terugbetalen: welk deel wordt onterecht goedgekeurd?

**Dia 3. Een rekenvoorbeeld.** In groep X worden 20 van de 100 goede betalers afgewezen: 20% onterecht afgewezen. In groep Y zijn dat er 40: 40%. Een goede betaler uit groep Y heeft dus twee keer zoveel kans om ten onrechte geen lening te krijgen. Het idee dat goede betalers in elke groep dezelfde kans moeten hebben, heet gelijke kansen.

> **Tussenvraag 1.** In het binnenland zijn er 50 goede betalers, van wie het model er 15 afwijst. Hoeveel procent is onterecht afgewezen? A. 15%. B. 30%. C. 50%.

**Dia 4. Welke eerlijkheid?** Er zijn meerdere manieren om eerlijk te definiëren. Elke groep even vaak goedkeuren. Goede betalers in elke groep even weinig onterecht afwijzen. Of ervoor zorgen dat een goedkeuring in elke groep even betrouwbaar is. Als groepen verschillen in hoe vaak ze terugbetalen, kun je niet aan alle drie tegelijk voldoen. Je moet dus kiezen, en die keuze onderbouwen. Dat is een ethische keuze, geen technische.

**Dia 5. Nauwkeuriger en oneerlijker tegelijk.** Stel dat in een groep minder dan de helft terugbetaalt. Een model dat iedereen in die groep afwijst, heeft dan voor die groep vaker gelijk. Maar alle goede betalers in die groep betalen de prijs. Een hogere nauwkeurigheid kan dus samengaan met meer onrecht. In practicum 2 zie je dat met eigen ogen.

> **Tussenvraag 2.** Een nieuw model is nauwkeuriger dan het oude. Is het daarmee ook eerlijker? A. Ja. B. Niet per se; kijk naar de fouten per groep.

**Dia 6. Samengevat.** Meet per groep: goedgekeurd, onterecht afgewezen en onterecht goedgekeurd. Er bestaan meerdere definities van eerlijk, en je moet kiezen. Nauwkeuriger is niet hetzelfde als eerlijker.

### Clip 10. Uitleg die werkt (4 minuten)

**Dia 1. Drie begrippen.** Transparantie: mensen weten dat AI wordt gebruikt en waarvoor. Uitlegbaarheid: je kunt uitleggen waarom een bepaalde uitkomst eruit kwam. Traceerbaarheid: je kunt achteraf nagaan wat er gebeurde, met welke gegevens en welke versie van het model.

**Dia 2. Twee wegen naar uitleg.** Je kunt een model kiezen dat zelf te begrijpen is, zoals een beslisboom met een paar vragen of een eenvoudige puntentelling. Of je gebruikt een complex model en maakt achteraf een uitleg, bijvoorbeeld van de belangrijkste factoren. Die uitleg achteraf is een benadering. Rudin pleit daarom voor de eerste weg bij beslissingen met grote gevolgen.

**Dia 3. Uitleg per doelgroep.** De aanvrager wil weten welke factoren de doorslag gaven en wat die zelf kan doen. De medewerker wil weten hoe zeker het model is en wanneer afwijken verstandig is. De toezichthouder wil weten hoe het model werkt, hoe het getest is, en of het voor alle groepen goed werkt. Eén uitleg voor iedereen werkt dus niet.

**Dia 4. Uitleg met een als-dan.** Een sterke vorm van uitleg zegt wat er anders had moeten zijn voor een andere uitkomst. Dat heet een contrafactische uitleg. Die is begrijpelijk en geeft de aanvrager iets om mee te doen. Maar let op: als het antwoord is "als u in Paramaribo had gewoond", dan zegt de uitleg vooral iets over de eerlijkheid van het model.

> **Tussenvraag 1.** Welke uitleg is contrafactisch? A. "Uw score was 41%." B. "Met een looptijd van 24 in plaats van 12 maanden was uw aanvraag goedgekeurd."

**Dia 5. Uitleg en menselijke controle.** Een medewerker kan alleen zinvol afwijken als die begrijpt waarom het model iets zegt. En een aanvrager kan alleen bezwaar maken als die weet waarop de beslissing rust. Uitleg is dus een voorwaarde voor menselijke controle en voor bezwaar.

> **Tussenvraag 2.** Een aanvrager hoort: "Uw woonplaats verlaagde uw score." Wat is het probleem? A. Geen; het is eerlijke uitleg. B. De aanvrager kan er niets aan doen, en het wijst op mogelijke ongelijke behandeling.

**Dia 6. Samengevat.** Transparantie, uitlegbaarheid en traceerbaarheid zijn drie verschillende dingen. Kies bij grote gevolgen liever een begrijpelijk model. Pas de uitleg aan de doelgroep aan, en gebruik waar het kan een als-dan.

### Kaderclip B. IEEE CertifAIEd: transparantie en bias toetsen (7 minuten)

**Dia 1. Een certificering voor ethiek.** IEEE, de grootste beroepsvereniging van ingenieurs, beoordeelt AI-systemen met CertifAIEd. Een beoordelaar kijkt naar vier onderdelen: transparantie, verantwoording, algoritmische bias en privacy. In ons kader hoort dat bij de laag wat: transparantie is domein 6, verantwoording domein 2, bias domein 5 en privacy domein 4.

**Dia 2. Drivers en inhibitors.** Per onderdeel kijkt CertifAIEd naar twee soorten factoren. Drivers maken het waarschijnlijker dat een systeem ethisch werkt. Inhibitors werken het tegen, vaak om begrijpelijke redenen. Wie alleen de drivers controleert, mist waarom goede bedoelingen in de praktijk stranden.

**Dia 3. Transparantie.** Drivers zijn onder meer: de gebruiker weet meteen dat die met AI praat, de werking is helder beschreven, en de gebruiker kan ingrijpen, feedback geven en heeft een alternatief. Inhibitors zijn: gedrag verhullen of mensen manipuleren, angst voor aansprakelijkheid, en een bedrijfsgeheim beschermen. Een organisatie die zegt "dat kunnen we niet vertellen", heeft vaak een van die drie redenen.

> **Tussenvraag 1.** Een bedrijf vertelt klanten niet dat een chatbot hun vragen beantwoordt, uit angst voor claims als het misgaat. Wat is dit volgens CertifAIEd? A. Een driver van transparantie. B. Een inhibitor: angst voor aansprakelijkheid.

**Dia 4. Algoritmische bias.** Drivers zijn onder meer: de context van alle betrokkenen is begrepen, het gebruik of weglaten van beschermde kenmerken zoals geslacht of district is onderbouwd, het gedrag per groep wordt gevolgd, ook na livegang, en de organisatie kan bias corrigeren als die opduikt. De inhibitor: een proces dat zo ondoorzichtig is, met onduidelijke data en bronnen, dat niemand de bias kan meten. Dat zag je in practicum 2.

**Dia 5. Bewijs per doel, met een score.** Een beoordelaar vraagt per doel bewijs en geeft een score. Dat is dezelfde logica als jullie snelle scan: een score zonder bewijs telt niet. Gebruik de drivers en inhibitors als checklist bij domein 5 en 6 van de nulmeting.

> **Tussenvraag 2.** Een bank laat district weg uit het model, maar legt niet vast waarom, en meet de uitkomsten per regio niet. Welke drivers ontbreken vooral? A. Weten dat je met AI praat. B. Het gebruik van beschermde kenmerken onderbouwen en het gedrag per groep volgen.

**Dia 6. Samengevat.** Vier onderdelen, die passen bij domein 2, 4, 5 en 6. Kijk naar wat helpt én naar wat tegenwerkt. En onderbouw elke score met bewijs, zoals een echte beoordelaar dat doet.
