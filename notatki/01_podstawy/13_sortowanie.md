## Algorytmy sortowania

Sortowanie to proces ustawiania elementów kolekcji w określonej kolejności (np. rosnącej lub malejącej). Jest jednym z fundamentalnych zagadnień informatyki. W Pythonie możemy korzystać z wbudowanej funkcji `sorted()` lub metody `list.sort()`, jednak znajomość klasycznych algorytmów sortowania pomaga zrozumieć pojęcia złożoności obliczeniowej, efektywności i podejścia "dziel i zwyciężaj".

### Wbudowane sortowanie w Pythonie

Python udostępnia dwa wbudowane sposoby sortowania:

```python
lista = [5, 2, 8, 1, 9, 3]

# sorted() — tworzy nową posortowaną listę, oryginał się nie zmienia
posortowana = sorted(lista)
print(posortowana)  # [1, 2, 3, 5, 8, 9]
print(lista)        # [5, 2, 8, 1, 9, 3]

# list.sort() — sortuje listę w miejscu
lista.sort()
print(lista)  # [1, 2, 3, 5, 8, 9]

# Sortowanie odwrotne
print(sorted(lista, reverse=True))  # [9, 8, 5, 3, 2, 1]

# Sortowanie po kluczu
slowa = ["banan", "jabłko", "gruszka", "śliwka"]
print(sorted(slowa, key=len))  # ['banan', 'jabłko', 'gruszka', 'śliwka']
```

---

### Sortowanie bąbelkowe (Bubble Sort)

**Idea**: Wielokrotnie przechodzimy przez listę, porównując sąsiednie elementy i zamieniając je, jeśli są w złej kolejności. Po każdym przebiegu największy element "wypływa" na koniec listy — stąd nazwa "bąbelkowe".

**Złożoność**: O(n²) — nieefektywne dla dużych zbiorów, ale prosty do zrozumienia.

```python
def sortowanie_babelkowe(lista):
    for _ in range(len(lista)):
        for j in range(len(lista) - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

print(sortowanie_babelkowe([5, 4, 3, 2, 1]))  # [1, 2, 3, 4, 5]
print(sortowanie_babelkowe([1, 5, 2, 4, 3]))  # [1, 2, 3, 4, 5]
```

Krok po kroku dla `[5, 3, 1]`:

```
Przebieg 1: [5, 3, 1] → [3, 5, 1] → [3, 1, 5]
Przebieg 2: [3, 1, 5] → [1, 3, 5] → [1, 3, 5]
Wynik: [1, 3, 5]
```

---

### Sortowanie przez wybieranie (Selection Sort)

**Idea**: W każdej iteracji znajdujemy najmniejszy element z nieposortowanej części listy i przenosimy go na początek. Powtarzamy, aż lista jest posortowana.

**Złożoność**: O(n²) — podobna do bąbelkowego, ale wykonuje mniej zamian.

```python
def znajdz_najmniejszy(lista):
    najmniejszy_index = 0
    for i in range(1, len(lista)):
        if lista[i] < lista[najmniejszy_index]:
            najmniejszy_index = i
    return najmniejszy_index

def sortowanie_przez_wybieranie(lista):
    nowa_lista = []
    kopia = lista[:]
    for _ in range(len(kopia)):
        najmniejszy = znajdz_najmniejszy(kopia)
        nowa_lista.append(kopia.pop(najmniejszy))
    return nowa_lista

print(sortowanie_przez_wybieranie([5, 4, 3, 2, 1]))  # [1, 2, 3, 4, 5]
print(sortowanie_przez_wybieranie([1, 5, 2, 4, 3]))  # [1, 2, 3, 4, 5]
```

Krok po kroku dla `[5, 3, 1, 4]`:

```
Krok 1: minimum = 1 (indeks 2) → nowa_lista = [1], pozostałe = [5, 3, 4]
Krok 2: minimum = 3 (indeks 1) → nowa_lista = [1, 3], pozostałe = [5, 4]
Krok 3: minimum = 4 (indeks 1) → nowa_lista = [1, 3, 4], pozostałe = [5]
Krok 4: minimum = 5 (indeks 0) → nowa_lista = [1, 3, 4, 5]
```

---

### Sortowanie szybkie (Quicksort)

**Idea** (podejście "dziel i zwyciężaj"):
1. Wybierz element zwany **pivotem** (np. pierwszy element listy).
2. Podziel pozostałe elementy na dwie grupy: mniejsze lub równe pivotowi i większe.
3. Rekurencyjnie posortuj obie grupy.
4. Złącz wyniki: `[posortowane_mniejsze] + [pivot] + [posortowane_wieksze]`.

**Złożoność**: O(n log n) średnio, O(n²) w najgorszym przypadku — w praktyce jeden z najszybszych algorytmów.

