## Dokumentacja

Dokumentacja stanowi kluczowy komponent każdego projektu programistycznego, umożliwiając użytkownikom zrozumienie funkcjonalności, struktury oraz sposobu działania aplikacji. W Pythonie jednym z popularnych narzędzi służących do tworzenia profesjonalnej dokumentacji jest **SPHINX**. Pozwala on na generowanie dokumentacji w różnorodnych formatach, w tym HTML, LaTeX, epub czy plain text. Istnieje również możliwość konwersji dokumentacji z formatu LaTeX do PDF.

### Rozpoczęcie z Sphinx

Aby zainicjować szkielet dokumentacji, potrzebujesz uruchomić następującą komendę:

```bash
sphinx-quickstart
```

Po uruchomieniu tej komendy, SPHINX poprosi cię o podanie kilku szczegółów dotyczących twojego projektu. Na podstawie udzielonych odpowiedzi, narzędzie to wygeneruje odpowiednie pliki startowe i przygotuje je do uzupełnienia konkretną treścią.

Aby skompilować i wygenerować dokumentację opartą o istniejące pliki konfiguracyjne, wykorzystaj:

```bash
make html
```

Po pomyślnym wykonaniu tej komendy, jeśli wszystko przebiegnie bez błędów, SPHINX poinformuje cię o sukcesie. W przypadku wystąpienia problemów, zostaniesz poinformowany za pomocą komunikatów błędów.

## reStructuredText i jego zastosowanie w Sphinx

**reStructuredText** (rST) to elastyczny i rozbudowany język znaczników przeznaczony do tworzenia dokumentacji i prostych stron internetowych. W porównaniu z popularnym językiem markdown, rST oferuje znacznie bogatszy zestaw funkcji, co czyni go idealnym narzędziem do tworzenia rozbudowanej dokumentacji.

### Kluczowe cechy reStructuredText

1. reStructuredText oferuje zaawansowane formatowanie, takie jak przypisy dolne, tabele, linki oraz definicje, które nie są tak łatwo dostępne w markdown.
   
2. Dzięki wsparciu dla różnych pluginów, reStructuredText można łatwo dostosować do konkretnych potrzeb projektu.

3. reStructuredText jest głównym formatem używanym przez Sphinx, popularne narzędzie do generowania dokumentacji. Plik `index.rst` jest centralnym punktem dokumentacji w Sphinx, zawierającym główną strukturę oraz linki do innych części dokumentacji.

4. Linkowanie do innych plików czy sekcji w reStructuredText jest bardziej intuicyjne i przejrzyste, co ułatwia utrzymanie spójności w rozbudowanych dokumentacjach.

5. Sphinx, korzystając z plików reStructuredText, umożliwia generowanie dokumentacji w różnych formatach, w tym w HTML. Wystarczy użyć komendy `make html`, aby przekształcić pliki reStructuredText w elegancką stronę internetową.

### Podstawowe formatowanie w reStructuredText

#### Nagłówki

Nagłówki są tworzone poprzez dodanie linii znaków pod tekstem.

```
Nagłówek 1
==========

Nagłówek 2
----------

Nagłówek 3
^^^^^^^^^^
```

#### Wyróżnienia tekstu

```
*Pochylenie*

**Pogrubienie**

``Poczwórny akcent dla kodu źródłowego``
```

#### Listy

```
- Element 1
- Element 2
    - Pod-element 2.1
    - Pod-element 2.2
- Element 3
```

#### Linki

```
`Link tekstowy <http://example.com>`_
```

#### Obrazy

```
.. image:: ścieżka/do/obrazu.jpg
   :alt: Tekst alternatywny
```

#### Tabele

```
+---------------+-------------+-------------+
| Nagłówek 1    | Nagłówek 2  | Nagłówek 3  |
+---------------+-------------+-------------+
| komórka 1.1   | komórka 1.2 | komórka 1.3 |
| komórka 2.1   | komórka 2.2 | komórka 2.3 |
+---------------+-------------+-------------+
```

#### Przypisy

```
Przykład tekstu z przypisem.[1]

.. [1] Tekst przypisu dolnego.
```

#### Dyrektywy

Dyrektywy służą do wstawiania różnych elementów, takich jak obrazy, tabele czy fragmenty kodu.

```
.. note:: To jest notatka.
```

```
.. warning:: To jest ostrzeżenie.
```

```
.. code-block:: python

    def funkcja():
        print("Przykład kodu")
