#!/usr/bin/env bash
# Wisselt het MyCampus-voorvoegsel overal, bijvoorbeeld: tools/set_prefix.sh "BK-ICT" "MAI"
# 1) vervangt "<OUD> A-ET" door "<NIEUW> A-ET" in de markdown van studentversies en uploadlijsten,
# 2) rendert de studentpdf's opnieuw (kicker en titel uit titles.tsv),
# 3) zet het voorvoegsel in build_package.sh en bouwt het pakket en de zip opnieuw.
set -euo pipefail
OLD="$1"; NEW="$2"; cd "$(dirname "$0")"
grep -l "$OLD A-ET" ../md/*.md | while read -r f; do sed -i "s/$OLD A-ET/$NEW A-ET/g" "$f"; echo "md: $f"; done
sed -i "s/^P=\"$OLD A-ET\"/P=\"$NEW A-ET\"/" build_package.sh
while IFS=$'\t' read -r base kicker title; do
  node render.js "../md/$base.md" "../pdf/$base.pdf" "$kicker" "$title" >/dev/null && echo "pdf: $base"
done < titles.tsv
bash build_package.sh
