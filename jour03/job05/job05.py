# Définir la fonction est ses paramètres
def calcule(num1, operator, num2):
    # Conditions
    # Si operator est strictement égale à '+'
    if operator == '+':
        # alors result égale à num1 + num2
        result = num1 + num2
        # Sinon si operator est strictement égale à '-'
    elif operator == '-':
        # alors result égale à num1 + num2
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        result = num1 / num2
    elif operator == '%':
        result = num1 % num2
    
    # Imprime le contenu de la f string qui formate l'ensemble des variables
    print(f"{num1} {operator} {num2} = {result}")

# Affiche l'ensemble des calculs de la fonction calcule et de ses paramètres
calcule(2, '+', 5)
calcule(2, '-', 5)
calcule(2, '*', 5)
calcule(2, '/', 5)
calcule(2, '%', 5)