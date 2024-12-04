## Argumenty linii poleceń

Python oferuje wszechstronne narzędzia do obsługi argumentów linii poleceń, umożliwiając tworzenie elastycznych i konfigurowalnych skryptów. W zależności od wymagań, można skorzystać zarówno z prostego modułu `sys`, jak i bardziej zaawansowanego `argparse`, które dostarczają różnorodne możliwości w zakresie przetwarzania argumentów.

### Podstawowa obsługa argumentów za pomocą modułu `sys`

Moduł `sys` z biblioteki standardowej Pythona udostępnia zmienną `argv`, która jest listą przechowującą nazwę programu oraz argumenty przekazane z linii poleceń. Jest to najprostszy sposób na dostęp do argumentów, jednak wymaga ręcznej obsługi i walidacji danych.

#### Przykład prostego skryptu sumującego liczby

Oto jak można stworzyć prosty skrypt `suma.py`, który sumuje liczby przekazane jako argumenty:

```python
import sys

# Sprawdzenie, czy użytkownik przekazał odpowiednią liczbę argumentów
if len(sys.argv) < 2:
    print("Użycie: python suma.py liczba1 liczba2 ...")
    sys.exit(1)

try:
    # Konwersja argumentów na liczby całkowite i sumowanie
    liczby = map(int, sys.argv[1:])
    wynik = sum(liczb)
    print(wynik)
except ValueError:
    print("Wszystkie argumenty muszą być liczbami całkowitymi.")
    sys.exit(1)
```

#### Uruchamianie skryptu

Uruchamiając skrypt, można przekazać liczby jako argumenty:

```bash
$ python suma.py 3 2 1
6
```

Jeśli użytkownik nie poda argumentów lub poda nieprawidłowe wartości, skrypt wyświetli odpowiedni komunikat o błędzie.

### Zaawansowane zarządzanie argumentami z użyciem `argparse`

Moduł `argparse` jest bardziej zaawansowanym narzędziem do obsługi argumentów linii poleceń. Umożliwia definiowanie różnych typów argumentów, automatyczne generowanie pomocy, weryfikację typów danych, obsługę wartości domyślnych oraz subkomend, co jest szczególnie przydatne w bardziej złożonych aplikacjach.

#### Główne cechy modułu `argparse`

1. Pozwala na definiowanie argumentów, które są wymagane oraz tych, które są opcjonalne.
2. Na podstawie zdefiniowanych argumentów, `argparse` generuje automatycznie tekst pomocy, dostępny pod opcją `-h` lub `--help`.
3. Możliwość określenia typu danych dla każdego argumentu, co pozwala na automatyczną konwersję i walidację.
4. Definiowanie wartości domyślnych dla argumentów opcjonalnych.
5. Umożliwia tworzenie skryptów z wieloma subkomendami, co zwiększa modularność i czytelność kodu.

#### Przykład skryptu z użyciem `argparse`

Poniżej znajduje się przykład skryptu, który dodaje linię do podanego pliku, korzystając z `argparse`:

```python
import argparse

# Inicjalizacja parsera z opisem skryptu
parser = argparse.ArgumentParser(description="Dodaje linię do podanego pliku.")

# Dodanie argumentu pozycyjnego
parser.add_argument("plik", help="Ścieżka do pliku do modyfikacji.")

# Dodanie argumentu opcjonalnego z wartością domyślną
parser.add_argument("-t", "--tekst", help="Tekst do dodania do pliku", default="Domyślna linia")

# Dodanie argumentu liczbowego z domyślną wartością i weryfikacją typu
parser.add_argument("-l", "--liczba", help="Przykład argumentu liczbowego", type=int, default=10)

# Parsowanie argumentów
args = parser.parse_args()

# Operacja na podstawie przekazanych argumentów
with open(args.plik, 'a') as file:
    file.write(f"\n{args.tekst}")
```

#### Przykłady użycia skryptu

I. **Wywołanie z pomocą `-h` (lub `--help`)**:

To wywołanie wyświetli automatycznie generowaną pomoc, którą `argparse` tworzy na podstawie zdefiniowanych argumentów.

```bash
$ python skrypt.py -h
```

**Wynik:**

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

II. **Proste wywołanie z podaniem tylko nazwy pliku**:

Skrypt doda do pliku "plik.txt" linię "Domyślna linia".

```bash
$ python skrypt.py plik.txt
```

III. **Dodawanie własnego tekstu do pliku**:

Skrypt doda do pliku "plik.txt" linię "Moja własna linia".

```bash
$ python skrypt.py plik.txt -t "Moja własna linia"
```

