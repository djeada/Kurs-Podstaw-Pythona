## Iteratory

Iteratory to fundamentalny koncept w języku Python, szczególnie w kontekście pętli i struktur iterowalnych, takich jak listy, krotki czy zbiory. Python traktuje iteratory jako narzędzie do sukcesywnego uzyskiwania kolejnych elementów z kolekcji danych w sposób zorganizowany, z możliwością zatrzymania i wznowienia procesu iteracji. W tej rozbudowanej wersji omówimy, jak działają iteratory, jak je tworzyć, oraz jak są wykorzystywane przez różne mechanizmy Pythonowe, takie jak pętla `for` oraz generatory.

### Pojęcie iterowalności

W Pythonie obiekt jest **iterowalny** (ang. *iterable*), jeśli można po nim iterować, tj. można sukcesywnie uzyskiwać kolejne elementy. Obiekty te muszą implementować metodę `__iter__()`, która zwraca **iterator**. Iterator jest obiektem, który realizuje protokół iteratora, to znaczy posiada metodę `__next__()`, która zwraca kolejny element w sekwencji.

Typowe struktury danych, takie jak listy, krotki, zbiory czy słowniki, są iterowalne, co pozwala na użycie pętli `for` do iteracji nad ich elementami. W tle działa tutaj mechanizm oparty na iteratorach.

#### Iteracja przez listę

```python
for elem in [1, 2, 3]:
    print(elem)
```

Powyższa pętla `for` w rzeczywistości wywołuje na liście metodę `__iter__()`, która zwraca iterator. Iterator ten posiada metodę `__next__()`, która jest wywoływana w każdej iteracji w celu uzyskania kolejnego elementu listy.

### Przykład ręcznego użycia iteratora

Możemy bezpośrednio pracować z iteratorem, korzystając z funkcji wbudowanej `iter()` oraz metody `next()`.

```python
lista = [1, 2, 3]
iterator = iter(lista)  # Tworzy iterator z listy
print(next(iterator))   # 1
print(next(iterator))   # 2
print(next(iterator))   # 3
# Kolejne wywołanie `next()` wyrzuci wyjątek StopIteration
```

Kiedy iterator nie ma już kolejnych elementów do zwrócenia, wywołanie `next()` powoduje wygenerowanie wyjątku `StopIteration`. Jest to sygnał dla pętli `for`, aby zakończyć iterację.

### Protokół iteratora

Protokół iteratora w Pythonie składa się z dwóch kluczowych metod:

- `__iter__()`: Zwraca obiekt iteratora, zazwyczaj zwraca `self`.
- `__next__()`: Zwraca kolejny element w sekwencji, a gdy elementów brak, generuje wyjątek `StopIteration`.

Zrozumienie tych metod jest kluczowe, jeśli chcemy definiować własne iteratory.

### Tworzenie własnych iteratorów

Aby stworzyć własny iterator, konieczne jest zdefiniowanie klasy z implementacją metod `__iter__()` i `__next__()`. Przykład klasy będącej iteratorem:

```python
class MojaKolekcja:
    def __init__(self):
        self.elementy = [1, 2, 3]
        self.indeks = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.indeks < len(self.elementy):
            wynik = self.elementy[self.indeks]
            self.indeks += 1
            return wynik
        else:
            raise StopIteration

kolekcja = MojaKolekcja()
for elem in kolekcja:
    print(elem)
```

Działanie powyższego przykładu:

1. Metoda `__iter__()` zwraca referencję do samego siebie, co oznacza, że instancja klasy jest także swoim własnym iteratorem.
2. Metoda `__next__()` zwraca kolejny element z listy, a gdy wszystkie elementy zostaną wyczerpane, rzuca wyjątek `StopIteration`, kończąc iterację.

### Teoretyczne uzasadnienie iteratorów

Iteratory w Pythonie opierają się na koncepcji **leniwej ewaluacji** (ang. *lazy evaluation*). W przeciwieństwie do standardowych kolekcji, które przechowują wszystkie swoje elementy w pamięci, iterator nie generuje elementów z góry, ale produkuje je na żądanie. Pozwala to na efektywne wykorzystanie pamięci, zwłaszcza w przypadku dużych kolekcji danych lub nieskończonych sekwencji.

