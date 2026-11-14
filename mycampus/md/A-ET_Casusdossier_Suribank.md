Dit dossier bevat twaalf stukken over het kredietmodel van Suribank, een fictieve Surinaamse bank. Het is de oefencasus van de module en het uitgewerkte voorbeeld bij elk instrument en bij de practica. Groepen die met hun eigen oplossing uit A-AI2 vastlopen, gebruiken het als casus en bewijsbron voor hun rapport. Alle personen, bedragen en organisaties zijn verzonnen; elke gelijkenis met bestaande organisaties berust op toeval.

## Over dit dossier

**De situatie.** Suribank N.V. heeft 140 medewerkers en kantoren in Paramaribo, Nickerie en Albina. Sinds 1 september 2026 gebruikt de bank het kredietmodel Snel Krediet, gebouwd door Kredimo Analytics B.V. in Utrecht. Het model beoordeelt aanvragen voor consumptief krediet. Jullie onderzoeken of dit verantwoord gebeurt, en adviseren Suribank.

**Zo gebruik je het dossier.** Lees alle stukken vóór je de nulmeting scoort. Elk stuk heeft een nummer. Verwijs in je rapport naar het nummer als bewijs, bijvoorbeeld: "medewerkers wijken zelden af van het advies \[D11\]". Let op tegenstrijdigheden tussen stukken: die zijn vaak het interessantst. Wat niet in het dossier staat, is onbekend. Noteer het als onzekerheid en vul het niet zelf in.

**Inhoud.**

| Nr | Stuk | Soort bewijs |
| --- | --- | --- |
| D1 | Projectvoorstel en business case | Document |
| D2 | Modeldocumentatie van de leverancier | Document |
| D3 | Werkinstructie voor kredietmedewerkers | Document |
| D4 | Standaard afwijzingsbrief | Document |
| D5 | Privacyverklaring, uittreksel | Document |
| D6 | Overeenkomst met de leverancier, uittreksel | Document |
| D7 | Interview met het hoofd kredietverlening | Gesprek |
| D8 | Interview met een kredietmedewerker in Albina | Gesprek |
| D9 | Interview met een medewerker klantenservice | Gesprek |
| D10 | Interview met een data-analist van IT | Gesprek |
| D11 | Maandrapportage kredietverlening, oktober 2026 | Cijfers |
| D12 | Drie klachten van klanten | Klachten |

De oefendataset suribank\_kredietaanvragen.csv uit de practica is een geanonimiseerde steekproef van 1.200 aanvragen uit de trainingsdata van het model.

## D1. Projectvoorstel en business case

*Intern document. Opgesteld door het hoofd kredietverlening, goedgekeurd door de directie op 12 mei 2026.*

**Aanleiding.** Een aanvraag voor consumptief krediet duurt gemiddeld 14 werkdagen. Klanten stappen over naar concurrenten en naar informele geldschieters. Medewerkers beoordelen vergelijkbare aanvragen verschillend. De werkdruk op de afdeling is hoog.

**Voorstel.** Invoering van Snel Krediet: een AI-model dat elke aanvraag een score geeft voor de kans op terugbetaling. Aanvragen tot SRD 50.000 worden automatisch afgehandeld. Grotere aanvragen beoordeelt een kredietmedewerker met het advies van het model.

**Doelen.**

| Doel | Huidig | Streven |
| --- | --- | --- |
| Gemiddelde doorlooptijd | 14 werkdagen | Minder dan 2 werkdagen |
| Kosten per aanvraag | 100% | 30% lager |
| Aandeel wanbetaling | 9% | Niet hoger dan nu |
| Aantal aanvragen per maand | 450 | 600 |

**Leverancier.** Kredimo Analytics B.V. uit Utrecht levert het model en het onderhoud. Kredimo heeft ervaring met kredietmodellen in Europa en het Caribisch gebied.

**Risico's.**

| Risico | Inschatting | Maatregel |
| --- | --- | --- |
| Technische storing | Middel | Onderhoudscontract met Kredimo |
| Weerstand van medewerkers | Middel | Training door Kredimo |
| Reputatierisico | Laag | Het model is door de leverancier getest |

**Planning.** Ontwikkeling juni tot augustus 2026. Livegang op 1 september 2026. Evaluatie na zes maanden.

**Besluit directie.** Akkoord, onder voorwaarde dat de doorlooptijd binnen drie maanden onder de twee dagen ligt.

## D2. Modeldocumentatie van de leverancier

*Kredimo Analytics B.V., Model Factsheet Snel Krediet, versie 1.0, augustus 2026.*

**Doel van het model.** Het voorspellen van de kans dat een aanvrager van consumptief krediet de lening terugbetaalt zonder achterstand van meer dan 90 dagen.

**Modeltype.** Logistische regressie.

