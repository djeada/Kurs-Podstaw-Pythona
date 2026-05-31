## Dbanie o jakość kodu i lintowanie

Kod może być składniowo poprawny, ale jednocześnie nieczytelny lub źle zorganizowany. Przestrzeganie pewnych standardów i konwencji pisania kodu jest niezbędne, zwłaszcza gdy w projekcie uczestniczy wielu programistów. Konwencje te opisane są w dokumentach PEP (Python Enhancement Proposals), a wśród nich wyróżniają się **PEP8** (styl kodowania) oraz **PEP257** (docstringi).

Aby pomóc programistom w przestrzeganiu tych konwencji, stworzono narzędzia do tzw. lintowania kodu, takie jak **Pylint**, **Black**, **Flake8** czy **autoflake**.

### Pylint

`Pylint` jest jednym z najpopularniejszych narzędzi lintujących dla języka Python. Jest używany do analizowania kodu źródłowego w celu znalezienia błędów programistycznych, pomagania w przestrzeganiu konwencji stylu kodowania, i sugerowania możliwości poprawy kodu.

#### Co robi Pylint?

1. Pylint sprawdza błędy w kodzie Pythona, potencjalne błędy, zgodność ze stylem kodowania PEP8, PEP257 i wiele innych.
2. Dostarcza szczegółowe raporty o problemach w kodzie, w tym o problemach związanych ze stylami, błędami i ostrzeżeniami.
3. Sugeruje zmiany, które mogą poprawić strukturę i czytelność kodu, a także wydajność.
4. Może być rozszerzony za pomocą wtyczek, które mogą dodać nowe funkcje lub dostosować istniejące funkcjonalności.

#### Jak działa Pylint?

Pylint działa przez analizę modułów Pythona, które są przekazywane jako argumenty w linii poleceń. Skanuje on moduły, szuka konfiguracji w plikach `pylintrc` lub `setup.cfg`, a następnie generuje raport na podstawie tych analiz.

#### Instalacja Pylint

Pylint można łatwo zainstalować za pomocą pip:

```bash
pip install pylint
```

#### Użycie Pylint

Aby użyć Pylint do sprawdzenia pliku, wystarczy uruchomić:

```bash
pylint nazwa_pliku.py
```

Pylint oceni kod i wygeneruje raport, wskazując wszystkie znalezione problemy.

#### Konfiguracja Pylint

Pylint jest wysoce konfigurowalny. Można dostosować jego zachowanie poprzez modyfikację pliku konfiguracyjnego `.pylintrc`. Można utworzyć ten plik komendą:

```bash
pylint --generate-rcfile > .pylintrc
```

W pliku `.pylintrc` można dostosować różne aspekty Pylint, takie jak:

- **disable**: Wyłączanie określonych ostrzeżeń.
- **enable**: Włączanie dodatkowych sprawdzeń.
- **good-names**: Lista nazw, które są zawsze akceptowalne.
- **max-line-length**: Maksymalna długość linii kodu.
- **variable-rgx**: Wyrażenie regularne opisujące dopuszczalne nazwy zmiennych.

#### Przykładowe ustawienia .pylintrc

Aby wyłączyć sprawdzanie długości linii i ignorować ostrzeżenia o zbyt mało skomplikowanych nazwach zmiennych, możesz dodać do pliku `.pylintrc`:

```ini
[FORMAT]
max-line-length=120

[BASIC]
good-names=i,j,k,ex,Run,_
```

#### Rozszerzanie Pylint

Pylint może być rozszerzony za pomocą wtyczek, które można instalować oddzielnie lub pisać samodzielnie. Wtyczki mogą być ładowane poprzez dodanie ich do pliku konfiguracyjnego.

```ini
load-plugins=pylint_django
```

### Black - The Uncompromising Code Formatter

`Black` to nowoczesne narzędzie do formatowania kodu Python, które ma na celu zapewnienie jednolitego stylu kodowania. Jest promowane jako "bezkompromisowy" formatowacz kodu, ponieważ nie oferuje szerokiej gamy opcji konfiguracyjnych, co w praktyce oznacza, że każdy używający Black'a kod będzie wyglądać bardzo podobnie.

