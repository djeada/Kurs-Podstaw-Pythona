## Środowisko wirtualne

Środowisko wirtualne to mechanizm, który pozwala na tworzenie odizolowanych przestrzeni dla różnych projektów Pythona. Zapewnia to, że każdy projekt może mieć własne zależności, niezależnie od innych projektów. Dzięki temu możemy unikać potencjalnych konfliktów związanych z różnymi wersjami bibliotek.

### Zalety używania środowisk wirtualnych

1. Każde środowisko wirtualne ma własne niezależne biblioteki i wersje Pythona, co oznacza, że aktualizacje lub zmiany w jednym projekcie nie wpłyną na inny. To szczególnie przydatne w dużych zespołach, gdzie różne projekty mogą wymagać różnych wersji tej samej biblioteki.
2. Zarządzanie zależnościami staje się łatwiejsze, ponieważ wszystkie biblioteki wymagane przez projekt są instalowane w izolacji od globalnego środowiska. To ułatwia także wdrożenia, ponieważ lista zależności jest jasno zdefiniowana i łatwa do zreplikowania w innym środowisku.
3. Środowiska wirtualne gwarantują, że aplikacje będą działać tak samo na różnych maszynach deweloperskich, jak i serwerach produkcyjnych, co minimalizuje "działa u mnie" syndrom błędów.
4. Ustawienie nowego środowiska wirtualnego jest proste i może być szybko skonfigurowane z minimalnym nakładem pracy, co jest idealne dla nowych członków zespołu lub podczas rozpoczynania nowych projektów.
5. Izolacja zależności minimalizuje ryzyko związane z nieautoryzowanym dostępem do systemów przez zależności, ponieważ każdy projekt może ograniczać się do minimalnie wymaganych uprawnień.
6. Środowiska wirtualne umożliwiają bezpieczne eksperymentowanie z nowymi pakietami i wersjami bez ryzyka zakłócenia działania stabilnych aplikacji. Dzięki temu można testować nowe wersje bibliotek bez wpływu na istniejące projekty.
7. Wiele projektów może wymagać różnych wersji Pythona. Środowiska wirtualne pozwalają na łatwe przełączanie między wersjami Pythona, co jest niezbędne w środowiskach, gdzie trwająca konserwacja kodu wymaga pracy na wielu wersjach języka.

### Virtualenv: Izolacja Środowisk i Zarządzanie Zależnościami w Pythonie

Virtualenv tworzy **wirtualne środowiska**, które są kopiami określonej instalacji Pythona, ale działają niezależnie od globalnych pakietów zainstalowanych w systemie. Każde takie środowisko posiada swój własny interpreter Pythona oraz zestaw bibliotek, co umożliwia elastyczne zarządzanie projektami o różnych wymaganiach.

#### I. Instalacja Virtualenv

Aby zainstalować Virtualenv, potrzebujemy narzędzia **pip**, które jest domyślnym menedżerem pakietów w Pythonie. Instalację Virtualenv wykonujemy poleceniem:

```bash
pip install virtualenv
```

##### Sprawdzenie Instalacji

Aby upewnić się, że virtualenv został zainstalowany prawidłowo, można wyświetlić wersję narzędzia:

```bash
virtualenv --version
```

Poprawna instalacja zwróci wersję Virtualenv.

#### II. Tworzenie Nowego Środowiska Wirtualnego

Utworzenie środowiska wirtualnego to kluczowy krok w separacji zależności. Za pomocą polecenia:

```bash
virtualenv env
```

tworzymy środowisko wirtualne o nazwie `env` w bieżącym katalogu. Środowisko to posiada własny katalog z interpreterem Pythona oraz zbiorem domyślnych bibliotek. Jeśli chcemy utworzyć środowisko z konkretną wersją Pythona, możemy to zrobić w następujący sposób:

```bash
virtualenv -p /usr/bin/python3 env
```

Tym samym wybieramy wersję interpretera, który znajduje się pod ścieżką `/usr/bin/python3`.

##### Ogólne Zasady Działania

Virtualenv działa na zasadzie kopii plików binarnych Pythona do nowego katalogu, co gwarantuje, że zmiany globalne w systemie (np. aktualizacje) nie wpłyną na działające środowisko wirtualne. W matematyce podobny koncept znajduje zastosowanie w topologii, gdzie operujemy na **przestrzeniach lokalnych**, niezależnych od siebie, ale powiązanych ze wspólnym **globalnym zbiorem** (w tym przypadku instalacją systemową Pythona).

#### III. Aktywacja Środowiska Wirtualnego

