## Programowanie funkcyjne

Programowanie funkcyjne, znane również pod angielską nazwą *functional programming*, to paradygmat programowania, który może wydawać się nieco odmienny od tradycyjnych metod. Zamiast skupiać się na sekwencji kroków i zmianie stanu programu, jak to ma miejsce w programowaniu imperatywnym, programowanie funkcyjne traktuje obliczenia jako ewaluację funkcji matematycznych. W tym podejściu unika się zmiany stanu oraz używania danych mutowalnych, co oznacza, że dane nie są modyfikowane po ich utworzeniu. Zamiast tego, tworzy się nowe dane na podstawie istniejących, co prowadzi do kodu bardziej przewidywalnego i łatwiejszego w utrzymaniu.

W programowaniu funkcyjnym funkcje są traktowane jako obywatelki pierwszej klasy. Oznacza to, że funkcje mogą być przekazywane jako argumenty do innych funkcji, zwracane jako wyniki, a nawet przechowywane w strukturach danych. Dzięki temu możliwe jest tworzenie bardziej elastycznego i modularnego kodu. Ponadto, funkcje są zazwyczaj *czyste*, co znaczy, że nie mają efektów ubocznych i dla tych samych argumentów zawsze zwracają ten sam wynik. To sprawia, że kod jest bardziej przewidywalny i łatwiejszy do testowania.

Kolejną istotną cechą jest niezmienność danych. Po utworzeniu obiektu jego stan nie jest zmieniany; jeśli potrzebujemy zmodyfikowanej wersji danych, tworzymy nowy obiekt na podstawie istniejącego. To podejście pomaga unikać błędów związanych z nieoczekiwaną zmianą stanu i ułatwia równoległe przetwarzanie danych.

Zamiast tradycyjnych pętli iteracyjnych, programowanie funkcyjne często wykorzystuje rekurencję do realizacji powtarzających się operacji. Rekurencja polega na tym, że funkcja wywołuje samą siebie z nowymi argumentami, aż do osiągnięcia warunku bazowego.

### Transformacja danych z użyciem `map()`

Wyobraź sobie, że masz listę liczb i chcesz przekształcić każdą z nich według określonej reguły, na przykład podzielić przez pewną wartość. Funkcja `map()` w Pythonie umożliwia to w prosty i elegancki sposób. Przyjmuje ona funkcję i kolekcję jako argumenty, a następnie zwraca nową kolekcję z przekształconymi elementami.

Przykład:

```python
lista = [5, 10, 15, 20, 25, 30, 35, 40]
```

Chcemy podzielić każdą liczbę przez 5 i otrzymać nową listę wyników. Możemy to osiągnąć na dwa sposoby.

Pierwszy sposób to użycie wyrażenia listowego:

```python
lista_a = [elem // 5 for elem in lista]
# Wynik: [1, 2, 3, 4, 5, 6, 7, 8]
```

Drugi sposób to zastosowanie funkcji `map()`:

```python
lista_b = list(map(lambda elem: elem // 5, lista))
# Wynik: [1, 2, 3, 4, 5, 6, 7, 8]
```

Oba podejścia dają ten sam rezultat. Funkcja `map()` stosuje podaną funkcję do każdego elementu kolekcji, tworząc nową kolekcję z wynikami. Jest to szczególnie przydatne, gdy chcemy zastosować bardziej złożoną funkcję przekształcającą lub gdy zależy nam na zachowaniu stylu funkcyjnego w naszym kodzie.

### Selekcja danych z użyciem `filter()`

Czasami potrzebujemy wybrać z kolekcji tylko te elementy, które spełniają określone kryterium. Funkcja `filter()` służy właśnie do tego celu. Przyjmuje funkcję i kolekcję jako argumenty, a następnie zwraca nową kolekcję zawierającą tylko te elementy, dla których funkcja zwróciła wartość prawdziwą.

Przykładowo, chcemy z listy liczb wybrać tylko liczby parzyste:

```python
lista = [5, 10, 15, 20, 25, 30, 35, 40]
```

Możemy to zrobić za pomocą wyrażenia listowego:

```python
lista_a = [elem for elem in lista if elem % 2 == 0]
# Wynik: [10, 20, 30, 40]
```

Lub używając funkcji `filter()`:

```python
lista_b = list(filter(lambda elem: elem % 2 == 0, lista))
# Wynik: [10, 20, 30, 40]
```

Funkcja `filter()` przechodzi przez każdy element kolekcji i przepuszcza tylko te, dla których podana funkcja zwraca wartość prawdziwą. Jest to użyteczne narzędzie do filtrowania danych bez konieczności pisania dodatkowych pętli czy warunków.

### Redukcja danych z użyciem `reduce()`

Zdarza się, że potrzebujemy zredukować kolekcję do pojedynczej wartości, na przykład sumując wszystkie jej elementy. Funkcja `reduce()`, dostępna w module `functools`, jest do tego idealna. Działa ona poprzez iteracyjne stosowanie funkcji do elementów kolekcji, przekazując wynik poprzedniego wywołania jako pierwszy argument do kolejnego.

