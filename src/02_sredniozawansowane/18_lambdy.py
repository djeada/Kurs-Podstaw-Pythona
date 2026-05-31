"""
Modul demonstracyjny: Wyrazenia lambda w Pythonie.

Omawiane zagadnienia:
- Skladnia lambda
- Lambda vs def
- Uzycie z map(), filter(), sorted()
- Lambda z warunkiem (operator trojargumentowy)
- Lambda w strukturach danych
- Typowe wzorce i antywzorce
"""

from dataclasses import dataclass


# =============================================================================
# 1. Porownanie: lambda vs def
# =============================================================================

def funkcja_mat(a, b):
    """Zwykla funkcja obliczajaca a * b - b + 5."""
    return a * b - b + 5


# Rownowazna lambda (anonimowa funkcja jednowyrazeniowa)
mat_lambda = lambda a, b: a * b - b + 5


# =============================================================================
# 2. Klasa pomocnicza
# =============================================================================

@dataclass
class Miasto:
    nazwa: str
    liczba_mieszkancow: int
    powierzchnia_km2: float = 0.0


@dataclass
class Student:
    imie: str
    nazwisko: str
    srednia: float


# =============================================================================
# Program glowny
# =============================================================================

if __name__ == "__main__":
    # ----- Podstawy lambda -----
    print("=== 1. Lambda vs def ===")
    print(f"funkcja_mat(4, 6) = {funkcja_mat(4, 6)}")
    print(f"mat_lambda(4, 6)  = {mat_lambda(4, 6)}")

    # Proste lambdy
    kwadrat = lambda x: x ** 2
    dodaj = lambda a, b: a + b
    print(f"kwadrat(5) = {kwadrat(5)}")
    print(f"dodaj(3, 7) = {dodaj(3, 7)}")

    # ----- map() -----
    print("\n=== 2. map() z lambda ===")
    liczby = [-3, -1, 0, 2, 5, 8]
    kwadraty = list(map(lambda x: x ** 2, liczby))
    print(f"Liczby:   {liczby}")
    print(f"Kwadraty: {kwadraty}")

    # Konwersja temperatury: Celsius -> Fahrenheit
    celsius = [0, 20, 37, 100]
    fahrenheit = list(map(lambda c: round(c * 9/5 + 32, 1), celsius))
    print(f"Celsius:    {celsius}")
    print(f"Fahrenheit: {fahrenheit}")

    # ----- filter() -----
    print("\n=== 3. filter() z lambda ===")
    print(f"Liczby: {liczby}")
    dodatnie = list(filter(lambda x: x > 0, liczby))
    parzyste = list(filter(lambda x: x % 2 == 0, liczby))
    print(f"Dodatnie: {dodatnie}")
    print(f"Parzyste: {parzyste}")

    # Filtrowanie napisow
    slowa = ["Python", "AI", "programowanie", "OOP", "lambda", "if"]
    dlugie = list(filter(lambda s: len(s) > 3, slowa))
    print(f"Slowa dluzsze niz 3 znaki: {dlugie}")

    # ----- sorted() z kluczem -----
    print("\n=== 4. sorted() z lambda (klucz sortowania) ===")
    miasta = [
        Miasto("Inowroclaw", 70_000, 30.4),
        Miasto("Warszawa", 2_000_000, 517.2),
        Miasto("Wroclaw", 1_000_000, 292.8),
        Miasto("Krakow", 800_000, 326.8),
        Miasto("Gdansk", 470_000, 262.0),
    ]

    # Po liczbie mieszkancow (rosnaco)
    po_mieszkancach = sorted(miasta, key=lambda m: m.liczba_mieszkancow)
    print("Po liczbie mieszkancow:")
    for m in po_mieszkancach:
        print(f"  {m.nazwa}: {m.liczba_mieszkancow:,}")

    # Po dlugosci nazwy (malejaco)
    po_nazwie = sorted(miasta, key=lambda m: len(m.nazwa), reverse=True)
    print("\nPo dlugosci nazwy (malejaco):")
    for m in po_nazwie:
        print(f"  {m.nazwa} ({len(m.nazwa)} znakow)")

    # Po gestosc zaludnienia
    po_gestosci = sorted(
        miasta,
        key=lambda m: m.liczba_mieszkancow / m.powierzchnia_km2 if m.powierzchnia_km2 else 0,
        reverse=True
    )
    print("\nPo gestosci zaludnienia:")
    for m in po_gestosci:
        gestosc = m.liczba_mieszkancow / m.powierzchnia_km2 if m.powierzchnia_km2 else 0
        print(f"  {m.nazwa}: {gestosc:.0f} os/km2")

    # ----- Lambda z warunkiem -----
    print("\n=== 5. Lambda z warunkiem (trojargumentowy) ===")
    klasyfikuj = lambda x: "dodatnia" if x > 0 else ("ujemna" if x < 0 else "zero")
    for n in [-5, 0, 3]:
        print(f"  {n} -> {klasyfikuj(n)}")

    wielka_litera = lambda x: x.capitalize() if isinstance(x, str) else x
    print(f"wielka_litera('ala') = '{wielka_litera('ala')}'")
    print(f"wielka_litera(123)   = {wielka_litera(123)}")

    # ----- Sortowanie zlozonych struktur -----
    print("\n=== 6. Sortowanie studentow ===")
    studenci = [
        Student("Jan", "Kowalski", 4.2),
        Student("Anna", "Nowak", 4.8),
        Student("Piotr", "Wisniewski", 3.9),
        Student("Maria", "Zielinska", 4.5),
        Student("Adam", "Lewandowski", 4.8),
    ]

    # Po sredniej malejaco, potem po nazwisku
    ranking = sorted(studenci, key=lambda s: (-s.srednia, s.nazwisko))
    print("Ranking studentow:")
    for i, s in enumerate(ranking, 1):
        print(f"  {i}. {s.imie} {s.nazwisko} (srednia: {s.srednia})")

    # ----- reduce z lambda -----
    print("\n=== 7. reduce() z lambda ===")
    from functools import reduce
    liczby_do_redukcji = [1, 2, 3, 4, 5]
    iloczyn = reduce(lambda x, y: x * y, liczby_do_redukcji)
    suma = reduce(lambda x, y: x + y, liczby_do_redukcji)
    print(f"Liczby: {liczby_do_redukcji}")
    print(f"Iloczyn (reduce): {iloczyn}")
    print(f"Suma (reduce):    {suma}")

    # Najdluzsze slowo
    slowa_2 = ["Python", "programowanie", "jest", "super"]
    najdluzsze = reduce(lambda a, b: a if len(a) >= len(b) else b, slowa_2)
    print(f"Najdluzsze slowo: '{najdluzsze}'")

    # ----- Slownik operacji -----
    print("\n=== 8. Lambda w slowniku (dispatch) ===")
    operacje = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "*": lambda a, b: a * b,
        "/": lambda a, b: a / b if b != 0 else float("inf"),
        "**": lambda a, b: a ** b,
    }

    a, b = 10, 3
    for symbol, op in operacje.items():
        print(f"  {a} {symbol} {b} = {op(a, b)}")

    # ----- Generowanie funkcji -----
    print("\n=== 9. Lambda jako fabryka funkcji ===")
    def stworz_mnoznik(n):
        return lambda x: x * n

    podwoj = stworz_mnoznik(2)
    potroj = stworz_mnoznik(3)
    print(f"podwoj(7)  = {podwoj(7)}")
    print(f"potroj(7)  = {potroj(7)}")
