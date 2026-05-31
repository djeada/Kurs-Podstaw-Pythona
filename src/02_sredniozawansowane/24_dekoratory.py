"""
Modul demonstracyjny: Dekoratory w Pythonie.

Omawiane zagadnienia:
- Dekorator mierzacy czas wykonania
- Dekorator logujacy wywolania
- Dekorator z argumentami
- Dekorator powtarzajacy wywolanie
- Dekorator cache (memoizacja)
- Dekorator walidujacy typy argumentow
- Laczenie wielu dekoratorow
- functools.wraps (zachowanie metadanych)
"""

import time
import random
import functools


# =============================================================================
# 1. Dekorator mierzacy czas wykonania
# =============================================================================

def licz_czas(funkcja):
    """Mierzy i wyswietla czas wykonania funkcji."""
    @functools.wraps(funkcja)
    def wrapper(*args, **kwargs):
        poczatek = time.perf_counter()
        wynik = funkcja(*args, **kwargs)
        czas = time.perf_counter() - poczatek
        print(f"  [{funkcja.__name__}] Czas: {czas:.6f}s")
        return wynik
    return wrapper


# =============================================================================
# 2. Dekorator logujacy wywolania
# =============================================================================

def loguj(funkcja):
    """Loguje wywolanie funkcji z argumentami i wynikiem."""
    @functools.wraps(funkcja)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        sygnatura = ", ".join(args_repr + kwargs_repr)
        print(f"  Wywolanie: {funkcja.__name__}({sygnatura})")
        wynik = funkcja(*args, **kwargs)
        print(f"  Zwrocono:  {wynik!r}")
        return wynik
    return wrapper


# =============================================================================
# 3. Dekorator z argumentami (fabryka dekoratorow)
# =============================================================================

def powtorz(n):
    """Dekorator powtarzajacy wywolanie funkcji n razy."""
    def dekorator(funkcja):
        @functools.wraps(funkcja)
        def wrapper(*args, **kwargs):
            wynik = None
            for _ in range(n):
                wynik = funkcja(*args, **kwargs)
            return wynik
        return wrapper
    return dekorator


def timeout(sekundy):
    """Dekorator ograniczajacy czas wykonania (uproszczony - tylko loguje)."""
    def dekorator(funkcja):
        @functools.wraps(funkcja)
        def wrapper(*args, **kwargs):
            start = time.perf_counter()
            wynik = funkcja(*args, **kwargs)
            elapsed = time.perf_counter() - start
            if elapsed > sekundy:
                print(f"  UWAGA: {funkcja.__name__} przekroczyla {sekundy}s "
                      f"(zajelo {elapsed:.2f}s)")
            return wynik
        return wrapper
    return dekorator


# =============================================================================
# 4. Dekorator cache (memoizacja)
# =============================================================================

def cache(funkcja):
    """Prosty dekorator cache - zapamietuje wyniki wywolan."""
    pamiec = {}

    @functools.wraps(funkcja)
    def wrapper(*args):
        if args in pamiec:
            return pamiec[args]
        wynik = funkcja(*args)
        pamiec[args] = wynik
        return wynik

    wrapper.pamiec = pamiec
    wrapper.wyczysc = lambda: pamiec.clear()
    return wrapper


# =============================================================================
# 5. Dekorator walidujacy typy argumentow
# =============================================================================

def waliduj_typy(*typy_arg, **typy_kwarg):
    """Dekorator sprawdzajacy typy argumentow funkcji."""
    def dekorator(funkcja):
        @functools.wraps(funkcja)
        def wrapper(*args, **kwargs):
            # Walidacja argumentow pozycyjnych
            for wartosc, oczekiwany_typ in zip(args, typy_arg):
                if not isinstance(wartosc, oczekiwany_typ):
                    raise TypeError(
                        f"{funkcja.__name__}: argument {wartosc!r} powinien byc "
                        f"typu {oczekiwany_typ.__name__}, "
                        f"otrzymano {type(wartosc).__name__}"
                    )
            # Walidacja argumentow nazwanych
            for nazwa, wartosc in kwargs.items():
                if nazwa in typy_kwarg:
                    if not isinstance(wartosc, typy_kwarg[nazwa]):
                        raise TypeError(
                            f"{funkcja.__name__}: {nazwa}={wartosc!r} powinien byc "
                            f"typu {typy_kwarg[nazwa].__name__}"
                        )
            return funkcja(*args, **kwargs)
        return wrapper
    return dekorator