Aby skorzystać z `reduce()`, najpierw ją importujemy:

```python
from functools import reduce
```

Przykład sumowania listy liczb:

```python
liczby = [1, 2, 3, 4, 5]
suma = reduce(lambda x, y: x + y, liczby)
# Wynik: 15
```

W tym przypadku `reduce()` sumuje kolejno elementy listy:

1. Dodaje pierwsze dwa elementy: `1 + 2 = 3`.
2. Następnie dodaje wynik do kolejnego elementu: `3 + 3 = 6`.
3. Kontynuuje ten proces aż do ostatniego elementu.

W rezultacie otrzymujemy sumę wszystkich elementów listy.

### Łączenie funkcji `map()`, `filter()` i `reduce()`

Funkcje `map()`, `filter()` i `reduce()` można łączyć, aby wykonywać bardziej złożone operacje na danych. Dzięki temu możemy przetwarzać kolekcje w sposób deklaratywny i czytelny.

Przykład:

Mamy napis:

```python
napis = 'Python is Love'
```

Chcemy z tego napisu:

1. Wybrać wszystkie wielkie litery.
2. Zamienić je na ich kody ASCII.
3. Zsumować te kody.

Krok po kroku:

**Wybieranie wielkich liter za pomocą `filter()`:**

```python
wielkie_litery = filter(lambda znak: znak.isupper(), napis)
# Wynik: iterator zawierający 'P' i 'L'
```

Funkcja `znak.isupper()` zwraca `True` dla wielkich liter, więc `filter()` przepuszcza tylko te znaki.

**Zamiana liter na kody ASCII za pomocą `map()`:**

```python
kody_ascii = map(lambda znak: ord(znak), wielkie_litery)
# Wynik: iterator zawierający 80 i 76
```

Funkcja `ord()` zwraca kod ASCII znaku.

**Sumowanie kodów za pomocą `reduce()`:**

```python
from functools import reduce
suma_kodow = reduce(lambda x, y: x + y, kody_ascii)
# Wynik: 156
```

`reduce()` sumuje kody ASCII, dając ostateczny wynik.

Możemy to wszystko połączyć w jedno wyrażenie:

```python
suma_kodow = reduce(
    lambda x, y: x + y,
    map(
        lambda znak: ord(znak),
        filter(lambda znak: znak.isupper(), napis)
    )
)
# Wynik: 156
```

To połączenie funkcji pokazuje, jak można w sposób deklaratywny i zwięzły przetwarzać dane, łącząc proste operacje w potężne narzędzia. Dzięki temu kod jest czytelny i łatwy do modyfikacji, a także zgodny z zasadami programowania funkcyjnego.

### Wyrażenia listowe kontra `map()`/`filter()`

Zarówno wyrażenia listowe, jak i `map()`/`filter()` realizują to samo zadanie — różnią się jedynie stylem. W Pythonie wyrażenia listowe są zazwyczaj bardziej czytelne:

```python
liczby = list(range(1, 11))

# Filtrowanie parzystych i podniesienie do kwadratu
# Styl funkcyjny
wynik_f = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, liczby)))

# Styl wyrażenia listowego — czytelniej
wynik_l = [x**2 for x in liczby if x % 2 == 0]

print(wynik_f)   # [4, 16, 36, 64, 100]
print(wynik_l)   # [4, 16, 36, 64, 100]
```

### Funkcje wyższego rzędu — bardziej zaawansowane przykłady

Funkcja wyższego rzędu to taka, która przyjmuje lub zwraca inną funkcję. Pozwala to tworzyć bardzo elastyczne abstrakcje:

```python
# Fabryka transformatorów
def stworz_transformator(operacje):
    """Tworzy funkcję łączącą listę operacji w łańcuch."""
    def transformuj(x):
        wynik = x
        for op in operacje:
            wynik = op(wynik)
        return wynik
    return transformuj

podwoj_i_dodaj_1 = stworz_transformator([
    lambda x: x * 2,
    lambda x: x + 1,
])

print(list(map(podwoj_i_dodaj_1, [1, 2, 3, 4])))   # [3, 5, 7, 9]
```

### Kompozycja funkcji

Kompozycja funkcji (ang. *function composition*) polega na stosowaniu jednej funkcji do wyniku drugiej: `f(g(x))`:

