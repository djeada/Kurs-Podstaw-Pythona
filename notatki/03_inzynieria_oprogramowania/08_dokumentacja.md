## Dokumentacja

Dokumentacja jest istotnym elementem każdego projektu programistycznego. Umożliwia użytkownikom zrozumienie, jak działa aplikacja, jak jest zbudowana, oraz jakie funkcje oferuje. Odpowiednio przygotowana dokumentacja pomaga również innym programistom w szybkim zrozumieniu kodu, ułatwiając jego dalszy rozwój i utrzymanie. W przypadku projektów w języku Python, jednym z najczęściej wybieranych narzędzi do tworzenia profesjonalnej dokumentacji jest **SPHINX**. SPHINX pozwala na generowanie dokumentacji w różnych formatach, takich jak HTML, LaTeX, epub czy zwykły tekst. Dodatkowo, istnieje możliwość łatwej konwersji dokumentacji stworzonej w formacie LaTeX do plików PDF, co czyni to narzędzie bardzo wszechstronnym i elastycznym w użyciu. Dzięki SPHINX można tworzyć czytelne i przejrzyste materiały, które stanowią nieocenione wsparcie dla użytkowników i deweloperów projektu.

### Rozpoczęcie pracy ze Sphinx

Aby utworzyć podstawowy szkielet dokumentacji, należy uruchomić następującą komendę:

```bash
sphinx-quickstart
```

Po uruchomieniu tej komendy, SPHINX poprosi Cię o podanie kilku informacji na temat Twojego projektu. Na podstawie tych odpowiedzi narzędzie wygeneruje niezbędne pliki początkowe i przygotuje je do uzupełnienia treścią.

Aby skompilować i wygenerować dokumentację na podstawie już istniejących plików konfiguracyjnych, użyj:

```bash
make html
```

Po wykonaniu tej komendy, jeśli wszystko przebiegnie poprawnie, SPHINX wyświetli informację o sukcesie. W przeciwnym razie, w przypadku jakichkolwiek problemów, pojawią się komunikaty o błędach, które poinformują cię, co poszło nie tak.

## reStructuredText i jego zastosowanie w Sphinx

**reStructuredText** (rST) to elastyczny i rozbudowany język znaczników przeznaczony do tworzenia dokumentacji i prostych stron internetowych. W porównaniu z popularnym językiem markdown, rST oferuje znacznie bogatszy zestaw funkcji, co czyni go idealnym narzędziem do tworzenia rozbudowanej dokumentacji.

Kilka uwag o reStructuredText:

1. reStructuredText oferuje zaawansowane opcje formatowania, takie jak przypisy dolne, tabele, linki oraz definicje, które są trudniejsze do osiągnięcia w Markdown.
2. Dzięki wsparciu dla różnorodnych wtyczek, reStructuredText można łatwo dostosować do specyficznych wymagań projektu.
3. reStructuredText jest podstawowym formatem wykorzystywanym przez Sphinx – popularne narzędzie do tworzenia dokumentacji. Plik `index.rst` pełni kluczową rolę, ponieważ zawiera główną strukturę oraz linki do pozostałych części dokumentacji.
4. Linkowanie do innych plików i sekcji w reStructuredText jest bardziej intuicyjne i przejrzyste, co ułatwia utrzymanie spójności w dużych dokumentacjach.
5. Korzystając z plików reStructuredText, Sphinx umożliwia generowanie dokumentacji w różnych formatach, w tym w HTML. Aby przekształcić pliki reStructuredText w elegancką stronę internetową, wystarczy użyć komendy `make html`.

### Podstawowe formatowanie w reStructuredText

#### Nagłówki

Nagłówki w reStructuredText są tworzone poprzez dodanie linii znaków bezpośrednio pod tekstem. W zależności od rodzaju użytych znaków, uzyskuje się różne poziomy nagłówków:

- `=` dla nagłówka najwyższego poziomu.
- `-` dla nagłówka niższego poziomu.
- `^` dla jeszcze niższego poziomu, i tak dalej.

Na przykład:

```
Nagłówek 1
==========

Nagłówek 2
----------

Nagłówek 3
^^^^^^^^^^
```

Dzięki temu systemowi, można szybko tworzyć hierarchię sekcji w dokumentacji, co jest bardzo przydatne przy organizowaniu rozdziałów i podrozdziałów.

