## Argumenty linii poleceń

Python oferuje wszechstronne narzędzia do obsługi argumentów linii poleceń, co pozwala na tworzenie elastycznych i konfigurowalnych skryptów. W zależności od potrzeb, można wykorzystać zarówno prosty moduł `sys`, jak i bardziej zaawansowany `argparse`.

### Podstawowa obsługa argumentów za pomocą modułu `sys`

Moduł `sys` z biblioteki standardowej Pythona udostępnia zmienną `argv`. Ta zmienna jest listą, która przechowuje nazwę programu oraz argumenty przekazane z linii poleceń.

Oto jak możemy stworzyć prosty skrypt `suma.py`, który sumuje liczby przekazane jako argumenty:

```python
import sys

# Zakładając, że wszystkie argumenty to liczby, konwertujemy je i sumujemy
liczby = map(int, sys.argv[1:])
print(sum(liczby))
```

Uruchamiając skrypt, otrzymamy:

```bash
$ python suma.py 3 2 1
6
```

### Zaawansowane zarządzanie argumentami z użyciem `argparse`

Moduł `argparse` to potężne narzędzie umożliwiające zaawansowaną obsługę argumentów linii poleceń. Oto kilka głównych cech i zalet tego modułu:

1. Obsługa pozycyjnych i opcjonalnych argumentów
2. Automatyczne generowanie pomocy
3. Weryfikacja typów argumentów
4. Obsługa wartości domyślnych
5. Obsługa subkomend, które można stosować w bardziej złożonych aplikacjach

```python
import argparse
from pathlib import Path

# Inicjalizacja parsera z opisem skryptu
parser = argparse.ArgumentParser(description="Dodaje linię do podanego pliku.")

# Dodanie argumentu pozycyjnego
parser.add_argument("plik", help="Ścieżka do pliku do modyfikacji.")

# Dodanie argumentu opcjonalnego z wartością domyślną
parser.add_argument("-t", "--tekst", help="Tekst do dodania do pliku", default="Domyślna linia")

# Dodanie argumentu liczbowego z domyślną wartością i weryfikacją typu
parser.add_argument("-l", "--liczba", help="Przykład argumentu liczbowego", type=int, default=10)

args = parser.parse_args()

# Przykład działania na podstawie przekazanych argumentów
with open(args.plik, 'a') as file:
    file.write(f"\n{args.tekst}")
```

Oto kilka przykładów wywołań dla skryptu:

1. Wywołanie z pomocą `-h` (lub `--help`):

To wywołanie pokaże automatycznie generowaną pomoc, którą argparse tworzy na podstawie zdefiniowanych argumentów.

```bash
$ python skrypt.py -h
```

Wynik:

```
usage: skrypt.py [-h] [-t TEKST] [-l LICZBA] plik

Dodaje linię do podanego pliku.

positional arguments:
  plik                  Ścieżka do pliku do modyfikacji.

optional arguments:
  -h, --help            show this help message and exit
  -t TEKST, --tekst TEKST
                        Tekst do dodania do pliku (default: Domyślna linia)
  -l LICZBA, --liczba LICZBA
                        Przykład argumentu liczbowego (default: 10)
```

2. Proste wywołanie z podaniem tylko nazwy pliku:

W tym przypadku skrypt doda do pliku "plik.txt" linię "Domyślna linia".

```bash
$ python skrypt.py plik.txt
```

3. Dodawanie własnego tekstu do pliku:

Skrypt doda do pliku "plik.txt" linię "Moja własna linia".

```bash
$ python skrypt.py plik.txt -t "Moja własna linia"
```

Dzięki takiemu podejściu, nasz skrypt jest bardziej elastyczny. Jeśli chcielibyśmy dodatkowo zdefiniować własne komunikaty błędów, `argparse` umożliwia to poprzez klasy wyjątków takich jak `argparse.ArgumentTypeError`. Możemy też grupować argumenty, co przydaje się w bardziej złożonych aplikacjach.

Warto również zwrócić uwagę na fakt, że `argparse` pozwala na definiowanie subkomend. Dzięki temu można tworzyć skrypty przypominające popularne narzędzia, takie jak `git`, gdzie mamy wiele subkomend (`git commit`, `git push` itd.).

Oto jak możemy dodać subkomendy w naszym skrypcie za pomocą `argparse`:

```python
import argparse

# Inicjalizacja głównego parsera
parser = argparse.ArgumentParser(description="Przykład użycia subkomend w argparse.")

# Dodajemy subparser - ten obiekt będzie używany do dodawania subkomend
subparsers = parser.add_subparsers(dest="subkomenda")

# Dodanie subkomendy 'dodaj'
parser_dodaj = subparsers.add_parser('dodaj', help="Dodaje dwie liczby.")
parser_dodaj.add_argument("a", type=int, help="Pierwsza liczba")
parser_dodaj.add_argument("b", type=int, help="Druga liczba")

# Dodanie subkomendy 'odejmij'
parser_odejmij = subparsers.add_parser('odejmij', help="Odejmuje drugą liczbę od pierwszej.")
parser_odejmij.add_argument("a", type=int, help="Pierwsza liczba")
parser_odejmij.add_argument("b", type=int, help="Druga liczba")

args = parser.parse_args()

if args.subkomenda == 'dodaj':
    wynik = args.a + args.b
    print(f"Wynik dodawania: {wynik}")
elif args.subkomenda == 'odejmij':
    wynik = args.a - args.b
    print(f"Wynik odejmowania: {wynik}")
```

Dzięki takiemu podejściu, możemy teraz wywołać nasz skrypt z różnymi subkomendami:

```bash
$ python skrypt.py dodaj 5 3
Wynik dodawania: 8

$ python skrypt.py odejmij 5 3
Wynik odejmowania: 2
```

Dzięki subkomendom skrypt staje się bardziej elastyczny i modularny, a także łatwiejszy w obsłudze dla użytkownika końcowego.


### Przechowywanie konfiguracji w plikach

Dla skomplikowanych skryptów, gdzie liczba argumentów jest duża, warto rozważyć przechowywanie konfiguracji w zewnętrznych plikach konfiguracyjnych, a następnie wczytywanie ich za pomocą odpowiednich modułów, takich jak `configparser`.

```python
import configparser

config = configparser.ConfigParser()
config.read('konfiguracja.ini')

# Odczytanie wartości z pliku konfiguracyjnego
nazwa_pliku = config['DEFAULT']['nazwa_pliku']
```

Takie podejście pozwala na bardziej przejrzystą organizację argumentów i ułatwia zarządzanie konfiguracją dla różnych środowisk.
