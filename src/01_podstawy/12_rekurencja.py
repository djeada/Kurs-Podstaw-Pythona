"""
Modul demonstracyjny: Rekurencja w Pythonie.

Omawiane zagadnienia:
- Porownanie iteracji z rekurencja
- Silnia
- Ciag Fibonacciego (naiwna i z memoizacja)
- Potegowanie szybkie
- Odwracanie napisu
- Wierze Hanoi
- Przeszukiwanie binarne (rekurencyjne)
- Rekurencja ogonowa
"""

from functools import lru_cache


# =============================================================================
# 1. Suma elementow listy
# =============================================================================

def suma_petla(lista):
    """Sumuje elementy listy iteracyjnie."""
    suma = 0
    for element in lista:
        suma += element
    return suma


def suma_rekurencja(lista):
    """Sumuje elementy listy rekurencyjnie."""
    if len(lista) == 0:
        return 0
    return lista[0] + suma_rekurencja(lista[1:])


# =============================================================================
# 2. Silnia
# =============================================================================

def silnia_petla(n):
    """Oblicza silnie iteracyjnie."""
    silnia = 1
    for i in range(1, n + 1):
        silnia *= i
    return silnia


def silnia_rekurencja(n):
    """Oblicza silnie rekurencyjnie."""
    if n == 0:
        return 1
    return n * silnia_rekurencja(n - 1)


def silnia_ogonowa(n, akumulator=1):
    """Oblicza silnie z rekurencja ogonowa (tail recursion)."""
    if n == 0:
        return akumulator
    return silnia_ogonowa(n - 1, n * akumulator)


# =============================================================================
# 3. Ciag Fibonacciego
# =============================================================================

def fibonacci_petla(n):
    """Oblicza n-ty element ciagu Fibonacciego iteracyjnie."""
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def fibonacci_rekurencja(n):
    """Oblicza n-ty element ciagu Fibonacciego rekurencyjnie (naiwnie)."""
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_rekurencja(n - 1) + fibonacci_rekurencja(n - 2)


@lru_cache(maxsize=None)
def fibonacci_memo(n):
    """Oblicza n-ty element ciagu Fibonacciego z memoizacja."""
    if n < 2:
        return n
    return fibonacci_memo(n - 1) + fibonacci_memo(n - 2)


# =============================================================================
# 4. Potegowanie szybkie (fast exponentiation)
# =============================================================================

