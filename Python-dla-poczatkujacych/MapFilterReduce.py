from functools import reduce

#map dwa argumenty,
#pierwszy inna funkcja
#drugi struktura
#zwraca zmodyfikowana strukture

def kwadrat(lista):
    lista2 = []
    for i in range(len(lista)):
        lista2.append(lista[i]**2)
    return lista2

def kwadracik(x):
    return x**2

lista = [2, 5, 6, 8, 4]
print(lista)
print(kwadrat(lista))
print(list(map(kwadracik,lista)))

#filter dwa argumenty
#pierwszy inna funkcja (zawiera warunek)
#drugi struktura
#zwraca odfiltrowana strukture

def wieksze5(lista):
    lista2 = []
    for i in range(len(lista)):
        if lista[i] > 5:
            lista2.append(lista[i])
    return lista2

def filtr5(x):
    if x > 5:
        return x

print(wieksze5(lista))
print(list(filter(filtr5,lista)))

#reduce dwa argumenty
#pierwszy funkcja ktora zwraca jakis wynik i przyjmuje dwa argumenty
#drugi struktura
#zwraca wynik

def suma(lista):
    suma = 0
    for x in lista:
        suma += x
    return suma

def dodaj(a,b):
    return a+b

print(suma(lista))
print(reduce(dodaj,lista))




    



