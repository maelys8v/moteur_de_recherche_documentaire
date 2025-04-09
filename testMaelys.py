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
