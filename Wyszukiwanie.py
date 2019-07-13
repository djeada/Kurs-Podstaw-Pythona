import random

def wyszukiwanie_liniowe(lista, x):
    for i in range(len(lista)):
        if lista[i] == x:
            return i
    return -1

def wyszukiwanie_binarne(lista, x):
    l = 0
    r = len(lista)

    while l <= r:
        mid = l + int((r-l)/2)

        if lista[mid] == x:
            return mid
        
        elif lista[mid] < x:
            l = mid + 1
            
        else:
            r = mid - 1
    return -1
            

lista = [4, 15, 18, 20, 24, 30, 34]

print('Wyszukiwanie liniowe:')
print(wyszukiwanie_liniowe(lista, 30))
print(wyszukiwanie_liniowe(lista, 2))
print('')
print('Wyszukiwanie binarne:')
print(wyszukiwanie_binarne(lista, 30))
print(wyszukiwanie_binarne(lista, 2))

