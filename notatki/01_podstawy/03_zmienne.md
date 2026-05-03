## Zmienne

Zmienne pełnią kluczową rolę w programowaniu, umożliwiając przechowywanie i manipulację danymi. Dzięki nim możemy zapisywać, modyfikować i odzyskiwać wartości w trakcie wykonywania programu. Zrozumienie zmiennych i ich typów jest podstawą do pisania efektywnego i poprawnego kodu.

### Deklaracja i inicjalizacja

W Pythonie nie ma potrzeby jawnego deklarowania typu zmiennej przed jej użyciem. Język ten jest dynamicznie typowany, co oznacza, że typ zmiennej jest określany automatycznie w trakcie jej inicjalizacji. Możemy po prostu przypisać wartość do zmiennej, a Python sam rozpozna jej typ.

```python
x = 10    # Zmienna typu int
y = 3.14  # Zmienna typu float
name = "Alice"  # Zmienna typu str
is_active = True  # Zmienna typu bool
```

### Typy podstawowe

W Pythonie mamy kilka podstawowych typów danych, które są używane do przechowywania różnych rodzajów informacji:

| Typ danych                  | Opis                                                 | Przykłady            |
|-----------------------------|------------------------------------------------------|----------------------|
| **Liczby całkowite (`int`)**| Służą do przechowywania liczb całkowitych, zarówno dodatnich, jak i ujemnych. | `5`, `-3`, `42`      |
| **Liczby zmiennoprzecinkowe (`float`)** | Służą do przechowywania liczb rzeczywistych z częścią dziesiętną. | `3.14`, `-0.001`, `4.0` |
| **Napisy (`str`)**          | Służą do przechowywania ciągów znaków, takich jak słowa czy zdania. | `"Hello"`, `'Python'`|
| **Typ logiczny (`bool`)**   | Służy do przechowywania wartości logicznych, które mogą być `True` lub `False`. | `True`, `False`      |

### Nazewnictwo zmiennych

Poprawne nazewnictwo zmiennych jest kluczowe dla czytelności i zrozumienia kodu. W Pythonie obowiązują pewne zasady dotyczące nazw zmiennych:

- Nazwa zmiennej musi zaczynać się od litery (a-z, A-Z) lub znaku podkreślenia (`_`), po którym może następować dowolna kombinacja liter, cyfr (0-9) i znaków podkreślenia.
- Nazwy zmiennych są wrażliwe na wielkość liter, co oznacza, że `zmienna`, `Zmienna` i `ZMIENNA` to trzy różne zmienne.
- Chociaż Python nie ma ograniczenia co do długości nazw zmiennych, zaleca się nadawanie krótkich, ale jednoznacznych nazw, które opisują przeznaczenie zmiennej. Na przykład `wiek`, `cena_produktu` są lepsze niż `a`, `b`, `c`.

### Przykład

Rozważmy poniższy kod:

```python
a = 3
b = a
b = 5
print(a) # Co zostanie wypisane?
```

W tym przypadku, zmiennej `b` przypisujemy wartość zmiennej `a`, a następnie zmieniamy wartość `b` na 5. Mimo to, wartość zmiennej `a` pozostaje bez zmian, więc odpowiedź to 3.

### Operacje na zmiennych

Zmiennymi można wykonywać różnorodne operacje, w zależności od ich typu:

#### Operacje arytmetyczne na liczbach

Możliwe operacje arytmetyczne obejmują dodawanie, odejmowanie, mnożenie, dzielenie itp.

```python
x = 10
y = 3
print(x + y)  # Wynik: 13
print(x - y)  # Wynik: 7
print(x * y)  # Wynik: 30
print(x / y)  # Wynik: 3.333...
```

#### Operacje na napisach

Możliwe operacje na napisach obejmują konkatenację, powielanie, wycinanie podciągów.

```python
name = "Alice"
greeting = "Hello, " + name  # Konkatenacja
print(greeting)  # Wynik: Hello, Alice

repeated = name * 3  # Powielanie
print(repeated)  # Wynik: AliceAliceAlice
```

#### Operacje logiczne

Możliwe operacje logiczne obejmują `and`, `or`, `not`.

```python
is_active = True
is_admin = False
print(is_active and is_admin)  # Wynik: False
print(is_active or is_admin)   # Wynik: True
print(not is_active)           # Wynik: False
```

### Dynamiczna zmiana typu

W Pythonie możemy przypisać nową wartość zmiennej, zmieniając jej typ dynamicznie:

```python
var = 10  # Typ int
var = "Ten"  # Typ str
var = 3.14  # Typ float
```

### Sprawdzanie typu zmiennej

Możemy sprawdzić typ zmiennej za pomocą funkcji `type()`:

```python
x = 10
print(type(x))  # Wynik: <class 'int'>

y = 3.14
print(type(y))  # Wynik: <class 'float'>

name = "Alice"
print(type(name))  # Wynik: <class 'str'>

is_active = True
print(type(is_active))  # Wynik: <class 'bool'>
```

Możemy również sprawdzić, czy zmienna jest określonego typu, korzystając z funkcji `isinstance()`:

```python
x = 10
print(isinstance(x, int))    # True
print(isinstance(x, float))  # False
print(isinstance(x, (int, float)))  # True — sprawdzamy jeden z kilku typów
```

### Konwersja typów (rzutowanie)

Czasami musimy jawnie przekonwertować wartość z jednego typu na inny. Python udostępnia w tym celu wbudowane funkcje konwersji:

| Funkcja    | Opis                                      | Przykład                       |
|------------|-------------------------------------------|--------------------------------|
| `int(x)`   | Konwertuje `x` na liczbę całkowitą        | `int("42")` → `42`             |
| `float(x)` | Konwertuje `x` na liczbę zmiennoprzecinkową | `float("3.14")` → `3.14`     |
| `str(x)`   | Konwertuje `x` na napis                   | `str(100)` → `"100"`           |
| `bool(x)`  | Konwertuje `x` na wartość logiczną        | `bool(0)` → `False`            |

#### Konwersja na `int`

```python
print(int(3.99))    # 3  — część dziesiętna jest odcinana (nie zaokrąglana)
print(int("42"))    # 42
print(int(True))    # 1
print(int(False))   # 0
```

#### Konwersja na `float`

```python
print(float(7))      # 7.0
print(float("3.14")) # 3.14
print(float(True))   # 1.0
```

#### Konwersja na `str`

```python
print(str(100))    # "100"
print(str(3.14))   # "3.14"
print(str(True))   # "True"
```

#### Konwersja na `bool`

W Pythonie każda wartość może zostać oceniona jako `True` lub `False`. Za `False` uważane są:

- liczba `0` (i `0.0`)
- pusty napis `""`
- pusta lista `[]`, pusty słownik `{}`, pusty zbiór `set()`
- wartość `None`

Wszystkie pozostałe wartości są traktowane jako `True`:

```python
print(bool(0))     # False
print(bool(1))     # True
print(bool(-5))    # True
print(bool(""))    # False
print(bool("Hi"))  # True
print(bool([]))    # False
print(bool([0]))   # True
```

#### Błędy konwersji

Nieprawidłowa konwersja powoduje wyjątek `ValueError`:

```python
int("sto")     # ValueError: invalid literal for int() with base 10: 'sto'
float("abc")   # ValueError: could not convert string to float: 'abc'
```

Można zabezpieczyć się przed błędem używając bloku `try/except`:

```python
tekst = "abc"
try:
    liczba = int(tekst)
except ValueError:
    print(f"Nie można przekonwertować '{tekst}' na int")
```
