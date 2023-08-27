## Pliki wykonywalne i PyInstaller

Jeśli chcesz podzielić się swoją aplikacją Python z innymi użytkownikami, którzy niekoniecznie mają zainstalowane środowisko Pythona, pakowanie twojego kodu w plik wykonywalny (.exe, .app, .bin itp. w zależności od systemu operacyjnego) jest doskonałym rozwiązaniem. Narzędziem, które doskonale spełnia to zadanie, jest [PyInstaller](https://www.pyinstaller.org/).

### Instalacja

Aby zacząć korzystać z PyInstaller, najpierw musisz go zainstalować. Możesz to zrobić za pomocą narzędzia pip:

```bash
pip install pyinstaller
```

### Tworzenie pliku wykonywalnego

Po zainstalowaniu PyInstaller możesz łatwo przekształcić swój skrypt Pythona w plik wykonywalny:

```bash
pyinstaller --onefile nazwa_pliku.py
```

Opcja `--onefile` powoduje, że cała aplikacja, wraz ze wszystkimi zależnościami, jest pakowana w jeden plik wykonywalny.

Po zakończeniu procesu, w wygenerowanym katalogu dist znajdziesz plik wykonywalny (np. `nazwa_pliku.exe` dla Windows). Teraz możesz łatwo podzielić się swoją aplikacją, przesyłając ten plik.

### Zaawansowane ustawienia

PyInstaller oferuje szeroką gamę opcji i flag, które pozwalają dostosować proces tworzenia pliku wykonywalnego. Oto kilka przykładów:

- **Tryb GUI vs Tryb konsoli**: Domyślnie PyInstaller tworzy plik wykonywalny z oknem konsoli. Jeśli chcesz ukryć okno konsoli (przydatne dla aplikacji z interfejsem graficznym), możesz użyć flagi `--noconsole`.

- **Dołączanie zasobów**: Jeśli twoja aplikacja korzysta z dodatkowych plików, takich jak obrazy czy dźwięki, możesz je dołączyć do pliku wykonywalnego za pomocą flagi `--add-data='ścieżka/źródłowa;ścieżka/docelowa'`.

- **Ikonka aplikacji**: Chcesz, aby twój plik wykonywalny miał niestandardową ikonę? Użyj flagi `--icon=ścieżka_do_ikony.ico`.

- **Wyłączanie modułów**: Jeśli wiesz, że pewne moduły Pythona nie są potrzebne w twoim pliku wykonywalnym, możesz je wykluczyć za pomocą flagi `--exclude`.

- **Optymalizacja**: Możesz zredukować rozmiar pliku wykonywalnego i przyspieszyć start aplikacji, korzystając z flagi `--optimize=1` lub `--optimize=2`.

- **Jedno plik vs Katalog**: Domyślnie PyInstaller tworzy katalog z plikiem wykonywalnym i wszystkimi zależnościami. Jeśli chcesz, aby cała aplikacja była spakowana w jeden plik, użyj opcji `--onefile`.

Aby uzyskać pełną listę dostępnych opcji i dokładne ich opisy, warto odwiedzić [oficjalną dokumentację PyInstaller](https://pyinstaller.readthedocs.io/en/stable/index.html).
