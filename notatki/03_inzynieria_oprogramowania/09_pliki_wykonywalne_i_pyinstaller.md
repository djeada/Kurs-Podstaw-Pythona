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

W aplikacji spakowanej pliki będą dostępne pod tymi samymi ścieżkami.

#### Uwaga: Dostęp do zasobów

Po spakowaniu, ścieżki dostępu do zasobów mogą się zmienić. Użyj funkcji `resource_path` w PyInstaller, aby uzyskać poprawną ścieżkę:

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

### Zaawansowane Ustawienia

- **Tryb GUI vs Tryb Konsoli**: Domyślnie PyInstaller tworzy plik z oknem konsoli. Aby stworzyć aplikację GUI bez konsoli, użyj `--noconsole`.

- **Ikona Aplikacji**: Możesz zmienić ikonę pliku wykonywalnego, używając `--icon=ścieżka_do_ikony.ico`.

- **Wykluczanie Modułów**: Możesz wykluczyć określone moduły Python, które nie są potrzebne, używając `--exclude=moduł`.

- **Optymalizacja**: Redukuj rozmiar i przyspieszaj start aplikacji za pomocą `--optimize=1` lub `--optimize=2`.

- **Specyfikacja Pakowania**: Zaawansowane konfiguracje można osiągnąć tworząc i modyfikując plik specyfikacji (`.spec`). Pozwala to na szczegółowe określenie, jakie pliki mają być dołączone, jakie moduły wykluczone, strukturę katalogów itd.

- **Jeden Plik vs Katalog**: Oprócz trybu `--onefile`, istnieje również domyślny tryb, gdzie PyInstaller tworzy katalog z plikiem wykonywalnym i wszystkimi zależnościami oddzielnie. Opcja ta jest przydatna, gdy rozmiar końcowego pliku jest krytyczny.

Dla pełnego zrozumienia możliwości PyInstaller, zalecam zapoznanie się z [dokumentacją PyInstaller](https://pyinstaller.readthedocs.io/en/stable/index.html). Jest to niezbędne, aby w pełni wykorzystać potencjał narzędzia, szczególnie w przypadku bardziej złożonych aplikacji.
