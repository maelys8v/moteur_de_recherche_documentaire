
# Information Retrieval System – TF-IDF & Cosine Similarity

**Projet IR sur le corpus CISI – Python, spaCy, SciPy**

Ce projet implémente **un moteur de recherche documentaire simplifié**, basé sur les techniques classiques d’_Information Retrieval_.  
Il charge, nettoie et indexe des documents du corpus **CISI**, puis applique une vectorisation **TF-IDF**, un **index inversé** et un **calcul de similarité cosinus** pour classer les documents les plus pertinents face à une requête.

---

## Fonctionnalités

### Prétraitement du texte

- Nettoyage (espaces, ponctuation…)
- Tokenisation avec _spaCy_
- Lemmatisation
- Suppression des stopwords (NLTK)

### Indexation des documents

- Calcul du **TF-IDF** pour chaque terme
- Construction d’un **vecteur de caractéristiques** par document
- Génération d’un **fichier inversé** (inverted index) pour accès rapide
### Recherche par requête

- Extraction des requêtes `CISI.QRY`
- Lemmatisation + vectorisation identique aux documents
- Calcul de similarité cosinus entre :
    - vecteur requête
    - vecteur document
### Évaluation

- Génération d’un fichier `.REL` compatible avec les outils d’évaluation IR :
    - rappel / précision
    - MAP
    - etc.
## Architecture du projet

```
Information Retrieval
│
├── CISI/
│   ├── DATA/
│   │   ├── CISI.ALL
│   │   ├── CISI.QRY
|   |   ├── eval.pl
│   │   └── …
│
├── eval.py
├── collection_indexing.py
├── shrink.py    (pour réduire la data)
└── README.md
```

---

## Technologies

- Python 3
- spaCy (lemmatisation NLP)
- NumPy
- SciPy (cosine similarity)
- NLTK (stopwords)
- tqdm (progress bars)

---
## Objectifs pédagogiques

- Comprendre le fonctionnement d’un moteur de recherche traditionnel
- Manipuler TF-IDF, index inversés et vecteurs de similarité
- Travailler sur un dataset IR réel (CISI)
- Implémenter une pipeline complète NLP + vectorisation

---
## Licence

Projet académique – libre d’adaptation.

---
