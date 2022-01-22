# Kurs-podstaw-Pythona
Kurs podstaw Pythona

## Podstawy

### Instalacja w systemie Windows
### Interaktywna konsola
### Zmienne

Zmienna to pudełko przechowujące dane. Każda zmienna ma swoją nazwę, poprzez którą odwołujemy się do niej w programie. Każda zmienna ma również swój typ, czyli rodzaj danych, jaki przechowuje. 

Typy danych w Pythonie: 
- Liczby całkowite (int) 
- Liczby zmiennoprzecinkowe (float) 
- Napisy (string) 
- Typ logiczny (bool) 

Zmienne są podstawą każdego języka programowania. Nazwa może składać się z liter i cyfr, jednak nie może zaczynać się od cyfry. Python nie ogranicza długości nazwy zmiennej. Dobry programista nadaje zmiennym nazwy reprezentujące ich zadanie w kodzie. Dzięki temu program staje się czytelny i łatwiejszy w utrzymaniu.

### Warunki

Typ logiczny może przyjmować jedna z dwóch wartości <code>True</code> lub <code>False</code>. Typ logiczny ma istotne znaczenie dla instrukcji warunkowej. 

Przy porównaniach początkujący programiści często zapominają, że pojedynczy znak równości to przypisanie.

- <code>x = 5</code> w taki sposób zapiszemy w zmiennej x wartość 5.
- <code>x == 5</code> w taki sposób sprawdzimy czy zmienna x przechowuje wartość 5.

Instrukcja warunkowa ma następującą postać:

    If warunek:
        kod
    else:
        kod

Część kodu umieszczona w pierwszym wcięciu po instrukcji warunkowej zostanie wykonana jedynie, gdy warunek jest prawdziwy. Gdy warunek nie jest spełniony, ta część kodu zostanie całkowicie pominięta, a zamiast niej wykonany zostanie kod umieszczony w drugim wcięciu (pod słowem kluczowym else). Instrukcje warunkowe zwane są też czasami instrukcjami sterującymi.

Operatory logiczne służą do łączenia warunków. W Pythonie mamy do dyspozycji trzy operatory logiczne: <code>and</code>, <code>or</code> i <code>not</code>: 

* <code>and</code> – aby wyrażenie było prawdziwe, oba warunki muszą być prawdziwe.
* <code>or</code> – aby wyrażenie było prawdziwe, tylko jeden warunek musi być prawdziwy.
* <code>not</code> – zaprzeczenie wyrażenia.

Wyrażenie <code>a != 0 and b == 5</code> będzie prawdziwe, jeśli oba warunki są spełnione, tzn. jeśli a jest różne od 0 i jednocześnie b jest równe 5.

Wyrażenie <code>x % 2 == 0 or x % 7 == 0</code> będzie prawdziwe, jeśli jeden z warunków jest spełniony, tzn. jeśli x jest podzielne przez 2 lub x jest podzielne przez 7.

### Pętle

Pętle wraz z instrukcjami warunkowymi to podstawa wszystkich języków programowania. Pętla umożliwia wielokrotne wykonanie pojedynczej instrukcji lub całego bloku instrukcji. Oprócz bloku instrukcji każda pętla ma również warunek zakończenia. Pętla powtarza blok instrukcji, dopóki nie zostanie spełniony warunek kończący pętlę. W Pythonie mamy dwie pętle <code>For</code> oraz <code>While</code>. 

#### For
Pętla <code>For</code> ma postać:

    for element in kolekcja: 
        kod

Na razie do tworzenia pętli będziemy używać funkcji <code>range()</code>. Funkcja ta może przyjmować jeden, dwa lub trzy parametry.

1. <code>range(10)</code> utworzy ciąg 0123456789, tak więc pętla: <code>for x in range(10)</code> zostanie wykonana 10 razy.
2. <code>range(5,12)</code> utworzy ciąg 567891011, tak więc pętla: <code>for x in range(5,12)</code> zostanie wykonana 7 razy.
3. <code>range(0,50,10)</code> utworzy ciąg 010203040, tak więc pętla: <code>for x in range(0,50,10)</code> zostanie wykonana 5 razy.

#### While

Pętla <code>While</code> ma postać:

    while warunek konczacy petle: 
         kod

Użycie instrukcji <code>break</code> spowoduje zakończenie wykonywania najbliżej zagnieżdżonej pętli (działa zarówno dla pętli <code>While</code>, jak i <code>For</code>).

Użycie instrukcji <code>continue</code> spowoduje przejście do następnego obiegu pętli. Wszystkie instrukcje umieszczone pod instrukcją <code>continue</code> nie zostaną wykonane po jej wywołaniu.

### Pętle zagnieżdżone

Podobnie jak możemy zagnieżdżać instrukcje warunkowe, możemy również zagnieżdżać pętle. Jedna pętla może znajdować się w ciele innej pętli. W celu zobrazowania działania takiej konstrukcji posłużymy się graficznymi przykładami i będziemy wypisywać na konsoli różne kształty.

