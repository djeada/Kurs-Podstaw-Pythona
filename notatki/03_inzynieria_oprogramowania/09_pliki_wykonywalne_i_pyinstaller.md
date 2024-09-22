## Pliki wykonywalne i PyInstaller

Tworzenie plików wykonywalnych z kodu Python to efektywny sposób na dystrybucję aplikacji do użytkowników, którzy nie mają zainstalowanego Pythona na swoim komputerze. Jest to szczególnie istotne w środowiskach korporacyjnych lub dla użytkowników niebędących programistami, gdzie instalacja interpretera Python może być problematyczna lub niemożliwa. **PyInstaller** odgrywa kluczową rolę w tym procesie, umożliwiając konwersję skryptów Python na samodzielne pliki wykonywalne dla różnych systemów operacyjnych, takich jak Windows (`.exe`), macOS (`.app`) czy Linux (`.bin`). Dzięki temu aplikacja może być uruchomiona na docelowym systemie bez konieczności instalacji dodatkowego oprogramowania czy bibliotek.

**Dlaczego PyInstaller?** 

Istnieją inne narzędzia do tworzenia plików wykonywalnych z kodu Python, takie jak `cx_Freeze`, `py2exe` czy `Nuitka`. Jednak PyInstaller wyróżnia się prostotą użycia, szerokim wsparciem dla różnych systemów operacyjnych oraz zdolnością do obsługi złożonych aplikacji z wieloma zależnościami. Ponadto, PyInstaller automatycznie analizuje zależności skryptu i dołącza niezbędne biblioteki, co ułatwia proces pakowania aplikacji.

### Instalacja PyInstaller

Aby rozpocząć korzystanie z PyInstaller, należy go najpierw zainstalować. PyInstaller jest dostępny w repozytorium PyPI, więc można go zainstalować za pomocą menedżera pakietów `pip`. Upewnij się, że masz zainstalowaną najnowszą wersję `pip` oraz Pythona.

```bash
pip install pyinstaller
```

Jeśli posiadasz zarówno Pythona 2, jak i Pythona 3, możesz użyć `pip3`, aby upewnić się, że PyInstaller zostanie zainstalowany dla Pythona 3:

```bash
pip3 install pyinstaller
```

**Sprawdzenie poprawności instalacji:**

Po zainstalowaniu PyInstaller możesz sprawdzić jego wersję, aby upewnić się, że instalacja przebiegła pomyślnie:

```bash
pyinstaller --version
```

Jeśli komenda zwróci numer wersji, oznacza to, że PyInstaller jest gotowy do użycia.

**Rozwiązywanie problemów:**

Jeśli napotkasz problemy podczas instalacji, upewnij się, że:

- Masz uprawnienia administratora lub użyj `--user` przy instalacji:

```bash
pip install --user pyinstaller
```

- Twoje środowisko wirtualne (jeśli używasz `venv` lub `virtualenv`) jest aktywne.
- Masz zainstalowaną odpowiednią wersję Pythona (PyInstaller wspiera Pythona 3.5 i nowsze).

### Tworzenie pliku wykonywalnego

Po zainstalowaniu PyInstaller możesz przystąpić do konwersji swojego skryptu Python na plik wykonywalny. Podstawowa składnia polecenia PyInstaller jest następująca:

```bash
pyinstaller [opcje] nazwa_skryptu.py
```

Aby stworzyć pojedynczy plik wykonywalny zawierający wszystkie zależności, użyj opcji `--onefile`:

```bash
pyinstaller --onefile nazwa_skryptu.py
```

**Co dzieje się podczas tego procesu?**

- PyInstaller analizuje twój skrypt, identyfikuje wszystkie importowane moduły i biblioteki.
- Kod Python jest kompilowany do kodu bajtowego (`.pyc`).
- Wszystkie niezbędne pliki, w tym biblioteki dynamiczne (.dll, .so, .dylib), są dołączane.
- PyInstaller tworzy plik wykonywalny specyficzny dla systemu operacyjnego.

**Struktura wynikowych plików:**

Po wykonaniu polecenia PyInstaller utworzy kilka plików i folderów:

- `build/`: Katalog tymczasowy używany podczas procesu kompilacji.
- `dist/`: Katalog zawierający finalny plik wykonywalny lub folder aplikacji.
- `nazwa_skryptu.spec`: Plik specyfikacji zawierający konfigurację procesu pakowania.

**Uruchomienie pliku wykonywalnego:**

Plik wykonywalny znajduje się w folderze `dist/`. Możesz go uruchomić bezpośrednio:

Na Windows:

```bash
dist\nazwa_skryptu.exe
```

Na macOS/Linux:

