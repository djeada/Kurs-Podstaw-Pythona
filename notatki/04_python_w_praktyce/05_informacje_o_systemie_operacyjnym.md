## Informacje o systemie operacyjnym

Praca z systemem operacyjnym jest nieodłączną częścią tworzenia aplikacji i skryptów w Pythonie. Moduł `os` z biblioteki standardowej dostarcza bogaty zestaw funkcji, które pozwalają na interakcję z systemem operacyjnym w sposób przenośny i niezależny od platformy. Dzięki temu możemy uzyskiwać informacje o bieżącym środowisku, manipulować plikami i katalogami, a nawet uruchamiać procesy.

**Dzięki funkcjom modułu `os` możemy tworzyć kod, który będzie działać podobnie na różnych systemach operacyjnych, takich jak Linux, Windows czy macOS.** To duże udogodnienie, ponieważ nie musimy dostosowywać poleceń do określonej platformy. Wystarczy, że skorzystamy z uniwersalnych metod `os`, a Python „pod spodem” wykona odpowiednie czynności w zależności od środowiska.

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

Dzięki tym informacjom możemy precyzyjnie dostosować działanie naszego programu do środowiska użytkownika. Na przykład, jeśli stwierdzimy, że pracujemy na Windowsie, możemy użyć innych ścieżek do plików niż na Linuxie, czy też wykonać określone polecenia shellowe.

### Manipulacja systemem plików

Operacje na plikach i katalogach są kluczowe w wielu aplikacjach. Moduł `os` oferuje funkcje, które umożliwiają zarządzanie systemem plików w sposób przenośny między różnymi systemami operacyjnymi.

**Jest to bardzo ważne w kontekście kompatybilności projektów – używając metod `os`, nie musimy martwić się o różnice w separatorach ścieżek pomiędzy Windows a Unix/Linux (które używają innych znaków w ścieżkach).** W efekcie piszemy kod bardziej uniwersalny i mniej podatny na błędy zależne od platformy.

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
W ten sposób szybko i prosto możemy zobaczyć, co znajduje się w danej lokalizacji. Metoda `listdir()` nie rozróżnia jednak plików od katalogów – zwraca wszystkie nazwy obiektów znajdujących się w katalogu.


#### Tworzenie nowego katalogu

Do utworzenia nowego katalogu służy funkcja `os.mkdir()`:

```python
import os

os.mkdir('nowy_folder')
print("Utworzono katalog 'nowy_folder'.")
```

Po uruchomieniu tego kodu w bieżącym katalogu pojawi się nowy folder o nazwie `nowy_folder`.

**Dzięki takim operacjom mamy pełną kontrolę nad strukturą naszych plików i katalogów – możemy dynamicznie tworzyć foldery, w których będziemy zapisywać dane, logi czy raporty.** Pamiętajmy, że jeśli folder już istnieje, wywołanie `os.mkdir()` spowoduje błąd. Aby uniknąć tego, możemy najpierw sprawdzić, czy folder już nie istnieje, używając `os.path.exists()`.

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

**Podobnie jak przy tworzeniu katalogów, operacje usuwania należy wykonywać ostrożnie.** Przed wywołaniem `os.remove()` czy `shutil.rmtree()` upewnijmy się, że faktycznie chcemy usunąć wskazane elementy, bo cofnięcie takiej operacji może być trudne lub niemożliwe (zwłaszcza gdy dane nie są nigdzie zbackupowane).

#### Łączenie ścieżek w sposób przenośny

Przy łączeniu fragmentów ścieżek warto użyć funkcji `os.path.join()`, która automatycznie uwzględnia separator odpowiedni dla danego systemu operacyjnego:

```python
import os

sciezka = os.path.join('katalog', 'podkatalog', 'plik.txt')
print(f"Ścieżka do pliku: {sciezka}")
```
Na systemie Windows wynik będzie wyglądał jak `katalog\podkatalog\plik.txt`, a na Unix/Linux `katalog/podkatalog/plik.txt`.

**To rozwiązanie jest absolutnie kluczowe dla transportowalności kodu, ponieważ w przeciwnym wypadku musielibyśmy tworzyć warunkową logikę do obsługi różnych rodzajów separatorów.** Warto od samego początku przyzwyczaić się do używania `os.path.join()`, zwłaszcza w wieloosobowych projektach, aby uniknąć problemów z kompatybilnością.


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

**Warto rozróżniać te funkcje, gdyż pozwalają nam bezpiecznie wykonywać kolejne kroki na ścieżkach, np. najpierw sprawdzić, czy plik istnieje, zanim spróbujemy go otworzyć.** Dzięki temu unikamy nieoczekiwanych błędów lub wyjątków w czasie działania programu.

