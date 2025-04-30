import spacy.cli
from scipy.spatial import distance
import math
import numpy

from nltk import word_tokenize

# spacy.cli.download("en_core_web_md") # Load English tokenizer in middle size because the texts are in english
nlp = spacy.load("en_core_web_md")

import nltk
import re
from nltk.corpus import stopwords  # liste de stopwords de NLTK
# nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer

nlp = spacy.load("en_core_web_md")
# nltk.download('punkt')
# nltk.download('punkt_tab')
# nltk.download('stopwords')

# test creeDicoFreq
document_list = [
    "18 Editions of the Dewey Decimal Classifications The present study is a history of the DEWEY Decimal Classification. The first edition of the DDC was published in 1876, the eighteenth edition in 1971, and future editions will continue to appear as needed. In spite of the DDC’s long and healthy life, however, its full story has never been told. There have been biographies of Dewey that briefly describe his system, but this is the first attempt to provide a detailed history of the work that more than any other has spurred the growth of librarianship in this country and abroad.",
    "Use Made of Technical Libraries This report is an analysis of 6300 acts of use in 104 technical libraries in the United Kingdom. Library use is only one aspect of the wider pattern of information use.  Information transfer in libraries is restricted to the use of documents.  It takes no account of documents used outside the library, still less of information transferred orally from person to person.  The library acts as a channel in only a proportion of the situations in which information is transferred. Taking technical information transfer as a whole, there is no doubt that this proportion is not the major one.  There are users of technical information - particularly in technology rather than science - who visit libraries rarely if at all, relying on desk collections of handbooks, current periodicals and personal contact with their colleagues and with people in other organizations.  Even regular library users also receive information in other ways."]
test2 = ["There are horses next to this horse. It is sunny.", "Document 2 is here."]

"""
# Ouverture du fichier et séparation en textes
"""


def open_split():
    with open("CISI/DATA/CISI_test.ALLnettoye") as f:
        documents = f.read()
    documents = re.sub(r'\r\n|\r|\n', ' ',
                       documents)  # pour remplacer les retours à la ligne / retours chariot par un espace
    documents = re.sub(r'\s+', ' ', documents)  # pour enlever les espaces consécutifs
    pattern = r"\.I \d+"
    textes = re.split(pattern, documents)  # liste des documents itérable de 1 à 1460
    return textes


"""
compte le nombre de documents
"""


def count_doc():
    # pas très optim
    return len(open_split())


# Step 1.1) : Tokenisation
"""
creeDicoFreq : liste des docs dans lesquels apparaît le lemme, liste de tous les dicos des documents
on part du principe que les textes sont dans une liste de strings
appelée document_list issue de open_split()
"""


def creeDicoFreq(listeTexte):
    dico_liste = []  # liste pour stocker les dicos pour chaque textes
    idoc = 0  # pour savoir quel doc on est en train de traiter
    for doc in listeTexte:  # parcourir les différents docs
        dico_liste.append({})
        docu = nlp(doc)  # lemmatisation du doc
        lemmes = []  # liste pour stocker tous les lemmes présents dans docu
        for w in docu:  # remplissage de la liste lemmes
            lemmes.append(w.lemma_.lower().__str__())
        for le in lemmes:  # comptage des lemmes
            # pour les dicos individuels
            if le in dico_liste[idoc].keys():
                dico_liste[idoc][le] += 1
            else:
                dico_liste[idoc][le] = 1
        idoc += 1  # on passe au doc suivant
    dico_liste = [{w: d[w] for w in d if w not in stopsWords_list} for d in
                  dico_liste]  # enlève les stopwords dans chaque dico
    dico_liste = [{w: d[w] for w in d if d[w] < 5} for d in
                  dico_liste]  # enlève chaque token de freq>=5 dans chaque dico
    return dico_liste


# Step 1.2) : A choice of indexing terms
stopWords = set(stopwords.words('english'))  # Liste de stopwords de NLTK en anglais
# Une liste de stopwords trouvées sur internet
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
                   "now"]
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
                   "now", " ", ".", ",", "!", "?", ";", "'s", "-", "(", ")", "[", "]", ":", "\"", "'", "--"]

# Step 1.3) : TF IDF
listeDeTousLesDicos = creeDicoFreq(test2)

"""
nombre de lemmes total dans doc (genre 4 si on a 2 fois be et 2 fois love)
"""


def nbLemmesDansDoc(doc, liste_de_tous_les_dicos):
    res = 0
    dicoDuDoc = liste_de_tous_les_dicos[doc]  # donne le dico du document
    for w in dicoDuDoc:
        res += dicoDuDoc[w]  # dicoDuDoc de w contient le nb de fois où le mot apparaît
        # donc la somme à la fin du for nous donne le nombre de lemmes total dans le document
    return res


