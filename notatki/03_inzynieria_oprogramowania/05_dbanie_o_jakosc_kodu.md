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

### Linki

- [PEP 8 - Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)
- [PEP 257 - Docstring Conventions](https://www.python.org/dev/peps/pep-0257/)
- [Black - The uncompromising code formatter](https://github.com/psf/black)
- [Pylint - A Python source code analyzer](https://github.com/PyCQA/pylint)
- [Flake8 - A tool for checking Python code](https://github.com/PyCQA/flake8)
- [autoflake - Removes unused imports and unused variables](https://github.com/myint/autoflake)
