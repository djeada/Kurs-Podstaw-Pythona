## Praca z plikami i folderami

Praca z plikami i folderami jest nieodłączną częścią wielu aplikacji i skryptów w Pythonie. Dzięki bogatej bibliotece standardowej, Python oferuje szereg narzędzi, które umożliwiają efektywną manipulację danymi na dysku. Niezależnie od tego, czy chcesz odczytać dane z pliku tekstowego, zapisać wyniki obliczeń, czy też zautomatyzować porządkowanie folderów, Python ma narzędzia, które Ci w tym pomogą.

### Otwarcie i zamknięcie pliku

Aby rozpocząć pracę z plikami, musimy je najpierw otworzyć. W Pythonie służy do tego funkcja `open()`. Przyjmuje ona jako argumenty ścieżkę do pliku oraz tryb otwarcia, który określa, w jaki sposób chcemy z tym plikiem pracować (np. odczyt, zapis, dopisywanie).

Przykładowo:

```python
# Otwarcie pliku w trybie odczytu
plik = open("przykladowy_plik.txt", "r")
# ... tutaj możemy wykonywać operacje na pliku ...
plik.close()
```

Ważne jest, aby po zakończeniu pracy z plikiem go zamknąć, korzystając z metody `close()`. Dzięki temu upewniamy się, że wszystkie zasoby są zwolnione, a dane zapisane poprawnie.

Jednak Python oferuje wygodniejszy sposób zarządzania plikami przy użyciu konstrukcji `with`. Używając jej, nie musimy martwić się o zamykanie pliku – Python zrobi to za nas automatycznie.

```python
# Otwarcie pliku z użyciem 'with'
with open("przykladowy_plik.txt", "r") as plik:
    # ... operacje na pliku ...
```

#### Tryby otwarcia pliku

Przy otwieraniu pliku możemy określić różne tryby pracy, w zależności od naszych potrzeb. Oto najczęściej używane:

| Tryb  | Opis                                                                                          |
|-------|-----------------------------------------------------------------------------------------------|
| `'r'` | Odczyt z pliku (domyślny tryb). Plik musi istnieć.                                            |
| `'w'` | Zapis do pliku. Jeśli plik istnieje, jego zawartość zostanie nadpisana. Jeśli nie istnieje, zostanie utworzony nowy. |
| `'a'` | Dopisywanie do pliku. Dane zostaną dodane na końcu pliku. Jeśli plik nie istnieje, zostanie utworzony. |
| `'r+'`| Odczyt i zapis. Plik musi istnieć.                                                            |
| `'w+'`| Odczyt i zapis. Jeśli plik istnieje, jego zawartość zostanie nadpisana. Jeśli nie istnieje, zostanie utworzony nowy. |

#### Przykład otwarcia pliku w trybie zapisu:

```python
with open("nowy_plik.txt", "w") as plik:
    plik.write("To jest nowy plik.\n")
    plik.write("Druga linia tekstu.\n")
```

Po uruchomieniu tego kodu, w bieżącym katalogu zostanie utworzony plik `nowy_plik.txt` z następującą zawartością:

```
To jest nowy plik.
Druga linia tekstu.
```

### Odczytywanie i zapisywanie danych z/do pliku

Praca z plikami polega głównie na odczytywaniu danych oraz ich zapisywaniu. Python oferuje proste metody do tych operacji.

#### Odczytywanie danych z pliku

Aby odczytać zawartość pliku, możemy użyć metody `read()`, która zwraca cały tekst z pliku jako jeden łańcuch znaków. Alternatywnie, metoda `readlines()` zwraca listę, gdzie każdy element to kolejna linia z pliku.

```python
with open("przykladowy_plik.txt", "r") as plik:
    zawartosc = plik.read()
    print("Cała zawartość pliku:")
    print(zawartosc)
```

Jeśli plik `przykladowy_plik.txt` zawiera:

```
Pierwsza linia.
Druga linia.
Trzecia linia.
```

To wynik programu będzie:

```
Cała zawartość pliku:
Pierwsza linia.
Druga linia.
Trzecia linia.
```

Jeśli chcemy przetwarzać plik linia po linii, możemy użyć pętli:

```python
with open("przykladowy_plik.txt", "r") as plik:
    for numer, linia in enumerate(plik, start=1):
        print(f"Linia {numer}: {linia.strip()}")
```

Wynik:

```
Linia 1: Pierwsza linia.
Linia 2: Druga linia.
Linia 3: Trzecia linia.
```

