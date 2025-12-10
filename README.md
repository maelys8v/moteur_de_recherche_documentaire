# Moteur de Recherche Documentaire – TF-IDF & Cosine Similarity

**Projet IR sur le corpus CISI – Python, spaCy, SciPy**

Ce projet implémente un moteur de recherche documentaire simplifié. Il charge, nettoie et indexe des documents du corpus **CISI**, puis applique une vectorisation **TF-IDF**, un **index inversé** et un **calcul de similarité cosinus** pour classer les documents les plus pertinents face à une requête.

---

## Fonctionnalités

### Prétraitement du texte

- Nettoyage (espaces, ponctuation…)
- Tokenisation avec **spaCy**
- Lemmatisation
- Suppression des stopwords (**NLTK**)

### Indexation des documents

- Calcul TF-IDF pour chaque terme
- Construction d’un vecteur de caractéristiques par document
- Génération d’un **inverted index** pour accès rapide

### Recherche par requête

- Extraction des requêtes `CISI_dev.QRY`
- Lemmatisation et vectorisation identique aux documents
- Calcul de **similarité cosinus** entre vecteur requête et vecteur document
- Classement des documents les plus pertinents

### Évaluation

- Génération d’un fichier `.REL` compatible avec les outils d’évaluation IR (rappel, précision, MAP…)

---

## Organisation du projet

```
moteur_de_recherche_documentaire
│
├── CISI/DATA/
│   ├── CISI.ALLnettoye       # Corpus nettoyé
│   ├── CISI_dev.QRY          # Requêtes
│   └── eval.pl               # Script d’évaluation
│
├── collection_indexing.py    # Indexation TF-IDF et vecteurs
├── eval.py                   # Génération fichier .REL
├── shrink.py                 # Réduction de dataset pour tests
├── README.md                 # Documentation
└── test_eval.REL             # Résultat exemple
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

## Guide d’installation et d’exécution

### Étape 1 – Cloner le projet

`git clone https://github.com/maelys8v/moteur_de_recherche_documentaire.git cd moteur_de_recherche_documentaire`

### Étape 2 – Créer un environnement Python (optionnel mais recommandé)

```shell
python -m venv venv 
source venv/bin/activate      # Linux/Mac 
venv\Scripts\activate         # Windows
```

### Étape 3 – Installer les dépendances

`pip install -r requirements.txt`

### Étape 4 – Télécharger le modèle spaCy

`python -m spacy download en_core_web_md`

### Étape 5 – Exécuter le script principal

`python collection_indexing.py`

- Le script traitera les fichiers du dossier `CISI/DATA/`
- Il produira le fichier d’évaluation `test_eval.REL` (si on exécutes `eval.py` après l’indexation)

---

## Compétences démontrées

- Python avancé
- NLP : Tokenisation, Lemmatisation, Stopwords
- TF-IDF, Cosine Similarity
- Construction de fichiers inversés
- Pipeline IR complète et évaluable

---

## 📜 Licence

MIT License – Projet académique

---
