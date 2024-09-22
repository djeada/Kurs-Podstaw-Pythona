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
    for

 wartosc in generator:
        yield wartosc * 2

generator_liczb = (i for i in range(5))
podwojony_generator = podwoj_wartosci(generator_liczb)

for wartosc in podwojony_generator:
    print(wartosc)
```

Powyższy przykład pokazuje, jak można tworzyć złożone przepływy danych, gdzie generatory są używane do transformacji danych w sposób płynny i leniwy.
