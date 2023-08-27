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

### Moduł `pathlib` w Pythonie

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
