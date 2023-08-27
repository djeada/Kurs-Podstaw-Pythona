## Klasy danych

Klasy danych w Pythonie ułatwiają tworzenie klas, które mają głównie służyć do przechowywania danych. Automatyzują one powtarzalne fragmenty kodu, takie jak inicjalizacja atrybutów czy implementacja operatorów porównania. Używanie klas danych może znacząco upraszczać kod, szczególnie w sytuacjach, kiedy klasy służą głównie jako struktury danych.

### Definiowanie klasy danych

Aby zdefiniować klasę danych, używamy dekoratora `@dataclass`. W obrębie takiej klasy definiujemy atrybuty, które mają być przechowywane:

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

- `unsafe_hash`: Określa, czy klasy danych mogą być używane jako klucze w słownikach czy elementy zbiorów.
- `order`: Włącza automatyczne generowanie metod porównawczych, takich jak `__lt__`, `__le__`, `__gt__`, i `__ge__`.

```python
@dataclass(unsafe_hash=True, order=True)
class RGB:
    czerwony: int
    zielony: int
    niebieski: int
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
