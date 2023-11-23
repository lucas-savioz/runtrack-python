L = [8, 24, 48, 2, 16]

mulipe_de_3 = [n for n in L if n % 3 == 0]

if mulipe_de_3:
    print("Il y a un mutliple de 3")
else:
    print("Il n'y a pas de multiple de 3")