
## Moduły i pakiety w Pythonie

W Pythonie, moduły i pakiety umożliwiają organizację i strukturyzację kodu. Ułatwiają zarządzanie dużymi projektami oraz współpracę z innymi programistami.

### Moduły

Moduł to pojedynczy plik Pythona, który zawiera zestaw funkcji, klas i zmiennych. Moduł może być zaimportowany do innego modułu lub skryptu za pomocą instrukcji `import`. [Dokumentacja Pythona](https://docs.python.org/3/library/index.html) zawiera pełną listę wbudowanych modułów w bibliotece standardowej.

Przykład importu modułu `requests`:

```python
import requests
print(type(requests))  # <class 'module'>
```

### Pakiety

Pakiet to kolekcja powiązanych modułów zgrupowanych w jednym katalogu. Katalog ten musi zawierać plik __init__.py (może być pusty), który informuje Pythona, że dany katalog powinien być traktowany jako pakiet.

Struktura katalogu dla pakietu:

```
.
├── nazwa_paczki
│   ├── __init__.py
│   ├── przykladowy_skrypt_a.py
│   ├── przykladowy_skrypt_b.py
│   └── przykladowy_skrypt_c.py
└── main.py
```

### Importowanie modułów i pakietów

Moduły i funkcje z nich można importować na różne sposoby:

- Zaimportowanie całego modułu:

```python
import nazwa_modulu
```

- Zaimportowanie modułu z aliasem:

```python
import nazwa_modulu as alias
```

- Zaimportowanie konkretnych funkcji z modułu:

```python
from nazwa_modulu import fun_1, fun_2
```

- Zaimportowanie funkcji z aliasem:

```python
from nazwa_modulu import fun_1 as f1, fun_2 as f2
```

- Zaimportowanie całej zawartości modułu:

```python
from nazwa_paczki.przykladowy_skrypt_a import *
```

Korzystaj ostrożnie z instrukcji `from modul import *`. Importuje ona wszystkie funkcje i zmienne z modułu, co może prowadzić do niechcianych konfliktów nazw.

### Wykonywanie kodu podczas importowania

Kod, który nie jest częścią definicji funkcji czy klasy, zostaje wykonany podczas importowania modułu. 

Przykład:

```python
def fun_a():
    ...

def fun_b():
    ...

wyslij_rakiety()
```

Jeśli ten moduł zostanie zaimportowany w innym skrypcie, to funkcja `wyslij_rakiety()` zostanie wywołana podczas importowania modułu.
Aby zapobiec niechcianemu wywoływaniu kodu podczas importowania, używa się konstrukcji:

```python
def fun_a():
    ...

def fun_b():
        ...

if __name__ == "__main__":
    wyslij_rakiety()
```
