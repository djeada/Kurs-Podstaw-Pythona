## Dekoratory

Dekoratory w Pythonie to potężne narzędzie, które pozwala na dynamiczne dodawanie funkcjonalności do istniejących funkcji lub metod. Są one często używane do rozszerzania, modyfikowania lub dostosowywania zachowania funkcji bez konieczności modyfikowania samego kodu źródłowego.

### Podstawy użycia dekoratorów

Dekorator to funkcja wyższego rzędu, która przyjmuje funkcję (lub klasę) jako argument i zwraca nową funkcję, która zwykle zawiera rozszerzone zachowanie funkcji dekorowanej.

```python
def dekoruj(funkcja):
    def funkcja_wew():
        print('przetwarzam dane')
        funkcja()
    return funkcja_wew

@dekoruj
def foo():
    print('foo')

foo()  # Wyjście: przetwarzam dane \n foo
```

W powyższym przykładzie `dekoruj` jest dekoratorem, który dodaje komunikat "przetwarzam dane" przed wywołaniem funkcji `foo`.

### Zachowanie metadanych z funkcji dekorowanej

Aby zachować metadane oryginalnej funkcji po jej dekorowaniu, używamy dekoratora `functools.wraps()`:

```python
import functools

def dekoruj(funkcja):
    @functools.wraps(funkcja)
    def funkcja_wew():
        print('przetwarzam dane')
        funkcja()
    return funkcja_wew

@dekoruj
def foo():
    """Dokumentacja funkcji foo."""
    print('foo')

print(foo.__name__)  # Wyjście: foo
print(foo.__doc__)   # Wyjście: Dokumentacja funkcji foo.
```

### Przekazywanie argumentów do dekoratora i funkcji dekorowanej

Aby dekorator mógł obsługiwać funkcje z dowolną liczbą argumentów, używamy `*args` i `**kwargs`:

```python
import functools

def dekoruj(funkcja):
    @functools.wraps(funkcja)
    def funkcja_wew(*args, **kwargs):
        print('przetwarzam dane')
        funkcja(*args, **kwargs)
    return funkcja_wew

@dekoruj
def foo(a, b):
    print(f'a: {a}; b: {b}')

foo(1, 2)  # Wyjście: przetwarzam dane \n a: 1; b: 2
```

### Dekoratory z argumentami

W niektórych przypadkach możemy chcieć, aby nasz dekorator przyjmował argumenty. W takim przypadku dekorator będzie funkcją zwracającą dekorator wewnętrzny:

```python
import functools

def dekoruj_tekstem(tekst):
    def dekoruj(funkcja):
        @functools.wraps(funkcja)
        def funkcja_wew(*args, **kwargs):
            print(tekst)
            return funkcja(*args, **kwargs)
        return funkcja_wew
    return dekoruj

@dekoruj_tekstem('Dekorator z argumentem!')
def bar():
    print('bar')

bar()  # Wyjście: Dekorator z argumentem! \n bar
```

### Zastosowanie dekoratorów w rzeczywistych scenariuszach

Dekoratory są niezwykle użyteczne w wielu scenariuszach, takich jak:

#### Caching

Dekorator może być użyty do zapamiętywania wyników funkcji, co jest szczególnie przydatne w przypadku kosztownych obliczeniowo operacji.

```python
import functools

def memoize(funkcja):
    cache = {}
    
    @functools.wraps(funkcja)
    def funkcja_wew(*args):
        if args in cache:
            return cache[args]
        result = funkcja(*args)
        cache[args] = result
        return result
    
    return funkcja_wew

@memoize
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

print(fib(10))  # Wyjście: 55
```

#### Logowanie

Dekorator może dodać logowanie do funkcji, pomagając śledzić wywołania funkcji i ich parametry.

```python
import functools

def logowanie(funkcja):
    @functools.wraps(funkcja)
    def funkcja_wew(*args, **kwargs):
        print(f'Wywoływanie {funkcja.__name__} z argumentami: {args}, {kwargs}')
        result = funkcja(*args, **kwargs)
        print(f'{funkcja.__name__} zwrócił: {result}')
        return result
    return funkcja_wew

@logowanie
def dodaj(a, b):
    return a + b

dodaj(3, 5)  # Wyjście: Wywoływanie dodaj z argumentami: (3, 5), {} \n dodaj zwrócił: 8
```

Dekoratory to funkcjonalność, która sprawia, że Python jest językiem wyjątkowo elastycznym i ekspresyjnym, umożliwiającym tworzenie zaawansowanych wzorców projektowych w prosty i zwięzły sposób.
