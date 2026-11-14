# AI & Ethics (A-ET) · lesmateriaal 2026-2027

Volledig lesmateriaal voor de module AI & Ethics (A-ET) van de minor AI (Janssen University), januari–maart 2027.
De bewerkbare bronnen (weekdocumenten, lesplan, dia's) staan op claude.ai; zie [LINKS.md](LINKS.md).
Deze repository bewaart de gegenereerde bestanden en alles om ze opnieuw te maken.

## Mappen

| Map | Inhoud |
| --- | --- |
| `lesmateriaal/` | Lesplan (docx/pdf), beoordelingsrubric (xlsx), voorbeeldrapport, kruistabel certificeringen, feedbackformulieren, werkboek instrumenten en Word-sjablonen (`instrumenten/`), practica met notebooks en datasets (`week0`, `week3`, `week4`, `week9`), kennisclips 2 en 3 (`week0/*.mp4`), voorvertoningen van de animaties (`preview/`), berichten aan Janssen, docenten en administratie |
| `mycampus/` | Studentversies als markdown (`md/`) en pdf (`pdf/`), docentbestanden (weekcheck-antwoorden, uploadlijst), dia-pdf's (`decks/`), huisstijl en scripts (`tools/`) |
| `animatie/` | Remotion-project voor de kennisclips: scènes (`src/`), spreekteksten per clip (`clip*/zinnen.json`, `kaders/*/zinnen.json`), uitspraaklijst (`uitspraak.json`), ingesproken zinnen (`public/aud_*`), spraakscript (`tts_elevenlabs.py`) |
| `opnamekits/` | Bronbestanden van de dia-decks waarmee de docent clips 11–22 zelf opneemt |
| `scripts/` | Generatoren voor rubric, werkboek, sjablonen, feedbackformulieren, notebooks en datasets |

## MyCampus-pakket opnieuw maken

```bash
cd animatie && npm install      # levert ook de lettertypen voor de pdf's
cd ../mycampus/tools && bash build_package.sh
```

Het pakket komt in `mycampus/upload/` en `mycampus/A-ET_MyCampus_pakket.zip` (niet in git).
Naamgeving volgens de MyCampus-conventie: `<studierichting> A-ET <naam>`. Het voorvoegsel wisselen (bijvoorbeeld naar de code die de administratie opgeeft):

```bash
bash mycampus/tools/set_prefix.sh "BK-ICT" "MAI"
```

Een studentversie opnieuw renderen: `node mycampus/tools/render.js mycampus/md/<bestand>.md mycampus/pdf/<bestand>.pdf "Week N" "<titel>"` (titels staan in `mycampus/tools/titles.tsv`).

## Kennisclips (animatie)

```bash
cd animatie
python3 tts_elevenlabs.py clip5/zinnen.json public/aud_c5      # inspreken (Matilda, eleven_v3)
python3 scripts_timing_wk1.py                                   # echte duur in de timing
npx remotion render src/entry_wk1.jsx Clip5 out/Clip5.mp4 --concurrency=4
```

Entries per week: `src/entry_wk1.jsx` (kaderclip A, clip 5), `src/entry_wk2.jsx` (clips 6–8), `src/entry_wk3.jsx` (clips 9, 10, kaderclip B); `src/index.jsx` bevat clips 2–4.
Stand: clips 2 en 3 klaar; clip 4 en de animaties voor weken 1–3 wachten op stemtegoed; kaderclips C–E nog te bouwen; clips 11–22 neemt de docent zelf op met de opnamekits.

## Let op

- Privé houden: de map `mycampus/` en `lesmateriaal/` bevatten docentmateriaal (antwoorden, nakijknotities, lesplan met vragen aan Janssen). Alleen wat in het uploadpakket staat, is voor studenten.
- Een deel van de bouwscripts is in de werkomgeving gemaakt en verwijst nog naar het oude werkpad (`/tmp/claude-0/…/scratchpad`). Pas het basispad bovenaan zo'n script aan voordat je het draait. `build_package.sh`, `set_prefix.sh`, `render.js` en `decks2pdf.js` werken direct vanuit de repository.
- Geen API-sleutels in deze repository: `tts_elevenlabs.py` leest de sleutel uit `ELEVENLABS_API_KEY`.