```

### Automatyczne generowanie dokumentacji dla API

Współczesne aplikacje często korzystają z interfejsów API, które pozwalają na komunikację między różnymi usługami. Aby ułatwić korzystanie z takiego API, kluczowe jest dostarczenie dokładnej, ale i czytelnej dokumentacji. Automatyczne generowanie dokumentacji może znacząco przyspieszyć ten proces, jednocześnie zapewniając, że jest ona zawsze aktualna. Proces ten pozwala nam zaoszczędzić czas oraz minimalizuje ryzyko błędów i nieścisłości wynikających z ręcznego pisania dokumentacji.

W Pythonie możemy wykorzystać narzędzie **Sphinx** do generowania dokumentacji, a w kontekście API, jego rozszerzenie **sphinx-apidoc** jest szczególnie przydatne.

#### Krok po kroku

Początkowa struktura projektu może wyglądać następująco:

```
my_project/
├── my_module/
│   ├── __init__.py
│   ├── module1.py
│   └── module2.py
└── setup.py
```

**I. Instalacja sphinx-apidoc**:

- Przed przystąpieniem do generowania dokumentacji, należy upewnić się, że mamy zainstalowane narzędzie Sphinx. Można to zrobić za pomocą menedżera pakietów pip:

```bash
pip install sphinx
```

Sphinx to narzędzie, które pozwala na łatwe tworzenie dokumentacji w formacie reStructuredText (rst) lub Markdown, a następnie konwertowanie jej na różne formaty wyjściowe, takie jak HTML, PDF, czy ePub. Sphinx jest szeroko stosowany w społeczności Pythona i jest wspierany przez wiele narzędzi CI/CD.

- Sphinx-apidoc to rozszerzenie Sphinxa, które automatycznie generuje dokumentację dla API na podstawie docstringów w kodzie. Instalacja jest prosta i również odbywa się za pomocą pip:

```bash
pip install sphinx-apidoc
```

Ten pakiet rozszerza funkcjonalność Sphinxa, umożliwiając automatyczne skanowanie kodu źródłowego i generowanie odpowiednich plików dokumentacji. Dzięki sphinx-apidoc, każdy moduł i pakiet w projekcie zostanie opisany na podstawie docstringów, co pozwala na zachowanie spójności między kodem a dokumentacją.

**II. Generowanie dokumentacji dla API**

- Przed przystąpieniem do generowania dokumentacji, upewnij się, że masz katalog, w którym będą przechowywane pliki dokumentacji. Najczęściej jest to katalog `docs` w głównym katalogu projektu. Możesz go utworzyć poleceniem:

```bash
mkdir docs
```

- Aby wygenerować pliki reStructuredText, które będą podstawą dokumentacji, użyj polecenia `sphinx-apidoc`. Przejdź do katalogu dokumentacji i wykonaj następujące polecenie:

```bash
sphinx-apidoc -o docs/source/api/ <ścieżka do katalogu z kodem>
```

W powyższym poleceniu `<ścieżka do katalogu z kodem>` zastąp ścieżką do katalogu zawierającego twój kod źródłowy. Polecenie to skanuje wskazany katalog i generuje pliki `.rst` dla wszystkich modułów i pakietów w projekcie. Dla naszego przykładu to będzie:

```bash
sphinx-apidoc -o docs/source/api/ ../my_module/
```

Po tym kroku struktura katalogów będzie wyglądać następująco:

```
my_project/
├── docs/
│   ├── Makefile
│   ├── build/
│   └── source/
│       ├── api/
│       │   ├── my_module.module1.rst
│       │   ├── my_module.module2.rst
│       │   └── my_module.rst
│       ├── conf.py
│       ├── index.rst
│       └── _static/
│       └── _templates/
├── my_module/
│   ├── __init__.py
│   ├── module1.py
│   └── module2.py
└── setup.py
```

**III. Konfiguracja Sphinx i dodanie wygenerowanej dokumentacji do głównej zawartości**

Aby wygenerowane pliki `.rst` były widoczne w głównej dokumentacji, musisz je dodać do pliku `index.rst`, który jest głównym plikiem startowym dokumentacji Sphinx. Otwórz plik `index.rst` i dodaj do niego wpis dla wygenerowanej dokumentacji API:

```rst
.. toctree::
   :maxdepth: 2
   :caption: Spis treści:

   api/index
