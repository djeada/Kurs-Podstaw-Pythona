# listy to kolekcje elementow, ktore moga byc dowolnego typu

liczby = [1, 2, 3, 4, 5]
print(liczby)

for liczba in liczby:
    print(liczba)

napisy = ["Ala", "ma", "kota"]
print(napisy)

for napis in napisy:
    print(napis)

# listy moga mieszac typy
lista = [1, 2, 3, "Ala", "ma", "kota", ["lista", "w", "liscie"]]
print(lista)

# listy sa mutowalne
lista = [1, 2, 3]
lista[0] = -5
print(lista)

# sumowanie elementow listy
suma = 0
for element in lista:
    suma += element
print(suma)

# dlugosc listy
print(len(lista))

# sprawdzanie czy element jest w liscie
print(1 in lista)

# zliczanie wystapien elementu w liscie
print([1, 1, 2, 1].count(1))

# rozszerzanie listy o nowy element
lista = [1, 2, 3]
lista.append(4)
print(lista)

lista.insert(0, 0)
print(lista)

# laczenie list
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista3 = lista1 + lista2
print(lista3)

# usuwanie elementow z listy
lista = [1, 2, 3, 4, 5]
lista.pop()

# usuwanie elementu o danym indeksie
lista.pop(0)

# usuwanie elementu o danej wartosci
lista.remove(3)

# operowanie na indeksach (slicing)
lista = [1, 2, 3, 4, 5]
print(lista[0])
print(lista[-1])
print(lista[1:3])
print(lista[:3])
print(lista[3:])
