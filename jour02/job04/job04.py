n = int(input("Entrez un entier supérieur à zéro (N) :")) # "n" est la table de multiplication choisi
table = 1
while table <= n: # la boucle while imprime n fois le nombre indiqué de la table jusqu'à ce nombre
    print("La table de multiplication de : ", table," est :")
    for i in range(1, 11): # boucle for dans while qui dit de faire la table demandée, de 1 à 10
        print(i , " x ", table, " = ",i*table) # Imprime "i" puis n puis le résultat de i*n
    table +=1