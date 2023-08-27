## Dbanie o jakość kodu i lintowanie

Kod może być składniowo poprawny, ale jednocześnie nieczytelny lub źle zorganizowany. Przestrzeganie pewnych standardów i konwencji pisania kodu jest niezbędne, zwłaszcza gdy w projekcie uczestniczy wielu programistów. Konwencje te opisane są w dokumentach PEP (Python Enhancement Proposals), a wśród nich wyróżniają się **PEP8** (styl kodowania) oraz **PEP257** (docstringi).

Aby pomóc programistom w przestrzeganiu tych konwencji, stworzono narzędzia do tzw. lintowania kodu, takie jak **Pylint**, **Black**, **Flake8** czy **autoflake**.

### Narzędzia lintujące

#### Pylint
- Sprawdza zgodność z PEP8 i PEP257
- Analizuje nazewnictwo zmiennych i funkcji
- Sprawdza brak docstringów
- Podaje wskazówki dotyczące stylu i potencjalnych błędów w kodzie

  Instalacja i użycie:
  
  ```bash
  pip install pylint
  pylint <nazwa_pliku.py>
  ```
  
#### Black

- Automatycznie formatuje kod do standardu PEP8
- Proste i szybkie w użyciu, bez możliwości konfiguracji

Instalacja i użycie:

```bash
pip install black
black <nazwa_pliku.py>
```

#### Flake8

- Sprawdza zgodność z PEP8
- Wykrywa błędy semantyczne i składniowe
- Możliwość konfiguracji i korzystania z pluginów

Instalacja i użycie:

```bash
pip install flake8
flake8 <nazwa_pliku.py>
```

#### autoflake

- Automatycznie usuwa nieużywane importy i zmienne

- Pomaga w utrzymaniu czystości kodu

Instalacja i użycie:

```bash
pip install autoflake
autoflake --in-place --remove-all-unused-imports <nazwa_pliku.py>
```

### Porównanie narzędzi

| Cechy                           | Black | Pylint | Flake8  | 
|---------------------------------|-------|--------|---------|
| Automatyczna korekcja           | Tak   | Nie    | Nie     | 
| Wskazówki dotyczące stylu      | Tak   | Tak    | Częściowo |
| Wyszukiwanie błędów            | Nie   | Tak    | Częściowo |
| Ostrzeżenia o złożoności kodu  | Nie   | Tak    | Nie     |
| Dostępność pluginów            | Nie   | Nie    | Tak     | 

### Linki:

- [PEP 8 - Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)
- [PEP 257 - Docstring Conventions](https://www.python.org/dev/peps/pep-0257/)
- [Black - The uncompromising code formatter](https://github.com/psf/black)
- [Pylint - A Python source code analyzer](https://github.com/PyCQA/pylint)
- [Flake8 - A tool for checking Python code](https://github.com/PyCQA/flake8)
- [autoflake - Removes unused imports and unused variables](https://github.com/myint/autoflake)