### Informacje o użytkownikach

W systemach Unix/Linux możemy uzyskać informacje o użytkownikach i grupach za pomocą modułu `pwd`. Jest to szczególnie przydatne, gdy chcemy dostosować działanie programu do konkretnego użytkownika.

**Typowym przykładem użycia jest sytuacja, w której skrypt powinien zapisywać dane wyłącznie w katalogu domowym bieżącego użytkownika, a my chcemy pobrać nazwę tego użytkownika czy lokalizację jego katalogu `home`.** Moduł `pwd` uprości nam te zadania.

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
**Dzięki takiej wiedzy skrypt może np. automatycznie zapisywać raporty w `/home/jan/raporty` albo sprawdzić, czy dany użytkownik ma uprawnienia do uruchomienia pewnych funkcji w systemie.**


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

**Taka kontrola nad użytkownikami i grupami pozwala np. na pisanie skryptów administracyjnych, które wykonują różne akcje zależnie od uprawnień danej osoby.** Zazwyczaj tego typu operacje są bardziej zaawansowane i wymagają uruchamiania skryptu z odpowiednimi prawami (np. jako administrator), dlatego trzeba pamiętać o kwestiach bezpieczeństwa.

### Informacje o dyskach

Monitorowanie dostępnego miejsca na dysku jest istotne w aplikacjach, które przechowują lub przetwarzają duże ilości danych. Możemy uzyskać te informacje za pomocą funkcji `os.statvfs()`.

**Dzięki temu unikniemy sytuacji, w której skrypt zaczyna zapisywać pliki na dysku i nagle napotyka brak miejsca, co może prowadzić do utraty danych lub nieoczekiwanych błędów.** Możemy na przykład zaplanować działania prewencyjne, jeśli wolnego miejsca jest mniej niż określony próg.

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
**Tego rodzaju informacja pozwala nam elastycznie zarządzać danymi i reagować, gdy zasoby systemowe zaczynają się kończyć.** Zanim zostanie w pełni zapełniony, aplikacja może np. automatycznie przenieść nieużywane pliki w inne miejsce lub powiadomić administratora o potrzebie powiększenia przestrzeni.


### Informacje o procesorze

Poznanie parametrów procesora może być przydatne przy optymalizacji wydajności aplikacji. Niektóre zadania da się rozproszyć na wiele rdzeni, co pozwala znacznie przyspieszyć obliczenia.

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

**Dzięki temu możemy na przykład dostosować liczbę wątków lub procesów, które nasz program będzie używał, by optymalnie wykorzystać dostępną moc obliczeniową.** W środowisku DevOps i przy przetwarzaniu równoległym ta wiedza jest szczególnie cenna.

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
**Takie dane bywają wykorzystywane np. w menedżerach zadań, narzędziach monitorujących czy w aplikacjach optymalizujących działanie systemu, które mogą np. zmniejszać obciążenie procesora przy braku potrzeby pracy na najwyższych częstotliwościach.**


### Zmienne środowiskowe

Zmienne środowiskowe są używane do przechowywania informacji konfiguracyjnych systemu operacyjnego i aplikacji. Mogą to być m.in. ścieżki do różnych katalogów systemowych, klucze dostępu do serwisów zewnętrznych lub adresy serwerów baz danych.

**Dzięki możliwości definiowania zmiennych środowiskowych możemy łatwo parametryzować nasz program, bez konieczności zmiany kodu źródłowego.** Jest to szczególnie wygodne w środowiskach ciągłej integracji i konteneryzacji (np. Docker), gdzie w zależności od potrzeb podajemy różne wartości zmiennych środowiskowych.


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

**Odczytując zmienne środowiskowe, możemy w prosty sposób dopasować działanie programu do środowiska, w którym aktualnie działa.** Przykładowo w systemach Windows może nie istnieć zmienna `SHELL`, więc `os.environ.get('SHELL')` zwróci wartość `None`.

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

**Innymi słowy, jeśli po uruchomieniu skryptu wpiszemy w terminalu `echo $MOJA_ZMIENNA`, najprawdopodobniej nic nie zobaczymy.** Aby zmienna środowiskowa była widoczna globalnie, należałoby ją ustawić bezpośrednio w powłoce lub w pliku konfiguracyjnym systemu.


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

**Ten wzorzec jest bardzo popularny w środowiskach produkcyjnych, gdzie klucze i hasła nie powinny znajdować się w kodzie, tylko w dedykowanym rozwiązaniu do zarządzania sekretami, który przekazuje je jako zmienne środowiskowe.** Dzięki temu nie musimy obawiać się, że ktoś podejrzy hasła w repozytorium kodu.
