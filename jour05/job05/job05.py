alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] 

# message = str(input("Entrer votre message : "))
# print(message)

# if message 

# message = "bad"

# crypted_message = "t"

# resultant_message = message.replace("d", crypted_message)

# print(resultant_message)

for x in range(len(alphabet)):
    alphabet.append(alphabet[x])

message = input("Entrer votre message : ")
decalage = 3

def message_clear(lettre, alphabet, decalage):
    for i in range(len(alphabet)):
        if lettre == ' ':
            return ' '
        elif alphabet[i]==lettre:
            return str(alphabet[i+decalage])

message_crypte = str()

for lettre in message: 
    message_crypte += message_clear(lettre, alphabet, decalage)
print(message_crypte)