#### Co robi Black?

1. Black automatycznie formatuje kod, przekształcając go w styl, który jest zgodny z PEP8 (z kilkoma wyjątkami). Celem jest, aby kod był nie tylko zgodny ze standardami, ale także czytelny i zrozumiały.
2. Chociaż Black robi pewne odstępstwa od standardowej specyfikacji PEP8 (np. dłuższe linie kodu), generalnie jego działanie jest zgodne z duchem tego przewodnika po stylu.
3. Black jest deterministyczny, co oznacza, że wielokrotne uruchomienie Black na tym samym kodzie zawsze da ten sam wynik.

#### Instalacja Black

Można zainstalować Black za pomocą pip:

```bash
pip install black
```

#### Użycie Black

Aby sformatować plik kodu Pythona, użyj:

```bash
black nazwa_pliku.py
```

Możesz także uruchomić Black na całym katalogu, aby sformatować wszystkie pliki Pythona w nim zawarte:

```bash
black sciezka/do/katalogu
```

#### Konfiguracja Black

Black oferuje ograniczone możliwości konfiguracji, ale można dostosować niektóre aspekty, takie jak długość linii. Domyślnie, Black formatuje kod z maksymalną długością linii wynoszącą 88 znaków. Można to zmienić przy użyciu opcji `--line-length`:

```bash
black --line-length 100 nazwa_pliku.py
```

Jeśli chcesz, aby Black sprawdzał pliki bez ich formatowania (tryb "check mode"), możesz użyć opcji `--check`:

```bash
black --check sciezka/do/katalogu
```

To sprawdzi, czy pliki są już sformatowane zgodnie z regułami Black, bez wprowadzania zmian.

#### Integracja Black z innymi narzędziami

Black można łatwo zintegrować z edytorami kodu, takimi jak VS Code, PyCharm, czy Sublime Text, oraz z systemami kontroli wersji poprzez hooki git. Dla przykładu, konfiguracja pre-commit hook dla Git może wyglądać tak:

```yaml
repos:
  - repo: https://github.com/psf/black
    rev: stable
    hooks:
      - id: black
        language_version: python3
```

#### Zalety

- Eliminuje dyskusje o stylu kodowania w zespołach.
- Oszczędza czas podczas code review, skupiając uwagę na logice zamiast na stylu.
- Poprawia czytelność kodu dzięki spójnemu formatowaniu.

#### Wady

- Brak szerokich możliwości konfiguracyjnych może być ograniczający dla niektórych zespołów.
- Deterministyczne podejście do formatowania może nie odpowiadać wszystkim programistom.

### Flake8

`Flake8` jest potężnym narzędziem do analizy statycznej kodu Python, które łączy w sobie funkcje stylu kodowania, błędów programistycznych i kontroli złożoności kodu. Jest szeroko używane przez programistów Pythona dla utrzymania czystości kodu i zgodności z PEP8.

#### Co robi Flake8?

1. Flake8 analizuje kod pod kątem zgodności ze standardem PEP8, co obejmuje formatowanie, spację, nazewnictwo zmiennych, i inne.
2. Narzędzie to identyfikuje błędy składniowe oraz typowe błędy programistyczne, które mogą prowadzić do błędów w czasie wykonania.
3. Flake8 może ocenić złożoność cyklomatyczną kodu, co jest miarą skomplikowania kodu na podstawie ilości ścieżek wykonania.
4. Może być rozszerzone o dodatkowe wtyczki, które dostarczają dodatkowej funkcjonalności analizy kodu.

#### Instalacja Flake8

Flake8 można zainstalować za pomocą pip, co jest standardowym sposobem instalacji narzędzi Pythona:

```bash
pip install flake8
```

#### Użycie Flake8

Podstawowe użycie Flake8 polega na uruchomieniu narzędzia w katalogu projektu lub na określonym pliku:

```bash
flake8 sciezka/do/pliku.py
```

Możesz również uruchomić Flake8 na wielu plikach lub całych katalogach:

```bash
flake8 sciezka/do/katalogu/
```

