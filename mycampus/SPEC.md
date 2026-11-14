# Spec: studentversies als pdf voor MyCampus (maatwerk-LMS, geen toetsimport)

Map: /tmp/claude-0/-home-user-menssana/175e1d50-6875-5f56-acf6-23260f0c6b9a/scratchpad/mycampus/
- md/   gefilterde markdown per week (bron voor de pdf)
- pdf/  de pdf's
- tools/render.js + style.css  (één huisstijl; niet aanpassen)

Render: `cd mycampus/tools && node render.js ../md/<bestand>.md ../pdf/<bestand>.pdf "Week N" "<Titel van de week>"`
De titel komt in een kopblok; begin de markdown daarom NIET met een `# titel`, maar met `## ...`.
Markdown = GitHub-flavoured (pandoc -f gfm): tabellen, lijsten, blockquotes, links.

## Hoe je aan de tekst komt
mcp__Claude_Docs__export (via ToolSearch) met format "markdown" op de tab van het weekdoc (read project voor de tab-id).
Grote resultaten staan als bestand in /root/.claude/projects/-home-user-menssana/175e1d50-6875-5f56-acf6-23260f0c6b9a/tool-results/ ;
decodeer bytes_b64 zoals scratchpad/decode_exports.py. Bewaar de volledige export als md/raw_wXX.md.
Embeds (diagrammen/widgets) die in markdown wegvallen: als ze voor studenten belangrijk zijn (bv. K2/K3-voorbeeldfiguur),
probeer ze als afbeelding te krijgen (bv. export pdf van het doc en pdftoppm -png van die pagina + crop met python/PIL), sla op in pdf/img/
en verwijs ernaar met een absoluut pad; lukt dat niet, schrijf een korte tekstuele beschrijving en meld het.

## Wat erin MOET (studentgericht)
Volgorde in de studentversie:
1. "Deze week": leerdoelen, planning met data en contactmoment, tijdsbesteding, checklist/wat je inlevert.
2. "Voorbereiding": de moduletekst (letterlijk), kernbron met leesvragen.
3. "Kennisclips": per clip titel, duur, vragen bij de clip; zet bij elke clip "Video: [link volgt op MyCampus]".
4. Opdrachten: instrumenten (uitleg, sjabloon → verwijs naar tabblad in A-ET_werkboek_instrumenten_2026-2027.xlsx of het Word-sjabloon),
   ingevulde voorbeelden die voor studenten bedoeld zijn, checklists; practica (stappenplan Orange en Python, bestanden).
5. "Weekcheck": de vijf vragen MET antwoordopties maar ZONDER juiste antwoord, feedback of uitleg; logboekregel; standpunt + stelling.
6. Contactmoment (college/online sessie): alleen wat de student moet voorbereiden of meenemen, en de stelling. Geen draaiboek.
7. Bijlage "Tekst van de kennisclips (meelezen)": de gesproken tekst per dia; laat "Beeld: ..."-regels en productie-aanwijzingen weg.
   Tussenvragen in de clip: wel de vraag, niet het antwoord.
Toetsweken: week 5 en week 8/10 bevatten de rubric en de inlevereisen → die horen erin.

## Wat er NIET in mag (docentmateriaal)
Draaiboeken van college/online sessie, docentvoorbereiding, "Voor de docent", "Alleen voor de docent", docentnotities,
antwoordsleutels, modelantwoorden, uitwerkingen die de opdracht verklappen, juiste antwoorden + feedback van de weekcheck,
reservestellingen, nakijknotities, "Waar je op let" voor de docent, interne afstemming met A-AI2/A-DG/Janssen, open vragen aan collega's.
Twijfel? Laat weg en noem het in je rapport.

## Docentbestanden (niet uploaden)
- md/docent_weekcheck_wXX.md: per week de vijf vragen met juiste antwoord en feedback (letterlijk uit het doc).
- md/upload_wXX.md: uploadlijst voor die week: welke pdf en welke bestanden uit scratchpad/out/ (notebooks, csv, ows, xlsx, docx-sjablonen, video's)
  waar op MyCampus horen, plus wat nog ontbreekt (bv. video nog te maken).

## Stijl
Tekst letterlijk uit de docs; alleen inkorten/weglaten, niet herschrijven, behalve verwijzingen naar docentmateriaal die zonder context niet kloppen.
Bestandsnaam pdf: A-ET_WeekXX_studentversie.pdf (XX = 00..10). Controleer elke pdf: pdfinfo (pagina's), pdftotext | grep -i op
"docent|draaiboek|antwoord:|juist:|modelantwoord|sleutel" en bekijk 2 pagina's met pdftoppm -r 50.