def potega_szybka(baza, wykladnik):
    """
    Oblicza baza^wykladnik w O(log n) krokach.
    Wykorzystuje wlasnosc: x^n = (x^(n/2))^2 dla parzystego n.
    """
    if wykladnik == 0:
        return 1
    if wykladnik % 2 == 0:
        polowa = potega_szybka(baza, wykladnik // 2)
        return polowa * polowa
    else:
        return baza * potega_szybka(baza, wykladnik - 1)


# =============================================================================
# 5. Odwracanie napisu
# =============================================================================

def odwroc_napis(napis):
    """Odwraca napis rekurencyjnie."""
    if len(napis) <= 1:
        return napis
    return napis[-1] + odwroc_napis(napis[:-1])


# =============================================================================
# 6. Sprawdzanie palindromu
# =============================================================================

def czy_palindrom(napis):
    """Sprawdza czy napis jest palindromem (rekurencyjnie)."""
    if len(napis) <= 1:
        return True
    if napis[0] != napis[-1]:
        return False
    return czy_palindrom(napis[1:-1])


# =============================================================================
# 7. Wierze Hanoi
# =============================================================================

def hanoi(n, zrodlo="A", cel="C", pomocniczy="B"):
    """
    Rozwiazuje problem Wierz Hanoi.
    Przenosi n krazkow z wieze zrodlowej na celowa.
    """
    if n == 1:
        print(f"  Przenies krazek 1 z {zrodlo} na {cel}")
        return
    hanoi(n - 1, zrodlo, pomocniczy, cel)
    print(f"  Przenies krazek {n} z {zrodlo} na {cel}")
    hanoi(n - 1, pomocniczy, cel, zrodlo)


# =============================================================================
# 8. Przeszukiwanie binarne (rekurencyjne)
# =============================================================================

def szukaj_binarnie(lista, cel, lewy=0, prawy=None):
    """
    Przeszukuje posortowana liste binarnie.
    Zwraca indeks elementu lub -1 jesli nie znaleziono.
    """
    if prawy is None:
        prawy = len(lista) - 1

    if lewy > prawy:
        return -1

    srodek = (lewy + prawy) // 2

    if lista[srodek] == cel:
        return srodek
    elif lista[srodek] < cel:
        return szukaj_binarnie(lista, cel, srodek + 1, prawy)
    else:
        return szukaj_binarnie(lista, cel, lewy, srodek - 1)


# =============================================================================
# 9. NWD (Algorytm Euklidesa)
# =============================================================================

def nwd(a, b):
    """Oblicza najwiekszy wspolny dzielnik rekurencyjnie (Euklides)."""
    if b == 0:
        return a
    return nwd(b, a % b)


# =============================================================================
# 10. Splaszczanie zagniezdzonej listy
# =============================================================================

def splaszcz(lista):
    """Splaszcza zagniezdzona liste do jednego poziomu."""
    wynik = []
    for element in lista:
        if isinstance(element, list):
            wynik.extend(splaszcz(element))
        else:
            wynik.append(element)
    return wynik


# =============================================================================
# Program glowny
# =============================================================================

if __name__ == "__main__":
    print("=== Suma elementow listy ===")
    lista = [1, 2, 3, 4, 5]
    print(f"lista = {lista}")
    print(f"suma_petla:      {suma_petla(lista)}")
    print(f"suma_rekurencja: {suma_rekurencja(lista)}")

    print("\n=== Silnia ===")
    for n in [0, 1, 5, 10]:
        print(f"  {n}! = {silnia_rekurencja(n)}")
    print(f"  silnia_ogonowa(5) = {silnia_ogonowa(5)}")

    print("\n=== Ciag Fibonacciego ===")
    print("Pierwsze 15 elementow:", [fibonacci_petla(i) for i in range(15)])
    print(f"fibonacci_memo(50) = {fibonacci_memo(50)}")

    print("\n=== Potegowanie szybkie ===")
    print(f"2^10 = {potega_szybka(2, 10)}")
    print(f"3^5  = {potega_szybka(3, 5)}")

    print("\n=== Odwracanie napisu ===")
    print(f"odwroc_napis('Python') = '{odwroc_napis('Python')}'")
    print(f"odwroc_napis('abcde')  = '{odwroc_napis('abcde')}'")

    print("\n=== Palindrom ===")
    for slowo in ["kajak", "racecar", "python", "aba", ""]:
        print(f"  czy_palindrom('{slowo}') = {czy_palindrom(slowo)}")

    print("\n=== Wierze Hanoi (3 krazki) ===")
    hanoi(3)

    print("\n=== Przeszukiwanie binarne ===")
    posortowana = [2, 5, 8, 12, 16, 23, 38, 45, 56, 72, 91]
    print(f"lista = {posortowana}")
    for cel in [23, 45, 100]:
        idx = szukaj_binarnie(posortowana, cel)
        if idx != -1:
            print(f"  szukaj({cel}) -> indeks {idx}")
        else:
            print(f"  szukaj({cel}) -> nie znaleziono")

    print("\n=== NWD (Euklides) ===")
    print(f"nwd(48, 18) = {nwd(48, 18)}")
    print(f"nwd(100, 75) = {nwd(100, 75)}")

    print("\n=== Splaszczanie listy ===")
    zagniezdzona = [1, [2, 3], [4, [5, 6]], [[7, 8], 9]]
    print(f"splaszcz({zagniezdzona})")
    print(f"  = {splaszcz(zagniezdzona)}")
