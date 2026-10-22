#!/usr/bin/env python3
"""Vérifie les fiches du bac à sable (participants/ et groupe-*/).

Même principe que la vérification du corpus : un nom de fichier propre,
des champs remplis. Sans dépendance : python outils/verifier.py
"""
import os
import re
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
NOM = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)+\.md$")
CHAMPS = {"prenom": None, "ordinateur": {"mac", "pc"}, "couleur": None}


def lire(chemin):
    m = re.match(r"^---\s*\n(.*?)\n---", chemin.read_text(encoding="utf-8"), re.S)
    if not m:
        return None
    champs = {}
    for ligne in m.group(1).splitlines():
        ligne = re.sub(r"\s+#.*$", "", ligne).strip()
        if ":" in ligne:
            cle, val = ligne.split(":", 1)
            champs[cle.strip()] = val.strip().strip('"').strip("'").strip()
    return champs


def main():
    fichiers = sorted(RACINE.glob("participants/*.md")) + sorted(RACINE.glob("groupe-*/*.md"))
    fichiers = [f for f in fichiers if f.name.lower() != "readme.md"]
    erreurs = []
    for f in fichiers:
        rel = f.relative_to(RACINE)
        if not NOM.match(f.name):
            erreurs.append(f"{rel} : nom attendu en minuscules, sans accent ni espace, ex. camille-martin.md")
        champs = lire(f)
        if champs is None:
            erreurs.append(f"{rel} : l'en-tête entre les deux lignes « --- » a disparu")
            continue
        for cle, valeurs in CHAMPS.items():
            v = champs.get(cle, "").lower()
            if not v:
                erreurs.append(f"{rel} : champ « {cle} » vide")
            elif valeurs and v not in valeurs:
                erreurs.append(f"{rel} : « {cle} » doit valoir {' ou '.join(sorted(valeurs))} (trouvé : {v})")
    lignes = ["## Vérification du bac à sable", "", f"{len(fichiers)} fiche(s) contrôlée(s).", ""]
    lignes += ([f"### ❌ {len(erreurs)} erreur(s)", ""] + [f"- {e}" for e in erreurs]) if erreurs else ["### ✅ Tout est bon"]
    rapport = "\n".join(lignes)
    print(rapport)
    if os.environ.get("GITHUB_STEP_SUMMARY"):
        with open(os.environ["GITHUB_STEP_SUMMARY"], "a", encoding="utf-8") as s:
            s.write(rapport + "\n")
    sys.exit(1 if erreurs else 0)


if __name__ == "__main__":
    main()