Matematycznie iteratory można postrzegać jako funkcje, które na każdym kroku zwracają kolejny element z pewnej sekwencji, bez potrzeby przechowywania jej pełnej reprezentacji w pamięci. Dzięki temu możliwa jest np. praca z nieskończonymi sekwencjami.

### Generatory jako iteratory

**Generatory** są specjalnym rodzajem iteratorów, które są definiowane za pomocą funkcji wykorzystujących słowo kluczowe `yield`. Generatory upraszczają proces tworzenia iteratorów, automatycznie zarządzając stanem iteracji i rzucaniem wyjątku `StopIteration` po zakończeniu iteracji.

Przykład prostego generatora:

```python
def generator_liczb():
    for i in range(3):
        yield i

for liczba in generator_liczb():
    print(liczba)
```

Wyjaśnienie działania generatorów:

1. Każde wywołanie `yield` zatrzymuje wykonanie funkcji i zwraca wartość. Wznowienie następuje w miejscu, w którym funkcja została przerwana.
2. Generator zachowuje swój stan pomiędzy kolejnymi wywołaniami, co czyni go bardzo efektywnym przy implementacji złożonych iteracji.

### Wyjątek `StopIteration` w praktyce

Każdy iterator po wyczerpaniu swoich elementów rzuca wyjątek `StopIteration`, który informuje o zakończeniu iteracji. Jest to mechanizm kontrolny, który pozwala pętlom `for` automatycznie wykrywać, kiedy przestać iterować.

Pętla `for` automatycznie obsługuje wyjątek `StopIteration` i przerywa iterację, co czyni ten mechanizm intuicyjnym i łatwym w użyciu. Jeśli jednak korzystamy z iteracji ręcznie za pomocą `next()`, musimy sami zadbać o odpowiednią obsługę wyjątku.

```python
iterator = iter([1, 2, 3])
while True:
    try:
        element = next(iterator)
        print(element)
    except StopIteration:
        break
```

### Korzyści z używania iteratorów

- Iteratory są efektywne pamięciowo, ponieważ generują elementy na żądanie, a nie przechowują całej kolekcji w pamięci.
- Iteratory umożliwiają pracę z nieskończonymi strumieniami danych, generując elementy tylko wtedy, gdy są potrzebne.
- Generatory pozwalają tworzyć zwięzłe i czytelne iteratory bez konieczności pisania pełnych klas z metodami `__iter__()` i `__next__()`.

### Złożone generatory i przepływ danych

Generatory można również łączyć, tworząc bardziej złożone strumienie danych. Na przykład, można stworzyć generator, który pobiera dane z innego generatora, przetwarza je i zwraca przetworzony wynik.

```python
def podwoj_wartosci(generator):
    for wartosc in generator:
        yield wartosc * 2

generator_liczb = (i for i in range(5))
podwojony_generator = podwoj_wartosci(generator_liczb)

for wartosc in podwojony_generator:
    print(wartosc)
```

Powyższy przykład pokazuje, jak można tworzyć złożone przepływy danych, gdzie generatory są używane do transformacji danych w sposób płynny i leniwy.

### Wbudowane funkcje iteratorowe

Python dostarcza kilku wbudowanych funkcji, które zwracają iteratory i znacznie ułatwiają pracę z kolekcjami.

#### `enumerate(iterable, start=0)`

Tworzy iterator par `(indeks, element)`. Przydatny gdy potrzebujemy indeksu elementu w pętli:

```python
owoce = ["jabłko", "banan", "gruszka"]

# Bez enumerate — ręczne zarządzanie indeksem
indeks = 0
for owoc in owoce:
    print(f"{indeks}: {owoc}")
    indeks += 1

# Z enumerate — czytelniej
for indeks, owoc in enumerate(owoce):
    print(f"{indeks}: {owoc}")

# Numerowanie od 1
for nr, owoc in enumerate(owoce, start=1):
    print(f"{nr}. {owoc}")
```

