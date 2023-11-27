nombre_marche = int(input("Saisir un nombre de marches : "))
hauteur_marche = 20

def distance_gardien(nb_marche, h_marche):
    print("{} marches de {} cm. La distance qu'il devra parcourir par semaine est de {:.2f} m.".format(nb_marche, h_marche, nb_marche*h_marche*2*5*7/100.0))
distance_gardien(nombre_marche, hauteur_marche)