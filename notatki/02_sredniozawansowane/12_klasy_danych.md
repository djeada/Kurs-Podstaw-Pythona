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
