## Funkcje

Funkcje są blokami instrukcji zamkniętymi pod jedną nazwą i pozwalającymi na kontrolowanie z zewnątrz poprzez przekazywanie argumentów. Definicja funkcji polega na określeniu, które instrukcje należą do ciała funkcji, ile argumentów oczekuje funkcja oraz jaką nazwą będzie ona wywoływana w innych miejscach kodu. Definicja sama w sobie nie uruchamia jeszcze żadnych instrukcji - potrzebne jest użycie nazwy funkcji wraz z wartościami argumentów w innym miejscu kodu, aby instrukcje zostały wykonane.

### Koncepcja i potrzeba funkcji

W matematyce funkcja może wyglądać tak:

$$f(x) = x^2 + 1$$

Tutaj funkcja `f` przyjmuje argument `x`, wykonuje operację \( x^2 + 1 \) i zwraca wynik. W programowaniu funkcje działają na podobnej zasadzie, ale zamiast operacji matematycznych mogą wykonywać dowolny kod.

Główne powody używania funkcji w programowaniu to:

1. Funkcje pozwalają na podział kodu na mniejsze fragmenty, co znacząco wspiera **modularność** programu, ułatwiając zarządzanie poszczególnymi jego elementami.
2. Dzięki zastosowaniu funkcji, możliwe jest wielokrotne wykorzystanie tych samych fragmentów kodu w różnych częściach programu, co znacznie poprawia **reużywalność**.
3. Ponadto, funkcje pomagają uporządkować kod w taki sposób, że staje się on bardziej zrozumiały, co przekłada się na lepszą **czytelność** oraz łatwiejsze jego utrzymanie.
4. Poprzez stosowanie funkcji można również ukryć szczegóły implementacji, co pozwala użytkownikowi skupić się tylko na kluczowych aspektach działania, wspierając tym samym **abstrakcję** kodu.

### Definicja funkcji

Funkcje mają następującą postać:

```python
def nazwa_funkcji(argumenty):
    kod # ciało funkcji
```

Ciało funkcji może być dowolnie rozbudowane, ale zaleca się dzielenie większych funkcji na mniejsze, które mają jasno określony cel. W ten sposób zmniejsza się złożoność kodu i ułatwia jego czytanie.

### Wywołanie funkcji

Zdefiniowaną funkcję wywołujemy w kodzie poprzez jej nazwę. Poniżej znajduje się podstawowy przykład wywołania funkcji.

```python
# w tym miejscu definiujemy funkcję
def ryba():
    print('rybka')

# w tym miejscu wywołujemy funkcję
ryba()
# wyświetli: rybka
```

### Funkcje z argumentami

Funkcje mogą mieć dowolną ilość argumentów - możliwe jest stworzenie funkcji bez argumentów lub funkcji z wieloma argumentami. Argumenty te pozwalają na przekazywanie danych do funkcji, które mogą być wykorzystywane w jej wnętrzu. Poniżej znajduje się przykład funkcji z jednym argumentem.

```python
def ryba(argument):
    # oczekujemy, że argument będzie liczbą naturalną
    for i in range(argument):
        print('ryba')

# wywołanie funkcji z argumentem 3
ryba(3)

# wyświetli:
# ryba
# ryba
# ryba
```

### Słowo kluczowe `return`

Słowo kluczowe `return` powoduje opuszczenie funkcji (instrukcje umieszczone poniżej nie są wykonywane). `Return` pozwala również na przekazanie wartości z wnętrza funkcji do reszty programu. Taka wartość po wywołaniu funkcji jest często zapisywana w zmiennej w innym miejscu programu. Na przykład:

```python
def suma_trzech(a, b, c):
    return a + b + c

suma_a = suma_trzech(3, 6, 2)
suma_b = suma_trzech(4, 1, 7)

print(suma_a)  # wyświetli 11
print(suma_b)  # wyświetli 12
```

### Funkcje z domyślnymi argumentami

Możemy również zdefiniować funkcję z domyślnymi argumentami, które zostaną użyte, jeśli nie zostaną przekazane żadne inne. Domyślne argumenty muszą być umieszczone po argumentach obowiązkowych. Przykład:

```python
def suma_trzech(a, b, c=0):
    return a + b + c

suma_a = suma_trzech(3, 6)  # a + b + c = 3 + 6 + 0 = 9
suma_b = suma_trzech(4, 1, 7)  # a + b + c = 4 + 1 + 7 = 12

print(suma_a)  # wyświetli 9
print(suma_b)  # wyświetli 12
```

### Funkcje z nieograniczoną liczbą argumentów

Istnieje sposób na zdefiniowanie funkcji z nieograniczoną liczbą argumentów obowiązkowych, przy czym nie możemy ich użyć w połączeniu z argumentami domyślnymi. Przykład:

```python
def suma_n(*args):
    return sum(args)

suma_a = suma_n(1, 2, 3, 4)  # 1 + 2 + 3 + 4 = 10
suma_b = suma_n(10, 20, 30)  # 10 + 20 + 30 = 60

print(suma_a)  # wyświetli 10
print(suma_b)  # wyświetli 60
```

### Funkcje z argumentami nazwanymi

Argumenty nazwane, przekazywane w postaci słownika za pomocą `**kwargs`, pozwalają na elastyczne i czytelne wywoływanie funkcji, szczególnie gdy mamy do czynienia z dużą liczbą opcjonalnych parametrów. `**kwargs` jest używane do przekazywania zmiennej liczby argumentów nazwanych do funkcji. Umożliwia to tworzenie bardziej uniwersalnych i wielokrotnego użytku funkcji, które mogą przyjmować różne zestawy argumentów w zależności od potrzeb wywołania.

Przykład:

```python
def zbuduj_adres(**kwargs):
    adres = ""
    if "ulica" in kwargs:
        adres += kwargs["ulica"] + ", "
    if "miasto" in kwargs:
        adres += kwargs["miasto"] + ", "
    if "kod_pocztowy" in kwargs:
        adres += kwargs["kod_pocztowy"] + ", "
    if "kraj" in kwargs:
        adres += kwargs["kraj"]
    return adres

# Przykład wywołania z pełnym zestawem argumentów
adres1 = zbuduj_adres(ulica="Kwiatowa 15", miasto="Warszawa", kod_pocztowy="00-001", kraj="Polska")
print(adres1)  # wyświetli: Kwiatowa 15, Warszawa, 00-001, Polska

# Przykład wywołania z brakującym argumentem "kod_pocztowy"
adres2 = zbuduj_adres(ulica="Kwiatowa 15", miasto="Warszawa", kraj="Polska")
print(adres2)  # wyświetli: Kwiatowa 15, Warszawa, Polska

# Przykład wywołania z brakującym argumentem "miasto" i "kod_pocztowy"
adres3 = zbuduj_adres(ulica="Kwiatowa 15", kraj="Polska")
print(adres3)  # wyświetli: Kwiatowa 15, Polska
```

W powyższym przykładzie, funkcja zbuduj_adres przyjmuje dowolną liczbę argumentów nazwanych. Argumenty te są następnie używane do zbudowania pełnego adresu, ale tylko te, które zostały przekazane do funkcji. Dzięki `**kwargs`, funkcja jest bardzo elastyczna i może być używana z różnymi zestawami argumentów bez konieczności ich wcześniejszego definiowania.
Zalety używania `**kwargs`

- Funkcje oferują dużą **elastyczność**, ponieważ mogą przyjmować dowolną liczbę argumentów, co jest szczególnie przydatne w sytuacjach, gdy liczba lub nazwy argumentów mogą się zmieniać w trakcie działania programu.
- Rozbudowa funkcji o nowe argumenty jest bardzo prosta, a jej struktura nie wymaga większych modyfikacji, co zdecydowanie wspiera **łatwość rozszerzania** i ułatwia przyszłe zmiany.
- Zastosowanie mechanizmu **kwargs** pozwala na przekazywanie argumentów jako nazwanych par, co pomaga **unikać błędów** związanych z nieprawidłową liczbą lub kolejnością argumentów, zwiększając niezawodność kodu.

### Podsumowanie typów argumentów

