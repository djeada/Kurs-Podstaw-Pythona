## PIP i PyPI

`PIP` (Python Package Installer) to menedżer pakietów dla języka Python, który pozwala na łatwą instalację, aktualizację i usunięcie pakietów dostępnych w repozytorium `PyPI` (Python Package Index).

### Instalacja PIP

1. Pobierz skrypt [get-pip.py](https://bootstrap.pypa.io/get-pip.py).
2. Uruchom skrypt za pomocą:

```bash
python get-pip.py
```

3. Sprawdź, czy instalacja przebiegła pomyślnie, wywołując:

```bash
pip help
```

### Podstawowe operacje z PIP

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

Używając poniższego polecenia, możesz zapisać listę zainstalowanych pakietów wraz z ich wersjami do pliku requirements.txt.

```bash
pip freeze > requirements.txt
```

- Instalacja pakietów z pliku requirements.txt:

```bash
pip install -r requirements.txt
```

- Odinstalowywanie pakietu:

```bash
pip uninstall nazwa_pakietu
```

- Aktualizacja PIP:

```bash
pip install --upgrade pip
```

- Wyszukiwanie pakietów:

Możesz wyszukać pakiet w repozytorium PyPI za pomocą:

```bash
pip search nazwa_pakietu
```

### Aktualizacja pakietów

- Aktualizacja konkretnego pakietu:

```bash
pip install --upgrade nazwa_pakietu
```

- Aktualizacja wszystkich pakietów:

Możesz użyć poniższego polecenia, aby uzyskać listę przestarzałych pakietów:

```bash
pip list --outdated
```

Następnie aktualizuj je przy użyciu `pip install --upgrade`.

### Linki

- [Oficjalna strona PyPI (Python Package Index)](https://pypi.org/)
- [Kompletna dokumentacja PIP](https://pip.pypa.io/en/stable/)
- [PIP na GitHubie](https://github.com/pypa/pip)
- [Narzędzie venv do tworzenia wirtualnych środowisk](https://docs.python.org/3/library/venv.html)
- [Narzędzie virtualenv](https://virtualenv.pypa.io/en/latest/)
- [Porównanie menedżerów pakietów Pythona](https://packaging.python.org/guides/tool-recommendations/)
- [Jak bezpiecznie korzystać z PyPI](https://pyfound.blogspot.com/2013/10/clarifying-peps-role-in-pypi.html)
