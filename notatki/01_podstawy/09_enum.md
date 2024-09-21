## Enum w Pythonie

`Enum` (od angielskiego słowa "enumerate" - numerować) to specjalny typ danych w Pythonie, który pozwala na definiowanie uporządkowanych zestawów nazwanych wartości. Wartości te są unikalne i niemodyfikowalne, co czyni je idealnymi do reprezentowania stałych w kodzie.

Główną zaletą używania `Enum` jest czytelność i bezpieczeństwo kodu. Dzięki nim możemy zastąpić "magiczne" wartości liczbowe czy tekstowe bardziej opisowymi nazwami, co zwiększa zrozumiałość kodu.

### Korzyści z używania Enum

1. Nazwy członków w `Enum` są bardziej zrozumiałe i opisowe, co zdecydowanie zwiększa **czytelność** kodu w porównaniu do używania "magicznych" liczb lub ciągów znaków.
2. Zastosowanie `Enum` zapewnia **bezpieczeństwo typów**, ponieważ pozwala na użycie tylko wcześniej określonych wartości, co zmniejsza ryzyko błędów.
3. Wartości w `Enum` są **niemodyfikowalne**, co oznacza, że po ich zdefiniowaniu nie można ich zmienić, co dodatkowo zwiększa stabilność kodu.
4. Dzięki `Enum` powiązane wartości mogą być łatwo zorganizowane w jednym miejscu, co wpływa na lepszą **organizację kodu**.

### Tworzenie Enum

Aby korzystać z `Enum`, należy najpierw zaimportować odpowiedni moduł.

```python
from enum import Enum, auto
```

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

### Przypisywanie jawnych wartości

Możemy również przypisać jawne wartości do członków `Enum`, co może być przydatne, gdy wartości te mają specjalne znaczenie lub muszą być zgodne z zewnętrznymi systemami.

```python
from enum import Enum

class Status(Enum):
    AKTYWNY = 1
    NIEAKTYWNY = 0
    ZAWIESZONY = -1

status = Status.AKTYWNY
print(status.name)   # AKTYWNY
print(status.value)  # 1
```

### Porównywanie pól Enum

Pola `Enum` mogą być porównywane tylko z innymi członkami tego samego `Enum`. Porównywanie pól różnych `Enum` lub porównywanie pól z wartościami liczbowymi/textowymi spowoduje błąd.

```python
if kolor_a == Kolor.ZIELONY:
    print("Kolor jest zielony!")

# Poniższe porównanie spowoduje błąd:
# if kolor_a == 1:
#     print("Błąd!")
```

### Iteracja po członkach Enum

Możemy łatwo iterować po wszystkich członkach `Enum` za pomocą pętli.

```python
for kolor in Kolor:
    print(kolor)
```

Wynik:

```
Kolor.ZIELONY
Kolor.CZERWONY
Kolor.NIEBIESKI
```

### Użycie Enum w praktyce

`Enum` są szczególnie przydatne w sytuacjach, gdy mamy do czynienia z zestawem stałych wartości, które mogą być przypisane do zmiennych, takich jak stany aplikacji, kategorie produktów, role użytkowników itp. Dzięki `Enum` kod staje się bardziej zrozumiały i mniej podatny na błędy.

#### Przykład zastosowania Enum w programie

```python
from enum import Enum, auto

class Ranga(Enum):
    POCZATKUJACY = auto()
    SREDNIOZAAWANSOWANY = auto()
    ZAAWANSOWANY = auto()

def okresl_rangę(uzytkownik):
    if uzytkownik.punkty < 100:
        return Ranga.POCZATKUJACY
    elif uzytkownik.punkty < 1000:
        return Ranga.SREDNIOZAAWANSOWANY
    else:
        return Ranga.ZAAWANSOWANY

# Przykładowe użycie:
class Uzytkownik:
    def __init__(self, imie, punkty):
        self.imie = imie
        self.punkty = punkty

uzytkownik = Uzytkownik("Anna", 150)
ranga = okresl_rangę(uzytkownik)
print(f"Użytkownik {uzytkownik.imie} ma rangę: {ranga.name}")
```

Wynik:

```
Użytkownik Anna ma rangę: SREDNIOZAAWANSOWANY
```
