# Kurs-podstaw-Pythona
Kurs podstaw Pythona

## Podstawy

### Installation on Windows
### Interactive Python console
### Zmienne
### Typy Danych
### Warunki
### Pętle
### Funkcje
### Napisy
### Kolekcje
### Enum

## Średniozawanowane

### Klasy i obiekty
### Referencje i mutacje
### Czyte funkcje i skutki uboczne
### Dziedziczenie i kompozycja
### Wyrażenia regularne
### Wyjątki
### Wątki
### Lambdy
### Generatory
### Iteratory

## Inżynieria oprogramowania

### Pomoc i dokumentajca
### Moduły i pakiety
### Werjse Pythona

<code>Pyenv</code> używany jest do izolowania różnych wersji Pythona. Na przykład jeśli chcesz przetestować swój kod w Pythonie 2.5, 3.6 i 3.10, potrzebujesz łatwego sposobu na przełączanie się między nimi. <code>Pyenv</code> modyfikuje zmienną środowiskową PATH dodając do niej ścieżkę do specjalnego folderu <code>(pyenv root)/shims</code>. <code>Pyenv</code> ułatwia również proces pobierania i instalowania różnych wersji Pythona za pomocą polecenia <code>pyenv install</code>.

Linki:

* https://github.com/pyenv/pyenv

### PIP i PyPI
### Środowisko wirtualne

Środowisko wirtualne to odizolowane od reszty systemu wersje bibliotek i pakietów Pythona. Instalując daną wersję pakietu w środowisku wirtualnym jest ona dostępna tylko w nim. Gdy usuwamy środowisko wirtualne wraz z nim znika również wszystko to co zostało zainstalowane w jęgo obrębie.

Popularnym narzędziem do tworzenia środowisk wirtualnych jest <code>virtualenv</code>. Narzędzie to tworzy specjalny folder o dowolnej nazwie (np. env/) oraz modyfikuje zmienną środowiskową PATH dodając do niej refernecje do podfolderu bin znajdującego się w utworzonym folderze (np. env/bin/). Wszystkie pakiety i biblioteki instalowane w środowisku wirtualnym wędrują do tego folderu.

Aby utworzyć środowisko wirtualnne w aktualnym folderze, użyj:

    virtualenv env

Aby wejść do środowiska wirtualnego, użyj:

    source env/bin/activate
    
Aby wyjść ze środowiska wirtualnego, użyj:

    deactivate
    
Linki:

* https://github.com/pypa/virtualenv

### Dbanie o jakość kodu i lintowanie
### Debugowanie

Debuger to program, którego zadanie jest inspeckja stanu programu w trakcie wykonywanie. Możesz użyć debugera, aby zatrzymać wykonywanie programu, gdy w trakcie wykonywania osiągnięta zostanie określone przez ciebie miejsce w kodzie. Po zatrzymaniu programu debuger pokazuje aktualne wartości wszystkich zmiennych istniejących w danym punkcie programu. Dzięki temu możemy zweryfikować, czy nasze wyobrażenia o tym jak działa program mają potwierdzenie w rzeczywistości. 

Dwa główne zastosowania debugera:
- Wyszukiwanie przyczyn bugów w kodzie.
- Analiza działania programu przez zaznajamiających się z nim programistów.

Większość współczesnych środwisk programistycznych (IDE) ma wbudowany debuger. Graficzny interfejs użytkownika umożliwa sterowanie debugerem za pomocą myszy. Miejsca, w których debuger ma zatrzymać program zaznaczane są często za pomocą czerownej kropki, a wartości zmiennych wyświetlane są w specjalnym panelu.

### Testy jednostkowe
### Dokumentacja
### Pliki wykonywalne i PyInstaller

## Python w Praktyce

### Praca z plikami i folderami
### Pandas i csv
### Daty
### Informacje o systemie operacyjnym
### HTTP i prosty serwer
### API wraz z FastAPI
### Bazy danych z SQLite
### Tkinter
### Logi

## Dodatkowe materiały

* https://braydie.gitbook.io/how-to-be-a-programmer/
