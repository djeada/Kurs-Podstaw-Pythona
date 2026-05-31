"""
Modul demonstracyjny: Listy w Pythonie.

Omawiane zagadnienia:
- Tworzenie list
- Indeksowanie i wycinki (slicing)
- Modyfikowanie list (append, insert, extend, remove, pop)
- Iterowanie po listach
- Operacje na listach (sortowanie, odwracanie, kopiowanie)
- Listy zagniezdzone
- Przydatne funkcje wbudowane (len, sum, min, max, enumerate, zip)
- Rozpakowywanie list
"""

# =============================================================================
# 1. Tworzenie list
# =============================================================================

# Listy moga przechowywac elementy dowolnego typu
liczby = [1, 2, 3, 4, 5]
napisy = ["Ala", "ma", "kota"]
mieszana = [1, "dwa", 3.0, True, None, [5, 6]]

print("=== Tworzenie list ===")
print(f"liczby = {liczby}")
print(f"napisy = {napisy}")
print(f"mieszana = {mieszana}")

# Tworzenie list innymi sposobami
pusta = []
z_range = list(range(1, 11))  # [1, 2, ..., 10]
powtorzona = [0] * 5           # [0, 0, 0, 0, 0]
print(f"list(range(1,11)) = {z_range}")
print(f"[0] * 5 = {powtorzona}")

# =============================================================================
# 2. Indeksowanie i wycinki (slicing)
# =============================================================================

print("\n=== Indeksowanie i slicing ===")
lista = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print(f"lista = {lista}")
print(f"lista[0]    = {lista[0]}")      # pierwszy element
print(f"lista[-1]   = {lista[-1]}")     # ostatni element
print(f"lista[2:5]  = {lista[2:5]}")    # elementy od indeksu 2 do 4
print(f"lista[:4]   = {lista[:4]}")     # pierwsze 4 elementy
print(f"lista[5:]   = {lista[5:]}")     # od indeksu 5 do konca
print(f"lista[::2]  = {lista[::2]}")    # co drugi element
print(f"lista[::-1] = {lista[::-1]}")   # odwrocona lista

# =============================================================================
# 3. Modyfikowanie list
# =============================================================================

print("\n=== Modyfikowanie list ===")
owoce = ["jablko", "banan", "gruszka"]
print(f"Poczatkowa: {owoce}")

# Dodawanie elementow
owoce.append("kiwi")               # na koniec
print(f"Po append('kiwi'): {owoce}")

owoce.insert(1, "pomarancza")      # na pozycji 1
print(f"Po insert(1, 'pomarancza'): {owoce}")

owoce.extend(["mango", "ananas"])   # wiele elementow na koniec
print(f"Po extend(['mango', 'ananas']): {owoce}")

# Usuwanie elementow
usuniety = owoce.pop()             # usuwa i zwraca ostatni
print(f"Po pop(): {owoce} (usunieto: '{usuniety}')")

usuniety = owoce.pop(0)           # usuwa i zwraca z pozycji 0
print(f"Po pop(0): {owoce} (usunieto: '{usuniety}')")

owoce.remove("banan")             # usuwa pierwsze wystapienie
print(f"Po remove('banan'): {owoce}")

# Zmiana wartosci
owoce[0] = "truskawka"
print(f"Po owoce[0]='truskawka': {owoce}")

# =============================================================================
# 4. Iterowanie po listach
# =============================================================================

print("\n=== Iterowanie ===")
kolory = ["czerwony", "zielony", "niebieski", "zolty"]

# Podstawowe iterowanie
print("Kolory:")
for kolor in kolory:
    print(f"  - {kolor}")

# Z indeksem (enumerate)
print("Z indeksem:")
for i, kolor in enumerate(kolory, start=1):
    print(f"  {i}. {kolor}")

# Iterowanie po dwoch listach rownoczesnie (zip)
nazwy = ["Python", "Java", "C++"]
lata = [1991, 1995, 1985]
print("Jezyki i lata powstania:")
for nazwa, rok in zip(nazwy, lata):
    print(f"  {nazwa} ({rok})")

# =============================================================================
# 5. Operacje na listach
# =============================================================================

print("\n=== Operacje ===")
liczby = [3, 1, 4, 1, 5, 9, 2, 6, 5]
print(f"liczby = {liczby}")
print(f"len(liczby)   = {len(liczby)}")
print(f"sum(liczby)   = {sum(liczby)}")
print(f"min(liczby)   = {min(liczby)}")
print(f"max(liczby)   = {max(liczby)}")
print(f"5 in liczby   = {5 in liczby}")
print(f"7 in liczby   = {7 in liczby}")
print(f"count(1)      = {liczby.count(1)}")
print(f"index(9)      = {liczby.index(9)}")

# Sortowanie
posortowane = sorted(liczby)                  # nowa lista
print(f"sorted(liczby) = {posortowane}")

posortowane_desc = sorted(liczby, reverse=True)
print(f"sorted(rev)    = {posortowane_desc}")

# Sortowanie w miejscu
kopia = liczby.copy()
kopia.sort()
print(f"Po .sort():    {kopia}")

# Odwracanie
odwrocone = list(reversed(liczby))
print(f"reversed:      {odwrocone}")

# =============================================================================
# 6. Kopiowanie list
# =============================================================================

print("\n=== Kopiowanie ===")
oryginalna = [1, [2, 3], 4]
kopia_plytka = oryginalna.copy()   # lub oryginalna[:]
kopia_plytka[0] = 99
kopia_plytka[1][0] = 99  # zmienia tez oryginal (plytka kopia!)
print(f"Oryginalna:  {oryginalna}")
print(f"Kopia plytka: {kopia_plytka}")

import copy
oryginalna2 = [1, [2, 3], 4]
kopia_gleboka = copy.deepcopy(oryginalna2)
kopia_gleboka[1][0] = 99  # NIE zmienia oryginalu
print(f"Oryginalna2:  {oryginalna2}")
print(f"Kopia gleboka: {kopia_gleboka}")

# =============================================================================
# 7. Laczenie i rozpakowywanie
# =============================================================================

print("\n=== Laczenie i rozpakowywanie ===")
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
polaczona = lista1 + lista2
print(f"{lista1} + {lista2} = {polaczona}")

# Rozpakowywanie z gwiazdka
pierwsza, *srodek, ostatnia = [10, 20, 30, 40, 50]
print(f"pierwsza={pierwsza}, srodek={srodek}, ostatnia={ostatnia}")

# =============================================================================
# 8. Przydatne wzorce
# =============================================================================

print("\n=== Przydatne wzorce ===")

# Usuwanie duplikatow (zachowujac kolejnosc)
z_duplikatami = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
bez_duplikatow = list(dict.fromkeys(z_duplikatami))
print(f"Bez duplikatow: {z_duplikatami} -> {bez_duplikatow}")

# Splaszczanie listy (jeden poziom)
zagniezdzona = [[1, 2], [3, 4], [5, 6]]
plaszczenie = [elem for podlista in zagniezdzona for elem in podlista]
print(f"Splaszczona: {zagniezdzona} -> {plaszczenie}")

# Dzielenie na kawalki (chunks)
dane = list(range(1, 11))
rozmiar = 3
kawalki = [dane[i:i+rozmiar] for i in range(0, len(dane), rozmiar)]
print(f"Kawalki po {rozmiar}: {kawalki}")

# Transpozycja macierzy (lista list)
macierz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transponowana = list(map(list, zip(*macierz)))
print(f"Macierz:       {macierz}")
print(f"Transponowana: {transponowana}")