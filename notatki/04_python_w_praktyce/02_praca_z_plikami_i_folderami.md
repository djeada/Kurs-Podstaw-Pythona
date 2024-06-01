## Praca z plikami i folderami

Biblioteka standardowa Pythona oferuje szereg funkcji i narzędzi do efektywnej pracy z plikami i folderami. Dzięki tym narzędziom, skrypty Pythona mogą być używane do automatyzacji różnych zadań, od prostych czynności biurowych po bardziej zaawansowane operacje na danych.

### Otwarcie i zamknięcie pliku 

Aby otworzyć plik w Pythonie, używamy funkcji `open()`. Główne argumenty tej funkcji to ścieżka do pliku oraz tryb otwarcia. Ważne jest, aby po pracy z plikiem odpowiednio go zamknąć, co można zrealizować za pomocą metody `close()`. Zalecane jest korzystanie z konstrukcji `with`, która automatycznie dba o poprawne zamknięcie pliku.

```python
# Otwarcie pliku w trybie odczytu
plik = open("sciezka/do/pliku.txt", "r")
# ... operacje na pliku ...
plik.close()

# Alternatywna metoda z użyciem `with`
with open("sciezka/do/pliku.txt", "r") as plik:
    # ... operacje na pliku ...
```

Do dyspozycji mamy różne tryby otwarcia pliku:

- `r` - odczyt pliku.
- `r+` - odczyt i modyfikacja pliku.
- `w` - zapis do pliku (usunięcie istniejącej treści i zapis nowej).
- `a` - dopisanie do pliku (bez usuwania istniejącej treści).

### Odczytywanie i zapisywanie danych z/do pliku

Odczytanie całego pliku można zrealizować za pomocą metody readlines(), która zwróci listę linii z pliku. Każdy element tej listy to napis reprezentujący kolejny wiersz. Zapis danych do pliku odbywa się przy użyciu metody write().

```python
with open("sciezka/do/pliku.txt", "r") as plik:
    # Odczytanie zawartości pliku
    wiersze = plik.readlines()
    for wiersz in wiersze:
        print(wiersz.strip())  # `strip()` usuwa znaki końca linii

# Zapis nowych danych do pliku
with open("sciezka/do/pliku.txt", "w") as plik:
    plik.write("nowy tekst\nwiersz nr. 2\n")
```

Pamiętajmy, aby wybierać odpowiedni tryb otwarcia pliku zależnie od planowanych operacji!

### Moduł `pathlib`

Współczesna praca z plikami i folderami w Pythonie stała się znacznie bardziej intuicyjna i wydajna dzięki wprowadzeniu modułu `pathlib` w wersji 3.4. Zamiast manipulowania ścieżkami jako zwykłymi łańcuchami znaków, `pathlib` pozwala na reprezentowanie ścieżek jako obiektów z wieloma użytecznymi metodami.

Oto kilka podstawowych metod dostępnych w klasie `Path`:

* `.exists()` - sprawdza, czy dana ścieżka istnieje.
* `.is_file()` - sprawdza, czy ścieżka wskazuje na plik.
* `.is_dir()` - sprawdza, czy ścieżka wskazuje na folder.
* `.read_text()` - odczytuje zawartość pliku jako tekst.
* `.write_text()` - zapisuje tekst do pliku.
* `.open()` - otwiera plik w określonym trybie (domyślnie w trybie odczytu 'r').

Poniżej przedstawiam, jak używać wymienionych metod:

```python
from pathlib import Path

sciezka = Path("/sciezka/do/pliku.txt")

if sciezka.exists():
    print("Plik istnieje.")
else:
    print("Plik nie istnieje.")

zawartosc = sciezka.read_text()
print(zawartosc)

sciezka.write_text("Nowy tekst w pliku.")
```

Reprezentowanie folderu jest równie proste:

```python
folder = Path("/sciezka/do/folderu")

for element in folder.iterdir():
    print(element)
```

Dzięki obiektowemu podejściu pathlib, możemy łatwo sprawdzić, czy dany obiekt to plik czy folder:

```python
if element.is_file():
    print("To jest plik.")
elif element.is_dir():
    print("To jest folder.")
```

`pathlib` oferuje również wiele innych przydatnych metod, takich jak:

- `.mkdir()` - tworzy nowy folder.
- `.rename()` - zmienia nazwę pliku lub folderu.
- `.glob()` - wyszukuje pliki i foldery według podanego wzorca.

Przykład użycia `.mkdir()` i sprawdzenia istnienia folderu:

```python
if not folder.exists():
    folder.mkdir(parents=True, exist_ok=True)
```

Parametr `parents=True` sprawia, że zostaną utworzone wszystkie nieistniejące foldery nadrzędne, a `exist_ok=True` zapobiega błędom, jeśli folder już istnieje.

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

