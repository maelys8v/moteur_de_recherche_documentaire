import spacy.cli
from scipy.spatial import distance
import math
import numpy
from collections import Counter

import re
from nltk.corpus import stopwords  # liste de stopwords de NLTK

# pour voir la progression quand on execute
from tqdm import tqdm



nlp = spacy.load("en_core_web_md")


def open_split():
    """Ouverture du fichier et séparation en liste de textes"""
    with open("CISI/DATA/CISI_test2.ALLnettoye") as f:  # "CISI/DATA/CISI_test.ALLnettoye"
        documents = f.read()
    documents = re.sub(r'\r\n|\r|\n', ' ',
                       documents)  # pour remplacer les retours à la ligne / retours chariot par un espace
    documents = re.sub(r'\s+', ' ', documents)  # pour enlever les espaces consécutifs
    pattern = r"\.I \d+"
    textes = re.split(pattern, documents)  # liste des documents itérable de 1 à 1460
    return textes


def count_doc():
    """Compte le nombre de documents"""
    # pas très optim
    return len(open_split())


# Step 1.1) : Tokenisation


from spacy.lang.fr.stop_words import STOP_WORDS as stopWords


def clean_txt(doc):
    """
    Prend une chaîne de caractères, renvoie une liste de lemmes nettoyés (sans stop words, ni ponctuation, etc.)
    """
    doc = nlp(doc)
    lemmes = []
    for token in doc:
        if (
                token.is_alpha and  # que des lettres (pas de ponctuation ni chiffres seuls)
                not token.is_stop and  # pas un stop word
                len(token.lemma_) > 1  # évite les lemmes trop courts ("e", etc.)
        ):
            lemmes.append(token.lemma_.lower())
    return lemmes




def creeDicoFreq(listeTexte):
    """
    listeTexte : liste de chaînes de texte : les textes sont dans une liste de strings issue de open_split()
    Retourne une liste de dictionnaires {lemme : fréquence} pour chaque texte, avec nettoyage.
    """
    dico_liste = []
    for doc in tqdm(listeTexte):
        lemmes = clean_txt(doc)
        dico_freq = dict(Counter(lemmes))  # compte les occurrences automatiquement
        dico_liste.append(dico_freq)

    return dico_liste

"""
def creeDicoFreq(listeTexte):
    
    #listeTexte : les textes sont dans une liste de strings issue de open_split()
    #rend une liste qui contient un dico par texte; clé = lemme ; valeur = freq du lemme dans le texte
    
    dico_liste = []  # liste pour stocker les dicos pour chaque textes
    idoc = 0  # pour savoir quel doc on est en train de traiter
    for doc in tqdm(listeTexte):  # parcourir les différents docs
        dico_liste.append({})  # initialisation des dicos
        docu = nlp(doc)  # lemmatisation du doc
        print(docu)
        lemmes = []  # liste pour stocker tous les lemmes présents dans docu
        for w in docu:  # remplissage de la liste lemmes
            lemmes.append(w.lemma_.lower().__str__())
        print(lemmes)
        for le in lemmes:  # comptage des lemmes
            # pour les dicos individuels
            if le in dico_liste[idoc].keys():
                dico_liste[idoc][le] += 1
            else:
                dico_liste[idoc][le] = 1
        idoc += 1  # on passe au doc suivant
    dico_liste = [{w: d[w] for w in d if w not in stopWords} for d in
                  dico_liste]  # enlève les stopwords dans chaque dico # stopsWords_list
    # dico_liste = [{w: d[w] for w in d if d[w] < 5} for d in dico_liste]  # enlève chaque token de freq>=5 dans chaque dico
    return dico_liste
"""

# Step 1.2) : A choice of indexing terms
stopWords = set(stopwords.words('english'))  # Liste de stopwords de NLTK en anglais

# Une liste de stopwords trouvées sur internet
"""
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
"""


# Step 1.3) : TF IDF
# listeDeTousLesDicos = creeDicoFreq(test2)


def nbLemmesDansDoc(doc, liste_de_tous_les_dicos):
    """rend le nombre de lemmes total dans doc (genre 4 si on a 2 fois be et 2 fois love)"""
    res = 0
    dicoDuDoc = liste_de_tous_les_dicos[doc]  # donne le dico du document
    for w in dicoDuDoc:
        res += dicoDuDoc[w]  # dicoDuDoc de w contient le nb de fois où le mot apparaît
        # donc la somme à la fin du for nous donne le nombre de lemmes total dans le document
    return res

