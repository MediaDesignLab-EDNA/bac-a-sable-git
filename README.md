# Bac à sable Git

Un dépôt pour **s'entraîner sans risque** à envoyer (push) et récupérer (pull)
avant de déposer le vrai corpus. Ici, on peut tout casser : rien n'est grave.

Durée : 15 minutes en salle, plus un bonus facultatif.
Prérequis : avoir fait l'installation de [ANTISECHE.md](ANTISECHE.md) (partie 0).

> **Mac** : ouvrez l'app **Terminal**.
> **PC** : ouvrez **Git Bash** (pas l'invite de commandes ni PowerShell) :
> toutes les commandes ci-dessous y fonctionnent à l'identique.
>
> Tapez ou collez les commandes **une ligne à la fois**, puis Entrée.
> Remplacez ce qui est entre `< >` (sans garder les chevrons).

---

## Exercice 1 — Se présenter (7 min)

**But : faire son premier push, et rencontrer son premier refus.**

1. Se placer dans Documents et récupérer le dépôt :

   ```
   cd ~/Documents
   git clone https://github.com/<ORGANISATION>/bac-a-sable-git.git
   cd bac-a-sable-git
   ```

2. Créer **votre** fiche à partir du modèle (prénom et nom en minuscules,
   sans accent ni espace, avec un tiret) :

   ```
   cp modele-participant.md participants/<prenom-nom>.md
   ```

3. Remplir la fiche :

   - Mac : `open -e participants/<prenom-nom>.md`
   - PC : `notepad participants/<prenom-nom>.md`

   Remplissez les trois champs, **enregistrez**, fermez l'éditeur.

4. Regarder ce que Git a remarqué, puis préparer, enregistrer et envoyer :

   ```
   git status
   git add participants/<prenom-nom>.md
   git commit -m "Ajout de <Prénom>"
   git push
   ```

5. **Votre push est refusé ?** C'est normal, et c'est le cœur de l'exercice :
   un·e camarade a envoyé quelque chose avant vous. Récupérez, puis renvoyez :

   ```
   git pull
   git push
   ```

## Exercice 2 — Récupérer le travail des autres (3 min)

1. Attendez que vos voisin·es aient fini, puis :

   ```
   git pull
   ls participants
   git log --oneline
   ```

2. Combien de fiches dans `participants/` ? Qui a poussé juste avant vous ?

## Exercice 3 — Travailler sur la branche de son groupe (5 min)

**But : le geste exact du dépôt du corpus.** Chaque groupe a sa branche
(`groupe-A`, `groupe-B`…), et chacun n'écrit que dans le dossier de son groupe.

1. Passer sur la branche de votre groupe et vérifier :

   ```
   git switch groupe-<X>
   git status
   ```

   La première ligne doit dire `On branch groupe-<X>`.

   Le dossier `participants/` ne contient plus votre fiche : c'est normal,
   elle est restée sur `main`. Une branche est une version parallèle du dépôt.

2. Créer une fiche dans le dossier du groupe, **sans la remplir** pour
   l'instant, et l'envoyer :

   ```
   cp modele-participant.md groupe-<X>/<prenom-nom>.md
   git add groupe-<X>
   git commit -m "Fiche de <Prénom> dans le groupe <X>"
   git push
   ```

3. Ouvrez `https://github.com/<ORGANISATION>/bac-a-sable-git/pulls`.
   **Une seule personne par groupe** ouvre la pull request
   (*New pull request*, base : `main` ← compare : `groupe-<X>`).
   Les push suivants s'y ajoutent tout seuls.

4. Regardez la vérification automatique, en bas de la pull request : elle
   est **rouge**, puisque votre fiche est vide. Cliquez sur *Details* : la
   liste dit quel fichier corriger et quels champs manquent.

5. Remplissez la fiche (`open -e` ou `notepad`, comme à l'exercice 1),
   enregistrez, puis :

   ```
   git add groupe-<X>
   git commit -m "Fiche de <Prénom> complétée"
   git push
   ```

   Rechargez la pull request : la coche passe au vert quand **toutes** les
   fiches du groupe sont complètes. C'est exactement ce qui se passera avec
   les fiches du corpus.

## Bonus — Le conflit (10 min, en binôme)

Ce qui arrive quand deux personnes modifient **la même ligne** du même fichier.
Dans le corpus, ça n'arrive pas si chacun reste dans son dossier ; mais autant
savoir le résoudre.

1. Les deux, sur `main`, **au même moment** (avant que l'un ou l'autre n'ait
   poussé quoi que ce soit) :

   ```
   git switch main
   git pull
   ```

2. Ouvrez `binomes.md`, trouvez la ligne de votre binôme, et écrivez **chacun
   une couleur différente** à la place de `?`. Enregistrez.
3. Les deux :

   ```
   git add binomes.md
   git commit -m "Couleur du binôme"
   git push
   ```

4. La personne dont le push est refusé fait `git pull`. Git annonce
   `CONFLICT`. Ouvrez `binomes.md` : vous y voyez les deux versions.

   ```
   <<<<<<< HEAD
   | 03 | vert |
   =======
   | 03 | rouge |
   >>>>>>> 04576e9 (Couleur du binôme)
   ```

   Au-dessus de `=======` : la version déjà sur GitHub. En dessous : la vôtre.

5. Gardez **une** ligne (ou écrivez « vert et rouge »), supprimez les lignes
   `<<<<<<<`, `=======` et `>>>>>>>`, enregistrez, puis :

   ```
   git add binomes.md
   git -c core.editor=true rebase --continue
   git push
   ```

Si vous êtes perdu·e en plein conflit : `git rebase --abort` revient à l'état
d'avant le `git pull`.

---

L'antisèche complète, avec le dépannage : [ANTISECHE.md](ANTISECHE.md).
