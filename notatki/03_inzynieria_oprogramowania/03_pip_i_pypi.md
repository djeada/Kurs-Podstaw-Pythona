## PIP i PyPI

`PIP` (Python Package Installer) to menedżer pakietów dla języka Python, który ułatwia zarządzanie pakietami z repozytorium `PyPI` (Python Package Index). PIP pozwala na łatwą instalację, aktualizację i usuwanie pakietów, co jest nieocenione przy rozbudowie projektów i zarządzaniu zależnościami.

### Czym są menadżery pakietów?

Menadżery pakietów to narzędzia, które odgrywają kluczową rolę w zarządzaniu oprogramowaniem, ułatwiając procesy instalacji, aktualizacji, konfiguracji i usuwania pakietów oprogramowania w systemie komputerowym. Są one niezwykle przydatne w różnych środowiskach – od systemów operacyjnych po specyficzne platformy programistyczne, takie jak Python, Ruby czy JavaScript. Oto kilka głównych celów i korzyści z używania menadżerów pakietów:

- Menadżery pakietów automatycznie zarządzają zależnościami między pakietami, co oznacza, że potrafią zidentyfikować i zainstalować wszystkie inne pakiety (zależności), które są niezbędne do prawidłowego działania instalowanego oprogramowania. Dzięki temu użytkownicy nie muszą ręcznie śledzić i instalować każdej zależności.
- Menadżery pakietów umożliwiają łatwą instalację oprogramowania za pomocą pojedynczego polecenia. Usuwają potrzebę ręcznego pobierania i konfigurowania oprogramowania, co jest szczególnie przydatne w przypadku skomplikowanych systemów z wieloma komponentami.
- *Zapewniają łatwe aktualizacje dla oprogramowania, pozwalając na szybkie i skuteczne wdrażanie poprawek bezpieczeństwa i ulepszeń funkcjonalnych. Menadżery pakietów często oferują także narzędzia do przeglądania historii instalacji i wycofywania zmian, jeśli aktualizacje nie działają prawidłowo.
- Umożliwiają instalację i utrzymanie wielu wersji tego samego oprogramowania, co jest istotne w środowiskach deweloperskich, gdzie różne projekty mogą wymagać różnych wersji tej samej biblioteki lub narzędzia.
- Automatyzacja wielu rutynowych zadań związanych z zarządzaniem oprogramowaniem oszczędza czas, minimalizuje ryzyko błędów ludzkich i pozwala zespołom programistycznym skoncentrować się na bardziej strategicznych aspektach projektów.
- Menadżery pakietów przyczyniają się do spójności w instalacji i konfiguracji oprogramowania poprzez zapewnienie standardowych procedur dla tych procesów. Pomaga to w utrzymaniu porządku w systemach, które są szeroko rozpowszechnione w przedsiębiorstwach i dużych organizacjach.

### Instalacja PIP

W nowszych wersjach Pythona, PIP jest instalowany automatycznie razem z interpreterem. Jeśli jednak z jakiegoś powodu nie masz zainstalowanego PIP, istnieje kilka metod jego instalacji:

I. Najprostsze rozwiązanie to ponowna instalacja Pythona, co zapewni, że PIP będzie dołączony do instalacji.

II. Jeśli preferujesz manualną instalację PIP, możesz pobrać skrypt instalacyjny `get-pip.py` z oficjalnej strony.

```bash
python get-pip.py
```

III. Po instalacji warto sprawdzić, czy PIP działa poprawnie:

```bash
pip help
```

### Podstawowe operacje z PIP

PIP oferuje szeroki wachlarz funkcji, które ułatwiają zarządzanie pakietami Pythona:

- Instalacja pakietu:

```bash
pip install nazwa_pakietu
```

- Wyświetlanie szczegółów zainstalowanego pakietu:

```bash
pip show nazwa_pakietu
```

- Lista zainstalowanych pakietów:

```bash
pip list
```

- Zapisywanie zainstalowanych pakietów do pliku:

Możesz zapisać listę zainstalowanych pakietów wraz z ich wersjami do pliku `requirements.txt`, co jest pomocne przy replikacji środowiska projektu:

```bash
pip freeze > requirements.txt
```

