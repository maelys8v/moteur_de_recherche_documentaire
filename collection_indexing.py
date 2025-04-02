import spacy.cli
spacy.cli.download("en_core_web_sm") # Load English tokenizer because the texts
nlp = spacy.load("en_core_web_sm")

with open('CISI/DATA/CISI.ALLnettoye') as documents:
    print(documents.read())

# faire une boucle sur tous les fichiers
# a chq fichier on tokenise
