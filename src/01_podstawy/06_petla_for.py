"""
Modul demonstracyjny: Petla for w Pythonie.

Omawiane zagadnienia:
- Iteracja po range()
- Iteracja po kolekcjach (listy, napisy, slowniki)
- enumerate() i zip()
- break, continue w petli for
- Petla for z else
- Zagniezdzone petle for
- Typowe wzorce
"""

# =============================================================================
# 1. range() - generowanie sekwencji
# =============================================================================

print("=== 1. range() ===")

# range(stop) - od 0 do stop-1
print("range(5):", list(range(5)))

# range(start, stop) - od start do stop-1
print("range(3, 8):", list(range(3, 8)))

# range(start, stop, step) - z krokiem
print("range(0, 20, 3):", list(range(0, 20, 3)))

# Odliczanie wstecz
print("range(10, 0, -1):", list(range(10, 0, -1)))

# =============================================================================
# 2. Iteracja po kolekcjach
# =============================================================================

print("\n=== 2. Iteracja po kolekcjach ===")

# Lista
owoce = ["jablko", "banan", "gruszka", "kiwi"]
print("Owoce:")
for owoc in owoce:
    print(f"  - {owoc}")

# Napis (znak po znaku)
napis = "Python"
print(f"\nZnaki w '{napis}':")
for znak in napis:
    print(f"  '{znak}'", end="")
print()

# Slownik
oceny = {"matematyka": 5, "fizyka": 4, "informatyka": 5, "polski": 3}
print("\nOceny:")
for przedmiot, ocena in oceny.items():
    print(f"  {przedmiot}: {ocena}")

# =============================================================================
# 3. enumerate() - iteracja z indeksem
# =============================================================================

print("\n=== 3. enumerate() ===")

jezyki = ["Python", "Java", "C++", "Rust", "Go"]
print("Ranking jezykow:")
for i, jezyk in enumerate(jezyki, start=1):
    print(f"  {i}. {jezyk}")

# =============================================================================
# 4. zip() - iteracja po wielu kolekcjach
# =============================================================================

print("\n=== 4. zip() ===")

imiona = ["Jan", "Anna", "Piotr"]
wiek = [25, 30, 22]
miasta = ["Warszawa", "Krakow", "Gdansk"]

print("Osoby:")
for imie, lat, miasto in zip(imiona, wiek, miasta):
    print(f"  {imie}, {lat} lat, mieszka w {miasto}")

# =============================================================================
# 5. break i continue
# =============================================================================

print("\n=== 5. break i continue ===")

# break - szukanie elementu
liczby = [4, 7, 2, 9, 1, 5, 8]
szukana = 9
for i, n in enumerate(liczby):
    if n == szukana:
        print(f"Znaleziono {szukana} na pozycji {i}")
        break

# continue - pomijanie elementow
print("\nLiczby nieparzyste z 1-15:")
for n in range(1, 16):
    if n % 2 == 0:
        continue
    print(n, end=" ")
print()

# =============================================================================
# 6. for...else
# =============================================================================

print("\n=== 6. for...else ===")

# else wykonuje sie gdy petla zakonczy sie normalnie (bez break)
def czy_pierwsza(n):
    """Sprawdza czy n jest liczba pierwsza."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % 2 == 0:
            return False
    else:
        return True  # petla zakonczyla sie bez break

for n in [2, 7, 10, 13, 15, 23]:
    print(f"  {n} {'jest' if czy_pierwsza(n) else 'nie jest'} pierwsza")

# =============================================================================
# 7. Zagniezdzone petle
# =============================================================================

print("\n=== 7. Zagniezdzone petle ===")

# Tabliczka mnozenia 4x4
print("Tabliczka mnozenia:")
for i in range(1, 5):
    for j in range(1, 5):
        print(f"{i*j:4}", end="")
    print()

# Wzorzec trojkata
print("\nTrojkat gwiazdek:")
for i in range(1, 6):
    print("  " + "*" * i)

# =============================================================================
# 8. Akumulowanie wynikow
# =============================================================================

print("\n=== 8. Akumulowanie wynikow ===")

# Sumowanie
dane = [3.5, 2.1, 7.8, 1.4, 5.2]
suma = 0
for wartosc in dane:
    suma += wartosc
print(f"Suma {dane} = {suma:.1f}")

# Filtrowanie do nowej listy
slowa = ["Python", "jest", "swietnym", "jezykiem", "programowania"]
dlugie_slowa = []
for slowo in slowa:
    if len(slowo) >= 6:
        dlugie_slowa.append(slowo)
print(f"Slowa >= 6 znakow: {dlugie_slowa}")

# Tworzenie slownika
kwadraty = {}
for n in range(1, 8):
    kwadraty[n] = n ** 2
print(f"Kwadraty: {kwadraty}")

# =============================================================================
# 9. Iteracja po plikach i katalogach (przyklad wzorca)
# =============================================================================

print("\n=== 9. Rozne iterowalne obiekty ===")

# Zbior (set) - kolejnosc nieokreslona
zbior = {3, 1, 4, 1, 5, 9}
print(f"Elementy zbioru: ", end="")
for elem in sorted(zbior):
    print(elem, end=" ")
print()

# Generowanie par (indeks, wartosc) recznie
dane = "ABCDE"
print("Pary (indeks, wartosc):")
for i in range(len(dane)):
    print(f"  [{i}] = '{dane[i]}'")

# =============================================================================
# 10. Wzorzec: sumowanie z warunkiem
# =============================================================================

print("\n=== 10. Praktyczne wzorce ===")

# Zliczanie wystapien
tekst = "programowanie w pythonie jest fascynujace"
samogloski = "aeiou"
licznik = 0
for znak in tekst:
    if znak in samogloski:
        licznik += 1
print(f"Samogloski w '{tekst[:30]}...': {licznik}")

# Maksimum i minimum
temperatury = [15.2, 18.7, 22.1, 19.5, 25.3, 14.8, 20.0]
maks = temperatury[0]
mini = temperatury[0]
for temp in temperatury:
    if temp > maks:
        maks = temp
    if temp < mini:
        mini = temp
print(f"Temperatury: min={mini}°C, max={maks}°C")
