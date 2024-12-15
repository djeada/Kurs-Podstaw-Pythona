## Informacje o systemie operacyjnym

Praca z systemem operacyjnym jest nieodłączną częścią tworzenia aplikacji i skryptów w Pythonie. Moduł `os` z biblioteki standardowej dostarcza bogaty zestaw funkcji, które pozwalają na interakcję z systemem operacyjnym w sposób przenośny i niezależny od platformy. Dzięki temu możemy uzyskiwać informacje o bieżącym środowisku, manipulować plikami i katalogami, a nawet uruchamiać procesy.

### Ustalanie rodzaju systemu operacyjnego

Czasami potrzebujemy dostosować działanie naszego programu w zależności od systemu operacyjnego, na którym jest uruchamiany. Aby poznać podstawową nazwę systemu, możemy skorzystać z atrybutu `os.name`:

```python
import os

print(os.name)
```

Jeśli uruchomimy ten kod, otrzymamy jedno z następujących wyjść, w zależności od systemu:

- **'posix'** na systemach Unix/Linux,
- **'nt'** na Windows,
- **'java'** na platformie Java.

Otrzymana wartość daje ogólne pojęcie o rodzaju systemu, ale często potrzebujemy bardziej szczegółowych informacji. W tym celu możemy użyć modułu `platform`:

```python
import platform

print(platform.system())    # Nazwa systemu operacyjnego
print(platform.release())   # Wersja systemu
print(platform.version())   # Szczegółowa wersja systemu
print(platform.machine())   # Architektura sprzętowa
```

Przykładowe wyniki mogą wyglądać następująco:

**Linux**:

- `platform.system()` zwróci `'Linux'`,
- `platform.release()` może zwrócić `'5.4.0-42-generic'`,
- `platform.machine()` zwróci `'x86_64'`.

**Windows**:

- `platform.system()` zwróci `'Windows'`,
- `platform.release()` może zwrócić `'10'`,
- `platform.machine()` zwróci `'AMD64'`.

Dzięki tym informacjom możemy precyzyjnie dostosować działanie naszego programu do środowiska użytkownika.

### Manipulacja systemem plików

Operacje na plikach i katalogach są kluczowe w wielu aplikacjach. Moduł `os` oferuje funkcje, które umożliwiają zarządzanie systemem plików w sposób przenośny między różnymi systemami operacyjnymi.

#### Listowanie zawartości katalogu

Aby wyświetlić listę plików i folderów w określonym katalogu, używamy funkcji `os.listdir()`:

```python
import os

zawartosc = os.listdir('.')
print("Zawartość bieżącego katalogu:")
for element in zawartosc:
    print(element)
```

Jeśli w bieżącym katalogu znajdują się pliki `dokument.txt`, `skrypt.py` oraz folder `dane`, wynik będzie:

```
Zawartość bieżącego katalogu:
dokument.txt
skrypt.py
dane
```

#### Tworzenie nowego katalogu

Do utworzenia nowego katalogu służy funkcja `os.mkdir()`:

```python
import os

os.mkdir('nowy_folder')
print("Utworzono katalog 'nowy_folder'.")
```

Po uruchomieniu tego kodu w bieżącym katalogu pojawi się nowy folder o nazwie `nowy_folder`.

#### Usuwanie pliku lub katalogu

Aby usunąć plik, korzystamy z funkcji `os.remove()`:

```python
import os

os.remove('dokument.txt')
print("Usunięto plik 'dokument.txt'.")
```

Jeśli chcemy usunąć pusty katalog, używamy `os.rmdir()`:

```python
import os

os.rmdir('nowy_folder')
print("Usunięto katalog 'nowy_folder'.")
```

Uwaga: `os.rmdir()` usuwa tylko puste katalogi. Jeśli katalog zawiera pliki lub podkatalogi, musimy użyć modułu `shutil` i funkcji `shutil.rmtree()`.

#### Łączenie ścieżek w sposób przenośny

Przy łączeniu fragmentów ścieżek warto użyć funkcji `os.path.join()`, która automatycznie uwzględnia separator odpowiedni dla danego systemu operacyjnego:

```python
import os

sciezka = os.path.join('katalog', 'podkatalog', 'plik.txt')
print(f"Ścieżka do pliku: {sciezka}")
```

Na systemie Windows wynik będzie wyglądał jak `katalog\podkatalog\plik.txt`, a na Unix/Linux `katalog/podkatalog/plik.txt`.

#### Sprawdzanie istnienia pliku lub katalogu

Możemy sprawdzić, czy dana ścieżka istnieje oraz czy jest plikiem lub katalogiem:

```python
import os

sciezka = 'dane'

if os.path.exists(sciezka):
    if os.path.isfile(sciezka):
        print(f"'{sciezka}' jest plikiem.")
    elif os.path.isdir(sciezka):
        print(f"'{sciezka}' jest katalogiem.")
else:
    print(f"'{sciezka}' nie istnieje.")
```

Jeśli `dane` jest katalogiem, otrzymamy:

```
'dane' jest katalogiem.
```

### Informacje o użytkownikach

W systemach Unix/Linux możemy uzyskać informacje o użytkownikach i grupach za pomocą modułu `pwd`. Jest to szczególnie przydatne, gdy chcemy dostosować działanie programu do konkretnego użytkownika.

