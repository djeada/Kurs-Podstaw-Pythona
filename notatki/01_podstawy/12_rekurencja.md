## Rekurencja

Rekurencja to technika programowania, w której funkcja wywołuje samą siebie w celu rozwiązania problemu. Każde wywołanie rekurencyjne operuje na mniejszym lub prostszym podproblemie, aż do osiągnięcia tzw. **warunku bazowego** (ang. *base case*), który kończy rekurencję. Rekurencja jest eleganckim sposobem rozwiązywania problemów, które naturalnie mają strukturę rekurencyjną, takich jak obliczanie silni, liczby Fibonacciego czy przeszukiwanie drzew.

### Struktura funkcji rekurencyjnej

Każda poprawna funkcja rekurencyjna składa się z dwóch kluczowych elementów:

1. **Warunek bazowy** – przypadek, dla którego odpowiedź jest znana bez dalszego wywołania rekurencyjnego. Bez niego funkcja wywoływałaby się w nieskończoność.
2. **Krok rekurencyjny** – wywołanie funkcji samej siebie z uproszczonym argumentem, przybliżając problem do warunku bazowego.

```python
def funkcja_rekurencyjna(n):
    if n == warunek_bazowy:   # zatrzymanie rekurencji
        return wynik_bazowy
    return funkcja_rekurencyjna(mniejszy_n)  # krok rekurencyjny
```

### Porównanie: pętla vs. rekurencja

Wiele problemów można rozwiązać zarówno iteracyjnie (pętlą), jak i rekurencyjnie. Oba podejścia mają swoje mocne strony.

#### Suma elementów listy

```python
def suma_petla(lista):
    suma = 0
    for element in lista:
        suma += element
    return suma

def suma_rekurencja(lista):
    if len(lista) == 0:
        return 0
    return lista[0] + suma_rekurencja(lista[1:])

print(suma_petla([1, 2, 3, 4, 5]))       # 15
print(suma_rekurencja([1, 2, 3, 4, 5]))  # 15
```

W wersji rekurencyjnej:
- **Warunek bazowy**: pusta lista → suma = 0.
- **Krok rekurencyjny**: pierwszy element + suma reszty listy.

### Przykład: Silnia

Silnia liczby `n` to iloczyn wszystkich liczb naturalnych od 1 do `n`. Matematycznie:

$$n! = n \times (n-1)!,\quad 0! = 1$$

```python
def silnia_petla(n):
    silnia = 1
    for i in range(1, n + 1):
        silnia *= i
    return silnia

def silnia_rekurencja(n):
    if n == 0:          # warunek bazowy
        return 1
    return n * silnia_rekurencja(n - 1)  # krok rekurencyjny

print(silnia_petla(5))       # 120
print(silnia_rekurencja(5))  # 120
```

Działanie dla `silnia_rekurencja(5)`:

```
silnia(5) = 5 * silnia(4)
          = 5 * 4 * silnia(3)
          = 5 * 4 * 3 * silnia(2)
          = 5 * 4 * 3 * 2 * silnia(1)
          = 5 * 4 * 3 * 2 * 1 * silnia(0)
          = 5 * 4 * 3 * 2 * 1 * 1
          = 120
```

### Przykład: Ciąg Fibonacciego

Ciąg Fibonacciego zdefiniowany jest wzorami:

$$F(0) = 0,\quad F(1) = 1,\quad F(n) = F(n-1) + F(n-2)$$

```python
def fibonacci_petla(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def fibonacci_rekurencja(n):
    if n == 0:    # warunek bazowy 1
        return 0
    if n == 1:    # warunek bazowy 2
        return 1
    return fibonacci_rekurencja(n - 1) + fibonacci_rekurencja(n - 2)

print(fibonacci_petla(10))       # 55
print(fibonacci_rekurencja(10))  # 55
```

