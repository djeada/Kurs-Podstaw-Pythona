"""
Modul demonstracyjny: Klasy danych (dataclasses) w Pythonie.

Omawiane zagadnienia:
- Dekorator @dataclass (automatyczne __init__, __repr__, __eq__)
- Pola z wartosciami domyslnymi
- field() i default_factory
- Pola zamrozone (frozen=True)
- Porownywanie i sortowanie (order=True)
- Dziedziczenie klas danych
- Konwersja do/ze slownika
- post_init do walidacji
"""

from dataclasses import dataclass, field, asdict, astuple
from typing import Optional
import math


# =============================================================================
# 1. Podstawowa klasa danych
# =============================================================================

@dataclass
class Punkt:
    """Punkt w przestrzeni 2D."""
    x: float
    y: float

    def odleglosc_od(self, inny: "Punkt") -> float:
        """Oblicza odleglosc euklidesowa do innego punktu."""
        return math.sqrt((self.x - inny.x) ** 2 + (self.y - inny.y) ** 2)

    def przesun(self, dx: float, dy: float) -> "Punkt":
        """Zwraca nowy punkt przesuniety o (dx, dy)."""
        return Punkt(self.x + dx, self.y + dy)


# =============================================================================
# 2. Klasa danych z wartosciami domyslnymi
# =============================================================================

@dataclass
class Student:
    """Dane studenta z wartosciami domyslnymi."""
    imie: str
    nazwisko: str
    wiek: int
    kierunek: str = "Informatyka"
    srednia: float = 0.0
    aktywny: bool = True


# =============================================================================
# 3. field() i default_factory
# =============================================================================

@dataclass
class Koszyk:
    """Koszyk zakupowy z mutowalnym polem domyslnym."""
    wlasciciel: str
    produkty: list = field(default_factory=list)
    _suma: float = field(default=0.0, repr=False)

    def dodaj(self, nazwa: str, cena: float):
        """Dodaje produkt do koszyka."""
        self.produkty.append({"nazwa": nazwa, "cena": cena})
        self._suma += cena

    @property
    def suma(self) -> float:
        """Zwraca laczna wartosc koszyka."""
        return self._suma

    @property
    def ile_produktow(self) -> int:
        return len(self.produkty)


# =============================================================================
# 4. Klasa zamrozona (frozen) - niemutowalna
# =============================================================================

@dataclass(frozen=True)
class Kolor:
    """Niemutowalny kolor RGB."""
    r: int
    g: int
    b: int

    def __post_init__(self):
        """Walidacja wartosci po inicjalizacji."""
        for nazwa, wartosc in [("r", self.r), ("g", self.g), ("b", self.b)]:
            if not (0 <= wartosc <= 255):
                raise ValueError(f"{nazwa} musi byc w zakresie 0-255, otrzymano {wartosc}")

    @property
    def hex(self) -> str:
        """Zwraca kolor w formacie hex."""
        return f"#{self.r:02x}{self.g:02x}{self.b:02x}"


# =============================================================================
# 5. Porownywanie i sortowanie (order=True)
# =============================================================================

@dataclass(order=True)
class Pracownik:
    """Pracownik z automatycznym porownywaniem."""
    # sort_index sluzy do sortowania (nie jest wyswietlany)
    sort_index: float = field(init=False, repr=False)
    imie: str
    stanowisko: str
    pensja: float

    def __post_init__(self):
        # Sortowanie domyslnie po pensji (malejaco = ujemna wartosc)
        self.sort_index = -self.pensja


# =============================================================================
# 6. Dziedziczenie klas danych
# =============================================================================

@dataclass
class Pojazd:
    """Bazowa klasa pojazdu."""
    marka: str
    model: str
    rok: int

    @property
    def wiek(self) -> int:
        return 2024 - self.rok


@dataclass
class Samochod(Pojazd):
    """Samochod - rozszerzenie Pojazdu."""
    liczba_drzwi: int = 4
    przebieg_km: float = 0.0


@dataclass
class Motocykl(Pojazd):
    """Motocykl - rozszerzenie Pojazdu."""
    pojemnosc_cm3: int = 600