#### Wyróżnienia tekstu

W reStructuredText możemy wyróżniać tekst na kilka sposobów, takich jak:

- Pochylenie (kursywa) poprzez otoczenie tekstu gwiazdkami `*tekst*`.
- Pogrubienie poprzez podwójne gwiazdki `**tekst**`.
- Fragmenty kodu źródłowego lub komendy wstawiamy w ``poczwórnych akcentach`` (backticks).

Przykład:

```
*Pochylenie* - Tekst będzie wyświetlany kursywą.

**Pogrubienie** - Tekst będzie wyświetlany pogrubiony.

``Poczwórny akcent dla kodu źródłowego`` - Najczęściej używane do wstawiania krótkich fragmentów kodu.
```

#### Listy

Listy są łatwe do tworzenia i mogą być numerowane lub nienumerowane. W przypadku nienumerowanych list, używamy myślników (`-`). Możemy też tworzyć zagnieżdżone listy poprzez odpowiednie wcięcia.

Przykład:

```
- Element 1
- Element 2
    - Pod-element 2.1
    - Pod-element 2.2
- Element 3
```

W powyższym przykładzie `Pod-element 2.1` i `Pod-element 2.2` są elementami podrzędnymi `Elementu 2`, co jest reprezentowane przez wcięcie. Tego rodzaju struktura jest przydatna do organizacji punktów w dokumentacji.

#### Linki

Tworzenie linków w reStructuredText jest bardzo proste i może być wykonane za pomocą backticków z dodaniem adresu URL w nawiasach ostrych:

```
`Link tekstowy <http://example.com>`_
```

Linki te są intuicyjne i czytelne, dzięki czemu łatwo dodaje się odnośniki do dokumentacji.

#### Obrazy

Aby dodać obraz do dokumentacji, używamy dyrektywy `.. image::`, po której następuje ścieżka do pliku obrazu. Dodatkowo możemy dodać tekst alternatywny (`alt`), który będzie wyświetlany, gdy obraz nie może być załadowany.

Przykład:

```
.. image:: ścieżka/do/obrazu.jpg
   :alt: Tekst alternatywny
```

Tekst alternatywny jest przydatny zarówno dla dostępności (czytniki ekranowe), jak i dla SEO, gdy dokumentacja jest publikowana w sieci.

#### Tabele

reStructuredText obsługuje również tabele, które mogą być tworzone za pomocą znaków `+` i `|`. Każda komórka jest oddzielona pionową kreską `|`, a `+` służy do definiowania krawędzi tabeli.

Przykład:

```
+---------------+-------------+-------------+
| Nagłówek 1    | Nagłówek 2  | Nagłówek 3  |
+---------------+-------------+-------------+
| komórka 1.1   | komórka 1.2 | komórka 1.3 |
| komórka 2.1   | komórka 2.2 | komórka 2.3 |
+---------------+-------------+-------------+
```

Tabele w reStructuredText są statyczne, co oznacza, że musimy ręcznie zarządzać szerokością kolumn. Niemniej jednak, ich czytelność sprawia, że są często używane do prezentowania uporządkowanych danych w dokumentacji.

#### Przypisy

Przypisy są przydatne do dodawania dodatkowych informacji lub źródeł, które mogą nie być bezpośrednio potrzebne w tekście, ale są ważne do zrozumienia danego zagadnienia.

Przykład przypisu:

```
Przykład tekstu z przypisem.[1]

.. [1] Tekst przypisu dolnego.
```

Przypisy te są automatycznie numerowane i można do nich odnosić się w całym dokumencie, co ułatwia utrzymanie spójności i przejrzystości.

#### Dyrektywy

Dyrektywy w reStructuredText to specjalne komendy, które pozwalają na wstawianie bardziej zaawansowanych elementów, takich jak ostrzeżenia, notatki, czy bloków kodu. Są one bardzo przydatne przy tworzeniu rozbudowanej dokumentacji, gdzie niektóre sekcje wymagają wyróżnienia.

Na przykład, aby wstawić notatkę lub ostrzeżenie, możemy użyć:

```
.. note:: To jest notatka.
```

```
.. warning:: To jest ostrzeżenie.
```

Dzięki dyrektywom można łatwo dodawać wizualnie wyróżnione sekcje, które zwracają uwagę czytelnika na ważne informacje.

Dla fragmentów kodu, stosuje się dyrektywę `.. code-block::` z określeniem języka, co zapewnia odpowiednie formatowanie składni:

```
.. code-block:: python

    def funkcja():
        print("Przykład kodu")
