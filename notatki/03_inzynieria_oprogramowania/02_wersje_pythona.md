## Zarządzanie wersjami Pythona za pomocą Pyenv

`Pyenv` to potężne narzędzie open-source, które umożliwia programistom łatwe zarządzanie wieloma wersjami Pythona na jednym komputerze. Dzięki `Pyenv` można nie tylko instalować i przełączać się między różnymi wersjami Pythona, ale także izolować środowiska dla poszczególnych projektów. Jest to szczególnie przydatne w sytuacjach, gdy pracujemy nad wieloma projektami wymagającymi różnych wersji Pythona lub gdy chcemy przetestować nasz kod pod kątem kompatybilności z różnymi wersjami interpretera.

### Zalety korzystania z Pyenv

- Pozwala na przypisanie konkretnej wersji Pythona do danego projektu, eliminując konflikty między zależnościami.
- Umożliwia szybkie przełączanie się między wersjami Pythona bez konieczności ponownej instalacji czy konfiguracji systemu.
- Ułatwia testowanie aplikacji pod różnymi wersjami Pythona, co jest kluczowe dla utrzymania kompatybilności.
- Proces instalacji i zarządzania jest prosty i intuicyjny, nawet dla początkujących użytkowników.

### Dostępne wersje Pythona

Python przeszedł długą drogę od swojego powstania, a każda kolejna wersja wprowadzała istotne zmiany i usprawnienia. Poniżej znajduje się zestawienie głównych wersji Pythona wraz z datami wydania i najważniejszymi zmianami, które wprowadzały.

#### Seria Python 2.x

| Wersja  | Data Wydania  | Główne Zmiany                                      |
|---------|---------------|--------------------------------------------------|
| **2.0**     | 16.10.2000    | - **List comprehensions** (wyrażenia listowe), umożliwiające tworzenie nowych list w bardziej zwięzły sposób.<br>- **Detektor cyklu w zbieraniu śmieci**, poprawiający zarządzanie pamięcią. |
| **2.1**     | 17.04.2001    | - Wprowadzenie **zagnieżdżonych zakresów** (nested scopes), pozwalających na lepsze zarządzanie zmiennymi w funkcjach.<br>- **Docstrings** (dokumentacja w funkcjach), umożliwiające dodawanie opisu funkcji bezpośrednio w jej definicji. |
| **2.2**     | 21.12.2001    | - Nowy **model typów i klas**, unifikujący klasy i typy.<br>- **Generatory**, wprowadzenie słowa kluczowego `yield`, umożliwiającego tworzenie iteratorów w prosty sposób. |
| **2.3**     | 29.07.2003    | - Wprowadzenie **setów** (zbiorów) jako nowego typu danych.<br>- Nowa biblioteka **datetime** do pracy z datami i czasem. |
| **2.4**     | 30.11.2004    | - **Dekoratory funkcji**, umożliwiające modyfikowanie funkcji w momencie ich definiowania.<br>- **Wyrażenia generatorów**, pozwalające na tworzenie generatorów w jednej linijce kodu. |
| **2.5**     | 19.09.2006    | - Wprowadzenie instrukcji **`with`**, ułatwiającej zarządzanie zasobami takimi jak pliki czy połączenia sieciowe.<br>- **Wyrażenia warunkowe**, pozwalające na skrócony zapis instrukcji warunkowych. |
| **2.6**     | 01.10.2008    | - Dodanie funkcji wprowadzonych w Pythonie 3.x, przygotowujących do migracji.<br>- Poprawki błędów i optymalizacje. |
| **2.7**     | 03.07.2010    | - Ostatnia wersja z serii 2.x, wsparcie przedłużone do 2020 roku.<br>- **Dictionary comprehensions** (wyrażenia słownikowe).<br>- Usprawnienia modułu **unittest**. |

#### Seria Python 3.x

