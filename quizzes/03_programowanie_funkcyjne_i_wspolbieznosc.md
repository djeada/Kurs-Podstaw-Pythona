# Programowanie funkcyjne i współbieżność — quiz

Notatki: [Lambdy](../notatki/02_sredniozawansowane/10_lambdy.md), [Programowanie funkcyjne](../notatki/02_sredniozawansowane/11_programowanie_funkcyjne.md), [Generatory](../notatki/02_sredniozawansowane/13_generatory.md), [Iteratory](../notatki/02_sredniozawansowane/14_iteratory.md), [Dekoratory](../notatki/02_sredniozawansowane/15_dekoratory.md), [Wątki](../notatki/02_sredniozawansowane/07_watki.md), [Procesy](../notatki/02_sredniozawansowane/08_procesy.md), [Asyncio](../notatki/02_sredniozawansowane/09_asyncio.md)

Sprawdź, czy rozumiesz lambdy, `map`/`filter`/`reduce`, generatory, iteratory, dekoratory, wątki, procesy i `asyncio`.

#### Q. Co wypisze ten program?

```python
f = lambda x, y=2: x ** y
print(f(3), f(2, 3))
```

* [ ] `6 6`
* [x] `9 8`
* [ ] `9 9`
* [ ] `8 9`

> **Wyjaśnienie:** Lambda może mieć parametry z wartościami domyślnymi, tak jak zwykła funkcja. `f(3)` liczy $3^2$, a `f(2, 3)` nadpisuje `y` i liczy $2^3$.

#### Q. Co wypisze ten program?

```python
funkcje = [lambda: i for i in range(3)]
print([f() for f in funkcje])
```

* [ ] `[0, 1, 2]`
* [x] `[2, 2, 2]`
* [ ] `[0, 0, 0]`
* [ ] Zgłosi `NameError`

> **Wyjaśnienie:** Lambda zapamiętuje zmienną `i`, a nie jej wartość z chwili utworzenia. Wszystkie trzy funkcje są wywoływane po zakończeniu pętli, gdy `i` wynosi już 2; pomaga np. `lambda i=i: i`.

#### Q. Czego nie można umieścić w ciele funkcji lambda?

* [ ] Wyrażenia warunkowego `a if w else b`
* [ ] Wywołania innej funkcji
* [x] Pętli `for` zapisanej jako instrukcja
* [ ] Odwołania do zmiennej spoza lambdy

> **Wyjaśnienie:** Ciało lambdy to jedno wyrażenie, więc nie mogą się w nim znaleźć instrukcje takie jak pętla `for` czy przypisanie `=` (dozwolone jest tylko wyrażenie przypisania `:=`). Wyrażenie warunkowe i wywołania funkcji są wyrażeniami, więc są dozwolone.

#### Q. Co wypisze ten program?

```python
from functools import partial

def potega(podstawa, wykladnik):
    return podstawa ** wykladnik

szescian = partial(potega, wykladnik=3)
print(szescian(2), szescian(podstawa=3))
```

* [x] `8 27`
* [ ] `9 27`
* [ ] `8 9`
* [ ] Zgłosi `TypeError`

> **Wyjaśnienie:** `partial` tworzy nową funkcję z „zamrożonym” argumentem `wykladnik=3`. Brakujący argument `podstawa` można podać pozycyjnie albo po nazwie.

#### Q. Co wypisze ten program?

```python
m = map(lambda x: x * 10, [1, 2, 3])
print(list(m), list(m))
```

* [ ] `[10, 20, 30] [10, 20, 30]`
* [x] `[10, 20, 30] []`
* [ ] `[] []`
* [ ] `<map object> <map object>`

> **Wyjaśnienie:** `map()` zwraca leniwy iterator, a nie listę. Pierwsze `list(m)` go wyczerpuje, więc drugie nie dostaje już żadnych elementów.

#### Q. Co wypisze ten program?

```python
print(list(filter(None, [0, 1, "", "a", None, [], [0]])))
```

* [ ] `[0, 1, "", "a", None, [], [0]]`
* [ ] `[1, 'a']`
* [x] `[1, 'a', [0]]`
* [ ] `[0, '', None, []]`

