"""
Modul demonstracyjny: Klasy i obiekty w Pythonie.

Omawiane zagadnienia:
- Definiowanie klas i tworzenie obiektow
- Konstruktor __init__ i atrybuty instancji
- Metody instancyjne
- Metody specjalne (__str__, __repr__, __eq__)
- Dekorator @property (gettery i settery)
- Metody klasowe (@classmethod) i statyczne (@staticmethod)
- Dziedziczenie i super()
- Enkapsulacja (konwencja _prywatne)
"""

import math


# =============================================================================
# 1. Prosta klasa z atrybutami
# =============================================================================

class Punkt:
    """Reprezentuje punkt w przestrzeni 2D."""

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def przesun(self, dx, dy):
        """Przesuwa punkt o wektor (dx, dy)."""
        self.x += dx
        self.y += dy

    def odleglosc_od(self, inny):
        """Oblicza odleglosc euklidesowa do innego punktu."""
        return math.sqrt((self.x - inny.x) ** 2 + (self.y - inny.y) ** 2)

    def __str__(self):
        return f"Punkt({self.x}, {self.y})"

    def __repr__(self):
        return f"Punkt(x={self.x}, y={self.y})"

    def __eq__(self, other):
        if not isinstance(other, Punkt):
            return NotImplemented
        return self.x == other.x and self.y == other.y


# =============================================================================
# 2. Klasa z enkapsulacja i @property
# =============================================================================

class Kolo:
    """Reprezentuje kolo z kontrolowanym promieniem."""

    def __init__(self, promien, srodek=None):
        self._promien = 0
        self.promien = promien  # uzywa settera do walidacji
        self.srodek = srodek or Punkt(0, 0)

    @property
    def promien(self):
        """Zwraca promien kola."""
        return self._promien

    @promien.setter
    def promien(self, wartosc):
        """Ustawia promien z walidacja (musi byc > 0)."""
        if wartosc <= 0:
            raise ValueError(f"Promien musi byc dodatni, otrzymano: {wartosc}")
        self._promien = wartosc

    @property
    def pole(self):
        """Oblicza pole kola (wlasciwosc tylko do odczytu)."""
        return math.pi * self._promien ** 2

    @property
    def obwod(self):
        """Oblicza obwod kola."""
        return 2 * math.pi * self._promien

    def __str__(self):
        return f"Kolo(promien={self._promien}, srodek={self.srodek})"


# =============================================================================
# 3. Metody klasowe i statyczne
# =============================================================================

class Prostokat:
    """Reprezentuje prostokat z licznikiem instancji."""

    _liczba_instancji = 0

    def __init__(self, szerokosc, wysokosc):
        self.szerokosc = szerokosc
        self.wysokosc = wysokosc
        Prostokat._liczba_instancji += 1

    @property
    def pole(self):
        return self.szerokosc * self.wysokosc

    @property
    def obwod(self):
        return 2 * (self.szerokosc + self.wysokosc)

    @property
    def jest_kwadratem(self):
        return self.szerokosc == self.wysokosc

    @classmethod
    def kwadrat(cls, bok):
        """Alternatywny konstruktor - tworzy kwadrat."""
        return cls(bok, bok)

    @classmethod
    def ile_instancji(cls):
        """Zwraca liczbe utworzonych prostokatow."""
        return cls._liczba_instancji

    @staticmethod
    def czy_poprawne_wymiary(szerokosc, wysokosc):
        """Sprawdza czy wymiary sa poprawne (oba > 0)."""
        return szerokosc > 0 and wysokosc > 0

    def __str__(self):
        return f"Prostokat({self.szerokosc}x{self.wysokosc})"

    def __repr__(self):
        return f"Prostokat(szerokosc={self.szerokosc}, wysokosc={self.wysokosc})"


# =============================================================================
# 4. Dziedziczenie
# =============================================================================

class Figura:
    """Klasa bazowa dla figur geometrycznych."""

    def __init__(self, nazwa):
        self.nazwa = nazwa

    def pole(self):
        raise NotImplementedError("Podklasa musi implementowac metode pole()")

    def obwod(self):
        raise NotImplementedError("Podklasa musi implementowac metode obwod()")

    def opis(self):
        return f"{self.nazwa}: pole={self.pole():.2f}, obwod={self.obwod():.2f}"


