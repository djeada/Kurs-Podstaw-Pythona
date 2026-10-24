# Podstawy Pythona — quiz

Notatki: [Zmienne](../notatki/01_podstawy/03_zmienne.md), [Warunki](../notatki/01_podstawy/04_warunki.md), [Pętle](../notatki/01_podstawy/05_petle.md), [Funkcje](../notatki/01_podstawy/06_funkcje.md), [Napisy](../notatki/01_podstawy/07_napisy.md), [Struktury danych](../notatki/01_podstawy/08_struktury_danych.md), [Enum](../notatki/01_podstawy/09_enum.md), [Liczby losowe](../notatki/01_podstawy/10_liczby_losowe.md), [Wyrażenia listowe](../notatki/01_podstawy/11_wyrazenia_listowe.md), [Rekurencja](../notatki/01_podstawy/12_rekurencja.md), [Sortowanie](../notatki/01_podstawy/13_sortowanie.md)

Sprawdź, czy rozumiesz zmienne, warunki, pętle, funkcje, napisy, kolekcje, enumy, losowość, rekurencję i sortowanie.

#### Q. Co wypisze ten program?

```python
print(int(3.99), int(-3.99))
```

* [ ] `3 -4`
* [ ] `4 -4`
* [x] `3 -3`
* [ ] `4 -3`

> **Wyjaśnienie:** `int()` odcina część ułamkową, czyli zaokrągla w stronę zera, a nie do najbliższej liczby ani w dół. Dlatego `-3.99` daje `-3`, a nie `-4`.

#### Q. Co wypisze ten program?

```python
print(bool("False"), bool(0.0), bool([0]))
```

* [x] `True False True`
* [ ] `False False False`
* [ ] `False False True`
* [ ] `True False False`

> **Wyjaśnienie:** Każdy niepusty napis jest prawdziwy, nawet `"False"`, a lista `[0]` ma jeden element, więc też jest prawdziwa. Fałszywe jest tylko zero, czyli `0.0`.

#### Q. Co wypisze ten program?

```python
odpowiedz = "nie"
print(odpowiedz == "tak" or "TAK")
```

* [ ] `False`
* [ ] `True`
* [x] `TAK`
* [ ] `nie`

> **Wyjaśnienie:** Porównanie daje `False`, więc `or` zwraca drugi operand, czyli niepusty napis `"TAK"`. Operator `or` zwraca wartość, która rozstrzygnęła wynik, a nie zawsze `True`/`False`.

#### Q. Co wypisze ten program?

```python
a, b, c = 1, 5, 3
print(a < b > c, a < b < c)
```

* [ ] `False False`
* [x] `True False`
* [ ] `True True`
* [ ] `False True`

> **Wyjaśnienie:** Porównania łańcuchowe są rozwijane do `and`: `a < b > c` to `1 < 5 and 5 > 3`, czyli `True`, a `a < b < c` to `1 < 5 and 5 < 3`, czyli `False`.

#### Q. Co wypisze ten program?

```python
oceny = {"Jan": 5, "Anna": 4}
print(5 in oceny, "Jan" in oceny)
```

* [ ] `True True`
* [ ] `True False`
* [x] `False True`
* [ ] `False False`

> **Wyjaśnienie:** Operator `in` zastosowany do słownika sprawdza wyłącznie klucze. `5` jest wartością, więc wynik to `False`; do wartości służy `5 in oceny.values()`.

#### Q. Co wypisze ten program?

```python
match "go wschód 5".split():
    case ["go", kierunek]:
        print("A", kierunek)
    case ["go", kierunek, ile]:
        print("B", kierunek, ile)
    case _:
        print("C")
```

* [ ] `A wschód`
* [ ] `C`
* [x] `B wschód 5`
* [ ] `A wschód 5`

