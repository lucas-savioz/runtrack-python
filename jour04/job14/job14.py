def my_long_word(chiffre, chaine):
    mots_plus_longs = []
    mots = chaine.split()
    
    for mot in mots:
        if len(mot) > chiffre:
            mots_plus_longs.append(mot)
    
    return mots_plus_longs

resultat = my_long_word(2, "T'aider, je puis. Personne par la guerre ne devient grand. Toujours en mouvement est l'avenir. Luke, quand je ne serai plus, le dernier des Jedi tu seras…")
print(resultat)

resultat = my_long_word(3, "T'aider, je puis. Personne par la guerre ne devient grand. Toujours en mouvement est l'avenir. Luke, quand je ne serai plus, le dernier des Jedi tu seras…")
print(resultat)