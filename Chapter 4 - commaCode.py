import copy

def commaCode(listeParameter):
    print(listeParameter)

liste = []
print('LIST GENERATOR')
while not '':
    liste += [input('Add an item to your list: ')]
    décision = input('Do you want to add another item? Y/n: ')
    if décision == 'Y' or décision == 'y':
        continue
    elif décision == 'n' or décision == 'N':
        break
    else:
        print('ERROR.')
        break
liste_copie = copy.copy(liste)
liste_copie.insert(-1, 'and')
commaCode(liste_copie)