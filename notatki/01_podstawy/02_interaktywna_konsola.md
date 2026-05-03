## Interaktywna konsola Pythona

Interaktywna konsola Pythona, znana również jako interpreter, to niezwykle przydatne narzędzie umożliwiające natychmiastowe wykonywanie instrukcji w języku Python. Dzięki niej możemy szybko testować fragmenty kodu, eksplorować biblioteki, debugować problemy oraz uczyć się nowych funkcji języka w sposób dynamiczny i interaktywny.

### Uruchomienie konsoli

Aby otworzyć interaktywną konsolę Pythona, należy uruchomić wiersz poleceń (na przykład `cmd` lub `PowerShell` w systemie Windows, `Terminal` w systemie macOS lub Linux) i wpisać polecenie `python`. Po jego wykonaniu powinna pojawić się informacja o wersji Pythona oraz znak zachęty (`>>>`), co oznacza, że konsola jest gotowa do przyjmowania poleceń.

```
$ python
Python 3.9.6 (default, Jul 30 2021, 16:36:19)
[Clang 12.0.0 (clang-1200.0.32.29)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
```

### Wykonywanie poleceń

Interaktywna konsola umożliwia wykonywanie pojedynczych poleceń Pythona, co jest niezwykle pomocne podczas nauki i testowania kodu. Wprowadź instrukcję i naciśnij `Enter`, aby ją wykonać. Oto kilka przykładów prostych poleceń:

```
2 + 3
5

print("Witaj, świecie!")
Witaj, świecie!
```

Konsola pozwala również na definiowanie funkcji, korzystanie z pętli oraz warunków, co umożliwia testowanie bardziej złożonych fragmentów kodu w czasie rzeczywistym.

### Eksploracja bibliotek

Jedną z największych zalet korzystania z interaktywnej konsoli jest możliwość szybkiego eksplorowania bibliotek Pythona. Możemy importować biblioteki i natychmiast sprawdzać ich funkcjonalności. Na przykład, aby uzyskać wartość liczby π z biblioteki `math`:

```
import math
math.pi
3.141592653589793
```

### Definiowanie zmiennych i funkcji

Konsola pozwala również na definiowanie zmiennych i funkcji, co umożliwia przechowywanie danych i tworzenie bardziej złożonych programów:

```
a = 10
b = 20
def suma(x, y):
  return x + y
...
...
suma(a, b)
30
```

### Praca z pakietami i modułami

Możesz również korzystać z zewnętrznych pakietów i modułów, instalując je za pomocą `pip` i importując do swojego środowiska pracy:

```
import requests
response = requests.get("https://api.github.com")
response.status_code
200
```

### Pomoc i dokumentacja

Interaktywna konsola oferuje również wbudowane funkcje pomocy, które są niezwykle przydatne podczas nauki i debugowania. Używając funkcji `help()`, możemy uzyskać informacje o funkcjach, modułach i klasach:

```
help(math)
```

Funkcja `dir()` może być użyta do wyświetlenia wszystkich atrybutów i metod obiektu:

```
dir(math)
['doc', 'loader', 'name', 'package', 'spec', 'acos', 'acosh', 'asin', 'asinh', ...]
```

### Zakończenie pracy z konsolą

Aby zakończyć sesję w interaktywnej konsoli Pythona, wystarczy wpisać komendę `exit()` lub użyć skrótu klawiszowego `Ctrl+D` (w systemach Unix) lub `Ctrl+Z` (w systemie Windows).

```
exit()
```

## Wejście i wyjście danych

Programy często muszą komunikować się z użytkownikiem: wyświetlać wyniki i pobierać dane. Python udostępnia dwa wbudowane narzędzia: `print()` do wypisywania danych i `input()` do ich pobierania.

### Funkcja `print()`

`print()` wypisuje wartości na standardowe wyjście (konsolę). Można jej przekazać dowolną liczbę argumentów:

```python
print("Cześć!")                     # Cześć!
print("Wynik:", 42)                 # Wynik: 42
print(1, 2, 3)                      # 1 2 3
print(1, 2, 3, sep=", ")            # 1, 2, 3
print("Linia 1", end=" | ")
print("Linia 2")                    # Linia 1 | Linia 2
```

Parametry funkcji `print()`:

| Parametr | Domyślnie | Opis |
|----------|-----------|------|
| `sep`    | `" "`     | Separator między argumentami |
| `end`    | `"\n"`    | Znak kończący (domyślnie nowa linia) |
| `file`   | `sys.stdout` | Plik wyjściowy |

#### Formatowanie napisów

Python oferuje kilka sposobów formatowania napisów:

```python
imie = "Jan"
wiek = 30

# f-stringi (zalecane, Python 3.6+)
print(f"Witaj, {imie}! Masz {wiek} lat.")

# Metoda .format()
print("Witaj, {}! Masz {} lat.".format(imie, wiek))

# Operator % (starszy styl)
print("Witaj, %s! Masz %d lat." % (imie, wiek))
```

Formatowanie liczb:

```python
pi = 3.14159265

print(f"{pi:.2f}")     # '3.14'    — dwa miejsca po przecinku
print(f"{pi:8.3f}")    # '   3.142' — szerokość pola 8 (z wiodącymi spacjami), 3 miejsca po przecinku
print(f"{1000000:,}")  # 1,000,000 — separator tysięcy
print(f"{255:#x}")     # 0xff — liczba szesnastkowa
```

### Funkcja `input()`

`input()` wczytuje tekst wpisany przez użytkownika z klawiatury. Funkcja zawsze zwraca wartość jako napis (`str`), nawet jeśli użytkownik wpisał liczbę:

```python
napis = input("Podaj swoje imię: ")
print(f"Witaj, {napis}!")
```

#### Konwersja wejścia

Aby pracować z liczbami, należy jawnie przekonwertować wynik:

```python
liczba = int(input("Podaj liczbę całkowitą: "))
print(f"Podwojena wartość: {liczba * 2}")

zmiennoprzec = float(input("Podaj liczbę zmiennoprzecinkową: "))
print(f"Kwadrat: {zmiennoprzec ** 2:.2f}")
```

#### Pobieranie wielu wartości

```python
# Podział wejścia na elementy (domyślnie według spacji)
a, b = input("Podaj dwie liczby: ").split()
a, b = int(a), int(b)
print(f"Suma: {a + b}")

# Skrócony zapis
liczby = list(map(int, input("Podaj kilka liczb: ").split()))
print(f"Suma: {sum(liczby)}")
```

#### Zabezpieczenie przed błędnym wejściem

```python
while True:
    try:
        n = int(input("Podaj liczbę całkowitą: "))
        break
    except ValueError:
        print("To nie jest liczba całkowita. Spróbuj ponownie.")

print(f"Wpisałeś: {n}")
```
