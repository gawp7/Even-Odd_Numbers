print ("Entre ta valeur et je vais deviner si elle est PAIR ou IMPAIR")
nombre = int(input("Entrez la valeur :"))
longueur = len(str(abs(nombre))) > 1
calcul = (nombre % 2 == 0)

if nombre % 2 == 0 : 
    nb = ("PAIR")
else : 
    nb = ("IMPAIR")

if longueur < 1 : 
    print("Votre chiffre est",nb)
else : 
    print("Votre nombre est",nb)
    