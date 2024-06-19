## Zarządzanie wersjami Pythona za pomocą Pyenv

`Pyenv` to narzędzie umożliwiające łatwe zarządzanie wieloma wersjami Pythona na jednym komputerze. Dzięki Pyenv można izolować różne projekty, korzystając z odpowiednich wersji Pythona dla każdego z nich, oraz testować kod pod różnymi wersjami interpretera, co jest kluczowe dla utrzymania kompatybilności i stabilności aplikacji.

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