> **Wyjaśnienie:** `filter(None, ...)` zostawia tylko elementy prawdziwe w kontekście logicznym. `[0]` to niepusta lista, więc przechodzi, choć zawiera zero.

#### Q. Co wypisze ten program?

```python
from functools import reduce

print(reduce(lambda a, b: a * 10 + b, [1, 2, 3]), reduce(lambda a, b: a + b, [], 0))
```

* [ ] `6 0`
* [ ] `123 None`
* [x] `123 0`
* [ ] `321 0`

> **Wyjaśnienie:** `reduce` przekazuje dotychczasowy wynik jako pierwszy argument: $(1 \cdot 10 + 2) \cdot 10 + 3 = 123$. Dla pustej listy zwraca podaną wartość początkową; bez niej zgłosiłby `TypeError`.

#### Q. Co wypisze ten program?

```python
from functools import reduce

def zloz(*funkcje):
    return reduce(lambda f, g: lambda x: f(g(x)), funkcje)

dodaj_1 = lambda x: x + 1
podwoj = lambda x: x * 2
print(zloz(dodaj_1, podwoj)(5), zloz(podwoj, dodaj_1)(5))
```

* [ ] `12 11`
* [ ] `11 11`
* [ ] `12 12`
* [x] `11 12`

> **Wyjaśnienie:** `zloz(f, g)(x)` to `f(g(x))`, więc funkcje działają od prawej do lewej. Pierwsze złożenie liczy `5 * 2 + 1`, a drugie `(5 + 1) * 2`.

#### Q. Co wypisze ten program?

```python
print(list(map(lambda x, y: x + y, [1, 2, 3], [10, 20])))
```

* [x] `[11, 22]`
* [ ] `[11, 22, 3]`
* [ ] `[11, 22, 33]`
* [ ] Zgłosi `TypeError`

> **Wyjaśnienie:** `map` z kilkoma kolekcjami pobiera po jednym elemencie z każdej i kończy pracę, gdy wyczerpie się najkrótsza, podobnie jak `zip`.

#### Q. Co wypisze ten program?

```python
def gen():
    print("start")
    yield 1
    print("koniec")

g = gen()
print("utworzony")
print(next(g))
```

* [ ] `start`, `utworzony`, `1`
* [x] `utworzony`, `start`, `1`
* [ ] `utworzony`, `start`, `1`, `koniec`
* [ ] `start`, `1`, `koniec`, `utworzony`

> **Wyjaśnienie:** Wywołanie funkcji generatora tylko tworzy obiekt generatora i nie wykonuje ciała. Kod startuje przy pierwszym `next()` i zatrzymuje się na `yield`, więc `koniec` nigdy się nie wypisze.

#### Q. Co wypisze ten program?

```python
g = (x * x for x in range(3))
print(sum(g), sum(g))
```

* [ ] `5 5`
* [ ] `14 0`
* [x] `5 0`
* [ ] `0 5`

> **Wyjaśnienie:** Wyrażenie generatorowe daje wartości 0, 1, 4, ale można je przejść tylko raz. Drugie `sum()` dostaje wyczerpany generator i zwraca 0.

#### Q. Co wypisze ten program?

```python
def a():
    yield 1
    yield 2

def b():
    yield 0
    yield from a()
    yield 3

print(list(b()))
```

* [ ] `[0, <generator object a>, 3]`
* [ ] `[0, 3]`
* [ ] `[0, [1, 2], 3]`
* [x] `[0, 1, 2, 3]`

> **Wyjaśnienie:** `yield from` deleguje iterację do innego generatora i przekazuje dalej każdą jego wartość. Bez `from` (`yield a()`) generator zwróciłby sam obiekt generatora.

#### Q. Co wypisze ten program?

```python
def akumulator():
    suma = 0
    while True:
        x = yield suma
        suma += x

g = akumulator()
next(g)
g.send(5)
print(g.send(10))
```

* [ ] `10`
* [x] `15`
* [ ] `5`
* [ ] `None`

> **Wyjaśnienie:** Pierwsze `next()` uruchamia generator do pierwszego `yield`. Każde `send(v)` wznawia go, wstawiając `v` jako wynik wyrażenia `yield`, i zwraca kolejną wartość, czyli sumę dotychczasowych danych.

#### Q. Co wypisze ten program?

