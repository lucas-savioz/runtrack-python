alphabet = "abcdefghijklmnopqrstuvwxyz"

for i in range(1, len(alphabet) + 1, 2):
    pyramid_row = alphabet[:i]
    print(pyramid_row)