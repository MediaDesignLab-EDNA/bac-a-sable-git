# Antisèche Git au terminal

## 0. Une seule fois : installer et configurer

| | Mac | PC (Windows) |
|---|---|---|
| Le terminal | App **Terminal** (Applications → Utilitaires) | **Git Bash**, installé avec Git |
| Installer Git | Tapez `git --version` dans Terminal. Si Git manque, macOS propose d'installer les « outils de ligne de commande » : acceptez (quelques minutes). | Téléchargez **Git for Windows** sur [git-scm.com](https://git-scm.com), installez en gardant les options par défaut. |
| Installer GitHub CLI | Installateur pour Mac sur [cli.github.com](https://cli.github.com) | Installateur pour Windows sur [cli.github.com](https://cli.github.com) |

Puis, **dans le terminal** (Mac et PC), une ligne à la fois :

```
gh auth login
```

Répondez : `GitHub.com` → `HTTPS` → `Yes` (authentifier Git) →
`Login with a web browser`. Copiez le code affiché, appuyez sur Entrée, collez
le code dans la page qui s'ouvre et validez. Ensuite :

```
git config --global user.name "Prénom Nom"
git config --global user.email "adresse@de-votre-compte-github"
git config --global pull.rebase true
git config --global core.editor nano
```

Vérifiez : `git config --global --list` doit afficher vos réglages.

## 1. Se repérer

| Je veux… | Mac | PC (Git Bash) |
|---|---|---|
| savoir où je suis | `pwd` | `pwd` |
| voir le contenu du dossier | `ls` | `ls` |
| entrer dans un dossier | `cd nom-du-dossier` | `cd nom-du-dossier` |
| remonter d'un cran | `cd ..` | `cd ..` |
| aller dans Documents | `cd ~/Documents` | `cd ~/Documents` |
| ouvrir le dossier dans le Finder / l'Explorateur | `open .` | `explorer .` |
| ouvrir un fichier texte | `open -e fichier.md` | `notepad fichier.md` |
| coller dans le terminal | Cmd + V | Maj + Inser, ou clic droit → Paste |
| compléter un nom | Tab | Tab |
| arrêter une commande | Ctrl + C | Ctrl + C |

Astuce : glissez un dossier depuis le Finder ou l'Explorateur dans la fenêtre du
terminal après avoir tapé `cd ` : son chemin s'écrit tout seul.

## 2. Le cycle de chaque séance

```
git pull
git status
git add <fichier-ou-dossier>
git commit -m "Ce que j'ai fait"
git push
```

| Commande | Ce qu'elle fait |
|---|---|
| `git clone <adresse>` | Une seule fois : copie le dépôt sur votre ordinateur. |
| `git pull` | Récupère ce que les autres ont envoyé. **Toujours en premier.** |
| `git status` | Votre boussole : sur quelle branche, quels fichiers ont changé. |
| `git add <chemin>` | Prépare des fichiers pour le prochain commit. |
| `git commit -m "…"` | Enregistre une étape, avec une phrase. |
| `git push` | Envoie vos commits sur GitHub. |
| `git switch <branche>` | Passe sur une autre branche (`groupe-B`). |
| `git log --oneline` | L'historique, un commit par ligne (`q` pour quitter). |

## 3. Lire `git status`

```
On branch groupe-B                          ← la branche où vous êtes
Your branch is ahead of 'origin/groupe-B'
by 1 commit.                                ← commit fait, mais pas encore poussé
Changes not staged for commit:
        modified:   fiches/B-07-F.md        ← modifié, pas encore « add »
Untracked files:
        originaux/B-07-F.png                ← nouveau, pas encore « add »
```

`nothing to commit, working tree clean` : tout est enregistré.

## 4. Si ça coince

| Ce que vous voyez | Ce qu'il faut faire |
|---|---|
| `! [rejected] … (fetch first)` | Quelqu'un a poussé avant vous : `git pull`, puis `git push`. |
| `not a git repository` | Vous n'êtes pas dans le dossier du dépôt : `cd ~/Documents/<depot>`. |
| `Authentication failed` / on vous demande un mot de passe | Le mot de passe GitHub ne marche pas ici : refaites `gh auth login`. |
| `Please tell me who you are` | Refaites les deux `git config --global user…` de la partie 0. |
| `push declined due to email privacy` | Utilisez votre adresse `…@users.noreply.github.com` (GitHub → Settings → Emails) dans `git config --global user.email`. |
| `CONFLICT` après un `git pull` | Voir le bonus du README ; en cas de doute : `git rebase --abort`, puis appelez l'enseignant. |
| Un éditeur s'ouvre dans le terminal (nano) | Ctrl + O, Entrée pour enregistrer, puis Ctrl + X pour quitter. |
| Un écran avec `~` partout ou `(END)` | Tapez `q`. Si ça ne suffit pas : Échap, puis `:q!` et Entrée. |
| Mac : `xcrun: error: invalid active developer path` | `xcode-select --install`, puis recommencez. |
| PC : `git` ou `gh` « command not found » | Fermez et rouvrez Git Bash après l'installation. |
| Vous avez commité sur la mauvaise branche | Ne poussez pas ; appelez l'enseignant. |

**Ne jamais faire** : `git push --force`, `git reset --hard` (sauf si
l'enseignant le demande).