#### Konfiguracja Flake8

Flake8 jest konfigurowalny za pomocą pliku konfiguracyjnego `.flake8`, który można umieścić w katalogu głównym projektu. Można w nim określić różne opcje, takie jak:

- **exclude**: Pliki i katalogi, które mają być ignorowane.
- **max-line-length**: Maksymalna dozwolona długość linii.
- **ignore**: Błędy, które mają być ignorowane.
- **max-complexity**: Maksymalna dozwolona złożoność cyklomatyczna.

Przykładowy plik konfiguracyjny może wyglądać tak:

```ini
[flake8]
exclude = .git,__pycache__,docs/source/conf.py,old,build,dist
max-line-length = 120
ignore = E402
max-complexity = 10
```

#### Integracja z IDE

Flake8 można łatwo zintegrować z popularnymi środowiskami programistycznymi (IDE), takimi jak PyCharm, Visual Studio Code czy Sublime Text, co pozwala na bieżące analizowanie kodu podczas jego pisania.

#### Zalety

- Poprawia jakość kodu przez identyfikację i naprawę błędów stylu oraz programistycznych.
- Zmniejsza prawdopodobieństwo subtelnych błędów i ułatwia utrzymanie spójnego stylu kodowania w zespole.

#### Wady

- Konfiguracja wymaga pewnej wiedzy i może być czasochłonna dla dużych projektów.
- Niektóre wtyczki mogą spowalniać działanie narzędzia, zwłaszcza w dużych projektach.

### Porównanie narzędzi

| Cechy                           | Black | Pylint | Flake8  |
|---------------------------------|-------|--------|---------|
| Automatyczna korekcja           | Tak   | Nie    | Nie     |
| Wskazówki dotyczące stylu       | Nie   | Tak    | Tak     |
| Wyszukiwanie błędów             | Nie   | Tak    | Tak     |
| Ostrzeżenia o złożoności kodu   | Nie   | Tak    | Tak     |
| Dostępność pluginów             | Nie   | Tak    | Tak     |
| Możliwość konfiguracji          | Nie   | Tak    | Tak     |
| Integracja z IDE                | Tak   | Tak    | Tak     |
| Sprawdzanie typów (Type hints)  | Nie   | Tak    | Nie     |

### Sprawdzanie typów — `mypy` i `pyright`

Statyczna analiza typów wychwytuje błędy typów bez uruchamiania kodu:

```bash
pip install mypy
mypy skrypt.py
```

```python
# skrypt.py
def oblicz_vat(kwota: float, stawka: float = 0.23) -> float:
    return kwota * stawka

wynik = oblicz_vat("100")   # mypy: error: Argument 1 to "oblicz_vat" has incompatible type "str"; expected "float"
```

`pyright` (od Microsoftu, używany w VS Code) oferuje jeszcze szybszą i bardziej precyzyjną analizę:

```bash
pip install pyright
pyright skrypt.py
```

### Pre-commit hooks

`pre-commit` pozwala automatycznie uruchamiać narzędzia jakości kodu przed każdym commitem:

```bash
pip install pre-commit
```

Przykładowy plik `.pre-commit-config.yaml`:

```yaml
repos:
  - repo: https://github.com/psf/black
    rev: 24.4.2
    hooks:
      - id: black

  - repo: https://github.com/PyCQA/flake8
    rev: 7.1.0
    hooks:
      - id: flake8
        args: ["--max-line-length=88"]

  - repo: https://github.com/pycqa/isort
    rev: 5.13.2
    hooks:
      - id: isort
        args: ["--profile=black"]
```

```bash
pre-commit install      # Instalacja hooków
pre-commit run --all-files  # Uruchomienie na wszystkich plikach
```

### Konwencja nazewnictwa w Pythonie (PEP 8)