#### `zip(*iterables)`

Łączy elementy z kilku kolekcji w pary (krotki). Zatrzymuje się, gdy krótsza kolekcja zostanie wyczerpana:

```python
imiona = ["Jan", "Anna", "Piotr"]
oceny = [5, 4, 3]

for imie, ocena in zip(imiona, oceny):
    print(f"{imie}: {ocena}")

# Tworzenie słownika ze zip
slownik = dict(zip(imiona, oceny))
print(slownik)  # {'Jan': 5, 'Anna': 4, 'Piotr': 3}

# Rozpakowywanie zip (transpozycja)
pary = [(1, 'a'), (2, 'b'), (3, 'c')]
liczby, litery = zip(*pary)
print(list(liczby))   # [1, 2, 3]
print(list(litery))   # ['a', 'b', 'c']
```

Python 3.10 dodał `zip(..., strict=True)`, które zgłasza błąd jeśli kolekcje mają różne długości.

#### `reversed(sequence)`

Zwraca iterator przechodzący przez sekwencję od końca:

```python
lista = [1, 2, 3, 4, 5]
for el in reversed(lista):
    print(el)  # 5, 4, 3, 2, 1

print(list(reversed("Python")))  # ['n', 'o', 'h', 't', 'y', 'P']
```

#### `map(function, iterable)`

Stosuje funkcję do każdego elementu iterowalnego i zwraca iterator:

```python
liczby = [1, 2, 3, 4, 5]
kwadraty = map(lambda x: x**2, liczby)
print(list(kwadraty))   # [1, 4, 9, 16, 25]

# Z wieloma kolekcjami
a = [1, 2, 3]
b = [10, 20, 30]
print(list(map(lambda x, y: x + y, a, b)))  # [11, 22, 33]
```

#### `filter(function, iterable)`

Filtruje elementy iterowalnego — zachowuje tylko te, dla których funkcja zwraca `True`:

```python
liczby = range(-5, 6)
dodatnie = filter(lambda x: x > 0, liczby)
print(list(dodatnie))   # [1, 2, 3, 4, 5]

# Usuwanie wartości falsy
lista = [0, 1, "", "tekst", None, [], [1]]
print(list(filter(None, lista)))  # [1, 'tekst', [1]]
```

### Moduł `itertools` — zaawansowane iteratory

Moduł `itertools` dostarcza wydajnych narzędzi do tworzenia złożonych iteratorów:

```python
import itertools

# chain — łączenie kilku iterowalnych
print(list(itertools.chain([1, 2], [3, 4], [5])))
# [1, 2, 3, 4, 5]

# islice — wycinek z iteratora (jak slice dla list)
print(list(itertools.islice(range(100), 5, 15, 2)))
# [5, 7, 9, 11, 13]

# groupby — grupowanie sąsiednich elementów według klucza
dane = [("A", 1), ("A", 2), ("B", 3), ("B", 4), ("A", 5)]
for klucz, grupa in itertools.groupby(dane, key=lambda x: x[0]):
    print(klucz, list(grupa))
# A [('A', 1), ('A', 2)]
# B [('B', 3), ('B', 4)]
# A [('A', 5)]

# accumulate — narastające sumy/iloczyny
print(list(itertools.accumulate([1, 2, 3, 4, 5])))
# [1, 3, 6, 10, 15]

import operator
print(list(itertools.accumulate([1, 2, 3, 4, 5], operator.mul)))
# [1, 2, 6, 24, 120]  — silnia!
```

### Nieskończony iterator

Możemy napisać własny iterator generujący nieskończoną sekwencję:

```python
class FibonacciIter:
    """Iterator generujący nieskończony ciąg Fibonacciego."""
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        wynik = self.a
        self.a, self.b = self.b, self.a + self.b
        return wynik

fib = FibonacciIter()
pierwsze_10 = [next(fib) for _ in range(10)]
print(pierwsze_10)  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```
