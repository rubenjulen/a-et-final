import json
S=[
# (key, beeld (only on first sentence of scene), tekst, pauze)
("C0","Titel: \"De AI-verordening: risicoklasse en rol\". Links Shanti met haar kredietaanvraag bij Suribank, rechts de chat van Frisco Installaties.","In deze clip kijken we naar een wet: de Europese AI-verordening.",0.5),
("C0b",None,"Je risicoregister zegt wat er mis kan gaan. De AI-verordening zegt hoe zwaar de wet een AI-toepassing weegt.",0.5),
("C0c",None,"Na deze clip kun je jullie eigen oplossing indelen in een risicoklasse, de rol van jullie partner benoemen, en uitleggen waarom die klasse geen eindoordeel is.",0.9),
("C1","Kaart: Europa gekleurd, Suriname grijs. Een pijl van een Surinaams bedrijf naar Europese klanten kleurt groen.","Suriname valt niet onder deze wet. Waarom kijken we er dan toch naar?",0.5),
("C1b",None,"Twee redenen. Heeft een organisatie Europese klanten of verwerkt ze Europese data, dan moet ze zich er wel aan houden.",0.5),
("C1c",None,"En het is het bekendste voorbeeld van hoe een wetgever AI indeelt. Het helpt je om te zien hoe zwaar jullie eigen oplossing weegt.",0.5),
("C1d",None,"De wet is sinds 2024 van kracht en gaat stap voor stap gelden. De verboden en de plicht tot AI-geletterdheid gelden al sinds februari 2025.",0.9),
("C2","Piramide met vier lagen, van onder naar boven opgebouwd. Elke laag krijgt een kleur en twee voorbeelden.","De wet deelt AI in vier risicoklassen in.",0.5),
("C2b",None,"Bovenaan staat onaanvaardbaar risico. Dat is verboden, in artikel 5. Denk aan een sociale score voor burgers, of AI die iemands kwetsbaarheid uitbuit.",0.5),
("C2c",None,"Daaronder staat hoog risico. Dat mag, maar onder strenge eisen. Bijlage III noemt waar het om gaat: onder meer kredietwaardigheid, werving en selectie, onderwijs en publieke uitkeringen.",0.5),
("C2d",None,"Dan beperkt risico. Daar geldt vooral een transparantieplicht, in artikel 50: mensen moeten weten dat ze met AI praten.",0.5),
("C2e",None,"Onderaan staat minimaal risico, zoals een spamfilter. Daarvoor gelden geen extra eisen.",0.5),
("C2f",None,"Hoe hoger in de piramide, hoe zwaarder de eisen. De vraag is dus steeds: waarvoor wordt het systeem gebruikt, en wat staat er voor mensen op het spel?",0.9),
("C3","Twee kaartjes: \"Aanbieder\" met een tandwiel, \"Gebruiksverantwoordelijke\" met een persoon achter een bureau. Een pijl van de leverancier naar Suribank.","Naast de klasse is je rol belangrijk. De wet kent twee hoofdrollen.",0.5),
("C3b",None,"De aanbieder ontwikkelt een AI-systeem, of laat het ontwikkelen, en brengt het onder eigen naam op de markt of in gebruik.",0.5),
("C3c",None,"De gebruiksverantwoordelijke zet het systeem onder eigen verantwoordelijkheid in, bijvoorbeeld in het eigen kantoor.",0.5),
("C3d",None,"Een organisatie kan ook allebei zijn. Bij Suribank is de leverancier van het model de aanbieder, en de bank de gebruiksverantwoordelijke.",0.5),
("C3e",None,"Waarom maakt die rol uit? Omdat de plichten verschillen. De aanbieder moet zorgen dat het systeem goed gebouwd en getest is. De gebruiksverantwoordelijke moet zorgen dat het in de praktijk goed gebruikt wordt.",0.9),
("CQ1","Vraag in beeld, daarna pauze 8 s met aftelbalk.","Vraag één. Een bank gebruikt een model dat beslist of iemand een persoonlijke lening krijgt. In welke risicoklasse valt dit model?",8),
("CQ1b","Antwoord in beeld: Shanti's aanvraag schuift in de laag \"hoog risico\".","Het antwoord: hoog risico, bijlage III, punt 5b. De bank moet als gebruiksverantwoordelijke ook een FRIA doen.",0.9),
("C4","Shanti's aanvraag ligt in de laag \"hoog risico\". Drie stempels verschijnen: risicobeheer (art. 9), data (art. 10), menselijk toezicht (art. 14). Daarna een vierde: FRIA (art. 27), die overgaat in \"K2 + nulmeting\".","Kijk naar het kredietmodel van Suribank. Het beoordeelt de kredietwaardigheid van mensen zoals Shanti. Dat is hoog risico.",0.5),
("C4b",None,"Dan gelden onder meer risicobeheer, in artikel 9, eisen aan de data, in artikel 10, en menselijk toezicht, in artikel 14.",0.5),
("C4c",None,"En de bank moet een FRIA doen: een beoordeling van de gevolgen voor grondrechten, in artikel 27. Wie wordt geraakt, hoe ernstig, en wat doe je eraan?",0.5),
("C4d",None,"Dat herken je. Het lijkt sterk op jullie AI-impactbeoordeling: de stakeholderkaart K2 plus de nulmeting.",0.5),
("C4e",None,"Stel dat het model Shanti onterecht afwijst. Dan moet een mens kunnen ingrijpen, en moet de bank kunnen uitleggen waarom. Dat is precies wat jullie in K7 ontwerpen.",0.9),
("C5","De chat van Frisco Installaties. De eerste bubbel van de agent: \"Hallo, ik ben de digitale assistent van Frisco. Ik ben een AI.\" Een vinkje bij \"artikel 50\".","Nu de orderagent van Frisco Installaties. Hij neemt bestellingen op voor technische installaties.",0.5),
("C5b",None,"Zo'n agent staat niet in bijlage III. Meestal is dat beperkt risico.",0.5),
("C5c",None,"Artikel 50 geldt wel: klanten moeten weten dat ze met AI praten. Daarom zegt de agent dat meteen in zijn eerste bericht. En vraagt een klant: praat ik met een mens? Dan zegt de agent eerlijk van niet, en biedt hij een medewerker aan.",0.5),
("C5d",None,"Frisco laat de agent bouwen en zet hem onder eigen naam in. Dan is Frisco aanbieder en gebruiksverantwoordelijke tegelijk.",0.5),
("C5e",None,"Let op: gaat de agent zelf beslissen over krediet, of over wie wel en niet geholpen wordt? Kijk dan opnieuw naar de klasse.",0.9),
("CQ2","Vraag in beeld, daarna pauze 8 s met aftelbalk.","Vraag twee. Een maatkledingzaak laat een orderchatbot bouwen en zet die onder eigen naam op haar website. Welke rol heeft de zaak, en welke plicht geldt in elk geval?",8),
("CQ2b","Antwoord in beeld: twee kaartjes met een vinkje, en de AI-melding in de chat.","Het antwoord: de zaak is aanbieder én gebruiksverantwoordelijke. En in elk geval geldt de transparantieplicht van artikel 50: klanten moeten weten dat ze met AI praten.",0.9),
("C6","Vier kaartjes met een artikelnummer schuiven in beeld: 10, 13, 26 en 86. Bij 10 een klein label \"A-DG\".","Vier artikelen kom je nog tegen bij hoog risico, ook in de antwoordsleutel van week 6.",0.5),
("C6b",None,"Artikel 10 gaat over data en datagovernance. Dat werk doen jullie vooral bij A-DG.",0.5),
("C6c",None,"Artikel 13 zegt dat de aanbieder duidelijke informatie meegeeft aan wie het systeem gebruikt: wat het kan, wat niet, en hoe je het controleert.",0.5),
("C6d",None,"Artikel 26 noemt de plichten van de gebruiksverantwoordelijke, zoals het systeem gebruiken zoals bedoeld, en het in de gaten houden.",0.5),
("C6e",None,"En artikel 86 geeft wie door zo'n besluit geraakt wordt, recht op uitleg.",0.9),
("C7","De piramide wordt kleiner en komt op een sokkel met het woord \"ondergrens\". Daarboven de vier ethische lenzen.","De klasse is niet het hele verhaal.",0.5),
("C7b",None,"Artikel 4 vraagt AI-geletterdheid van iedereen die met het systeem werkt, in elke klasse.",0.5),
("C7c",None,"Menselijk toezicht en transparantie komen terug in clip 18 en clip 20.",0.5),
("C7d",None,"En onthoud: de klasse is een ondergrens. Wat de wet toestaat, is niet altijd verantwoord. En waar de wet zwijgt, zoals in Suriname, blijft de ethische vraag gewoon staan.",0.5),
("C7e",None,"Een voorbeeld. De orderagent van Frisco is beperkt risico. Toch kan hij klanten met een andere naam, of klanten die liever een spraakbericht sturen, slechter helpen. De wet vraagt daar weinig. Jullie test in practicum 4 vraagt het wel.",0.9),
("C7f","Samenvatting: drie regels verschijnen onder elkaar.","Samengevat. Eén: de wet deelt AI in vier klassen in, van verboden tot minimaal risico. Twee: je rol, aanbieder of gebruiksverantwoordelijke, bepaalt je plichten. Drie: de klasse is een ondergrens, geen eindoordeel.",0.9),
("C8","Het risicoregister K6 met bovenaan een lege regel \"EU-risicoklasse en rol\": klasse, onderbouwing, rol van de partner. De velden vullen zich voor Suribank.","Nu jij. Zet boven jullie risicoregister de regel: EU-risicoklasse en rol.",0.5),
("C8b",None,"Schrijf op welke klasse, waarom, met het artikel of de bijlage, en welke rol jullie partner heeft.",0.5),
("C8c",None,"Twijfel je? Schrijf dan op tussen welke klassen je twijfelt, en waarom. Ook dat is een goed antwoord.",0.9),
]
n=sum(len(t) for _,_,t,_ in S); print('tekens',n)
json.dump([[k,t,p] for k,_,t,p in S],open('zinnen.json','w'),ensure_ascii=False,indent=0)
# markdown table: group by scene (key without trailing letter b..e)
import re
rows=[]; cur=None
for k,b,t,p in S:
    base=k if (k=='C7f' or k.startswith('CQ')) else re.sub(r'[b-z]$','',k)
    if base!=cur:
        rows.append([base,b,[t]]); cur=base
    else: rows[-1][2].append(t)
def esc(s): return s.replace('|','\\|')
md="| Sleutel | Beeld | Gesproken tekst |\n| --- | --- | --- |\n"
for k,b,ts in rows:
    md+=f"| {k} | {esc(b)} | {esc(' '.join(ts))} |\n"
open('table.md','w').write(md); print(md[:300]); print(len(rows),'scenes')
