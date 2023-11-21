for n in range(2, 1001):
    nombre_premier = True
    # parcourt les nombres de 2 à la racine carrée de n
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            nombre_premier = False
            # si la variable et fausse interruption de la boucle
            break
    if nombre_premier:
        # Imprime le resultat suivi d'un espace 
        print(n, end=" ")