- Instalacja pakietów z pliku `requirements.txt`:

```bash
pip install -r requirements.txt
```

- Odinstalowywanie pakietu:

```bash
pip uninstall nazwa_pakietu
```

- Wyszukiwanie pakietów:

PIP umożliwia także wyszukiwanie pakietów dostępnych w PyPI:

```bash
pip search nazwa_pakietu
```

### Aktualizacja pakietów

Aktualizacja pakietów jest kluczowym elementem utrzymania bezpieczeństwa i efektywności aplikacji. Dzięki menedżerom pakietów, jak `pip` w Pythonie, proces ten jest znacznie uproszczony.

- Możesz zaktualizować konkretny pakiet do najnowszej dostępnej wersji, używając poniższego polecenia:

```bash
pip install --upgrade nazwa_pakietu
```

- Aby uzyskać listę przestarzałych pakietów, użyj:

```bash
pip list --outdated
```

Następnie możesz zaktualizować każdy z nich przy użyciu `pip install --upgrade`. Jeśli chcesz zaktualizować wszystkie przestarzałe pakiety jednocześnie, możesz użyć pętli w Bashu:

```bash
pip list --outdated | grep -v 'Package' | awk '{print $1}' | xargs -n1 pip install --upgrade
```

- Regularna aktualizacja samego narzędzia `pip` jest ważna, by mieć dostęp do najnowszych funkcji i poprawek bezpieczeństwa:

```bash
pip install --upgrade pip
```

### Czym jest `setup.py`?

`setup.py` jest tradycyjnym plikiem konfiguracyjnym w projektach Python, który służy do definiowania metadanych projektu oraz zarządzania zależnościami i dystrybucją pakietu. Jest to część standardowego narzędzia `setuptools`, które pomaga w pakowaniu i dystrybucji bibliotek Pythona.

#### Zawartość pliku `setup.py`

Plik `setup.py` jest kluczowym elementem w pakowaniu i dystrybucji bibliotek Pythona. Plik ten powinien zawierać metadane dotyczące pakietu, informacje o zależnościach oraz konfigurację niezbędną do poprawnego zainstalowania pakietu. Oto główne elementy, które powinien zawierać plik `setup.py`:

- **name:** Nazwa pakietu.
- **version:** Wersja pakietu.
- **description:** Krótki opis pakietu.
- **long_description:** Dłuższy opis pakietu, często w formacie Markdown lub reStructuredText.
- **author:** Autor pakietu.
- **author_email:** Adres email autora.
- **url:** Adres URL projektu (np. repozytorium GitHub).
- **packages:** Lista pakietów do załączenia w dystrybucji.
- **install_requires:** Lista zależności wymaganych do działania pakietu.
- **license:** Licencja, na której udostępniany jest pakiet.

#### Teoretyczna struktura repozytorium

Przykładowa struktura repozytorium dla projektu Pythonowego może wyglądać następująco:

```
nazwa_projektu/
│
├── nazwa_projektu/
│ ├── init.py
│ ├── modul1.py
│ └── modul2.py
│
├── tests/
│ ├── init.py
│ ├── test_modul1.py
│ └── test_modul2.py
│
├── README.md
├── LICENSE
└── setup.py
```

- Katalog główny `nazwa_projektu/` zawiera wszystkie pliki źródłowe i zasoby.
- Podkatalog `nazwa_projektu/` zawiera moduły źródłowe pakietu.
- Katalog `tests/` zawiera testy jednostkowe dla modułów.
- Plik `README.md` zawiera opis projektu.
- Plik `LICENSE` definiuje licencję, na której udostępniane są źródła.
- Plik `setup.py` zawiera konfigurację niezbędną do zbudowania i zainstalowania pakietu.

#### Przykładowy plik `setup.py`

Dla przykładowej struktury repozytorium plik `setup.py` mógłby wyglądać tak:

```python
from setuptools import setup, find_packages

setup(
    name='nazwa_projektu',
    version='0.1.0',
    description='Krótki opis mojego projektu',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Imię Nazwisko',
    author_email='email@example.com',
    url='https://github.com/uzytkownik/nazwa_projektu',
    packages=find_packages(),
    install_requires=[
        'biblioteka1>=1.0',
        'biblioteka2>=2.0',
    ],
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='przykladowe slowa kluczowe',
)
```

