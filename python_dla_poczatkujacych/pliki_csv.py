import csv

pola = []
wiersze = []

# otwieramy do odczytu
with open("Zeszyt.csv") as plikCSV:
    czytnikCSV = csv.reader(plikCSV, delimiter=";")

    # wczytujemy naglowki
    pola = next(czytnikCSV)

    # wzytujemy dane
    wiersze = [wiersz for wiersz in czytnikCSV]

    print(pola)
    print(wiersze[0])

    # liczymy srednia
    suma = 0
    for wiersz in wiersze:
        suma += float(wiersz[2])
    srednia = suma / len(wiersze)
    print("%.2f" % srednia)

    """for wiersz in czytnikCSV:
        print(wiersz)"""

# tworzymy plik
with open("Zeszyt2.csv", mode="w") as plikCSV:
    pola = ["pracownik", "stanowisko", "pensja"]
    lista = [
        {"pracownik": "Jan", "stanowisko": "biegacz", "pensja": "1000"},
        {"pracownik": "Brokul", "stanowisko": "dietetyk", "pensja": "3000"},
        {"pracownik": "James", "stanowisko": "dyrektor", "pensja": "20"},
    ]

    writer = csv.DictWriter(plikCSV, fieldnames=pola)

    writer.writeheader()
    for x in lista:
        writer.writerow(x)

# sprawdzamy czy plik zostal stworzony poprawnie
with open("Zeszyt2.csv") as plikCSV:
    czytnikCSV = csv.reader(plikCSV, delimiter=";")

    wiersze = [wiersz for wiersz in czytnikCSV if wiersz]
    print(wiersze)
