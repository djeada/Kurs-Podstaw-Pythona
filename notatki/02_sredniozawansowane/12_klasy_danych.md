## Klasy danych

Klasy danych w Pythonie (data classes) ułatwiają tworzenie klas, które mają głównie służyć do przechowywania danych. Automatyzują one powtarzalne fragmenty kodu, takie jak inicjalizacja atrybutów, implementacja operatorów porównania, a także generowanie metod takich jak `__repr__` i `__eq__`. Używanie klas danych może znacząco upraszczać kod, szczególnie w sytuacjach, kiedy klasy służą głównie jako struktury danych.

### Definiowanie klasy danych

Aby zdefiniować klasę danych, używamy dekoratora `@dataclass` z modułu `dataclasses`. W obrębie takiej klasy definiujemy atrybuty, które mają być przechowywane:

```python
from dataclasses import dataclass

@dataclass
class RGB:
    czerwony: int
    zielony: int
    niebieski: int
```

### Dodatkowe opcje dla klasy danych

Dekorator `@dataclass` oferuje kilka opcjonalnych argumentów do dostosowywania zachowania klasy danych:

- `unsafe_hash`: Określa, czy klasy danych mogą być używane jako klucze w słownikach lub elementy zbiorów.
- `order`: Włącza automatyczne generowanie metod porównawczych, takich jak `__lt__`, `__le__`, `__gt__`, i `__ge__`.
- `frozen`: Sprawia, że instancje klasy danych stają się niemutowalne (read-only).
- `init`: Pozwala wyłączyć automatyczne generowanie metody `__init__`.
- `repr`: Pozwala wyłączyć automatyczne generowanie metody `__repr__`.

```python
@dataclass(unsafe_hash=True, order=True, frozen=True)
class RGB:
    czerwony: int
    zielony: int
    niebieski: int
```

### Przykłady zastosowań

#### Automatyczne generowanie metod

Dzięki dekoratorowi `@dataclass`, metody takie jak `__init__`, `__repr__`, `__eq__`, oraz metody porównawcze są automatycznie generowane. 

```python
kolor1 = RGB(255, 0, 0)
kolor2 = RGB(0, 255, 0)

# Porównywanie obiektów
print(kolor1 < kolor2)  # False (bo czerwony > zielony w porządku leksykograficznym)
print(kolor1 == RGB(255, 0, 0))  # True

# Wypisywanie obiektu
print(kolor1)  # RGB(czerwony=255, zielony=0, niebieski=0)
```

#### Niemutowalność

Użycie argumentu `frozen=True` sprawia, że instancje klasy danych stają się niemutowalne. Przykład:

```python
@dataclass(frozen=True)
class Point:
    x: int
    y: int

p = Point(10, 20)
# p.x = 15  # To spowoduje błąd: dataclasses.FrozenInstanceError
```

#### Niestandardowe inicjalizacje

Czasami chcemy dodać dodatkową logikę inicjalizacji, mimo automatycznego generowania metody `__init__`.

```python
from dataclasses import dataclass, field

@dataclass
class Circle:
    radius: float
    area: float = field(init=False)

    def __post_init__(self):
        self.area = 3.14159 * (self.radius ** 2)

circle = Circle(5)
print(circle.area)  # 78.53975
```

### Funkcjonalności dostępne w klasach danych

Klasy danych w Pythonie oferują różnorodne, wbudowane funkcje, które czynią je niezwykle użytecznymi w wielu kontekstach. Oto przegląd najważniejszych z nich:

| Funkcjonalność          | Przykład                                                                                     |
|-------------------------|---------------------------------------------------------------------------------------------|
| Inicjalizacja atrybutów | `kolor = RGB(255, 255, 0)`                                                                   |
| Reprezentacja tekstowa  | `print(RGB(255, 255, 0))   # "RGB(czerwony=255, zielony=255, niebieski=0)"`                  |
| Porównywanie instancji  | `RGB(255, 255, 0) == RGB(255, 120, 255)`                                                     |
| Sortowanie instancji    | `sorted([ RGB(255, 255, 0), RGB(255, 120, 255)])`                                           |
| Użycie jako klucz w słowniku | `slownik = {kolor : "żółty"}`                                                           |
| Konwersja do słownika   | `from dataclasses import asdict; asdict(RGB(255, 255, 0))`                                   |
| Pomiar wielkości w pamięci | `import sys; sys.getsizeof(RGB(255, 255, 0))`                                              |

### Wartości domyślne i pola z wartościami fabrycznymi

Atrybuty klasy danych mogą mieć wartości domyślne. Dla mutowalnych typów (np. list) używamy `field(default_factory=...)`, aby uniknąć współdzielenia jednego obiektu między instancjami:

```python
from dataclasses import dataclass, field

@dataclass
class Osoba:
    imie: str
    wiek: int = 0
    hobby: list = field(default_factory=list)  # każda instancja dostaje własną listę

p1 = Osoba("Jan")
p2 = Osoba("Anna", wiek=25)
p1.hobby.append("programowanie")

print(p1)  # Osoba(imie='Jan', wiek=0, hobby=['programowanie'])
print(p2)  # Osoba(imie='Anna', wiek=25, hobby=[])  — lista p2 jest niezależna
```

### Konwersja do/ze słownika i krotki

Moduł `dataclasses` dostarcza funkcji pomocniczych:

```python
from dataclasses import dataclass, asdict, astuple

@dataclass
class Punkt:
    x: float
    y: float

p = Punkt(1.5, 2.5)

print(asdict(p))    # {'x': 1.5, 'y': 2.5}
print(astuple(p))   # (1.5, 2.5)

# Tworzenie obiektu ze słownika
slownik = {"x": 3.0, "y": 4.0}
p2 = Punkt(**slownik)
print(p2)           # Punkt(x=3.0, y=4.0)
```

