"""
Modul demonstracyjny: Zmienne w Pythonie.

Omawiane zagadnienia:
- Deklaracja i inicjalizacja zmiennych
- Typy podstawowe (int, float, str, bool, None)
- Operacje arytmetyczne i ich priorytety
- Operacje na napisach
- Dynamiczna zmiana typu (duck typing)
- Konwersja typow (rzutowanie)
- Zamiana wartosci zmiennych
- Identyfikator obiektu (id)
- Typy niemutowalne vs mutowalne
"""

# =============================================================================
# 1. Deklaracja i inicjalizacja zmiennych
# =============================================================================

liczba = 10
print(f"liczba = {liczba}")  # 10

liczba = 20  # przypisanie nowej wartosci do zmiennej
print(f"liczba po zmianie = {liczba}")  # 20

wynik = liczba + 10  # operacja na zmiennych
print(f"wynik = liczba + 10 = {wynik}")  # 30

# =============================================================================
# 2. Typy podstawowe
# =============================================================================

calkowita = 42
zmiennoprzecinkowa = 3.14
napis = "Ala ma kota"
logiczna = True
pusta = None

print(f"\ncalkowita = {calkowita}, typ: {type(calkowita)}")
print(f"zmiennoprzecinkowa = {zmiennoprzecinkowa}, typ: {type(zmiennoprzecinkowa)}")
print(f"napis = '{napis}', typ: {type(napis)}")
print(f"logiczna = {logiczna}, typ: {type(logiczna)}")
print(f"pusta = {pusta}, typ: {type(pusta)}")

# =============================================================================
# 3. Operacje arytmetyczne
# =============================================================================

a = 17
b = 5

print(f"\na = {a}, b = {b}")
print(f"a + b  = {a + b}")    # dodawanie: 22
print(f"a - b  = {a - b}")    # odejmowanie: 12
print(f"a * b  = {a * b}")    # mnozenie: 85
print(f"a / b  = {a / b}")    # dzielenie (float): 3.4
print(f"a // b = {a // b}")   # dzielenie calkowite: 3
print(f"a % b  = {a % b}")    # reszta z dzielenia (modulo): 2
print(f"a ** b = {a ** b}")   # potegowanie: 1419857

# mieszanie typow: int + float daje float
wynik_mieszany = calkowita + zmiennoprzecinkowa
print(f"\n{calkowita} + {zmiennoprzecinkowa} = {wynik_mieszany} (typ: {type(wynik_mieszany)})")

# =============================================================================
# 4. Operacje na napisach
# =============================================================================

imie = "Python"
print(f"\nimie = '{imie}'")
print(f"imie + ' 3' = '{imie + ' 3'}'")   # konkatenacja
print(f"imie * 3 = '{imie * 3}'")          # powielanie
print(f"len(imie) = {len(imie)}")          # dlugosc napisu
print(f"imie.upper() = '{imie.upper()}'")  # wielkie litery
print(f"imie.lower() = '{imie.lower()}'")  # male litery

# f-stringi (od Python 3.6)
wersja = 3
print(f"{imie} w wersji {wersja} jest swietny!")

# =============================================================================
# 5. Dynamiczna zmiana typu
# =============================================================================

zmienna = 100
print(f"\nzmienna = {zmienna}, typ: {type(zmienna)}")
zmienna = "teraz jestem napisem"
print(f"zmienna = '{zmienna}', typ: {type(zmienna)}")
zmienna = [1, 2, 3]
print(f"zmienna = {zmienna}, typ: {type(zmienna)}")

# =============================================================================
# 6. Konwersja typow (rzutowanie)
# =============================================================================

tekst_liczba = "123"
przekonwertowana = int(tekst_liczba)
print(f"\nint('{tekst_liczba}') = {przekonwertowana}")

liczba_do_napisu = str(456)
print(f"str(456) = '{liczba_do_napisu}'")

do_float = float("3.14")
print(f"float('3.14') = {do_float}")

# bool() - wartosci falszywe: 0, 0.0, "", [], {}, None
print(f"\nbool(0) = {bool(0)}")
print(f"bool(1) = {bool(1)}")
print(f"bool('') = {bool('')}")
print(f"bool('tekst') = {bool('tekst')}")
print(f"bool([]) = {bool([])}")
print(f"bool(None) = {bool(None)}")

# =============================================================================
# 7. Zamiana wartosci zmiennych
# =============================================================================

a = 3
b = 9
print(f"\nPrzed zamiana: a = {a}, b = {b}")

a, b = b, a  # idiomatyczna zamiana w Pythonie
print(f"Po zamianie:  a = {a}, b = {b}")

# =============================================================================
# 8. Identyfikator obiektu (id) i niemutowalnosc
# =============================================================================

x = 5
y = x  # y wskazuje na ten sam obiekt co x
print(f"\nx = {x}, y = {y}")
print(f"id(x) = {id(x)}, id(y) = {id(y)}")
print(f"x is y: {x is y}")  # True - ten sam obiekt w pamieci

y = 10  # y teraz wskazuje na nowy obiekt
print(f"\nPo y = 10:")
print(f"x = {x}, y = {y}")
print(f"id(x) = {id(x)}, id(y) = {id(y)}")
print(f"x is y: {x is y}")  # False - rozne obiekty

# =============================================================================
# 9. Rozpakowywanie (unpacking)
# =============================================================================

# przypisanie wielokrotne
pierwszy, drugi, trzeci = 10, 20, 30
print(f"\npierwszy={pierwszy}, drugi={drugi}, trzeci={trzeci}")

# rozpakowywanie z gwiazdka
poczatek, *srodek, koniec = [1, 2, 3, 4, 5]
print(f"poczatek={poczatek}, srodek={srodek}, koniec={koniec}")

# =============================================================================
# 10. Stale (konwencja nazewnictwa)
# =============================================================================

# Python nie ma prawdziwych stalych, ale konwencja wielkich liter
# sygnalizuje, ze wartosc nie powinna byc zmieniana
MAKSYMALNA_PREDKOSC = 120
PI = 3.14159265
NAZWA_APLIKACJI = "MojaAplikacja"

print(f"\nPI = {PI}")
print(f"MAKSYMALNA_PREDKOSC = {MAKSYMALNA_PREDKOSC}")
print(f"NAZWA_APLIKACJI = '{NAZWA_APLIKACJI}'")