Ten plik `setup.py` zawiera podstawowe informacje o pakiecie, w tym zależności, metadane oraz dodatkowe klasyfikatory, które pomagają w kategoryzacji pakietu na `PyPI`.

#### Relacja między `setup.py`, `pip` i `PyPI`

- **`setup.py`:** Ten plik jest używany do przygotowania pakietu, który może być później zainstalowany za pomocą `pip`. Definiuje on, jak pakiet powinien być zbudowany, jakie ma zależności i jakie dodatkowe pliki powinny zostać dołączone do dystrybucji.

- **`pip`:** Jest to narzędzie, które pozwala na instalację pakietów zdefiniowanych przez `setup.py` lub dostępnych w `PyPI`. Umożliwia instalację, aktualizację i usuwanie pakietów.

- **`PyPI`:** Python Package Index (PyPI) to repozytorium, które przechowuje większość publicznych pakietów Pythona. Użytkownicy mogą przesyłać swoje pakiety do PyPI, aby inni mogli je łatwo zainstalować za pomocą `pip`.

### Jak opublikować własny pakiet na `PyPI`

Aby opublikować pakiet na PyPI, należy wykonać kilka kroków:

I. Upewnij się, że Twój pakiet ma odpowiednio skonfigurowany plik `setup.py`. Powinien zawierać wszystkie niezbędne informacje, takie jak nazwa pakietu, wersja, autor, zależności itp.

II. Utwórz konto na [PyPI](https://pypi.org/) i na [Test PyPI](https://test.pypi.org/), które można użyć do testowania przesyłania pakietów.

III. Użyj `setuptools` do zbudowania swojego pakietu. Możesz to zrobić, uruchamiając poniższe polecenie w katalogu projektu:

```
python setup.py sdist bdist_wheel
```

To polecenie utworzy archiwum źródłowe oraz koło dystrybucyjne, które są preferowanym formatem dystrybucji.

IV. Przed oficjalnym opublikowaniem pakietu możesz przetestować proces przesyłania na Test PyPI, używając `twine`:

```
twine upload --repository testpypi dist/*
```

Po przetestowaniu, możesz zalogować się i sprawdzić, czy pakiet jest dostępny.

V. Jeśli wszystko jest gotowe, możesz opublikować swój pakiet na oficjalnym PyPI za pomocą:

```
twine upload dist/*
```

VI. Po opublikowaniu, Twój pakiet powinien być dostępny na PyPI i gotowy do instalacji przez każdego za pomocą:

```
pip install nazwa_twojego_pakietu
```

Pamiętaj, że utrzymanie pakietu to również aktualizowanie go o nowe funkcje, poprawki błędów oraz aktualizacje zależności, co jest ważne dla utrzymania dobrych praktyk bezpieczeństwa i kompatybilności.

### Linki

- [Oficjalna strona PyPI (Python Package Index)](https://pypi.org/) — repozytorium z pakietami dla Pythona.
- [Kompletna dokumentacja PIP](https://pip.pypa.io/en/stable/) — zawiera szczegółowe informacje na temat zarządzania pakietami w Pythonie.
- [PIP na GitHubie](https://github.com/pypa/pip) — kod źródłowy i projekt `pip`.
- [Narzędzie venv do tworzenia wirtualnych środowisk](https://docs.python.org/3/library/venv.html) — standardowe narzędzie w Python 3 do izolacji projektów.
- [Narzędzie virtualenv](https://virtualenv.pypa.io/en/latest/) — alternatywne narzędzie do tworzenia wirtualnych środowisk w Pythonie.
- [Porównanie menedżerów pakietów Pythona](https://packaging.python.org/guides/tool-recommendations/) — przewodnik po różnych dostępnych narzędziach i ich zastosowaniach.
- [Jak bezpiecznie korzystać z PyPI](https://pyfound.blogspot.com/2013/10/clarifying-peps-role-in-pypi.html) — wskazówki dotyczące bezpieczeństwa przy korzystaniu z pakietów.