```python
g = (x for x in [])
print(bool(g), next(g, "brak"))
```

* [ ] `False brak`
* [x] `True brak`
* [ ] `False None`
* [ ] Zgłosi `StopIteration`

> **Wyjaśnienie:** Obiekt generatora jest zawsze prawdziwy, nawet gdy nie wyprodukuje żadnej wartości, więc `if gen:` nie sprawdza pustości. `next()` z drugim argumentem zwraca wartość domyślną zamiast zgłaszać `StopIteration`.

#### Q. Co wypisze ten program?

```python
import itertools

dane = [1, 4, 2, 6, 3]
print(list(itertools.takewhile(lambda x: x < 5, dane)), list(itertools.dropwhile(lambda x: x < 5, dane)))
```

* [ ] `[1, 4, 2, 3] [6]`
* [x] `[1, 4, 2] [6, 3]`
* [ ] `[1, 4, 2] [6]`
* [ ] `[1] [4, 2, 6, 3]`

> **Wyjaśnienie:** `takewhile` pobiera elementy do pierwszego, który nie spełnia warunku, a `dropwhile` pomija elementy do tego momentu i zwraca całą resztę. Żadna z funkcji nie filtruje: `3` za szóstką nie jest już sprawdzane.

#### Q. Co wypisze ten program?

```python
import itertools

print([k for k, _ in itertools.groupby("aabbbac")])
```

* [ ] `['a', 'b', 'c']`
* [ ] `['a', 'b', 'c', 'a']`
* [x] `['a', 'b', 'a', 'c']`
* [ ] `['aa', 'bbb', 'a', 'c']`

> **Wyjaśnienie:** `groupby` grupuje tylko sąsiadujące elementy o tym samym kluczu, więc pojedyncze `a` po `bbb` tworzy nową grupę. Aby zgrupować wszystkie takie same wartości, dane trzeba najpierw posortować.

#### Q. Co wypisze ten program?

```python
class Odliczanie:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.n <= 0:
            raise StopIteration
        self.n -= 1
        return self.n + 1

o = Odliczanie(3)
print(list(o), list(o))
```

* [ ] `[3, 2, 1] [3, 2, 1]`
* [ ] `[2, 1, 0] []`
* [x] `[3, 2, 1] []`
* [ ] `[3, 2, 1] [0]`

> **Wyjaśnienie:** `__iter__` zwraca `self`, więc obiekt jest jednocześnie iteratorem i przechowuje stan przejścia. Po pierwszym przebiegu `n` wynosi 0; wielokrotną iterację daje dopiero tworzenie nowego iteratora w `__iter__`.

#### Q. Które dwie metody tworzą protokół iteratora w Pythonie?

* [x] `__iter__` i `__next__`
* [ ] `__iter__` i `__len__`
* [ ] `__getitem__` i `__len__`
* [ ] `__next__` i `__call__`

> **Wyjaśnienie:** Iterator musi mieć `__iter__` (zwykle zwracające `self`) oraz `__next__`, które zwraca kolejny element albo zgłasza `StopIteration`. Właśnie z nich korzysta pętla `for`.

#### Q. Co wypisze ten program?

```python
pary = [(1, "a"), (2, "b")]
liczby, litery = zip(*pary)
print(liczby, litery)
```

* [ ] `[1, 2] ['a', 'b']`
* [ ] `(1, 'a') (2, 'b')`
* [x] `(1, 2) ('a', 'b')`
* [ ] Zgłosi `ValueError`

> **Wyjaśnienie:** `zip(*pary)` rozpakowuje listę par jako osobne argumenty, czyli działa jak `zip((1, "a"), (2, "b"))`. W efekcie transponuje dane i zwraca krotki.

#### Q. Co wypisze ten program?

```python
it = iter([1, 2, 3, 4])
print(3 in it, list(it))
```

* [ ] `True [1, 2, 3, 4]`
* [ ] `True []`
* [ ] `False [4]`
* [x] `True [4]`

> **Wyjaśnienie:** Operator `in` na iteratorze pobiera kolejne elementy, aż znajdzie szukany, więc zużywa 1, 2 i 3. Do `list(it)` zostaje już tylko 4.

#### Q. Co wypisze ten program?

