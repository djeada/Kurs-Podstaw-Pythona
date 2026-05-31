"""
Modul demonstracyjny: Wyjatki (exceptions) w Pythonie.

Omawiane zagadnienia:
- try/except/else/finally
- Hierarchia wyjatkow wbudowanych
- Wlasne wyjatki (klasy wyjatkow)
- Przechwytywanie wielu wyjatkow
- Ponowne rzucanie wyjatkow (raise)
- Kontekst wyjatku (from, __cause__)
- Dobre praktyki obslugi bledow
"""


# =============================================================================
# 1. Podstawy: try/except/else/finally
# =============================================================================

def dziel(a, b):
    """Demonstruje pelna skladnie try/except/else/finally."""
    try:
        wynik = a / b
    except ZeroDivisionError:
        print(f"  BLAD: Nie mozna dzielic {a} przez zero!")
        return None
    except TypeError as e:
        print(f"  BLAD: Nieprawidlowe typy - {e}")
        return None
    else:
        # Wykonuje sie tylko gdy NIE bylo wyjatku
        print(f"  {a} / {b} = {wynik:.4f}")
        return wynik
    finally:
        # Wykonuje sie ZAWSZE (niezaleznie od wyjatku)
        print(f"  [finally] Zakonczono operacje dzielenia.")


# =============================================================================
# 2. Przechwytywanie wielu wyjatkow
# =============================================================================

def bezpieczna_konwersja(wartosc):
    """Konwertuje wartosc na int z obsluga bledow."""
    try:
        return int(wartosc)
    except (ValueError, TypeError) as e:
        print(f"  Nie mozna skonwertowac '{wartosc}': {type(e).__name__}: {e}")
        return None


def pobierz_element(lista, indeks):
    """Pobiera element z listy z obsluga bledow."""
    try:
        return lista[indeks]
    except IndexError:
        print(f"  Indeks {indeks} poza zakresem (dlugosc: {len(lista)})")
        return None
    except TypeError:
        print(f"  Nieprawidlowy typ indeksu: {type(indeks).__name__}")
        return None


# =============================================================================
# 3. Wlasne klasy wyjatkow
# =============================================================================

class BladWalidacji(Exception):
    """Bazowy wyjatek dla bledow walidacji."""

    def __init__(self, pole, wiadomosc):
        self.pole = pole
        self.wiadomosc = wiadomosc
        super().__init__(f"Blad walidacji pola '{pole}': {wiadomosc}")


class ZaKrotkaWartosc(BladWalidacji):
    """Wyjatek rzucany gdy wartosc jest za krotka."""

    def __init__(self, pole, minimalna_dlugosc, aktualna_dlugosc):
        self.minimalna_dlugosc = minimalna_dlugosc
        self.aktualna_dlugosc = aktualna_dlugosc
        super().__init__(
            pole,
            f"minimalna dlugosc to {minimalna_dlugosc}, "
            f"otrzymano {aktualna_dlugosc}"
        )


class PozaZakresem(BladWalidacji):
    """Wyjatek rzucany gdy wartosc jest poza dopuszczalnym zakresem."""

    def __init__(self, pole, minimum, maksimum, wartosc):
        self.minimum = minimum
        self.maksimum = maksimum
        self.wartosc = wartosc
        super().__init__(
            pole,
            f"wartosc {wartosc} poza zakresem [{minimum}, {maksimum}]"
        )


# =============================================================================
# 4. Uzycie wlasnych wyjatkow
# =============================================================================

def waliduj_haslo(haslo):
    """Waliduje haslo - minimum 8 znakow, zawiera cyfre i wielka litere."""
    if len(haslo) < 8:
        raise ZaKrotkaWartosc("haslo", 8, len(haslo))
    if not any(c.isdigit() for c in haslo):
        raise BladWalidacji("haslo", "musi zawierac co najmniej jedna cyfre")
    if not any(c.isupper() for c in haslo):
        raise BladWalidacji("haslo", "musi zawierac co najmniej wielka litere")
    return True


def waliduj_wiek(wiek):
    """Waliduje wiek - musi byc w zakresie 0-150."""
    if not isinstance(wiek, int):
        raise TypeError(f"Wiek musi byc liczba calkowita, otrzymano {type(wiek).__name__}")
    if wiek < 0 or wiek > 150:
        raise PozaZakresem("wiek", 0, 150, wiek)
    return True


# =============================================================================
# 5. Ponowne rzucanie wyjatkow i lancuchowanie
# =============================================================================

class BladPrztwarzania(Exception):
    """Wyjatek wysokiego poziomu dla bledow przetwarzania."""
    pass


