ma_liste = ["pomme", "cerise", "orange"]

def fruits(liste):

    # Ajoute en fin de liste la var nouv_fruit grace au par .extend
    liste.insert(2, "Mangue")

fruits(ma_liste)
print(ma_liste)