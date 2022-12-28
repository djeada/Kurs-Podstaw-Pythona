# tworzenie listy przy pomocy petli for
lista = []
for i in range(10):
    lista.append(i)

print(lista)

# tworzenie listy przy pomocy wyrazenia listowego
lista = [i for i in range(10)]
print(lista)

# tworzenie listy z warunkiem
lista = [i for i in range(10) if i % 2 == 0]
print(lista)

# tworzenie listy przy pomocy funkcji
def kwadrat(x):
    return x ** 2


lista = [kwadrat(i) for i in range(10)]
print(lista)

# filtrowanie elementow listy
lista = ["adam", "ewa", "kasia", "tomek", "jan", "grzegorz"]
nowa_lista = [imie for imie in lista if len(imie) > 3]
print(nowa_lista)

# wyrazenie listowe w funkcji
def wieksze_niz_n(lista, n):
    return [element for element in lista if element > n]


print(wieksze_niz_n([1, 2, 3, 4, 5], 3))
