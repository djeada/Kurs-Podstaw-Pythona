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

Poprawny z punktu widzenia interpretera kod można często napisać na wiele sposobów. Nawet jedna linia kodu może być zazwyczaj zapisana na więcej niż jeden sposób. Jedną z przyczyn różnic jest formatowanie. Przykładowo w kodzie można użyć zarówno spacji, jak i tabów. Definicje funkcji można oddzielać jednym, dwoma lub trzema enterami. Linie kodu mogą być tak długie, że nie zmieszczą się na ekranie. Czy należy ograniczać ich długość? Jeśli tak, to ile dokładnie znaków powinno być górną granicą? Dopóki pracujemy sami z kodem, wszystkie te przykłady nie mają dla nas znaczenia. Sami możemy podejmować decyzje i w dowolnej chwili zmienić zdanie. Co ma jednak zrobić grupa programistów pracująca wspólnie nad jednym projektem? Całe szczęście istnieje lista konwencji pisania kodu przygotowana przez twórców Pythona. Dwa główne dokumenty przedstawiające te konwencje to <code>PEP8</code> i <code>PEP257</code>. Dokumenty te definiują wytyczne do wszystkich poruszonych przez nas zagadnień, jak również wielu innych. Poza samymi suchymi regułami dokumenty te zawierają wiele przykładów kodu stosującego się do reguł oraz łamiącego reguły.

Istnieje wiele narzędzi (tak zwanych linterów) sprawdzających, czy kod przestrzega wytycznych twórców Pythona.

<code>Black</code> nie pyta o zdanie, automatycznie zmienia formatowanie kodu na zgodne z PEP8.

<code>Pylint</code> to jeden z najpopularniejszych linterów Pythona. Daje nam trochę więcej wskazówek niż <code>Black</code>, który interesuje się jedynie formatowaniem. <code>Pylint</code> zwróci również uwagę na niepoprawne nazwy zmiennych (np. a lub bb), czy funkcje i klasy pozostawione bez komentarzy (docstrings). Dodatkowo wiele narzędzi do CI/CD (np. Team City, Github Actions) zintegrowało <code>Pylint</code> ze swoim interfejsem graficznym.

<code>Flake8</code> to kolejne świetne narzędzie do lintowania. Choć w działaniu podobny jest do <code>Pylint</code> to jego największą zaletą jest ogromna paleta pluginów tworzonych przez społeczność. Dzięki temu możemy otrzymać jeszcze więcej wskazówek jak poprawić nasz kod.

Linki:

* https://www.python.org/dev/peps/pep-0008/
* https://www.python.org/dev/peps/pep-0257/
* https://github.com/psf/black
* https://github.com/PyCQA/pylint
* https://github.com/PyCQA/flake8

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
