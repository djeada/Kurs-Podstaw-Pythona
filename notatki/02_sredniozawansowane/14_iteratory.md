## Iteratory

W języku Python pętla `for` służy do iterowania przez kolekcje lub iterowalne obiekty, takie jak listy, napisy, krotki czy słowniki. Kluczowym konceptem w kontekście iteracji jest tzw. iterator.

### Podstawy działania iteratorów

Przykład iteracji przez listę:

```python
for elem in [1, 2, 3]:
    print(elem)
```

Wbudowane kolekcje, takie jak listy, napisy czy krotki, są "iterowalne", co oznacza, że mają zaimplementowaną metodę `__iter__()`. Wywołanie tej metody zwraca iterator - obiekt, który posiada metodę `__next__()`. Dzięki niej można uzyskać dostęp do kolejnych elementów kolekcji.

```python
lista = [1, 2, 3]
iterator = iter(lista)
print(next(iterator))  # 1
print(next(iterator))  # 2
print(next(iterator))  # 3
# print(next(iterator))  # Wyrzuca wyjątek StopIteration
```

Gdy iterator osiągnie koniec kolekcji, wywołanie metody `__next__()` spowoduje wyrzucenie wyjątku `StopIteration`, informującego o tym, że nie ma już więcej elementów do zwrócenia.

### Tworzenie własnych iteratorów

Aby stworzyć własny iterator, trzeba zdefiniować dwie metody: `__iter__()` oraz `__next__()`. Metoda `__iter__()` powinna zwrócić obiekt iteratora (często jest to self), a metoda `__next__()` powinna zwracać kolejny element lub rzucać wyjątek StopIteration, gdy elementy się skończą.

Przykład:

```python
class MojaKolekcja:
    def __init__(self):
        self.elementy = [1, 2, 3]

    def __iter__(self):
        self.indeks = 0
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

### Generatory jako iteratory

Generatory są specjalnym rodzajem iteratorów, które definiuje się za pomocą funkcji i słowa kluczowego `yield`. Dzięki generatorom można łatwo tworzyć własne iterowalne sekwencje bez konieczności definiowania klas z metodami `__iter__()` i `__next__()`.

Przykład:

```python
def generator_liczb():
    for i in range(3):
        yield i

for liczba in generator_liczb():
    print(liczba)
```