> **Wyjaśnienie:** Wzorzec sekwencji pasuje tylko do listy o tej samej długości. Lista ma trzy elementy, więc pierwszy wzorzec (dwa elementy) odpada, a drugi wiąże `kierunek` i `ile`.

#### Q. Co wypisze ten program?

```python
for n in [3, 5, 7]:
    if n % 2 == 0:
        print("parzysta")
        break
else:
    print("brak parzystych")
```

* [ ] `parzysta`
* [x] `brak parzystych`
* [ ] Nic nie wypisze
* [ ] `parzysta` i `brak parzystych`

> **Wyjaśnienie:** Blok `else` pętli wykonuje się, gdy pętla zakończy się normalnie, bez `break`. Na liście nie ma liczby parzystej, więc `break` nie zadziałał i wykonał się `else`.

#### Q. Co wypisze ten program?

```python
for i in range(10):
    if i % 3 == 0:
        continue
    if i > 5:
        break
    print(i, end=" ")
```

* [ ] `1 2 4 5 7`
* [ ] `0 1 2 4 5`
* [x] `1 2 4 5`
* [ ] `1 2`

> **Wyjaśnienie:** `continue` pomija 0, 3 i 6, bo są podzielne przez 3. Pierwszą liczbą większą od 5, która dociera do drugiego warunku, jest 7, więc `break` kończy pętlę przed jej wypisaniem.

#### Q. Która definicja funkcji jest niepoprawna składniowo?

* [x] `def f(a=1, b):`
* [ ] `def f(a, b=1):`
* [ ] `def f(a, *, b):`
* [ ] `def f(*args, **kwargs):`

> **Wyjaśnienie:** Parametry z wartością domyślną muszą stać po parametrach obowiązkowych. Zapis `def f(a=1, b):` kończy się błędem `SyntaxError`, a pozostałe definicje są poprawne.

#### Q. Co wypisze ten program?

```python
def f(*args, **kwargs):
    print(type(args).__name__, type(kwargs).__name__)

f(1, 2, x=3)
```

* [ ] `list dict`
* [ ] `tuple list`
* [x] `tuple dict`
* [ ] `list tuple`

> **Wyjaśnienie:** `*args` zbiera dodatkowe argumenty pozycyjne w krotkę, a `**kwargs` zbiera argumenty nazwane w słownik.

#### Q. Które wywołanie funkcji `def f(a, /, b, *, c)` jest poprawne?

* [ ] `f(a=1, b=2, c=3)`
* [x] `f(1, 2, c=3)`
* [ ] `f(1, 2, 3)`
* [ ] `f(1, c=3)`

> **Wyjaśnienie:** `a` stoi przed `/`, więc musi być pozycyjny, a `c` stoi po `*`, więc musi być nazwany. `f(1, c=3)` nie podaje wymaganego `b`, a `f(1, 2, 3)` przekazuje `c` pozycyjnie.

#### Q. Co się stanie po uruchomieniu tego programu?

```python
licznik = 0

def zwieksz():
    licznik += 1

zwieksz()
print(licznik)
```

* [ ] Wypisze `1`, bo funkcja widzi zmienną globalną
* [ ] Wypisze `0`, bo zmienia tylko lokalną kopię
* [x] Zgłosi wyjątek `UnboundLocalError`
* [ ] Zgłosi `SyntaxError` już przy definicji funkcji

> **Wyjaśnienie:** Przypisanie wewnątrz funkcji sprawia, że `licznik` jest traktowany jako zmienna lokalna, a ta nie ma jeszcze wartości w chwili odczytu. Żeby zmienić zmienną globalną, trzeba zadeklarować `global licznik`.

#### Q. Co wypisze ten program?

```python
def licznik():
    wartosc = 0
    def zwieksz():
        nonlocal wartosc
        wartosc += 1
        return wartosc
    return zwieksz

a = licznik()
b = licznik()
a()
a()
print(a(), b())
```

* [x] `3 1`
* [ ] `3 3`
* [ ] `4 1`
* [ ] `1 1`

