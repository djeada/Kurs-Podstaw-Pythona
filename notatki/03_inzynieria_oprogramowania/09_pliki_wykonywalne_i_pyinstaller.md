
## Pliki wykonywalne i PyInstaller

Jeśli chcesz udostępnić swoją aplikację innym osobom, prawdopodobnie będziesz chciał zapakować ją w plik wykonywalny. W przypadku systemu Windows najprostszym sposobem na stworzenie pliku wykonywalnego jest użycie programu <a href = "https://www.pyinstaller.org/">PyInstaller</a>.

Aby użyć PyInstaller, należy zainstalować go za pomocą pip:

```
pip install pyinstaller
```

Następnie możesz wygenerować plik wykonywalny za pomocą polecenia:

```
pyinstaller nazwa_pliku.py
```

Po wykonaniu polecenia zostanie utworzony folder dist, w którym znajdziesz plik wykonywalny o nazwie nazwa_pliku.exe. Możesz go umieścić w dowolnym miejscu na dysku i uruchomić.

PyInstaller ma również opcje pozwalające na dostosowanie sposobu tworzenia plików wykonywalnych do swoich potrzeb. Przykładowo, możesz wybrać, czy chcesz zawrzeć w pliku wykonywalnym zasoby (np. obrazy, dźwięki), czy też chcesz udostępnić je osobno. Możesz także określić, czy plik wykonywalny ma być uruchamiany w oknie konsoli, czy też w osobnym oknie. Więcej informacji o opcjach dostępnych w PyInstaller znajdziesz w <a href = "https://pyinstaller.readthedocs.io/en/stable/index.html">dokumentacji</a>.