Dwie reguły zagnieżdżania pętli:

1. Pętla zewnętrzna pilnuje wysokości.
1. Pętla wewnętrzna pilnuje szerokości.

        for y in range(10):
            for x in range(10): 
                kod

Jeśli idziemy do sali kinowej i nasz bilet mówi nam, że przysługuje nam miejsce numer 5 w rzędzie numer 2, to pętle zewnętrzna ustawi nas w odpowiednim rzędzie, a pętla wewnętrzna na odpowiednim miejscu.

### Funkcje
### Napisy

String to tekstowy typ danych. Tutaj będziemy nazywali go napisem. Napis składa się z ciągu znaków. Znakami mogą być litery lub znaki interpunkcyjne, ale również cyfry.

W Pythonie napis deklarujemy, używając apostrofów  bądź cudzysłowów. 

    napis = 'James' 
    napis = "James" 
    napis = '''James''' 

Nie ma oddzielnego typu dla pojedynczego znaku. Pojedynczy znak to napis o długości równej 1. Napisy są indeksowane od 0 tak jak i listy. Do konkretnego znaku w danym napisie możemy odwołać się poprzez jego indeks. 

Przykładowo dla kodu <code>James = 'Lubie go'</code>, wywołanie <code>James[0]</code> zwróci literę 'L'. Wywołanie <code>James[2]</code> zwróci literę 'b'. 

Zainicjalizowany napis nie może być zmieniony. To znaczy, nie możemy zrobić czegoś takiego: <code>James[0]='z'</code>. Jeśli chcemy wprowadzić zmiany do napisu, musimy nadpisać aktualny napis innym napisem.

    napis = "pierwotny"
    napis = "nowy"

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

### Pomoc
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

Jednym z najpopularniejszych narzędzi do zarządzania dokumentacją w Pythonie jest Sphinx. Jest prosty w użyciu i zawiera wiele przydatnych funkcji. Z pomocą tego narzędzia możesz tworzyć dokumentację w różnych formatach, takich jak HTML, LaTeX, epub, czy zwykły tekst. Można łatwo dokonać konwersji pliku w formacie LaTeX na PDF.

Użyj komendy <code>quickstart</code>, aby zbudować szkielet dokumentacji. Będziesz musiał odpowiedzieć na kilka pytań (tak lub nie), na podstawie twoich odpowiedzi Sphinx wygeneruje odpowiednie pliki startowe i wypełni je treścią.

    quickstart

Aby utworzyć dokumentację z plików konfiguracyjnych, należy użyć komendy <code>make</code> wraz z formatem, w jakim chcemy, aby była nasza dokumentacja.

    make html

Program poinformuje cię o pomyślnym utworzeniu dokumentacji, jeśli w trakcie procesu <code>make</code> nie napotkał żadnych problemów. W przeciwnym razie proces tworzenia dokumentacji zostanie przerwany, a na konsoli zostaną wyświetlone komunikaty o błędach. Przykładem błędu może być umieszczenie linku do nieistniejącego pliku.

#### reStructuredText

Plikiem startowym dokumentacji jest <code>index.rst</code>. Plik ten zapisany jest w formacie zwanym reStructuredText, a w skrócie rst. Jest to rozszerzenie języka mark down, innego języka znaczników. Jego głównym atutem jest możliwość instalowania przydatnych pluginów. Uproszczony został również proces linkowania plików, co jest znaczące dla dokumentacji.  Komenda <code>make html</code> generuje na podstawie wszystkich plików z rozszerzeniem .rst odpowiadające im pliki html.

#### Jak pisać dobrą dokumentację?

1. Pierwsza rzecz to tutoriale. Powinniśmy pokazać użytkownikowi naszego oprogramowania jak je zainstalować i uruchomić.
2. Drugim istotnym punktem jest poradnik. Powinniśmy jasno przedstawić jak używać naszego programu. Wszystkie dostępne funkcje powinny być zaprezentowane i wyjaśnione.
3. Inną istotną rzeczą są wyjaśnienia. Innych programistów interesować będzie jak działa nasz program za kulisami. Należy opisać jakie decyzje zostały podjęte przy projektowaniu.
4. Na koniec warto również dodać referencje do komentarzy (docstrings) umieszczonych w naszym kodzie. W szczególności szczegółowo powinno zostać opisane API (interfejs programistyczny aplikacji).

#### Automatyczne generowanie dokumentacji do API

Jeśli opisujesz swoje funkcje, klasy oraz moduły w kodzie to te komentarze (docstrings)  mogą zostać wykorzystane do automatycznego generowania dokumentacji.

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

* https://docs.python.org/3/tutorial/
* https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/
* https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0002-introduction-to-computational-thinking-and-data-science-fall-2016/
* https://braydie.gitbook.io/how-to-be-a-programmer/