| Typ argumentu                | Składnia                | Przykład wywołania                   | Opis                                           |
|------------------------------|-------------------------|--------------------------------------|------------------------------------------------|
| Pozycyjny obowiązkowy        | `def f(a, b)`           | `f(1, 2)`                            | Musi być podany w odpowiedniej kolejności      |
| Domyślny (opcjonalny)       | `def f(a, b=10)`        | `f(1)` lub `f(1, 20)`               | Użyje wartości domyślnej jeśli nie podano      |
| `*args` (pozycyjne zbiorcze)| `def f(*args)`          | `f(1, 2, 3)`                         | Krotka dowolnej liczby argumentów pozycyjnych  |
| `**kwargs` (nazwane zbiorcze)| `def f(**kwargs)`      | `f(x=1, y=2)`                        | Słownik dowolnej liczby argumentów nazwanych   |
| Wyłącznie pozycyjne (`/`)   | `def f(a, b, /)`        | `f(1, 2)`                            | Nie można podać nazwy argumentu                |
| Wyłącznie nazwane (`*`)     | `def f(*, a, b)`        | `f(a=1, b=2)`                        | Muszą być przekazane z nazwą                   |
| Mieszane                     | `def f(a, /, b, *, c)` | `f(1, 2, c=3)` lub `f(1, b=2, c=3)` | Łączenie różnych typów                         |

### Dokumentowanie funkcji

Dokumentowanie funkcji jest kluczowe dla utrzymania przejrzystości i zrozumienia kodu. Python pozwala na dodawanie docstringów, które są specjalnymi komentarzami umieszczonymi bezpośrednio pod definicją funkcji. Przykład:

```python
def oblicz_pole_prostokata(dlugosc, szerokosc):
    """
    Funkcja oblicza pole prostokąta.

    Args:
        dlugosc (float): Długość prostokąta.
        szerokosc (float): Szerokość prostokąta.

    Returns:
        float: Pole prostokąta.
    """
    return dlugosc * szerokosc

pole = oblicz_pole_prostokata(5.0, 3.5)
print(pole)  # wyświetli: 17.5
```

### Zasięg zmiennych (scope)

Zasięg zmiennej określa, gdzie w kodzie dana zmienna jest widoczna i dostępna. Python stosuje reguły zasięgu opisywane skrótem **LEGB** (Local → Enclosing → Global → Built-in):

1. **Local** — zmienne zdefiniowane wewnątrz bieżącej funkcji.
2. **Enclosing** — zmienne zdefiniowane w funkcji zewnętrznej (dla funkcji zagnieżdżonych).
3. **Global** — zmienne zdefiniowane na poziomie modułu.
4. **Built-in** — nazwy wbudowane w Pythona (np. `len`, `print`, `range`).

Python przeszukuje te poziomy dokładnie w tej kolejności.

#### Zmienne lokalne

Zmienne utworzone wewnątrz funkcji są **lokalne** — widoczne tylko w tej funkcji i niszczone po jej zakończeniu:

```python
def powitaj():
    wiadomosc = "Cześć!"  # zmienna lokalna
    print(wiadomosc)

powitaj()           # Cześć!
# print(wiadomosc)  # NameError — zmienna nie istnieje poza funkcją
```

#### Zmienne globalne

Zmienne zdefiniowane na poziomie modułu są **globalne** — widoczne wewnątrz funkcji, ale domyślnie tylko do odczytu:

```python
licznik = 0  # zmienna globalna

def pokaz_licznik():
    print(licznik)  # można czytać

pokaz_licznik()  # 0
```

Aby **modyfikować** zmienną globalną wewnątrz funkcji, należy użyć słowa kluczowego `global`:

```python
licznik = 0

def zwieksz():
    global licznik
    licznik += 1

zwieksz()
zwieksz()
print(licznik)  # 2
```

> Nadużywanie zmiennych globalnych utrudnia zrozumienie i testowanie kodu. Preferuj przekazywanie wartości przez argumenty i zwracanie przez `return`.

#### Funkcje zagnieżdżone i zasięg enclosing

Funkcja zdefiniowana wewnątrz innej funkcji ma dostęp do zmiennych funkcji zewnętrznej (zasięg *enclosing*):

```python
def zewnetrzna():
    x = 10  # zasięg enclosing dla wewnetrzna()

    def wewnetrzna():
        print(x)  # dostęp do x z funkcji zewnętrznej

    wewnetrzna()

zewnetrzna()  # 10
```