**Trainingsdata.** 8.412 goedgekeurde leningen van Suribank uit de periode januari 2019 tot en met juni 2025. Aanvragen die destijds zijn afgewezen, zijn niet opgenomen, omdat daarvan geen uitkomst bekend is.

**Invoervariabelen.** Leeftijd, geslacht, district, regio, soort dienstverband, jaren in huidig werk, netto maandinkomen, bestaande schulden, gevraagd bedrag, looptijd, eerdere betalingsachterstand en klantduur. Alle beschikbare velden zijn meegenomen om de voorspellende kracht te maximaliseren.

**Ontbrekende waarden.** Bij 4% van de aanvragen ontbreekt het maandinkomen. Deze waarden zijn aangevuld met het mediane inkomen van alle aanvragers.

**Validatie.** Het model is getest op een willekeurige 30% van de data.

| Maat | Waarde |
| --- | --- |
| Nauwkeurigheid | 69% |
| AUC | 0,75 |

Het model presteert daarmee ruim boven een willekeurige gok.

**Advies over de drempel.** Wij adviseren goedkeuring bij een score van 60% of hoger.

**Uitleg per aanvraag.** Het model geeft per aanvraag een score. Een toelichting per aanvraag, met de belangrijkste factoren, is technisch mogelijk, maar maakt geen deel uit van de huidige levering.

**Beperkingen.** Het model is gevalideerd op historische data van Suribank. Prestaties in andere omstandigheden kunnen afwijken.

**Onderhoud.** Hertraining van het model gebeurt op verzoek van de klant, tegen een aanvullende vergoeding.

## D3. Werkinstructie voor kredietmedewerkers

*Werkinstructie WI-KR-07, Beoordeling consumptief krediet met Snel Krediet, versie 1, ingangsdatum 1 september 2026.*

1. De baliemedewerker voert de aanvraag in het kernsysteem in en scant de bewijsstukken.
2. Snel Krediet berekent automatisch een score en een advies.
3. **Aanvragen tot en met SRD 50.000:** het advies wordt automatisch overgenomen. De klant ontvangt binnen één werkdag bericht.
4. **Aanvragen boven SRD 50.000:** de kredietmedewerker beoordeelt het dossier met het advies van Snel Krediet. Richttijd: 15 minuten per dossier.
5. De medewerker volgt in principe het advies van Snel Krediet.
6. Wil de medewerker afwijken van het advies, dan vult die formulier F-12 in met de reden. Afwijken is alleen toegestaan na schriftelijk akkoord van het afdelingshoofd.
7. Afwijkingen worden maandelijks gerapporteerd aan het hoofd kredietverlening.
8. Vragen van klanten over een afwijzing worden doorverwezen naar de klantenservice.

## D4. Standaard afwijzingsbrief

*Sjabloon BR-KR-03, gebruikt sinds 1 september 2026.*

> Geachte heer, mevrouw,
>
> Hartelijk dank voor uw aanvraag voor een persoonlijke lening bij Suribank.
>
> Na zorgvuldige beoordeling moeten wij u helaas meedelen dat uw aanvraag op dit moment niet voldoet aan onze acceptatiecriteria. Wij kunnen uw aanvraag daarom niet honoreren.
>
> U kunt na drie maanden een nieuwe aanvraag indienen.
>
> Voor vragen kunt u contact opnemen met onze klantenservice.
>
> Met vriendelijke groet,
>
> Afdeling Kredietverlening, Suribank N.V.

## D5. Privacyverklaring, uittreksel

*Gepubliceerd op de website van Suribank, laatst gewijzigd in maart 2023.*

> **Welke gegevens verzamelen wij?** Wij verzamelen gegevens die u aan ons verstrekt, zoals uw naam, adres, geboortedatum, identiteitsgegevens, inkomen en financiële situatie, en gegevens over uw gebruik van onze producten.
>
> **Waarvoor gebruiken wij uw gegevens?** Om onze diensten te leveren, om uw aanvragen te beoordelen, om fraude te voorkomen, en om onze dienstverlening te verbeteren.
>
> **Met wie delen wij uw gegevens?** Wij kunnen uw gegevens delen met zorgvuldig geselecteerde dienstverleners die ons helpen bij onze dienstverlening, ook buiten Suriname. Wij zorgen ervoor dat zij uw gegevens vertrouwelijk behandelen.
>
> **Hoe lang bewaren wij uw gegevens?** Zolang dat nodig is voor de doeleinden waarvoor ze zijn verzameld.
>
> **Uw rechten.** U kunt ons vragen welke gegevens wij van u hebben. Neem hiervoor contact op met onze klantenservice.

## D6. Overeenkomst met de leverancier, uittreksel

*Dienstverleningsovereenkomst tussen Suribank N.V. en Kredimo Analytics B.V., getekend op 3 juni 2026.*

