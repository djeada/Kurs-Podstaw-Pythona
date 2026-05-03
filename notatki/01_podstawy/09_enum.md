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

### Konwersja między Enum a wartościami

Możemy konwertować wartości na `Enum` i z powrotem:

```python
from enum import Enum

class Status(Enum):
    AKTYWNY = 1
    NIEAKTYWNY = 0
    ZAWIESZONY = -1

# int → Enum
s = Status(1)
print(s)           # Status.AKTYWNY
print(s.name)      # AKTYWNY
print(s.value)     # 1

# str → Enum (przez nazwę)
s2 = Status["ZAWIESZONY"]
print(s2)          # Status.ZAWIESZONY

# Enum → int
print(s.value)     # 1
print(int(s.value))  # 1

# Sprawdzenie przynależności
print(Status(0) in Status)        # True
print(1 in [e.value for e in Status])  # True
```

### IntEnum — Enum zachowujący się jak liczba całkowita

`IntEnum` łączy cechy `Enum` z `int`: wartości mogą być bezpośrednio porównywane z liczbami:

```python
from enum import IntEnum

class Priorytet(IntEnum):
    NISKI = 1
    SREDNI = 2
    WYSOKI = 3

print(Priorytet.WYSOKI > Priorytet.NISKI)   # True
print(Priorytet.SREDNI == 2)                 # True
print(Priorytet.WYSOKI + 1)                  # 4 (zwykła liczba int)

# Sortowanie z IntEnum
zadania = [
    ("raport", Priorytet.NISKI),
    ("aktualizacja", Priorytet.WYSOKI),
    ("backup", Priorytet.SREDNI),
]
posortowane = sorted(zadania, key=lambda x: x[1], reverse=True)
for nazwa, p in posortowane:
    print(f"{nazwa}: {p.name}")
# aktualizacja: WYSOKI
# backup: SREDNI
# raport: NISKI
```

### Flag — flagi bitowe

`Flag` (i `IntFlag`) służą do definiowania flag bitowych, które można łączyć operatorami bitowymi (`|`, `&`, `^`, `~`):

```python
from enum import Flag, auto

class Uprawnienia(Flag):
    ODCZYT   = auto()  # 1
    ZAPIS    = auto()  # 2
    WYKONANIE = auto() # 4

# Kombinowanie flag
uzytkownik = Uprawnienia.ODCZYT | Uprawnienia.ZAPIS
print(uzytkownik)                               # Uprawnienia.ODCZYT|ZAPIS
print(Uprawnienia.ODCZYT in uzytkownik)         # True
print(Uprawnienia.WYKONANIE in uzytkownik)      # False

# Dodawanie i usuwanie flag
uzytkownik |= Uprawnienia.WYKONANIE
print(Uprawnienia.WYKONANIE in uzytkownik)      # True

uzytkownik &= ~Uprawnienia.ZAPIS
print(Uprawnienia.ZAPIS in uzytkownik)          # False
```

### Enum w instrukcji match (Python 3.10+)

Enum świetnie współpracuje z `match`:

```python
from enum import Enum

class Kolor(Enum):
    CZERWONY = 1
    ZIELONY = 2
    NIEBIESKI = 3

def opis_koloru(kolor):
    match kolor:
        case Kolor.CZERWONY:
            return "Kolor czerwony — stop"
        case Kolor.ZIELONY:
            return "Kolor zielony — jedź"
        case Kolor.NIEBIESKI:
            return "Kolor niebieski — spokój"

print(opis_koloru(Kolor.ZIELONY))  # Kolor zielony — jedź
```

### Alias i unikalne wartości

Domyślnie, jeśli dwa elementy `Enum` mają tę samą wartość, drugi staje się **aliasem** pierwszego:

```python
from enum import Enum, unique

class Kierunek(Enum):
    POLNOC = 1
    N = 1       # alias — wskazuje na POLNOC

print(Kierunek.N is Kierunek.POLNOC)  # True
print(list(Kierunek))  # [<Kierunek.POLNOC: 1>]  — alias nie pojawia się w iteracji
```

Dekorator `@unique` wymusza, aby każda wartość była unikalna (błąd przy duplikatach):

```python
from enum import Enum, unique

@unique
class Status(Enum):
    AKTYWNY = 1
    NIEAKTYWNY = 2
    # ZAWIESZONY = 1  # ValueError: duplicate values found in <enum 'Status'>: ZAWIESZONY -> AKTYWNY
```

### Podsumowanie typów Enum

| Typ        | Dziedziczy po      | Porównanie z liczbą | Flagi bitowe | Zastosowanie                      |
|------------|--------------------|---------------------|--------------|-----------------------------------|
| `Enum`     | `object`           | Nie                 | Nie          | Ogólny zestaw stałych             |
| `IntEnum`  | `int`, `Enum`      | Tak                 | Nie          | Gdy potrzebujemy wartości liczbowej |
| `Flag`     | `Enum`             | Nie                 | Tak          | Flagi bitowe (czyste)             |
| `IntFlag`  | `int`, `Flag`      | Tak                 | Tak          | Flagi bitowe + porównanie z int   |
| `StrEnum`  | `str`, `Enum`      | Tak (str)           | Nie          | Enum tekstowy (Python 3.11+)      |
