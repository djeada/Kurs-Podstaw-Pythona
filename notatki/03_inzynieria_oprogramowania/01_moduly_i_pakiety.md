
## Moduły i pakiety w Pythonie

W Pythonie, moduły i pakiety umożliwiają organizację i strukturyzację kodu. Ułatwiają zarządzanie dużymi projektami oraz współpracę z innymi programistami. Zrozumienie tych elementów jest kluczowe dla efektywnego programowania i utrzymania czystego kodu.

### Moduły

Moduł to pojedynczy plik Pythona, który zawiera zestaw funkcji, klas i zmiennych. Moduł może być zaimportowany do innego modułu lub skryptu za pomocą instrukcji `import`. Importowanie modułów pomaga w uniknięciu duplikacji kodu oraz ułatwia jego utrzymanie. [Dokumentacja Pythona](https://docs.python.org/3/library/index.html) zawiera pełną listę wbudowanych modułów w bibliotece standardowej.

```python
import requests
print(type(requests))  # <class 'module'>
```

### Pakiety

Pakiet to kolekcja powiązanych modułów zgrupowanych w jednym katalogu. Katalog ten musi zawierać plik `__init__.py` (może być pusty), który informuje Pythona, że dany katalog powinien być traktowany jako pakiet. Pakiety umożliwiają organizację kodu na wyższym poziomie i mogą zawierać podpakiety, co umożliwia tworzenie bardziej złożonych struktur.

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

W Pythonie importowanie modułów i funkcji z nich jest fundamentalne dla efektywnego zarządzania przestrzenią nazw i unikania duplikacji kodu. Oto różne metody importowania:

- **Zaimportowanie całego modułu:**
    Pozwala to na dostęp do wszystkich funkcji, klas i zmiennych w module, używając kropki (.) jako separatora.
    ```python
    import nazwa_modulu
    print(nazwa_modulu.nazwa_funkcji())
    ```

- **Zaimportowanie modułu z aliasem:**
    Umożliwia korzystanie z krótszej, bardziej praktycznej nazwy modułu w kodzie.
    ```python
    import nazwa_modulu as alias
    print(alias.nazwa_funkcji())
    ```

- **Zaimportowanie konkretnych funkcji z modułu:**
    Importuje tylko określone funkcje lub klasy, co może przyczynić się do mniejszego zużycia pamięci, gdy nie potrzebujemy całego modułu.
    ```python
    from nazwa_modulu import fun_1, fun_2
    fun_1()
    ```

- **Zaimportowanie funkcji z aliasem:**
    Pozwala na zmianę nazwy importowanej funkcji, co jest szczególnie przydatne w przypadku konfliktów nazw lub długich nazw funkcji.
    ```python
    from nazwa_modulu import fun_1 as f1, fun_2 as f2
    f1()
    ```

- **Zaimportowanie całej zawartości modułu:**
    Chociaż ta metoda jest wygodna, powinna być stosowana z rozwagą, ponieważ może prowadzić do konfliktów nazw, jeśli dwa moduły mają funkcje o tych samych nazwach.
    ```python
    from nazwa_paczki.przykladowy_skrypt_a import *
    ```

Korzystaj ostrożnie z instrukcji `from modul import *`. Importuje ona wszystkie funkcje i zmienne z modułu, co może prowadzić do niechcianych konfliktów nazw.


### Wykonywanie kodu podczas importowania

W Pythonie, kod znajdujący się poza definicjami funkcji czy klasami w module jest wykonywany od razu przy jego importowaniu. To zachowanie jest często niezrozumiałe dla początkujących programistów i może prowadzić do nieoczekiwanych efektów, zwłaszcza gdy moduł zawiera skryptowe wywołania funkcji.

#### Przykład problematycznego zachowania:

Załóżmy, że mamy moduł z funkcjami do zarządzania misjami kosmicznymi, który również od razu wysyła rakietę. Taki moduł, po zaimportowaniu, automatycznie wykona funkcję `wyslij_rakiety()`:

```python
def fun_a():
    print("Przygotowanie misji")

def fun_b():
    print("Analiza trajektorii")

wyslij_rakiety()  # Ta funkcja zostanie wywołana podczas importowania
```

Jeśli ten moduł zostanie zaimportowany w innym skrypcie, funkcja `wyslij_rakiety()` zostanie niechcący wywołana, co może być niepożądane.

#### Rozwiązanie problemu:

Aby uniknąć takich sytuacji, Python oferuje specjalną konstrukcję `if __name__ == "__main__":`, która sprawdza, czy moduł jest uruchamiany jako program główny, a nie importowany jako moduł. Kod umieszczony wewnątrz tego bloku nie zostanie wykonany przy imporcie, lecz tylko przy bezpośrednim uruchomieniu pliku jako skryptu:

```python
def fun_a():
    print("Przygotowanie misji")

def fun_b():
    print("Analiza trajektorii")

def wyslij_rakiety():
    print("Wysyłanie rakiet!")

if __name__ == "__main__":
    wyslij_rakiety()  # Funkcja zostanie wywołana tylko gdy uruchomimy moduł bezpośrednio
```
