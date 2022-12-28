# zbiory to kolekcje unikalnych elementow
# zbiory sa nieuporzadkowane

zbior = {1, 2, 3, 4, 5}
print(zbior)

zbior.add(1)
print(zbior)

zbior.add(6)
print(zbior)

zbior.remove(6)
print(zbior)

# dlugosc zbioru
print(len(zbior))

# sprawdzanie czy element jest w zbiorze
print(1 in zbior)

# czesc wspolna zbiorow
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}
print(a & b)
print(a.intersection(b))

# suma zbiorow
print(a | b)
print(a.union(b))

# roznica zbiorow
print(a - b)
print(a.difference(b))

# roznica symetryczna
print(a ^ b)
print(a.symmetric_difference(b))

# sprawdzanie czy zbior jest podzbiorem innego zbioru
print(a <= b)
print(a.issubset(b))

print({1, 2} <= {1, 2, 3})
print({1, 2}.issubset({1, 2, 3}))

# sprawdzanie czy zbior jest nadzbiorem innego zbioru
print({1, 2, 3} >= {1, 2})
print({1, 2, 3}.issuperset({1, 2}))

# unikalne elementy listy
lista = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
print(set(lista))

# znajdz duplikaty w liscie
lista = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
unikalne = set(lista)
duplikaty = set()

for element in lista:
    if element not in unikalne:
        duplikaty.add(element)

print(duplikaty)
