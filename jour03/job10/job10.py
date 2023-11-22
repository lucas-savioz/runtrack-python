def funct(nombre):
    if isinstance(nombre, int) and nombre >= 0:
        if nombre % 2 == 0:
            print(nombre, " : est un nombre pair")
        else:
            print(nombre, " : est un nombre impair")
    else:
        print("Veuillez entrer un nombre entier positif")

# Appel de la fonction avec différentes valeurs
funct(8)
funct(43)
funct(76)
funct(15)
funct(0)
funct("BLABLA")