#### Rozszerzenie funkcjonalności skryptu

Aby skrypt był bardziej elastyczny, można zdefiniować własne komunikaty błędów lub grupować argumenty, co jest szczególnie przydatne w bardziej złożonych aplikacjach. Moduł `argparse` umożliwia to poprzez klasy wyjątków, takie jak `argparse.ArgumentTypeError`.

#### Definiowanie subkomend za pomocą `argparse`

Moduł `argparse` pozwala na definiowanie subkomend, co umożliwia tworzenie skryptów przypominających popularne narzędzia, takie jak `git`, gdzie mamy wiele subkomend (`git commit`, `git push` itd.).

##### Przykład dodania subkomend

Poniżej znajduje się przykład skryptu, który obsługuje subkomendy `dodaj` i `odejmij`:

```python
import argparse

# Inicjalizacja głównego parsera
parser = argparse.ArgumentParser(description="Przykład użycia subkomend w argparse.")

# Dodanie subparserów - obiekt będzie używany do dodawania subkomend
subparsers = parser.add_subparsers(dest="subkomenda", required=True, help="Dostępne subkomendy")

# Dodanie subkomendy 'dodaj'
parser_dodaj = subparsers.add_parser('dodaj', help="Dodaje dwie liczby.")
parser_dodaj.add_argument("a", type=int, help="Pierwsza liczba")
parser_dodaj.add_argument("b", type=int, help="Druga liczba")

# Dodanie subkomendy 'odejmij'
parser_odejmij = subparsers.add_parser('odejmij', help="Odejmuje drugą liczbę od pierwszej.")
parser_odejmij.add_argument("a", type=int, help="Pierwsza liczba")
parser_odejmij.add_argument("b", type=int, help="Druga liczba")

# Parsowanie argumentów
args = parser.parse_args()

# Wykonanie odpowiedniej operacji na podstawie subkomendy
if args.subkomenda == 'dodaj':
    wynik = args.a + args.b
    print(f"Wynik dodawania: {wynik}")
elif args.subkomenda == 'odejmij':
    wynik = args.a - args.b
    print(f"Wynik odejmowania: {wynik}")
```

##### Przykładowe wywołania skryptu

I. **Dodawanie dwóch liczb:**

```bash
$ python skrypt.py dodaj 5 3
Wynik dodawania: 8
```

II. **Odejmowanie dwóch liczb:**

```bash
$ python skrypt.py odejmij 5 3
Wynik odejmowania: 2
```

### Przechowywanie konfiguracji w plikach

Dla skomplikowanych skryptów, w których liczba argumentów jest znaczna, warto rozważyć przechowywanie konfiguracji w zewnętrznych plikach konfiguracyjnych. Pozwala to na bardziej przejrzystą organizację ustawień oraz ułatwia zarządzanie konfiguracją dla różnych środowisk.

#### Korzystanie z modułu `configparser`

Moduł `configparser` umożliwia czytanie i zapisywanie plików konfiguracyjnych w formacie INI, które są łatwe do czytania i edycji.

##### Przykład pliku konfiguracyjnego `konfiguracja.ini`

```ini
[DEFAULT]
nazwa_pliku = plik.txt
tekst = Linia z pliku konfiguracyjnego
liczba = 20
```

##### Przykład skryptu odczytującego konfigurację

```python
import argparse
import configparser

# Inicjalizacja parsera argumentów
parser = argparse.ArgumentParser(description="Skrypt z konfiguracją z pliku.")
parser.add_argument("-c", "--config", help="Ścieżka do pliku konfiguracyjnego", default="konfiguracja.ini")
args = parser.parse_args()

# Inicjalizacja parsera konfiguracji
config = configparser.ConfigParser()
config.read(args.config)

# Odczytanie wartości z pliku konfiguracyjnego
nazwa_pliku = config['DEFAULT'].get('nazwa_pliku', 'domyślny_plik.txt')
tekst = config['DEFAULT'].get('tekst', 'Domyślna linia z konfiguracji')
liczba = config['DEFAULT'].getint('liczba', 10)

# Przykładowe użycie odczytanych wartości
print(f"Plik: {nazwa_pliku}")
print(f"Tekst: {tekst}")
print(f"Liczba: {liczba}")
```

##### Uruchamianie skryptu z plikiem konfiguracyjnym

```bash
$ python skrypt.py -c konfiguracja.ini
Plik: plik.txt
Tekst: Linia z pliku konfiguracyjnego
Liczba: 20
```

#### Zalety korzystania z plików konfiguracyjnych

