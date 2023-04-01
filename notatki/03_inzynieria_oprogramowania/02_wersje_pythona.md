
## Wersje Pythona

Narzędzie <code>Pyenv</code> służy do izolowania różnych wersji Pythona. Jeśli na przykład chcesz przetestować swój kod w Pythonie 2.5, 3.6 i 3.10, potrzebujesz prostego sposobu na przełączanie się między nimi. <code>Pyenv</code> modyfikuje zmienną środowiskową PATH dodając do niej ścieżkę do specjalnego folderu <code>(pyenv root)/shims</code>. Ponadto <code>Pyenv</code> umożliwia pobieranie i instalowanie różnych wersji Pythona za pomocą polecenia <code>pyenv install</code>.

Linki:

* https://github.com/pyenv/pyenv
* https://github.com/pyenv-win/pyenv-win

Po zainstalowaniu pyenv, możemy użyć polecenia pyenv install aby zainstalować nową wersję Pythona. Na przykład, aby zainstalować wersję Python 3.10, użyjemy polecenia:

```python
pyenv install 3.10
```

Aby ustawić wersję Pythona, która będzie używana dla danego katalogu, użyj polecenia pyenv local:

```python
pyenv local 3.10
```

Aby ustawić wersję Pythona, która będzie używana dla całego systemu, użyj polecenia pyenv global:

```python
pyenv global 3.10
```

Aby wyświetlić listę zainstalowanych wersji Pythona, użyj polecenia pyenv versions:

```python
pyenv versions
```

Aby wyświetlić bieżącą wersję Pythona, użyj polecenia pyenv version:

```python
pyenv version
```
