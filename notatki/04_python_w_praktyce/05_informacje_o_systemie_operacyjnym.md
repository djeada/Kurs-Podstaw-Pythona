## Informacje o systemie operacyjnym

Moduł `os` w bibliotece standardowej Pythona dostarcza zestaw funkcji umożliwiających interakcję z systemem operacyjnym. Dzięki temu możemy uzyskiwać informacje o bieżącym środowisku oraz manipulować strukturą katalogów i plikami.

### Ustalanie rodzaju systemu operacyjnego

Aby poznać podstawową nazwę systemu operacyjnego, na którym działa nasz kod, można użyć zmiennej `os.name`:

```python
import os
print(os.name)
```

Wartość `os.name` może przyjmować takie wartości jak 'posix', 'nt', 'java' itd., w zależności od używanego systemu.

Jednakże, jeśli chcemy uzyskać bardziej szczegółowe informacje, takie jak dystrybucja, wersja systemu itp., lepszym wyborem jest moduł platform:

```python
import platform

print(platform.system())    # np. 'Linux', 'Windows' lub 'Darwin' (dla MacOS)
print(platform.release())   # wersja systemu
print(platform.version())   # szczegółowa wersja systemu
print(platform.machine())   # architektura sprzętowa
```

### Manipulacja systemem plików

Moduł os oferuje również funkcje do pracy z systemem plików:

- `os.listdir(path='.')` - listuje pliki i foldery w podanym katalogu.
- `os.mkdir(path)` - tworzy nowy katalog.
- `os.rmdir(path)` - usuwa katalog (jeśli jest pusty).
- `os.remove(path)` - usuwa plik.
- `os.path.join(path1, path2, ...)` - łączy ścieżki w sposób zgodny z używanym systemem operacyjnym.
- `os.path.exists(path)` - sprawdza, czy dana ścieżka istnieje.
- `os.path.isfile(path)` - sprawdza, czy podana ścieżka jest plikiem.
- `os.path.isdir(path)` - sprawdza, czy podana ścieżka jest katalogiem.

Dzięki tym funkcjom można łatwo manipulować strukturą katalogów i plikami w systemie operacyjnym.

### Informacje o użytkownikach

Aby uzyskać informacje o użytkownikach systemu oraz grupach, możemy skorzystać z modułu `pwd` (uwaga: moduł ten dostępny jest tylko na systemach Unix). 

```python
import os
import pwd

# Pobierz informacje o bieżącym użytkowniku
user_info = pwd.getpwuid(os.getuid())
print(f"Nazwa użytkownika: {user_info.pw_name}")
print(f"ID użytkownika: {user_info.pw_uid}")
print(f"ID grupy: {user_info.pw_gid}")
print(f"Katalog domowy: {user_info.pw_dir}")

# Pobierz informacje o głównej grupie użytkownika
group_info = pwd.getgrgid(user_info.pw_gid)
print(f"Nazwa grupy: {group_info.gr_name}")
print(f"ID grupy: {group_info.gr_gid}")
print(f"Lista użytkowników w grupie: {', '.join(group_info.gr_mem)}")
```

### Informacje o dyskach

Aby uzyskać informacje o dostępnych dyskach oraz wolnym miejscu na nich, możemy skorzystać z modułu os i jego metody statvfs:

```python
import os

# Pobierz informacje o głównym dysku
disk_info = os.statvfs("/")
print(f"Całkowita pojemność dysku: {disk_info.f_frsize * disk_info.f_blocks:,} bajtów")
print(f"Wolne miejsce na dysku: {disk_info.f_frsize * disk_info.f_bfree:,} bajtów")
```

### Informacje o procesorze

Moduł `os` z biblioteki standardowej Pythona zawiera funkcję `cpu_count()`, która zwraca liczbę rdzeni procesora. Aby uzyskać bardziej szczegółowe informacje o mocy obliczeniowej procesora, możemy skorzystać z modułu `psutil`. Poniższy kod przedstawia, jak wyświetlić liczbę rdzeni oraz maksymalną częstotliwość procesora:

```python
import os
import psutil

# Liczba rdzeni procesora
print(f"Liczba rdzeni procesora: {os.cpu_count()}")

# Częstotliwość procesora
cpu_freq = psutil.cpu_freq()
print(f"Maksymalna częstotliwość procesora: {cpu_freq.max} MHz")
```

Warto zaznaczyć, że moduł `psutil` nie jest częścią biblioteki standardowej Pythona i może wymagać dodatkowej instalacji (np. za pomocą `pip install psutil`).

### Zmienne środowiskowe

Moduł `os` pozwala na dostęp do zmiennych środowiskowych przez atrybut `environ`. Jest to słownik, w którym kluczem jest nazwa zmiennej środowiskowej, a wartością jej treść. Aby odczytać wartość konkretnej zmiennej środowiskowej, można skorzystać z notacji słownikowej. Poniżej przedstawiono sposób odczytania wartości zmiennej środowiskowej `SHELL`:

```python
import os

# Odczyt wartości zmiennej środowiskowej SHELL
print(f"Zmienna środowiskowa SHELL: {os.environ.get('SHELL')}")
```

Uwaga: Metoda get pozwala na bezpieczne odczytanie wartości klucza ze słownika, nawet jeśli klucz nie istnieje. Dzięki temu unikamy błędów w przypadku braku klucza.

Aby modyfikować zmienne środowiskowe, można używać `os.environ` jak zwykłego słownika Pythona. Poniżej przedstawiono sposób ustawienia wartości zmiennej środowiskowej VAR:

```python
import os

os.environ['VAR'] = 'value'
```

Warto jednak pamiętać, że zmiany dokonane w `os.environ` wpływają tylko na zmienne środowiskowe w obrębie bieżącego procesu. Po zakończeniu działania skryptu, zmiany nie są przechowywane dla innych procesów ani sesji. Aby zachować zmiany zmiennych środowiskowych na stałe, trzeba je zapisać w odpowiednich plikach konfiguracyjnych systemu. W przypadku systemów Linux, mogą to być pliki jak `/etc/environment` czy skrypty startowe powłoki, np. `~/.bashrc` czy `/etc/bash.bashrc`.