# on s'en sert pas ?
"""
def nbDocContenantW(w, liste_de_tous_les_dicos):
    # rend le nb de documents contenant w (modifs : lemmatisation de w avant de le chercher dans les dicos)
    res = 0
    # w = nlp(w)
    # print(type(w)) # spacy.tokens.doc.Doc
    # lemme = w.lemma_
    # print(type(lemme)) # str
    for dico in liste_de_tous_les_dicos:
        if w in dico:  # if w in dico.keys().__str__():
            # on veut du str et pas du spacy.tokens.doc.Doc
            res += 1

    return res
"""

"""
def tfidf(word, doc, nb_doc, liste_de_tous_les_dicos):
    # application de tfidf sur le document doc avec le mot word
    dicoDuDoc = liste_de_tous_les_dicos[doc]  # dictionnaire correspondant au document doc

    return (dicoDuDoc[word] / nbLemmesDansDoc(doc, liste_de_tous_les_dicos)) * (
        math.log10(nb_doc / nbDocContenantW(word, liste_de_tous_les_dicos)))
"""


def tfidf(word, doc_index, nb_doc, liste_de_tous_les_dicos):
    """
    Calcule le score TF-IDF du mot `word` dans le document d'indice `doc_index`.

    Arguments :
    - word : str, le mot à évaluer
    - doc_index : int, l'indice du document dans `liste_de_tous_les_dicos`
    - nb_doc : int, nombre total de documents
    - liste_de_tous_les_dicos : list[dict], liste de dictionnaires (un par document) contenant les fréquences de mots

    Retour :
    - float : valeur TF-IDF
    """
    dico_doc = liste_de_tous_les_dicos[doc_index]

    freq = dico_doc.get(word, 0)
    if freq == 0:
        return 0.0  # mot absent du document

    nb_lemmes = sum(dico_doc.values())
    nb_docs_avec_word = sum(1 for d in liste_de_tous_les_dicos if word in d)

    if nb_docs_avec_word == 0:
        return 0.0  # pour éviter les divisions par zéro ou log(0)

    tf = freq / nb_lemmes
    # idf = math.log10(nb_doc / nb_docs_avec_word)
    idf = math.log10(1 + nb_doc / (1 + nb_docs_avec_word))

    return tf * idf


def weighting(liste_de_tous_les_dicos, nb_doc):
    """Utilisation de tfidf pour tous les mots de tous les doc"""
    poids = {}
    #  m8d modif
    """
    compteur = 1  # on identifie les textes par leur numéro (commence à 1 -> pb à regler plus tard)
    for i in tqdm(range(0, len(liste_de_tous_les_dicos))):  # m8d j'ai remplacé le 0 par un 1
        dico = liste_de_tous_les_dicos[i]
        poids[compteur] = {}
        for mot in dico.keys():
            # print(mot)
            poids[compteur][mot] = tfidf(mot, compteur, nb_doc, liste_de_tous_les_dicos)
        compteur += 1
    """
    for i in tqdm(range(len(liste_de_tous_les_dicos))):
        dico = liste_de_tous_les_dicos[i]
        poids[i] = {}
        for mot in dico.keys():
            poids[i][mot] = tfidf(mot, i, nb_doc, liste_de_tous_les_dicos)

    return poids


