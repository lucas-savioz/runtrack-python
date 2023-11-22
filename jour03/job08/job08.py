def funct(type, saison):
    if type == "fruit" and saison == "hiver":
        print("orange, mandarine et kiwi")
    elif type == "fruit" and saison == "ete":
        print("Poire, fraise, cassis")
    elif type == "legume" and saison == "hiver":
        print("carotte, topinambour, endive")
    elif type == "legume" and saison == "ete":
        print("artichaut, aubergine, navet")
    
funct("fruit", "hiver")
funct("fruit", "ete")
funct("legume", "hiver")
funct("legume", "ete")