#### Zapis danych do pliku

Do zapisu danych służy metoda `write()`. Możemy jej używać w trybie zapisu `'w'` lub dopisywania `'a'`.

```python
with open("przykladowy_plik.txt", "a") as plik:
    plik.write("Czwarta linia.\n")
```

Po wykonaniu powyższego kodu, do pliku `przykladowy_plik.txt` zostanie dodana nowa linia na końcu:

```
Pierwsza linia.
Druga linia.
Trzecia linia.
Czwarta linia.
```

#### Przykład: Kopiowanie zawartości jednego pliku do drugiego

```python
with open("plik_wejsciowy.txt", "r") as plik_we:
    dane = plik_we.read()

with open("plik_wyjsciowy.txt", "w") as plik_wy:
    plik_wy.write(dane)
```

Jeśli `plik_wejsciowy.txt` zawiera:

```
To jest plik wejściowy.
Zawiera ważne dane.
```

Po uruchomieniu skryptu, `plik_wyjsciowy.txt` będzie miał identyczną zawartość.

### Moduł `pathlib`

Praca z plikami i ścieżkami może być jeszcze bardziej intuicyjna dzięki modułowi `pathlib`, wprowadzonego w Pythonie 3.4. Zamiast traktować ścieżki jako zwykłe łańcuchy znaków, `pathlib` pozwala na operowanie nimi jako obiektami, co ułatwia wiele zadań.

#### Tworzenie obiektu ścieżki

```python
from pathlib import Path

sciezka_pliku = Path("przykladowy_plik.txt")
```

#### Sprawdzanie istnienia pliku lub folderu

```python
if sciezka_pliku.exists():
    print("Plik istnieje.")
else:
    print("Plik nie istnieje.")
```

Jeśli plik `przykladowy_plik.txt` istnieje, wynik będzie:

```
Plik istnieje.
```

#### Odczyt i zapis z użyciem `pathlib`

```python
# Odczyt zawartości pliku
zawartosc = sciezka_pliku.read_text()
print("Zawartość pliku:")
print(zawartosc)
```

Wynik będzie taki sam jak wcześniej przy użyciu `open()`, ale kod jest bardziej zwięzły.

```python
# Zapis tekstu do pliku
sciezka_pliku.write_text("Nowa zawartość pliku.")
```

Po tym zapisie, zawartość pliku `przykladowy_plik.txt` będzie:

```
Nowa zawartość pliku.
```

#### Praca z folderami

Możemy również łatwo operować na folderach:

```python
folder = Path("nowy_folder")

# Tworzenie folderu
folder.mkdir(parents=True, exist_ok=True)
print(f"Folder '{folder}' został utworzony.")
```

Wynik:

```
Folder 'nowy_folder' został utworzony.
```

#### Wyświetlanie zawartości folderu

Jeśli w folderze `nowy_folder` znajdują się pliki:

- `plik1.txt`
- `plik2.txt`
- `skrypt.py`

Możemy je wyświetlić:

```python
print("Zawartość folderu:")
for element in folder.iterdir():
    print(element.name)
```

Wynik:

```
Zawartość folderu:
plik1.txt
plik2.txt
skrypt.py
```

#### Sprawdzanie, czy ścieżka to plik czy folder

```python
for element in folder.iterdir():
    if element.is_file():
        print(f"{element.name} jest plikiem.")
    elif element.is_dir():
        print(f"{element.name} jest folderem.")
```

Wynik:

```
plik1.txt jest plikiem.
plik2.txt jest plikiem.
skrypt.py jest plikiem.
```

#### Wyszukiwanie plików z użyciem wzorców

Jeśli chcemy znaleźć wszystkie pliki o określonym rozszerzeniu, możemy użyć metody `glob()`:

```python
# Znajdź wszystkie pliki .txt w folderze
for plik_txt in folder.glob("*.txt"):
    print(f"Znaleziono plik tekstowy: {plik_txt.name}")
```

Wynik:

```
Znaleziono plik tekstowy: plik1.txt
Znaleziono plik tekstowy: plik2.txt
```

#### Diagram przedstawiający strukturę folderów (ASCII)

Wyobraźmy sobie, że mamy następującą strukturę folderów:

```
projekt/
├── dane/
│   ├── dane1.csv
│   └── dane2.csv
├── skrypty/
│   ├── main.py
│   └── pomocniczy.py
└── README.md
```