| Typ               | Konwencja         | Przykład                        |
|-------------------|-------------------|---------------------------------|
| Zmienna           | `snake_case`      | `moja_zmienna`, `liczba_wierszy`|
| Funkcja           | `snake_case`      | `oblicz_vat()`, `wczytaj_dane()`|
| Klasa             | `PascalCase`      | `NazwaKlasy`, `KlientHTTP`      |
| Stała             | `UPPER_SNAKE_CASE`| `MAX_ROZMIAR`, `DOMYSLNY_PORT`  |
| Prywatny atrybut  | `_snake_case`     | `_wartosc`, `_indeks`           |
| "Dunder" metoda   | `__snake_case__`  | `__init__`, `__str__`           |
| Moduł / pakiet    | `snake_case`      | `utils.py`, `moj_pakiet/`       |

### Wskazówki dotyczące importów (`isort`)

`isort` automatycznie sortuje importy zgodnie ze standardem PEP 8:

```bash
pip install isort
isort skrypt.py
```

Prawidłowa kolejność importów:

```python
# 1. Importy standardowej biblioteki
import os
import sys
from pathlib import Path

# 2. Importy zewnętrznych bibliotek
import requests
import numpy as np

# 3. Importy własnych modułów
from moj_pakiet import utils
from moj_pakiet.models import Uzytkownik
```

### Linki

- [PEP 8 - Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)
- [PEP 257 - Docstring Conventions](https://www.python.org/dev/peps/pep-0257/)
- [Black - The uncompromising code formatter](https://github.com/psf/black)
- [Pylint - A Python source code analyzer](https://github.com/PyCQA/pylint)
- [Flake8 - A tool for checking Python code](https://github.com/PyCQA/flake8)
- [autoflake - Removes unused imports and unused variables](https://github.com/myint/autoflake)

### Porównanie narzędzi do jakości kodu

| Narzędzie    | Kategoria        | Automatyczna naprawa? | Konfiguracja         | Szybkość   | Główne zastosowanie                |
|-------------|------------------|----------------------|----------------------|------------|-------------------------------------|
| `black`     | Formatter        | Tak                  | Minimalna (opinionated) | Szybki   | Jednolity styl formatowania         |
| `ruff`      | Linter+Formatter | Tak (częściowo)      | `pyproject.toml`     | Najszybszy | Zamiennik flake8+isort+pyupgrade    |
| `flake8`    | Linter           | Nie                  | `.flake8`, `setup.cfg` | Szybki  | Sprawdzanie stylu i błędów          |
| `pylint`    | Linter           | Nie                  | `.pylintrc`          | Wolny      | Głęboka analiza kodu                |
| `mypy`      | Type checker     | Nie                  | `mypy.ini`           | Średni     | Statyczna analiza typów             |
| `pyright`   | Type checker     | Nie                  | `pyrightconfig.json` | Szybki     | Statyczna analiza typów (VSCode)    |
| `isort`     | Import sorter    | Tak                  | `pyproject.toml`     | Szybki     | Sortowanie importów                 |
| `autoflake` | Cleaner          | Tak                  | Minimalna            | Szybki     | Usuwanie nieużywanych importów      |
| `bandit`    | Security         | Nie                  | `.bandit`            | Szybki     | Wykrywanie problemów bezpieczeństwa |

### Konfiguracja w `pyproject.toml` — współczesny standard

Nowoczesne projekty Python centralizują konfigurację narzędzi w `pyproject.toml`:

```toml
[tool.black]
line-length = 88
target-version = ['py311']

[tool.ruff]
line-length = 88
select = ["E", "F", "W", "I", "N", "UP"]
ignore = ["E501"]

[tool.ruff.isort]
known-first-party = ["moj_pakiet"]

[tool.mypy]
python_version = "3.11"
strict = true
warn_return_any = true

[tool.pytest.ini_options]
testpaths = ["tests"]
addopts = "-v --tb=short"
```

### Pre-commit hooks — automatyczne sprawdzanie przed commitem

```yaml
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/psf/black
    rev: 24.3.0
    hooks:
      - id: black

  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.3.0
    hooks:
      - id: ruff
        args: [--fix]

  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v1.9.0
    hooks:
      - id: mypy
```

Instalacja i użycie:

```bash
pip install pre-commit
pre-commit install          # zainstaluj hooki
pre-commit run --all-files  # uruchom ręcznie na wszystkich plikach
```