```

W powyższym przykładzie kod jest automatycznie wyróżniany zgodnie ze składnią Pythona, co znacznie poprawia jego czytelność i pomaga użytkownikom zrozumieć, co dana funkcja robi.

### Automatyczne generowanie dokumentacji dla API

W erze dynamicznego rozwoju oprogramowania, aplikacje coraz częściej opierają się na interfejsach API, które umożliwiają komunikację i integrację między różnymi usługami, systemami oraz platformami. Dla deweloperów i użytkowników korzystających z tych API, kluczowe jest posiadanie **przejrzystej**, **dokładnej** i **aktualnej** dokumentacji.

Ręczne tworzenie i aktualizowanie dokumentacji może być czasochłonne i podatne na błędy, zwłaszcza w dużych projektach z częstymi zmianami w kodzie. Automatyczne generowanie dokumentacji rozwiązuje te problemy, zapewniając spójność między kodem źródłowym a dokumentacją oraz oszczędzając cenny czas deweloperów.

Jednym z najpopularniejszych narzędzi do automatycznego generowania dokumentacji w Pythonie jest **Sphinx**. Umożliwia on tworzenie profesjonalnej dokumentacji w różnych formatach, takich jak HTML, PDF czy ePub. Dodatkowo, w przypadku dokumentowania API, narzędzie **sphinx-apidoc** jest niezwykle pomocne, gdyż automatycznie generuje pliki dokumentacji na podstawie kodu źródłowego i docstringów.

Poniżej przedstawiamy szczegółowy przewodnik, który pomoże Ci w automatycznym generowaniu dokumentacji dla Twojego API przy użyciu Sphinx i sphinx-apidoc.

#### I. Przygotowanie struktury projektu

Na początek, upewnij się, że Twój projekt ma odpowiednią strukturę. Przykładowa struktura projektu może wyglądać następująco:

```
my_project/
├── my_module/
│   ├── __init__.py
│   ├── module1.py
│   └── module2.py
└── setup.py
```

Wyjaśnienie struktury:

- `my_project/` – główny katalog projektu.
- `my_module/` – katalog z kodem źródłowym modułu lub pakietu, który chcesz udokumentować.
  - `__init__.py` – plik wskazujący, że `my_module` jest pakietem Pythona.
  - `module1.py`, `module2.py` – pliki z funkcjami, klasami i metodami Twojego API.
- `setup.py` – skrypt instalacyjny projektu, przydatny przy dystrybucji pakietu.

#### II. Przykładowa zawartość `module1.py`

Aby Sphinx mógł poprawnie wygenerować dokumentację, ważne jest stosowanie docstringów w kodzie źródłowym. Oto przykładowa zawartość pliku `module1.py`:

```python
# my_module/module1.py

def add(a, b):
    """
    Dodaje dwie liczby.

    :param a: Pierwsza liczba.
    :type a: int lub float
    :param b: Druga liczba.
    :type b: int lub float
    :return: Suma dwóch liczb.
    :rtype: int lub float
    """
    return a + b


class Calculator:
    """
    Klasa reprezentująca prosty kalkulator.
    """

    def multiply(self, a, b):
        """
        Mnoży dwie liczby.

        :param a: Pierwsza liczba.
        :type a: int lub float
        :param b: Druga liczba.
        :type b: int lub float
        :return: Iloczyn dwóch liczb.
        :rtype: int lub float
        """
        return a * b
