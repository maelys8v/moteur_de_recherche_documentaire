import spacy.cli
import nltk
import re
#spacy.cli.download("en_core_web_sm") # Load English tokenizer because the texts
from nltk.corpus import stopwords # liste de stopwords de NLTK
nlp = spacy.load("en_core_web_sm")
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')

with open("CISI/DATA/CISI.ALLnettoye") as f:
    documents = f.readlines()

nb_doc = 0

# len(documents) renvoie le nombre de caractère
# faire une boucle sur tous les fichiers
for line in documents:
    if re.findall(r"^\.I \d+", line):
        nb_doc += 1

print(nb_doc)


# Supprimer les tokens qui sont des stopwords
# Liste de stopwords de NLTK en anglais
stopWords = set(stopwords.words('english'))
# Une liste de stopwords trouvés sur internet
stopsWords_list = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

tokenized_words=[]
wordsFiltered = [w for w in tokenized_words if w not in stopWords] # Liste des mots filtrés