```python
def sortowanie_szybkie(lista):
    if len(lista) <= 1:
        return lista

    pivot = lista[0]
    mniejsze = [e for e in lista[1:] if e <= pivot]
    wieksze  = [e for e in lista[1:] if e > pivot]

    return sortowanie_szybkie(mniejsze) + [pivot] + sortowanie_szybkie(wieksze)

print(sortowanie_szybkie([5, 4, 3, 2, 1]))  # [1, 2, 3, 4, 5]
print(sortowanie_szybkie([1, 5, 2, 4, 3]))  # [1, 2, 3, 4, 5]
```

Wizualizacja dla `[3, 1, 4, 1, 5, 9, 2]`:

```
pivot = 3
mniejsze = [1, 1, 2]
wieksze  = [4, 5, 9]

quick([1, 1, 2]) = [1, 1, 2]
quick([4, 5, 9]) = [4, 5, 9]

Wynik: [1, 1, 2] + [3] + [4, 5, 9] = [1, 1, 2, 3, 4, 5, 9]
```

---

### Porównanie algorytmów

| Algorytm                   | Złożoność (średnia) | Złożoność (najgorszy) | Stabilny | Uwagi                              |
|----------------------------|---------------------|-----------------------|----------|------------------------------------|
| Bąbelkowe                  | O(n²)               | O(n²)                 | Tak      | Prosty, ale wolny dla dużych danych|
| Przez wybieranie           | O(n²)               | O(n²)                 | Nie      | Mało zamian; wolny dla dużych danych|
| Szybkie (Quicksort)        | O(n log n)          | O(n²)                 | Nie      | Bardzo szybkie w praktyce          |
| Wbudowane (`sorted`)       | O(n log n)          | O(n log n)            | Tak      | Algorytm Timsort; zalecane         |

> **Zalecenie praktyczne**: W codziennym kodzie Python zawsze używaj wbudowanego `sorted()` lub `.sort()`. Własne implementacje algorytmów sortowania są wartościowe edukacyjnie — pomagają zrozumieć złożoność obliczeniową — ale w produkcji wbudowane funkcje są szybsze i dokładniej zoptymalizowane.

---

### Wyszukiwanie w liście

Szukanie elementu w liście to równie podstawowe zagadnienie. Dwie klasyczne metody to wyszukiwanie liniowe i wyszukiwanie binarne.

#### Wyszukiwanie liniowe

Sprawdzamy elementy jeden po drugim, aż znajdziemy szukany lub wyczerpamy listę. Działa na listach **nieposortowanych**.

**Złożoność**: O(n)

```python
def wyszukiwanie_liniowe(lista, element):
    for i in range(len(lista)):
        if lista[i] == element:
            return i   # zwróć indeks znalezionego elementu
    return -1          # element nie znaleziony

lista = [3, 1, 4, 1, 5, 9, 2]
print(wyszukiwanie_liniowe(lista, 5))   # 4
print(wyszukiwanie_liniowe(lista, 7))   # -1
```

#### Wyszukiwanie binarne

Działa tylko na listach **posortowanych**. Dzieli listę na pół przy każdym kroku: jeśli środkowy element jest za duży, szukamy w lewej połowie; jeśli za mały — w prawej.

**Złożoność**: O(log n) — znacznie szybsze niż liniowe dla dużych danych.

```python
def wyszukiwanie_binarne(lista, element):
    lewy = 0
    prawy = len(lista) - 1

    while lewy <= prawy:
        srodek = (lewy + prawy) // 2
        if lista[srodek] == element:
            return srodek
        elif lista[srodek] < element:
            lewy = srodek + 1
        else:
            prawy = srodek - 1

    return -1

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(wyszukiwanie_binarne(lista, 6))   # 5
print(wyszukiwanie_binarne(lista, 10))  # -1
```

Wizualizacja dla listy `[1, 3, 5, 7, 9, 11]`, szukamy `7`:

```
Krok 1: lewy=0, prawy=5, środek=2 → lista[2]=5 < 7 → lewy=3
Krok 2: lewy=3, prawy=5, środek=4 → lista[4]=9 > 7 → prawy=3
Krok 3: lewy=3, prawy=3, środek=3 → lista[3]=7 == 7 → zwróć 3
```

Python ma wbudowany moduł `bisect` do wyszukiwania binarnego:

```python
import bisect

lista = [1, 3, 5, 7, 9, 11]
indeks = bisect.bisect_left(lista, 7)
print(indeks)          # 3
print(lista[indeks])   # 7
```

### Moduł `bisect` — wyszukiwanie i wstawianie do posortowanej listy

Moduł `bisect` zapewnia wydajne operacje na posortowanych listach bez potrzeby ponownego sortowania:

```python
import bisect

posortowana = [1, 3, 5, 7, 9]

# bisect_left — indeks, gdzie wstawić nowy element (przed duplikatem)
print(bisect.bisect_left(posortowana, 5))    # 2

# bisect_right — indeks, gdzie wstawić (po duplikacie)
print(bisect.bisect_right(posortowana, 5))   # 3

# insort_left — wstawienie elementu w posortowane miejsce
bisect.insort_left(posortowana, 4)
print(posortowana)   # [1, 3, 4, 5, 7, 9]

# insort — wstawienie (domyślnie jak insort_right)
bisect.insort(posortowana, 6)
print(posortowana)   # [1, 3, 4, 5, 6, 7, 9]
```