```python
def nawias(f):
    def wew():
        return "(" + f() + ")"
    return wew

def gwiazdka(f):
    def wew():
        return "*" + f() + "*"
    return wew

@nawias
@gwiazdka
def tekst():
    return "x"

print(tekst())
```

* [x] `(*x*)`
* [ ] `*(x)*`
* [ ] `(x)`
* [ ] `*x*`

> **Wyjaśnienie:** Dekoratory stosuje się od dołu: zapis jest równoważny `tekst = nawias(gwiazdka(tekst))`. Zewnętrzny `nawias` opakowuje wynik, który już zawiera gwiazdki.

#### Q. Co wypisze ten program?

```python
import functools

def bez(f):
    def wew(*a):
        return f(*a)
    return wew

def z(f):
    @functools.wraps(f)
    def wew(*a):
        return f(*a)
    return wew

@bez
def alfa():
    pass

@z
def beta():
    pass

print(alfa.__name__, beta.__name__)
```

* [ ] `alfa beta`
* [ ] `wew wew`
* [x] `wew beta`
* [ ] `alfa wew`

> **Wyjaśnienie:** Dekorator zastępuje funkcję obiektem `wew`, więc bez dodatkowych kroków nazwa i dokumentacja oryginału giną. `functools.wraps` kopiuje te metadane z dekorowanej funkcji.

#### Q. Co wypisze ten program?

```python
def dekoruj(f):
    def wew(*args):
        f(*args)
    return wew

@dekoruj
def dodaj(a, b):
    return a + b

print(dodaj(2, 3))
```

* [ ] `5`
* [x] `None`
* [ ] `wew`
* [ ] Zgłosi `TypeError`

> **Wyjaśnienie:** Funkcja `wew` wywołuje oryginał, ale nie zwraca jego wyniku, więc zwraca `None`. W dekoratorze trzeba pisać `return f(*args, **kwargs)`.

#### Q. Co wypisze ten program?

```python
def powtorz(n):
    def dekorator(f):
        def wew():
            return [f() for _ in range(n)]
        return wew
    return dekorator

@powtorz(3)
def hej():
    return "hej"

print(hej())
```

* [ ] `hejhejhej`
* [x] `['hej', 'hej', 'hej']`
* [ ] `['hej']`
* [ ] Zgłosi `TypeError`

> **Wyjaśnienie:** `powtorz(3)` zwraca właściwy dekorator, który zostaje zastosowany do `hej`. Dekorator z argumentami to więc funkcja zwracająca dekorator, a nie sam dekorator.

#### Q. Co wypisze ten program?

```python
def rejestruj(f):
    print("rejestruję", f.__name__)
    return f

@rejestruj
def a():
    print("a")

print("start")
a()
```

* [ ] `start`, `rejestruję a`, `a`
* [ ] `start`, `a`
* [x] `rejestruję a`, `start`, `a`
* [ ] `start`, `a`, `rejestruję a`

> **Wyjaśnienie:** Kod dekoratora wykonuje się w chwili definicji funkcji, a nie przy jej wywołaniu. Na tym opierają się dekoratory rejestrujące, np. `@app.route` we Flasku.

#### Q. Dlaczego w CPython 3.12 (bez trybu free-threading) wiele wątków nie przyspiesza obliczeń intensywnie korzystających z CPU?

* [ ] Bo system operacyjny zawsze przydziela wątki Pythona do jednego rdzenia
* [ ] Bo każdy wątek kopiuje całą pamięć procesu
* [x] Bo GIL pozwala wykonywać kod bajtowy tylko jednemu wątkowi naraz
* [ ] Bo moduł `threading` uruchamia wątki jeden po drugim

> **Wyjaśnienie:** Global Interpreter Lock sprawia, że w danej chwili tylko jeden wątek wykonuje kod Pythona. Wątki pomagają przy I/O, bo GIL jest zwalniany podczas oczekiwania; do obliczeń lepsze są procesy.

#### Q. Co wypisze ten program?

```python
import threading

licznik = 0
blokada = threading.Lock()

def praca():
    global licznik
    for _ in range(10000):
        with blokada:
            licznik += 1

watki = [threading.Thread(target=praca) for _ in range(4)]
for w in watki:
    w.start()
for w in watki:
    w.join()
print(licznik)
```

