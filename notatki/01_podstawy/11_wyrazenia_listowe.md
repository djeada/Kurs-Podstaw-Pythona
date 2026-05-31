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

### Najczęstsze wzorce i idiomy

| Wzorzec                        | Wyrażenie listowe                                     | Opis                              |
|--------------------------------|------------------------------------------------------|-----------------------------------|
| Filtrowanie                    | `[x for x in dane if warunek(x)]`                   | Zachowanie wybranych elementów    |
| Transformacja                  | `[f(x) for x in dane]`                              | Przekształcenie każdego elementu  |
| Filtrowanie + transformacja   | `[f(x) for x in dane if warunek(x)]`                | Oba na raz                        |
| Spłaszczanie                   | `[x for sub in dane for x in sub]`                  | Lista list → płaska lista         |
| Iloczyn kartezjański          | `[(x, y) for x in A for y in B]`                    | Wszystkie pary                    |
| Zamiana wartości               | `[x if x > 0 else 0 for x in dane]`                | Warunkowe podstawienie            |
| Indeksowanie                   | `[(i, x) for i, x in enumerate(dane)]`              | Pary (indeks, wartość)            |

### Typowe pułapki i dobre praktyki

#### Kiedy NIE stosować wyrażeń listowych

```python
# ❌ Zbyt skomplikowane — trudne do zrozumienia
wynik = [f(x) for x in dane if g(x) > 0 for y in h(x) if y != 0]

# ✓ Lepiej użyć zwykłej pętli
wynik = []
for x in dane:
    if g(x) > 0:
        for y in h(x):
            if y != 0:
                wynik.append(f(x))
```

#### Pułapka z mutowalnymi obiektami

```python
# ❌ Wszystkie wiersze to ta sama lista!
macierz = [[0] * 3] * 3
macierz[0][0] = 1
print(macierz)  # [[1, 0, 0], [1, 0, 0], [1, 0, 0]]

# ✓ Poprawnie — każdy wiersz to nowa lista
macierz = [[0] * 3 for _ in range(3)]
macierz[0][0] = 1
print(macierz)  # [[1, 0, 0], [0, 0, 0], [0, 0, 0]]
```

#### Efekt uboczny — wyrażenia listowe nie powinny modyfikować stanu

```python
# ❌ Nie używaj wyrażeń listowych dla efektów ubocznych
[print(x) for x in range(5)]  # Tworzy niepotrzebną listę [None, None, ...]

# ✓ Użyj pętli for
for x in range(5):
    print(x)
```

### Zaawansowane przykłady praktyczne

#### Transpozycja macierzy

```python
macierz = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]

transponowana = [[wiersz[i] for wiersz in macierz] for i in range(len(macierz[0]))]
print(transponowana)  # [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
```

#### Grupowanie elementów w paczki (chunking)

```python
dane = list(range(10))
n = 3
paczki = [dane[i:i+n] for i in range(0, len(dane), n)]
print(paczki)  # [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9]]
```

#### Słownik częstości wystąpień

```python
tekst = "abrakadabra"
czestosci = {znak: tekst.count(znak) for znak in set(tekst)}
print(czestosci)  # {'a': 5, 'b': 2, 'r': 2, 'k': 1, 'd': 1}
```

#### Filtrowanie słownika

```python
oceny = {"Anna": 5, "Jan": 3, "Kasia": 4, "Tomek": 2, "Ewa": 5}
najlepsi = {k: v for k, v in oceny.items() if v >= 4}
print(najlepsi)  # {'Anna': 5, 'Kasia': 4, 'Ewa': 5}
```
