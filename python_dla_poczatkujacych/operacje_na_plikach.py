# proste otwarcie i zamkniecie pliku
plik = open("plik.txt")
print(plik.name)
print(plik.mode)
print(plik.read())
plik.close

# otwarcie i zamkniecie pliku przy uzyciu bloku with
with open("plik.txt") as plik:
    print(plik.name)
    print(plik.mode)
    print(plik.read())

# wczytanie konretnych porcji z pliku, dane beda pobierane po 20 znakow przy uzyciu bloku with
with open("plik.txt") as plik:
    rozmiar = 20
    tresc = plik.read(rozmiar)

    while len(tresc) > 0:
        print(tresc, end="*")
        tresc = plik.read(rozmiar)

# zliczenie liczby wierszy w pliku
with open("plik.txt") as plik:
    print("Liczba wierszy: ", len(plik.readlines()))

# zliczenie liczby slow w pliku
wiersze = []
with open("plik.txt") as plik:
    for linia in plik:
        wiersze.append(plik.readline().split())

    liczba_slow = 0
    for wiersz in wiersze:
        liczba_slow += len(wiersz)

    print("Liczba slow: ", liczba_slow)


# modyfikacja plikow
lista = ["czesc", "test", "lol", "tunczyk"]

with open("test.txt", "w") as plik:
    for napis in lista:
        print(napis, file=plik)

# dopisywanie do pliku
with open("test.txt", "a") as plik:
    print("dopisane", file=plik)