"""
nb de documents contenant w
modifs : lemmatisation de w avant de le chercher dans les dicos
"""


def nbDocContenantW(w, liste_de_tous_les_dicos):
    res = 0
    #w = nlp(w)
    # print(type(w)) # spacy.tokens.doc.Doc
    #lemme = w.lemma_
    # print(type(lemme)) # str
    for dico in liste_de_tous_les_dicos:
        if w in dico.keys().__str__():
            # on veut du str et pas du spacy.tokens.doc.Doc
            res += 1

    return res


"""
application de tfidf sur le document doc avec le mot word
"""


def tfidf(word, doc, nb_doc, liste_de_tous_les_dicos):
    dicoDuDoc = liste_de_tous_les_dicos[doc]  # dictionnaire correspondant au document doc

    return (dicoDuDoc[word] / nbLemmesDansDoc(doc, liste_de_tous_les_dicos)) * (
        math.log10(nb_doc / nbDocContenantW(word, liste_de_tous_les_dicos)))


"""
utilisation de tfidf pour tous les mots de tous les doc
exemple :

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
"""


def weighting(liste_de_tous_les_dicos, nb_doc):
    poids = {}
    compteur = 1  # on identifie les textes par leur numéro (commence à 1 -> pb à regler plus tard)
    for i in range(1, len(liste_de_tous_les_dicos)):
        dico = liste_de_tous_les_dicos[i]
        poids[compteur] = {}
        for mot in dico.keys():
            # print(mot)
            poids[compteur][mot] = tfidf(mot, compteur, nb_doc, liste_de_tous_les_dicos)
        compteur += 1
    return poids


# Step 1.4) : Vectors
"""
rend une Liste de listes de Tuple(Terme, Poids) (pour chaque dico on a une liste des tokens avec leur poids associé)
ex : [[('major', 0.01296918750639406), ('deficiency', 0.02461868757866104), ('traditional', 0.0392030........
"""


def vector_representation(dico):
    representation_vector = []
    for dic_token in dico:
        sublist = []
        for token in dico[dic_token]:
            sublist.append((token, dico[dic_token][token]))
        representation_vector.append(sublist)
    return representation_vector


# Step 1.5) : inverted files


"""
pour passer de -> nombre d'apparition d'un terme PAR texte
à              -> poids du terme dans CHAQUE text

exemple : 
vec_doc_liste_test = [[("chat", 1), ("Tomate", 0.5)], [("house", 0.9), ("car", 0.8), ("chat", 0.234)]]
invertedFiles(vec_doc_liste_test)) 
>>> {'chat': [(0, 1), (1, 0.234)], 'Tomate': [(0, 0.5)], 'house': [(1, 0.9)], 'car': [(1, 0.8)]}
"""


def invertedFiles(vec_doc_liste):
    dico = {}
    idoc = 0
    for l_doc in vec_doc_liste:
        for doublet in l_doc:
            #print(doublet)
            #print(doublet[0])
            if doublet[0] in dico.keys():
                dico[doublet[0]].append((idoc, doublet[1]))
            else:
                dico[doublet[0]] = [(idoc, doublet[1])]
        idoc += 1
    return dico


# test invertedFiles
#  vec_doc_liste_test = [[("chat", 1), ("Tomate", 0.5)], [("house", 0.9), ("car", 0.8), ("chat", 0.234)]]
#  print("inverted-------------------------")
#  print(invertedFiles(vec_doc_liste_test))
#  print("---------------------------------")
# fin test invertedFiles

# Step 2.1) : query indexing
"""
Split le document de QRY en une liste de textes (1 par query)
"""


def open_split_query():
    with open("CISI/DATA/CISI_dev.QRY") as f:
        documents = f.read()
    documents = re.sub(r'\r\n|\r|\n', ' ',
                       documents)  # pour remplacer les retours à la ligne / retours chariot par un espace
    documents = re.sub(r'\s+', ' ', documents)  # pour enlever les espaces consécutifs
    pattern = r"\.I \d+"
    raw_queries = re.split(pattern, documents)  # liste des requêtes avec .T,.A et .B qu'il faut enlever
    queries = []  # liste des requêtes avec le champ W. seulement
    for q in raw_queries:
        match = re.search(r".W\s+(.*?)(?:\s+\.[A-Z]\s|$)", q, re.DOTALL)
        if match:
            queries.append(match.group(1).strip())
    return queries

# Step 3) producing the .REL file for evaluation
# we have a ranked list of tuple(document, similarity) in response to a given query (in a list with index 0 corresponding to the first query)
def output_file(ranked_documents):
    f=open("test_eval.REL","w+")
    for i in range(len(ranked_documents)):
        for j in range(len(ranked_documents[i])):
            f.write(str(i+1)+" "+str(ranked_documents[i][j][0])+" "+str(ranked_documents[i][j][1])+"\n")



