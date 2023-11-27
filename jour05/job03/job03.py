
size = int(input('Entrez un nombre de lignes : '))

for i in range(size):
    spaces_before = ' ' * (size - i - 1)
    if i == size - 1:
        print(spaces_before + '/' + '_' * (2 * i) + '\\')
    else:
        spaces_inside = ' ' * (2 * (size - i - 1))
        print(spaces_before + '/' + ' ' * (2 * i) + '\\' + spaces_inside)
