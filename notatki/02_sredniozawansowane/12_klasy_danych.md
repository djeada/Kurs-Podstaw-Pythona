### Klasy danych

Tworzenie klas często wiąże się z powtarzalnym pisaniem elementów, takich jak inicjalizacja zmiennych przy użyciu funkcji specjalnej `__init__` oraz implementacja operatorów porównania. W takich przypadkach klasy danych (ang. data classes) mogą okazać się bardzo przydatne. Są one specjalnym rodzajem klas, które automatyzują proces tworzenia powtarzalnych elementów, takich jak inicjalizacja zmiennych i implementacja operatorów porównania. W celu utworzenia klasy danych wystarczy, że w obrębie klasy zadeklarujemy pola, które chcemy przechowywać. Są one szczególnie przydatne, gdy głównym celem naszej klasy jest grupowanie danych.

```python
@dataclass(unsafe_hash=True, order=True)
class RGB:
  czerwony: int
  zielony: int
  niebieski: int
```

W powyższym przykładzie klasa `RGB` jest oznaczona dekoratorem `@dataclass`, co oznacza, że jest to klasa danych. Oznacza to, że automatycznie otrzyma ona metody specjalne, takie jak `__init__`, `__eq__` i `__repr__`, które są zwykle ręcznie implementowane w klasach.

Dekorator @dataclass przyjmuje również dwa dodatkowe argumenty: `unsafe_hash` i `order`. Argument `unsafe_hash` określa, czy instancje tej klasy mają być używane jako elementy słowników lub zbiorów (jeśli argument jest ustawiony na `True`, instancje tej klasy mogą być używane jako elementy słowników lub zbiorów). Argument `order` określa, czy instancje tej klasy będą używane jako elementy posortowanej sekwencji (np. listy). Jeśli argument order jest ustawiony na `True`, instancje tej klasy będą automatycznie posiadać metodę specjalną `__lt__`, która pozwala na porównywanie instancji za pomocą operatora `<`.

|    Funkcjonalność     |                      Przykład                                                           |
----------------------- |---------------------------------------------------------------------------------------- |
| Inicjalizacja pól     |  <code>kolor = RGB(255, 255, 0)</code>                                                  |
| Konwersja na napis    |  <code>print(RGB(255, 255, 0))   # "RGB(czerwony=255, zielony=255, niebieski=0)"</code> |
| Porównanie            |  <code>RGB(255, 255, 0) == RGB(255, 120, 255)</code>                                    |
| Porządkowanie         |  <code>sorted([ RGB(255, 255, 0), RGB(255, 120, 255)])</code>                           |
| Funkcja haszująca     |  <code>slownik = {kolor : "kolor"}</code>                                               |
| Rozpakowanie          |  <code>asdict(RGB(255, 255, 0)).values()</code>                                         |
| Optymalizacja pamięci |  <code>sys.getsizeof(RGB)</code>                                                        |
