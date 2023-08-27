## Enum w Pythonie

`Enum` (od angielskiego słowa "enumerate" - numerować) to specjalny typ danych w Pythonie, który pozwala na definiowanie uporządkowanych zestawów nazwanych wartości. Wartości te są unikalne i niemodyfikowalne, co czyni je idealnymi do reprezentowania stałych w kodzie.

Główną zaletą używania `Enum` jest czytelność i bezpieczeństwo kodu. Dzięki nim możemy zastąpić "magiczne" wartości liczbowe czy tekstowe bardziej opisowymi nazwami, co zwiększa zrozumiałość kodu.

Aby korzystać z `Enum`, należy najpierw zaimportować odpowiedni moduł.

### Tworzenie Enum

Definicja klasy `Enum` polega na tworzeniu atrybutów klasy, które reprezentują stałe symboliczne. Każdy atrybut w klasie `Enum` jest jednym z jego członków i ma unikalną wartość. Możemy jawnie przypisać wartość do członka lub użyć `enum.auto()`, aby automatycznie przypisać kolejną dostępną wartość.

Przykład definicji `Enum` dla kolorów:

```python
from enum import Enum, auto

class Kolor(Enum):
    ZIELONY = auto()
    CZERWONY = auto()
    NIEBIESKI = auto()

kolor_a = Kolor.ZIELONY
kolor_b = Kolor.CZERWONY

print(kolor_a.name)   # ZIELONY
print(kolor_a.value)  # 1

print(kolor_b.name)   # CZERWONY
print(kolor_b.value)  # 2
```

### Porównywanie pól Enum

Pola Enum mogą być porównywani tylko z innymi członkami tego samego Enum. Porównywanie pól różnych Enum lub porównywanie pól z wartościami liczbowymi/textowymi spowoduje błąd.

```python
if kolor_a == Kolor.ZIELONY:
    print("Kolor jest zielony!")

# Poniższe porównanie spowoduje błąd:
# if kolor_a == 1:
#     print("Błąd!")
```

Wykorzystanie Enum w kodzie Pythona jest rekomendowane, gdy chcemy zapewnić jasność, bezpieczeństwo i niezmienniczość wartości symbolicznych.
