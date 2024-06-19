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

I. **Liczby całkowite (`int`)**: Służą do przechowywania liczb całkowitych, zarówno dodatnich, jak i ujemnych.

Przykłady: `5`, `-3`, `42`

II. **Liczby zmiennoprzecinkowe (`float`)**: Służą do przechowywania liczb rzeczywistych z częścią dziesiętną.

Przykłady: `3.14`, `-0.001`, `4.0`

III. **Napisy (`str`)**: Służą do przechowywania ciągów znaków, takich jak słowa czy zdania.

Przykłady: `"Hello"`, `'Python'`

IV. **Typ logiczny (`bool`)**: Służy do przechowywania wartości logicznych, które mogą być `True` lub `False`.

Przykłady: `True`, `False`

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