"""
pour comparer les vecteurs des queries et des textes > mettre les rst dans un dico > dans une liste triée
prend en paramètres : 
- le dictionnaire sorti de inverted files dico_w_lemmesParTexte
- une liste de Tuples(Terme, Poids) correspondant à la query l_w_qry
- nbDoc : nb de documents à comparer avec la query

renvoit les docs pertinents avec la similarité correspondante sous forme de liste de tuples
"""


def similarity_measurement(dico_w_lemmesParTexte, l_w_qry, nbDoc):
    similarity = []  # liste qui contient la similarité entre la query et le texte i
    poidsDoc = []  # pour chaque texte i, un vecteur avec les poids des mots de la query
    poidsQuery = []  # vecteur avec les poids des mots de la query
    nbMots = 0  # combien de mots on a stocké
    rst = []  # liste qui contiendra le résultat

    #  initialisation de poidsDoc avec les listes qui contiendront les vecteurs
    for i in range(nbDoc):
        poidsDoc.append([])
    #  remplissage des listes de poidsDoc et du vecteur poidsQuery
    for tupleW in l_w_qry:
        if tupleW[0] in dico_w_lemmesParTexte.keys():
            poidsQuery.append(tupleW[1])
            poids = dico_w_lemmesParTexte[tupleW[0]]
            for j in range(nbDoc):
                poidsDoc[j].append(1)
            for doublet in poids:
                poidsDoc[doublet[0]][-1] = doublet[1]  # ajouter dans le vecteur du doc, le poids correspondant
            nbMots += 1

    #  calcul de la similarité
    wQuery = numpy.array(poidsQuery)
    for i in range(nbDoc):
        wDoc = numpy.array(poidsDoc[i])
        print(i)
        print(poidsDoc[i])
        print(wDoc)
        similarity.append(-1 * distance.euclidean(wDoc, wQuery))
    print("simiilarity ----------------------------------------------------------")
    print(similarity)
    #  tri des similarités pour trouver les documents les plus pertinents
    for i in range(nbDoc):
        maxi = max(similarity)
        imax = similarity.index(maxi)
        rst.append((imax, maxi))
        similarity[imax] = -1 * math.inf
    return rst


# rst de inverted files docs : >>> {'chat': [(0, 1), (1, 0.234)], 'Tomate': [(0, 0.5)], 'house': [(1, 0.9)], 'car': [(1, 0.8)]}
# rst de :    [[('major', 0.01296918750639406), ('deficiency', 0.02461868757866104),
# queries = open_split_query()
#    nb_query = len(queries)
#    liste_de_tous_les_dicos_query = creeDicoFreq(queries)
#    poids_query = weighting(liste_de_tous_les_dicos_query, nb_query)
#    vector_query = vector_representation(poids_query)


def main():
    # Step 1.1 and 1.2) : Tokenisation and choice of indexing terms
    textes = open_split()
    # global liste_de_tous_les_dicos # avec les fréquences
    # global nb_doc
    nb_docs = len(textes)  # 11 sur CISI_test
    liste_tous_les_dicos = creeDicoFreq(textes)
    # print("Premier texte : ")
    # print(textes[1])
    # print("Premier dictionnaire : ")
    # print(liste_de_tous_les_dicos[1])

    # Step 1.3) : TF IDF
    ''' Test de tf idf sur le lemme "need" dans le premier doc sur CISI_test
    mon_doc = 1
    mot = "need"
    print("Nombre de documents contenant le lemme  ", mot, " : ", nbDocContenantW(mot)) # 5
    print("Nombre de lemme dans mon_doc :", nbLemmesDansDoc(mon_doc)) # 51
    print("tfidf de ", mot, " : ", tfidf(mot, mon_doc)) # 0.006 c'est bon
    '''
    poids = weighting(liste_tous_les_dicos, nb_docs)

    # Step 1.4) : production of a representation vector for each document
    vector = vector_representation(poids)

    # Step 1.5) : production of inverted files for our system
    inverted = invertedFiles(vector)

    # Step 2.1) : indexing queries
    queries = open_split_query()
    nb_query = len(queries)
    liste_de_tous_les_dicos_query = creeDicoFreq(queries)
    poids_query = weighting(liste_de_tous_les_dicos_query, nb_query)
    vector_query = vector_representation(poids_query)
    #print("- - - vector_query - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
    #print(vector_query)  # liste de listes avec pour chaque query, les poids

    testSim = similarity_measurement(inverted, vector_query[0], nb_docs)
    print("- - - testSim    -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  - - - - - - - - - - - - ")
    print(testSim)


if __name__ == "__main__":
    main()