Aby **modyfikować** zmienną z zasięgu *enclosing*, używamy słowa kluczowego `nonlocal`:

```python
def licznik():
    wartosc = 0

    def zwieksz():
        nonlocal wartosc
        wartosc += 1
        return wartosc

    return zwieksz

krok = licznik()
print(krok())  # 1
print(krok())  # 2
print(krok())  # 3
```

#### Domknięcia (closures)

Domknięcie (ang. *closure*) to funkcja wewnętrzna, która "zapamiętuje" zmienne z zasięgu funkcji zewnętrznej nawet po jej zakończeniu. Powyższy przykład z `licznik()` jest właśnie domknięciem — `zwieksz` nadal ma dostęp do `wartosc`, mimo że `licznik()` już zakończyła działanie.

Domknięcia są przydatne do tworzenia fabryk funkcji:

```python
def mnoznik(n):
    def pomnoz(x):
        return x * n  # n pochodzi z zasięgu enclosing
    return pomnoz

podwoj = mnoznik(2)
potroil = mnoznik(3)

print(podwoj(5))   # 10
print(potroil(5))  # 15
```

### Adnotacje typów (type hints)

Python jest dynamicznie typowany, ale od wersji 3.5 wspiera opcjonalne **adnotacje typów**, które zwiększają czytelność kodu i pozwalają narzędziom (np. `mypy`, `pyright`) wykrywać błędy:

```python
def dodaj(a: int, b: int) -> int:
    return a + b

def powiedz_czesc(imie: str, razy: int = 1) -> None:
    for _ in range(razy):
        print(f"Cześć, {imie}!")

def przetworz(dane: list[int]) -> dict[str, int]:
    return {"suma": sum(dane), "max": max(dane), "min": min(dane)}
```

Adnotacje nie są egzekwowane w czasie wykonania — są jedynie wskazówką dla programisty i narzędzi. Dostęp do nich można uzyskać przez `__annotations__`:

```python
print(dodaj.__annotations__)
# {'a': <class 'int'>, 'b': <class 'int'>, 'return': <class 'int'>}
```

Moduł `typing` dostarcza dodatkowych typów:

```python
from typing import Optional, Union, Callable, Tuple

def znajdz(lista: list[int], wartosc: int) -> Optional[int]:
    """Zwraca indeks lub None."""
    try:
        return lista.index(wartosc)
    except ValueError:
        return None

def zastosuj(f: Callable[[int], int], x: int) -> int:
    return f(x)

# Python 3.10+ — skrócona składnia Union za pomocą |
def parsuj(wartosc: str | int) -> int:
    return int(wartosc)
```

### Argumenty wyłącznie pozycyjne (`/`) i wyłącznie nazwane (`*`)

Python 3.8+ pozwala precyzyjnie kontrolować, jak argumenty muszą być przekazywane:

```python
# Argumenty PRZED / → wyłącznie pozycyjne (nie można podać nazwy)
# Argumenty PO * → wyłącznie nazwane (muszą być podane z nazwą)
def funkcja(poz1, poz2, /, normalny, *, kw1, kw2):
    pass

# Poprawne wywołania:
funkcja(1, 2, 3, kw1=4, kw2=5)
funkcja(1, 2, normalny=3, kw1=4, kw2=5)

# Niepoprawne — błąd:
# funkcja(poz1=1, poz2=2, normalny=3, kw1=4, kw2=5)  # poz1/poz2 muszą być pozycyjne
# funkcja(1, 2, 3, 4, 5)  # kw1/kw2 muszą być nazwane
```

Praktyczny przykład:

```python
def oblicz_sile(masa: float, przyspieszenie: float, /) -> float:
    """F = ma. Argumenty wyłącznie pozycyjne — kolejność ma znaczenie."""
    return masa * przyspieszenie

def nasluchuj(host: str, *, port: int, timeout: float = 30.0) -> None:
    """port jest wyłącznie nazwany — musi być podany explicite."""
    print(f"Słucham na {host}:{port} (timeout={timeout}s)")

nasluchuj("localhost", port=8080)
nasluchuj("0.0.0.0", port=443, timeout=60.0)
```