"""
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


# Step 1.4) : Vectors


def vector_representation(dico):
    """
    rend une Liste de listes de Tuple(Terme, Poids) (pour chaque dico on a une liste des tokens avec leur poids associé)
    ex : [[('major', 0.01296918750639406), ('deficiency', 0.02461868757866104), ('traditional', 0.0392030........
    """
    representation_vector = []
    for dic_token in dico:
        sublist = []
        for token in dico[dic_token]:
            sublist.append((token, dico[dic_token][token]))
        representation_vector.append(sublist)
    return representation_vector


# Step 1.5) : inverted files


def invertedFiles(vec_doc_liste):
    """
    pour passer de -> nombre d'apparition d'un terme PAR texte
    à              -> poids du terme dans CHAQUE textes

    Parameters
    ----------
    vec_doc_liste (exemple : = [[("chat", 1), ("Tomate", 0.5)], [("house", 0.9), ("car", 0.8), ("chat", 0.234)]] )

    Returns poids du terme dans CHAQUE textes : {'chat': [(0, 1), (1, 0.234)], 'Tomate': [(0, 0.5)], 'house': [(1, 0.9)], 'car': [(1, 0.8)]}
    -------


    """
    dico = {}
    idoc = 0
    for l_doc in vec_doc_liste:
        for doublet in l_doc:
            # print(doublet)
            # print(doublet[0])
            if doublet[0] in dico.keys():
                dico[doublet[0]].append((idoc, doublet[1]))
            else:
                dico[doublet[0]] = [(idoc, doublet[1])]
        idoc += 1
    return dico


# Step 2.1) : query indexing


def open_split_query():
    """
    Split le document de QRY en une liste de textes (1 par query)

    Returns liste de string contenant les textes
    -------

    """
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

def output_file(ranked_documents):
    """we have a ranked list of tuple(document, similarity) in response to a given query (in a list with index 0 corresponding to the first query)"""
    f = open("test_eval.REL", "w+")
    for i in range(len(ranked_documents)):
        for j in range(len(ranked_documents[i])):
            f.write(str(i + 1) + " " + str(ranked_documents[i][j][0]) + " " + str(ranked_documents[i][j][1]) + "\n")


def similarity_measurement(dico_w_lemmesParTexte, l_w_qry, nbDoc):
    """
    Pour comparer les vecteurs des queries et des textes > mettre les rst dans un dico > dans une liste triée

    Parameters
    ----------
    dico_w_lemmesParTexte   le dictionnaire sorti de inverted_files(dico_w_lemmesParTexte)
    l_w_qry   une liste de Tuples(Terme, Poids) correspondant à la query l_w_qry
    nbDoc   nb de documents à comparer avec la query

    Returns   les docs pertinents avec la similarité correspondante sous forme de liste de tuples
    -------
    """
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
                poidsDoc[j].append(0)  # m8d j'ai remplacé le 1 par un 0
            for doublet in poids:
                poidsDoc[doublet[0]][-1] = doublet[1]  # ajouter dans le vecteur du doc, le poids correspondant
            nbMots += 1

    #  calcul de la similarité

    wQuery = numpy.array(poidsQuery)
    for i in range(nbDoc):
        wDoc = numpy.array(poidsDoc[i])
        # print(i)
        # print(poidsDoc[i])
        # print(wDoc)
        # similarity.append(-1 * distance.euclidean(wDoc, wQuery))
        if numpy.linalg.norm(wDoc) == 0 or numpy.linalg.norm(wQuery) == 0:
            similarity.append(0.0)
        else:
            sim = 1 - distance.cosine(wDoc, wQuery)
            similarity.append(sim)

    # print("simiilarity ----------------------------------------------------------")
    # print(similarity)
    #  tri des similarités pour trouver les documents les plus pertinents
    for i in range(nbDoc//10):
        maxi = max(similarity)
        imax = similarity.index(maxi)
        rst.append((imax, maxi))
        similarity[imax] = -1 * math.inf # pour pas mettre 2 fois le meme indice
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
    print(len(textes))
    print("1")  # time
    # global liste_de_tous_les_dicos # avec les fréquences
    # global nb_doc
    nb_docs = len(textes)  # 11 sur CISI_test
    liste_tous_les_dicos = creeDicoFreq(textes)
    print("2")  # time
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
    print("3")  # time
    # Step 1.4) : production of a representation vector for each document
    vector = vector_representation(poids)
    print("4")  # time

    # Step 1.5) : production of inverted files for our system
    inverted = invertedFiles(vector)
    print("5")  # time

    # Step 2.1) : indexing queries
    queries = open_split_query()
    nb_query = len(queries)
    liste_de_tous_les_dicos_query = creeDicoFreq(queries)
    print("6")  # time
    poids_query = weighting(liste_de_tous_les_dicos_query, nb_query)
    vector_query = vector_representation(poids_query)
    print("7")  # time
    # print("- - - vector_query - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
    # print(vector_query)  # liste de listes avec pour chaque query, les poids

    testSim = similarity_measurement(inverted, vector_query[0], nb_docs)
    print("8")  # time
    # print("- - - testSim    -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  - - - - - - - - - - - - ")
    print(testSim)

    # rendre propre -----------------------------------------------------------------------------------------------
    testEval = []
    for i in tqdm(range(len(vector_query))):
        testEval.append(similarity_measurement(inverted, vector_query[i], nb_docs))

    output_file(testEval)
    # -----------------------------------------------------------------------------------------------


if __name__ == "__main__":
    main()
