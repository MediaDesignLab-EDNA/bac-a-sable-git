# Préparer le bac à sable (enseignant)

À faire une fois, avant la séance.

1. Créer un dépôt **privé** vide `bac-a-sable-git` sur GitHub (dans
   l'organisation du lab ou sur votre compte), sans README.
2. Dans le dossier de ce bac à sable, sur votre ordinateur :

   ```
   git init -b main
   git add .
   git commit -m "Bac à sable"
   git remote add origin https://github.com/<ORGANISATION>/bac-a-sable-git.git
   git push -u origin main
   sh outils/preparer-branches.sh A B C D E F
   ```

   Le script crée une branche et un dossier par groupe (`groupe-A`…) et les
   pousse. Adaptez la liste des lettres au nombre de groupes.
3. Ajouter les étudiant·es avec le droit d'écriture : *Settings →
   Collaborators* (ou une équipe de l'organisation avec le rôle *Write*).
   Ils doivent **accepter l'invitation** reçue par e-mail avant jeudi.
4. Remplacer `<ORGANISATION>` dans `README.md` par le vrai nom, puis commit et
   push.

Ne protégez **pas** `main` dans le bac à sable : l'exercice 1 consiste
justement à y pousser à plusieurs pour provoquer le refus. (Dans le dépôt du
corpus, au contraire, `main` est protégée.)

Après la séance, le dépôt peut être supprimé ou archivé.
