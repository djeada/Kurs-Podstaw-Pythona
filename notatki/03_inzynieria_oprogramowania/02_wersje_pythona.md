## Zarządzanie wersjami Pythona za pomocą Pyenv

`Pyenv` to narzędzie umożliwiające łatwe zarządzanie wieloma wersjami Pythona na jednym komputerze. Dzięki Pyenv można izolować różne projekty, korzystając z odpowiednich wersji Pythona dla każdego z nich, oraz testować kod pod różnymi wersjami interpretera, co jest kluczowe dla utrzymania kompatybilności i stabilności aplikacji.

### Dostępne wersje Pythona

| Wersja  | Data Wydania  | Główne Zmiany                                      |
|---------|---------------|--------------------------------------------------|
| 2.0     | 16.10.2000    | Wprowadzenie list comprehensions (wyrażenia listowe), detektor cyklu zbierania śmieci |
| 2.1     | 17.04.2001    | Wprowadzenie zagnieżdżonych zakresów, docstrings (dokumentacja w funkcjach) |
| 2.2     | 21.12.2001    | Nowy model typów i klas, generatory |
| 2.3     | 29.07.2003    | Wprowadzenie setów (zbiorów), nowa biblioteka datetime |
| 2.4     | 30.11.2004    | Dekoratory funkcji, wyrażenia generatorów |
| 2.5     | 19.09.2006    | Wprowadzenie instrukcji `with`, wyrażenia warunkowe |
| 2.6     | 01.10.2008    | Funkcje wstępne dla Pythona 3.x, poprawa błędów |
| 2.7     | 03.07.2010    | Ostatnia wersja z serii 2.x, wsparcie do 2020 roku, dictionary comprehensions (wyrażenia słownikowe), usprawnienia unittest |

| Wersja  | Data Wydania  | Główne Zmiany                                      |
|---------|---------------|--------------------------------------------------|
| 3.0     | 03.12.2008    | Przełomowe zmiany: print() jako funkcja, nowa semantyka stringów (unicode domyślnie), dzielenie całkowitoliczbowe |
| 3.1     | 27.06.2009    | Poprawa wydajności, nowa biblioteka I/O, OrderedDict |
| 3.2     | 20.02.2011    | Wsparcie dla `concurrent.futures`, `argparse`, formaty float repr |
| 3.3     | 29.09.2012    | Wprowadzenie `yield from`, kluczowych słów `faulthandler`, lustracja katalogów |
| 3.4     | 16.03.2014    | `asyncio`, enums, pathlib, poprawa modułu unittest |
| 3.5     | 13.09.2015    | Wprowadzenie `async` i `await`, operator mnożenia macierzy |
| 3.6     | 23.12.2016    | F-strings, zmiany w dicts, nowe funkcje async generators i comprehensions |
| 3.7     | 27.06.2018    | Klasy danych, odroczona ewaluacja adnotacji typów, zmienne kontekstowe.|
| 3.8     | 14.10.2019    | Assignment expressions (walrus operator :=), positional-only parameters |
| 3.9     | 05.10.2020    | Nowe operatory dla słowników, funkcje stringów removeprefix() i removesuffix() |
| 3.10    | 04.10.2021    | Pattern matching, lepsze wsparcie dla podpowiedzi typów, usprawnienia w zarządzaniu kontekstami |
| 3.11    | 03.10.2022    | Wzrost wydajności, lepsze debugowanie, dynamiczne profile i bardziej szczegółowe wyjątki |
| 3.12    | 02.10.2023    | Bardziej elastyczne parsowanie f-stringów, wsparcie dla protokołu buforowania, nowy API debugowania/profilowania, wsparcie dla izolowanych subinterpreterów z osobnymi Global Interpreter Locks, poprawa komunikatów błędów, wsparcie dla Linux perf profiler oraz liczne usprawnienia wydajnościowe |
| 3.13    | Planowana: 2024 | Wprowadzenie kompilatora JIT, poprawa wydajności, wprowadzenie PEP 649 (opóźniona ocena adnotacji), większa elastyczność i optymalizacja kodu |

### Sprawdzanie Zainstalowanej Wersji Pythona

Znajomość zainstalowanej wersji Pythona jest ważna, gdyż pozwala na odpowiednie dostosowanie środowiska pracy oraz rozwiązywanie problemów związanych z kompatybilnością. Sposób sprawdzenia zainstalowanej wersji różni się w zależności od systemu operacyjnego.

#### Linux

W systemach Linux, standardowe polecenie do sprawdzania wersji Pythona to:

```
python --version
```

