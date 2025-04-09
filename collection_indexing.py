import spacy.cli
import math
#spacy.cli.download("en_core_web_md") # Load English tokenizer in middle size because the texts are in english
nlp = spacy.load("en_core_web_md")

import nltk
import re
from nltk.corpus import stopwords  # liste de stopwords de NLTK

nlp = spacy.load("en_core_web_sm")
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')

# test creeDicoFreq
document_list = [
    "18 Editions of the Dewey Decimal Classifications The present study is a history of the DEWEY Decimal Classification. The first edition of the DDC was published in 1876, the eighteenth edition in 1971, and future editions will continue to appear as needed. In spite of the DDC’s long and healthy life, however, its full story has never been told. There have been biographies of Dewey that briefly describe his system, but this is the first attempt to provide a detailed history of the work that more than any other has spurred the growth of librarianship in this country and abroad.",
    "Use Made of Technical Libraries This report is an analysis of 6300 acts of use in 104 technical libraries in the United Kingdom. Library use is only one aspect of the wider pattern of information use.  Information transfer in libraries is restricted to the use of documents.  It takes no account of documents used outside the library, still less of information transferred orally from person to person.  The library acts as a channel in only a proportion of the situations in which information is transferred. Taking technical information transfer as a whole, there is no doubt that this proportion is not the major one.  There are users of technical information - particularly in technology rather than science - who visit libraries rarely if at all, relying on desk collections of handbooks, current periodicals and personal contact with their colleagues and with people in other organizations.  Even regular library users also receive information in other ways."]
test2 = ["There are horses next to this horse. It is sunny.", "Document 2 is here."]

# Ouverture du fichier et séparation en textes
def open_split():
    with open("CISI/DATA/CISI_test.ALLnettoye") as f:
        documents = f.read()
    pattern = r"\.I \d+"
    textes = re.split(pattern, documents) # liste des documents itérable de 1 à 1460
    return textes

def count_doc():
    # pas très optim
    len(open_split())


# Step 1.1) : Tokenisation
#creeDicoFreq : liste des docs dans lesquels apparaît le lemme, liste de tous les dicos des documents
# on part du principe que le textes sont dans une liste de strings
# appelée document_list issue de open_split()
def creeDicoFreq(listeTexte):
    dico_liste = []  # liste pour stocker les dico pour chaque textes
    idoc = 0
    for doc in listeTexte:
        dico_liste.append({})
        docu = nlp(doc)
        lemmes = []
        for w in docu:
            lemmes.append(w.lemma_)
        for le in lemmes:
            # pour les dicos individuels
            if le in dico_liste[idoc].keys():
                dico_liste[idoc][le] += 1
            else:
                dico_liste[idoc][le] = 1
        idoc += 1
    dico_liste = [{w:d[w] for w in d if w not in stopsWords_list} for d in dico_liste] # enlève les stopwords dans chaque dico
    dico_liste = [{w:d[w] for w in d if d[w]<5 } for d in dico_liste] # enlève chaque token de freq>5 dans chaque dico
    return dico_liste



# Step 1.2) : A choice of indexing terms
stopWords = set(stopwords.words('english')) # Liste de stopwords de NLTK en anglais
# Une liste de stopwords trouvées sur internet
stopsWords_list = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]
# Une liste de stopwords trouvés sur internet
stopsWords_list = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
                   "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
                   "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that",
                   "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had",
                   "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as",
                   "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through",
                   "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off",
                   "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how",
                   "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not",
                   "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should",
                   "now", " ", ".", ",", "!", "?", ";", "\n"]


# Step 1.3) : TF IDF

#nombre de lemmes total dans doc (genre 4 si on a 2 fois be et 2 fois love)
def nbLemmesDansDoc(doc):
    res = 0
    dicoDuDoc = liste_de_tous_les_dicos[doc] #donne le dico du document
    for w in dicoDuDoc :
        res+= dicoDuDoc[w] #dicoDuDoc de w contient le nb de fois où le mot apparaît
        #donc la somme à la fin du for nous donne le nombre de lemmes total dans le document
    return res

#nb de documents contenant w
def nbDocContenantW(w):
    res = 0
    for dico in liste_de_tous_les_dicos :
        if w in dico:
            res += 1
    return res

def tfidf(word, doc):
    dicoDuDoc = liste_de_tous_les_dicos[doc]
    return (dicoDuDoc[word]/nbLemmesDansDoc(doc)) * (math.log(nb_doc/nbDocContenantW(word)))

# utilisation de tfidf pour tous les mots de tous les doc
def weighting(ListeDeTousLesDicos):
    '''
    {
        1:
        { "cat" lemme: tfidf(cat, texte1), poids
          "dog": tfidf(dog, texte1),
          ...
        },
        2:
        { "cat": tfidf(cat, texte2),
          "sun": tfidf(sun, texte2),
          ...
        },
        ...
    }
    '''

    poids = {}
    compteur = 1
    for texte in liste_de_tous_les_dicos.keys():
        poids[compteur] = {}
        compteur += 1
        for mot in texte.split(" "):
            poids[texte][mot] = tfidf(mot, texte)
    return poids


# Step 1.4) : Vectors


# Step 1.5) : inverted files

def invertedFiles(vec_doc_liste):
    dico = {}
    idoc = 0
    for l_doc in vec_doc_liste:
        for doublet in l_doc:
            print(doublet)
            print(doublet[0])
            if doublet[0] in dico.keys():
                dico[doublet[0]].append((idoc, doublet[1]))
            else:
                dico[doublet[0]] = [(idoc, doublet[1])]
        idoc += 1
    return dico

# test invertedFiles
vec_doc_liste_test = [[("chat", 1), ("Tomate", 0.5)], [("house", 0.9), ("car", 0.8), ("chat", 0.234)]]
print("inverted-------------------------")
print(invertedFiles(vec_doc_liste_test))
print("---------------------------------")
# fin test invertedFiles



def main():
    # Step 1.1 and 1.2) : Tokenisation and choice of indexing terms
    textes = open_split()
    global liste_de_tous_les_dicos
    liste_de_tous_les_dicos = creeDicoFreq(textes)
    print(liste_de_tous_les_dicos[1])

    # Step 1.3) : TF IDF
    test = nbDocContenantW("Editions")
    ''' Remarque de Léna
    Je ne suis pas sûre que la lemmatisation soit bien passée car par exemple pour le premier doc
    j'ai les mots "Editions" qui apparait une fois et "edition" qui apparait une fois aussi
    alors que la lemmatisation aurait dû faire en sorte que "edition" apparaissent deux fois.
    '''
    print(test)

    # Step 1.4) :




if __name__ == "__main__":
    main()