* [ ] `10000`
* [ ] Losową wartość mniejszą niż `40000`
* [ ] `0`
* [x] `40000`

> **Wyjaśnienie:** Blokada sprawia, że tylko jeden wątek naraz wykonuje `licznik += 1`, więc żadna inkrementacja nie ginie. `join()` czeka na wszystkie wątki przed wypisaniem wyniku.

#### Q. Co wypisze ten program?

```python
from concurrent.futures import ThreadPoolExecutor
import time

def zadanie(n):
    time.sleep(0.1 * (3 - n))
    return n

with ThreadPoolExecutor(max_workers=3) as ex:
    print(list(ex.map(zadanie, [0, 1, 2])))
```

* [ ] `[2, 1, 0]`
* [x] `[0, 1, 2]`
* [ ] Kolejność zależy od tego, który wątek skończy pierwszy
* [ ] `[0, 2, 1]`

> **Wyjaśnienie:** `executor.map` zwraca wyniki w kolejności danych wejściowych, nawet jeśli zadania kończą się w innej kolejności. Wyniki w kolejności kończenia daje `as_completed`.

#### Q. Co się stanie, gdy zamiast `watek.start()` wywołasz `watek.run()`?

* [ ] Wątek uruchomi się dwa razy szybciej
* [x] Kod wykona się w bieżącym wątku, bez współbieżności
* [ ] Python zgłosi `RuntimeError`, bo `run` jest prywatne
* [ ] Wątek zostanie uruchomiony w osobnym procesie

> **Wyjaśnienie:** `run()` to zwykła metoda z kodem wątku. Dopiero `start()` tworzy nowy wątek systemowy, który wywołuje `run()`; bezpośrednie wywołanie działa synchronicznie.

#### Q. Co wypisze ten program?

```python
import multiprocessing

lista = []

def dodaj():
    lista.append(1)

if __name__ == "__main__":
    p = multiprocessing.Process(target=dodaj)
    p.start()
    p.join()
    print(lista)
```

* [x] `[]`
* [ ] `[1]`
* [ ] `[1, 1]`
* [ ] Zgłosi `PicklingError`

> **Wyjaśnienie:** Każdy proces ma własną przestrzeń adresową, więc proces potomny zmienia swoją kopię listy. Do przekazania danych potrzebne są mechanizmy IPC, np. `Queue`, `Pipe` albo `Manager`.

#### Q. Dlaczego kod tworzący procesy umieszcza się w bloku `if __name__ == "__main__":`?

* [ ] Bo inaczej procesy nie mają dostępu do modułu `multiprocessing`
* [x] Bo przy `spawn` proces potomny importuje moduł główny od nowa
* [ ] Bo bez tego procesy uruchamiają się jako wątki w tym samym interpreterze
* [ ] Bo tylko w tym bloku można wywołać `join()`

> **Wyjaśnienie:** Przy metodzie uruchamiania `spawn` (domyślnej w Windows i macOS) proces potomny importuje skrypt od nowa. Bez warunku kod tworzący procesy wykonałby się ponownie w każdym dziecku, co `multiprocessing` przerywa błędem `RuntimeError`.

#### Q. Które narzędzie najlepiej przyspieszy w CPython obliczenia CPU-bound na wielu rdzeniach?

* [ ] `threading.Thread`
* [ ] `asyncio.gather`
* [x] `ProcessPoolExecutor`
* [ ] `ThreadPoolExecutor`

> **Wyjaśnienie:** Każdy proces ma własny interpreter i własny GIL, więc procesy mogą liczyć naprawdę równolegle. Wątki i `asyncio` dzielą jeden GIL, dlatego sprawdzają się przy operacjach I/O.

#### Q. Co wypisze ten program?

```python
import asyncio

async def f():
    return 42

x = f()
print(type(x).__name__)
x.close()
```

* [ ] `int`
* [x] `coroutine`
* [ ] `function`
* [ ] `Task`

> **Wyjaśnienie:** Wywołanie funkcji `async def` nie wykonuje jej ciała, tylko zwraca obiekt korutyny. Aby otrzymać 42, trzeba go uruchomić przez `await`, `asyncio.run()` lub zadanie.

#### Q. Co wypisze ten program?