```bash
./dist/nazwa_skryptu
```

**Uwaga:** Na systemach Unix może być konieczne nadanie plikowi uprawnień wykonywania:

```bash
chmod +x ./dist/nazwa_skryptu
```

**Rozwiązywanie problemów z zależnościami:**

W niektórych przypadkach PyInstaller może nie wykryć wszystkich zależności, zwłaszcza jeśli używasz dynamicznego importu lub modułów ładowanych w czasie wykonywania. Może to prowadzić do błędów typu `ModuleNotFoundError` podczas uruchamiania pliku wykonywalnego.

**Rozwiązanie:**

Użyj opcji `--hidden-import`:

```bash
pyinstaller --onefile --hidden-import=modul_ukryty nazwa_skryptu.py
```

Możesz podać wiele ukrytych importów, powtarzając opcję:

```bash
pyinstaller --onefile --hidden-import=modul1 --hidden-import=modul2 nazwa_skryptu.py
```

Alternatywnie, możesz edytować plik specyfikacji `.spec` i dodać brakujące moduły do listy `hiddenimports`.

### Dołączanie zasobów: Grafika, Dźwięk i Inne

W aplikacjach Python często korzysta się z zewnętrznych zasobów takich jak grafiki, dźwięki, pliki konfiguracyjne czy bazy danych. Aby aplikacja działała poprawnie po spakowaniu, te zasoby muszą być dołączone do pliku wykonywalnego lub dystrybuowane wraz z nim.

#### Jak to zrobić?

PyInstaller umożliwia dołączanie dodatkowych plików za pomocą opcji `--add-data`. Składnia tej opcji różni się w zależności od systemu operacyjnego:

Na Windows:

```bash
pyinstaller --add-data "ścieżka_do_zasobu;ścieżka_w_aplikacji" nazwa_skryptu.py
```

Na macOS/Linux:

```bash
pyinstaller --add-data "ścieżka_do_zasobu:ścieżka_w_aplikacji" nazwa_skryptu.py
```

**Parametry:**

- `ścieżka_do_zasobu` to ścieżka do pliku lub katalogu na twoim komputerze.
- `ścieżka_w_aplikacji` to ścieżka, pod którą zasób będzie dostępny w aplikacji.

**Przykład:**

Dołączenie pliku `config.json` znajdującego się w katalogu `settings`:

Windows:

```bash
pyinstaller --add-data "settings\config.json;settings" nazwa_skryptu.py
```

macOS/Linux:

```bash
pyinstaller --add-data "settings/config.json:settings" nazwa_skryptu.py
```

#### Dołączanie wielu zasobów

Możesz dołączyć wiele zasobów, powtarzając opcję `--add-data` dla każdego z nich:

Windows:

```bash
pyinstaller --add-data "images\logo.png;images" --add-data "sounds\alert.wav;sounds" nazwa_skryptu.py
```

macOS/Linux:

```bash
pyinstaller --add-data "images/logo.png:images" --add-data "sounds/alert.wav:sounds" nazwa_skryptu.py
```

#### Przykład

Masz aplikację z następującą strukturą:

```
projekt/
│   main.py
│
└───resources/
    ├───images/
    │       logo.png
    │       icon.png
    │
    └───config/
            settings.conf
            data.json
```

Aby dołączyć cały katalog `resources`, użyj:

Windows:

```bash
pyinstaller --onefile --add-data "resources;resources" main.py
```

macOS/Linux:

```bash
pyinstaller --onefile --add-data "resources:resources" main.py
```

#### Uwaga: Dostęp do zasobów

Aby poprawnie odnaleźć zasoby w kodzie po spakowaniu aplikacji, musisz uwzględnić fakt, że ścieżki do plików zmieniają się w zależności od tego, czy aplikacja jest uruchamiana jako skrypt, czy jako spakowany plik wykonywalny.

**Funkcja `resource_path`:**

```python
import sys
import os

def resource_path(relative_path):
    """Zwraca absolutną ścieżkę do zasobu, obsługując PyInstaller."""
    try:
        # PyInstaller tworzy tymczasowy folder i przechowuje w nim zasoby
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
```

- `sys._MEIPASS` to atrybut dodawany przez PyInstaller wskazujący na tymczasowy katalog, w którym przechowywane są zasoby.
- Jeśli aplikacja jest uruchamiana jako skrypt, `sys._MEIPASS` nie istnieje, więc używamy bieżącego katalogu.

**Przykład użycia:**

```python
image_path = resource_path('resources/images/logo.png')
image = Image.open(image_path)
```

Dzięki temu kod będzie działał poprawnie zarówno w środowisku deweloperskim, jak i po spakowaniu aplikacji.

