## Funkcje Lambda: Anonimowe Funkcje i Ich Zastosowanie

Funkcje **lambda**, zwane również funkcjami anonimowymi, są narzędziem szeroko stosowanym w programowaniu funkcyjnym. Są to krótkie, jedno-wierszowe funkcje, które nie posiadają przypisanej nazwy i są używane tam, gdzie zdefiniowanie pełnoprawnej funkcji byłoby nadmiarowe lub zbędne. W Pythonie i wielu innych językach programowania funkcje lambda odgrywają istotną rolę, zwłaszcza przy manipulacji danymi i implementacji algorytmów funkcyjnych.

### Definicja i Charakterystyka Funkcji Lambda

Funkcje lambda są przykładami **funkcji wyższego rzędu**, co oznacza, że funkcje te mogą być traktowane jak obiekty – mogą być przekazywane jako argumenty do innych funkcji, zwracane jako wynik innych funkcji lub przechowywane w strukturach danych, takich jak listy. Lambda funkcje pozwalają na zapisanie funkcji w sposób zwięzły i syntaktycznie uproszczony.

### Dlaczego warto używać lambd?

Funkcje lambda mają następujące zalety:

1. Funkcje lambda są krótkie i mogą być zdefiniowane w jednym wierszu. Unikamy rozbudowanych konstrukcji składniowych, co poprawia czytelność w prostych przypadkach.
2. Lambdy nie wymagają nadawania nazw, co jest wygodne, gdy funkcja ma być użyta jednorazowo.
3. Lambdy świetnie wpisują się w paradygmat programowania funkcyjnego, który traktuje funkcje jako obiekty pierwszej klasy. Umożliwia to przekazywanie funkcji lambda jako argumentów do innych funkcji, takich jak `map()`, `filter()`, `reduce()`.

### Składnia funkcji lambda

W Pythonie składnia funkcji lambda wygląda następująco:

```python
lambda argumenty: wyrażenie
```

- `lambda`: Słowo kluczowe do zdefiniowania funkcji anonimowej.
- `argumenty`: Lista argumentów funkcji. Możliwe jest przekazanie dowolnej liczby argumentów oddzielonych przecinkami.
- `wyrażenie`: Wyrażenie, które zostanie obliczone i zwrócone jako wynik funkcji.

Przykład składni w porównaniu do tradycyjnej funkcji:

```python
def zwykla_funkcja(x):
    return x ** 2

# Odpowiednik lambda
lambda_funkcja = lambda x: x ** 2
```

### Lambda a tradycyjna funkcja

Funkcja lambda pełni rolę uproszczonej wersji zwykłej funkcji. Różnice między nimi można wyrazić następująco:

- **Lambda** to funkcja anonimowa, zazwyczaj jednowierszowa, bez nazwy. Przykłady jej zastosowania obejmują przypadki, gdy funkcja jest używana jednorazowo.
- **Funkcja tradycyjna** to pełnoprawna funkcja z nazwą, definiowana za pomocą słowa kluczowego `def`. Jest bardziej elastyczna i może zawierać złożoną logikę.

### Przykład

Poniżej przedstawiamy porównanie między funkcją tradycyjną a funkcją lambda, obie podnoszą liczbę do kwadratu.

```python
def zwykla_funkcja(liczba: int) -> int:
    return liczba ** 2

przyklad_lambdy = lambda liczba: liczba ** 2

wartosc = 2

print(zwykla_funkcja(wartosc))  # Wynik: 4
print(przyklad_lambdy(wartosc))  # Wynik: 4
print((lambda liczba: liczba ** 2)(wartosc))  # Wynik: 4
```

### Funkcje lambda w kontekście funkcji wyższego rzędu

Funkcje wyższego rzędu to funkcje, które przyjmują inne funkcje jako argumenty lub zwracają funkcje jako wynik. Przykładowo, funkcje takie jak `map()`, `filter()` i `reduce()` wykorzystują lambdy do przetwarzania kolekcji danych.

#### Przykład z `map()`

Funkcja `map()` stosuje daną funkcję do każdego elementu iterowalnego obiektu (np. listy).

