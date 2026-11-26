# AI & Ethics (A-ET) · lesmateriaal 2026-2027

Volledig lesmateriaal voor de module AI & Ethics (A-ET) van de minor AI (Janssen University), januari–maart 2027.
De module heeft drie colleges en vier blokken (0 Voorbereiden, 1 Analyseren, 2 Ontwerpen, 3 Verantwoorden). De bewerkbare bronnen (lesplan, collegedecks, docentdossiers) staan op claude.ai; zie [LINKS.md](LINKS.md).
Deze repository bewaart de gegenereerde bestanden en alles om ze opnieuw te maken.

## Mappen

| Map | Inhoud |
| --- | --- |
| `lesmateriaal/` | Lesplan (`ICT A-ET Lesplan.docx`/`.pdf`), beoordelingsrubric (xlsx), voorbeeldrapport, kruistabel certificeringen, feedbackformulieren, werkboek instrumenten en Word-sjablonen (`instrumenten/`), practica met notebooks en datasets (bronmappen `week0`, `week3`, `week4`, `week9`; in het pakket staan ze per blok), kennisclips 2 en 3 (`week0/*.mp4`), voorvertoningen van de animaties (`preview/`), berichten aan Janssen, docenten en administratie |
| `mycampus/` | Kennispakketten per blok en naslag als markdown (`md/`) en pdf (`pdf/`), docentbestanden (kennischeck-antwoorden, uploadlijst per blok), collegedecks met generatoren (`decks/gen_c1-3.py`), huisstijl en scripts (`tools/`); verouderde weekbestanden in `archief/` |
| `animatie/` | Remotion-project voor de kennisclips: scènes (`src/`), spreekteksten per clip (`clip*/zinnen.json`, `kaders/*/zinnen.json`), uitspraaklijst (`uitspraak.json`), ingesproken zinnen (`public/aud_*`), spraakscript (`tts_elevenlabs.py`) |
| `opnamekits/` | Bronbestanden van de dia-decks waarmee de docent clips 11–22 zelf opneemt |
| `scripts/` | Generatoren voor rubric, werkboek, sjablonen, feedbackformulieren, notebooks en datasets |

## MyCampus-pakket opnieuw maken

```bash
cd animatie && npm install      # levert ook de lettertypen voor de pdf's
cd ../mycampus/tools && bash build_package.sh
```

Het pakket komt in `mycampus/upload/` (mappen 00_Algemeen, Blok0_Voorbereiden tot en met Blok3_Verantwoorden, 99_Docent_niet_uploaden) en `mycampus/A-ET_MyCampus_pakket.zip` (niet in git).
Naamgeving volgens de MyCampus-conventie: `ICT A-ET <naam>` (huidige waarde van het voorvoegsel: `ICT`). Het voorvoegsel later wisselen, bijvoorbeeld naar `MAI`:

```bash
bash mycampus/tools/set_prefix.sh "ICT" "MAI"
```

Een kennispakket opnieuw renderen: `node mycampus/tools/render.js mycampus/md/<bestand>.md mycampus/pdf/<bestand>.pdf "Blok N" "<titel>"` (titels staan in `mycampus/tools/titles.tsv`).

## Kennisclips (animatie)

```bash
cd animatie
python3 tts_elevenlabs.py clip5/zinnen.json public/aud_c5      # inspreken (Matilda, eleven_v3)
python3 scripts_timing_wk1.py                                   # echte duur in de timing
npx remotion render src/entry_wk1.jsx Clip5 out/Clip5.mp4 --concurrency=4
```

Entries per week: `src/entry_wk1.jsx` (kaderclip A, clip 5), `src/entry_wk2.jsx` (clips 6–8), `src/entry_wk3.jsx` (clips 9, 10, kaderclip B); `src/index.jsx` bevat clips 2–4.
Stand: clips 2 tot en met 10, 5b, 5c en kaderclips A en B klaar (ingesproken met Matilda; timing met `scripts_timing_c4.py`, `scripts_timing_wk1.py` en `scripts_timing_wk3.py <zinnen> <audiomap> <timing>`; testbeelden met `node stills_any.mjs <entry> <compositie> <timing> <sleutel+sec,...>`). Clips 2-10, A en B in de oorspronkelijke groene stijl; 5b en 5c in Janssen-huisstijl (`src/Clip5b.jsx`, `src/Clip5c.jsx`, gedeeld `src/janssen_kit.jsx` en `src/janssen_parts.jsx`, entries `src/entry_c5b.jsx` en `src/entry_c5c.jsx`, scripts `clip5b/build.py` en `clip5c/build.py`, timing `scripts_timing_c5b.py` en `scripts_timing_c5c.py`); kaderclips C–E nog te bouwen; clips 11–22 neemt de docent zelf op met de opnamekits.

## Let op

- Privé houden: de map `mycampus/` en `lesmateriaal/` bevatten docentmateriaal (antwoorden, nakijknotities, lesplan met vragen aan Janssen). Alleen wat in het uploadpakket staat, is voor studenten.
- Een deel van de bouwscripts is in de werkomgeving gemaakt en verwijst nog naar het oude werkpad (`/tmp/claude-0/…/scratchpad`). Pas het basispad bovenaan zo'n script aan voordat je het draait. `build_package.sh`, `set_prefix.sh`, `render.js` en `decks2pdf.js` werken direct vanuit de repository. `set_prefix.sh` past ook `titles.tsv`, `build_package.sh`, deze README, `LINKS.md` en de bestandsnaam van het lesplan aan; de naam en tekst van het lesplan-doc op claude.ai pas je daar aan, waarna je het lesplan opnieuw exporteert.
- Geen API-sleutels in deze repository: `tts_elevenlabs.py` leest de sleutel uit `ELEVENLABS_API_KEY`.