#### Pobieranie informacji o bieżącym użytkowniku

```python
import os
import pwd

user_info = pwd.getpwuid(os.getuid())

print(f"Nazwa użytkownika: {user_info.pw_name}")
print(f"ID użytkownika: {user_info.pw_uid}")
print(f"ID grupy: {user_info.pw_gid}")
print(f"Katalog domowy: {user_info.pw_dir}")
```

Przykładowe wyjście:

```
Nazwa użytkownika: jan
ID użytkownika: 1000
ID grupy: 1000
Katalog domowy: /home/jan
```

#### Pobieranie informacji o grupie użytkownika

Aby uzyskać informacje o grupie, możemy użyć modułu `grp`:

```python
import grp

group_info = grp.getgrgid(user_info.pw_gid)

print(f"Nazwa grupy: {group_info.gr_name}")
print(f"ID grupy: {group_info.gr_gid}")
print(f"Członkowie grupy: {', '.join(group_info.gr_mem)}")
```

Jeśli grupa `jan` ma dodatkowych członków, zostaną oni wymienieni w wyniku.

### Informacje o dyskach

Monitorowanie dostępnego miejsca na dysku jest istotne w aplikacjach, które przechowują lub przetwarzają duże ilości danych. Możemy uzyskać te informacje za pomocą funkcji `os.statvfs()`.

#### Sprawdzanie pojemności i wolnego miejsca na dysku

```python
import os

statvfs = os.statvfs('/')

# Rozmiar bloku systemu plików
rozmiar_bloku = statvfs.f_frsize

# Całkowita liczba bloków
liczba_blokow = statvfs.f_blocks

# Liczba wolnych bloków
wolne_bloki = statvfs.f_bavail

# Obliczenia
calkowita_pojemnosc = rozmiar_bloku * liczba_blokow
wolne_miejsce = rozmiar_bloku * wolne_bloki

print(f"Całkowita pojemność dysku: {calkowita_pojemnosc / (1024**3):.2f} GB")
print(f"Wolne miejsce na dysku: {wolne_miejsce / (1024**3):.2f} GB")
```

Jeśli dysk ma 500 GB, a wolne jest 200 GB, wynik będzie:

```
Całkowita pojemność dysku: 500.00 GB
Wolne miejsce na dysku: 200.00 GB
```

### Informacje o procesorze

Poznanie parametrów procesora może być przydatne przy optymalizacji wydajności aplikacji.

#### Liczba rdzeni procesora

Moduł `os` udostępnia funkcję `cpu_count()`:

```python
import os

liczba_rdzeni = os.cpu_count()
print(f"Liczba rdzeni procesora: {liczba_rdzeni}")
```

Przykładowy wynik:

```
Liczba rdzeni procesora: 8
```

#### Szczegółowe informacje o częstotliwości procesora

Aby uzyskać informacje o częstotliwości procesora, możemy skorzystać z modułu `psutil`. Pamiętajmy jednak, że wymaga on instalacji (`pip install psutil`).

```python
import psutil

cpu_freq = psutil.cpu_freq()

print(f"Bieżąca częstotliwość procesora: {cpu_freq.current:.2f} MHz")
print(f"Maksymalna częstotliwość procesora: {cpu_freq.max:.2f} MHz")
```

Jeśli procesor działa z częstotliwością 2.20 GHz, a maksymalna częstotliwość to 3.50 GHz, wynik będzie:

```
Bieżąca częstotliwość procesora: 2200.00 MHz
Maksymalna częstotliwość procesora: 3500.00 MHz
```

### Zmienne środowiskowe

Zmienne środowiskowe są używane do przechowywania informacji konfiguracyjnych systemu operacyjnego i aplikacji.

#### Odczytywanie zmiennych środowiskowych

Możemy uzyskać dostęp do zmiennych środowiskowych za pomocą `os.environ`, które działa jak słownik:

```python
import os

shell = os.environ.get('SHELL')
print(f"Używana powłoka: {shell}")
```

Jeśli używamy powłoki Bash na systemie Unix/Linux, wynik będzie:

```
Używana powłoka: /bin/bash
```

#### Ustawianie zmiennych środowiskowych

Możemy ustawić nową zmienną środowiskową w bieżącym procesie:

```python
import os

os.environ['MOJA_ZMIENNA'] = 'wartość'
print(f"MOJA_ZMIENNA: {os.environ.get('MOJA_ZMIENNA')}")
```

Wynik:

```
MOJA_ZMIENNA: wartość
```

Warto pamiętać, że zmiany wprowadzone w `os.environ` są widoczne tylko w bieżącym procesie i nie są zachowywane po zakończeniu programu.

#### Użycie zmiennych środowiskowych w aplikacji

Zmienne środowiskowe są często wykorzystywane do przechowywania danych konfiguracyjnych, takich jak klucze API czy dane dostępowe do bazy danych.

```python
import os

api_key = os.environ.get('API_KEY')
if api_key:
    print("Klucz API został pobrany.")
else:
    print("Brak klucza API. Ustaw zmienną środowiskową 'API_KEY'.")
```

Jeśli zmienna `API_KEY` nie jest ustawiona, program poinformuje nas o tym, co ułatwia zarządzanie konfiguracją.