`bisect` jest szczególnie przydatny przy utrzymywaniu posortowanych list z dynamicznie dodawanymi elementami.

### Sortowanie przez scalanie (Merge Sort)

**Idea** (podejście "dziel i zwyciężaj"):
1. Podziel listę na dwie równe połowy.
2. Rekurencyjnie posortuj każdą z nich.
3. Scalaj posortowane połowy w jedną posortowaną listę.

**Złożoność**: O(n log n) — zawsze, w każdym przypadku. Stabilny algorytm.

```python
def sortowanie_przez_scalanie(lista):
    if len(lista) <= 1:
        return lista

    srodek = len(lista) // 2
    lewa = sortowanie_przez_scalanie(lista[:srodek])
    prawa = sortowanie_przez_scalanie(lista[srodek:])

    return scal(lewa, prawa)

def scal(lewa, prawa):
    wynik = []
    i = j = 0
    while i < len(lewa) and j < len(prawa):
        if lewa[i] <= prawa[j]:
            wynik.append(lewa[i])
            i += 1
        else:
            wynik.append(prawa[j])
            j += 1
    wynik.extend(lewa[i:])
    wynik.extend(prawa[j:])
    return wynik

print(sortowanie_przez_scalanie([5, 3, 8, 1, 9, 2]))  # [1, 2, 3, 5, 8, 9]
```

### Sortowanie za pomocą kopca (`heapq`)

Moduł `heapq` implementuje kopiec min (ang. *min-heap*) — strukturę danych, w której najmniejszy element jest zawsze na szczycie:

```python
import heapq

# heapify — zamień listę na kopiec (in-place)
lista = [5, 3, 8, 1, 9, 2]
heapq.heapify(lista)
print(lista)   # [1, 3, 2, 5, 9, 8] — struktura kopca

# heappush — wstaw element
heapq.heappush(lista, 4)

# heappop — usuń i zwróć najmniejszy element
print(heapq.heappop(lista))  # 1
print(heapq.heappop(lista))  # 2

# nsmallest / nlargest — n najmniejszych/największych elementów
dane = [5, 3, 8, 1, 9, 2, 7]
print(heapq.nsmallest(3, dane))  # [1, 2, 3]
print(heapq.nlargest(3, dane))   # [9, 8, 7]
```

### Zaawansowane sortowanie z kluczem

```python
from operator import attrgetter, itemgetter

# Sortowanie list słowników
pracownicy = [
    {"imie": "Jan", "wiek": 35, "pensja": 6000},
    {"imie": "Anna", "wiek": 28, "pensja": 7500},
    {"imie": "Piotr", "wiek": 42, "pensja": 5800},
]

# Po jednym kluczu
posortowani = sorted(pracownicy, key=itemgetter("wiek"))

# Po wielu kluczach — krotka
posortowani2 = sorted(pracownicy, key=itemgetter("pensja", "wiek"), reverse=True)

# Sortowanie obiektów po atrybucie
from dataclasses import dataclass

@dataclass
class Student:
    imie: str
    ocena: float

studenci = [Student("Jan", 4.5), Student("Anna", 5.0), Student("Piotr", 3.5)]
posortowani3 = sorted(studenci, key=attrgetter("ocena"), reverse=True)
for s in posortowani3:
    print(f"{s.imie}: {s.ocena}")
# Anna: 5.0
# Jan: 4.5
# Piotr: 3.5

# Sortowanie ze złożoną logiką — sort stabilny (Timsort)
# Najpierw po ocenie malejąco, przy remisie po imieniu rosnąco
posortowani4 = sorted(studenci, key=lambda s: (-s.ocena, s.imie))
```

### Rozbudowane porównanie algorytmów

| Algorytm                   | Złożoność (średnia) | Złożoność (najgorszy) | Stabilny | Uwagi                              |
|----------------------------|---------------------|-----------------------|----------|------------------------------------|
| Bąbelkowe                  | O(n²)               | O(n²)                 | Tak      | Prosty, ale wolny dla dużych danych|
| Przez wybieranie           | O(n²)               | O(n²)                 | Nie      | Mało zamian; wolny dla dużych danych|
| Szybkie (Quicksort)        | O(n log n)          | O(n²)                 | Nie      | Bardzo szybkie w praktyce          |
| Przez scalanie (Mergesort) | O(n log n)          | O(n log n)            | Tak      | Zawsze O(n log n); dodatkowa pamięć|
| Wbudowane (`sorted`)       | O(n log n)          | O(n log n)            | Tak      | Timsort — hybrydowy, zoptymalizowany|

> **Zalecenie praktyczne**: W codziennym kodzie Python zawsze używaj wbudowanego `sorted()` lub `.sort()`. Własne implementacje algorytmów sortowania są wartościowe edukacyjnie — pomagają zrozumieć złożoność obliczeniową — ale w produkcji wbudowane funkcje są szybsze i dokładniej zoptymalizowane.