> **Artikel 4. Gegevensverwerking.** Suribank levert dagelijks de aanvraaggegevens aan Kredimo via een beveiligde verbinding. Kredimo verwerkt de gegevens in een cloudomgeving binnen de Europese Unie.
>
> **Artikel 5. Gebruik van gegevens.** Kredimo mag geanonimiseerde gegevens van Suribank gebruiken voor de verbetering en ontwikkeling van haar eigen producten.
>
> **Artikel 7. Onderhoud.** Kredimo zorgt voor de technische beschikbaarheid van het model. Aanpassing of hertraining van het model gebeurt op verzoek van Suribank, tegen het geldende uurtarief.
>
> **Artikel 9. Aansprakelijkheid.** Kredimo is niet aansprakelijk voor beslissingen die Suribank neemt op basis van de uitkomsten van het model. De aansprakelijkheid van Kredimo is beperkt tot het bedrag van de jaarlijkse licentievergoeding.
>
> **Artikel 11. Duur.** De overeenkomst geldt voor drie jaar en wordt daarna stilzwijgend verlengd.

De overeenkomst bevat geen bepalingen over inzage in het model, controle door derden, of testen van de prestaties per groep.

## D7. Interview met het hoofd kredietverlening

*Gesprek op 20 oktober 2026, hoofdkantoor Paramaribo, 40 minuten. Verslag goedgekeurd door de respondent.*

**Waarom koos Suribank voor AI?** "We verloren klanten door de lange wachttijd. Nu heeft een klant binnen anderhalve dag antwoord. Dat is een enorme verbetering."

**Wie is verantwoordelijk voor Snel Krediet?** "IT beheert het systeem, Kredimo onderhoudt het model, en ik ben verantwoordelijk voor de kredietportefeuille. Een apart AI-beleid hebben we niet; dat vonden we voor één model niet nodig."

**Wie mag het systeem stopzetten?** "Dat is nooit aan de orde geweest. Ik neem aan de directie."

**Is getest of het model voor alle klanten even goed werkt?** "Kredimo heeft het model getest en het scoort 69%. Het model is objectief: het kijkt alleen naar cijfers, niet naar wie je bent."

**In Albina wordt vaker afgewezen. Hoe verklaart u dat?** "Daar is het risico nu eenmaal hoger. Veel klanten hebben geen vast inkomen. Het model ziet dat gewoon scherper dan wij vroeger."

**Weten klanten dat een model meebeslist?** "Dat staat niet in de brief. Het gaat klanten om de uitkomst, niet om hoe we daar komen."

**Hoe zijn medewerkers voorbereid?** "Kredimo heeft een training van een uur gegeven, over hoe je de score leest."

**Hoe houdt u bij of het goed gaat?** "Elke maand krijg ik een rapport met de aantallen en de doorlooptijd. Over wanbetaling weten we pas in de loop van 2027 meer."

**Wat zou u willen verbeteren?** "Ik wil het automatische deel uitbreiden naar SRD 75.000. Dat scheelt nog meer tijd."

## D8. Interview met een kredietmedewerker in Albina

*Gesprek op 22 oktober 2026, kantoor Albina, 35 minuten. Verslag goedgekeurd door de respondent.*

**Hoe werkt u met Snel Krediet?** "Kleine aanvragen zie ik niet meer; die gaan automatisch. Bij grotere aanvragen krijg ik de score en het advies te zien. Ik heb ongeveer een kwartier per dossier."

**Wat voor klanten heeft u?** "Veel mensen hier werken op de markt, in de goudsector of in het transport over de rivier. Ze verdienen vaak goed, maar contant. Een loonstrook hebben ze niet. Vroeger kende ik mijn klanten en wist ik wie betrouwbaar was."

**Wat ziet u sinds de invoering?** "Veel meer afwijzingen. Ook van klanten die al jaren netjes betalen. Het systeem kent onze klanten niet."

**Wijkt u weleens af van het advies?** "Eén keer. Ik moest formulier F-12 invullen en het akkoord van het afdelingshoofd in Paramaribo vragen. Dat duurde drie dagen, en de klant was intussen naar een geldschieter gegaan. Sindsdien doe ik het niet meer. Als het misgaat met een lening die ik zelf goedkeur, ligt het bij mij. Als het model het zegt, niet."

**Wat vragen klanten u?** "Waarom ze zijn afgewezen. Dat kan ik niet uitleggen, want ik zie alleen een getal. Ik zeg dan dat ze het na drie maanden opnieuw kunnen proberen."

**Welke training heeft u gehad?** "De training van een uur. Daar ging het over het scherm, niet over wanneer je het model niet moet vertrouwen."

## D9. Interview met een medewerker klantenservice

