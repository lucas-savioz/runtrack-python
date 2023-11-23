L = [8, 24, 47, 15, 16]

valeur_pair = [n for n in L if n % 2 == 0]

if valeur_pair:
    print("Il y au moins une valeur pair")
else:
    print("Il n'y a pas de valeur pair")