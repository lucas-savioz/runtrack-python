i = 1

while i <= 100:

# modulo "%" pour vérifie si "i" est divisible par 3 et 5 imprime moi "FizzBuzz"
    if i % 3 == 0 and i % 5 == 0: 
        print("FizzBuzz")
# sinon si "i" est divisible par 3 imprime moi "Fizz"
    elif i % 3 == 0:
        print("Fizz")
# sinon si "i" est divisible par 3 imprime moi "Fizz"
    elif i % 5 == 0:
        print("Buzz")
# sinon imprime simplement "i"
    else:
        print(i)

    i += 1  # Incrémente i de 1 à chaque itération de la boucle while
