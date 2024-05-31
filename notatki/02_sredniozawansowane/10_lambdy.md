## Funkcje Lambda

Lambda to anonimowa funkcja, która może być używana w wielu językach programowania. Funkcje te są nazywane "anonimowymi", ponieważ nie mają przypisanej nazwy. Lambdy są używane, gdy potrzebujemy krótkiej funkcji, którą można zdefiniować w jednym wierszu.

## Dlaczego warto używać lambd?

Funkcje lambda mają kilka zalet:

1. **Zwięzłość**: Pozwalają na definiowanie krótkich funkcji w jednym wierszu, co może uprościć kod.
2. **Anonimowość**: Nie wymagają nazwy, co jest przydatne, gdy funkcja jest używana tylko raz i nie ma potrzeby jej ponownego wywołania.
3. **Funkcyjność**: Umożliwiają programowanie funkcyjne, gdzie funkcje są traktowane jako obiekty pierwszej klasy i mogą być przekazywane jako argumenty, zwracane z innych funkcji, itp.

### Składnia funkcji lambda

Składnia funkcji lambda zależy od języka programowania, ale zazwyczaj jest zbliżona do poniższego schematu:

```python
lambda argumenty: wyrażenie
```

- `lambda`: Słowo kluczowe do stworzenia funkcji anonimowej.
- `argumenty`: Lista argumentów wejściowych, które mogą być dowolną liczbą argumentów oddzielonych przecinkami.
- `wyrażenie`: Wyrażenie, które jest zwracane przez funkcję lambda.

### Przykład

Oto podstawowy przykład wyrażenia lambda w porównaniu do standardowej funkcji:

```python
def zwykla_funkcja(liczba: int) -> int:
    return liczba**2

przyklad_lambdy = lambda liczba: liczba**2

wartosc = 2

print(zwykla_funkcja(wartosc)) # 4
print(przyklad_lambdy(wartosc)) # 4
print((lambda liczba: liczba**2)(wartosc)) # 4
```

### Ograniczenia wyrażeń lambda

Chociaż wyrażenia lambda są wygodne, mają pewne ograniczenia w porównaniu do standardowych funkcji:

- Można zdefiniować tylko jedno wyrażenie.
- Nie jest możliwe używanie instrukcji, takich jak `if-elif-else`, `for` czy `while`.
- Nie można definiować ani przypisywać zmiennych (chociaż można używać `setattr()` dla obiektów).
- Są one mniej czytelne w przypadku skomplikowanych operacji.

### Zaawansowane zastosowania

#### Symulacja `if`

Chociaż w wyrażeniach lambda nie można bezpośrednio używać instrukcji `if`, można je symulować za pomocą operatora warunkowego (ternary operator):

```python
lambda x: 'parzysta' if x % 2 == 0 else 'nieparzysta'
```

Przykład użycia:

```python
czy_parzysta = lambda x: 'parzysta' if x % 2 == 0 else 'nieparzysta'
print(czy_parzysta(4)) # 'parzysta'
print(czy_parzysta(5)) # 'nieparzysta'
```

#### Symulacja `for`

W wyrażeniach lambda nie można bezpośrednio używać pętli `for`, ale można symulować operacje iteracyjne za pomocą funkcji wbudowanych, takich jak `map` i `filter`:

```python
lambda lista: list(map(lambda x: x**2, lista))
```

Przykład użycia:

```python
kwadraty = lambda lista: list(map(lambda x: x**2, lista))
print(kwadraty([1, 2, 3, 4])) # [1, 4, 9, 16]
```

#### Symulacja `while`

Bezpośrednia symulacja `while` w wyrażeniach lambda nie jest możliwa, ale prostsze przypadki można obsłużyć poprzez rekurencję (chociaż nie jest to zalecane ze względu na ograniczenia rekurencji w Pythonie):

```python
faktorial = lambda n: 1 if n == 0 else n * faktorial(n-1)
```

Przykład użycia:

```python
faktorial = lambda n: 1 if n == 0 else n * faktorial(n-1)
print(faktorial(5)) # 120
```

#### Sortowanie złożonych struktur danych

Kiedy pracujemy ze złożonym strukturami danych, wyrażenia lambda mogą okazać się niezastąpione przy operacjach takich jak sortowania:

```python
studenci = [
    {'imie': 'Jan', 'wiek': 23},
    {'imie': 'Anna', 'wiek': 22},
    {'imie': 'Piotr', 'wiek': 24}
]

sortowani_po_wieku = sorted(studenci, key=lambda x: x['wiek'])
print(sortowani_po_wieku)
# [{'imie': 'Anna', 'wiek': 22}, {'imie': 'Jan', 'wiek': 23}, {'imie': 'Piotr', 'wiek': 24}]
```
