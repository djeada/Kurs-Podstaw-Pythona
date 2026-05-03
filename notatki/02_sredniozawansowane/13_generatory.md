## Generatory

Generator to specjalny rodzaj funkcji w Pythonie, który umożliwia zwracanie wartości pojedynczo zamiast wszystkich naraz, tak jak w przypadku listy lub innego iterowalnego obiektu. Dzięki temu generatory są bardziej wydajne pod względem zużycia pamięci, ponieważ nie muszą przechowywać całej kolekcji wartości w pamięci od razu. Zamiast tego, generują one wartości na bieżąco w miarę ich potrzeby. To sprawia, że są one idealne do przetwarzania dużych zbiorów danych, które nie mieszczą się w pamięci operacyjnej.

### Przykłady użycia generatorów

Aby utworzyć generator, używa się słowa kluczowego `yield` zamiast `return`. Każde wystąpienie słowa kluczowego `yield` w ciele funkcji określa wartość, którą generator ma zwrócić.

#### Prosty generator

W poniższym kodzie funkcja `foo()` jest generatorem, który zwraca trzy wartości.

```python
def foo():
  yield 1
  yield 2
  yield 3

for val in foo():
    print(val)
```

Wynik:

```
1
2
3
```

Można również przekształcić generator w listę:

```python
print(list(foo()))
```

Wynik:

```
[1, 2, 3]
```

b) Zwracanie wartości przy pomocy return:

Dla porównania, tradycyjne funkcje używają return do zwracania wartości. Jednak tylko pierwsze wystąpienie return jest wykonane, a pozostałe linie kodu po nim są traktowane jako martwy kod.

```python
def bar():
  return 1
  return 2  # Martwy kod, nie zostanie wykonany
  return 3  # Martwy kod, nie zostanie wykonany

print(bar())
```

Wynik:

```
1
```

Generatory są potężnym narzędziem, pozwalającym na tworzenie efektywnych pod względem pamięci i elastycznych rozwiązań dla wielu problemów związanych z przetwarzaniem danych.

#### Generator tworzący sekwencje liczb

```python
def range_generator(n):
    i = 0
    while i < n:
        yield i
        i += 1

for number in range_generator(5):
    print(number)
```

Wynik:

```
0
1
2
3
4
```

### Generatory a Wyrażenia Listowe

Python oferuje składnię tzw. "generator comprehensions", która jest bardzo podobna do wyrażeń listowych (ang. list comprehensions), ale zamiast tworzyć listy, tworzy generatory.

Przykład:

```python
gen = (i**2 for i in range(5))

for val in gen:
    print(val)
```

Wynik:

```
0
1
4
9
16
```

#### Wbudowane Funkcje Wspierające Generatory

- `itertools`: Moduł ten oferuje wiele użytecznych narzędzi do tworzenia i manipulowania iteratorami.
- `next(generator, default)`: Pobiera następną wartość z generatora. Jeśli generator jest pusty, zwraca wartość domyślną.
- `yield from`: Umożliwia delegowanie części wartości do innego generatora.

Przykład użycia `yield from`:

```python
def chain_generators(*iterables):
    for iterable in iterables:
        yield from iterable

gen1 = range(3)
gen2 = foo()

for val in chain_generators(gen1, gen2):
    print(val)
```

Wynik:

```
0
1
2
1
2
3
```

### Zastosowania i korzyści z używania generatorów

- Generatory zużywają mniej pamięci, ponieważ generują wartości na bieżąco.
- Oszczędność czasu, gdy nie musimy czekać, aż wszystkie wartości zostaną wygenerowane.
- Można łatwo tworzyć potoki przetwarzania danych, łącząc kilka generatorów razem.

W praktyce, generatory są niezbędnym narzędziem dla programistów Pythona, umożliwiając tworzenie kodu bardziej wydajnego i zwięzłego.

### Metody `send()`, `throw()` i `close()`

Generator to nie tylko prosta sekwencja — to pełnoprawny współprogramu (ang. *coroutine*). Poniżej opisano trzy metody sterowania generatorem:

#### `send(value)` — wysłanie wartości do generatora

`send()` wznawia generator i przekazuje do niego wartość jako wynik wyrażenia `yield`:

```python
def akumulator():
    suma = 0
    while True:
        wartosc = yield suma   # yield zwraca sumę, przyjmuje nową wartość
        if wartosc is None:
            break
        suma += wartosc

gen = akumulator()
next(gen)          # Uruchomienie generatora (do pierwszego yield)
print(gen.send(10))  # 10
print(gen.send(5))   # 15
print(gen.send(20))  # 35
gen.close()
```