# =============================================================================
# 6. Dekorator zliczajacy wywolania
# =============================================================================

def zlicz_wywolania(funkcja):
    """Zlicza ile razy funkcja zostala wywolana."""
    @functools.wraps(funkcja)
    def wrapper(*args, **kwargs):
        wrapper.licznik += 1
        return funkcja(*args, **kwargs)
    wrapper.licznik = 0
    return wrapper


# =============================================================================
# 7. Dekorator retry (ponowne proby)
# =============================================================================

def retry(max_prob=3, opoznienie=0.1):
    """Ponawia wywolanie funkcji w razie wyjatku."""
    def dekorator(funkcja):
        @functools.wraps(funkcja)
        def wrapper(*args, **kwargs):
            ostatni_blad = None
            for proba in range(1, max_prob + 1):
                try:
                    return funkcja(*args, **kwargs)
                except Exception as e:
                    ostatni_blad = e
                    print(f"  Proba {proba}/{max_prob} nie powiodla sie: {e}")
                    if proba < max_prob:
                        time.sleep(opoznienie)
            raise ostatni_blad
        return wrapper
    return dekorator


# =============================================================================
# Zastosowanie dekoratorow
# =============================================================================

@licz_czas
@loguj
def sumuj_liste(lista):
    """Sumuje elementy listy."""
    return sum(lista)


@powtorz(3)
def przywitaj(imie):
    """Wyswietla powitanie."""
    print(f"  Czesc, {imie}!")
    return imie


@cache
def fibonacci(n):
    """Oblicza n-ty wyraz ciagu Fibonacciego."""
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


@waliduj_typy(str, int)
def powtorz_napis(tekst, razy):
    """Powtarza tekst podana liczbe razy."""
    return tekst * razy


@zlicz_wywolania
def dodaj(a, b):
    """Dodaje dwie liczby."""
    return a + b


@retry(max_prob=3, opoznienie=0.05)
def losowa_operacja():
    """Operacja ktora moze sie nie powiesc."""
    if random.random() < 0.7:
        raise ConnectionError("Serwer niedostepny")
    return "Sukces!"


@timeout(0.5)
@licz_czas
def wolna_funkcja(n):
    """Symuluje wolne obliczenie."""
    wynik = 0
    for i in range(n):
        wynik += i
    return wynik


# =============================================================================
# Program glowny
# =============================================================================

if __name__ == "__main__":
    print("=== 1. Dekorator @licz_czas + @loguj ===")
    lista = [random.random() for _ in range(1_000_000)]
    wynik = sumuj_liste(lista)
    print(f"  Wynik: {wynik:.2f}")

    print("\n=== 2. Dekorator @powtorz(3) ===")
    przywitaj("Python")

    print("\n=== 3. Dekorator @cache (memoizacja) ===")
    print(f"  fibonacci(30) = {fibonacci(30)}")
    print(f"  fibonacci(35) = {fibonacci(35)}")
    print(f"  Rozmiar cache: {len(fibonacci.pamiec)} wpisow")

    print("\n=== 4. Dekorator @waliduj_typy ===")
    print(f"  powtorz_napis('abc', 3) = '{powtorz_napis('abc', 3)}'")
    try:
        powtorz_napis(123, 3)
    except TypeError as e:
        print(f"  Blad: {e}")

    print("\n=== 5. Dekorator @zlicz_wywolania ===")
    for _ in range(5):
        dodaj(1, 2)
    print(f"  dodaj wywolano {dodaj.licznik} razy")

    print("\n=== 6. Dekorator @retry ===")
    try:
        wynik = losowa_operacja()
        print(f"  Wynik: {wynik}")
    except ConnectionError as e:
        print(f"  Ostatecznie nie udalo sie: {e}")

    print("\n=== 7. Dekorator @timeout + @licz_czas ===")
    wolna_funkcja(5_000_000)

    print("\n=== 8. Zachowanie metadanych (functools.wraps) ===")
    print(f"  sumuj_liste.__name__ = '{sumuj_liste.__name__}'")
    print(f"  sumuj_liste.__doc__  = '{sumuj_liste.__doc__}'")
