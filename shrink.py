import re

def main():
    with open("CISI/DATA/CISI.ALLnettoye") as f:
           documents = f.read()
    with open("CISI/DATA/CISI_test2.ALLnettoye", "w") as f:
        compteur = 1
        pattern = r"\.I \d+"
        textes = re.split(pattern, documents)
        for ligne in documents.splitlines():
            if compteur <= 500:
                if re.match(pattern, ligne):
                    f.write("\n")
                    compteur += 1
                f.write(ligne)
                f.write("\n")
                if re.match(pattern, ligne):
                    f.write("\n")
            else:
                
                return 
            

if __name__ == "__main__":
    main()