Możemy użyć `pathlib`, aby przeszukać całą strukturę i wykonać operacje na plikach.

#### Przykład: Rekurencyjne przeszukiwanie folderów

```python
# Przeszukanie całego drzewa katalogów w poszukiwaniu plików .py
for plik_py in Path("projekt").rglob("*.py"):
    print(f"Znaleziono skrypt Pythona: {plik_py}")
```

Wynik:

```
Znaleziono skrypt Pythona: projekt/skrypty/main.py
Znaleziono skrypt Pythona: projekt/skrypty/pomocniczy.py
```

#### Zmiana nazwy pliku lub folderu

```python
# Zmiana nazwy pliku
stara_nazwa = Path("stary_plik.txt")
nowa_nazwa = Path("nowy_plik.txt")

if stara_nazwa.exists():
    stara_nazwa.rename(nowa_nazwa)
    print(f"Plik został przemianowany na {nowa_nazwa.name}")
else:
    print("Plik do zmiany nazwy nie istnieje.")
```

Jeśli `stary_plik.txt` istnieje, wynik będzie:

```
Plik został przemianowany na nowy_plik.txt
```

#### Usuwanie pliku

```python
plik_do_usuniecia = Path("niepotrzebny_plik.txt")

if plik_do_usuniecia.exists():
    plik_do_usuniecia.unlink()
    print("Plik został usunięty.")
else:
    print("Plik nie istnieje.")
```

Jeśli plik istniał, otrzymamy:

```
Plik został usunięty.
```

### Porównanie modułów `pathlib` i `os`

| Funkcjonalność           | `pathlib`                                                    | `os`                                                           |
|--------------------------|--------------------------------------------------------------|----------------------------------------------------------------|
| Bieżący katalog roboczy  | `Path.cwd()`                                                 | `os.getcwd()`                                                  |
| Katalog domowy           | `Path.home()`                                                | `os.path.expanduser("~")`                                      |
| Sprawdzanie istnienia    | `Path('/some/path').exists()`                                | `os.path.exists('/some/path')`                                 |
| Sprawdzanie katalogu     | `Path('/some/path').is_dir()`                                | `os.path.isdir('/some/path')`                                  |
| Sprawdzanie pliku        | `Path('/some/path').is_file()`                               | `os.path.isfile('/some/path')`                                 |
| Tworzenie katalogu       | `Path('/new/dir').mkdir(parents=True, exist_ok=True)`        | `os.makedirs('/new/dir', exist_ok=True)`                       |
| Usuwanie katalogu        | `Path('/some/dir').rmdir()`                                  | `os.rmdir('/some/dir')`                                        |
| Usuwanie pliku           | `Path('/some/file').unlink()`                                | `os.remove('/some/file')`                                      |
| Zmiana nazwy             | `Path('/old/name').rename('/new/name')`                      | `os.rename('/old/name', '/new/name')`                          |
| Odczyt tekstu z pliku    | `Path('/some/file').read_text()`                             | `with open('/some/file') as f: content = f.read()`             |
| Zapis tekstu do pliku    | `Path('/some/file').write_text('New content')`               | `with open('/some/file', 'w') as f: f.write('New content')`    |
| Odczyt bajtów z pliku    | `Path('/some/file').read_bytes()`                            | `with open('/some/file', 'rb') as f: content = f.read()`       |
| Zapis bajtów do pliku    | `Path('/some/file').write_bytes(b'New content')`             | `with open('/some/file', 'wb') as f: f.write(b'New content')`  |
| Iterowanie przez katalog | `for item in Path('.').iterdir(): print(item)`               | `for item in os.listdir('.'): print(item)`                     |
| Wzorzec glob             | `for p in Path('.').glob('*.txt'): print(p)`                 | `import glob; for p in glob.glob('*.txt'): print(p)`           |
| Rekurencyjny glob        | `for p in Path('.').rglob('*.txt'): print(p)`                | `import glob; for p in glob.iglob('**/*.txt', recursive=True): print(p)` |
| Absolutna ścieżka        | `abs_path = Path('some/relative/path').resolve()`            | `abs_path = os.path.abspath('some/relative/path')`             |

Moduł `pathlib` oferuje bardziej nowoczesne, obiektowe podejście do pracy z systemem plików, podczas gdy `os` i `os.path` dostarczają bardziej tradycyjne, proceduralne metody. `pathlib` jest zazwyczaj bardziej intuicyjny i czytelny, szczególnie dla operacji na ścieżkach plików.

