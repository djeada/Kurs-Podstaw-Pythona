"""
Modul demonstracyjny: Programowanie funkcyjne w Pythonie.

Omawiane zagadnienia:
- Funkcje wyzszego rzedu (map, filter, reduce)
- Kompozycja funkcji
- Czyste funkcje vs funkcje z efektami ubocznymi
- Funkcje jako argumenty i wartosci zwracane
- Czesiowe zastosowanie (partial)
- Laczenie wielu transformacji (pipeline)
"""

from functools import reduce, partial


# =============================================================================
# 1. Funkcje pomocnicze
# =============================================================================

def celsjusz_na_fahrenheit(temp):
    """Konwertuje temperature z Celsjusza na Fahrenheita."""
    return (temp * 9 / 5) + 32


def fahrenheit_na_celsjusz(temp):
    """Konwertuje temperature z Fahrenheita na Celsjusza."""
    return (temp - 32) * 5 / 9


def float_z_precyzja(wartosc, precyzja=2, jednostka="°C"):
    """Formatuje liczbe z precyzja i jednostka."""
    return f"{wartosc:.{precyzja}f} {jednostka}"


# =============================================================================
# 2. Czyste funkcje (bez efektow ubocznych)
# =============================================================================

def dodaj(a, b):
    """Czysta funkcja: zawsze ten sam wynik dla tych samych argumentow."""
    return a + b


def podwoj(x):
    """Czysta funkcja: podwaja wartosc."""
    return x * 2


def kwadrat(x):
    """Czysta funkcja: podnosi do kwadratu."""
    return x ** 2


def jest_parzysta(n):
    """Czysta funkcja: sprawdza parzystosc."""
    return n % 2 == 0


# =============================================================================
# 3. Kompozycja funkcji
# =============================================================================

def komponuj(*funkcje):
    """Tworzy kompozycje funkcji: komponuj(f, g, h)(x) = f(g(h(x)))."""
    def skompowana(x):
        wynik = x
        for f in reversed(funkcje):
            wynik = f(wynik)
        return wynik
    return skompowana


def potok(*funkcje):
    """Tworzy potok (pipeline): potok(f, g, h)(x) = h(g(f(x)))."""
    def wykonaj(x):
        wynik = x
        for f in funkcje:
            wynik = f(wynik)
        return wynik
    return wykonaj


# =============================================================================
# Program glowny
# =============================================================================

