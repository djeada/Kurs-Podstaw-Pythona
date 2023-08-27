## Zarządzanie wersjami Pythona za pomocą Pyenv

`Pyenv` to narzędzie, które pozwala łatwo zarządzać wieloma wersjami Pythona na jednym komputerze. Dzięki niemu możemy nie tylko izolować różne projekty od siebie, korzystając z różnych wersji Pythona, ale także przetestować nasz kod pod różnymi wersjami interpretera.

### Jak działa Pyenv?

Głównym zadaniem `Pyenv` jest manipulacja zmienną środowiskową `PATH`. Narzędzie to dodaje ścieżkę do specjalnego folderu `(pyenv root)/shims`, co pozwala na wybór odpowiedniej wersji Pythona w zależności od kontekstu.

### Instalacja

Aby zainstalować `Pyenv`, możesz skorzystać z oficjalnych repozytoriów:

* [Pyenv dla systemów UNIX-podobnych (Linux, MacOS)](https://github.com/pyenv/pyenv)
* [Pyenv dla Windows](https://github.com/pyenv-win/pyenv-win)

### Zarządzanie wersjami Pythona

1. **Instalacja konkretnej wersji Pythona**

    Aby zainstalować żądaną wersję Pythona, użyj polecenia:

    ```bash
    pyenv install 3.10.0
    ```

    Zwróć uwagę na to, że warto podać pełny numer wersji, w tym przypadku `3.10.0`, a nie tylko `3.10`.

2. **Ustawienie wersji Pythona dla danego katalogu**

    Jeśli chcesz ustawić wersję Pythona specyficznie dla jednego projektu, użyj polecenia:

    ```bash
    pyenv local 3.10.0
    ```

    Spowoduje to utworzenie pliku `.python-version` w bieżącym katalogu, który informuje `Pyenv` o tym, jaką wersję Pythona należy używać w tym konkretnym kontekście.

3. **Ustawienie globalnej wersji Pythona**

    Jeśli chcesz zmienić wersję Pythona, która jest używana jako domyślna dla Twojego użytkownika, użyj:

    ```bash
    pyenv global 3.10.0
    ```

4. **Wyświetlanie listy dostępnych wersji Pythona**

    Aby sprawdzić, które wersje Pythona są zainstalowane na Twoim systemie, użyj:

    ```bash
    pyenv versions
    ```

5. **Sprawdzanie bieżącej wersji Pythona**

    Aby sprawdzić aktualnie używaną wersję Pythona, użyj polecenia:

    ```bash
    pyenv version
    ```

Korzystanie z `Pyenv` pozwala na elastyczne zarządzanie wersjami Pythona, co jest szczególnie przydatne w środowiskach deweloperskich i przy wielu projektach opartych na różnych wersjach interpretera.
