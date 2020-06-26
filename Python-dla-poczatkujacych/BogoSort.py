import random

def bogo_sort(lista):
    licznik = 0
    while not czy_posortowany(lista):
        random.shuffle(lista)
        licznik += 1
    print('Sortowanie odbylo sie ', licznik, ' razy.')

def czy_posortowany(lista):
    for i in range(1,len(lista)):
        if lista[i] < lista[i-1]:
            return False
    return True

lista = []
for i in range(8):
    lista.append(random.randint(0,100))

print('Przed posortowaniem: ')
print(lista)

bogo_sort(lista)
print('Po posortowaniu: ')
print(lista)
