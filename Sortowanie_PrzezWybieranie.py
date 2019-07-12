import random

def znajdzMinIndeks(lista):
    minimum = lista[0]
    minIndeks = 0
    for i in range(1,len(lista)):
        if minimum > lista[i]:
            minimum = lista[i]
            minIndeks = i
    return minIndeks

def sortowaniePrzezWybieranie(lista):
    for i in range(len(lista)):
        temp = lista[i]
        minIndeks = znajdzMinIndeks(lista[i:len(lista)])+i
        lista[i] = lista[minIndeks]
        lista[minIndeks] = temp
    return lista
            
lista = []
for i in range(10):
    lista.append(random.randint(0,100))

print('Lista przed posortowaniem: ')
print(lista)
print('Lista po posortowaniu: ')
print(sortowaniePrzezWybieranie(lista))

