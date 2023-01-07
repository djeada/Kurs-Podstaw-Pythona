
### Praca z plikami i folderami

Standardowa biblioteka Pythona zawiera wiele funkcji do pracy z plikami i folderami. Skrypty Pythona mogą być używane do automatyzacji prostych zadań biurowych.

#### Otwarcie pliku 

Do otwierania plików w Pythonie używamy funkcji open(). Funkcja ta przyjmuje ścieżkę do pliku oraz tryb otwarcia. Po użyciu funkcji open() należy pamiętać o wywołaniu funkcji close(), aby zamknąć plik. Możemy to zrobić ręcznie lub skorzystać z konstrukcji with, która automatycznie zamknie plik po jej zakończeniu.

```python
# otwarcie pliku w trybie odczytu
plik = open("sciezka/do/pliku.txt", "r")

...

plik.close()

# lub z wykorzystaniem konstrukcji with
with open("sciezka/do/pliku.txt", "r") as plik:
    ...
```

Istnieją 4 standardowe tryby otwarcia pliku:

1. <code>r</code> - odczytywanie.
1. <code>r+</code> - odczytywanie oraz modyfikacja.
1. <code>w</code> - modyfikacja wraz z usunięciem poprzedniej treści.
1. <code>a</code> - modyfikacja wraz z dopisaniem nowej treści do poprzedniej treści pliku.

#### Odczytywanie i zapisywanie danych

Aby odczytać zawartość pliku, możemy skorzystać z funkcji readlines(), która zwraca listę napisów. Każdy napis w liście reprezentuje kolejny wiersz pliku. Aby zapisać dane do pliku, używamy funkcji write. Funkcja ta przyjmuje jeden argument, napis, gdzie kolejne wiersze powinny być oddzielone znakiem *\n*.

```python
with open("sciezka/do/pliku.txt") as plik:

    # odczytaj tresc pliku
    wiersze = plik.readlines()
    for wiersz in wiersze:
        print(wiersz)

    # zapisz nowa tresc do pliku
    plik.write("nowy tekst\nwiersz nr. 2\n")
```

#### Moduł pathlib

Moduł pathlib pojawił się w Pythonie w wersji 3.4. Jest to zestaw narzędzi, które umożliwiają pracę z plikami i folderami w sposób bardziej przyjazny dla użytkownika.

Oto kilka przykładów metod z tego modułu:

* `.exists()` - zwraca True jeśli plik lub folder o podanej ścieżce istnieje, w przeciwnym wypadku zwraca False.
* `.is_file()` - zwraca True jeśli obiekt Path reprezentuje plik, w przeciwnym wypadku zwraca False.
* `.is_dir()` - zwraca True jeśli obiekt Path reprezentuje folder, w przeciwnym wypadku zwraca False.
* `.read_text()` - odczytuje zawartość pliku jako napis.
* `.write_text()` - zapisuje napis do pliku.
* `.open()` - otwiera plik w trybie określonym przez drugi argument (domyślnie 'r').

Poniższy przykład pokazuje, jak można wykorzystać te metody:

```python
from pathlib import Path

sciezka = Path("/sciezka/do/pliku.txt")

# sprawdzenie, czy plik istnieje
if sciezka.exists():
    print("Plik istnieje.")
else:
    print("Plik nie istnieje.")

# odczytanie zawartości pliku
zawartosc = sciezka.read_text()
print(zawartosc)

# zapisanie nowej zawartości do pliku
sciezka.write_text("Nowy tekst w pliku.")
```

Aby uzyskać obiekt reprezentujący folder, należy utworzyć obiekt klasy Path z odpowiednią ścieżką do folderu:

```python
folder = Path("sciezka/do/folderu")
```

Następnie możemy użyć metod tego obiektu, takich jak iterdir() do iterowania po plikach i folderach w danym folderze:

```python
for element in folder.iterdir():
    print(element)
```

Możemy również sprawdzić, czy obiekt jest plikiem czy folderem za pomocą metod is_file() i is_dir():

```python
if element.is_file():
    print("To jest plik")
elif element.is_dir():
    print("To jest folder")
```

Inne przydatne metody to exists(), która sprawdza, czy dany element istnieje, oraz mkdir(), która tworzy nowy folder.

```python
if not folder.exists():
    folder.mkdir()
```