def przetworz_dane(dane):
    """Przetwarza dane z lancuchowaniem wyjatkow."""
    try:
        wynik = int(dane) * 2
        return wynik
    except ValueError as e:
        # 'from e' zachowuje oryginalny wyjatek jako przyczyne
        raise BladPrztwarzania(f"Nie mozna przetworzyc danych: '{dane}'") from e


# =============================================================================
# 6. Menedzer kontekstu (with) i wyjatki
# =============================================================================

class BezpiecznyPlik:
    """Menedzer kontekstu z obsluga wyjatkow."""

    def __init__(self, nazwa, tryb="r"):
        self.nazwa = nazwa
        self.tryb = tryb
        self.plik = None

    def __enter__(self):
        try:
            self.plik = open(self.nazwa, self.tryb)
            return self.plik
        except FileNotFoundError:
            print(f"  Plik '{self.nazwa}' nie istnieje - tworzenie...")
            self.plik = open(self.nazwa, "w+")
            return self.plik

    def __exit__(self, typ_wyjatku, wartosc, traceback):
        if self.plik:
            self.plik.close()
        if typ_wyjatku is not None:
            print(f"  Wystapil blad: {typ_wyjatku.__name__}: {wartosc}")
        return False  # nie tlumi wyjatku


# =============================================================================
# 7. Dekorator obslugujacy wyjatki
# =============================================================================

def obsluz_bledy(domyslna=None):
    """Dekorator zwracajacy wartosc domyslna w razie wyjatku."""
    def dekorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                print(f"  [{func.__name__}] Blad: {e}")
                return domyslna
        return wrapper
    return dekorator


@obsluz_bledy(domyslna=0)
def bezpieczne_dzielenie(a, b):
    return a / b


@obsluz_bledy(domyslna=[])
def parsuj_liczby(tekst):
    return [int(x) for x in tekst.split(",")]


# =============================================================================
# Program glowny
# =============================================================================

if __name__ == "__main__":
    print("=== 1. try/except/else/finally ===")
    dziel(10, 3)
    dziel(10, 0)
    dziel("10", "abc")

    print("\n=== 2. Wiele wyjatkow ===")
    for wartosc in [42, "123", "abc", None, 3.14]:
        wynik = bezpieczna_konwersja(wartosc)
        if wynik is not None:
            print(f"  '{wartosc}' -> {wynik}")

    print("\n  Pobieranie elementow:")
    lista = [10, 20, 30]
    for idx in [0, 2, 5, "a"]:
        wynik = pobierz_element(lista, idx)
        if wynik is not None:
            print(f"    lista[{idx}] = {wynik}")

    print("\n=== 3. Wlasne wyjatki ===")
    hasla_testowe = ["abc", "dlugiehaslo", "Krotkie1", "DlugieBezCyfry", "Poprawne1"]
    for haslo in hasla_testowe:
        try:
            waliduj_haslo(haslo)
            print(f"  '{haslo}' -> OK")
        except BladWalidacji as e:
            print(f"  '{haslo}' -> {e.wiadomosc}")

    print("\n  Walidacja wieku:")
    for wiek in [25, -5, 200, 0, 150]:
        try:
            waliduj_wiek(wiek)
            print(f"    wiek={wiek} -> OK")
        except (PozaZakresem, TypeError) as e:
            print(f"    wiek={wiek} -> BLAD: {e}")

    print("\n=== 4. Lancuchowanie wyjatkow ===")
    try:
        przetworz_dane("abc")
    except BladPrztwarzania as e:
        print(f"  {e}")
        print(f"  Przyczyna: {e.__cause__}")

    print("\n=== 5. Dekorator obslugi bledow ===")
    print(f"  bezpieczne_dzielenie(10, 2) = {bezpieczne_dzielenie(10, 2)}")
    print(f"  bezpieczne_dzielenie(10, 0) = {bezpieczne_dzielenie(10, 0)}")
    print(f"  parsuj_liczby('1,2,3') = {parsuj_liczby('1,2,3')}")
    print(f"  parsuj_liczby('1,abc') = {parsuj_liczby('1,abc')}")

    print("\n=== 6. Hierarchia wyjatkow ===")
    print("  BaseException")
    print("  ├── SystemExit")
    print("  ├── KeyboardInterrupt")
    print("  └── Exception")
    print("      ├── ValueError")
    print("      ├── TypeError")
    print("      ├── IndexError")
    print("      ├── KeyError")
    print("      ├── FileNotFoundError")
    print("      ├── ZeroDivisionError")
    print("      └── ... (wiele innych)")