```

Wyjaśnienie docstringów:

- Docstringi są umieszczone bezpośrednio pod definicją funkcji lub klasy.
- Używają składni reStructuredText (reST), którą Sphinx potrafi interpretować.
- `:param a:` – opisuje parametr `a`.
- `:type a:` – określa typ parametru `a`.
- `:return:` – opisuje wartość zwracaną przez funkcję.
- `:rtype:` – określa typ zwracanej wartości.

#### III. Generowanie dokumentacji dla API

**Utworzenie katalogu `docs`**

W głównym katalogu projektu (`my_project/`) utwórz katalog `docs`, w którym będzie przechowywana dokumentacja:

```bash
mkdir docs
```

**Inicjalizacja Sphinx**

Przejdź do katalogu `docs` i uruchom narzędzie `sphinx-quickstart`:

```bash
cd docs
sphinx-quickstart
```

Podczas procesu zostaniesz poproszony o:

- Nazwę projektu.
- Nazwę autora.
- Wersję projektu.
- Wybór rozszerzeń Sphinx.

Możesz zaakceptować domyślne ustawienia lub dostosować je do swoich potrzeb.

**Generowanie plików `.rst` dla modułów**

Użyj `sphinx-apidoc`, aby automatycznie wygenerować pliki dokumentacji dla Twoich modułów:

```bash
sphinx-apidoc -o source/api ../my_module
```

Wyjaśnienie polecenia:

- `-o source/api` – określa katalog wyjściowy dla wygenerowanych plików `.rst`.
- `../my_module` – wskazuje katalog z kodem źródłowym, który ma zostać udokumentowany.

**Struktura katalogów po wygenerowaniu dokumentacji**

Po wykonaniu powyższych kroków struktura katalogów powinna wyglądać następująco:

```
my_project/
├── docs/
│   ├── Makefile
│   ├── build/
│   └── source/
│       ├── api/
│       │   ├── modules.rst
│       │   ├── my_module.module1.rst
│       │   ├── my_module.module2.rst
│       │   └── my_module.rst
│       ├── conf.py
│       ├── index.rst
│       ├── _static/
│       └── _templates/
├── my_module/
│   ├── __init__.py
│   ├── module1.py
│   └── module2.py
└── setup.py
```

Opis struktury:

- `docs/` – katalog z dokumentacją.
- `Makefile` – plik umożliwiający budowanie dokumentacji na systemach Unix.
- `build/` – katalog, w którym będą znajdować się wygenerowane pliki (np. HTML).
- `source/` – źródła dokumentacji.
 - `api/` – wygenerowane pliki `.rst` dla modułów.
 - `conf.py` – plik konfiguracyjny Sphinx.
 - `index.rst` – główny plik dokumentacji.
 - `_static/`, `_templates/` – katalogi na dodatkowe zasoby.

**Konfiguracja `conf.py`**

Otwórz plik `conf.py` znajdujący się w `docs/source/` i dodaj ścieżkę do katalogu z Twoim modułem:

```python
# docs/source/conf.py

import os
import sys
sys.path.insert(0, os.path.abspath('../../my_module'))
```

**Dlaczego to jest ważne?**

- Dodanie ścieżki do `sys.path` pozwala Sphinxowi na importowanie modułów i generowanie dokumentacji na podstawie docstringów.
- `os.path.abspath('../../my_module')` tworzy bezwzględną ścieżkę do katalogu `my_module`.

**Dodanie wygenerowanych plików do `index.rst`**

Aby wygenerowana dokumentacja była dostępna w głównym spisie treści, edytuj plik `index.rst` i dodaj:

```rst
.. toctree::
   :maxdepth: 2
   :caption: Spis treści:

   api/modules
```

Wyjaśnienie:

- `.. toctree::` – dyrektywa tworząca spis treści.
- `:maxdepth: 2` – określa głębokość spisu treści.
- `api/modules` – odnosi się do wygenerowanego pliku `modules.rst` w katalogu `api/`.

#### IV. Generowanie dokumentacji w formacie HTML

Aby wygenerować dokumentację w formacie HTML, wykonaj w katalogu `docs/` polecenie:

```bash
make html
```

Informacje dodatkowe:

- Pliki HTML zostaną wygenerowane w katalogu `docs/build/html/`.
- Otwórz `docs/build/html/index.html` w przeglądarce, aby zobaczyć wynik.

#### V. Automatyzacja aktualizacji dokumentacji

Aby dokumentacja zawsze była aktualna, warto zautomatyzować proces jej generowania.

**Integracja z narzędziami CI/CD**

Możesz użyć narzędzi takich jak **GitHub Actions**, **GitLab CI/CD**, **Travis CI** czy **Jenkins**, aby automatycznie generować i publikować dokumentację przy każdym pushu do repozytorium.

Przykład konfiguracji GitHub Actions:

```yaml
# .github/workflows/docs.yml

name: Build and Deploy Docs

