# slowniki maja klucze i wartosci
# klucze moga byc roznych typow, ale musza byc niemutowalne
# wartosci moga byc dowolnego typu

slownik = {"klucz": "wartosc", 1: 2, 3: 4}
print(slownik)

# pobieranie wartosci z slownika
print(slownik["klucz"])

# dodawanie nowych elementow do slownika
slownik["nowy klucz"] = "nowa wartosc"

# usuwanie elementow z slownika
del slownik["klucz"]

# sprawdzanie czy klucz jest w slowniku
print("klucz" in slownik)

# sprawdzanie czy wartosc jest w slowniku
print("wartosc" in slownik.values())

# iterowanie po kluczach
for klucz in slownik:
    print(klucz)

# iterowanie po kluczach i wartosciach
for klucz, wartosc in slownik.items():
    print(klucz, wartosc)

# sortowanie slownika po kluczach
slownik = {"c": 3, "a": 1, "b": 2}
print(sorted(slownik.items()))

# sortowanie slownika po wartosciach
print(sorted(slownik.items(), key=lambda x: x[1]))

# generowanie slownika z listy
lista = ["a", "b", "c"]
slownik = {element: element.upper() for element in lista}
print(slownik)

# konwertowanie dwoch list na slownik
klucze = ["a", "b", "c"]
wartosci = [1, 2, 3]
slownik = dict(zip(klucze, wartosci))
print(slownik)
