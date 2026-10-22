#!/bin/sh
# Crée une branche groupe-X (avec son dossier) par lettre passée en argument, et la pousse.
# Usage : sh outils/preparer-branches.sh A B C D E F
set -e
[ "$#" -gt 0 ] || { echo "Usage : sh outils/preparer-branches.sh A B C ..."; exit 1; }
git switch main
for g in "$@"; do
  b="groupe-$g"
  git switch -c "$b" main
  mkdir -p "$b"
  printf '# Groupe %s\n\nDéposez ici vos fiches (prenom-nom.md).\n' "$g" > "$b/README.md"
  git add "$b"
  git commit -m "Branche du groupe $g"
  git push -u origin "$b"
  git switch main
done
echo "Branches créées : $(printf 'groupe-%s ' "$@")"
