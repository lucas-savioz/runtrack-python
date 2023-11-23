ma_liste = ["pomme", "cerise", "orange"]

def fruits(liste):

    nouv_fruit = ["Melon"]
    # Ajoute en fin de liste la var nouv_fruit grace au par .extend
    liste.extend(nouv_fruit)

fruits(ma_liste)
print(ma_liste)