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

Dekoratory to funkcjonalność, która sprawia, że Python jest językiem wyjątkowo elastycznym i ekspresyjnym, umożliwiającym tworzenie zaawansowanych wzorców projektowych w prosty i zwięzły sposób.
