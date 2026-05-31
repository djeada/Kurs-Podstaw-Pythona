"""
Modul demonstracyjny: Wyrazenia listowe (list comprehensions) w Pythonie.

Omawiane zagadnienia:
- Podstawowe wyrazenia listowe
- Wyrazenia z warunkiem (filtrowanie)
- Wyrazenia z transformacja
- Zagniezdzone wyrazenia listowe
- Wyrazenia slownikowe i zbiorowe
- Wyrazenia generatorowe
- Porownanie z petla for
"""

# =============================================================================
# 1. Podstawy: petla vs wyrazenie listowe
# =============================================================================

print("=== 1. Petla vs wyrazenie listowe ===")

# Wersja z petla
kwadraty_petla = []
for i in range(10):
    kwadraty_petla.append(i ** 2)

# Rownowazne wyrazenie listowe
kwadraty_lc = [i ** 2 for i in range(10)]

print(f"Kwadraty (petla): {kwadraty_petla}")
print(f"Kwadraty (LC):    {kwadraty_lc}")

# =============================================================================
# 2. Wyrazenia z warunkiem (filtrowanie)
# =============================================================================

print("\n=== 2. Filtrowanie ===")

# Tylko parzyste
parzyste = [n for n in range(20) if n % 2 == 0]
print(f"Parzyste < 20: {parzyste}")

# Liczby podzielne przez 3 lub 5
podzielne = [n for n in range(1, 31) if n % 3 == 0 or n % 5 == 0]
print(f"Podzielne przez 3 lub 5 (1-30): {podzielne}")

# Filtrowanie imion
imiona = ["Adam", "Ewa", "Kasia", "Tomek", "Jan", "Grzegorz", "Ola"]
dlugie_imiona = [imie for imie in imiona if len(imie) > 3]
print(f"Imiona > 3 znaki: {dlugie_imiona}")

# Imiona zaczynajace sie na wielka samogloske
na_samogloske = [imie for imie in imiona if imie[0].lower() in "aeiou"]
print(f"Imiona na samogloske: {na_samogloske}")

# =============================================================================
# 3. Transformacje
# =============================================================================

print("\n=== 3. Transformacje ===")

# Konwersja temperatury
celsius = [0, 10, 20, 30, 37, 100]
fahrenheit = [round(c * 9/5 + 32, 1) for c in celsius]
print(f"Celsius:    {celsius}")
print(f"Fahrenheit: {fahrenheit}")

# Wielkie litery
slowa = ["python", "jest", "super"]
wielkie = [s.upper() for s in slowa]
print(f"Wielkie litery: {wielkie}")

# Dlugosc slow
dlugosci = [len(s) for s in slowa]
print(f"Dlugosci: {slowa} -> {dlugosci}")

# =============================================================================
# 4. Wyrazenie z warunkiem if-else (transformacja warunkowa)
# =============================================================================

print("\n=== 4. Warunkowa transformacja (if-else) ===")

liczby = [-5, -2, 0, 3, 7, -1, 4]
# Zamiana ujemnych na 0
nieujemne = [n if n >= 0 else 0 for n in liczby]
print(f"Nieujemne: {liczby} -> {nieujemne}")

# Klasyfikacja
klasyfikacja = ["parzysta" if n % 2 == 0 else "nieparzysta" for n in range(1, 8)]
print(f"Klasyfikacja 1-7: {klasyfikacja}")

# =============================================================================
# 5. Zagniezdzone wyrazenia listowe
# =============================================================================

print("\n=== 5. Zagniezdzone ===")

# Splaszczanie listy list
macierz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
plaszczenie = [elem for wiersz in macierz for elem in wiersz]
print(f"Macierz: {macierz}")
print(f"Splaszczona: {plaszczenie}")

# Iloczyn kartezjanski
kolory = ["czerwony", "niebieski"]
rozmiary = ["S", "M", "L"]
kombinacje = [(kolor, rozmiar) for kolor in kolory for rozmiar in rozmiary]
print(f"Kombinacje: {kombinacje}")

# Macierz jednostkowa 4x4
n = 4
macierz_jednostkowa = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
print(f"Macierz jednostkowa {n}x{n}:")
for wiersz in macierz_jednostkowa:
    print(f"  {wiersz}")

# =============================================================================
# 6. Wyrazenia slownikowe (dict comprehensions)
# =============================================================================

print("\n=== 6. Wyrazenia slownikowe ===")

# Kwadrat -> wartosc
kwadraty_dict = {n: n**2 for n in range(1, 8)}
print(f"Kwadraty: {kwadraty_dict}")

# Odwrocenie slownika
oryg = {"a": 1, "b": 2, "c": 3}
odwrocony = {v: k for k, v in oryg.items()}
print(f"Odwrocony: {oryg} -> {odwrocony}")

# Filtrowanie slownika
oceny = {"Jan": 5, "Anna": 3, "Piotr": 4, "Maria": 5, "Adam": 2}
dobrzy = {imie: ocena for imie, ocena in oceny.items() if ocena >= 4}
print(f"Oceny >= 4: {dobrzy}")

# Zliczanie znakow
tekst = "abrakadabra"
zliczenie = {znak: tekst.count(znak) for znak in set(tekst)}
print(f"Znaki w '{tekst}': {zliczenie}")

# =============================================================================
# 7. Wyrazenia zbiorowe (set comprehensions)
# =============================================================================

print("\n=== 7. Wyrazenia zbiorowe ===")

# Unikalne dlugosci slow
zdanie = "to jest przykladowe zdanie z kilkoma slowami"
dlugosci_slow = {len(slowo) for slowo in zdanie.split()}
print(f"Unikalne dlugosci slow: {sorted(dlugosci_slow)}")

# =============================================================================
# 8. Wyrazenia generatorowe (generator expressions)
# =============================================================================

print("\n=== 8. Wyrazenia generatorowe ===")

# Generator nie tworzy listy w pamieci - oszczedza RAM
suma_kwadratow = sum(x**2 for x in range(1, 101))
print(f"Suma kwadratow 1-100: {suma_kwadratow}")

# Sprawdzenie warunku dla wszystkich/dowolnego elementu
liczby_test = [2, 4, 6, 8, 10]
wszystkie_parzyste = all(n % 2 == 0 for n in liczby_test)
jakas_wieksza_5 = any(n > 5 for n in liczby_test)
print(f"Wszystkie parzyste? {wszystkie_parzyste}")
print(f"Jakas > 5? {jakas_wieksza_5}")

# Laczenie z join
slowa_gen = ["Python", "jest", "super"]
zdanie_gen = " ".join(s.capitalize() for s in slowa_gen)
print(f"Zdanie: '{zdanie_gen}'")

# =============================================================================
# 9. Funkcja z wyrazeniem listowym
# =============================================================================

print("\n=== 9. Funkcja z LC ===")


def wieksze_niz_n(lista, n):
    """Zwraca elementy listy wieksze niz n."""
    return [elem for elem in lista if elem > n]


def zastosuj_do_kazdego(func, lista):
    """Stosuje funkcje do kazdego elementu."""
    return [func(elem) for elem in lista]


dane = [1, 5, 3, 8, 2, 9, 4, 7]
print(f"Wieksze niz 5: {wieksze_niz_n(dane, 5)}")
print(f"Podwojone: {zastosuj_do_kazdego(lambda x: x * 2, dane)}")
