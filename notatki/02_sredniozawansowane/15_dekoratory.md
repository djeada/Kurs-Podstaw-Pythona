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

Python udostępnia gotowy dekorator `@functools.lru_cache`, który realizuje to samo bez pisania własnego kodu:

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

print(fib(50))  # 12586269025
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

#### Mierzenie czasu wykonania

```python
import functools
import time

def mierz_czas(funkcja):
    @functools.wraps(funkcja)
    def funkcja_wew(*args, **kwargs):
        start = time.perf_counter()
        wynik = funkcja(*args, **kwargs)
        koniec = time.perf_counter()
        print(f'{funkcja.__name__} wykonała się w {koniec - start:.4f}s')
        return wynik
    return funkcja_wew

@mierz_czas
def oblicz(n):
    return sum(range(n))

oblicz(1_000_000)  # oblicz wykonała się w 0.0231s
```

#### Walidacja argumentów

```python
import functools

def wymaga_dodatnich(funkcja):
    @functools.wraps(funkcja)
    def funkcja_wew(*args, **kwargs):
        for arg in args:
            if isinstance(arg, (int, float)) and arg < 0:
                raise ValueError(f"Argument {arg} musi być nieujemny")
        return funkcja(*args, **kwargs)
    return funkcja_wew

@wymaga_dodatnich
def pierwiastek(x):
    return x ** 0.5

print(pierwiastek(9))   # 3.0
pierwiastek(-4)         # ValueError: Argument -4 musi być nieujemny
```

#### Ponowienie próby (retry)

```python
import functools
import time

def ponow(ilosc_prob=3, opoznienie=1.0):
    def dekorator(funkcja):
        @functools.wraps(funkcja)
        def funkcja_wew(*args, **kwargs):
            for proba in range(1, ilosc_prob + 1):
                try:
                    return funkcja(*args, **kwargs)
                except Exception as e:
                    if proba == ilosc_prob:
                        raise
                    print(f'Próba {proba} nieudana: {e}. Ponawiam za {opoznienie}s...')
                    time.sleep(opoznienie)
        return funkcja_wew
    return dekorator

@ponow(ilosc_prob=3, opoznienie=0.5)
def pobierz_dane(url):
    # symulacja błędu sieciowego
    raise ConnectionError("Błąd połączenia")

# pobierz_dane("http://example.com")
# Próba 1 nieudana: Błąd połączenia. Ponawiam za 0.5s...
# Próba 2 nieudana: Błąd połączenia. Ponawiam za 0.5s...
# ConnectionError: Błąd połączenia
```

### Dekoratory klas

Dekoratory można stosować nie tylko do funkcji, ale też do klas:

```python
import functools

def singleton(klasa):
    instancje = {}
    @functools.wraps(klasa)
    def pobierz_instancje(*args, **kwargs):
        if klasa not in instancje:
            instancje[klasa] = klasa(*args, **kwargs)
        return instancje[klasa]
    return pobierz_instancje

@singleton
class Konfiguracja:
    def __init__(self):
        self.ustawienia = {}

k1 = Konfiguracja()
k2 = Konfiguracja()
print(k1 is k2)  # True — obie zmienne wskazują na ten sam obiekt
```

Dekoratory to funkcjonalność, która sprawia, że Python jest językiem wyjątkowo elastycznym i ekspresyjnym, umożliwiającym tworzenie zaawansowanych wzorców projektowych w prosty i zwięzły sposób.