if __name__ == "__main__":
    # ----- map() -----
    print("=== 1. map() - transformacja elementow ===")
    liczby = [3, 2, 4, 5, 8, 23, 42, 34, 81, 7]

    kwadraty = list(map(kwadrat, liczby))
    print(f"Liczby:   {liczby}")
    print(f"Kwadraty: {kwadraty}")

    # Konwersja temperatur
    temp_f = [32, 68, 98.6, 212]
    temp_c = list(map(fahrenheit_na_celsjusz, temp_f))
    sformatowane = list(map(float_z_precyzja, temp_c))
    print(f"\nFahrenheit: {temp_f}")
    print(f"Celsjusz:   {sformatowane}")

    # map z wieloma iterowalnymi
    a = [1, 2, 3, 4]
    b = [10, 20, 30, 40]
    sumy = list(map(dodaj, a, b))
    print(f"\n{a} + {b} = {sumy}")

    # ----- filter() -----
    print("\n=== 2. filter() - filtrowanie elementow ===")

    nieparzyste = list(filter(lambda x: x % 2 == 1, liczby))
    print(f"Nieparzyste z {liczby}: {nieparzyste}")

    parzyste = list(filter(jest_parzysta, liczby))
    print(f"Parzyste:    {parzyste}")

    # Filtrowanie napisow
    napis = "jakisNaPIS123"
    male_litery = "".join(filter(str.islower, napis))
    wielkie_litery = "".join(filter(str.isupper, napis))
    cyfry = "".join(filter(str.isdigit, napis))
    print(f"\nNapis: '{napis}'")
    print(f"  Male litery: '{male_litery}'")
    print(f"  Wielkie litery: '{wielkie_litery}'")
    print(f"  Cyfry: '{cyfry}'")

    # Filtrowanie None
    dane = [1, None, 3, None, 5, None, 7]
    bez_none = list(filter(None, dane))
    print(f"\nBez None: {dane} -> {bez_none}")

    # ----- reduce() -----
    print("\n=== 3. reduce() - redukcja do jednej wartosci ===")

    # Suma elementow
    suma = reduce(dodaj, liczby)
    print(f"Suma {liczby}: {suma}")

    # Iloczyn elementow
    iloczyn = reduce(lambda x, y: x * y, [1, 2, 3, 4, 5])
    print(f"Iloczyn [1..5]: {iloczyn}")

    # Maksimum (bez uzycia max())
    maksimum = reduce(lambda a, b: a if a > b else b, liczby)
    print(f"Maksimum {liczby}: {maksimum}")

    # Laczenie list
    listy = [[1, 2], [3, 4], [5, 6], [7, 8]]
    polaczone = reduce(lambda a, b: a + b, listy)
    print(f"Polaczone: {listy} -> {polaczone}")

    # ----- partial() -----
    print("\n=== 4. partial() - czesciowe zastosowanie ===")

    # Tworzenie wyspecjalizowanych funkcji
    dodaj_5 = partial(dodaj, 5)
    pomnoz_3 = partial(lambda a, b: a * b, 3)

    print(f"dodaj_5(10) = {dodaj_5(10)}")
    print(f"pomnoz_3(7) = {pomnoz_3(7)}")

    # Formatowanie z ustalona precyzja
    format_4 = partial(float_z_precyzja, precyzja=4, jednostka="°F")
    temp_sformatowane = list(map(format_4, temp_f))
    print(f"Format 4 cyfry: {temp_sformatowane}")

    # ----- Kompozycja -----
    print("\n=== 5. Kompozycja i potok (pipeline) ===")

    # komponuj: od prawej do lewej
    podwoj_i_dodaj_1 = komponuj(lambda x: x + 1, podwoj)
    print(f"komponuj(+1, *2)(5) = {podwoj_i_dodaj_1(5)}")  # (5*2)+1 = 11

    # potok: od lewej do prawej (bardziej intuicyjny)
    przetworz = potok(
        lambda x: x + 1,      # krok 1: dodaj 1
        podwoj,                # krok 2: podwoj
        kwadrat,               # krok 3: podnes do kwadratu
    )
    print(f"potok(+1, *2, ^2)(3) = {przetworz(3)}")  # ((3+1)*2)^2 = 64

    # ----- Laczenie map/filter/reduce -----
    print("\n=== 6. Laczenie transformacji ===")

    # Pipeline: filtruj parzyste -> podwoj -> sumuj
    wynik = reduce(
        dodaj,
        map(podwoj, filter(jest_parzysta, liczby))
    )
    print(f"Parzyste z {liczby}, podwojone, zsumowane: {wynik}")

    # Srednia ocen studentow, ktorzy zdali
    oceny = [2.0, 3.5, 4.0, 2.5, 5.0, 3.0, 4.5, 2.0, 4.0]
    zdali = list(filter(lambda o: o >= 3.0, oceny))
    srednia = reduce(dodaj, zdali) / len(zdali)
    print(f"Oceny: {oceny}")
    print(f"Zdali: {zdali}")
    print(f"Srednia zdajacych: {srednia:.2f}")

    # ----- Funkcje wyzszego rzedu -----
    print("\n=== 7. Funkcje wyzszego rzedu ===")

    def zastosuj_do_listy(func, lista):
        """Stosuje funkcje do kazdego elementu listy."""
        return [func(elem) for elem in lista]

    def stworz_filtr(predykat):
        """Tworzy funkcje filtrujaca na podstawie predykatu."""
        def filtruj(lista):
            return [elem for elem in lista if predykat(elem)]
        return filtruj

    filtruj_dodatnie = stworz_filtr(lambda x: x > 0)
    filtruj_krotkie = stworz_filtr(lambda s: len(s) <= 4)

    dane_liczbowe = [-3, 5, -1, 8, -4, 2]
    slowa = ["Python", "Java", "C", "Go", "Rust", "JavaScript"]

    print(f"Dodatnie: {filtruj_dodatnie(dane_liczbowe)}")
    print(f"Krotkie slowa: {filtruj_krotkie(slowa)}")