> **Wyjaśnienie:** Każde wywołanie `licznik()` tworzy osobne domknięcie z własną zmienną `wartosc`. `a` zostało wywołane trzy razy, a `b` tylko raz, więc ich liczniki są niezależne.

#### Q. Co wypisze ten program?

```python
def dodaj(a: int, b: int) -> int:
    return a + b

print(dodaj("2", "3"))
```

* [ ] `5`
* [x] `23`
* [ ] Zgłosi `TypeError`
* [ ] `None`

> **Wyjaśnienie:** Adnotacje typów nie są sprawdzane w czasie wykonania; są tylko wskazówką dla ludzi i narzędzi takich jak `mypy`. Dodanie dwóch napisów to konkatenacja, więc wynikiem jest `23`.

#### Q. Co wypisze ten program?

```python
napis = "Pythonista"
print(napis[2:6], napis[-3:])
```

* [ ] `ytho sta`
* [ ] `thoni ista`
* [x] `thon sta`
* [ ] `thon ista`

> **Wyjaśnienie:** Wycinek `[2:6]` obejmuje indeksy 2–5 (bez 6), czyli `thon`. Wycinek `[-3:]` zaczyna się trzy znaki od końca, czyli daje `sta`.

#### Q. Co się stanie po uruchomieniu tego programu?

```python
s = "Hello"
s[0] = "J"
print(s)
```

* [ ] Wypisze `Jello`
* [ ] Wypisze `Hello`
* [ ] Zgłosi `IndexError`
* [x] Zgłosi `TypeError`

> **Wyjaśnienie:** Napisy są niemutowalne, więc nie obsługują przypisania do indeksu i Python zgłasza `TypeError`. Zmieniony tekst trzeba zbudować jako nowy napis, np. `"J" + s[1:]`.

#### Q. Co wypisze ten program?

```python
print("-".join("a,b,,c".split(",")))
```

* [ ] `a-b-c`
* [x] `a-b--c`
* [ ] `abc`
* [ ] `a-b-,-c`

> **Wyjaśnienie:** `split(",")` przy dwóch przecinkach obok siebie tworzy pusty napis, więc lista to `['a', 'b', '', 'c']`. `join` wstawia myślnik między każdą parę elementów, także wokół pustego napisu.

#### Q. Co wypisze ten program?

```python
print("10" < "9", "Z" < "a")
```

* [ ] `False True`
* [ ] `False False`
* [x] `True True`
* [ ] `True False`

> **Wyjaśnienie:** Napisy są porównywane leksykograficznie, znak po znaku według kodów Unicode. `"1"` ma mniejszy kod niż `"9"`, a wielkie `Z` (90) ma mniejszy kod niż małe `a` (97).

#### Q. Co wypisze ten program?

```python
print(len(r"a\nb"), len("a\nb"))
```

* [ ] `3 3`
* [x] `4 3`
* [ ] `4 4`
* [ ] `3 4`

> **Wyjaśnienie:** W napisie surowym `r"..."` ukośnik nie tworzy sekwencji ucieczki, więc `\n` to dwa znaki. W zwykłym napisie `\n` to jeden znak nowej linii.

#### Q. Co wypisze ten program?

```python
a = [1, 2]
a.append([3, 4])
a.extend([5, 6])
print(len(a))
```

* [ ] `6`
* [x] `5`
* [ ] `4`
* [ ] `3`

> **Wyjaśnienie:** `append` dodaje całą listę `[3, 4]` jako jeden element, a `extend` dokłada osobno każdy element z `[5, 6]`. Lista ma więc postać `[1, 2, [3, 4], 5, 6]`.

#### Q. Co wypisze ten program?

```python
a = {1, 2, 3, 4}
b = {3, 4, 5}
print(sorted(a ^ b), sorted(a - b))
```