on:
  push:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v3
        with:
          python-version: '3.x'
      - name: Install dependencies
        run: |
          pip install sphinx
      - name: Build Docs
        run: |
          cd docs
          make html
      - name: Deploy Docs
        uses: peaceiris/actions-gh-pages@v3
        with:
          personal_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: docs/build/html
```

**Użycie pre-commit hooks**

Możesz skonfigurować **pre-commit hook**, który będzie generował dokumentację przed każdym commitem.

**Konfiguracja pre-commit:**

Zainstaluj narzędzie `pre-commit`:

```bash
pip install pre-commit
```

Utwórz plik `.pre-commit-config.yaml` w głównym katalogu projektu:

```yaml
repos:
- repo: local
  hooks:
  - id: generate-docs
    name: Generate Sphinx Documentation
    entry: bash -c 'cd docs && make html'
    language: system
    stages: [commit]
```

Zainstaluj pre-commit hooks:

```bash
pre-commit install
```

**Harmonogram zadań (cron)**

Jeśli Twoja dokumentacja jest hostowana na serwerze, możesz ustawić zadanie cron, które będzie regularnie aktualizować dokumentację.

#### VI. Dostosowanie wyglądu i funkcjonalności dokumentacji

Sphinx oferuje wiele możliwości personalizacji.

**Wybór motywu**

Zmiana motywu może znacząco poprawić wygląd dokumentacji.

Popularne motywy:

- `alabaster` (domyślny)
- `sphinx_rtd_theme` (motyw używany przez Read the Docs)
- `classic`
- `nature`

**Zmiana motywu na `sphinx_rtd_theme`:**

Zainstaluj motyw:

```bash
pip install sphinx_rtd_theme
```

Edytuj `conf.py`:

```python
html_theme = 'sphinx_rtd_theme'
```

**Dodawanie własnych stylów CSS**

Możesz dodać własne style, tworząc plik CSS i modyfikując `conf.py`.

Kroki:

1. Utwórz katalog `docs/source/_static/` jeśli jeszcze nie istnieje.
2. Dodaj plik CSS, np. `custom.css`, do katalogu `_static/`.
3. Edytuj `conf.py`:

```python
html_static_path = ['_static']
html_css_files = [
    'custom.css',
]
```

**Użycie rozszerzeń Sphinx**

Rozszerzenia dodają dodatkowe funkcje do Sphinx.

Przykładowe rozszerzenia:

- `sphinx.ext.autodoc` – automatycznie generuje dokumentację z docstringów.
- `sphinx.ext.napoleon` – obsługuje styl docstringów Google i NumPy.
- `sphinx.ext.viewcode` – dodaje linki do źródła kodu.

**Dodanie rozszerzeń do `conf.py`:**

```python
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
]
```

### Linki

* [Style Guide for Developers](https://developers.google.com/style)
* [Sphinx Official Documentation](https://www.sphinx-doc.org/en/master/)
* [reStructuredText Documentation](https://docutils.sourceforge.io/rst.html)
* [Read the Docs Documentation](https://docs.readthedocs.io/en/stable/)
* [Sphinx Themes](https://sphinx-themes.org/)
* [Sphinx GitHub Repository](https://github.com/sphinx-doc/sphinx)
* [Sphinx Extensions](https://www.sphinx-doc.org/en/master/usage/extensions/index.html)
* [Markdown Guide](https://www.markdownguide.org/)
* [Python Documentation](https://docs.python.org/3/)
* [NumPy Documentation](https://numpy.org/doc/)
* [Pandas Documentation](https://pandas.pydata.org/pandas-docs/stable/)
* [Jinja2 Documentation](https://jinja.palletsprojects.com/en/3.0.x/)
* [ReadTheDocs Tutorial](https://docs.readthedocs.io/en/stable/intro/getting-started-with-sphinx.html)
* [Sphinx AutoAPI Extension](https://sphinx-autoapi.readthedocs.io/en/latest/)
* [Sphinx Napoleon Extension](https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html)
* [Continuous Integration with Sphinx](https://docs.readthedocs.io/en/stable/ci/index.html)
* [Sphinx HTML Themes Gallery](https://sphinx-themes.org/)
* [GitHub Actions for Sphinx](https://github.com/marketplace/actions/sphinx-build)
* [Travis CI for Sphinx](https://travis-ci.org/)