| Wersja  | Data Wydania  | Główne Zmiany                                      |
|---------|---------------|--------------------------------------------------|
| **3.0**     | 03.12.2008    | - **Przełomowe zmiany** niekompatybilne z serią 2.x.<br>- `print()` jako funkcja zamiast instrukcji.<br>- Nowa semantyka napisów, gdzie **Unicode** jest domyślnym typem.<br>- Zmiana w operatorze dzielenia: `/` zwraca wynik zmiennoprzecinkowy, `//` całkowitoliczbowy. |
| **3.1**     | 27.06.2009    | - Poprawa wydajności.<br>- Nowa biblioteka wejścia/wyjścia.<br>- Wprowadzenie **`OrderedDict`** w module `collections`. |
| **3.2**     | 20.02.2011    | - Wsparcie dla modułu **`concurrent.futures`** do programowania równoległego.<br>- Nowy moduł **`argparse`** do analizy argumentów wiersza poleceń.<br>- Lepsza reprezentacja liczb zmiennoprzecinkowych. |
| **3.3**     | 29.09.2012    | - Wprowadzenie **`yield from`** dla generatorów.<br>- Nowe moduły takie jak **`faulthandler`**.<br>- Ulepszenia w funkcjach systemowych i plikowych. |
| **3.4**     | 16.03.2014    | - Wprowadzenie modułu **`asyncio`** do programowania asynchronicznego.<br>- **Typy wyliczeniowe** (enums) w module `enum`.<br>- Nowa biblioteka **`pathlib`** do obsługi ścieżek plików. |
| **3.5**     | 13.09.2015    | - Wprowadzenie słów kluczowych **`async`** i **`await`**.<br>- Operator **mnożenia macierzy** `@`. |
| **3.6**     | 23.12.2016    | - **Napisy formatowane (f-strings)**, ułatwiające wstawianie zmiennych do ciągów znaków.<br>- Poprawa wydajności słowników.<br>- Ulepszenia w asynchroniczności. |
| **3.7**     | 27.06.2018    | - **Dataclasses**, czyli prosty sposób na tworzenie klas danych.<br>- Odroczona ewaluacja adnotacji typów.<br>- **Context Variables** dla lepszego zarządzania stanem w programowaniu asynchronicznym. |
| **3.8**     | 14.10.2019    | - **Operator morsa `:=`**, umożliwiający przypisywanie w wyrażeniach.<br>- Wprowadzenie parametrów tylko pozycyjnych w funkcjach. |
| **3.9**     | 05.10.2020    | - Nowe operatory złączeń dla słowników: `|` i `|=`.<br>- Funkcje **`str.removeprefix()`** i **`str.removesuffix()`**. |
| **3.10**    | 04.10.2021    | - **Pattern Matching** (dopasowywanie wzorców), przypominające instrukcje `switch/case`.<br>- Ulepszenia w podpowiedziach typów. |
| **3.11**    | 03.10.2022    | - Znaczące poprawy wydajności.<br>- Lepsze komunikaty błędów.<br>- Ulepszenia w debugowaniu. |
| **3.12**    | 02.10.2023    | - Bardziej elastyczne **f-stringi**.<br>- Wsparcie dla protokołu buforowania.<br>- Nowe narzędzia do debugowania i profilowania.<br>- Wsparcie dla izolowanych podinterpreterów z osobnymi GIL (Global Interpreter Lock).<br>- Poprawa komunikatów błędów i wydajności. |
| **3.13**    | Planowana: 2024 | - Wprowadzenie kompilatora **JIT** (Just-In-Time) dla jeszcze lepszej wydajności.<br>- Implementacja **PEP 649** dotyczącego opóźnionej ewaluacji adnotacji.<br>- Dalsze optymalizacje i ulepszenia. |

### Sprawdzanie zainstalowanej wersji Pythona

Znajomość zainstalowanej wersji Pythona jest kluczowa dla odpowiedniego dostosowania środowiska pracy, instalacji kompatybilnych pakietów oraz rozwiązywania problemów związanych z kompatybilnością kodu.

#### Linux

W systemach Linux można sprawdzić zainstalowaną wersję Pythona za pomocą terminala:

```bash
python --version
```

Jeśli masz zainstalowane zarówno Pythona 2, jak i Pythona 3, możesz użyć:

```bash
python2 --version
python3 --version
```

Jeśli polecenie `python` odnosi się do Pythona 2, a chcesz użyć Pythona 3 jako domyślnego, możesz utworzyć alias:

```bash
alias python=python3
```

#### Windows

Na Windowsie otwórz Wiersz Poleceń (Command Prompt) lub PowerShell i wpisz:

```cmd
python --version
```

Jeśli pojawi się komunikat o błędzie, oznacza to, że Python nie jest dodany do zmiennej środowiskowej `PATH`. Możesz to naprawić, dodając ścieżkę do pliku `python.exe` do zmiennych środowiskowych lub zaznaczając opcję **"Add Python to PATH"** podczas instalacji.

### Upgrade Pythona

Aktualizacja Pythona jest ważna dla dostępu do najnowszych funkcjonalności, poprawek bezpieczeństwa i wydajności. Proces ten różni się w zależności od systemu operacyjnego.

#### Linux

**Używanie menedżera pakietów**

W dystrybucjach takich jak Ubuntu czy Debian, możesz zaktualizować Pythona za pomocą `apt`:

```bash
sudo apt-get update
sudo apt-get install python3
```

**Kompilacja ze źródeł**

