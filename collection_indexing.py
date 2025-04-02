import spacy.cli

# ----------------------------------------------------
import nltk
texte = "ceci est une phrase. Je veux tester. Héhé"
phrases = nltk.sent_tokenize(texte)
print(phrases)
# ------------------------------------------------------

spacy.cli.download("en_core_web_md")
nlp = spacy.load ( "en_core_web_md" )
