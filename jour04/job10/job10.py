# L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]

# select = L[25:90]


# print(select)


L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]
produit = 1

for valeur in L[25:91]:
    produit *= valeur

print("Le produit des valeurs de la liste comprises dans l'intervalle [25, 90] est :", produit)
