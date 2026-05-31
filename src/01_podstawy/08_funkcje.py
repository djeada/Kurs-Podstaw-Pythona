"""
Modul demonstracyjny: Funkcje w Pythonie.

Omawiane zagadnienia:
- Definiowanie i wywolywanie funkcji
- Argumenty pozycyjne i domyslne
- Zwracanie wartosci (return)
- Wiele wartosci zwracanych (krotki)
- Argumenty *args i **kwargs
- Funkcje jako obiekty pierwszej klasy
- Adnotacje typow (type hints)
- Docstringi
- Zasiag zmiennych (scope)
"""


# =============================================================================
# 1. Funkcje podstawowe
# =============================================================================

def powitanie():
    """Wyswietla proste powitanie."""
    print("Witaj w swiecie Pythona!")


def powitanie_z_imieniem(imie):
    """Wyswietla spersonalizowane powitanie."""
    print(f"Witaj, {imie}!")


def powitanie_dla_krola(imie):
    """Wyswietla powitanie krolewiskie dla Jana, zwykle dla innych."""
    if imie == "Jan":
        print("Witaj, Krolu!")
    else:
        print(f"Witaj, {imie}!")


# =============================================================================
# 2. Funkcje z wartoscia zwracana
# =============================================================================

def suma(a, b):
    """Zwraca sume dwoch liczb."""
    return a + b


def maks_dwoch(a, b):
    """Zwraca wieksza z dwoch liczb."""
    if a > b:
        return a
    else:
        return b


def maks_trzech(a, b, c):
    """Zwraca najwieksza z trzech liczb (wykorzystuje maks_dwoch)."""
    return maks_dwoch(a, maks_dwoch(b, c))


def sortuj_trzy(a, b, c):
    """Zwraca trzy liczby posortowane rosnaco."""
    if a > b:
        a, b = b, a
    if b > c:
        b, c = c, b
    if a > b:
        a, b = b, a
    return a, b, c


# =============================================================================
# 3. Argumenty domyslne
# =============================================================================

def potega(baza, wykladnik=2):
    """Oblicza potege; domyslnie podnosi do kwadratu."""
    return baza ** wykladnik


def zbuduj_powitanie(imie, tytul="Pan", uklony=1):
    """Buduje powitanie z tytulem i powtorzonym uklonem."""
    uklony_tekst = "!" * uklony
    return f"Szanowny {tytul} {imie}{uklony_tekst}"


# =============================================================================
# 4. Argumenty *args i **kwargs
# =============================================================================

def suma_wielu(*args):
    """Sumuje dowolna liczbe argumentow pozycyjnych."""
    wynik = 0
    for liczba in args:
        wynik += liczba
    return wynik


def przedstaw_osobe(**kwargs):
    """Wyswietla informacje o osobie przekazane jako argumenty nazwane."""
    for klucz, wartosc in kwargs.items():
        print(f"  {klucz}: {wartosc}")


def uniwersalna(*args, **kwargs):
    """Funkcja przyjmujaca dowolne argumenty pozycyjne i nazwane."""
    print(f"  Pozycyjne: {args}")
    print(f"  Nazwane: {kwargs}")


# =============================================================================
# 5. Wiele wartosci zwracanych
# =============================================================================

def statystyki(lista):
    """Zwraca minimum, maksimum i srednia listy."""
    if not lista:
        return None, None, None
    minimum = min(lista)
    maksimum = max(lista)
    srednia = sum(lista) / len(lista)
    return minimum, maksimum, srednia


def podziel_z_reszta(a, b):
    """Zwraca wynik dzielenia calkowitego i reszte."""
    return a // b, a % b


# =============================================================================
# 6. Funkcje jako obiekty pierwszej klasy
# =============================================================================

def zastosuj_funkcje(func, wartosc):
    """Wywoluje przekazana funkcje na podanej wartosci."""
    return func(wartosc)


def podwoj(x):
    """Zwraca podwojona wartosc."""
    return x * 2


def kwadrat(x):
    """Zwraca kwadrat wartosci."""
    return x ** 2


