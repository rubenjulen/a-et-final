import json
S=[
("B0","Titelkaart \"Kaderclip B · IEEE CertifAIEd\". Een zegel met vier lege vakken draait in beeld.",[
 ("Kaderclip B: hoe toets je of een AI-systeem eerlijk en open werkt?",0.5),
 ("In clip 9 en 10 zag je fouten per groep en uitleg die werkt. Nu kijk je mee met een echte beoordelaar.",0.9)]),
("B1","De vier vakken van het zegel vullen zich: transparantie, verantwoording, algoritmische bias, privacy. Daarna schuift elk vak naar zijn domein in de lijst van 11 domeinen: 6, 2, 5 en 4.",[
 ("IEEE is de grootste beroepsvereniging van ingenieurs ter wereld.",0.5),
 ("Met CertifAIEd beoordeelt IEEE of een AI-systeem ethisch werkt. Een systeem dat slaagt, krijgt een keurmerk.",0.5),
 ("Er is ook een certificaat voor de mensen die zulke beoordelingen doen. Je kijkt dus mee met een vak.",0.5),
 ("Een beoordelaar kijkt naar vier onderdelen: transparantie, verantwoording, algoritmische bias en privacy.",0.5),
 ("Die vier ken je al. In ons kader horen ze bij de laag wat.",0.5),
 ("Transparantie is domein 6. Verantwoording is domein 2. Bias is domein 5. En privacy is domein 4.",0.5),
 ("Privacy werk je vooral uit bij A-DG. In deze clip gaat het om transparantie en bias.",0.9)]),
("B2","Een weegschaal. Links verschijnen groene pijlen omhoog (drivers), rechts rode pijlen omlaag (inhibitors). De weegschaal kantelt heen en weer.",[
 ("Per onderdeel kijkt CertifAIEd naar twee soorten factoren.",0.5),
 ("Drivers maken het waarschijnlijker dat een systeem ethisch werkt.",0.5),
 ("Inhibitors werken het tegen, vaak om redenen die je best begrijpt.",0.5),
 ("Een bedrijf wil geen claims. Of het wil een slim idee niet weggeven aan de concurrent.",0.5),
 ("Wie alleen naar de drivers kijkt, ziet goede bedoelingen. Wie ook naar de inhibitors kijkt, ziet waarom die bedoelingen in de praktijk stranden.",0.9)]),
("B3","Telefoon met de chat van Frisco Installaties. Bovenaan: \"U praat met een digitale assistent\". Onderaan een knop \"Medewerker\" en duimpjes voor feedback. Bij elke driver verschijnt een groen vinkje.",[
 ("Neem de orderagent van Frisco Installaties.",0.5),
 ("Een klant die denkt dat hij een medewerker spreekt, vertrouwt een belofte over prijs of levertijd. Klopt die niet, dan voelt hij zich bedrogen.",0.5),
 ("Bij transparantie is een driver dat de klant meteen weet dat die met AI praat.",0.5),
 ("Een andere driver: de werking is helder beschreven. Wat kan de agent wel, en wat niet?",0.5),
 ("De klant kan ingrijpen en feedback geven, en er is een alternatief: een medewerker.",0.5),
 ("Ook telt of het systeem zich voorspelbaar gedraagt, en of de organisatie dat volhoudt, van ontwerp tot gebruik.",0.5)]),
("B4","Drie rode kaartjes schuiven over de telefoon: \"gedrag verhullen\", \"angst voor aansprakelijkheid\", \"bedrijfsgeheim\". Een manager met een tekstballon: \"Dat kunnen we niet vertellen.\"",[
 ("Daartegenover staan drie inhibitors.",0.5),
 ("Gedrag verhullen: het systeem verbergt wat het doet, of probeert mensen ongemerkt te sturen.",0.5),
 ("Angst voor aansprakelijkheid: je vertelt zo weinig mogelijk, zodat niemand je kan aanspreken.",0.5),
 ("En een bedrijfsgeheim beschermen: de werking blijft dicht, omdat een concurrent zou kunnen meekijken.",0.5),
 ("Stel dat Frisco niet mag zeggen welke taaldienst de agent gebruikt, omdat het contract met de leverancier dat verbiedt. Dan weet de klant ook niet waar zijn gegevens heen gaan.",0.5),
 ("Zegt een organisatie: dat kunnen we niet vertellen? Dan zit er vaak een van die drie achter. Vraag dan welke.",0.9)]),
("BQ1","Vraagkaart met A en B. Pauze 8 s met aftelbalk.",[
 ("Tussenvraag. Een bedrijf vertelt klanten niet dat een chatbot hun vragen beantwoordt, uit angst voor claims als het misgaat. Wat is dit volgens CertifAIEd? A: een driver van transparantie. B: een inhibitor, angst voor aansprakelijkheid.",8)]),
("BQ1b","Antwoord B licht groen op.",[
 ("Het antwoord is B. De reden om te zwijgen is angst voor claims, en dat werkt transparantie tegen.",0.9)]),
("B5","Suribank. Twee groepen aanvragers: Paramaribo en het binnenland, met Shanti uit Nickerie. Een vergrootglas glijdt over de groep die vaker wordt afgewezen. Het kenmerk \"district\" verdwijnt uit het model, maar een ander kenmerk licht op met een lijntje naar het district.",[
 ("Nu algoritmische bias. Denk aan het kredietmodel van Suribank uit practicum 2.",0.5),
 ("Een driver is dat je de context van alle betrokkenen begrijpt, ook die van Shanti in Nickerie.",0.5),
 ("Een tweede: je onderbouwt waarom je een beschermd kenmerk gebruikt of weglaat, zoals geslacht of district.",0.5),
 ("Weglaten alleen is niet genoeg. Een ander kenmerk kan het district alsnog verraden. Dat heet een proxy.",0.5),
 ("Verder volg je het gedrag per groep, ook na livegang.",0.5),
 ("En je houdt een biasprofiel bij: de organisatie kan bias corrigeren als die opduikt.",0.5),
 ("Doet niemand dat, dan gaat het mis zoals in practicum 2: de goede betalers in het binnenland betaalden de prijs.",0.5)]),
("B6","Mist trekt over de data. Bronnen krijgen een vraagteken. Een meetlat probeert de groepen te meten en blijft haken.",[
 ("Er is één inhibitor: gebrek aan procestransparantie.",0.5),
 ("Weet niemand waar de data vandaan komt en hoe besluiten tot stand kwamen? Dan kan ook niemand de bias meten.",0.5),
 ("Dat zag je in practicum 2: pas toen je per groep keek, werd het verschil zichtbaar.",0.5),
 ("Bij een orderagent is het niet anders. Zonder logboek van de gesprekken kun je niet nagaan of klanten uit de districten slechter geholpen worden.",0.9)]),
("BQ2","Vraagkaart met A en B. Pauze 8 s met aftelbalk.",[
 ("Tussenvraag. Een bank laat district weg uit het model, maar legt niet vast waarom, en meet de uitkomsten per regio niet. Welke drivers ontbreken vooral? A: weten dat je met AI praat. B: het gebruik van beschermde kenmerken onderbouwen en het gedrag per groep volgen.",8)]),
("BQ2b","Antwoord B licht groen op.",[
 ("Het antwoord is B. Iets weglaten zonder uitleg en zonder meting is geen bewijs dat het model eerlijk is.",0.9)]),
("B7","Een tabel met de kolommen Doel, Bewijs en Score (1 tot 5). Scores vullen zich; een score zonder bewijs wordt rood doorgestreept. De tabel verandert in de snelle scan (K4), met domein 5 en 6 gemarkeerd.",[
 ("Hoe komt een beoordelaar tot een oordeel?",0.5),
 ("Per doel vraagt die bewijs: een document, een test of een gesprek. Daarna volgt een score van 1 tot 5.",0.5),
 ("Een score zonder bewijs telt niet.",0.5),
 ("Dat is dezelfde logica als jullie snelle scan en de nulmeting.",0.5),
 ("Neem domein 6 bij Frisco. Je bewijs is de begroeting van de agent en je test uit practicum 4. Je geeft een score, met dat bewijs erbij.",0.5),
 ("Houdt een bedrijfsgeheim de score laag? Noem die inhibitor dan als reden. Zo ziet de lezer waar de verbetering moet beginnen.",0.5),
 ("Gebruik de drivers en inhibitors daarom als checklist bij domein 5 en domein 6.",0.9)]),
("B8","Samenvatting in drie kaarten: \"Vier onderdelen: domein 2, 4, 5 en 6\", \"Wat helpt én wat tegenwerkt\", \"Elke score met bewijs\".",[
 ("Samengevat.",0.5),
 ("CertifAIEd kijkt naar vier onderdelen, die passen bij domein 2, 4, 5 en 6.",0.5),
 ("Kijk naar wat helpt, en naar wat tegenwerkt.",0.5),
 ("En onderbouw elke score met bewijs, zoals een echte beoordelaar dat doet.",0.9)]),
("B9","\"Nu jij, met je groep\" met drie genummerde stappen.",[
 ("Nu jij. Pak met je groep jullie snelle scan erbij.",0.5),
 ("Welke inhibitor herken je bij jullie partner, of bij een leverancier?",0.5),
 ("En wat betekent dat voor jullie score op domein 6? Gebruik je antwoord in je nulmeting.",0.9)]),
]
z=[];rows=[];n=0
for k,beeld,zs in S:
    txt=[]
    for i,(t,p) in enumerate(zs):
        key=k if len(zs)==1 else f"{k}{chr(97+i)}"
        z.append([key,t,p]); txt.append(t); n+=len(t)
    rows.append((k,beeld," ".join(txt)))
json.dump(z,open('zinnen.json','w'),ensure_ascii=False,indent=0)
md="## Kaderclip B · IEEE CertifAIEd: transparantie en bias toetsen (7 minuten, blok 1)\n\nDoel: studenten leren hoe een echte beoordelaar transparantie en bias toetst, met drivers, inhibitors en bewijs per doel, en gebruiken dat als checklist bij domein 5 en 6 van de nulmeting.\n\n| Sleutel | Beeld | Gesproken tekst |\n| --- | --- | --- |\n"
for k,b,t in rows:
    md+=f"| {k} | {b.replace('|','/')} | {t.replace('|','/')} |\n"
md+=f"\nGesproken tekst: {n} tekens (budget 5.300). Tussenvragen: twee, letterlijk uit kennispakket 1, met een pauze van 8 seconden."
open('script.md','w').write(md)
print(n, len(z))