* [ ] `[3, 4] [1, 2]`
* [ ] `[1, 2, 5] [5]`
* [x] `[1, 2, 5] [1, 2]`
* [ ] `[1, 2, 3, 4, 5] [1, 2]`

> **Wyjaśnienie:** Różnica symetryczna `^` zawiera elementy należące do dokładnie jednego zbioru, a różnica `-` to elementy `a`, których nie ma w `b`. `[3, 4]` to część wspólna `&`.

#### Q. Którego obiektu nie można użyć jako klucza słownika?

* [ ] `(1, 2)`
* [ ] `"klucz"`
* [x] `[1, 2]`
* [ ] `3.5`

> **Wyjaśnienie:** Klucze słownika muszą być haszowalne. Lista jest mutowalna i nie ma skrótu (`hash`), więc `{[1, 2]: "x"}` zgłasza `TypeError`, natomiast krotka liczb, napis i liczba są poprawnymi kluczami.

#### Q. Co wypisze ten program?

```python
d = {"a": 1}
print(d.get("b"), d.setdefault("b", 5), d)
```

* [ ] `None 5 {'a': 1}`
* [x] `None 5 {'a': 1, 'b': 5}`
* [ ] `5 5 {'a': 1, 'b': 5}`
* [ ] Zgłosi `KeyError`

> **Wyjaśnienie:** `get` przy braku klucza zwraca `None` i nie zmienia słownika. `setdefault` dodaje brakujący klucz z wartością domyślną i ją zwraca, więc w chwili wypisania słownik zawiera już `'b': 5`.

#### Q. Co wypisze ten program?

```python
m = [[0] * 2] * 3
m[0][0] = 1
print(m)
```

* [ ] `[[1, 0], [0, 0], [0, 0]]`
* [x] `[[1, 0], [1, 0], [1, 0]]`
* [ ] `[[1, 1], [0, 0], [0, 0]]`
* [ ] `[[1, 0, 0], [0, 0], [0, 0]]`

> **Wyjaśnienie:** Mnożenie `* 3` powtarza referencję do tej samej wewnętrznej listy, więc wszystkie trzy wiersze to jeden obiekt. Niezależne wiersze daje `[[0] * 2 for _ in range(3)]`.

#### Q. Co wypisze ten program?

```python
from enum import Enum, auto

class Kolor(Enum):
    CZERWONY = auto()
    ZIELONY = auto()

print(Kolor.ZIELONY.value, Kolor(1).name)
```

* [ ] `1 ZIELONY`
* [ ] `2 Kolor.CZERWONY`
* [x] `2 CZERWONY`
* [ ] `ZIELONY 1`

> **Wyjaśnienie:** W zwykłym `Enum` funkcja `auto()` numeruje członków od 1, więc `ZIELONY` ma wartość 2. `Kolor(1)` wyszukuje członka po wartości, a `.name` zwraca samą nazwę bez prefiksu klasy.

#### Q. Co wypisze ten program?

```python
from enum import Enum, IntEnum

class A(Enum):
    X = 2

class B(IntEnum):
    X = 2

print(A.X == 2, B.X == 2)
```

* [x] `False True`
* [ ] `True True`
* [ ] `False False`
* [ ] Zgłosi `TypeError`

> **Wyjaśnienie:** Członek zwykłego `Enum` nie jest równy swojej wartości, więc `==` zwraca `False` (bez wyjątku; `TypeError` dają dopiero `<` i `>`). `IntEnum` dziedziczy po `int`, więc porównuje się z liczbami.

#### Q. Która funkcja modułu `random` losuje `k` elementów bez zwracania, czyli bez powtórzeń?

* [ ] `random.choices`
* [x] `random.sample`
* [ ] `random.choice`
* [ ] `random.shuffle`

> **Wyjaśnienie:** `random.sample(populacja, k)` zwraca `k` różnych elementów. `random.choices` losuje ze zwracaniem, więc elementy mogą się powtarzać, a `shuffle` tylko miesza listę w miejscu.