### Zaawansowane Ustawienia

PyInstaller oferuje wiele opcji pozwalających na dostosowanie procesu pakowania.

#### Ukrywanie konsoli

Domyślnie PyInstaller tworzy aplikację konsolową. Aby stworzyć aplikację GUI bez konsoli, użyj opcji `--noconsole`:

```bash
pyinstaller --onefile --noconsole nazwa_skryptu.py
```

**Przykład:** Jeśli tworzysz aplikację z interfejsem graficznym (np. z użyciem Tkinter, PyQt), użyj `--noconsole`, aby uniknąć pojawiania się pustego okna konsoli.

#### Zmiana ikony pliku wykonywalnego

Aby zmienić ikonę pliku wykonywalnego, użyj opcji `--icon`:

```bash
pyinstaller --onefile --icon=path/to/icon.ico nazwa_skryptu.py
```

**Uwaga:** Na Windows ikona powinna być w formacie `.ico`. Na macOS można użyć formatu `.icns`.

#### Wykluczanie niepotrzebnych modułów

Aby zredukować rozmiar pliku wykonywalnego, możesz wykluczyć nieużywane moduły:

```bash
pyinstaller --onefile --exclude-module=modul_do_wykluczenia nazwa_skryptu.py
```

**Przykład:** Jeśli nie używasz modułu `tkinter`, możesz go wykluczyć:

```bash
pyinstaller --onefile --exclude-module=tkinter nazwa_skryptu.py
```

#### Optymalizacja rozmiaru aplikacji

Możesz optymalizować kod bajtowy Pythona, co może zmniejszyć rozmiar aplikacji:

- `--optimize=1` lub `-O1`: Usuwa docstringi.
- `--optimize=2` lub `-O2`: Usuwa docstringi i asercje.

**Przykład:**

```bash
pyinstaller --onefile --optimize=2 nazwa_skryptu.py
```

**Uwaga:** Używaj `-O2` ostrożnie, ponieważ usunięcie asercji może ukryć potencjalne błędy.

#### Modyfikacja pliku specyfikacji (`.spec`)

Plik `.spec` zawiera szczegółowe informacje o tym, jak PyInstaller ma spakować twoją aplikację. Możesz go edytować, aby uzyskać większą kontrolę nad procesem.

**Kroki:**

I. Wygeneruj plik `.spec`:

```bash
pyinstaller --onefile --name=nazwa_aplikacji --specpath=. nazwa_skryptu.py
```

II. Edytuj `nazwa_aplikacji.spec` zgodnie z potrzebami.

III. Spakuj aplikację używając pliku specyfikacji:

```bash
pyinstaller nazwa_aplikacji.spec
```

**Co można zmienić w pliku `.spec`?**

- Możesz dodawać pliki danych bezpośrednio w sekcji `datas`.
- Możesz dodawać ukryte importy w liście `hiddenimports`.
- Możesz ustawić ikonę w obiekcie `EXE`.

#### Tryb katalogu

Zamiast tworzyć pojedynczy plik wykonywalny, możesz pozostawić aplikację w formie katalogu:

```bash
pyinstaller nazwa_skryptu.py
```

**Zalety:**

- Szybszy start aplikacji, ponieważ nie musi się rozpakowywać.
- Łatwiejsza diagnostyka i możliwość podmiany pojedynczych plików.

#### Zwiększenie poziomu logowania

Aby uzyskać więcej informacji podczas pakowania, możesz zwiększyć poziom logowania:

```bash
pyinstaller --onefile --log-level=DEBUG nazwa_skryptu.py
```

**Poziomy logowania:** `TRACE`, `DEBUG`, `INFO`, `WARN`, `ERROR`, `CRITICAL`.

Rozumiem, że potrzebujesz bardziej szczegółowego i rozbudowanego przykładu dotyczącego tworzenia hooków oraz obsługi niestandardowych modułów w PyInstallerze. Poniżej przedstawiam bardziej szczegółowy opis, który zawiera dokładne kroki i instrukcje.

#### Hooki i obsługa niestandardowych modułów

Hooki w PyInstallerze to specjalne skrypty Pythona, które pozwalają na obsługę modułów wymagających niestandardowej konfiguracji lub specjalnego traktowania podczas procesu budowania. Mogą być one potrzebne, gdy moduły dynamicznie importują inne moduły, używają zasobów zewnętrznych lub mają inne zależności, których PyInstaller nie jest w stanie wykryć automatycznie.