```

W powyższym przykładzie `api/index` odnosi się do głównego pliku indeksu wygenerowanego przez sphinx-apidoc. Upewnij się, że ścieżka jest zgodna z rzeczywistą lokalizacją pliku.

**IV. Generowanie strony internetowej z dokumentacją**:

Po dodaniu wygenerowanych plików do głównego indeksu, możemy przystąpić do generowania końcowego formatu dokumentacji. Najczęściej używanym formatem jest HTML, który umożliwia przeglądanie dokumentacji w przeglądarce internetowej. Aby wygenerować dokumentację w formacie HTML, wykonaj następujące polecenie w katalogu głównym dokumentacji:

```bash
make html
```

Po zakończeniu procesu, wygenerowane pliki HTML będą dostępne w katalogu `_build/html`. Możesz je otworzyć w przeglądarce internetowej, aby przejrzeć dokumentację.

Po tym kroku struktura katalogów będzie wyglądać następująco:

```
my_project/
├── docs/
│   ├── Makefile
│   ├── build/
│   │   └── html/
│   │       ├── index.html
│   │       ├── genindex.html
│   │       ├── ...
│   └── source/
│       ├── api/
│       │   ├── my_module.module1.rst
│       │   ├── my_module.module2.rst
│       │   └── my_module.rst
│       ├── conf.py
│       ├── index.rst
│       └── _static/
│       └── _templates/
├── my_module/
│   ├── __init__.py
│   ├── module1.py
│   └── module2.py
└── setup.py
```

**V. Automatyzacja aktualizacji dokumentacji**

Automatyzacja procesu aktualizacji dokumentacji jest kluczowa, aby zawsze odzwierciedlała bieżący stan kodu. Można to osiągnąć na kilka sposobów:

- Konfiguracja narzędzi **CI**, takich jak Travis CI, GitHub Actions, czy Jenkins, pozwala na automatyczne generowanie dokumentacji przy każdym wdrożeniu kodu na główną gałąź repozytorium. Dzięki temu dokumentacja jest zawsze aktualna i odzwierciedla ostatnie zmiany w kodzie.

- Użyj **pre-commit hooks**, aby generować dokumentację przed każdym zatwierdzeniem (commit). Dzięki temu każdy commit zawiera aktualną wersję dokumentacji. Można to skonfigurować za pomocą narzędzia `pre-commit`:

```yaml
# .pre-commit-config.yaml
repos:
- repo: local
  hooks:
  - id: generate-docs
    name: Generate Sphinx Documentation
    entry: sphinx-apidoc -o docs/source/api/ ../my_module/ && make -C docs html
    language: system
    stages: [commit]
```

- Można ustawić cron job lub inny systemowy harmonogram zadań, aby regularnie uruchamiał skrypt generujący dokumentację, np. co noc. To zapewni, że dokumentacja będzie aktualizowana na bieżąco bez ręcznej interwencji.

**VI. Dostosowanie wyglądu dokumentacji**

Sphinx umożliwia szerokie możliwości dostosowywania wyglądu i funkcjonalności dokumentacji. Możesz zmienić motyw, dodawać własne style CSS, a także modyfikować szablony HTML. Wszystkie te ustawienia znajdują się w pliku `conf.py`, który jest głównym plikiem konfiguracyjnym Sphinx:

- Możesz zmienić motyw dokumentacji, modyfikując linię `html_theme` w pliku `conf.py`. Na przykład, aby użyć motywu 'alabaster', zmień tę linię na:

```python
html_theme = 'alabaster'
```

- Możesz dodać własne style CSS, tworząc plik CSS i dodając go do `conf.py`:

```python
html_static_path = ['_static']
html_css_files = [
    'custom.css',
]
```

Sphinx pozwala na pełną personalizację szablonów HTML. Możesz tworzyć własne szablony lub modyfikować istniejące, dodając pliki HTML do katalogu `_templates`.

**VII. Konsystencja i dokładność**

Automatyczne narzędzia generowania dokumentacji, takie jak sphinx-apidoc, zapewniają, że dokumentacja jest spójna i dokładna. Dzięki automatycznemu skanowaniu kodu, narzędzia te są w stanie wygenerować dokumentację, która odzwierciedla rzeczywisty stan kodu, minimalizując ryzyko błędów i niezgodności.

**VIII. Oszczędzanie czasu**

Ręczne pisanie i aktualizowanie dokumentacji może być bardzo czasochłonne. Automatyzacja tego procesu pozwala zaoszczędzić czas programistów, który mogą przeznaczyć na rozwijanie funkcjonalności aplikacji, zamiast martwić się o ręczne aktualizowanie dokumentacji.

**IX. Lepsza współpraca zespołowa**

Dzięki automatycznemu generowaniu dokumentacji, wszyscy członkowie zespołu mają dostęp do najnowszych informacji o API. To ułatwia współpracę, ponieważ wszyscy członkowie zespołu mogą korzystać z aktualnej dokumentacji, co minimalizuje ryzyko nieporozumień i błędów.

**X. Łatwość użycia**

Narzędzia takie jak Sphinx i sphinx-apidoc są stosunkowo łatwe do skonfigurowania i użycia. Nawet mniej doświadczeni programiści mogą szybko nauczyć się korzystać z tych narzędzi, co czyni je dostępnymi dla szerokiego grona użytkowników.

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