#### `throw(type)` — wysłanie wyjątku do generatora

```python
def generator_z_obsluga():
    try:
        while True:
            yield "pracuję"
    except ValueError as e:
        print(f"Generator otrzymał wyjątek: {e}")
        yield "zakończono bezpiecznie"

gen = generator_z_obsluga()
print(next(gen))                    # pracuję
print(next(gen))                    # pracuję
print(gen.throw(ValueError, "stop")) # Generator otrzymał wyjątek: stop
                                     # zakończono bezpiecznie
```

#### `close()` — zamknięcie generatora

`close()` wysyła do generatora wyjątek `GeneratorExit`, co pozwala na sprzątanie zasobów:

```python
def generator_z_zamknieciem():
    try:
        while True:
            yield "dane"
    except GeneratorExit:
        print("Generator zamknięty — sprzątam zasoby")

gen = generator_z_zamknieciem()
next(gen)
gen.close()   # Generator zamknięty — sprzątam zasoby
```

### Nieskończone generatory

Generatory mogą produkować nieskończone sekwencje — istotne jest tylko, żeby pobierać z nich elementy za pomocą `next()` lub ograniczać iterację:

```python
def liczby_naturalne():
    n = 1
    while True:
        yield n
        n += 1

gen = liczby_naturalne()
print([next(gen) for _ in range(5)])  # [1, 2, 3, 4, 5]

# Bezpieczne pobranie pierwszych 10
import itertools
print(list(itertools.islice(liczby_naturalne(), 10)))  # [1, 2, ..., 10]
```

### Moduł `itertools` — gotowe generatory

Moduł `itertools` dostarcza wysoko wydajnych generatorów do typowych zadań:

#### Nieskończone iteratory

```python
import itertools

# count(start, step) — nieograniczona sekwencja liczb
for i in itertools.islice(itertools.count(5, 2), 5):
    print(i)   # 5, 7, 9, 11, 13

# cycle(iterable) — nieskończone powtarzanie sekwencji
kolory = itertools.cycle(["czerwony", "zielony", "niebieski"])
for _, kolor in zip(range(7), kolory):
    print(kolor)   # czerwony, zielony, niebieski, czerwony, ...

# repeat(value, n) — powtórz wartość n razy (lub nieskończenie)
print(list(itertools.repeat("echo", 3)))   # ['echo', 'echo', 'echo']
```

#### Kończące iteratory

```python
import itertools

# chain — łączenie kilku iterowalnych w jeden strumień
print(list(itertools.chain([1, 2], [3, 4], [5])))  # [1, 2, 3, 4, 5]

# islice — wycinek iteratora
print(list(itertools.islice(range(100), 2, 10, 2)))  # [2, 4, 6, 8]

# takewhile / dropwhile — pobieraj/pomijaj dopóki warunek prawdziwy
dane = [1, 3, 5, 2, 7, 4]
print(list(itertools.takewhile(lambda x: x < 4, dane)))   # [1, 3]
print(list(itertools.dropwhile(lambda x: x < 4, dane)))   # [2, 7, 4]

# compress — filtrowanie elementów przez maskę
print(list(itertools.compress("ABCDE", [1, 0, 1, 0, 1])))  # ['A', 'C', 'E']
```

#### Kombinatoryczne iteratory

```python
import itertools

# product — iloczyn kartezjański
print(list(itertools.product("AB", [1, 2])))
# [('A', 1), ('A', 2), ('B', 1), ('B', 2)]

# permutations — permutacje bez powtórzeń
print(list(itertools.permutations([1, 2, 3], 2)))
# [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]

# combinations — kombinacje bez powtórzeń
print(list(itertools.combinations([1, 2, 3, 4], 2)))
# [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
```

### Potok generatorów (pipeline)

Generatory można łączyć w łańcuchy — każdy generator przetwarza dane wyjściowe poprzedniego, tworząc wydajny potok:

```python
def czytaj_linie(plik):
    with open(plik) as f:
        yield from f

def filtruj_puste(linie):
    for linia in linie:
        if linia.strip():
            yield linia

def zamien_na_wielkie(linie):
    for linia in linie:
        yield linia.upper()

# Budowanie potoku (lazy — żadne dane nie są ładowane do pamięci)
# linie = czytaj_linie("plik.txt")
# niepuste = filtruj_puste(linie)
# wielkie = zamien_na_wielkie(niepuste)
# for linia in wielkie:
#     print(linia)
```

Potok generatorów jest szczególnie wydajny przy przetwarzaniu dużych plików, bo każda linia jest przetwarzana jeden raz, bez wczytywania całego pliku do pamięci.