```python
lista = [1, 2, 3, 4]
kwadraty = list(map(lambda x: x ** 2, lista))
print(kwadraty)  # Wynik: [1, 4, 9, 16]
```

#### Przykład z `filter()`

Funkcja `filter()` zwraca te elementy iterowalnego obiektu, które spełniają warunek podany w funkcji lambda.

```python
lista = [1, 2, 3, 4, 5, 6]
parzyste = list(filter(lambda x: x % 2 == 0, lista))
print(parzyste)  # Wynik: [2, 4, 6]
```

#### Przykład z `reduce()`

Funkcja `reduce()` (dostępna w module `functools`) redukuje iterowalny obiekt do jednej wartości, stosując funkcję do kolejnych elementów.

```python
from functools import reduce

suma = reduce(lambda a, b: a + b, [1, 2, 3, 4])
print(suma)  # Wynik: 10
```

### Ograniczenia wyrażeń lambda

Mimo swojej zwięzłości, funkcje lambda mają pewne ograniczenia w porównaniu do tradycyjnych funkcji:

- Funkcje lambda mogą zawierać **tylko jedno wyrażenie**. Nie można w nich stosować złożonych instrukcji kontrolnych, takich jak `if-elif-else`, pętle `for` czy `while`.
- Nie mogą zawierać wieloetapowych operacji ani definicji lokalnych zmiennych.
- Zrozumienie skomplikowanych wyrażeń lambda może być trudne, co sprawia, że są mniej czytelne w przypadku bardziej zaawansowanych operacji.

### Symulacja struktur kontrolnych w lambdach

#### Symulacja instrukcji warunkowej `if`

Chociaż lambdy nie mogą bezpośrednio zawierać pełnej instrukcji `if`, mogą korzystać z operatora warunkowego (ternary operator).

```python
czy_parzysta = lambda x: 'parzysta' if x % 2 == 0 else 'nieparzysta'
print(czy_parzysta(4))  # Wynik: 'parzysta'
print(czy_parzysta(5))  # Wynik: 'nieparzysta'
```

#### Symulacja pętli `for`

Funkcje lambda nie obsługują bezpośrednio pętli `for`. Jednak można symulować iteracje za pomocą funkcji takich jak `map()`, która stosuje lambdę do każdego elementu iterowalnego obiektu.

```python
lista = [1, 2, 3, 4]
kwadraty = list(map(lambda x: x ** 2, lista))
print(kwadraty)  # Wynik: [1, 4, 9, 16]
```

#### Symulacja rekurencji

Mimo że lambdy nie obsługują pętli, możliwe jest definiowanie prostych rekursji, chociaż nie jest to zalecane z powodu ograniczeń głębokości stosu w Pythonie.

```python
faktorial = lambda n: 1 if n == 0 else n * faktorial(n - 1)
print(faktorial(5))  # Wynik: 120
```

### Praktyczne Zastosowania Lambd

#### Sortowanie złożonych struktur danych

Lambdy są używane do definiowania kryteriów sortowania, zwłaszcza przy pracy z bardziej złożonymi strukturami danych, jak listy słowników.

```python
studenci = [
    {'imie': 'Jan', 'wiek': 23},
    {'imie': 'Anna', 'wiek': 22},
    {'imie': 'Piotr', 'wiek': 24}
]

sortowani_po_wieku = sorted(studenci, key=lambda x: x['wiek'])
print(sortowani_po_wieku)
# Wynik: [{'imie': 'Anna', 'wiek': 22}, {'imie': 'Jan', 'wiek': 23}, {'imie': 'Piotr', 'wiek': 24}]
```

#### Obsługa danych w analizie

Lambdy są powszechnie używane w analizie danych, szczególnie gdy przetwarzamy dane w ramach takich narzędzi jak pandas. Mogą być używane w operacjach typu `apply()`.

```python
import pandas as pd

df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [10, 20, 30]
})

df['C'] = df.apply(lambda row: row.A + row.B, axis=1)
print(df)
```

Wynik: 

```
   A   B   C
0  1  10  11
1  2  20  22
2  3  30  33
```