*Gesprek op 21 oktober 2026, hoofdkantoor Paramaribo, 25 minuten. Verslag goedgekeurd door de respondent.*

**Wat merkt u van Snel Krediet?** "Sinds september bellen veel meer mensen over een afwijzing. Ze zijn boos, omdat ze niet snappen waarom."

**Wat zegt u dan?** "We hebben een vaste tekst: uw aanvraag voldoet niet aan onze criteria. Meer weet ik zelf ook niet. Ik zie de score niet, en ik weet niet hoe het model werkt."

**Kan een klant bezwaar maken?** "Er is geen aparte procedure. We adviseren om na drie maanden opnieuw aan te vragen. Als iemand echt doorzet, noteer ik een klacht, en die gaat naar de afdeling kredietverlening."

**Weten klanten dat er een computer meebeslist?** "Nee. Sommigen denken dat de medewerker in hun filiaal hen niet mag."

**Wat zou helpen?** "Als ik kon zeggen wat de belangrijkste reden was. En als er iemand was die een afwijzing opnieuw kan bekijken."

## D10. Interview met een data-analist van IT

*Gesprek op 23 oktober 2026, online, 45 minuten. Verslag goedgekeurd door de respondent.*

**Hoe is Snel Krediet technisch ingericht?** "Elke nacht sturen we de nieuwe aanvragen via een versleutelde verbinding naar de cloudomgeving van Kredimo in Europa. De score komt binnen enkele seconden terug in ons kernsysteem."

**Hoe is de beveiliging geregeld?** "Goed. Alleen kredietmedewerkers en twee mensen van IT kunnen bij de scores. Alle inlogs en wijzigingen worden gelogd. We hebben vorige maand een penetratietest laten doen; die liet geen grote problemen zien."

**Waarom staan geslacht en district in het model?** "Kredimo heeft alle beschikbare velden gebruikt. Ik heb dat wel gezien, maar niemand heeft gevraagd of dat de bedoeling was."

**Wordt bijgehouden hoe het model presteert per groep?** "Nee. We rapporteren aantallen en doorlooptijd. Prestaties per groep of per filiaal analyseren we niet. Daar hebben we ook geen opdracht voor."

**Is er een privacyanalyse gemaakt, zoals een DPIA?** "Nee. Dat is in Suriname niet verplicht, dus daar is niet naar gekeken."

**Wordt het model bijgewerkt?** "Het draait nog op versie 1.0. Hertraining kost extra, en daar is nog geen besluit over. Ik weet eerlijk gezegd ook niet wie daarover beslist: wij, de afdeling krediet of de directie."

## D11. Maandrapportage kredietverlening, oktober 2026

*Opgesteld door IT voor het hoofd kredietverlening.*

| Kenmerk | September 2026 | Oktober 2026 |
| --- | --- | --- |
| Aanvragen | 548 | 612 |
| Automatisch afgehandeld (tot SRD 50.000) | 352 | 401 |
| Beoordeeld door een medewerker | 196 | 211 |
| Afgewezen, totaal | 39% | 42% |
| Afgewezen in Paramaribo | 35% | 37% |
| Afgewezen in Nickerie | 41% | 44% |
| Afgewezen in Albina | 58% | 63% |
| Medewerker week af van het advies | 3 van 196 | 4 van 211 |
| Gemiddelde doorlooptijd | 1,8 werkdagen | 1,6 werkdagen |
| Klachten over een afwijzing | 9 | 23 |
| Wanbetaling | Nog niet bekend | Nog niet bekend |

**Toelichting.** De doelen voor doorlooptijd en aantal aanvragen worden ruim gehaald. De wanbetaling is pas na zes maanden te beoordelen.

## D12. Drie klachten van klanten

*Geanonimiseerd. Ingediend bij de klantenservice in oktober 2026. Alle drie afgehandeld met het standaardantwoord.*

**Klacht 1, kantoor Albina.** "Ik verkoop al twaalf jaar op de markt en ben negen jaar klant bij Suribank. Ik heb altijd netjes afbetaald. Nu krijg ik binnen een dag een brief dat ik niet voldoe aan jullie criteria. Niemand kan me zeggen waarom. Moet ik nu naar een geldschieter?"

**Klacht 2, kantoor Paramaribo.** "Mijn broer en ik werken bij hetzelfde bedrijf en verdienen hetzelfde. We vroegen in dezelfde week een lening aan. Hij kreeg die wel, ik niet. Is dat toeval?"

**Klacht 3, kantoor Nickerie.** "Ik wilde geld lenen voor een nieuwe boot voor mijn visbedrijf. Aan de balie zeiden ze dat een persoonlijke lening het snelst ging. Afgewezen, zonder uitleg. Na drie maanden heb ik opnieuw aangevraagd: weer afgewezen, weer zonder uitleg. Met wie kan ik praten?"
