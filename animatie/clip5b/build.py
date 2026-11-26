import json
# Kennisclip 5b · Vijf ethische kaders (blok 1, bij college 1 deel 2 en kennispakket 1 "Vier ethische lenzen")
# (sleutel, beeld, tekst, pauze)
R=[
("E0","Titelkaart op navy: 'Kennisclip 5b · Vijf ethische kaders'. Vijf ronde iconen schuiven in: weegschaal, slagboom, verdeelde taart, ster, hand.","Vijf ethische kaders.",2.2),
("E1","Straat in Paramaribo met een cameramast. Een lichtbundel scant voorbijgangers; om hun gezichten verschijnen kaders.","Stel: de camera's van Safe City in Paramaribo gaan ook gezichten herkennen. De politie vindt verdachten sneller. Maar iedereen die over straat loopt, wordt ook bekeken.",0.5),
("E2","Vijf tekstballonnen boven vijf mensen: 'Ja', 'Nee', 'Onder voorwaarden', 'Eerst een wet', 'Wie controleert?'.","Is dat goed of fout? Vraag het aan vijf mensen, en je krijgt vijf antwoorden. Dat komt niet doordat ze dom zijn. Ze wegen andere dingen zwaarder.",0.6),
("E3","Drie kaarten: Structuur, Consistentie, Onderbouwing.","Een ethisch kader helpt je die afweging te maken. Het geeft structuur, je oordeelt consequent, en je kunt uitleggen waarom, ook aan wie het met je oneens is.",0.5),
("E4","Vijf kaderkaarten op een rij, elk met één vraag.","Je ziet vijf kaders. Wat vraagt elk kader, waar komt het vandaan, en waar schiet het tekort?",0.9),
# 1 gevolgen
("G1","Kader 1 · Gevolgen. Een weegschaal met baten en schade.","Het eerste kader gaat over gevolgen: wat levert het op, en voor wie? Dit heet utilitarisme.",0.4),
("G2","Herkomst: tijdlijn met Bentham (1789) en Mill (1863).","Het komt van de Engelse filosofen Jeremy Bentham, in 1789, en John Stuart Mill, in 1863. Kies wat de meeste baten en de minste schade oplevert, voor iedereen die geraakt wordt.",0.4),
("G3","Kaart 'risicoregister: kans × impact'.","Bij AI ken je dit al: een risicoregister met kans keer impact is een gevolgenberekening.",0.4),
("G4","Raster van honderd poppetjes: 95 blauw, 5 rood.","Maar een systeem dat vijfennegentig procent van de mensen helpt en vijf procent benadeelt, scoort goed. Tenzij jij bij die vijf procent hoort.",0.4),
("G5","Sterk en zwak.","Dat is de zwakte: kleine groepen worden weggemiddeld. En niet alles is meetbaar, zoals angst.",0.4),
("G6","Kaart 'Bij Safe City'.","Bij Safe City vraagt dit kader: hoeveel minder straatroof, tegenover hoeveel foute treffers?",0.9),
# 2 plichten
("P1","Kader 2 · Plichten. Een slagboom met het bord 'grens'.","Het tweede kader gaat over plichten: wat mag nooit, ook niet als het veel oplevert? Dit heet deontologie.",0.4),
("P2","Herkomst: Kant (1785) licht op op de tijdlijn.","Het komt van de Duitse filosoof Immanuel Kant, in 1785. Behandel een mens nooit alleen als middel, maar altijd ook als doel.",0.4),
("P3","Telefoon met een verkoopchatbot: 'Nog maar 1 over! Beslis nu!'","Een verkoopchatbot die klanten manipuleert, levert omzet op. Vanuit plichten is dat fout, hoe hoog de winst ook is.",0.4),
("P4","Sterk en zwak; twee regels botsen.","Sterk: heldere grenzen die rechten beschermen. Zwak: regels kunnen botsen, zoals privacy en veiligheid.",0.4),
("P5","Kaart 'Bij Safe City' met Grondwet artikel 17.","Bij Safe City: de Grondwet beschermt in artikel 17 de persoonlijke levenssfeer. Mag een camera die zomaar doorbreken?",0.9),
# 3 rechtvaardigheid
("R1","Kader 3 · Rechtvaardigheid. Een taart wordt verdeeld.","Het derde kader gaat over rechtvaardigheid: zijn de lasten eerlijk verdeeld?",0.4),
("R2","Herkomst: Rawls (1971). Een sluier valt over een figuur met een vraagteken.","Het komt van de Amerikaanse filosoof John Rawls, in 1971. Kies de regels alsof je niet weet welke plek je zelf krijgt. Hij noemde dat de sluier van onwetendheid.",0.4),
("R3","Tekst: 'Ongelijkheid alleen als de zwakste er beter van wordt'.","Ongelijkheid mag volgens Rawls alleen als de zwakste er beter van wordt.",0.4),
("R4","Twee labels onder de sluier: 'kust' en 'binnenland'. Het kredietmodel van Suribank.","Neem het kredietmodel van Suribank. Zou je het accepteren als je niet weet of je aan de kust woont of in het binnenland?",0.4),
("R5","Sterk en zwak.","Sterk: je ziet wie de lasten draagt. Zwak: er zijn meerdere definities van eerlijk, en die gaan niet allemaal tegelijk.",0.4),
("R6","Kaart 'Bij Safe City'.","Bij Safe City: in welke wijken hangen de camera's, en wie krijgt de foute treffers?",0.9),
# tussenvraag 1
("Q1","Tussenvraag 1: A. Gevolgen, B. Plichten, C. Rechtvaardigheid. Aftelbalk 8 s.","Tussenvraag. Een bankmedewerker zegt: het model helpt duizend klanten sneller, dus een paar foute afwijzingen nemen we voor lief. Welk kader is dat? A, gevolgen. B, plichten. C, rechtvaardigheid.",8),
("Q1b","Knop A licht groen op.","Het antwoord is A, gevolgen. Rechtvaardigheid zou vragen: wie zijn die paar klanten, en waarom juist zij?",0.9),
# 4 deugd
("D1","Kader 4 · Deugd. Een ster boven een ontwikkelaar.","Het vierde kader kijkt naar de mensen die het systeem maken en gebruiken. Dit is deugdethiek.",0.4),
("D2","Herkomst: Aristoteles (ca. 340 v.Chr.) helemaal links op de tijdlijn.","Het is het oudste kader, van de Griekse filosoof Aristoteles, rond 340 voor Christus. Hij vroeg: wat zou een goede vakman hier doen?",0.4),
("D3","Laptop met melding 'Model werkt slechter voor één groep'; schakelaar 'livegang' gaat naar 'uitgesteld'.","Een ontwikkelaar ziet dat het model slechter werkt voor één groep, en meldt het. Ook al schuift de livegang dan op.",0.4),
("D4","Sterk en zwak; beroepscode ACM (2018).","Beroepscodes, zoals die van de ACM uit 2018, maken dat concreet. Zwak: zonder criteria blijft het vaag.",0.4),
("D5","Kaart 'Bij Safe City'.","Bij Safe City: wat doet een goede politieleiding hier?",0.9),
# 5 zorg
("Z1","Kader 5 · Zorg. Een hand onder een poppetje.","Het vijfde kader is zorgethiek. Wie is afhankelijk, en wie kan zich niet verweren?",0.4),
("Z2","Herkomst: Gilligan (1982), Noddings (1984), Tronto (1993); de vier stappen van Tronto in een cirkel.","Het komt van Carol Gilligan, in 1982, en Nel Noddings, in 1984. Joan Tronto beschreef in 1993 vier stappen: zorg opmerken, verantwoordelijkheid nemen, zorg geven, en nagaan hoe die aankomt.",0.4),
("Z3","Telefoon: 'Aanvraag afgewezen.' Geen uitleg, geen telefoonnummer.","Denk aan een aanvrager uit het binnenland die zonder uitleg wordt afgewezen, en niemand kan bellen.",0.4),
("Z4","Sterk en zwak.","Sterk: kwetsbare mensen worden zichtbaar. Zwak: het is moeilijk op grote schaal.",0.4),
("Z5","Kaart 'Bij Safe City'.","Bij Safe City: wie kan zich niet verweren als de camera zich vergist?",0.9),
# tegenspraak
("T1","Tabel: vijf kaders, kolom 'Mag het?'. Gevolgen: ja. Plichten: nee, niet zonder privacywet.","Naast elkaar spreken de kaders elkaar tegen. Gevolgen zegt misschien: ja, het levert veiligheid op. Plichten zegt: niet zonder een privacywet.",0.4),
("T2","Rechtvaardigheid: onder voorwaarden. Deugd en zorg: vertrouwen?","Rechtvaardigheid zegt: alleen als de fouten eerlijk verdeeld zijn. Deugd en zorg vragen: wat doet dit met het vertrouwen in de politie?",0.4),
("T3","Navy balk: 'Geen kader heeft alle antwoorden'.","Dat is geen fout. Zo zie je waar de echte afweging zit. Gebruik de kaders samen, en zeg eerlijk wat je opgeeft.",0.9),
# canvas
("K1","Deugd- en zorgkaart schuiven samen tot 'Professionele integriteit'; daarna het dilemma-canvas met 'Lens · Theorie'.","In het dilemma-canvas worden het vier lenzen: deugd en zorg vallen samen onder professionele integriteit. Noem bij elke lens ook de theorie.",0.9),
# tussenvraag 2
("Q2","Tussenvraag 2: A. Gevolgen, B. Plichten, C. Zorg. Aftelbalk 8 s.","Tussenvraag. Iemand zegt: hoeveel het ook oplevert, een aanvrager heeft altijd recht op uitleg. Welk kader is dat? A, gevolgen. B, plichten. C, zorg.",8),
("Q2b","Knop B licht groen op.","Het antwoord is B, plichten: een recht dat geldt, ongeacht het nut.",0.9),
# samenvatting en opdracht
("S1","Vijf rijen met icoon en vraag.","Samengevat. Gevolgen vraagt wat het oplevert. Plichten vraagt wat nooit mag. Rechtvaardigheid vraagt hoe de lasten verdeeld zijn. Deugd vraagt wat een goede professional doet. En zorg vraagt wie afhankelijk is.",0.9),
("N1","Eindkaart 'Nu jij' met drie stappen.","Nu jij. Kies één dilemma uit jullie eigen oplossing. Welk kader gebruik je als eerste, en welk kader spreekt het het meest tegen? Schrijf het op voor je dilemma-canvas.",0.8),
]
n=sum(len(t) for _,_,t,_ in R)
json.dump([[k,t,p] for k,_,t,p in R],open('zinnen.json','w'),ensure_ascii=False,indent=0)
md=["## Kennisclip 5b · Vijf ethische kaders (ongeveer 6 minuten, blok 1)","",
"Na deze clip kan de student de vijf ethische kaders (gevolgen, plichten, rechtvaardigheid, deugd, zorg) uitleggen met hun kernvraag, herkomst, sterke en zwakke kant, ze toepassen op een AI-keuze, en uitleggen hoe ze in het dilemma-canvas samenkomen in vier lenzen.","",
"Bronnen: Bentham (1789), An Introduction to the Principles of Morals and Legislation; Mill (1863), Utilitarianism; Kant (1785), Grundlegung zur Metaphysik der Sitten; Rawls (1971), A Theory of Justice; Aristoteles, Ethica Nicomachea (ca. 340 v.Chr.); ACM Code of Ethics and Professional Conduct (2018); Gilligan (1982), In a Different Voice; Noddings (1984), Caring; Tronto (1993), Moral Boundaries; Grondwet van de Republiek Suriname, art. 17. Safe City staat als 'stel dat' in de clip: of de camera's gezichten herkennen, is niet bevestigd.","",
"| Sleutel | Beeld | Gesproken tekst |","| --- | --- | --- |"]
for k,b,t,p in R:
    md.append(f"| {k} | {b.replace('|','/')} | {t} |")
md+=["",f"Gesproken tekst: {n:,} tekens".replace(',','.')]
open('script.md','w').write("\n".join(md)+"\n")
print(n,len(R))