Aktywacja środowiska wirtualnego to proces, w którym zmieniamy domyślny interpreter i zestaw bibliotek na ten zawarty w środowisku wirtualnym. W systemach Unixowych, takich jak Linux i macOS, aktywacja odbywa się za pomocą polecenia:

```bash
source env/bin/activate
```

W systemach Windows aktywacja wygląda inaczej:

```bash
env\Scripts\activate
```

Po aktywacji, w terminalu przed nazwą ścieżki powinno pojawić się `(env)`, co informuje nas, że znajdujemy się w kontekście wirtualnego środowiska. To jak zmiana **przestrzeni roboczej** w matematyce — gdy przełączymy się do nowej przestrzeni, nasze operacje są ograniczone do niej.

#### IV. Dezaktywacja Środowiska Wirtualnego

Aby wyjść z wirtualnego środowiska i powrócić do globalnego interpretera Pythona, wystarczy wpisać:

```bash
deactivate
```

Po dezaktywacji terminal wraca do normalnego trybu, a wszelkie operacje na Pythonie odbywają się w kontekście globalnym.

#### V. Zarządzanie Zależnościami: Pip i Requirements.txt

Virtualenv współpracuje z narzędziem **pip**, które zarządza pakietami w Pythonie. Gdy zainstalujemy nową bibliotekę w aktywnym środowisku wirtualnym, zostanie ona dodana tylko do tego konkretnego środowiska, nie mając wpływu na inne projekty.

##### Zapisywanie Zależności

Aby zapisać listę wszystkich zainstalowanych pakietów w środowisku wirtualnym, używamy polecenia:

```bash
pip freeze > requirements.txt
```

Plik `requirements.txt` zawiera pełną listę zainstalowanych bibliotek wraz z ich wersjami. Taki plik jest kluczowy w projektach programistycznych, zwłaszcza w zespołach, gdzie musimy zapewnić, że każdy korzysta z tych samych wersji bibliotek. W matematycznych algorytmach to odpowiednik **zapisania stanu** algorytmu, tak aby każdy mógł go odtworzyć.

##### Instalacja Zależności

Aby zainstalować wszystkie pakiety wymienione w pliku `requirements.txt`, używamy:

```bash
pip install -r requirements.txt
```

To polecenie odczytuje plik `requirements.txt` i instaluje wszystkie zawarte tam pakiety z dokładnie określonymi wersjami. Taki sposób zarządzania jest kluczowy w unikaniu **konfliktów wersji** oraz w tworzeniu replikowalnych środowisk.

#### VI. Zastosowanie Virtualenv w Projektach

##### Przykład: Wykorzystanie różnych wersji bibliotek

Załóżmy, że pracujemy nad dwoma projektami:
1. Projekt A wymaga wersji 1.15 biblioteki NumPy.
2. Projekt B wymaga wersji 1.18 biblioteki NumPy.

Gdybyśmy instalowali te biblioteki globalnie, pojawiłby się konflikt. Użycie Virtualenv umożliwia utrzymanie różnych wersji bibliotek w oddzielnych środowiskach. W ten sposób w projekcie A możemy zainstalować NumPy 1.15:

```bash
pip install numpy==1.15
```

a w projekcie B NumPy 1.18:

```bash
pip install numpy==1.18
```

Dzięki izolacji środowisk oba projekty działają poprawnie, bez konfliktów wersji bibliotek.

##### Przykład: Testowanie różnych wersji Pythona

Virtualenv umożliwia również testowanie projektów na różnych wersjach Pythona. Możemy utworzyć jedno środowisko z Pythonem 3.8 i drugie z Pythonem 3.9, a następnie sprawdzić, jak nasz kod działa w każdej z wersji.

```bash
virtualenv -p /usr/bin/python3.8 env_py38
virtualenv -p /usr/bin/python3.9 env_py39
```

### venv

**venv** to wbudowane narzędzie w Pythonie, które umożliwia tworzenie izolowanych środowisk uruchomieniowych. Działa bardzo podobnie do **virtualenv**, ale jest dostępne od Pythona 3.3, co eliminuje konieczność instalacji zewnętrznych pakietów. Tworzenie takich środowisk pozwala na oddzielenie zależności projektów oraz łatwe zarządzanie różnymi wersjami bibliotek i interpretera Pythona.

#### I. Tworzenie Nowego Środowiska za pomocą venv

Aby utworzyć nowe środowisko wirtualne, używamy modułu **venv**, który jest częścią standardowej biblioteki Pythona. Tworzenie nowego środowiska odbywa się za pomocą następującego polecenia:

```bash
python3 -m venv env
```