#### Q. Co wypisze ten program?

```python
import random

random.seed(7)
a = [random.randint(1, 100) for _ in range(3)]
random.seed(7)
b = [random.randint(1, 100) for _ in range(3)]
print(a == b)
```

* [ ] `False`
* [ ] Raz `True`, raz `False`
* [x] `True`
* [ ] Zgłosi `ValueError`

> **Wyjaśnienie:** Generator Mersenne Twister jest deterministyczny: to samo ziarno daje zawsze tę samą sekwencję. Dlatego `seed()` służy do odtwarzalnych symulacji i testów.

#### Q. Którego modułu należy użyć do wygenerowania tokenu do resetowania hasła?

* [ ] `random`
* [ ] `math`
* [x] `secrets`
* [ ] `string`

> **Wyjaśnienie:** `random` jest przewidywalny i nie nadaje się do zastosowań związanych z bezpieczeństwem. Moduł `secrets` (np. `secrets.token_urlsafe()`) korzysta z kryptograficznie bezpiecznego źródła losowości.

#### Q. Co wypisze ten program?

```python
print([x * 2 for x in range(6) if x % 2])
```

* [ ] `[0, 4, 8]`
* [ ] `[1, 3, 5]`
* [x] `[2, 6, 10]`
* [ ] `[0, 2, 4, 6, 8, 10]`

> **Wyjaśnienie:** Warunek `x % 2` jest prawdziwy dla liczb nieparzystych (reszta 1), więc przechodzą 1, 3 i 5. Wyrażenie `x * 2` podwaja je dopiero po filtrowaniu.

#### Q. Co wypisze ten program?

```python
print([(i, j) for i in range(3) for j in range(i)])
```

* [ ] `[(0, 0), (1, 0), (2, 0)]`
* [x] `[(1, 0), (2, 0), (2, 1)]`
* [ ] `[(0, 1), (0, 2), (1, 2)]`
* [ ] `[]`

> **Wyjaśnienie:** Pętle `for` w wyrażeniu listowym są zagnieżdżone w kolejności zapisu, więc zewnętrzna jest `i`. Dla `i = 0` zakres `range(0)` jest pusty, a dla 1 i 2 powstają pary z mniejszymi `j`.

#### Q. Co wypisze ten program?

```python
d = {"a": 1, "b": 2, "c": 1}
print({v: k for k, v in d.items()})
```

* [ ] `{1: 'a', 2: 'b'}`
* [x] `{1: 'c', 2: 'b'}`
* [ ] `{1: 'a', 2: 'b', 1: 'c'}`
* [ ] `{1: ['a', 'c'], 2: ['b']}`

> **Wyjaśnienie:** Klucze słownika są unikalne, więc przy odwracaniu późniejsza para `1: 'c'` nadpisuje wcześniejszą `1: 'a'`. Pozycja klucza `1` pozostaje ta, z której został po raz pierwszy wstawiony.

#### Q. Co się stanie, gdy funkcja rekurencyjna nie ma warunku bazowego i wywołuje samą siebie bez końca?

* [ ] Python zamieni ją automatycznie na pętlę
* [ ] Program będzie działał w nieskończoność
* [ ] Funkcja w końcu zwróci `None`
* [x] Zostanie zgłoszony `RecursionError`

> **Wyjaśnienie:** Każde wywołanie odkłada ramkę na stos, a Python ma limit głębokości (domyślnie 1000). Python nie optymalizuje rekurencji ogonowej, więc po przekroczeniu limitu zgłasza `RecursionError`.

#### Q. Co wypisze ten program?

```python
def odlicz(n):
    if n == 0:
        return
    print(n, end=" ")
    odlicz(n - 1)
    print(n, end=" ")

odlicz(3)
```

* [ ] `3 2 1`
* [ ] `1 2 3 3 2 1`
* [ ] `3 2 1 0 1 2 3`
* [x] `3 2 1 1 2 3`

