## Pliki wykonywalne i PyInstaller

Tworzenie plików wykonywalnych z kodu to efektywny sposób na dzielenie się aplikacjami z użytkownikami, którzy nie mają zainstalowanego Pythona na swoim komputerze. W tym kontekście, PyInstaller odgrywa kluczową rolę, umożliwiając konwersję skryptów na pliki `.exe`, `.app`, `.bin` itd., zależnie od systemu operacyjnego.

### Instalacja PyInstaller

Zacznij od zainstalowania PyInstaller za pomocą `pip`:

`pip install pyinstaller`

### Tworzenie pliku wykonywalnego

Po instalacji, użyj PyInstaller do konwersji skryptu Python:

```
pyinstaller --onefile nazwa_skryptu.py
```

Użycie `--onefile` skutkuje stworzeniem pojedynczego pliku wykonywalnego, zawierającego wszystkie zależności.

### Dołączanie zasobów: Grafika, Dźwięk, i inne

W aplikacjach Python często korzysta się z zewnętrznych zasobów takich jak grafiki, dźwięki czy pliki konfiguracyjne. PyInstaller umożliwia dołączanie tych elementów do twojego pliku wykonywalnego.

#### Jak to zrobić?

Użyj opcji `--add-data`:

```
pyinstaller --add-data 'ścieżka_do_zasobu;ścieżka_w_aplikacji' twoj_skrypt.py
```

- `ścieżka_do_zasobu` to ścieżka do pliku lub katalogu na twoim komputerze.
- `ścieżka_w_aplikacji` to ścieżka, w której zasób będzie dostępny w aplikacji.

#### Dołączanie wielu zasobów

Możesz dołączyć wiele zasobów, powtarzając opcję `--add-data`:

```
pyinstaller --add-data 'ścieżka/do/obrazu;ścieżka/w/aplikacji' --add-data 'ścieżka/do/dźwięku;ścieżka/w/aplikacji' twoj_skrypt.py
```

#### Przykład

Masz aplikację z obrazami i plikami konfiguracyjnymi w folderze `resources`. 

```
app/
│   main.py
│
└───resources/
    ├───images/
    │   logo.png
    │   icon.png
    │
    └───config/
        settings.conf
```

Aby je dołączyć, użyj:

```
pyinstaller --add-data 'resources/images;resources/images' --add-data 'resources/config;resources/config' main.py
```

#### Uwaga: Dostęp do zasobów

Aby prawidłowo odnaleźć zasoby po spakowaniu aplikacji, można użyć funkcji `resource_path`. Funkcja ta sprawdza, czy aplikacja jest uruchamiana z katalogu tymczasowego (kiedy atrybut `sys._MEIPASS` jest dostępny). Jeśli tak, ścieżka do zasobów jest tworzona w odniesieniu do tego katalogu. W przeciwnym razie zwraca bezpośrednią ścieżkę do zasobu.

```python
import sys
from PyInstaller.utils.hooks import collect_data_files

data_files = collect_data_files('twoj_modul')

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(relative_path)

# Przykład użycia:
image_path = resource_path('resources/images/logo.png')
```

W przykładzie ścieżka do obrazka `logo.png` w katalogu `resources/images` jest uzyskiwana przy użyciu funkcji `resource_path`. Dzięki temu kod będzie działał poprawnie zarówno w środowisku deweloperskim, jak i po spakowaniu aplikacji do jednego pliku wykonywalnego.

### Zaawansowane Ustawienia

- PyInstaller domyślnie tworzy plik wykonywalny, który otwiera **okno konsoli**. Aby stworzyć aplikację GUI bez okna konsoli, należy użyć opcji `--noconsole`.
- **Ikonę** pliku wykonywalnego można zmienić, używając opcji `--icon=ścieżka_do_ikony.ico`.
- Określone **moduły** Pythona, które nie są potrzebne, można wykluczyć przy użyciu opcji `--exclude=moduł`.
- Rozmiar aplikacji można zredukować, a jej **start** przyspieszyć za pomocą opcji `--optimize=1` lub `--optimize=2`.
- Zaawansowane **konfiguracje** pakowania można osiągnąć, tworząc i modyfikując plik specyfikacji (`.spec`). Plik ten pozwala na szczegółowe określenie, jakie pliki mają być dołączone, jakie moduły wykluczone oraz strukturę katalogów.
- Oprócz trybu `--onefile`, w którym PyInstaller tworzy jeden plik wykonywalny, istnieje domyślny tryb, gdzie PyInstaller tworzy **katalog** z plikiem wykonywalnym i wszystkimi zależnościami oddzielnie. Opcja ta jest szczególnie przydatna, gdy rozmiar końcowego pliku ma kluczowe znaczenie.

Dla pełnego zrozumienia możliwości PyInstaller, zalecam zapoznanie się z [dokumentacją PyInstaller](https://pyinstaller.readthedocs.io/en/stable/index.html). Jest to niezbędne, aby w pełni wykorzystać potencjał narzędzia, szczególnie w przypadku bardziej złożonych aplikacji.