##### Kiedy potrzebujesz hooków?
Zwykle PyInstaller samodzielnie rozpoznaje zależności i moduły potrzebne do działania aplikacji. Jednak niektóre moduły korzystają z dynamicznego importowania, co może powodować, że PyInstaller nie wykryje ich poprawnie. Przykłady takich modułów to np. `numpy`, `tensorflow`, `scipy` czy własne niestandardowe moduły.

##### Tworzenie hooka: krok po kroku

**I. Utworzenie katalogu `hooks`**

Zanim stworzymy hooka, musimy przygotować odpowiednią strukturę katalogów. W tym celu utwórz katalog o nazwie `hooks` w głównym folderze projektu. W tym katalogu umieścisz wszystkie niestandardowe hooki, które będą obsługiwać dodatkowe moduły.

```bash
mkdir hooks
```

**II. Stworzenie pliku hooka**

Każdy hook to osobny plik o nazwie `hook-<nazwa_modulu>.py`, gdzie `<nazwa_modulu>` to nazwa modułu, który wymaga specjalnej obsługi. Załóżmy, że chcesz spakować aplikację korzystającą z modułu o nazwie `moj_modul`, który dynamicznie ładuje inne podmoduły.

W tym przypadku utwórz plik `hook-moj_modul.py` w katalogu `hooks/`:

```bash
touch hooks/hook-moj_modul.py
```

**III. Konfiguracja hooka**

W pliku `hook-moj_modul.py` musisz zdefiniować, jak PyInstaller powinien traktować `moj_modul`. W najprostszej formie możesz użyć funkcji `collect_submodules` z pakietu `PyInstaller.utils.hooks`, aby zebrać wszystkie podmoduły, które mogą być dynamicznie importowane. Przykład takiej konfiguracji:

```python
# hooks/hook-moj_modul.py
from PyInstaller.utils.hooks import collect_submodules

# Zbierz wszystkie podmoduły
hiddenimports = collect_submodules('moj_modul')
```

W tym przykładzie `hiddenimports` to lista podmodułów, które są dynamicznie ładowane przez `moj_modul`, a które muszą być explicite uwzględnione w pakiecie generowanym przez PyInstaller.

**IV. Zdefiniowanie dodatkowych zależności**

Oprócz `hiddenimports`, możesz także zdefiniować inne typy zasobów, takie jak dane, które muszą być dodane do pakietu. Na przykład, jeśli `moj_modul` korzysta z plików konfiguracyjnych, grafik, czy innych zasobów, można je uwzględnić, definiując dodatkową zmienną `datas`:

```python
# hooks/hook-moj_modul.py
from PyInstaller.utils.hooks import collect_submodules, collect_data_files

# Zbierz wszystkie podmoduły
hiddenimports = collect_submodules('moj_modul')

# Zbierz dane (np. pliki konfiguracyjne)
datas = collect_data_files('moj_modul')
```

**V. Użycie hooków podczas budowania aplikacji**

Aby PyInstaller uwzględnił nowo utworzone hooki, musisz przekazać ścieżkę do katalogu `hooks` za pomocą opcji `--additional-hooks-dir`. Przykład komendy budowania:

```bash
pyinstaller --onefile --additional-hooks-dir=hooks nazwa_skryptu.py
```

W tym przykładzie:

- `--onefile` tworzy jednoplikową binarkę.
- `--additional-hooks-dir=hooks` mówi PyInstallerowi, aby uwzględnił hooki z katalogu `hooks`.
- `nazwa_skryptu.py` to Twój główny skrypt Pythona.

**VI. Weryfikacja poprawności hooka**

Aby upewnić się, że hook działa prawidłowo, uruchom spakowaną aplikację i sprawdź, czy wszystkie moduły działają bez problemów. Możesz to zrobić, analizując plik `.spec`, który PyInstaller generuje podczas kompilacji, lub ręcznie testując aplikację po spakowaniu.

##### Przekazywanie argumentów do aplikacji

Jeśli Twoja aplikacja korzysta z argumentów wiersza poleceń, PyInstaller zachowa tę funkcjonalność po spakowaniu. Musisz jedynie upewnić się, że obsługa argumentów jest prawidłowo zaimplementowana w skrypcie, np. za pomocą modułów takich jak `argparse` lub `sys.argv`.

Przykład prostego skryptu obsługującego argumenty wiersza poleceń:

```python
import argparse

def main():
    parser = argparse.ArgumentParser(description="Opis aplikacji")
    parser.add_argument('--opcje', type=str, help="Przykładowa opcja")
    args = parser.parse_args()
    
    print(f"Otrzymano opcje: {args.opcje}")

if __name__ == '__main__':
    main()
```

Po spakowaniu aplikacji możesz ją uruchomić z argumentami wiersza poleceń:

```bash
./nazwa_aplikacji --opcje "wartość"
```