```python
import asyncio

async def zadanie(n, t):
    await asyncio.sleep(t)
    return n

async def main():
    print(await asyncio.gather(zadanie(1, 0.3), zadanie(2, 0.1), zadanie(3, 0.2)))

asyncio.run(main())
```

* [ ] `[2, 3, 1]`
* [x] `[1, 2, 3]`
* [ ] `[3, 2, 1]`
* [ ] Kolejność jest losowa

> **Wyjaśnienie:** `asyncio.gather` uruchamia korutyny współbieżnie, ale zwraca wyniki w kolejności przekazania argumentów, a nie w kolejności zakończenia.

#### Q. Co wypisze ten program?

```python
import asyncio

async def praca(n, t):
    await asyncio.sleep(t)
    print(n, end=" ")

async def main():
    t1 = asyncio.create_task(praca("A", 0.2))
    t2 = asyncio.create_task(praca("B", 0.1))
    print("start", end=" ")
    await t1
    await t2

asyncio.run(main())
```

* [ ] `start A B`
* [ ] `A B start`
* [x] `start B A`
* [ ] `B A start`

> **Wyjaśnienie:** `create_task` planuje korutyny, ale `main` działa dalej i najpierw wypisuje `start`. Zadania czekają współbieżnie, więc krótsze `B` kończy się pierwsze, choć na `t1` czekamy wcześniej.

#### Q. Co się stanie, gdy w korutynie użyjesz `time.sleep(2)` zamiast `await asyncio.sleep(2)`?

* [x] Zablokuje całą pętlę zdarzeń, więc inne korutyny też będą czekać
* [ ] Wstrzyma tylko tę jedną korutynę, a pozostałe będą normalnie działać dalej
* [ ] Python zgłosi `SyntaxError` wewnątrz `async def`
* [ ] Pętla zdarzeń automatycznie przeniesie ją do osobnego wątku

> **Wyjaśnienie:** `time.sleep` blokuje cały wątek, a w nim działa pętla zdarzeń ze wszystkimi korutynami. `await asyncio.sleep` oddaje sterowanie pętli, która w tym czasie może wykonywać inne zadania.

#### Q. Co wypisze ten program?

```python
import asyncio
import time

async def main():
    start = time.perf_counter()
    await asyncio.sleep(0.2)
    await asyncio.sleep(0.3)
    a = time.perf_counter() - start

    start = time.perf_counter()
    await asyncio.gather(asyncio.sleep(0.2), asyncio.sleep(0.3))
    b = time.perf_counter() - start
    print(round(a, 1), round(b, 1))

asyncio.run(main())
```

* [ ] `0.5 0.5`
* [ ] `0.3 0.3`
* [x] `0.5 0.3`
* [ ] `0.3 0.5`

> **Wyjaśnienie:** Kolejne `await` czekają jedno po drugim, więc czasy się sumują. `gather` czeka współbieżnie, więc całość trwa tyle, ile najdłuższe zadanie.

#### Q. Ile wątków wykorzystuje pętla zdarzeń `asyncio` do wykonywania korutyn w typowym programie uruchomionym przez `asyncio.run()`?

* [ ] Po jednym wątku na każdą korutynę
* [ ] Tyle, ile procesor ma rdzeni
* [x] Jeden
* [ ] Dwa: jeden na I/O i jeden na obliczenia

> **Wyjaśnienie:** `asyncio` to współbieżność kooperatywna w jednym wątku: korutyny same oddają sterowanie przy `await`. Dlatego nie daje równoległości obliczeń i nie omija GIL przy zadaniach CPU-bound.

#### Q. Co wypisze ten program?

```python
import asyncio

async def ok():
    return 1

async def zle():
    raise ValueError("x")

async def main():
    print(await asyncio.gather(ok(), zle(), return_exceptions=True))

asyncio.run(main())
```

* [ ] Zgłosi nieobsłużony `ValueError`
* [ ] `[1]`
* [ ] `[1, None]`
* [x] `[1, ValueError('x')]`

> **Wyjaśnienie:** Z `return_exceptions=True` wyjątki są zwracane na liście wyników zamiast przerywać `gather`. Bez tej opcji pierwszy wyjątek zostałby zgłoszony w miejscu `await`.
