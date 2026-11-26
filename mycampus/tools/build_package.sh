#!/usr/bin/env bash
# Bouwt het MyCampus-uploadpakket vanaf nul op met de naamgeving "$P <naam>" (voorvoegsel: variabele P hieronder).
# Bronnen: lesmateriaal/ (sjablonen, practica, video's, docentbestanden) en mycampus/pdf/ (kennispakketten, dia's, docent-pdf's).
# Indeling: 00_Algemeen, Blok0_Voorbereiden t/m Blok3_Verantwoorden, 99_Docent_niet_uploaden.
# Gebruik: tools/build_package.sh [doelmap]   (standaard: mycampus/upload, plus mycampus/A-ET_MyCampus_pakket.zip)
set -euo pipefail
HERE="$(cd "$(dirname "$0")/.." && pwd)"          # mycampus/
if [ -d "$HERE/../out" ]; then OUT="$(cd "$HERE/../out" && pwd)"; else OUT="$(cd "$HERE/../lesmateriaal" && pwd)"; fi                   # scratchpad/out/
PDF="$HERE/pdf"
U="${1:-$HERE/upload}"
P="ICT A-ET"

# 1. Docent-uploadlijst opnieuw samenstellen en renderen
{ echo "Wat er per blok op MyCampus komt, welke bestanden erbij horen en wat nog ontbreekt. Dit bestand is voor de docent."; echo
  echo "## Algemeen (buiten de blokken)"; sed -E 's/^# .*//; s/^## /### /' "$HERE/md/upload_studiewijzer.md"
  for b in 0 1 2 3; do f="$HERE/md/upload_blok$b.md"
    [ -f "$f" ] && { echo; sed -E 's/^# .*//' "$f" | awk 'NR==1&&/^## /{print;next} {sub(/^## /,"### ")} 1'; }
  done; } > "$HERE/md/DOCENT_uploadlijst.md"
(cd "$HERE/tools" && node render_docent.js ../md/DOCENT_uploadlijst.md ../pdf/DOCENT_Uploadlijst_MyCampus_A-ET.pdf "Uploadlijst" "Uploadlijst MyCampus" >/dev/null)

# 2. Pakket vanaf nul
rm -rf "$U"; mkdir -p "$U/00_Algemeen/Sjablonen" "$U/99_Docent_niet_uploaden/Opnamekits"
A="$U/00_Algemeen"; S="$A/Sjablonen"; I="$OUT/instrumenten"
cp "$PDF/A-ET_Studiewijzer_2026-2027.pdf"            "$A/$P Studiewijzer.pdf"
# Naslag en hulpmiddelen (lesmateriaal/algemeen): bronnamen beginnen met "ICT A-ET "; het voorvoegsel volgt $P
mkdir -p "$A/Naslag"
for f in "$OUT/algemeen/"*; do b="$(basename "$f")"; cp "$f" "$A/Naslag/$P ${b#* A-ET }"; done
cp "$PDF/A-ET_Beoordelingsrubric_studenten.pdf"      "$A/$P Beoordelingsrubric.pdf"
cp "$OUT/Voorbeeldrapport_ClaimWacht_A-ET_2026-2027.pdf" "$A/$P Voorbeeldrapport.pdf"
cp "$PDF/A-ET_Casusdossier_Suribank.pdf"             "$A/$P Casusdossier Suribank.pdf"
cp "$I/A-ET_werkboek_instrumenten_2026-2027.xlsx"    "$S/$P Werkboek instrumenten.xlsx"
cp "$I/K1_AI_Use_Case_en_Scope_Canvas.docx"          "$S/$P K1 Canvas.docx"
cp "$I/K5_Ethical_Dilemma_Canvas.docx"               "$S/$P K5 Dilemma Canvas.docx"
cp "$I/Sjabloon_tussenrapport_A1.docx"               "$S/$P Sjabloon tussenrapport.docx"
cp "$I/Sjabloon_eindrapport_A2.docx"                 "$S/$P Sjabloon eindrapport.docx"
cp "$I/Sjabloon_reflectie_A2.docx"                   "$S/$P Sjabloon reflectie.docx"
cp "$I/Evidence_card.docx"                           "$S/$P Evidence card.docx"
cp "$I/AI-verklaring.docx"                           "$S/$P AI-verklaring.docx"
cp "$I/Peerbeoordeling_A-ET.xlsx"                    "$S/$P Peerbeoordeling.xlsx"