- Umożliwia oddzielenie kodu programu od jego ustawień, co ułatwia utrzymanie i rozwój skryptu.
- Użytkownicy mogą łatwo zmieniać ustawienia bez konieczności modyfikowania kodu źródłowego.
- Możliwość tworzenia różnych plików konfiguracyjnych dla różnych środowisk (np. testowego, produkcyjnego).

### Dodatkowe możliwości modułu `argparse`

Moduł `argparse` oferuje wiele dodatkowych funkcji, które mogą być przydatne w bardziej zaawansowanych zastosowaniach:

1. **Grupowanie argumentów** pozwala na organizowanie argumentów w logiczne grupy, co zwiększa czytelność pomocy oraz ułatwia zarządzanie dużą liczbą opcji.

```python
import argparse

parser = argparse.ArgumentParser(description="Skrypt z grupowanymi argumentami.")

grupa_wejsciowa = parser.add_argument_group('Wejście')
grupa_wejsciowa.add_argument('--input', help="Plik wejściowy", required=True)

grupa_wyjscia = parser.add_argument_group('Wyjście')
grupa_wyjscia.add_argument('--output', help="Plik wyjściowy", required=True)

args = parser.parse_args()
```

2. **Argumenty wzajemnie wykluczające się** umożliwiają definiowanie argumentów, z których tylko jeden może być użyty naraz.

```python
import argparse

parser = argparse.ArgumentParser(description="Skrypt z argumentami wzajemnie wykluczającymi się.")

grupa = parser.add_mutually_exclusive_group()
grupa.add_argument('--verbose', action='store_true', help="Tryb szczegółowy")
grupa.add_argument('--quiet', action='store_true', help="Tryb cichy")

args = parser.parse_args()
```

III. **Argumenty wielokrotnego użytku** pozwala na definiowanie argumentów, które mogą wystąpić wielokrotnie, na przykład listy wartości.

```python
import argparse

parser = argparse.ArgumentParser(description="Skrypt z argumentem wielokrotnego użytku.")
parser.add_argument('--num', type=int, action='append', help="Liczba do dodania (może wystąpić wiele razy)")

args = parser.parse_args()
print(f"Liczby: {args.num}")
```

**Przykładowe wywołanie:**

```bash
$ python skrypt.py --num 1 --num 2 --num 3
Liczby: [1, 2, 3]
```

### Integracja z innymi modułami

Moduł `argparse` można łatwo integrować z innymi modułami Pythona, co pozwala na tworzenie bardziej złożonych i funkcjonalnych skryptów. Na przykład, można połączyć `argparse` z modułami do obsługi plików, baz danych czy sieci, aby stworzyć wszechstronne narzędzia do automatyzacji zadań.

#### Przykład integracji z modułem `pathlib`

Moduł `pathlib` umożliwia wygodne operacje na ścieżkach plików. Połączenie go z `argparse` może znacznie ułatwić manipulację plikami przekazanymi jako argumenty.

```python
import argparse
from pathlib import Path

parser = argparse.ArgumentParser(description="Skrypt operujący na plikach z użyciem pathlib.")
parser.add_argument("plik", type=Path, help="Ścieżka do pliku.")

args = parser.parse_args()

if args.plik.exists():
    print(f"Plik {args.plik} istnieje.")
    if args.plik.is_file():
        print(f"Rozmiar pliku: {args.plik.stat().st_size} bajtów.")
else:
    print(f"Plik {args.plik} nie istnieje.")
```

**Przykładowe wywołanie:**

```bash
$ python skrypt.py przykładowy_plik.txt
Plik przykładowy_plik.txt istnieje.
Rozmiar pliku: 1024 bajtów.
```

### Dobre praktyki przy obsłudze argumentów linii poleceń

1. Opisy argumentów powinny być zrozumiałe i precyzyjne, co ułatwia użytkownikom korzystanie ze skryptu.
2. Zawsze sprawdzaj poprawność przekazywanych argumentów, aby uniknąć błędów w działaniu skryptu.
3. Definiowanie sensownych wartości domyślnych dla argumentów opcjonalnych może zwiększyć użyteczność skryptu.
4. Upewnij się, że skrypt zawiera odpowiednią dokumentację, zwłaszcza jeśli jest przeznaczony do użytku przez innych użytkowników.
5. W miarę możliwości, dziel skrypt na mniejsze funkcje lub moduły, co ułatwia zarządzanie kodem i jego rozwój.
6. Implementuj odpowiednie mechanizmy obsługi błędów, aby skrypt reagował na nieprzewidziane sytuacje w kontrolowany sposób.