Powyższe polecenie tworzy nowe środowisko w katalogu `env`. Środowisko to zawiera własny interpreter Pythona oraz katalog `lib` na zainstalowane pakiety.

##### Wersja Pythona

Domyślnie `venv` używa tej samej wersji Pythona, z którą został uruchomiony, ale możemy też wybrać konkretną wersję, np. Python 3.9:

```bash
python3.9 -m venv env
```

W tym przypadku `venv` utworzy środowisko korzystające z Pythona 3.9, nawet jeśli mamy zainstalowane inne wersje Pythona.

##### Struktura Środowiska

Tworząc środowisko za pomocą `venv`, narzędzie to tworzy strukturę katalogów, która zawiera:
- **bin** (Unix) lub **Scripts** (Windows): Interpreter Pythona i skrypty aktywujące/dezaktywujące środowisko.
- **lib**: Katalog na pakiety zainstalowane w tym środowisku.
- **pyvenv.cfg**: Plik konfiguracyjny, który zawiera informacje o środowisku, m.in. o używanej wersji Pythona.

#### II. Aktywacja Środowiska venv

Po utworzeniu środowiska, należy je aktywować, aby móc pracować w jego kontekście. Aktywacja środowiska w systemach Unixowych (Linux, macOS) odbywa się za pomocą komendy:

```bash
source env/bin/activate
```

Dla systemów Windows polecenie aktywujące wygląda następująco:

```bash
env\Scripts\activate
```

Po aktywacji środowiska, w terminalu przed ścieżką pojawi się nazwa środowiska, np. `(env)`, co oznacza, że obecnie pracujemy w kontekście tego środowiska wirtualnego.

#### III. Dezaktywacja Środowiska venv

Aby wyjść ze środowiska wirtualnego i powrócić do globalnego interpretera Pythona, wystarczy wpisać polecenie:

```bash
deactivate
```

To jak zmiana przestrzeni roboczej w matematycznych przestrzeniach podzbiorów — po dezaktywacji wracamy do kontekstu globalnego (systemowego) Pythona.

#### IV. Zarządzanie Zależnościami w Środowisku venv

Jednym z kluczowych zastosowań izolowanych środowisk jest zarządzanie zależnościami projektów. W aktywowanym środowisku venv można instalować pakiety za pomocą **pip**, a instalacje te będą ograniczone wyłącznie do tego środowiska.

##### Instalacja Pakietów

Po aktywacji środowiska możemy zainstalować potrzebne pakiety w taki sam sposób jak globalnie, używając pip. Na przykład, aby zainstalować bibliotekę NumPy:

```bash
pip install numpy
```

Pakiety te zostaną zainstalowane tylko w środowisku `env`, a globalny system nie będzie na nie narażony.

##### Zapisywanie Zależności

Aby zapisać aktualny stan zainstalowanych bibliotek do pliku `requirements.txt`, możemy użyć polecenia:

```bash
pip freeze > requirements.txt
```

Plik ten może być później użyty do odtworzenia dokładnie tych samych zależności w innym środowisku.

##### Instalacja Zależności z Pliku

Aby odtworzyć zależności w nowym środowisku na podstawie pliku `requirements.txt`, należy użyć:

```bash
pip install -r requirements.txt
```

To zapewnia, że wszystkie pakiety będą zainstalowane w odpowiednich wersjach, co jest kluczowe dla utrzymania spójności projektu.

#### V. Zastosowanie venv w Praktyce

##### Przykład 1: Praca nad różnymi projektami z różnymi zależnościami

Załóżmy, że mamy dwa projekty:
1. **Projekt A**, który wymaga Pythona 3.8 i pakietu Flask w wersji 1.1.
2. **Projekt B**, który wymaga Pythona 3.9 i pakietu Flask w wersji 2.0.

Użycie globalnej instalacji Pythona prowadziłoby do konfliktów wersji. Jednak dzięki narzędziu **venv**, możemy utworzyć dwa izolowane środowiska:

Dla projektu A:

```bash
python3.8 -m venv env_A
source env_A/bin/activate
pip install flask==1.1
```

Dla projektu B:

```bash
python3.9 -m venv env_B
source env_B/bin/activate
pip install flask==2.0
```

W ten sposób oba projekty mogą działać bez problemów, każdy w swoim własnym środowisku z odpowiednimi wersjami interpretera i zależności.

##### Przykład 2: Testowanie aplikacji na różnych wersjach Pythona

Testowanie kompatybilności kodu z różnymi wersjami Pythona jest proste dzięki `venv`. Możemy utworzyć różne środowiska z różnymi wersjami Pythona i sprawdzić, czy nasz kod działa poprawnie:

Środowisko z Pythonem 3.8:

```bash
python3.8 -m venv env_py38
source env_py38/bin/activate
```

Środowisko z Pythonem 3.9:

```bash
python3.9 -m venv env_py39
source env_py39/bin/activate
```

Po aktywacji odpowiedniego środowiska możemy uruchomić testy i upewnić się, że nasza aplikacja działa w każdej wersji Pythona.

### Conda

**Conda** to wszechstronne narzędzie do zarządzania środowiskami i pakietami, popularne wśród użytkowników Pythona, R, oraz innych języków programowania. Umożliwia łatwe tworzenie i zarządzanie izolowanymi środowiskami wirtualnymi oraz instalację różnych bibliotek i pakietów, nie tylko w języku Python. W przeciwieństwie do narzędzi takich jak **virtualenv** czy **venv**, **conda** może zarządzać nie tylko zależnościami Pythonowymi, ale także innymi narzędziami systemowymi i bibliotekami, co czyni ją bardziej wszechstronną.

#### I. Instalacja Conda

Aby korzystać z **conda**, możemy zainstalować pełną dystrybucję **Anaconda** lub lżejszą wersję **Miniconda**, która zawiera tylko podstawowe narzędzia i pozwala na instalowanie jedynie niezbędnych pakietów.

##### Instalacja Miniconda

Miniconda to bardziej minimalistyczne podejście, które instaluje tylko conda i pozwala na samodzielne doinstalowanie reszty narzędzi i pakietów:

1. Pobierz instalator Miniconda odpowiedni dla twojego systemu operacyjnego z [oficjalnej strony Miniconda](https://docs.conda.io/en/latest/miniconda.html).
2. Po pobraniu, uruchom instalator i postępuj zgodnie z instrukcjami.
3. Po zainstalowaniu upewnij się, że conda działa poprawnie, sprawdzając wersję:

```bash
conda --version
```

#### II. Tworzenie Nowego Środowiska Conda

Tworzenie izolowanego środowiska w Conda jest kluczowym elementem pracy z tym narzędziem. Środowiska te mogą zawierać różne wersje Pythona, bibliotek oraz innych narzędzi systemowych.

##### Tworzenie Środowiska z Pythonem

Aby stworzyć nowe środowisko, używamy polecenia `conda create`. Na przykład, aby stworzyć środowisko z wersją Pythona 3.9:

```bash
conda create --name myenv python=3.9
```

To polecenie tworzy środowisko o nazwie `myenv`, w którym zainstalowany zostanie Python 3.9. Nazwa środowiska może być dowolnie wybrana, np. `myenv` może być zastąpione przez nazwę projektu.

##### Ogólne Zasady Działania

Tworzenie środowiska w Conda to proces podobny do tworzenia "osobnych światów" dla każdego projektu. W środowiskach tych możemy mieć różne wersje bibliotek i narzędzi, które są izolowane od siebie, co przypomina tworzenie różnych **układów współrzędnych** w algebrze liniowej. Każde środowisko działa w swoim własnym układzie współrzędnych, a operacje wykonywane w jednym środowisku nie mają wpływu na inne.

#### III. Aktywacja i Dezaktywacja Środowiska Conda

Aby aktywować środowisko Conda, używamy polecenia `activate`:

```bash
conda activate myenv
```

Po aktywacji, w terminalu przed ścieżką pojawi się nazwa środowiska, np. `(myenv)`, co oznacza, że pracujemy w kontekście tego środowiska.

Aby dezaktywować środowisko i powrócić do globalnego systemowego Pythona, używamy:

```bash
conda deactivate
```

#### IV. Zarządzanie Pakietami w Conda

Conda umożliwia instalację, aktualizację i usuwanie pakietów, nie tylko tych napisanych w Pythonie, ale również innych narzędzi, takich jak biblioteki C, C++ czy systemowe narzędzia deweloperskie.

##### Instalacja Pakietów

Aby zainstalować pakiet w aktywnym środowisku, używamy polecenia `conda install`. Na przykład, aby zainstalować bibliotekę NumPy:

```bash
conda install numpy
```

Conda automatycznie zadba o odpowiednie wersje zależności. Możemy także instalować pakiety z określonymi wersjami, np.:

```bash
conda install numpy=1.18
```

Conda wyszuka odpowiednią wersję pakietu oraz jego zależności w repozytoriach i zainstaluje wszystko automatycznie.

##### Usuwanie Pakietów

Aby usunąć pakiet z aktywnego środowiska, używamy polecenia:

```bash
conda remove numpy
```

##### Aktualizacja Pakietów

Pakiety w Conda mogą być łatwo aktualizowane do najnowszych wersji:

```bash
conda update numpy
```

Conda sprawdza, czy istnieje nowa wersja pakietu oraz jego zależności i aktualizuje je, minimalizując ryzyko konfliktów.

#### V. Praca z Plikami `environment.yml`

**environment.yml** to plik konfiguracyjny, który zawiera informacje o środowisku, takie jak jego nazwa, wersja Pythona oraz lista pakietów do zainstalowania. Plik ten można wykorzystać do przenoszenia i odtwarzania środowisk w różnych systemach.

##### Tworzenie Pliku environment.yml

Aby wygenerować plik `environment.yml` z aktualnego środowiska, używamy:

```bash
conda env export > environment.yml
```

Plik ten zawiera pełną specyfikację środowiska, co pozwala na jego odtworzenie na innym komputerze.

##### Tworzenie Środowiska z Pliku environment.yml

Aby stworzyć środowisko na podstawie pliku `environment.yml`, należy użyć:

```bash
conda env create -f environment.yml
```

To polecenie odtworzy środowisko z dokładnie tymi samymi wersjami pakietów i zależnościami.

#### VI. Zastosowanie Conda w Praktyce

##### Przykład 1: Praca nad różnymi projektami z różnymi wersjami Pythona

Załóżmy, że pracujemy nad dwoma projektami:

1. **Projekt A** wymaga Pythona 3.8 i pakietu Flask.
2. **Projekt B** wymaga Pythona 3.9 i pakietu Django.

Dzięki Conda możemy stworzyć dwa izolowane środowiska:

Dla projektu A:

```bash
conda create --name projA python=3.8 flask
conda activate projA
```

Dla projektu B:

```bash
conda create --name projB python=3.9 django
conda activate projB
```

Każde środowisko ma swoją własną wersję Pythona oraz pakietów, co eliminuje konflikty wersji.

##### Przykład 2: Przenoszenie środowisk między komputerami

Możemy stworzyć plik `environment.yml` z pełną specyfikacją środowiska:

```bash
conda env export > environment.yml
```

Następnie, aby odtworzyć to środowisko na innym komputerze, wystarczy użyć:

```bash
conda env create -f environment.yml
```

Dzięki temu wszystkie zależności zostaną zainstalowane w dokładnie tych samych wersjach, co na pierwotnym komputerze.

#### VII. Zarządzanie Różnymi Kanałami Pakietów

Conda korzysta z tzw. **kanałów** do zarządzania repozytoriami pakietów. Domyślnym kanałem jest `

defaults`, ale możemy korzystać z innych, np. **conda-forge** — popularnego kanału społecznościowego oferującego szeroką gamę pakietów.

##### Dodawanie Kanałów

Aby dodać kanał `conda-forge`, używamy:

```bash
conda config --add channels conda-forge
```

Po dodaniu kanału Conda będzie przeszukiwać go w poszukiwaniu pakietów.

### Porównanie różnych środowisk wirtualnych

| Środowisko wirtualne | Cechy charakterystyczne                          | Zalety                                            | Wady                                          |
|----------------------|--------------------------------------------------|---------------------------------------------------|-----------------------------------------------|
| virtualenv          | Bardziej elastyczne niż `venv`, wspiera starsze wersje Pythona | Wysoka kompatybilność wsteczna, może tworzyć środowiska dla dowolnej wersji Pythona | Może być redundantne na nowszych wersjach Pythona z `venv` |
| venv                 | Standardowe narzędzie w Pythonie do izolacji pakietów | Proste w użyciu, zintegrowane z Pythonem           | Brak zaawansowanego zarządzania zależnościami, nie zarządza Pythonem |
| conda                | Zarządza pakietami oraz środowiskami, obsługuje wiele języków | Zarządza zarówno pakietami jak i wersjami Pythona, działa na wielu platformach | Może być wolniejsze, niektóre pakiety mogą być nieaktualne |
| pipenv               | Automatycznie tworzy i zarządza wirtualnymi środowiskami, dodaje obsługę Pipfile i Pipfile.lock | Łatwe zarządzanie zależnościami, automatyzacja środowiska | Mniej popularne niż inne narzędzia, wolniejsze niż czysty pip |

### Linki

- [Oficjalna strona Virtualenv](https://virtualenv.pypa.io/en/latest/)
- [Repozytorium Virtualenv na GitHubie](https://github.com/pypa/virtualenv)
- [Dokumentacja Venv w Pythonie](https://docs.python.org/3/library/venv.html)
- [Poradnik po środowiskach wirtualnych w Pythonie](https://realpython.com/python-virtual-environments-a-primer/)
