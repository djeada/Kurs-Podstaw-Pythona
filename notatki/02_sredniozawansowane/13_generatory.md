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
gen2 = simple_generator()

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
