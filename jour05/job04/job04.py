n = 10

print("+" + "-" * 11 + "+")
for i in range(n + 1):
    espaces_avant = "|" + "#" * (n - i) + " " + "#" * i
    print(espaces_avant.ljust(11, ' ') + "|")

print("+" + "-" * 11 + "+")
