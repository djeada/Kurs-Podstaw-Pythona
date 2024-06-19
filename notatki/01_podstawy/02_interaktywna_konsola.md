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