# =============================================================================
# 7. Konwersja do/ze slownika
# =============================================================================

def slownik_na_punkt(**kwargs) -> Punkt:
    """Tworzy Punkt ze slownika."""
    return Punkt(**kwargs)


def klasa_na_slownik(instancja) -> dict:
    """Konwertuje klase danych na slownik (rekurencyjnie)."""
    return asdict(instancja)


# =============================================================================
# Program glowny
# =============================================================================

if __name__ == "__main__":
    print("=== 1. Podstawowa klasa danych ===")
    p1 = Punkt(1, 2)
    p2 = Punkt(4, 6)
    print(f"p1 = {p1}")
    print(f"p2 = {p2}")
    print(f"p1 == Punkt(1, 2): {p1 == Punkt(1, 2)}")  # True (automatyczny __eq__)
    print(f"Odleglosc p1-p2: {p1.odleglosc_od(p2):.2f}")
    print(f"p1.przesun(3, 4) = {p1.przesun(3, 4)}")

    print("\n=== 2. Wartosci domyslne ===")
    s1 = Student("Jan", "Kowalski", 22, srednia=4.5)
    s2 = Student("Anna", "Nowak", 21, "Matematyka", 4.8)
    print(f"s1 = {s1}")
    print(f"s2 = {s2}")

    print("\n=== 3. field() i default_factory ===")
    k1 = Koszyk("Jan")
    k2 = Koszyk("Anna")
    k1.dodaj("Laptop", 3500.0)
    k1.dodaj("Mysz", 150.0)
    k2.dodaj("Ksiazka", 45.0)
    print(f"k1 = {k1}")
    print(f"  Suma: {k1.suma} PLN, produktow: {k1.ile_produktow}")
    print(f"k2 = {k2}")
    print(f"  Suma: {k2.suma} PLN")
    # Kazdy koszyk ma OSOBNA liste (dzieki default_factory)
    print(f"  k1.produkty is k2.produkty: {k1.produkty is k2.produkty}")  # False

    print("\n=== 4. Frozen (niemutowalny) ===")
    czerwony = Kolor(255, 0, 0)
    zielony = Kolor(0, 128, 0)
    print(f"czerwony = {czerwony}, hex = {czerwony.hex}")
    print(f"zielony = {zielony}, hex = {zielony.hex}")
    # czerwony.r = 100  # FrozenInstanceError!
    try:
        niepoprawny = Kolor(300, 0, 0)
    except ValueError as e:
        print(f"Blad walidacji: {e}")
    # Mozna uzyc jako klucz slownika (hashable)
    paleta = {czerwony: "Czerwony", zielony: "Zielony"}
    print(f"  Paleta: {paleta}")

    print("\n=== 5. Porownywanie i sortowanie ===")
    pracownicy = [
        Pracownik("Jan", "Senior Dev", 15000),
        Pracownik("Anna", "Lead", 18000),
        Pracownik("Piotr", "Junior", 8000),
        Pracownik("Maria", "Mid Dev", 12000),
    ]
    posortowani = sorted(pracownicy)
    print("Pracownicy (wg pensji malejaco):")
    for p in posortowani:
        print(f"  {p.imie:6s} | {p.stanowisko:12s} | {p.pensja:,.0f} PLN")

    print("\n=== 6. Dziedziczenie ===")
    auto = Samochod("Toyota", "Corolla", 2020, przebieg_km=45000)
    moto = Motocykl("Honda", "CBR600", 2019, pojemnosc_cm3=600)
    print(f"auto = {auto}, wiek = {auto.wiek} lat")
    print(f"moto = {moto}, wiek = {moto.wiek} lat")

    print("\n=== 7. Konwersja ===")
    slownik = {"x": -5, "y": 3.14}
    p3 = slownik_na_punkt(**slownik)
    print(f"Ze slownika {slownik} -> {p3}")
    print(f"Na slownik: {klasa_na_slownik(p3)}")
    print(f"Na krotke:  {astuple(p3)}")
