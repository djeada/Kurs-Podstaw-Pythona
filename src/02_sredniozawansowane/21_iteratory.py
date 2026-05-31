"""
Modul demonstracyjny: Iteratory w Pythonie.

Omawiane zagadnienia:
- Protokol iteratora (__iter__, __next__)
- Wbudowane iteratory (iter(), next())
- Wlasne klasy iteratorow
- Iterator nieskonczonego ciagu
- Iterator z warunkiem stopu
- Porownanie: iterator vs generator
- itertools - przydatne iteratory
"""

import itertools


# =============================================================================
# 1. Prosty iterator odwracajacy
# =============================================================================

class IteratorOdwracajacy:
    """Iterator przechodzacy po elementach od konca do poczatku."""

    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.data[self.index]


# =============================================================================
# 2. Iterator zdania (slowo po slowie)
# =============================================================================

class IteratorZdania:
    """Iterator dzielacy zdanie na poszczegolne slowa."""

    def __init__(self, zdanie):
        self.slowa = zdanie.split()
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.slowa):
            raise StopIteration
        slowo = self.slowa[self.index]
        self.index += 1
        return slowo


# =============================================================================
# 3. Iterator zakresu (reimplementacja range)
# =============================================================================

class Zakres:
    """Wlasna implementacja range z obsluga iteratora."""

    def __init__(self, start, stop=None, krok=1):
        if stop is None:
            self.start = 0
            self.stop = start
        else:
            self.start = start
            self.stop = stop
        self.krok = krok

    def __iter__(self):
        self._biezacy = self.start
        return self

    def __next__(self):
        if (self.krok > 0 and self._biezacy >= self.stop) or \
           (self.krok < 0 and self._biezacy <= self.stop):
            raise StopIteration
        wartosc = self._biezacy
        self._biezacy += self.krok
        return wartosc

    def __len__(self):
        return max(0, (self.stop - self.start + self.krok - 1) // self.krok)


# =============================================================================
# 4. Iterator Fibonacciego (nieskonczonosc)
# =============================================================================

class Fibonacci:
    """Nieskoczony iterator generujacy kolejne liczby Fibonacciego."""

    def __init__(self):
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        wartosc = self.a
        self.a, self.b = self.b, self.a + self.b
        return wartosc


# =============================================================================
# 5. Iterator cykliczny
# =============================================================================

class Cykliczny:
    """Iterator powtarzajacy elementy w kolko."""

    def __init__(self, data, max_iteracji=None):
        self.data = list(data)
        self.index = 0
        self.max_iteracji = max_iteracji
        self.iteracja = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.max_iteracji is not None and self.iteracja >= self.max_iteracji:
            raise StopIteration
        if not self.data:
            raise StopIteration
        wartosc = self.data[self.index % len(self.data)]
        self.index += 1
        self.iteracja += 1
        return wartosc


# =============================================================================
# 6. Klasa iterowalna (oddzielny iterator)
# =============================================================================

class Ksiazka:
    """Ksiazka z rozdzialami - iterowalna kolekcja."""

    def __init__(self, tytul, rozdzialy):
        self.tytul = tytul
        self.rozdzialy = rozdzialy

    def __iter__(self):
        """Zwraca nowy iterator (pozwala na wielokrotna iteracje)."""
        return iter(self.rozdzialy)

    def __len__(self):
        return len(self.rozdzialy)

    def __getitem__(self, index):
        return self.rozdzialy[index]


# =============================================================================
# Program glowny
# =============================================================================

if __name__ == "__main__":
    print("=== 1. Wbudowany iterator (iter/next) ===")
    lista = [10, 20, 30]
    it = iter(lista)
    print(f"next() = {next(it)}")  # 10
    print(f"next() = {next(it)}")  # 20
    print(f"next() = {next(it)}")  # 30
    # next(it) -> StopIteration

    print("\n=== 2. Iterator odwracajacy ===")
    print("Lista [1, 2, 3, 4, 5] od konca:")
    for elem in IteratorOdwracajacy([1, 2, 3, 4, 5]):
        print(f"  {elem}")

    print("\nNapis 'Python' od konca:")
    print("  " + "".join(IteratorOdwracajacy("Python")))

    print("\n=== 3. Iterator zdania ===")
    for slowo in IteratorZdania("Python jest wspanialym jezykiem programowania"):
        print(f"  '{slowo}'")

    print("\n=== 4. Wlasny Zakres (jak range) ===")
    print(f"Zakres(5): {list(Zakres(5))}")
    print(f"Zakres(2, 10, 2): {list(Zakres(2, 10, 2))}")
    print(f"Zakres(10, 0, -3): {list(Zakres(10, 0, -3))}")

    print("\n=== 5. Iterator Fibonacciego ===")
    fib = Fibonacci()
    pierwsze_15 = [next(fib) for _ in range(15)]
    print(f"Pierwsze 15 Fibonacci: {pierwsze_15}")

    # Fibonacci < 1000
    fib2 = Fibonacci()
    fib_do_1000 = list(itertools.takewhile(lambda x: x < 1000, fib2))
    print(f"Fibonacci < 1000: {fib_do_1000}")

    print("\n=== 6. Iterator cykliczny ===")
    kolory = Cykliczny(["R", "G", "B"], max_iteracji=9)
    print(f"Kolory (9x): {list(kolory)}")

    print("\n=== 7. Klasa iterowalna (Ksiazka) ===")
    ksiazka = Ksiazka("Python w praktyce", [
        "Wprowadzenie",
        "Typy danych",
        "Funkcje",
        "Klasy",
        "Moduły"
    ])
    print(f"Ksiazka '{ksiazka.tytul}' ({len(ksiazka)} rozdzialow):")
    for i, rozdzial in enumerate(ksiazka, 1):
        print(f"  {i}. {rozdzial}")
    # Mozna iterowac wielokrotnie
    print(f"  Pierwszy: {ksiazka[0]}, Ostatni: {ksiazka[-1]}")

    print("\n=== 8. itertools - przydatne narzedzia ===")

    # chain - laczenie iteratorow
    lancuch = list(itertools.chain([1, 2, 3], [4, 5], [6, 7, 8]))
    print(f"chain: {lancuch}")

    # islice - wycinanie z iteratora
    fib3 = Fibonacci()
    wycinek = list(itertools.islice(fib3, 5, 10))
    print(f"Fibonacci[5:10]: {wycinek}")

    # groupby - grupowanie
    dane = [1, 1, 2, 2, 2, 3, 3, 1, 1]
    grupy = [(k, list(g)) for k, g in itertools.groupby(dane)]
    print(f"groupby({dane}): {grupy}")

    # product - iloczyn kartezjanski
    karty = list(itertools.product(["K", "D", "W"], ["pik", "kier"]))
    print(f"product: {karty}")

    # accumulate - kumulacja
    kumulacja = list(itertools.accumulate([1, 2, 3, 4, 5]))
    print(f"accumulate([1..5]): {kumulacja}")
