def sortowanie_babelkowe(lista):
    for i in range(len(lista)):
        for j in range(len(lista)-1-i):
            if lista[j] > lista[j+1]:
                swap(lista[j],lista[j+1])
        printList(lista)

def swap(a,b):
    temp = a
    a = b
    b = temp

def printList(lista):
    for x in lista:
        print(x, end=', ')
    print('')

lista = [1, 2, 3, 4, 5, 6, 7, 10, 9]

printList(lista)
sortowanie_babelkowe(lista)
