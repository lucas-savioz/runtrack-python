L = [1, 5, 3, 80, 25, 18, 40]
print(L)

L[0], L[1], L[2], L[3], L[4], L[5], L[6] = L[0], L[2], L[1], L[5], L[4], L[6], L[3]
print(L)



# Sinon ça

# L = [1, 5, 3, 80, 25, 18, 40]
# print(L)

# n = 0
# # "_" c'est les éléments de la liste
# for _ in L: 
#     n += 1

# for i in range(n - 1):
#     for j in range(0, n - i - 1):
#         if L[j] > L[j + 1]:
#             L[j], L[j + 1] = L[j + 1], L[j]

# print(L)
