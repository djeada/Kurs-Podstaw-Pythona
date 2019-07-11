import random

#funkcja do wyswietlania listy 2D
def print2D(lista):
    for i in range(len(lista)):
        for j in range(len(lista)):
            print(lista[i][j], end=', ')
        print('')

#przyklad listy2D wpisanej na sztywno
lista2D = [[1,2,3,4],[1,5,7],[2,9,100]]

#jak odniesc sie do konkretnego elementu
print(lista2D[1][1])
lista2D[1][2] = 'tunczyk'

#wypisujemy cala liste
print2D(lista2D)

#dwuwymiarowa lista skladajaca sie z losowych liczb z przedzialu od 0 do 10
lista1D = []
lista2D.clear()

for j in range(10):
    for i in range(10):
        lista1D.append(random.randint(0,100))
    lista2D.append(lista1D)
    lista1D = []
    
print2D(lista2D)

#tabliczka mnozenia
tabliczka = []
rzad = []

for i in range(1,11):
    for j in range(1,11):
        rzad.append(i*j)
    tabliczka.append(rzad)
    rzad = []

print2D(tabliczka)



        





