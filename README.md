# Kurs-podstaw-Pythona
Kurs podstaw Pythona

## Spis Treści
<!--ts-->
- [Podstawy](#Podstawy)
  - [Instalacja w systemie Windows](#Instalacja-w-systemie-Windows)
  - [Interaktywna konsola](#Interaktywna-konsola)
  - [Zmienne](#Zmienne)
  - [Warunki](#Warunki)
  - [Pętle](#Pętle)
  - [Pętle zagnieżdżone](#Pętle-zagnieżdżone)
  - [Funkcje](#Funkcje)
  - [Napisy](#Napisy)
  - [Struktury danych](#Struktury-danych)
  - [Enum](#Enum)
  - [Liczby losowe](#Liczby-losowe)

- [Średniozaawansowane](#Średniozaawansowane)
  - [Klasy i obiekty](#Klasy-i-obiekty)
  - [Referencje i mutacje](#Referencje-i-mutacje)
  - [Czyste funkcje i skutki uboczne](#Czyste-funkcje-i-skutki-uboczne)
  - [Dziedziczenie i kompozycja](#Dziedziczenie-i-kompozycja)
  - [Wyrażenia regularne](#Wyrażenia-regularne)
  - [Wyjątki](#Wyjątki)
  - [Wątki](#Wątki)
  - [Lambdy](#Lambdy)
  - [Data classes](#Data-classes)
  - [Generatory](#Generatory)
  - [Iteratory](#Iteratory)

- [Inżynieria oprogramowania](#Inżynieria-oprogramowania)
  - [Pomoc](#Pomoc)
  - [Moduły i pakiety](#Moduły-i-pakiety)
  - [Wersje Pythona](#Wersje-Pythona)
  - [PIP i PyPI](#PIP-i-PyPI)
  - [Środowisko wirtualne](#Środowisko-wirtualne)
  - [Dbanie o jakość kodu i lintowanie](#Dbanie-o-jakość-kodu-i-lintowanie)
  - [Debugowanie](#Debugowanie)
  - [Testy jednostkowe](#Testy-jednostkowe)
  - [Dokumentacja](#Dokumentacja)
  - [Pliki wykonywalne i PyInstaller](#Pliki-wykonywalne-i-PyInstaller)

- [Python w Praktyce](#Python-w-Praktyce)
  - [Praca z plikami i folderami](#Praca-z-plikami-i-folderami)
  - [Pandas i csv](#Pandas-i-csv)
  - [Daty](#Daty)
  - [Informacje o systemie operacyjnym](#Informacje-o-systemie-operacyjnym)
  - [HTTP i prosty serwer](#HTTP-i-prosty-serwer)
  - [API wraz z FastAPI](#API-wraz-z-FastAPI)
  - [Bazy danych z SQLite](#Bazy-danych-z-SQLite)
  - [Tkinter](#Tkinter)
  - [Logi](#Logi)

- [Dodatkowe materiały](#Dodatkowe-materiały) 

<!--te-->

## Podstawy

Fundamenty języka Python. Nauka budowania programów. Podstawy algorytmiki.

### Instalacja w systemie Windows

Aby zainstalować Pythona w systemie Windows, należy wykonać następujące kroki:

1. Odwiedź stronę [Python.org](https://www.python.org/downloads/).
2. Kliknij odpowiednią wersję Pythona.
3. Pobierz instalator i przejdź przez proces instalacji.

### Interaktywna konsola

Otwórz konsolę Python i wpisz:

    >>> python
    python 2.7.13 (default, Sep  2 2019, 20:42:59)

Zostanie wyświetlona informacja o wersji Pythona dostępnej w systemie.

Masz dostęp do wszystkich komend zdefiniowanych w danej wersji Pythona. Po wpisaniu komendy i naciśnięciu klawisza Enter, zostanie od razu zwrócony wynik wywołania komendy.

    >>> help
    Type help() for interactive help, or help(object) for help about object.

    >>> 3 + 4
    7

    >>> print('Hello world')
    Hello world

    >>> import math
    >>> math.pi
    3.141592653589793
    
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

1. <code>range(10)</code> utworzy ciąg <code>(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)</code>, tak więc pętla: <code>for x in range(10)</code> zostanie wykonana 10 razy.
2. <code>range(5,12)</code> utworzy ciąg <code>(5, 6, 7, 8, 9, 10, 11)</code>, tak więc pętla: <code>for x in range(5,12)</code> zostanie wykonana 7 razy.
3. <code>range(0,50,10)</code> utworzy ciąg <code>(0, 10 ,20, 30, 40)</code>, tak więc pętla: <code>for x in range(0,50,10)</code> zostanie wykonana 5 razy.

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

Jeśli idziemy do sali kinowej i nasz bilet mówi, że przysługuje nam miejsce numer 5 w rzędzie numer 2, to pętle zewnętrzna ustawi nas w odpowiednim rzędzie, a pętla wewnętrzna na odpowiednim miejscu.

### Funkcje

Funkcje umożliwiają wielokrotne wywołanie w kodzie pojedynczej instrukcji bądź całego bloku instrukcji poprzez nadanie mu nazwy. Funkcja ma następującą postać:

    def nazwa_funkcji(argumenty):
        kod

Ciało funkcji może być dowolnie rozbudowane, ale zaleca się, by większe funkcje rozbijać na mniejsze, każda o jednym zadaniu. W taki sposób zmniejszamy złożoność naszego kodu i kod staje się czytelniejszy.

Zdefiniowaną funkcję wywołujemy w kodzie poprzez jej nazwę. Przykład:

    # w tym miejscu definiuję funkcję
    def ryba():
       print('rybka')

    # w tym miejscu wywołuje funkcję
    ryba()

Funkcje mogą mieć dowolną ilość argumentów. Możliwe jest zarówno stworzenie funkcji bez argumentów, jak i funkcji z 10 argumentami. Przykład:

    def ryba(argument):
        # oczekujemy, że argument będzie liczbą naturalną
        for i in range(argument):
            print('ryba')

Użycie słowa kluczowego <code>return</code> spowoduje wyjście z pętli. Poprzez <code>return</code> możemy przekazać do reszty programu wartość z wnętrza funkcji. Taką wartość często zapisujemy w zmiennej po wywołaniu funkcji w innym miejscu programu.

    def suma_trzech(a, b, c):
        return a + b + c

    suma_a = suma_trzech(3, 6, 2)
    suma_b = suma_trzech(4, 1, 7)

### Napisy

<code>String</code> to tekstowy typ danych. Tutaj będziemy nazywali go napisem. Napis składa się z ciągu znaków. Znakami mogą być litery lub znaki interpunkcyjne, ale również cyfry.

W Pythonie napis deklarujemy, używając apostrofów  bądź cudzysłowów. 

    napis = 'James' 
    napis = "James" 
    napis = '''James''' 

Nie ma oddzielnego typu dla pojedynczego znaku. Pojedynczy znak to napis o długości równej 1. Napisy są indeksowane od 0 tak jak i listy. Do konkretnego znaku w danym napisie możemy odwołać się poprzez jego indeks. 

Przykładowo dla kodu <code>James = 'Lubie go'</code>, wywołanie <code>James[0]</code> zwróci literę 'L'. Wywołanie <code>James[2]</code> zwróci literę 'b'. 

Zainicjalizowany napis nie może być zmieniony. To znaczy, nie możemy zrobić czegoś takiego: <code>James[0]='z'</code>. Jeśli chcemy wprowadzić zmiany do napisu, musimy nadpisać aktualny napis innym napisem.

    napis = "pierwotny"
    napis = "nowy"

### Struktury danych

Algorytm to skończona lista kroków (instrukcji). Kroki te sprawdzają, kopiują, usuwają, czy w inny sposób manipulują danymi.
Struktury danych to sposoby na przechowywanie danych w pamięci komputera. Dzięki ich implementacjom w Pythonie możemy do całej kolekcji danych (a nie tylko pojedynczej zmiennej) odnosić się przy pomocy jednej nazwy. Istnieje bardzo wiele struktur danych, które różnią się oferowanymi funkcjonalnościami.

* Listy: elementy są uporządkowane i można je zmieniać. W liście mogą występować duplikaty.
* Krotki: elementy są uporządkowane i nie można ich zmieniać. W krotce mogą występować duplikaty.
* Zbiory: elementy są nieuporządkowane, nieindeksowane i nie można ich zmieniać. W zbiorze mogą występować duplikaty.
* Słowniki: elementy są nieuporządkowane, indeksowane i można je zmieniać. Wszystkie klucze w słowniku są unikalne. Wśród wartości mogą występować duplikaty.

#### Lista

List używamy, gdy chcemy mieć kilka wartości dostępnych pod jedną nazwą.

Aby znaleźć liczbę elementów listy, użyj: 
       
    len(lista)
       
Aby dodać element a na koniec listy, użyj:

    lista.append(a)

Aby dodać wszystkie elementy z lista2 na koniec lista1, użyj:

    lista1.extend(lista2)

Aby wstawić element a na pozycję i, użyj:

    lista.insert(i,a)

Aby usunąć pierwsze wystąpienie elementu a w liście, użyj:

    lista.remove(a)

Aby usunąć element z listy znajdujący się na pozycji i oraz zwrócić go jako wynik, użyj:

    lista.pop([i])

Aby znaleźć liczbę wystąpień elementu a w liście, użyj:

    lista.count(a)

Aby posortować listę, użyj:

    lista.sort()

Aby odwrócić kolejność elementów w liście, użyj:

    lista.reverse()

#### Krotka

Krotek zamiast list, używamy gdy:
* Liczy się szybkość.
* Chcemy zabezpieczyć dane przed nadpisaniem.

Aby znaleźć liczbę elementów krotki, użyj:

    len(krotka)

Aby dodać element a na koniec krotki, użyj:

    krotka = krotka + (a,)

Aby dodać wszystkie elementy z krotka2 na koniec krotka1, użyj:

    krotka1 = krotka1 + krotka2

Aby znaleźć indeks pierwszego wystąpienia elementu a w krotce, użyj:

    krotka.index(a)

Aby sprawdzić, czy element a występuje w krotce, użyj:

    a in krotka

Aby otrzymać wartość elementu z krotki znajdującego się na pozycji i, użyj:

    krotka[i]

Aby rozpakować krotkę składającą się z trzech elementów i zapisać je w trzech zmiennych, użyj:

    a, b, c = krotka

#### Zbiór

Zbiory są przydatne, gdy chcemy, by wszystkie elementy w kolekcji były unikalne. Dodatkowo dla zbiorów mamy zaimplementowane wiele przydatnych funkcji, pozwalających w prosty sposób pracować na kilku zbiorach jednocześnie.

Aby znaleźć liczbę elementów zbioru, użyj:

    len(zbior)

Aby dodać element a do zbioru, użyj:

    zbior.add(a)

Aby usunąć element a ze zbioru, użyj:

    zbior.remove(a)

Aby sprawdzić, czy element a występuje w zbiorze, użyj:

    a in zbior

Aby sprawdzić, czy zbiór zawiera w sobie wszystkie elementy zbioru zbior2, użyj:

    zbior.issuperset(zbior2)

Aby znaleźć część wspólną dwóch zbiorów, użyj:

    zbior.intersection(zbior2)

Aby znaleźć elementy zbioru zbior1, które nie są w zbiorze zbior2, użyj:

    zbior1.difference(zbior2)

#### Słownik

Słowniki przydatne są, gdy chcemy użyć innych indeksów niż numeryczne. Dodatkowo słowniki są mega szybkie.

Aby znaleźć liczbę elementów słownika, użyj:

    len(słownik)

Aby dodać element b do słownika i zapisać go pod kluczem a, użyj:

    słownik[a] = b

Aby usunąć element ze słownika pod kluczem a, użyj:

    del słownik[a]

Aby sprawdzić, czy klucz występuje w słowniku, użyj:

    a in słownik

Aby sprawdzić, czy wartość występuje w słowniku, użyj:

    b in słownik.values()

Aby wypisać klucze i wartości słownika, użyj:

    for klucz, wartość in słownik.items():
        print(klucz, wartość)

Aby klucze i wartości posortować wg kluczy, użyj:

    for klucz, wartość in sorted(słownik.items(), key=lambda x: x[0]):
        print(klucz, wartość)

Aby klucze i wartości posortować wg wartości, użyj:

    for klucz, wartość in sorted(słownik.items(), key=lambda x: x[1]):
        print(klucz, wartość)

### Enum

Typ wyliczeniowy enum pozwala na tworzenie zmiennych, które mogą przyjmować jedynie z góry określone wartości. Wartości te mają czytelne nazwy, a dodatkowo enum jest bardzo szybki i opłaca się go używać nawet w krytycznych miejscach programu.

    class Kolor(enum.Enum):
        ZIELONY = enum.auto()
        CZERWONY = enum.auto()
        NIEBIESKI = enum.auto()

    kolor_a = Kolor.ZIELONY
    kolor_b = Kolor.CZERWONY
    
    print(kolor_a.name)
    print(kolor_a.value)

    print(kolor_b.name)
    print(kolor_b.value)

### Liczby losowe

Nieraz w programie potrzebujemy użyć liczb losowych. Moduł <code>random</code> zawiera wiele przydatnych funkcji do losowania liczb całkowitych i zmiennoprzecinkowych.

- instrukcja <code>random.random()</code> wylosuje liczbę zmiennoprzecinkową z przedziału od 0 do 1.
- <code>random.uniform(a,b)</code> wylosuje liczbę zmiennoprzecinkową z przedziału od a do b.
- instrukcja <code>random.randint(a,b)</code> wylosuje liczbę całkowitą z przedziału od a do b.

Najprostszy przykład rozkładu prawdopodobieństwa to rozkład jednostajny. Dla jednostajnego rozkładu prawdopodobieństwa mamy stałą wartość gęstości prawdopodobieństwa na danym przedziale <code>[a,b]</code>. Poza tym przedziałem wartość gęstości prawdopodobieństwa wynosi 0. 

Dla rozkładu Gaussa wartości zbliżone do średniej mają znacznie większe prawdopodobieństwo wystąpienia niż te oddalone od średniej. Jeśli na jakąś wielkość wpływa dostatecznie wiele czynników, to rozkład prawdopodobieństwa będzie zbliżony do krzywej Gaussa. Dokładniej mówi o tym centralne twierdzenie graniczne. 

## Średniozaawansowane

Zaawansowane konstrukcje języka Python. Programowanie zorientowane obiektowo. Implementacja własnych struktur danych.

### Klasy i obiekty
### Referencje i mutacje
### Czyste funkcje i skutki uboczne
### Dziedziczenie i kompozycja
### Wyrażenia regularne
### Wyjątki
### Wątki
### Lambdy
### Data classes
### Generatory
### Iteratory

## Inżynieria oprogramowania

### Pomoc
### Moduły i pakiety
### Wersje Pythona

<code>Pyenv</code> używany jest do izolowania różnych wersji Pythona. Na przykład jeśli chcesz przetestować swój kod w Pythonie 2.5, 3.6 i 3.10, potrzebujesz łatwego sposobu na przełączanie się między nimi. <code>Pyenv</code> modyfikuje zmienną środowiskową PATH dodając do niej ścieżkę do specjalnego folderu <code>(pyenv root)/shims</code>. <code>Pyenv</code> ułatwia również proces pobierania i instalowania różnych wersji Pythona za pomocą polecenia <code>pyenv install</code>.

Linki:

* https://github.com/pyenv/pyenv
* https://github.com/pyenv-win/pyenv-win

### PIP i PyPI
### Środowisko wirtualne

Środowisko wirtualne to odizolowane od reszty systemu wersje bibliotek i pakietów Pythona. Instalując daną wersję pakietu w środowisku wirtualnym jest ona dostępna tylko w nim. Gdy usuwamy środowisko wirtualne wraz z nim znika również wszystko to co zostało zainstalowane w jęgo obrębie.

Popularnym narzędziem do tworzenia środowisk wirtualnych jest <code>virtualenv</code>. Narzędzie to tworzy specjalny folder o dowolnej nazwie (np. env/) oraz modyfikuje zmienną środowiskową PATH dodając do niej refernecje do podfolderu bin znajdującego się w utworzonym folderze (np. env/bin/). Wszystkie pakiety i biblioteki instalowane w środowisku wirtualnym wędrują do tego folderu.

Aby utworzyć środowisko wirtualne w aktualnym folderze, użyj:

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

<code>Pylint</code> to jeden z najpopularniejszych linterów Pythona. Daje nam trochę więcej wskazówek niż <code>Black</code>, który interesuje się jedynie formatowaniem. <code>Pylint</code> zwróci również uwagę na niepoprawne nazwy zmiennych (np. a lub bb), czy funkcje i klasy pozostawione bez komentarzy (docstrings). Dodatkowo wiele narzędzi do CI/CD (np. Team City, Github Actions) zintegrowało <code>Pylint</code> ze swoim interfejsem graficznym. Wskazówki od <code>Pylint</code> nie modyfikują naszego kodu automatycznie i będziemy musieli wprowadzić je ręcznie.

<code>Flake8</code> to kolejne świetne narzędzie do lintowania. Choć w działaniu podobny jest do <code>Pylint</code> to jego największą zaletą jest ogromna paleta pluginów tworzonych przez społeczność. Dzięki temu możemy otrzymać jeszcze więcej wskazówek jak poprawić nasz kod i jednocześnie mieć pełną kontrolę nad aspektami kodu, które są sprawdzane.


|                            | black | pylint | flake8 | 
|----------------------------|--------|--------|-------|
| automatyczna korekcja            |   ✔️   |   ❌   |   ❌  | 
| wskazówki do stylu     |   👷‍♂️   |   ✔️   |   👷‍♂️  |
| wyszukiwanie bugów             |   ❌   |   ✔️   |   👷‍♂️  | 
| wskazywanie zbyt złożonego kodu      |   ❌   |   👷‍♂️   |   ❌  |
| dostępność pluginów    |   ❌   |   ❌   |   ✔️  | 

Linki:

* https://www.python.org/dev/peps/pep-0008/
* https://www.python.org/dev/peps/pep-0257/
* https://github.com/psf/black
* https://github.com/PyCQA/pylint
* https://github.com/PyCQA/flake8
* https://github.com/myint/autoflake

### Debugowanie

Debuger to program, którego zadanie jest inspekcja stanu programu w trakcie wykonywanie. Możesz użyć debugera, aby zatrzymać wykonywanie programu, gdy w trakcie wykonywania osiągnięta zostanie określone przez ciebie miejsce w kodzie. Po zatrzymaniu programu debuger pokazuje aktualne wartości wszystkich zmiennych istniejących w danym punkcie programu. Dzięki temu możemy zweryfikować, czy nasze wyobrażenia o tym jak działa program mają potwierdzenie w rzeczywistości. 

Dwa główne zastosowania debugera:
- Wyszukiwanie przyczyn bugów w kodzie.
- Analiza działania programu przez zaznajamiających się z nim programistów.

Większość współczesnych środowisk programistycznych (IDE) ma wbudowany debuger. Graficzny interfejs użytkownika umożliwa sterowanie debugerem za pomocą myszy. Miejsca, w których debuger ma zatrzymać program zaznaczane są często za pomocą czerownej kropki, a wartości zmiennych wyświetlane są w specjalnym panelu.

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

1. Zacznijmy od tutoriali. Powinniśmy pokazać użytkownikowi naszego oprogramowania jak je zainstalować i uruchomić.
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