Jeśli najnowsza wersja Pythona nie jest dostępna w repozytoriach, możesz skompilować ją samodzielnie.

I. Pobierz najnowszą wersję Pythona ze strony [python.org](https://www.python.org/downloads/source/).

II. Zainstaluj niezbędne biblioteki:

```bash
sudo apt-get install build-essential libssl-dev libffi-dev python3-dev
```

III. Rozpakuj i skompiluj źródła:

```bash
tar -xf Python-3.x.x.tgz
cd Python-3.x.x
./configure --enable-optimizations
make -j 8
sudo make altinstall
```

Użycie `make altinstall` zapobiega nadpisaniu domyślnej wersji Pythona.

#### Windows

**Pobieranie nowej wersji z internetu**

1. Pobierz instalator ze strony [python.org](https://www.python.org/downloads/windows/).
2. Uruchom instalator i postępuj zgodnie z instrukcjami. Upewnij się, że zaznaczasz opcję **"Add Python to PATH"**.
3. Aktualizacja istniejącej wersji** Jeśli masz zainstalowaną starszą wersję, instalator automatycznie ją zaktualizuje.

**Pyenv**

`Pyenv` dla Windows pozwala na zarządzanie wieloma wersjami Pythona.

I. Zainstaluj pyenv-win:

```cmd
pip install pyenv-win --target %USERPROFILE%\.pyenv
```

II. Dodaj do zmiennej PATH:

- `%USERPROFILE%\.pyenv\pyenv-win\bin`
- `%USERPROFILE%\.pyenv\pyenv-win\shims`

III. Instalacja nowej wersji Pythona:

```cmd
pyenv install 3.x.x
```

IV. Ustawienie wersji globalnej:

```cmd
pyenv global 3.x.x
```

### Jak działa Pyenv?

`Pyenv` manipuluje zmienną środowiskową `PATH`, aby przełączać między różnymi wersjami Pythona. Dodaje do niej ścieżkę do specjalnego katalogu **shims**, który zawiera "cienie" poleceń Pythona. Gdy uruchamiasz polecenie `python`, system najpierw sprawdza shims, które następnie kierują do odpowiedniej wersji Pythona, zgodnie z konfiguracją `Pyenv`.

#### Mechanizm działania

I. **Shims (cienie)**

Shims są małymi skryptami przechwytującymi wywołania do poleceń Pythona. Gdy użytkownik uruchamia polecenie, które odnosi się do Pythona (np. `python`, `pip`), pyenv najpierw przechwytuje to wywołanie i przekierowuje je do odpowiedniej wersji Pythona. Shims umożliwiają dynamiczne zarządzanie wersjami Pythona, pozwalając na przełączanie między nimi bez potrzeby bezpośredniej modyfikacji ścieżek w systemie operacyjnym. Działa to w tle i pozwala użytkownikowi korzystać z wybranej wersji Pythona zgodnie z kontekstem (globalnym, lokalnym lub środowiskowym).

II. **Zmienna `PYENV_VERSION`**

Ta zmienna środowiskowa jest jednym z mechanizmów definiujących, która wersja Pythona jest aktywna w danym momencie. Ustawienie `PYENV_VERSION` na konkretną wersję Pythona powoduje, że system będzie korzystać z tej wersji, dopóki zmienna pozostanie aktywna lub dopóki użytkownik nie zdefiniuje innej wersji dla konkretnego projektu. Jest to elastyczne rozwiązanie, pozwalające na chwilowe zmiany wersji, np. podczas sesji terminalowej.

III. **Plik `.python-version`**

Jest to lokalny plik konfiguracyjny, który można umieścić w katalogu projektu. Pyenv automatycznie wykrywa jego obecność i przypisuje wersję Pythona zgodnie z zawartością pliku. Jest to szczególnie przydatne dla projektów, które wymagają specyficznej wersji Pythona, zapewniając, że każdy użytkownik pracujący nad projektem będzie korzystać z tej samej wersji języka. Plik `.python-version` może być przechowywany w repozytorium projektu, co dodatkowo ułatwia zarządzanie wersjami w zespole programistycznym.

IV. **Kolejność priorytetów**

Pyenv ustala, z której wersji Pythona korzystać na podstawie hierarchii źródeł wersji. Hierarchia priorytetów wygląda następująco:

- **Zmienna środowiskowa `PYENV_VERSION`** — jeżeli jest ustawiona, jej wartość ma najwyższy priorytet i decyduje o aktywnej wersji Pythona.
- **Plik `.python-version`** w bieżącym katalogu — jeśli nie jest ustawiona zmienna `PYENV_VERSION`, pyenv sprawdza, czy istnieje plik `.python-version` w katalogu projektu. Jeżeli tak, pyenv używa wersji Pythona określonej w tym pliku.
- **Wersja globalna** ustawiona przez `pyenv global` — w przypadku braku pliku `.python-version` oraz zmiennej `PYENV_VERSION`, pyenv korzysta z globalnej wersji ustawionej za pomocą polecenia `pyenv global`.

### Instalacja

Aby zainstalować `Pyenv`, postępuj zgodnie z poniższymi instrukcjami dla swojego systemu operacyjnego.

#### Linux i MacOS

I. **Zainstaluj zależności**:

```bash
# Dla Ubuntu/Debiana
sudo apt-get update
sudo apt-get install -y make build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm \
libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev
```

II. **Zainstaluj Pyenv**:

```bash
curl https://pyenv.run | bash
```

III. **Zaktualizuj plik konfiguracji shel'a**:

Dodaj następujące linie do `~/.bashrc` lub `~/.zshrc`:

```bash
export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init --path)"
eval "$(pyenv virtualenv-init -)"
```

IV. **Zrestartuj terminal** lub wykonaj:

```bash
source ~/.bashrc
```

#### Windows

I. **Pobierz i zainstaluj pyenv-win** z [repozytorium GitHub](https://github.com/pyenv-win/pyenv-win#installation).

II. **Dodaj ścieżki do zmiennych środowiskowych**:

- `%USERPROFILE%\.pyenv\pyenv-win\bin`
- `%USERPROFILE%\.pyenv\pyenv-win\shims`

III. **Sprawdź instalację**:

```cmd
pyenv --version
```

### Zarządzanie wersjami Pythona

#### Instalacja konkretnej wersji Pythona

Aby zainstalować konkretną wersję Pythona, użyj polecenia:

```bash
pyenv install 3.10.0
```

Możesz wyświetlić listę dostępnych wersji za pomocą:

```bash
pyenv install --list
```

####  Ustawienie wersji Pythona dla danego katalogu

Jeśli chcesz, aby w danym projekcie używana była konkretna wersja Pythona:

I. Przejdź do katalogu projektu:

```bash
cd /ścieżka/do/projektu
```

II. Ustaw wersję lokalną:

```bash
pyenv local 3.10.0
```

Utworzy to plik `.python-version` z numerem wersji.

#### Ustawienie globalnej wersji Pythona

Aby ustawić domyślną wersję Pythona dla całego systemu użytkownika:

```bash
pyenv global 3.10.0
```

#### Wyświetlanie listy dostępnych wersji Pythona

Aby zobaczyć, które wersje Pythona są zainstalowane:

```bash
pyenv versions
```

Przykładowy wynik:

```bash
  system
* 3.8.0 (set by /home/user/.pyenv/version)
  3.9.0
  3.10.0
```

#### V. Sprawdzanie bieżącej wersji Pythona

Aby sprawdzić, która wersja Pythona jest aktualnie aktywna:

```bash
pyenv version
```

### Dodatkowe informacje

**Aktualizacja Pyenv**:

Aby zaktualizować `Pyenv` do najnowszej wersji, wykonaj:

```bash
cd $(pyenv root)
git pull
```

**Usuwanie wersji Pythona**:

Jeśli chcesz usunąć zainstalowaną wersję:

```bash
pyenv uninstall 3.9.0
```

**Integracja z Virtualenv**:

Pyenv współpracuje z pyenv-virtualenv, umożliwiając łatwe tworzenie i zarządzanie wirtualnymi środowiskami dla wielu wersji Pythona, co jest przydatne przy pracy nad projektami z różnymi wymaganiami co do wersji. Tworzenie środowiska dla konkretnej wersji Pythona odbywa się za pomocą polecenia `pyenv virtualenv`, np. `pyenv virtualenv 3.8.10 myenv-3.8` tworzy środowisko `myenv-3.8` działające na wersji 3.8.10. Można łatwo aktywować to środowisko przez `pyenv activate myenv-3.8`, a dezaktywować je komendą `pyenv deactivate`. Pyenv wykrywa także lokalny plik `.python-version` w katalogu projektu, co pozwala automatycznie aktywować przypisane środowisko przy wejściu do katalogu projektu – jest to pomocne przy pracy zespołowej, gdyż zapewnia zgodność środowisk na różnych maszynach. Pełna lista dostępnych wersji i środowisk jest dostępna przez `pyenv versions`, gdzie aktywne środowisko oznaczone jest gwiazdką. Usuwanie środowisk odbywa się za pomocą polecenia `pyenv uninstall myenv-3.8`, co pozwala utrzymać porządek i zapobiegać gromadzeniu niepotrzebnych środowisk.
