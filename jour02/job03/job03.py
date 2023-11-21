excluded_numbers = [26, 37, 88] # exclusion des numéros

i = 0
while i <= 100: # Tant que i n'est pas <= 100 
    if i not in excluded_numbers: # Dans la boucle while, si i n'est pas dans la liste, cela exécute excluded_numbers
        print(i, end=" ")  # Imprime i
    i += 1  # Incrémente i de 1