### Porównanie: zwykła klasa vs. klasa danych vs. NamedTuple

| Cecha                   | Zwykła klasa           | `@dataclass`             | `NamedTuple`              |
|-------------------------|------------------------|--------------------------|---------------------------|
| Automatyczny `__init__` | ✗ (pisany ręcznie)     | ✓                        | ✓                         |
| Automatyczny `__repr__` | ✗                      | ✓                        | ✓                         |
| Automatyczny `__eq__`   | ✗                      | ✓                        | ✓ (porównanie po wartości)|
| Mutowalność             | Tak (domyślnie)        | Tak (domyślnie)          | Nie (jak krotka)          |
| Możliwość dziedziczenia | Tak                    | Tak                      | Ograniczona               |
| `frozen=True`           | —                      | Tak                      | Zawsze niemutowalna       |
| Konwersja do słownika   | Ręcznie                | `asdict()`               | `_asdict()`               |
| Dostęp przez indeks     | Nie                    | Nie                      | Tak (`p[0]`)              |

```python
from typing import NamedTuple

class PunktNT(NamedTuple):
    x: float
    y: float

p = PunktNT(1.0, 2.0)
print(p.x)   # 1.0
print(p[0])  # 1.0 — dostęp jak do krotki
# p.x = 3.0  # AttributeError — niemutowalna
```

### Opcje `field()` — kontrola poszczególnych pól

Funkcja `field()` pozwala precyzyjnie kontrolować zachowanie każdego pola:

```python
from dataclasses import dataclass, field

@dataclass
class Produkt:
    nazwa: str
    cena: float
    ilosc: int = field(default=0)
    _id: str = field(init=False, repr=False)  # pole wewnętrzne, pomijane w repr i init
    tagi: list = field(default_factory=list, compare=False)  # nie brane pod uwagę przy ==

    def __post_init__(self):
        import uuid
        self._id = str(uuid.uuid4())[:8]   # generuj ID automatycznie

p1 = Produkt("Jabłko", 2.50, 100)
p2 = Produkt("Jabłko", 2.50, 100)

print(p1)         # Produkt(nazwa='Jabłko', cena=2.5, ilosc=100)  — _id pominięte
print(p1 == p2)   # True — tagi pomijane przy porównaniu
print(p1._id, p2._id)  # różne UUID
```

Dostępne opcje `field()`:

| Opcja              | Domyślnie | Opis                                               |
|--------------------|-----------|-----------------------------------------------------|
| `default`          | —         | Wartość domyślna pola                              |
| `default_factory`  | —         | Fabryka wartości domyślnej (np. `list`)            |
| `init`             | `True`    | Czy pole jest argumentem `__init__`                |
| `repr`             | `True`    | Czy pole jest pokazywane w `__repr__`              |
| `compare`          | `True`    | Czy pole jest brane pod uwagę w `__eq__`           |
| `hash`             | `None`    | Czy pole jest brane pod uwagę w `__hash__`         |
| `metadata`         | `None`    | Dowolne metadane (słownik, tylko do odczytu)       |

### Zmienne klasowe (`ClassVar`)

Pole opatrzone adnotacją `ClassVar` jest **zmienną klasową** — wspólną dla wszystkich instancji, nie tworzącą parametru `__init__`:

```python
from dataclasses import dataclass
from typing import ClassVar

@dataclass
class Licznik:
    wartosc: int
    licznik_instancji: ClassVar[int] = 0   # nie w __init__, wspólna dla klasy

    def __post_init__(self):
        Licznik.licznik_instancji += 1

a = Licznik(10)
b = Licznik(20)
print(Licznik.licznik_instancji)   # 2
print(a.licznik_instancji)         # 2 — ta sama zmienna klasowa
```

### Funkcja `replace()` — tworzenie kopii z modyfikacją

`dataclasses.replace()` tworzy nową instancję klasy danych będącą kopią oryginału z wybranymi zmienionymi polami. Szczególnie przydatna dla `frozen=True`:

```python
from dataclasses import dataclass, replace

@dataclass(frozen=True)
class Konfiguracja:
    host: str = "localhost"
    port: int = 8080
    debug: bool = False

bazowa = Konfiguracja()
produkcyjna = replace(bazowa, host="example.com", port=443, debug=False)
dev = replace(bazowa, debug=True)

print(bazowa)      # Konfiguracja(host='localhost', port=8080, debug=False)
print(produkcyjna) # Konfiguracja(host='example.com', port=443, debug=False)
print(dev)         # Konfiguracja(host='localhost', port=8080, debug=True)
```

### Dziedziczenie klas danych

Klasy danych obsługują dziedziczenie. Klasa potomna może dodawać nowe pola:

```python
from dataclasses import dataclass

@dataclass
class Zwierze:
    imie: str
    wiek: int

@dataclass
class Pies(Zwierze):
    rasa: str
    wytresowany: bool = False

    def __post_init__(self):
        if self.wiek < 0:
            raise ValueError("Wiek nie może być ujemny")

burek = Pies("Burek", 3, "Labrador")
print(burek)  # Pies(imie='Burek', wiek=3, rasa='Labrador', wytresowany=False)
print(burek.imie)   # Burek — dziedziczone pole
```

> **Uwaga**: W Pythonie < 3.10 pola z wartościami domyślnymi w klasie bazowej nie mogą być poprzedzone przez pola bez wartości domyślnych w klasie potomnej (TypeError). W Python 3.10+ dodano `KW_ONLY` aby to obejść.
