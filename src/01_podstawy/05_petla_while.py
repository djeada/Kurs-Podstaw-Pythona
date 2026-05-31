"""
Modul demonstracyjny: Petla while w Pythonie.

Omawiane zagadnienia:
- Podstawowa petla while
- Kontrola petli: break, continue
- Petla while z else
- Typowe wzorce (odliczanie, walidacja, przetwarzanie cyfr)
- Unikanie petli nieskonczonej
"""

# =============================================================================
# 1. Podstawowa petla while
# =============================================================================

print("=== 1. Podstawowa petla while ===")

# Wypisywanie liczb 0..9
i = 0
while i < 10:
    print(i, end=" ")
    i += 1
print()  # nowa linia

# Odliczanie
print("\nOdliczanie:")
odliczanie = 5
while odliczanie > 0:
    print(f"  {odliczanie}...")
    odliczanie -= 1
print("  Start!")

# =============================================================================
# 2. break i continue
# =============================================================================

print("\n=== 2. break i continue ===")

# break - przerywa petle
print("Szukanie pierwszej liczby podzielnej przez 7 > 50:")
n = 50
while True:
    n += 1
    if n % 7 == 0:
        print(f"  Znaleziono: {n}")
        break

# continue - pomija reszte iteracji
print("\nLiczby 1-20 (pomijamy podzielne przez 3):")
i = 0
while i < 20:
    i += 1
    if i % 3 == 0:
        continue
    print(i, end=" ")
print()

# =============================================================================
# 3. Petla while z else
# =============================================================================

print("\n=== 3. while...else ===")

# else wykonuje sie gdy warunek while stanie sie False (nie przy break)
szukana = 7
lista = [1, 3, 5, 9, 11]
i = 0
while i < len(lista):
    if lista[i] == szukana:
        print(f"Znaleziono {szukana} na pozycji {i}")
        break
    i += 1
else:
    print(f"Nie znaleziono {szukana} w liscie")

# =============================================================================
# 4. Przetwarzanie cyfr liczby
# =============================================================================

print("\n=== 4. Przetwarzanie cyfr ===")

liczba = 987654
print(f"Cyfry liczby {liczba} od konca:")
kopia = liczba
while kopia > 0:
    cyfra = kopia % 10
    print(f"  {cyfra}")
    kopia //= 10

# Suma cyfr
liczba = 12345
suma = 0
kopia = liczba
while kopia > 0:
    suma += kopia % 10
    kopia //= 10
print(f"\nSuma cyfr {liczba} = {suma}")

# =============================================================================
# 5. Algorytm Euklidesa (NWD)
# =============================================================================

print("\n=== 5. Algorytm Euklidesa (NWD) ===")

a, b = 48, 18
a_orig, b_orig = a, b
while b != 0:
    a, b = b, a % b
print(f"NWD({a_orig}, {b_orig}) = {a}")

# =============================================================================
# 6. Aproksymacja pierwiastka (metoda Newtona)
# =============================================================================

print("\n=== 6. Pierwiastek metoda Newtona ===")

liczba = 25.0
przyblizenie = liczba / 2.0
tolerancja = 0.0001

iteracja = 0
while abs(przyblizenie * przyblizenie - liczba) > tolerancja:
    przyblizenie = (przyblizenie + liczba / przyblizenie) / 2
    iteracja += 1

print(f"sqrt({liczba}) ≈ {przyblizenie:.6f} (po {iteracja} iteracjach)")

# =============================================================================
# 7. Gra: zgadywanie liczby (symulacja)
# =============================================================================

print("\n=== 7. Symulacja zgadywania ===")

import random
sekret = random.randint(1, 100)
proba = 50  # strategia: przeszukiwanie binarne
dolna, gorna = 1, 100
proby = 0

while proba != sekret:
    proby += 1
    if proba < sekret:
        dolna = proba + 1
    else:
        gorna = proba - 1
    proba = (dolna + gorna) // 2

print(f"Zgadnieto {sekret} w {proby} probach (przeszukiwanie binarne)")

# =============================================================================
# 8. Collatz (problem 3n+1)
# =============================================================================

print("\n=== 8. Ciag Collatza ===")

n = 27
print(f"Ciag Collatza dla {n}:")
kroki = 0
ciag = [n]
while n != 1:
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1
    ciag.append(n)
    kroki += 1

print(f"  Dlugosc: {kroki} krokow")
print(f"  Maksimum: {max(ciag)}")
print(f"  Pierwsze 10: {ciag[:10]}...")