# =============================================================================
# 7. Adnotacje typow
# =============================================================================

def oblicz_bmi(waga_kg: float, wzrost_m: float) -> float:
    """Oblicza wskaznik masy ciala (BMI)."""
    return waga_kg / (wzrost_m ** 2)


def filtruj_parzyste(liczby: list[int]) -> list[int]:
    """Zwraca liste zawierajaca tylko liczby parzyste."""
    return [n for n in liczby if n % 2 == 0]


# =============================================================================
# 8. Funkcje zagniezdzone i domkniecia (closures)
# =============================================================================

def licznik(start=0):
    """Tworzy licznik z mozliwoscia inkrementacji."""
    wartosc = start

    def nastepny():
        nonlocal wartosc
        wartosc += 1
        return wartosc

    return nastepny


def mnoznik(n):
    """Fabryka funkcji - tworzy funkcje mnozaca przez n."""
    def pomnoz(x):
        return x * n
    return pomnoz


# =============================================================================
# Program glowny
# =============================================================================

if __name__ == "__main__":
    print("=== Funkcje podstawowe ===")
    powitanie()
    powitanie_z_imieniem("Jan")
    powitanie_dla_krola("Jan")
    powitanie_dla_krola("Adam")

    print("\n=== Funkcje z wartoscia zwracana ===")
    print(f"suma(3, 4) = {suma(3, 4)}")
    print(f"maks_dwoch(7, 3) = {maks_dwoch(7, 3)}")
    print(f"maks_trzech(5, 9, 2) = {maks_trzech(5, 9, 2)}")
    print(f"sortuj_trzy(3, 1, 2) = {sortuj_trzy(3, 1, 2)}")

    print("\n=== Argumenty domyslne ===")
    print(f"potega(5) = {potega(5)}")          # 25 (domyslnie kwadrat)
    print(f"potega(2, 10) = {potega(2, 10)}")  # 1024
    print(zbuduj_powitanie("Kowalski"))
    print(zbuduj_powitanie("Nowak", tytul="Profesor", uklony=3))

    print("\n=== *args i **kwargs ===")
    print(f"suma_wielu(1, 2, 3, 4, 5) = {suma_wielu(1, 2, 3, 4, 5)}")
    print("przedstaw_osobe:")
    przedstaw_osobe(imie="Jan", nazwisko="Kowalski", wiek=30)
    print("uniwersalna:")
    uniwersalna(1, 2, 3, klucz="wartosc", inny="argument")

    print("\n=== Wiele wartosci zwracanych ===")
    dane = [4, 7, 1, 9, 3, 6]
    mini, maksi, sr = statystyki(dane)
    print(f"statystyki({dane}): min={mini}, max={maksi}, srednia={sr:.2f}")
    iloraz, reszta = podziel_z_reszta(17, 5)
    print(f"podziel_z_reszta(17, 5) = iloraz: {iloraz}, reszta: {reszta}")

    print("\n=== Funkcje jako obiekty ===")
    print(f"zastosuj_funkcje(podwoj, 7) = {zastosuj_funkcje(podwoj, 7)}")
    print(f"zastosuj_funkcje(kwadrat, 7) = {zastosuj_funkcje(kwadrat, 7)}")
    operacje = [podwoj, kwadrat, abs]
    for op in operacje:
        print(f"  {op.__name__}(-3) = {op(-3)}")

    print("\n=== Adnotacje typow ===")
    print(f"oblicz_bmi(70, 1.75) = {oblicz_bmi(70, 1.75):.1f}")
    print(f"filtruj_parzyste([1..10]) = {filtruj_parzyste(list(range(1, 11)))}")

    print("\n=== Domkniecia (closures) ===")
    licz = licznik(10)
    print(f"licznik(10) -> nastepny(): {licz()}, {licz()}, {licz()}")

    podwoj_f = mnoznik(2)
    potroj_f = mnoznik(3)
    print(f"mnoznik(2)(5) = {podwoj_f(5)}")
    print(f"mnoznik(3)(5) = {potroj_f(5)}")