Jeśli jednak Python 3 jest instalowany równolegle z Pythonem 2, bardziej specyficzne polecenie to:

```
python3 --version
```

#### Windows

W systemie Windows, sprawdzenie zainstalowanej wersji Pythona odbywa się przez otwarcie wiersza poleceń (Command Prompt) i wpisanie:

```
python --version
```

### Upgrade Pythona

Aktualizacja Pythona do nowszej wersji jest ważnym krokiem w utrzymaniu zgodności kodu i bezpieczeństwa aplikacji. Proces ten różni się w zależności od systemu operacyjnego i wybranej metody instalacji.

#### Linux

I. **Używanie Menedżera Pakietów:**

W większości dystrybucji Linux, aktualizacja Pythona może być wykonana za pomocą menedżera pakietów. Na przykład, na Ubuntu można użyć następujących komend:

```
sudo apt-get update
sudo apt-get upgrade python3
```

II. **Kompilacja ze Źródeł:**

Dla zaawansowanych użytkowników, możliwe jest też zaktualizowanie Pythona przez skompilowanie najnowszej wersji ze źródeł. Proces ten umożliwia bardziej szczegółową konfigurację i optymalizację. Kody do kompilacji na Ubuntu:

```
sudo apt-get install build-essential checkinstall
sudo apt-get install libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev
sudo ./configure
sudo make
sudo checkinstall
```

#### Windows

I. **Pobieranie Nowej Wersji:**

Aby zaktualizować Pythona na Windows, najlepiej jest pobrać najnowszą wersję instalatora ze strony [python.org](https://www.python.org). Instalator zwykle oferuje opcję automatycznego zastąpienia starej wersji nową.

```
# Przykład pobierania nowej wersji z python.org
```

II. **Używanie Pyenv:**

Użytkownicy `Pyenv` na Windows mogą łatwo zarządzać wersjami Pythona. Aby zaktualizować Pythona, wystarczy zainstalować nową wersję i ustawić ją jako domyślną:

```
pyenv install 3.x.x
pyenv global 3.x.x
```

Zamień `3.x.x` na numer żądanej wersji Pythona.

### Jak działa Pyenv?

Głównym zadaniem `Pyenv` jest manipulacja zmienną środowiskową `PATH`, aby umożliwić przełączanie między różnymi wersjami Pythona. Dodając ścieżkę do specjalnego folderu `(pyenv root)/shims` w zmiennej `PATH`, `Pyenv` pozwala na wybór odpowiedniej wersji Pythona w zależności od kontekstu, co jest niezwykle przydatne przy pracy z różnymi projektami.

### Instalacja

Aby zainstalować `Pyenv`, skorzystaj z poniższych oficjalnych repozytoriów, które dostarczają instrukcji instalacyjnych dostosowanych do różnych systemów operacyjnych:

* [Pyenv dla systemów UNIX-podobnych (Linux, MacOS)](https://github.com/pyenv/pyenv)
* [Pyenv dla Windows](https://github.com/pyenv-win/pyenv-win)

### Zarządzanie wersjami Pythona

I. **Instalacja konkretnej wersji Pythona**

Aby zainstalować żądaną wersję Pythona, użyj polecenia:

```bash
pyenv install 3.10.0
```

Zalecane jest podanie pełnego numeru wersji, np. `3.10.0`, a nie tylko `3.10`, aby uniknąć nieporozumień co do subwersji.

II. **Ustawienie wersji Pythona dla danego katalogu**

Możesz określić wersję Pythona specyficznie dla jednego projektu, co jest szczególnie użyteczne w dużych środowiskach deweloperskich, gdzie różne projekty mogą wymagać różnych wersji interpretera:

```bash
pyenv local 3.10.0
```

To polecenie utworzy plik `.python-version` w bieżącym katalogu, który informuje `Pyenv` o tym, jaką wersję Pythona należy używać w tym kontekście.

III. **Ustawienie globalnej wersji Pythona**

Aby zmienić wersję Pythona, która jest używana jako domyślna dla Twojego użytkownika, użyj polecenia:

```bash
pyenv global 3.10.0
```

IV. **Wyświetlanie listy dostępnych wersji Pythona**

Aby sprawdzić, które wersje Pythona są zainstalowane na Twoim systemie oraz która z nich jest aktualnie aktywna, użyj:

```bash
pyenv versions
```

V. **Sprawdzanie bieżącej wersji Pythona**

Aby szybko zweryfikować, która wersja Pythona jest aktualnie używana w danym środowisku pracy, skorzystaj z polecenia:

```bash
pyenv version
```
