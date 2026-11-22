## Wat je nodig hebt

Voor de practica werk je in Orange of in Python. Je kiest zelf: Orange werkt zonder programmeren, Python past bij wie in A-DA met Python werkte. Voor elk practicum is er een stappenplan voor Orange en een Python-notebook.

| Wat | Waarvoor | Hoe |
| --- | --- | --- |
| Laptop met Windows of macOS | Orange en het werkboek | Reken op ongeveer 1 GB vrije schijfruimte voor Orange |
| Orange Data Mining | Practicum 1 tot en met 5, zonder programmeren | Installeren, zie hieronder |
| Python met Jupyter, of Google Colab | Practicum 1 tot en met 5 als notebook | Lokaal installeren, of online in Colab zonder installatie |
| Excel en Word (of LibreOffice) | Het werkboek met de instrumenten en de sjablonen | Zie "Werkboek en sjablonen" |
| De practicumbestanden | Data, notebooks en workflows | Per practicum een zip op MyCampus: ICT A-ET Practicum 1, 2 en 3, 4 en 5 |

Heb je een Chromebook of alleen een tablet? Orange werkt daar niet. Gebruik dan Google Colab voor de practica, en meld het zo snel mogelijk.

## Orange installeren

Orange Data Mining is gratis, open source en werkt zonder programmeren. Je bouwt een analyse door blokjes, widgets genoemd, op een werkblad te zetten en met lijnen te verbinden. De software is in het Engels.

**Windows.**

1. Ga naar orangedatamining.com en klik op Download.
2. Kies onder Windows de standaardinstallatie. Op een laptop waarop je niets mag installeren, kies je de portable versie: dat is een zip-bestand dat je uitpakt en direct start.
3. Open het gedownloade bestand en volg de stappen. Laat alle standaardinstellingen staan.
4. Start Orange via het startmenu. De eerste keer kan dat één tot twee minuten duren.

**macOS.**

1. Ga naar orangedatamining.com en klik op Download.
2. Kies onder macOS de versie die bij je Mac past: Apple silicon voor een Mac met een M-chip, Intel voor een oudere Mac. Twijfel je, kijk dan bij Apple-menu, Over deze Mac.
3. Open het dmg-bestand en sleep Orange naar de map Apps.
4. Start Orange vanuit de map Apps. De eerste keer kan dat één tot twee minuten duren.

**Linux.** Voor ICT-studenten met Linux: installeer via de Python-pakketbeheerder pip met het pakket orange3. Zie de downloadpagina voor de actuele instructie.

**Controle.** Orange werkt als je een leeg werkblad ziet met links een lijst met groepen widgets, zoals Data, Visualize en Model. Sluit het welkomstvenster als dat verschijnt.

**Een workflow openen.** Voor practicum 4 is er een kant-en-klare workflow (practicum4_suribank.ows in ICT A-ET Practicum 4.zip). Pak de zip uit en open het bestand via File, Open in Orange. Laat het databestand in dezelfde map staan.

## Python lokaal

De notebooks gebruiken de pakketten pandas, numpy en scikit-learn; het notebook van practicum 5 ook matplotlib.

**Met Anaconda (makkelijkst).**

1. Download Anaconda Distribution voor jouw besturingssysteem en installeer met de standaardinstellingen. De pakketten hierboven en Jupyter zitten er al in.
2. Start Anaconda Navigator en open Jupyter Notebook.
3. Ga in Jupyter naar de uitgepakte map van het practicum en open het notebook (.ipynb).

**Met Python van python.org.**

1. Installeer Python 3 van python.org. Vink op Windows "Add Python to PATH" aan.
2. Open een terminal (Windows: Opdrachtprompt) en installeer de pakketten:

```
pip install pandas numpy scikit-learn matplotlib notebook
```

3. Ga in de terminal naar de uitgepakte map van het practicum en start Jupyter:

```
jupyter notebook
```

4. Open in het browservenster het notebook (.ipynb).

Laat het notebook en de csv-bestanden in dezelfde map staan: het notebook zoekt de data op naam.

## Google Colab (zonder installatie)

Colab werkt in de browser, ook op een Chromebook. Je hebt een Google-account nodig.

1. Ga naar colab.research.google.com.
2. Kies Bestand, Notebook uploaden, en selecteer het notebook uit de uitgepakte zip.
3. Klik links op het mappictogram (Bestanden) en upload de csv-bestanden van dat practicum. Het notebook van practicum 5 heeft hiervoor ook een eigen uploadcel.
4. Voer de cellen van boven naar beneden uit met Shift + Enter.

Geüploade bestanden verdwijnen als je de sessie sluit. Upload ze opnieuw als je later verder werkt, of sla het notebook op in je Google Drive.

De getallen in Python wijken soms iets af van die in Orange. De vragen gaan over wat je ziet, niet over het precieze getal.

## Werkboek en sjablonen

- **ICT A-ET Werkboek instrumenten.xlsx** bevat alle instrumenten, met keuzelijsten en formules. Het werkt het best in Excel. In LibreOffice Calc werken de formules ook. Werk je met je groep in één bestand, zet het dan in een gedeelde map, zodat de versiegeschiedenis bewaard blijft.
- **De Word-sjablonen** (K1 Canvas, K5 Dilemma Canvas, Sjabloon tussenrapport, Sjabloon eindrapport, Sjabloon reflectie, AI-verklaring) openen in Word of LibreOffice Writer. De grijze hulptekst haal je weg voordat je inlevert.
- **ICT A-ET Peerbeoordeling.xlsx** vul je in op het tabblad Invullen.
- **Het testlogboek van practicum 4** (practicum4_testlogboek.xlsx in ICT A-ET Practicum 4.zip) werkt ook in Excel of LibreOffice.

## Problemen oplossen

| Probleem | Oplossing |
| --- | --- |
| Windows meldt "Windows heeft uw pc beschermd" | Klik op Meer informatie en daarna op Toch uitvoeren. |
| De Mac meldt dat de ontwikkelaar niet kan worden geverifieerd | Klik met de rechtermuisknop op Orange in de map Apps en kies Open. Of ga naar Systeeminstellingen, Privacy en beveiliging, en kies Open toch. |
| De installatie stopt door te weinig ruimte | Maak minstens 1 GB vrij en probeer opnieuw. |
| Orange start niet of blijft hangen | Herstart de laptop en probeer opnieuw. Werkt het dan nog niet, gebruik de portable versie (Windows). |
| Je mag niets installeren op een werklaptop | Gebruik de portable versie, of werk op een eigen laptop, of gebruik Google Colab. |
| Je hebt een Chromebook of alleen een tablet | Orange werkt daar niet. Gebruik Google Colab, en meld het zo snel mogelijk; dan zoeken we een oplossing, zoals samenwerken met een groepsgenoot. |
| Het notebook vindt het databestand niet | Zet het csv-bestand in dezelfde map als het notebook (lokaal), of upload het opnieuw in Colab. |
| "ModuleNotFoundError" in Python | Het pakket ontbreekt: installeer het met pip install en de naam uit de foutmelding (sklearn heet bij installeren scikit-learn). |
| De download gaat erg langzaam | Download op een plek met een snellere verbinding, of vraag om het installatiebestand op een usb-stick. |

Lukt het niet? Stel je vraag vóór college 1 (donderdag 7 januari) via [kanaal, bijvoorbeeld MyCampus of e-mail], met een schermafdruk van de foutmelding. Zorg dat practicum 1 vóór college 1 werkt: dan kun je in het college meedoen.
