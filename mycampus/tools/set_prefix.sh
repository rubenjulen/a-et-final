#!/usr/bin/env bash
# Wisselt het MyCampus-voorvoegsel overal, bijvoorbeeld: tools/set_prefix.sh "ICT" "MAI"
# 1) vervangt "<OUD> A-ET" door "<NIEUW> A-ET" in de markdown van studentversies en uploadlijsten,
#    in titles.tsv, in build_package.sh, en in README.md en LINKS.md van de repository,
# 2) hernoemt het lesplan in lesmateriaal/ ("<OUD> A-ET Lesplan.docx/.pdf" -> "<NIEUW> A-ET Lesplan.*"),
# 3) rendert de studentpdf's opnieuw (kicker en titel uit titles.tsv),
# 4) bouwt het pakket en de zip opnieuw.
# Let op: de naam van het lesplan-doc op claude.ai en de tekst in het lesplan zelf pas je daar aan,
# en exporteer het lesplan daarna opnieuw.
set -euo pipefail
OLD="$1"; NEW="$2"; cd "$(dirname "$0")"; ROOT="$(cd ../.. && pwd)"
grep -l "$OLD A-ET" ../md/*.md 2>/dev/null | while read -r f; do sed -i "s/$OLD A-ET/$NEW A-ET/g" "$f"; echo "md: $f"; done
sed -i "s/$OLD A-ET/$NEW A-ET/g" titles.tsv
sed -i "s/^P=\"$OLD A-ET\"/P=\"$NEW A-ET\"/" build_package.sh
for f in "$ROOT/README.md" "$ROOT/LINKS.md"; do [ -f "$f" ] && sed -i "s/$OLD A-ET/$NEW A-ET/g" "$f"; done
for ext in docx pdf; do
  src="$ROOT/lesmateriaal/$OLD A-ET Lesplan.$ext"; dst="$ROOT/lesmateriaal/$NEW A-ET Lesplan.$ext"
  if [ -f "$src" ]; then
    if git -C "$ROOT" ls-files --error-unmatch "$src" >/dev/null 2>&1; then git -C "$ROOT" mv "$src" "$dst"; else mv "$src" "$dst"; fi
    echo "lesplan: $(basename "$dst")"
  fi
done
while IFS=$'\t' read -r base kicker title; do
  node render.js "../md/$base.md" "../pdf/$base.pdf" "$kicker" "$title" >/dev/null && echo "pdf: $base"
done < titles.tsv
bash build_package.sh
