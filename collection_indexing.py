import spacy.cli
# spacy.cli.download("en_core_web_sm") # Load English tokenizer because the texts
nlp = spacy.load("en_core_web_sm")

# ----------------------------------------------------
import nltk
from nltk.corpus import stopwords # liste de stopwords de NLTK
# nltk.download('punkt')
# nltk.download('punkt_tab')
nltk.download('stopwords')

texte = "ceci est une phrase. Je veux tester. Héhé"
phrases = nltk.sent_tokenize(texte)
print(phrases)
# ------------------------------------------------------

with open('CISI/DATA/CISI.ALLnettoye') as documents:
    print(documents.read())

# faire une boucle sur tous les fichiers
# a chq fichier on tokenise


# Choose what vocabulary we want to keep and do the associate processing
stopWords = set(stopwords.words('english')) # Liste de stopwords de NLTK en anglais
# Une liste de stopwords trouvés sur internet
stopsWords_list = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]



