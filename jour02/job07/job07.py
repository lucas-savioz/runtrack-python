alphabet = "abcdefghijklmnopqrstuvwxyz" * 10 # 5 pour être plus lisible

for i in range(1, len(alphabet) + 1, 2):
    pyramid_row = alphabet[:i]
    print(pyramid_row)