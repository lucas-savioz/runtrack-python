# Dans ce cas là la fonction peut prendre qu'un seul paramètre
def funct(nombre):

    if nombre >= 0 :
        print(nombre, " = positif")
    elif nombre < 0 :
        print(nombre, " = negatif")

# Car la funct de fin à qu'un seul paramètre, 
funct(-5)



# OU 
# Pour x nombre

# def funct(*nombres):
#     for nombre in nombres:
#         if nombre >= 0 :
#             print(nombre, " = positif")
#         elif nombre < 0 :
#             print(nombre, " = negatif")

# funct(0, 5, -10)