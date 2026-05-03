## Wyrażenia listowe

Wyrażenia listowe (ang. *list comprehensions*) to zwięzły i czytelny sposób tworzenia list w Pythonie. Pozwalają na generowanie nowych list na podstawie istniejących sekwencji lub innych iterowalnych obiektów, opcjonalnie z zastosowaniem filtrowania lub transformacji elementów. Są wydajniejsze i czytelniejsze niż budowanie list za pomocą tradycyjnych pętli `for`.

### Podstawowa składnia

Ogólna postać wyrażenia listowego wygląda następująco:

```python
nowa_lista = [wyrażenie for element in iterowalny_obiekt]
```

Jest to skrócony zapis równoważny poniższej pętli:

```python
nowa_lista = []
for element in iterowalny_obiekt:
    nowa_lista.append(wyrażenie)
```

#### Przykład podstawowy

```python
# Tradycyjna pętla
lista = []
for i in range(10):
    lista.append(i)
print(lista)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Wyrażenie listowe
lista = [i for i in range(10)]
print(lista)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

#### Transformacja elementów

Wyrażenia listowe świetnie nadają się do przekształcania każdego elementu kolekcji:

```python
# Kwadraty liczb
kwadraty = [i ** 2 for i in range(10)]
print(kwadraty)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Zamiana liter na wielkie
imiona = ["anna", "jan", "maria", "piotr"]
imiona_wielkie = [imie.upper() for imie in imiona]
print(imiona_wielkie)  # ['ANNA', 'JAN', 'MARIA', 'PIOTR']
```

### Wyrażenia listowe z warunkiem

Możemy dodać warunek `if`, aby filtrować elementy:

```python
nowa_lista = [wyrażenie for element in iterowalny_obiekt if warunek]
```

#### Przykład z filtrowaniem

```python
# Tylko liczby parzyste
parzyste = [i for i in range(10) if i % 2 == 0]
print(parzyste)  # [0, 2, 4, 6, 8]

# Imiona dłuższe niż 3 znaki
imiona = ["adam", "ewa", "kasia", "tomek", "jan", "grzegorz"]
dlugie_imiona = [imie for imie in imiona if len(imie) > 3]
print(dlugie_imiona)  # ['kasia', 'tomek', 'grzegorz']
```

#### Warunek if-else w wyrażeniu listowym

Możemy również stosować wyrażenia warunkowe (operator trójargumentowy) po stronie `wyrażenia`, nie jako filtr:

```python
# Etykieta: "parzysta" lub "nieparzysta"
etykiety = ["parzysta" if i % 2 == 0 else "nieparzysta" for i in range(6)]
print(etykiety)  # ['parzysta', 'nieparzysta', 'parzysta', 'nieparzysta', 'parzysta', 'nieparzysta']
```

### Wyrażenia listowe z funkcją

Wyrażenia listowe mogą wywoływać dowolne funkcje na elementach kolekcji:

```python
def kwadrat(x):
    return x ** 2

lista = [kwadrat(i) for i in range(10)]
print(lista)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

### Zagnieżdżone wyrażenia listowe

Wyrażenia listowe mogą być zagnieżdżone — odpowiadają zagnieżdżonym pętlom `for`:

```python
# Wszystkie pary (i, j) gdzie i != j
pary = [(i, j) for i in range(3) for j in range(3) if i != j]
print(pary)
# [(0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1)]
```

#### Spłaszczanie listy list

```python
macierz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
plaski = [element for wiersz in macierz for element in wiersz]
print(plaski)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

### Wyrażenia słownikowe i zbiorowe

Python oferuje analogiczną składnię dla słowników i zbiorów:

#### Wyrażenia słownikowe (dict comprehensions)

```python
# Słownik: liczba → jej kwadrat
kwadraty = {i: i ** 2 for i in range(6)}
print(kwadraty)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Odwracanie klucz-wartość w słowniku
oryginalny = {'a': 1, 'b': 2, 'c': 3}
odwrocony = {v: k for k, v in oryginalny.items()}
print(odwrocony)  # {1: 'a', 2: 'b', 3: 'c'}
```

#### Wyrażenia zbiorowe (set comprehensions)

```python
# Zbiór unikalnych długości słów
slowa = ["ala", "ma", "kota", "ala", "kota"]
dlugosci = {len(slowo) for slowo in slowa}
print(dlugosci)  # {2, 3, 4}
```

### Wyrażenia generatorowe

Używając nawiasów okrągłych zamiast kwadratowych, uzyskujemy generator, który oblicza wartości leniwie (jeden po drugim), nie tworząc całej listy w pamięci:

```python
# Generator
gen = (i ** 2 for i in range(10))
print(type(gen))   # <class 'generator'>
print(next(gen))   # 0
print(next(gen))   # 1

# Użycie w pętli
for v in (i ** 2 for i in range(5)):
    print(v)
```

Generatory są szczególnie przydatne, gdy pracujemy z dużymi zbiorami danych, które nie muszą być jednocześnie trzymane w pamięci.

### Porównanie wydajności

Wyrażenia listowe są zazwyczaj szybsze od równoważnych pętli `for`, ponieważ Python optymalizuje je wewnętrznie. W przypadku bardzo dużych zbiorów danych warto jednak rozważyć użycie generatorów, które są oszczędniejsze pamięciowo.

```python
from timeit import timeit

# Pętla for
t1 = timeit("[i**2 for i in range(1000)]", number=10000)

# Generator w sum()
t2 = timeit("sum(i**2 for i in range(1000))", number=10000)

print(f"Wyrażenie listowe: {t1:.3f}s")
print(f"Generator:         {t2:.3f}s")
```

### Podsumowanie

| Typ wyrażenia         | Składnia                                 | Wynik             |
|-----------------------|------------------------------------------|-------------------|
| Listowe               | `[wyrażenie for x in it]`                | `list`            |
| Listowe z filtrem     | `[wyrażenie for x in it if warunek]`     | `list`            |
| Słownikowe            | `{k: v for x in it}`                     | `dict`            |
| Zbiorowe              | `{wyrażenie for x in it}`               | `set`             |
| Generatorowe          | `(wyrażenie for x in it)`               | `generator`       |

Wyrażenia listowe są idiomatycznym, czytelnym i wydajnym narzędziem Pythona, które warto stosować wszędzie tam, gdzie budujemy nową kolekcję na podstawie istniejących danych.
