# taleo

## ToDo
### A faire
- externaliser la liste dans un fichier qu'on open
- 

### Améliorations
- TF IDF
- faire une stopword liste personnalisée aux textes qu'on a
- première version : on prend les 10 mots les moins fréquents

## Git
* accepter une modif : git fetch + git merge
* proposer une modif : git add . + git commit -m "message" + git push

## prises de notes de chacunes
### Lou
### Léna
- TF IDF ou booléen ?
- lemming mieux que stemming
- on met que des lemmes dans stopword: lemme sur txt et lemme sur stopword et on applique stopword
### Jeanne
### Maëlys
#### pour la step 1 part1 :
- passer de txt à liste de mots
- traiter ces mots avec la fréquence -> dico
##### étapes
1. séparer les textes avec I.
2. segmenter chaque txt et stoquer les fréquences des mots dans un dico
   3. utiliser nltk pour avoir les mots
      4. Faire la stop words
      5. faire le stemming avec nltk
      4. faire une liste de dicos avec un dico par texte
4. fin
