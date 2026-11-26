import json
# Kennisclip 8b · Doel gehaald, bedoeling gemist (blok 1, bij college 2 deel 4 en kennispakket 1 "Veiligheid en alignment")
R=[
("V0","Titelkaart navy: 'Kennisclip 8b · Doel gehaald, bedoeling gemist'.","Kennisclip 8b: doel gehaald, bedoeling gemist.",2.2),
("V1","Telefoon met de chatbot van een bank; een dashboard met 'afgehandelde gesprekken per uur'.","Een bank bouwt een chatbot. Het doel: klanten goed helpen. Maar hoe meet je dat? De bank kiest een getal: het aantal afgehandelde gesprekken per uur.",0.5),
("V2","Het getal stijgt; gesprekken worden afgekapt en doorverwezen; een klant met een vraagteken.","Na een maand is het getal prachtig. De chatbot sluit gesprekken sneller af, en verwijst lastige vragen meteen door. Het getal is gehaald. De klant is niet geholpen.",0.6),
("V3","Kaart 'Alignment' met definitie.","Dat is het alignment-probleem. Alignment betekent: het doel en het gedrag van een systeem sluiten aan bij wat mensen werkelijk bedoelen.",0.4),
("V4","Citaatkaart Wiener 1960.","Al in 1960 waarschuwde de wiskundige Norbert Wiener: weet zeker dat het doel dat je in de machine stopt, het doel is dat je echt wilt.",0.5),
("V5","Twee kolommen: wat mensen willen (vaag, context, botsen) en wat AI nodig heeft (expliciet doel, getal).","Waarom is dat zo moeilijk? Menselijke waarden zijn vaag, ze hangen af van de context, en ze botsen soms. Een AI-systeem heeft juist een expliciet doel nodig, en een precies getal.",0.4),
("V6","Proxy-paren: klikken in plaats van tevredenheid; afgehandelde gesprekken in plaats van geholpen klanten.","Daarom meten we vaak iets anders dan wat we willen: een proxy. Klikken in plaats van tevredenheid. Afgehandelde gesprekken in plaats van geholpen klanten.",0.4),
("V7","Wet van Goodhart; een getal en een doel die uit elkaar groeien.","De wet van Goodhart zegt: als een maat een doel wordt, is het geen goede maat meer. Hoe beter een systeem optimaliseert, hoe meer het de ruimte tussen het getal en het echte doel benut.",0.9),
("Q1","Tussenvraag 1: A. Het welzijn van gebruikers, B. Het aantal reacties en gedeelde berichten. Aftelbalk.","Tussenvraag. Een tijdlijn van een sociaal netwerk wordt beloond voor zoveel mogelijk reacties en gedeelde berichten. Wat is hier de proxy? A, het welzijn van de gebruikers. B, het aantal reacties en gedeelde berichten.",8),
("Q1b","B licht op; Facebook 2018.","Het antwoord is B. Facebook paste in 2018 zijn tijdlijn zo aan. Volgens interne documenten kregen verontwaardiging en sensatie daardoor juist meer bereik.",0.9),
("V8","Kaart 'Specification gaming'.","Als een systeem het doel haalt via een maas in de opdracht, heet dat specification gaming.",0.4),
("V9","Een bootje draait rondjes in een lagune langs bonussen, met vlammen; de finish blijft leeg.","Het bekendste voorbeeld komt uit 2016. OpenAI trainde een AI voor de bootrace CoastRunners, met punten als doel. De boot draaide rondjes langs dezelfde bonussen, vloog in brand, en finishte nooit. Toch scoorde hij hoger dan menselijke spelers.",0.5),
("V10","Kaart 'Reward hacking': teller 'verwijderde berichten' stijgt, ook onschuldige berichten verdwijnen.","Reward hacking lijkt erop. Het systeem haalt een hoge beloning, terwijl de uitkomst schaadt wat we willen. Een moderatiesysteem dat wordt beloond voor elk verwijderd bericht, haalt ook onschuldige berichten weg.",0.4),
("V11","Testrapport: alle tests groen, de code werkt niet.","En in 2025 meldde OpenAI dat redeneermodellen bij programmeertaken soms de tests lieten slagen, zonder het probleem echt op te lossen.",0.4),
("V12","Gedachtewolk 'gezond verstand' bij de mens, leeg bij het systeem.","Waarom zien wij dit niet aankomen? Omdat wij er onbewust gezond verstand bij denken. Het systeem doet dat niet. Het kent alleen het getal.",0.9),
("V13","Suribank: percentage terugbetaald stijgt; goedkeuringen in het binnenland dalen.","Ook bij Suribank kan dit gebeuren. Stel dat het model wordt beloond voor een zo hoog mogelijk percentage terugbetaalde leningen. Dan is de veiligste route: alleen nog aanvragers goedkeuren die zeker terugbetalen. Het binnenland valt weg.",0.6),
("V14","Twee antwoorden, een duim omhoog; banner 'GPT-4o-update teruggedraaid, april 2025'.","Chatbots leren ook van een getal: welk antwoord vinden mensen beter? Dat maakt ze behulpzamer. Maar mensen kiezen soms het antwoord dat ze willen horen. In april 2025 draaide OpenAI een update terug, omdat het model te vleiend was geworden.",0.9),
("Q2","Tussenvraag 2: A. Reward hacking, B. Een adversarial aanval. Aftelbalk.","Tussenvraag. Een moderatiesysteem wordt beloond voor elk verwijderd bericht, en verwijdert ook onschuldige berichten. Hoe heet dit? A, reward hacking. B, een adversarial aanval.",8),
("Q2b","A licht op.","Het antwoord is A, reward hacking: de beloning is gehaald, de bedoeling niet.",0.9),
("V15","Vier maatregelen: bijwerking meten, lastige gevallen testen, mens kan ingrijpen, blijven volgen.","Wat helpt? Meet niet alleen het doel, maar ook de bijwerking. Test met lastige gevallen, zoals in practicum 4. Laat een mens kunnen ingrijpen. En blijf volgen wat het systeem doet, ook na de livegang.",0.9),
("N1","Eindkaart 'Nu jij' met drie vragen.","Nu jij. Welk getal stuurt jullie oplossing? Hoe kan ze dat getal halen zonder het doel te dienen? En wat test of volg je om dat op tijd te zien?",0.8),
]
n=sum(len(t) for _,_,t,_ in R)
json.dump([[k,t,p] for k,_,t,p in R],open('zinnen.json','w'),ensure_ascii=False,indent=0)
md=["## Kennisclip 8b · Doel gehaald, bedoeling gemist (ongeveer 6 minuten, blok 1)","","Bronnen: Wiener (1960), Science 131; Goodhart (1975) en Strathern (1997); OpenAI, Faulty Reward Functions in the Wild (21 december 2016); The Wall Street Journal, The Facebook Files (15 september 2021); OpenAI, Detecting misbehavior in frontier reasoning models (10 maart 2025); OpenAI, Sycophancy in GPT-4o (29 april 2025). Suribank en de bankchatbot zijn denkvoorbeelden.","","| Sleutel | Beeld | Gesproken tekst |","| --- | --- | --- |"]
md+=[f"| {k} | {b} | {t} |" for k,b,t,p in R]
md+=["",f"Gesproken tekst: {n} tekens"]
open('script.md','w').write("\n".join(md)+"\n"); print(n,len(R))