> **Uwaga**: Naiwna implementacja rekurencyjna Fibonacciego oblicza te same podproblemy wielokrotnie, co powoduje wykładniczą złożoność czasową O(2ⁿ). W praktyce należy stosować memoizację lub wersję iteracyjną dla dużych `n`.

### Stos wywołań (call stack)

Przy każdym wywołaniu rekurencyjnym Python odkłada nową ramkę na **stos wywołań** (ang. *call stack*). Zbyt głęboka rekurencja może wyczerpać dostępny stos i spowodować błąd:

```
RecursionError: maximum recursion depth exceeded
```

Domyślny limit głębokości wynosi 1000. Można go sprawdzić i zmienić:

```python
import sys
print(sys.getrecursionlimit())  # 1000
sys.setrecursionlimit(5000)
```

### Rekurencja ogonowa

Rekurencja ogonowa (ang. *tail recursion*) to taka, w której wywołanie rekurencyjne jest ostatnią operacją w funkcji. Niektóre języki optymalizują ten wzorzec (eliminacja rekurencji ogonowej), ale Python tego nie robi – mimo to warto ją znać jako wzorzec projektowy:

```python
def silnia_ogonowa(n, akumulator=1):
    if n == 0:
        return akumulator
    return silnia_ogonowa(n - 1, n * akumulator)

print(silnia_ogonowa(5))  # 120
```

### Memoizacja

Memoizacja polega na zapamiętywaniu wyników wcześniej obliczonych wywołań, aby unikać wielokrotnego przeliczania tych samych podproblemów. Python oferuje wbudowany dekorator `@functools.lru_cache`:

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(50))  # 12586269025 — szybko, dzięki memoizacji
```

### Rekurencja w praktyce — przetwarzanie napisów

```python
def czy_palindrom(napis):
    """Sprawdza, czy napis jest palindromem."""
    if len(napis) <= 1:        # warunek bazowy
        return True
    if napis[0] != napis[-1]:  # warunek bazowy
        return False
    return czy_palindrom(napis[1:-1])  # krok rekurencyjny

print(czy_palindrom("kajak"))   # True
print(czy_palindrom("python"))  # False
```

```python
def policz_samogloski(napis):
    """Zlicza samogłoski rekurencyjnie."""
    samogloski = "aeiouAEIOUaąeęiouóAĄEĘIOUÓ"
    if not napis:
        return 0
    return (1 if napis[0] in samogloski else 0) + policz_samogloski(napis[1:])

print(policz_samogloski("Python"))  # 1
print(policz_samogloski("ala"))     # 2
```

### Kiedy używać rekurencji?

Rekurencja jest szczególnie naturalna w przypadku:

- **Struktur drzewiastych** (np. drzewa katalogów, drzewa wyszukiwań binarnych).
- **Algorytmów "dziel i zwyciężaj"** (np. quicksort, mergesort).
- **Problemów z naturalną definicją rekurencyjną** (np. silnia, Fibonacci, NWD).
- **Grafów i labiryntów** — przeszukiwanie DFS (ang. *Depth-First Search*).

Natomiast w przypadkach, gdzie:

- Głębokość rekurencji może być duża → preferuj pętlę lub memoizację.
- Problem ma proste, liniowe rozwiązanie iteracyjne → pętla jest czytelniejsza i szybsza.

### Podsumowanie

| Cecha                  | Rekurencja                               | Pętla (iteracja)                |
|------------------------|------------------------------------------|---------------------------------|
| Czytelność             | Zwięzła dla problemów rekurencyjnych     | Zwięzła dla problemów liniowych |
| Wydajność              | Koszt wywołań funkcji; ryzyko przepełnienia stosu | Zazwyczaj szybsza, brak kosztu stosu |
| Warunek stopu          | Warunek bazowy w funkcji                 | Warunek w pętli                 |
| Zastosowanie           | Drzewa, "dziel i zwyciężaj", struktury rekurencyjne | Sekwencyjne przetwarzanie danych |
