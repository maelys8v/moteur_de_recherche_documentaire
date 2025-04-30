# taleo

## Remarques
/!\ Un fichier CISI_test.ALLnettoye a été crée avec juste 10 documents pour tester plus rapidement sur moins de données pendant la phase de développement.

## Améliorations
- faire une stopword liste personnalisée aux textes qu'on a
- première version : on prend les 10 mots les moins fréquents
- faire en sorte que ça ne soit pas sensible à la casse (majuscule ou minuscule peu importe): FAIT
- 'united-states' devient 'united' et 'states', piste d'amélioration

## Git
* accepter une modif : git fetch + git merge
* proposer une modif : git add . + git commit -m "message" + git push

## prises de notes de chacunes
### Lou
### Léna
- TODO
  - tester weighting suite aux tests de tfidf
- redondances d'info dans nbDocContenantW(word) (mais c'est pas grave)
- pourquoi y a detailed et pas detail dans la liste des dicos
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
#### step 2
##### build the search engine
1. query indexing : to index the queries, use the same methodology and the same weighting
schemes as for documents.
2. implementation of a search engine to answer the queries : a similarity measure between the
indexing vectors of the queries and the documents has to be chosen and implemented. **The
expected output is a ranked list of documents calculated by the system in response to a given
query.**