> **Wyjaśnienie:** Pierwszy `print` wykonuje się podczas schodzenia w głąb (3, 2, 1), a drugi dopiero przy powrocie z wywołań, czyli w odwrotnej kolejności (1, 2, 3). Dla `n == 0` funkcja nic nie wypisuje.

#### Q. Ile ruchów wykona rekurencyjne rozwiązanie problemu wież Hanoi dla 5 krążków?

* [ ] 32
* [ ] 25
* [x] 31
* [ ] 16

> **Wyjaśnienie:** Liczba ruchów wynosi 2ⁿ − 1, bo dla n krążków przenosimy dwa razy wieżę n − 1 krążków i raz największy krążek. Dla 5 krążków daje to 2⁵ − 1 = 31.

#### Q. Dlaczego `@lru_cache` tak bardzo przyspiesza naiwną rekurencyjną funkcję Fibonacciego?

* [x] Zapamiętuje wyniki, więc każdy wyraz jest liczony tylko raz
* [ ] Zamienia rekurencję na pętlę podczas kompilacji
* [ ] Uruchamia kolejne wywołania rekurencyjne równolegle w osobnych wątkach
* [ ] Zwiększa limit głębokości rekurencji interpretera

> **Wyjaśnienie:** Naiwna wersja liczy te same podproblemy wielokrotnie, co daje złożoność wykładniczą. Memoizacja przez `lru_cache` zwraca zapamiętany wynik dla powtórzonych argumentów, więc złożoność spada do liniowej.

#### Q. Co wypisze ten program?

```python
lista = [3, 1, 2]
wynik = lista.sort()
print(wynik, lista)
```

* [ ] `[1, 2, 3] [3, 1, 2]`
* [ ] `[1, 2, 3] [1, 2, 3]`
* [x] `None [1, 2, 3]`
* [ ] `None [3, 1, 2]`

> **Wyjaśnienie:** `list.sort()` sortuje listę w miejscu i zwraca `None`. Nową posortowaną listę bez zmiany oryginału tworzy funkcja `sorted()`.

#### Q. Co wypisze ten program?

```python
slowa = ["kot", "ul", "pies", "as", "ab"]
print(sorted(slowa, key=len))
```

* [ ] `['ab', 'as', 'ul', 'kot', 'pies']`
* [x] `['ul', 'as', 'ab', 'kot', 'pies']`
* [ ] `['ab', 'as', 'kot', 'pies', 'ul']`
* [ ] `['pies', 'kot', 'ul', 'as', 'ab']`

> **Wyjaśnienie:** Sortowanie odbywa się tylko według długości, a `sorted()` (Timsort) jest stabilny: elementy o równym kluczu zachowują pierwotną kolejność. Dlatego `ul`, `as`, `ab` nie są ustawiane alfabetycznie.

#### Q. Jaka jest złożoność czasowa sortowania szybkiego (quicksort) w najgorszym przypadku?

* [ ] O(n log n)
* [ ] O(n)
* [x] O(n²)
* [ ] O(log n)

> **Wyjaśnienie:** Średnio quicksort działa w czasie O(n log n), ale przy złym wyborze pivota (np. pierwszy element już posortowanej listy) każdy podział odcina tylko jeden element, co daje O(n²).

#### Q. Co wypisze ten program?

```python
import bisect

liczby = [1, 3, 5, 5, 7]
print(bisect.bisect_left(liczby, 5), bisect.bisect_right(liczby, 5))
```

* [ ] `2 3`
* [x] `2 4`
* [ ] `3 4`
* [ ] `2 2`

> **Wyjaśnienie:** `bisect_left` zwraca pozycję przed pierwszą piątką (indeks 2), a `bisect_right` pozycję za ostatnią piątką (indeks 4). Obie pozycje zachowują porządek listy po wstawieniu.