class Trojkat(Figura):
    """Trojkat zdefiniowany trzema bokami."""

    def __init__(self, a, b, c):
        super().__init__("Trojkat")
        self.a = a
        self.b = b
        self.c = c

    def pole(self):
        """Oblicza pole wzorem Herona."""
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def obwod(self):
        return self.a + self.b + self.c

    def __str__(self):
        return f"Trojkat(a={self.a}, b={self.b}, c={self.c})"


class KoloFigura(Figura):
    """Kolo jako podklasa Figury."""

    def __init__(self, promien):
        super().__init__("Kolo")
        self.promien = promien

    def pole(self):
        return math.pi * self.promien ** 2

    def obwod(self):
        return 2 * math.pi * self.promien

    def __str__(self):
        return f"Kolo(r={self.promien})"


# =============================================================================
# 5. Klasa z pelnym zestawem metod specjalnych
# =============================================================================

class Wektor2D:
    """Wektor 2D z operatorami arytmetycznymi."""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def dlugosc(self):
        """Zwraca dlugosc (modul) wektora."""
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __add__(self, other):
        return Wektor2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Wektor2D(self.x - other.x, self.y - other.y)

    def __mul__(self, skalar):
        return Wektor2D(self.x * skalar, self.y * skalar)

    def __rmul__(self, skalar):
        return self.__mul__(skalar)

    def __eq__(self, other):
        if not isinstance(other, Wektor2D):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def __abs__(self):
        return self.dlugosc

    def __str__(self):
        return f"Wektor2D({self.x}, {self.y})"

    def __repr__(self):
        return f"Wektor2D(x={self.x}, y={self.y})"

    def iloczyn_skalarny(self, other):
        """Oblicza iloczyn skalarny dwoch wektorow."""
        return self.x * other.x + self.y * other.y


# =============================================================================
# Program glowny
# =============================================================================

if __name__ == "__main__":
    print("=== Punkt ===")
    p1 = Punkt(1, 2)
    p2 = Punkt(4, 6)
    print(f"p1 = {p1}")
    print(f"p2 = {p2}")
    print(f"Odleglosc p1-p2: {p1.odleglosc_od(p2):.2f}")
    p1.przesun(3, 4)
    print(f"p1 po przesunieciu (3,4): {p1}")
    print(f"p1 == p2: {p1 == p2}")

    print("\n=== Kolo z @property ===")
    k = Kolo(5, Punkt(1, 1))
    print(f"{k}")
    print(f"Pole: {k.pole:.2f}")
    print(f"Obwod: {k.obwod:.2f}")
    k.promien = 10
    print(f"Po zmianie promienia: pole={k.pole:.2f}")
    try:
        k.promien = -1
    except ValueError as e:
        print(f"Blad walidacji: {e}")

    print("\n=== Prostokat z @classmethod ===")
    p = Prostokat(4, 6)
    kw = Prostokat.kwadrat(5)
    print(f"{p}, pole={p.pole}, jest kwadratem: {p.jest_kwadratem}")
    print(f"{kw}, pole={kw.pole}, jest kwadratem: {kw.jest_kwadratem}")
    print(f"Liczba instancji: {Prostokat.ile_instancji()}")
    print(f"Czy (3, 4) poprawne: {Prostokat.czy_poprawne_wymiary(3, 4)}")
    print(f"Czy (-1, 4) poprawne: {Prostokat.czy_poprawne_wymiary(-1, 4)}")

    print("\n=== Dziedziczenie (polimorfizm) ===")
    figury = [
        Trojkat(3, 4, 5),
        Trojkat(5, 5, 5),
        KoloFigura(7),
    ]
    for fig in figury:
        print(f"  {fig} -> {fig.opis()}")

    print("\n=== Wektor2D z operatorami ===")
    v1 = Wektor2D(3, 4)
    v2 = Wektor2D(1, 2)
    print(f"v1 = {v1}, dlugosc = {v1.dlugosc:.2f}")
    print(f"v2 = {v2}")
    print(f"v1 + v2 = {v1 + v2}")
    print(f"v1 - v2 = {v1 - v2}")
    print(f"v1 * 3 = {v1 * 3}")
    print(f"2 * v2 = {2 * v2}")
    print(f"v1 . v2 (iloczyn skalarny) = {v1.iloczyn_skalarny(v2)}")