```python
from functools import reduce

def zloz(*funkcje):
    """Tworzy złożenie funkcji: zloz(f, g, h)(x) == f(g(h(x)))"""
    return reduce(lambda f, g: lambda x: f(g(x)), funkcje)

# Proste przekształcenia
dodaj_1 = lambda x: x + 1
podwoj = lambda x: x * 2
kwadrat = lambda x: x ** 2

# Złożenie: kwadrat(podwoj(dodaj_1(x)))
transformacja = zloz(kwadrat, podwoj, dodaj_1)
print(transformacja(3))   # kwadrat(podwoj(dodaj_1(3))) = kwadrat(podwoj(4)) = kwadrat(8) = 64

# Przetwarzanie tekstu
normalizuj = zloz(str.strip, str.lower, str.title)
# Uwaga: kolejność to od prawej do lewej
import functools
def zloz_od_lewej(*fs):
    return functools.reduce(lambda f, g: lambda x: g(f(x)), fs)

normalizuj2 = zloz_od_lewej(str.strip, str.lower, str.title)
print(normalizuj2("  HELLO WORLD  "))   # Hello World
```

### Currying i aplikacja częściowa

**Currying** to przekształcenie funkcji przyjmującej wiele argumentów w serię funkcji jednoargumentowych. Python nie ma wbudowanego curringu, ale `functools.partial` realizuje **aplikację częściową**:

```python
from functools import partial

def dodaj(a, b):
    return a + b

dodaj_10 = partial(dodaj, 10)
print(dodaj_10(5))    # 15
print(dodaj_10(20))   # 30

# Pełny currying ręcznie
def curry_dodaj(a):
    def wew(b):
        return a + b
    return wew

print(curry_dodaj(3)(4))   # 7

# Bardziej zaawansowany przykład — filtrowanie z funkcją
def filtruj_wg(predykat, kolekcja):
    return list(filter(predykat, kolekcja))

filtruj_parzyste = partial(filtruj_wg, lambda x: x % 2 == 0)
filtruj_dodatnie = partial(filtruj_wg, lambda x: x > 0)

print(filtruj_parzyste([1, 2, 3, 4, 5, 6]))    # [2, 4, 6]
print(filtruj_dodatnie([-2, -1, 0, 1, 2, 3]))   # [1, 2, 3]
```

### Niemutowalność w programowaniu funkcyjnym

Programowanie funkcyjne faworyzuje niemutowalne struktury danych. W Pythonie możemy to osiągnąć na kilka sposobów:

```python
from typing import NamedTuple

# Niemutowalna klasa
class Punkt(NamedTuple):
    x: float
    y: float

    def przesuń(self, dx, dy):
        return Punkt(self.x + dx, self.y + dy)   # Zwraca nowy obiekt!

p1 = Punkt(1.0, 2.0)
p2 = p1.przesuń(3.0, 4.0)

print(p1)   # Punkt(x=1.0, y=2.0)  — niezmieniony!
print(p2)   # Punkt(x=4.0, y=6.0)

# frozenset — niemutowalny zbiór
dozwolone = frozenset(["A", "B", "C"])
# dozwolone.add("D")   # AttributeError!

# tuple zamiast listy dla niemutowalnych sekwencji
STALE = (1, 2, 3, 4, 5)
```

### Moduł `functools` — przydatne narzędzia

```python
import functools

# lru_cache — memoizacja wyników
@functools.lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

print(fib(50))   # 12586269025 — szybko, dzięki cache

# reduce z wartością początkową
from functools import reduce
print(reduce(lambda a, b: a * b, [1, 2, 3, 4, 5]))        # 120
print(reduce(lambda a, b: a * b, [], 1))                   # 1 — wartość domyślna

# total_ordering — automatyczne generowanie operatorów porównania
from functools import total_ordering

@total_ordering
class Temperatura:
    def __init__(self, stopnie):
        self.stopnie = stopnie

    def __eq__(self, other):
        return self.stopnie == other.stopnie

    def __lt__(self, other):
        return self.stopnie < other.stopnie

t1 = Temperatura(20)
t2 = Temperatura(30)
print(t1 < t2)    # True
print(t1 <= t2)   # True — wygenerowane automatycznie
print(t2 > t1)    # True — wygenerowane automatycznie
```

### Styl funkcyjny vs. imperatywny — porównanie

```python
# Zadanie: z listy zamówień wyciągnij wartość netto zamówień aktywnych
zamowienia = [
    {"id": 1, "aktywne": True,  "wartosc": 100.0},
    {"id": 2, "aktywne": False, "wartosc": 200.0},
    {"id": 3, "aktywne": True,  "wartosc": 150.0},
    {"id": 4, "aktywne": True,  "wartosc": 75.0},
]

# Styl imperatywny
suma_imp = 0
for z in zamowienia:
    if z["aktywne"]:
        suma_imp += z["wartosc"]
print(suma_imp)   # 325.0

# Styl funkcyjny
suma_fun = sum(
    z["wartosc"]
    for z in zamowienia
    if z["aktywne"]
)
print(suma_fun)   # 325.0

# Z użyciem map/filter/reduce
from functools import reduce
aktywne = filter(lambda z: z["aktywne"], zamowienia)
wartosci = map(lambda z: z["wartosc"], aktywne)
suma_mfr = reduce(lambda a, b: a + b, wartosci, 0)
print(suma_mfr)   # 325.0
```