# Per blok: kennispakket, collegedia's, video's en practica
B0="$U/Blok0_Voorbereiden"; B1="$U/Blok1_Analyseren"; B2="$U/Blok2_Ontwerpen"; B3="$U/Blok3_Verantwoorden"
mkdir -p "$B0" "$B1" "$B2" "$B3"
cp "$PDF/A-ET_Blok0_kennispakket.pdf" "$B0/$P Blok 0 Voorbereiden.pdf"
cp "$PDF/A-ET_Blok1_kennispakket.pdf" "$B1/$P Blok 1 Analyseren.pdf"
cp "$PDF/A-ET_Blok2_kennispakket.pdf" "$B2/$P Blok 2 Ontwerpen.pdf"
cp "$PDF/A-ET_Blok3_kennispakket.pdf" "$B3/$P Blok 3 Verantwoorden.pdf"
cp "$PDF/A-ET_College1_dias.pdf" "$B1/$P College 1.pdf"
cp "$PDF/A-ET_College2_dias.pdf" "$B1/$P College 2.pdf"
cp "$PDF/A-ET_College3_dias.pdf" "$B2/$P College 3.pdf"
cp "$OUT/week0/Kennisclip2_Waarom_maakt_AI_fouten_Matilda.mp4" "$B0/$P Kennisclip 2.mp4"
cp "$OUT/week0/Kennisclip3_Fouten_tellen_Matilda.mp4"          "$B0/$P Kennisclip 3.mp4"
cp "$OUT/blok1/Kennisclip5b_Vijf_ethische_kaders_Matilda.mp4"   "$B1/$P Kennisclip 5b.mp4"
cp "$OUT/blok1/Kennisclip5c_Drie_soorten_black_box_Matilda.mp4"  "$B1/$P Kennisclip 5c.mp4"
# Practica als zip; binnen de zip blijven de originele namen (notebooks lezen de csv's op naam)
mkzip(){ (cd "$1" && rm -f "$2" && zip -qX "$2" *); }
mkzip "$OUT/week0/practicum1"   "$B0/$P Practicum 1.zip"
mkzip "$OUT/week3/practicum2_3" "$B1/$P Practicum 2 en 3.zip"
mkzip "$OUT/week4/practicum4"   "$B1/$P Practicum 4.zip"
mkzip "$OUT/week9/practicum5"   "$B3/$P Practicum 5.zip"

# 3. Docentmap (interne namen, niet uploaden)
D="$U/99_Docent_niet_uploaden"
# Decks met sprekersnotities (voor de docent en als bron voor Gamma)
for f in "$PDF"/docent/A-ET_College*_notities.pdf; do [ -f "$f" ] || continue; n="${f##*College}"; n="${n%%_*}"; cp "$f" "$D/$P College $n met notities.pdf"; done
for f in "$HERE"/decks/gamma/Gamma_prompt_college*.txt; do [ -f "$f" ] || continue; n="${f##*college}"; n="${n%%.*}"; cp "$f" "$D/$P Gamma-prompt college $n.txt"; done
cp "$PDF/DOCENT_Kennischecks_antwoorden_A-ET.pdf" "$PDF/DOCENT_Uploadlijst_MyCampus_A-ET.pdf" "$PDF/DOCENT_Practicum5_verwachte_uitkomsten.pdf" "$D/"
cp "$HERE/../lesmateriaal/docent/ICT A-ET Kennischecks invoer.xlsx" "$HERE/../lesmateriaal/docent/ICT A-ET Kennischecks GIFT.txt" "$D/"
cp "$OUT"/feedback/*.docx "$D/"
cp "$OUT/Beoordelingsrubric_AI_en_Ethics_A-ET_2026-2027.xlsx" "$OUT/$P Lesplan.pdf" "$OUT/Kruistabel_certificeringen_A-ET.pdf" "$D/"
# Opnamekits onder de bloknaam (bronbestanden houden hun werknaam)
for f in "$PDF"/opnamekits/Opnamekit_Week*.pdf; do b="$(basename "$f" .pdf)"; w="${b#Opnamekit_Week}"; w="${w%%_*}"; rest="${b#Opnamekit_Week??_}"
  case "$w" in 00) bl=0;; 01|02|03|04|05) bl=1;; 06|07|08) bl=2;; *) bl=3;; esac
  r="${rest//_/ }"; r="${r/clip1/clip 1}"; cp "$f" "$D/Opnamekits/$P Opnamekit Blok $bl $r.pdf"; done
cp "$OUT/week10/Cijferbestand_A-ET_2026-2027.xlsx" "$D/$P Cijferbestand.xlsx"

# 4. Zip
if [ -z "${1:-}" ]; then
  (cd "$HERE" && rm -f A-ET_MyCampus_pakket.zip && zip -qr A-ET_MyCampus_pakket.zip upload -x "*.html")
  echo "Pakket: $HERE/A-ET_MyCampus_pakket.zip"
fi
echo "Klaar: $U"
