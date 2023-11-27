def print_rectangle(height, width):
    # Commence une boucle 'for' qui itère de 1 à 'height' inclus
    for i in range(1, height + 1):
        # Commence une boucle 'for' imbriquée qui itère de 1 à 'width' inclus
        for j in range(1, width + 1):
            # Vérifie si l'on est sur une bordure du rectangle.
            if i == 1 or i == height or j == 1 or j == width:
                # Si c'est une bordure verticale (première ou dernière colonne), imprime "|", sinon imprime "-"
                print("|" if j == 1 or j == width else "-", end="")
            else:
                # Si ce n'est pas une bordure, imprime un espace
                print(" ", end="")
        print()

height = 6
width = 20

print_rectangle(height, width)


