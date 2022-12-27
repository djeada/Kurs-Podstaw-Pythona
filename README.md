# Kurs-Podstaw-Pythona
Kurs podstaw Pythona.

![Capture](https://user-images.githubusercontent.com/37275728/185895408-59e16b58-4468-4bf3-8444-929e3fa4cc3d.PNG)

## Spis Treści

<!--ts-->

  - [Podstawy](#Podstawy)
    - [Instalacja-w-systemie-Windows](#Instalacja-w-systemie-Windows)
    - [Interaktywna-konsola](#Interaktywna-konsola)
    - [Zmienne](#Zmienne)
    - [Warunki](#Warunki)
    - [Pętle](#Pętle)
    - [Pętle-zagnieżdżone](#Pętle-zagnieżdżone)
    - [Funkcje](#Funkcje)
    - [Napisy](#Napisy)
    - [Struktury-danych](#Struktury-danych)
    - [Enum](#Enum)
    - [Liczby-losowe](#Liczby-losowe)
  - [Średniozaawansowane](#Średniozaawansowane)
    - [Klasy-i-obiekty](#Klasy-i-obiekty)
    - [Referencje-i-kopiowanie](#Referencje-i-kopiowanie)
    - [Czyste-funkcje-i-skutki-uboczne](#Czyste-funkcje-i-skutki-uboczne)
    - [Dziedziczenie-i-kompozycja](#Dziedziczenie-i-kompozycja)
    - [Wyrażenia-regularne](#Wyrażenia-regularne)
    - [Wyjątki](#Wyjątki)
    - [Wątki](#Wątki)
    - [Procesy](#Procesy)
    - [Asyncio](#Asyncio)
    - [Lambdy](#Lambdy)
    - [Programowanie-funkcyjne](#Programowanie-funkcyjne)
    - [Klasy-danych](#Klasy-danych)
    - [Generatory](#Generatory)
    - [Iteratory](#Iteratory)
    - [Dekoratory](#Dekoratory)
    - [Serializacja](#Serializacja)
  - [Inżynieria-oprogramowania](#Inżynieria-oprogramowania)
    - [Moduły-i-pakiety](#Moduły-i-pakiety)
    - [Wersje-Pythona](#Wersje-Pythona)
    - [PIP-i-PyPI](#PIP-i-PyPI)
    - [Środowisko-wirtualne](#Środowisko-wirtualne)
    - [Dbanie-o-jakość-kodu-i-lintowanie](#Dbanie-o-jakość-kodu-i-lintowanie)
    - [Debugowanie](#Debugowanie)
    - [Testy-jednostkowe](#Testy-jednostkowe)
    - [Dokumentacja](#Dokumentacja)
    - [Pliki-wykonywalne-i-PyInstaller](#Pliki-wykonywalne-i-PyInstaller)
    - [Kod-bajtowy](#Kod-bajtowy)
  - [Python-w-praktyce](#Python-w-praktyce)
    - [Argumenty-linii-poleceń](#Argumenty-linii-poleceń)
    - [Praca-z-plikami-i-folderami](#Praca-z-plikami-i-folderami)
    - [Pandas-i-csv](#Pandas-i-csv)
    - [Praca-z-plikami-PDF](#Praca-z-plikami-PDF)
    - [Informacje-o-systemie-operacyjnym](#Informacje-o-systemie-operacyjnym)
    - [HTTP-i-prosty-serwer](#HTTP-i-prosty-serwer)
    - [API-wraz-z-FastAPI](#API-wraz-z-FastAPI)
    - [Bazy-danych-z-SQLite](#Bazy-danych-z-SQLite)
    - [Tkinter](#Tkinter)
    - [Logi](#Logi)
  - [Dodatkowe-materiały](#Dodatkowe-materiały)

<!--te-->

## Podstawy

Język Python jest językiem programowania ogólnego przeznaczenia, charakteryzującym się prostą składnią i dużą elastycznością. Jest szeroko stosowany w różnych dziedzinach, od nauk ścisłych po tworzenie aplikacji internetowych. W niniejszym artykule skupimy się na fundamentach języka, a także na budowaniu małych programów i pracy z strukturami danych.

### Instalacja w systemie Windows
Aby rozpocząć przygodę z Pythonem, należy najpierw przygotować sobie odpowiednie środowisko. W tym celu najlepiej pobrać i zainstalować oprogramowanie na swoim komputerze.

Aby zainstalować Pythona w systemie Windows, musiszć wykonać następujące kroki:

1. Przejdź na stronę internetową <a href="https://www.python.org/downloads/">https://www.python.org/downloads/</a>.
1. W sekcji "Python Releases for Windows" znajdź i kliknij link do najnowszej stabilnej wersji Pythona dla systemu Windows.
1. Po pobraniu instalatora, uruchom go i postępuj według podanych instrukcji.
1. Podczas instalacji, upewnij się, że zaznaczyłeś opcję *Add Python to PATH*, dzięki której będziesz mógł uruchamiać Pythona z dowolnego miejsca w systemie.
1. Po zakończeniu instalacji, możesz uruchomić Python, wpisując w wierszu poleceń polecenie *python*.

### Interaktywna konsola

Konsola Pythona to interaktywne środowisko, w którym można wpisywać i wykonywać pojedyncze polecenia. Aby otworzyć konsolę, należy wpisać polecenie *python* w wierszu poleceń. Wówczas zostanie wyświetlona informacja o wersji Pythona dostępnej w systemie.

    >>> python
    python 2.7.13 (default, Sep  2 2019, 20:42:59)

Z poziomu konsoli można wykonywać wszystkie dostępne polecenia Pythona. Po wpisaniu polecenia i naciśnięciu klawisza *Enter*, zostanie ono natychmiast wykonane i zwrócony ewentualny wynik (nie wszystkie komendy zwracają wynik). Polecenie <code>help</code> pozwala uzyskać informacje o dostępnych komendach i ich możliwych parametrach. Można również wywoływać funkcje z bibliotek, takich jak np. <code>math.pi</code>, która zwraca stałą pi.

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

Zmienne stanowią podstawę każdego języka programowania. Służą do przechowywania różnych rodzajów danych, takich jak liczby, napisy czy wartości logiczne. Każda zmienna ma swoją nazwę, poprzez którą odwołujemy się do niej w programie.

W Pythonie istnieją różne typy zmiennych, które odpowiadają rodzajowi przechowywanych danych. Są to m.in.
- Liczby całkowite (*int*) 
- Liczby zmiennoprzecinkowe (*float*) 
- Napisy (*string*) 
- Typ logiczny (*bool*) 

Nazwa zmiennej może składać się z liter i cyfr, ale nie może zaczynać się od cyfry. Python nie ogranicza długości nazw. Dobrym zwyczajem jest nadawanie zmiennym nazw odpowiadających ich roli w programie. Dzięki temu nasz kod staje się bardziej czytelny i łatwiejszy w utrzymaniu.

Czy wiesz jaka liczba zostanie wypisana na konsoli w poniższym przykładzie?

    a = 3
    b = a
    b = 5
    print(a) # ???

### Warunki

Typ logiczny (bool) może przyjmować jedną z dwóch wartości: <code>True</code> lub <code>False</code>. Typ logiczny ma istotne znaczenie dla instrukcji warunkowej.

Prosta zmienna typu logicznego:

    wiek = 18 # zmienna typu int
    warunek = wiek > 18 # zmienna typu bool
    
Oto tabela z porównaniami dostępnymi w języku Python:

| Symbol | Opis |
| ------ | ---- |
| >	| większy niż |
| >=	| większy lub równy |
| <	| mniejszy niż |
| <=	| mniejszy lub równy |
| ==	| równy |
| !=	| różny |

Początkujący programiści często mylą pojedynczy znak równości (<code>=</code>) z podwójnym znakiem równości (<code>==</code>).

- <code>x = 5</code> oznacza przypisanie wartości 5 do zmiennej x.
- <code>x == 5</code> oznacza sprawdzenie, czy zmienna x jest równa 5.

Instrukcja warunkowa (if-else) ma następującą postać:

    if warunek:
        kod
    else:
        kod

Część kodu umieszczona w pierwszym wcięciu po instrukcji warunkowej <code>if</code> zostanie wykonana jedynie, gdy warunek zostanie oceniony na prawdziwy. Gdy warunek nie jest spełniony, ta część kodu zostanie całkowicie pominięta, a zamiast niej wykonany zostanie kod umieszczony w drugim wcięciu (pod
instrukcjami sterującymi.

Operatory logiczne służą do łączenia warunków. W Pythonie mamy do dyspozycji trzy operatory logiczne: <code>and</code>, <code>or</code> i <code>not</code>:

    <code>and</code> – aby wyrażenie było prawdziwe, oba warunki muszą być prawdziwe.
    <code>or</code> – aby wyrażenie było prawdziwe, tylko jeden warunek musi być prawdziwy.
    <code>not</code> – zaprzeczenie wyrażenia.

Na przykład, wyrażenie <code>a != 0 and b == 5</code> będzie prawdziwe, jeśli oba warunki są spełnione, tzn. jeśli a jest różne od 0 i jednocześnie b jest równe 5.

Natomiast wyrażenie <code>x % 2 == 0 or x % 7 == 0</code> będzie prawdziwe, jeśli jeden z warunków jest spełniony, tzn. jeśli x jest podzielne przez 2 lub x jest podzielne przez 7.

Być może zastanawiasz się, co zostanie wypisane na konsoli w poniższym przykładzie:
    
    odpowiedz = "TAK"
    print(odpowiedz == "tak" or "TAK")

Wyjaśnienie: operator <code>or</code> zwraca pierwszą wartość prawdziwą, jeśli taka istnieje, w przeciwnym razie zwraca drugą wartość. W tym przypadku pierwszy warunek jest fałszywy, ale drugi jest prawdziwy (bo "TAK" jest różne od fałszu). Z tego powodu całe wyrażenie zwraca drugi warunek, czyli wartość "TAK".

### Pętle

Pętle wraz z instrukcjami warunkowymi są podstawą wszystkich języków programowania. Pętle pozwalają na wielokrotne wykonanie pojedynczej instrukcji lub całego bloku instrukcji. Oprócz bloku instrukcji, każda pętla ma również warunek zakończenia. Pętla powtarza blok instrukcji, dopóki warunek kończący pętlę nie zostanie spełniony. W Pythonie mamy dwie pętle: <code>For</code> i <code>While</code>.

#### For
Pętla <code>For</code> umożliwia wielokrotne wykonanie bloku instrukcji dla każdego elementu z danej kolekcji. Kolekcją może być np. lista, zbiór lub krotka. W przypadku pętli <code>For</code> mamy pewność, że blok instrukcji zostanie wykonany określoną ilość razy, równą liczbie elementów w kolekcji. Pętla <code>For</code> ogólnie ma postać:

    for element in kolekcja: 
        kod

Na początek do tworzenia pętli będziemy używać funkcji range(). Funkcja ta może przyjmować jeden, dwa lub trzy parametry.

1. <code>range(10)</code> tworzy ciąg (0, 1, 2, 3, 4, 5, 6, 7, 8, 9), więc pętla: <code>for x in range(10)</code> zostanie wykonana 10 razy.
1. <code>range(5, 12)</code> tworzy ciąg (5, 6, 7, 8, 9, 10, 11), więc pętla: <code>for x in range(5, 12)</code> zostanie wykonana 7 razy.
1. <code>range(0, 50, 10)</code> tworzy ciąg (0, 10, 20, 30, 40), więc pętla: <code>for x in range(0, 50, 10)</code> zostanie wykonana 5 razy.

Przykład użycia pętli <code>For</code> z listą:

    dni_tygodnia = ['Poniedziałek', 'Wtorek', 'Środa', 'Czwartek', 'Piątek', 'Sobota', 'Niedziela']
    for dzien in dni_tygodnia:
        print(dzien)

Wynikiem wykonania powyższego kodu będzie wypisanie na konsoli nazw wszystkich dni tygodnia.

#### While

Pętla <code>While</code> jest podobna w działaniu do pętli <code>For</code>, ale istnieją również istotne różnice między obiema konstrukcjami. W przypadku pętli <code>While</code> warunek zakończenia pętli jest sprawdzane przed każdym przejściem do kolejnej iteracji. Jeśli warunek nie jest spełniony, pętla zostaje zakończona. Dzięki temu pętla <code>While</code> może być używana do wykonywania pewnych instrukcji w nieskończoność (jeśli warunek kończący pętlę zawsze jest prawdziwy). 

Pętla <code>While</code> ma postać:

    while warunek konczacy petle: 
         kod

Poniżej przedstawiony został prosty przykład użycia pętli <code>While</code>:

    licznik = 0
    while licznik < 5:
        print(licznik)
        licznik += 1

W powyższym przykładzie pętla <code>While</code> będzie wykonywana do momentu, aż zmienna licznik będzie mniejsza od 5. W każdym obiegu pętli wyświetlana jest aktualna wartość zmiennej licznik, a następnie jej wartość zostaje zwiększona o 1.

W rezultacie, na konsoli zostaną wyświetlone kolejno liczby od 0 do 4.

#### Polecenia break i continue

Instrukcja <code>break</code> służy do natychmiastowego przerwania działania pętli. Jeśli jest ona wywołana wewnątrz pętli, natychmiast przechodzi do kodu znajdującego się po pętli. Może być ona używana w połączeniu z instrukcjami warunkowymi, aby natychmiastowo zakończyć działanie pętli.

Przykład:

    for i in range(10):
        if i == 5:
            break
        print(i)

W tym przykładzie pętla będzie wykonywana dla wartości zmiennej *i* od 0 do 4, a następnie zostanie przerwana przez instrukcję <code>break</code>.

Instrukcja <code>continue</code> jest używana w pętlach i powoduje przejście do następnego obiegu pętli. Wszystkie instrukcje umieszczone poniżej instrukcji <code>continue</code> w bloku pętli nie zostaną wykonane po jej wywołaniu. Przykład użycia instrukcji <code>continue</code>:

    for i in range(10):
        if i % 2 == 0:  # jeśli i jest podzielne przez 2
            continue  # przejdź do następnego obiegu pętli
        print(i)  # wypisz i

W powyższym przykładzie pętla zostanie wykonana dla wszystkich liczb z zakresu od 0 do 9, ale zostaną one wyświetlone jedynie w przypadku, gdy są nieparzyste. W rezultacie na konsoli zostaną wypisane liczby: 1, 3, 5, 7, 9.

#### Pętle zagnieżdżone

Podobnie jak możemy zagnieżdżać instrukcje warunkowe, możemy również zagnieżdżać pętle. Pętle zagnieżdżone to pętle znajdujące się w ciele innych pętli. 

Istnieją dwie zasady zagnieżdżania pętli:

1. pętla zewnętrzna pilnuje wysokości,
1. pętla wewnętrzna pilnuje szerokości.

        for y in range(10): # wysokosc
            for x in range(5): # szerokosc
                kod

Pętla zewnętrzna ustawi nas w odpowiednim rzędzie, a pętla wewnętrzna na odpowiednim miejscu w danym rzędzie. Przykładowo, jeśli idziemy do sali kinowej i nasz bilet mówi, że przysługuje nam miejsce numer 5 w rzędzie numer 2, pętle zewnętrzna ustawi nas w odpowiednim rzędzie, a pętla wewnętrzna na odpowiednim miejscu.

W celu lepszego zobrazowania działania takiej konstrukcji posłużymy się graficznymi przykładami i będziemy wypisywać na konsoli różne kształty. Przykład zagnieżdżonej pętli z kształtami może być zapisany w następujący sposób:

    for i in range(5):
        for j in range(5):
            print("*", end="")
        print()

W wyniku wykonania tego kodu zostanie wypisany na konsoli prostokąt z gwiazdek:

    *****
    *****
    *****
    *****
    *****

Możemy również użyć zagnieżdżonych pętli, aby narysować bardziej skomplikowane kształty, takie jak trójkąty lub choinkę.

    for i in range(5):
        for j in range(i+1):
            print("*", end="")
        print()

W wyniku wykonania tego kodu zostanie wypisany na konsoli trójkąt z gwiazdek:

    *
    **
    ***
    ****
    *****
    
## Funkcje

Funkcje są blokami instrukcji zamkniętymi pod jedną nazwą i pozwalającymi na kontrolowanie z zewnątrz poprzez przekazywanie argumentów. Definicja funkcji polega na określeniu, które instrukcje należą do ciała funkcji, ile argumentów oczekuje funkcja oraz jaką nazwą będzie ona wywoływana w innych miejscach kodu. Definicja sama w sobie nie uruchamia jeszcze żadnych instrukcji - potrzebne jest użycie nazwy funkcji wraz z wartościami argumentów w innym miejscu kodu, aby instrukcje zostały wykonane. Funkcje mają następującą postać:

    def nazwa_funkcji(argumenty):
        kod # cialo funkcji

Ciało funkcji może być dowolnie rozbudowane, ale zaleca się dzielenie większych funkcji na mniejsze, które mają jasno określony cel. W ten sposób zmniejsza się złożoność kodu i ułatwia jego czytanie.

Zdefiniowaną funkcję wywołujemy w kodzie poprzez jej nazwę. Przykład:

    # w tym miejscu definiujemy funkcję
    def ryba():
       print('rybka')

    # w tym miejscu wywołujemy funkcję
    ryba()

Funkcje mogą mieć dowolną ilość argumentów - możliwe jest stworzenie funkcji bez argumentów lub funkcji z 10 argumentami. Przykład:

    def ryba(argument):
        # oczekujemy, że argument będzie liczbą naturalną
        for i in range(argument):
            print('ryba')

Słowo kluczowe <code>return</code> powoduje opuszczenie funkcji (instrukcje umieszczone poniżej nie są wykonywane). <code>return</code> pozwala również na przekazanie wartości z wnętrza funkcji do reszty programu. Taka wartość po wywołaniu funkcji jest często zapisywana w zmiennej w innym miejscu programu. Na przykład:

    def suma_trzech(a, b, c):
        return a + b + c

    suma_a = suma_trzech(3, 6, 2)
    suma_b = suma_trzech(4, 1, 7)

    print(suma_a)  # wyświetli 11
    print(suma_b)  # wyświetli 12

Możemy również zdefiniować funkcję z domyślnymi argumentami, które zostaną użyte, jeśli nie zostaną przekazane żadne inne. Domyślne argumenty muszą być umieszczone po argumentach obowiązkowych, a ich ilość nie może przekroczyć ilości argumentów obowiązkowych. Przykład:

    def suma_trzech(a, b, c=0):
        return a + b + c

    suma_a = suma_trzech(3, 6)  # a + b + c = 3 + 6 + 0 = 9
    suma_b = suma_trzech(4, 1, 7)  # a + b + c = 4 + 1 + 7 = 12

    print(suma_a)  # wyświetli 9
    print(suma_b)  # wyświetli 12

Istnieje też sposób na zdefiniowanie funkcji z nieograniczoną liczbą argumentów obowiązkowych, przy czym nie możemy ich użyć w połączeniu z argumentami domyślnymi. Przykład:

    def suma_n(*args):
        return sum(args)

    suma_a = suma_n(1, 2, 3, 4)  # 1 + 2 + 3 + 4 = 10
    suma_b = suma_n(10, 20, 30)  # 10 + 20 + 30 = 60

    print(suma_a)  # wyświetli 10
    print(suma_b)  # wyświetli 60
    
Ostatni sposób przkazywania arugmentów, to argumenty nazwane, które są przekazywane w postaci słownika. Przykład:

    def suma_n(**kwargs):
        return sum(kwargs.values())

    suma_a = suma_n(a=1, b=2, c=3, d=4)  # 1 + 2 + 3 + 4


### Napisy

Napisy to typ danych tekstowych, które składają się z ciągu znaków. Nnapisy mogą być używane do wielu różnych celów, takich jak:

* Wypisywanie tekstu na ekranie.
* Przechowywanie danych tekstowych w programie.
* Przetwarzanie i modyfikowanie tekstu.

Możemy deklarować je używając apostrofów lub cudzysłowów. 

    napis = 'James' 
    napis = "James" 
    napis = '''James''' 

Napisy są indeksowane, co oznacza, że możemy odwołać się do konkretnego znaku w napisie za pomocą jego indeksu. Możemy również wyodrębnić fragment napisu, zwany składnią wycinka (slice).

    napis = "James" 
    print(napis[1]) # a
    print(napis[2:5]) # mes

Napisy są niemodyfikowalne, co oznacza, że nie możemy bezpośrednio zmienić poszczególnych znaków w napisie. Możemy jednak tworzyć nowe napisy na podstawie istniejących napisów, zmieniając ich zawartość lub łącząc je ze sobą.

    napis = "pierwotny"
    napis = "nowy"
    
f-string to sposób formatowania napisów w Pythonie, który pozwala na wstawienie do napisu wartości zmiennych wewnątrz tekstu. W celu użycia f-string, należy przed cudzysłowami postawić literkę "f", a w odpowiednim miejscu między nawiasami klamrowymi nazwę zmiennej, której chcemy użyć.

Przykład:

    imie = "Jan"
    wiek = 30

    napis = f"Mam na imię {imie} i mam {wiek} lat."
    print(napis)

W powyższym przykładzie zmienna "imie" zostanie zamieniona na "Jan", a zmienna "wiek" na "30". Ostatecznie w wyniku wywołania print(napis) na ekranie pojawi się napis "Mam na imię Jan i mam 30 lat.".

f-string pozwala również na użycie wyrażeń arytmetycznych w napisach.

Przykład:

    a = 10
    b = 20

    napis = f"Suma a i b wynosi {a + b}."
    print(napis)

W powyższym przykładzie zostanie wyświetlony napis "Suma a i b wynosi 30.".

### Struktury danych

Mamy do dyspozycji kilka różnych sposobów przechowywania danych. Te sposoby to tzw. struktury danych. Są to narzędzia, dzięki którym możemy zbierać i przechowywać duże ilości danych w sposób uporządkowany, co ułatwia nam pracę z tymi danymi.

Oto najpopularniejsze sturktury danych:

* Listy: listy to uporządkowane kolekcje elementów, które mogą być dowolnego typu. Możemy do nich dodawać i usuwać elementy, a także zmieniać ich kolejność. W liście mogą występować duplikaty.
* Krotki: krotki to podobne do list struktury, ale są one niezmienne. Raz utworzona krotka nie może być zmieniona. W krotkach również mogą występować duplikaty.
* Zbiory: zbiory to nieuporządkowane kolekcje elementów, w których nie mogą występować duplikaty. Zbiory są szczególnie przydatne, gdy intersują nas jedynie unikalne wartości.
duplikaty.
* Słowniki: słowniki to indeksowane kolekcje par klucz-wartość. Wszystkie klucze w słowniku muszą być unikalne, natomiast wartości mogą być duplikatami. Słowniki są bardzo przydatne do przechowywania danych w formie tabeli.

Oczywiście, istnieją również inne struktury danych ale te wymienione są najczęściej używane i najważniejsze dla początkujących.

#### Lista

Lista jest strukturą danych służącą do przechowywania kilku wartości pod jedną nazwą.

Przykład listy złożonej z kilku liczb całkowitych:

    lista = [3, 2, 3, 9, 10]
    
Elementy listy nie muszą być tego samego typu:

    lista = ['a', True, 0.3]

Aby poznać liczbę elementów listy, należy użyć funkcji `len`:

    n = len(lista)
       
Aby dodać element a na końcu listy, użyj metody `append`:

    lista.append(a)

Aby dodać wszystkie elementy z listy lista2 na końcu listy lista1, użyj metody `extend`:

    lista1.extend(lista2)

Aby wstawić element a na pozycję i, użyj metody `insert`:

    lista.insert(i,a)

Aby usunąć pierwsze wystąpienie elementu a z listy, użyj metody `remove`:

    lista.remove(a)

Aby usunąć element z listy znajdujący się na pozycji i oraz zwrócić go jako wynik, użyj metody `pop`:

    element = lista.pop([i])

Aby znaleźć liczbę wystąpień elementu a w liście, użyj metody `count`:

    licznik = lista.count(a)

Aby posortować listę, użyj metody `sort`:

    lista.sort()

Aby odwrócić kolejność elementów w liście, użyj metody `reverse`:

    lista.reverse()

Aby przy pomocy pętli przejść przez elementy listy, użyj słowa kluczowego `for`:

    for element in lista: 
        print(element)
        
Aby otrzymać element i indeks, użyj funkcji `enumerate`:

     for indeks, element in enumerate(lista): 
        print(f'{indeks}: {element}')

Aby przy pomocy pętli przejść przez elementy dwóch list równej długości, użyj funckji `zip`:

     for elem_a, elem_b in zip(lista_a, lista_b): 
        print(f'element a: {elem_a}; element b: {elem_b}')

#### Krotka

Krotka to struktura danych, podobna do listy, ale niezmienna. To znaczy, że po utworzeniu krotki nie możemy jej zmodyfikować, np. dodając do niej nowe elementy czy usuwając już istniejące.

Krotek zamiast list, używamy gdy:
* Liczy się szybkość.
* Chcemy zabezpieczyć dane przed nadpisaniem.

Przykład krotki składającej się z kilku liczb całkowitych:

    krotka = (3, 2, 3, 9, 10)

Elementy krotki nie muszą być tego samego typu:

    krotka = ('a', True, 0.3)

Aby rozpakować krotkę składającą się z trzech elementów i zapisać je w trzech zmiennych, użyj:

    a, b, c = krotka

Aby znaleźć liczbę elementów krotki, użyj:

    len(krotka)

Aby przy pomocy pętli przejść przez elementy krotki, użyj:

    for element in krotka: 
        print(element)

Aby otrzymać element i indeks, użyj funkcji `enumerate`:

    for indeks, element in enumerate(krotka): 
        print(f'{indeks}: {element}')

Aby przy pomocy pętli przejść przez elementy dwóch krotek równej długości, użyj funckji `zip`:

    for elem_a, elem_b in zip(krotka_a, krotka_b): 
        print(f'element a: {elem_a}; element b: {elem_b}')

#### Zbiór

Zbiór (ang. set) to nieuporządkowana kolekcja unikalnych elementów. Zbiory są zazwyczaj używane do eliminowania duplikatów lub do testowania przynależności elementu do kolekcji.

Aby utworzyć pusty zbiór, użyj:

    zbior = set()

Aby utworzyć zbiór z elementów podanych jako argumenty, użyj:

    zbior = set([element1, element2, element3])

Aby utworzyć zbiór z elementów występujących w iterowalnym obiekcie (np. liście), użyj:

    zbior = set(iterowalny_obiekt)

Aby sprawdzić, czy element jest w zbiorze, użyj:

    element in zbior

Aby dodać element do zbioru, użyj:

    zbior.add(element)

Aby usunąć element ze zbioru, użyj:

    zbior.remove(element)

Aby usunąć element ze zbioru, jeśli istnieje, bez generowania błędu, użyj:

    zbior.discard(element)

Aby usunąć losowy element ze zbioru, użyj:

    zbior.pop()

Aby usunąć wszystkie elementy ze zbioru, użyj:

    zbior.clear()

Aby znaleźć liczbę elementów w zbiorze, użyj:

    len(zbior)

Aby złączyć zbiory, użyj operatora `|`:

    zbior1 | zbior2

Aby wyświetlić elementy wspólne dla dwóch zbiorów, użyj operatora `&`:

    zbior1 & zbior2

Aby wyświetlić elementy występujące w jednym zbiorze, ale nie w drugim, użyj operatora `^`:

    zbior1 ^ zbior2

Aby wyświetlić elementy z pierwszego zbioru, ale nie z drugiego, użyj operatora `-`:

    zbior1 - zbior2

Aby sprawdzić, czy zbiór jest podzbiorem innego zbioru, użyj operatora `<=`:

    zbior1 <= zbior2

#### Słownik
Słownik używamy, gdy chcemy mieć kilka wartości dostępnych pod różnymi nazwami (kluczami). Słownik jest nieuporządkowany i indeksowany.

W słowniku można używać jako kluczy dowolnych typów danych, które są niemutowalne (tj. nie mogą być zmieniane). Do niemutowalnych typów danych w Pythonie zaliczają się:

* liczby całkowite (int)
* liczby zmiennoprzecinkowe (float)
* napisy (str)
* krotki (tuple)

Nie można natomiast używać jako kluczy mutowalnych typów danych, takich jak listy, zbiory lub słowniki, ponieważ nie spełniają one wymogu niemutowalności.

Przykłady poprawnych kluczy:

* liczba całkowita: `slownik[42]`
* napis: `slownik['klucz']`
* krotka: `slownik[(1, 2, 3)]`

Przykłady niepoprawnych kluczy:

* lista: `slownik[[1, 2, 3]]`
* zbiór: `slownik{1, 2, 3}`
* słownik: `slownik{'klucz': 'wartosc'}`

Przykład słownika zawierającego kilka par klucz-wartość:

    slownik = {'klucz1': 3, 'klucz2': 2, 'klucz3': 3}

Elementy słownika nie muszą być tego samego typu:

    slownik = {'klucz1': 'a', 'klucz2': True, 'klucz3': 0.3}

Aby znaleźć liczbę elementów słownika, użyj:

    len(slownik)

Aby dodać element a pod kluczem 'klucz4', użyj:

    slownik['klucz4'] = a

Aby zmienić wartość pod kluczem 'klucz4', użyj:

    slownik['klucz4'] = nowa_wartosc

Aby usunąć element pod kluczem 'klucz4', użyj:

    del slownik['klucz4']

Aby sprawdzić czy klucz 'klucz4' istnieje w słowniku, użyj:

    'klucz4' in slownik

Aby przy pomocy pętli przejść przez elementy słownika, użyj:

    for klucz, wartosc in slownik.items(): 
        print(f'{klucz}: {wartosc}')
    
Aby przy pomocy pętli przejść tylko przez klucze słownika, użyj:

    for klucz in slownik: 
        print(klucz)

Aby przy pomocy pętli przejść tylko przez wartości słownika, użyj:

    for wartosc in slownik.values(): 
        print(wartosc)

### Enum

Enum (od słowa enumerate - numerować) to specjalny typ danych, który pozwala na tworzenie stałych symbolicznych nazw dla wartości. W przeciwieństwie do zwykłych stałych, wartości Enumów są obiektami, a nie prostymi wartościami. Enum jest szczególnie przydatny, gdy chcemy przypisać nazwy symboliczne do wartości liczbowych.

Wewnątrz definicji klasy Enum tworzymy atrybuty klasy, które będą reprezentować nasze stałe symboliczne. Wartości atrybutów są automatycznie przypisane do kolejnych liczb całkowitych, począwszy od 1. Możemy również przypisać im jawnie określoną wartość.

Przykład definicji Enum dla kolorów:

    class Kolor(enum.Enum):
        ZIELONY = enum.auto()
        CZERWONY = enum.auto()
        NIEBIESKI = enum.auto()

    kolor_a = Kolor.ZIELONY
    kolor_b = Kolor.CZERWONY
    
    print(kolor_a.name) # ZIELONY
    print(kolor_a.value) # 1

    print(kolor_b.name) # CZERWONY
    print(kolor_b.value) # 2

### Liczby losowe

Liczby losowe są często potrzebne w programach, gdyż umożliwiają symulację różnych zjawisk. W Pythonie do generowania liczb losowych można użyć modułu <code>random</code>. Zawiera on wiele przydatnych funkcji, takich jak <code>random.random()</code> czy <code>random.uniform(a,b)</code>, które pozwalają na wylosowanie liczby zmiennoprzecinkowej z odpowiedniego przedziału. Możliwe jest również losowanie liczb całkowitych za pomocą funkcji <code>random.randint(a,b)</code>.

- <code>random.random()</code> wylosuje liczbę zmiennoprzecinkową z przedziału od *0* do *1*.
- <code>random.uniform(a,b)</code> wylosuje liczbę zmiennoprzecinkową z przedziału od *a* do *b*.
- <code>random.randint(a,b)</code> wylosuje liczbę całkowitą z przedziału od *a* do *b*.

Rozkład prawdopodobieństwa opisuje, jakie wartości są bardziej prawdopodobne, a jakie mniej prawdopodobne w losowaniu. Najprostszym przykładem rozkładu prawdopodobieństwa jest rozkład jednostajny, gdzie prawdopodobieństwo wystąpienia dowolnej wartości w przedziale `[a,b]` jest stałe. Wartość gęstości prawdopodobieństwa poza tym przedziałem wynosi 0.

Innym rodzajem rozkładu jest rozkład Gaussa, gdzie wartości zbliżone do średniej mają znacznie większe prawdopodobieństwo wystąpienia niż te oddalone od średniej. Wartości tego rodzaju rozkładu są często wykorzystywane w symulacjach, gdyż przy wpływie wielu czynników rozkład prawdopodobieństwa jest zazwyczaj zbliżony do krzywej Gaussa, co opisuje centralne twierdzenie graniczne."

- `random.gauss(mu, sigma)` - losuje liczbę z rozkładu normalnego o średniej `mu` i odchyleniu standardowym `sigma`.
- `random.expovariate(lambd)` - losuje liczbę z rozkładu wykładniczego o parametrze `lambd`.
- `random.weibullvariate(alpha, beta)` - losuje liczbę z rozkładu Weibulla o parametrach `alpha` i `beta`.
- `random.vonmisesvariate(mu, kappa)` - losuje liczbę z rozkładu von Misesa o parametrach `mu` i `kappa`.

Przykład użycia:

    import random

    # losowanie liczb z rozkładu normalnego o średniej 0 i odchyleniu standardowym 1
    samples = [random.gauss(0, 1) for _ in range(10)]
    print(samples)

    # losowanie liczb z rozkładu wykładniczego o parametrze 0.5
    samples = [random.expovariate(0.5) for _ in range(10)]
    print(samples)

## Średniozaawansowane

Ten artykuł jest skierowany do osób, które już zdobyły podstawowe umiejętności w programowaniu w języku Python. Omawiane zagadnienia obejmują bardziej zaawansowane tematy, takie jak klasy i programowanie obiektowe, tworzenie własnych struktur danych, programowanie funkcyjne oraz mechanizmy takie jak wątki, wyjątki, iteratory, generatory i dekoratory.

### Klasy i obiekty
Klasa to abstrakcyjny model, który definiuje jakiś zestaw cech i zachowań. Obiekt to konkretna instancja klasy. Możemy tworzyć dowolne klasy, niemniej jednak należy zastanowić się nad tym, jakie dane najlepiej byłoby trzymać razem pod jednym pojemnikiem oraz jakie funkcje mogą być przydatne do pracy z tymi danymi.

Przykład:

    class Osoba:
        def __init__(self, imie, nazwisko):
            self.imie = imie
            self.nazwisko = nazwisko

        def przedstaw_sie(self):
            print("Cześć, jestem " + self.imie + " " + self.nazwisko)

    osoba = Osoba("Jan", "Kowalski")    # kazdy obiekt ma niezalezne wartosci zmiennych
    inna_osoba = Osoba("Adam", "Nowak") # obiket inna_osoba jest niezalezny od obiektu osoba 
    osoba.przedstaw_sie()
    inna_osoba.przedstaw_sie()

W powyższym przykładzie tworzymy klasę Osoba, która posiada dwa pola danych: imie i nazwisko. Klasa ta zawiera również funkcję przedstaw_sie, która wyświetla komunikat z imieniem i nazwiskiem osoby. Następnie tworzymy dwa obiekty klasy Osoba i wywołujemy dla nich metodę przedstaw_sie.

#### Dostęp do zmiennych w obiektach

W programowaniu obiektowym, zmienne przechowywane są w obiektach. Aby uzyskać dostęp do tych zmiennych, należy podać nazwę obiektu, następnie kropkę i nazwę zmiennej, którą chcemy odczytać.

    nazwa_obiektu.nazwa_zmiennej
    
Możliwe jest również modyfikowanie wartości tych zmiennych tak, jak w przypadku zwykłych zmiennych. 

    osoba = Osoba("Jan", "Kowalski")
    print(osoba.imie) # Zostanie wyswietlone Jan
    osoba.imie = "Adam"
    print(osoba.imie) # Zostanie wyswietlone Adam

Możemy również użyć dekoratorów `@property` i `@nazwa_zmiennej.setter`, aby wywoływać funkcje przy odczycie lub modyfikacji wartości zmiennych przechowywanych w obiektach.

    class Osoba:
        def __init__(self, imie, nazwisko):
            self._imie = imie          # utarlo sie ze nazwy zmiennych dla ktorych zdefiniowane jest @property 
            self._nazwisko = nazwisko  # oraz odpowiadajacy setter zaczynaja sie od podkreslnika

    @property
    def imie(self):
      print('Ktos probuje odczytac imie')
      return self._imie

    @imie.setter
    def imie(self, nowa_wartosc):
       print('Ktos modyfikuje imie')
       self._imie = nowa_wartosc

Klasa Osoba posiada dwa atrybuty - imie oraz nazwisko. Zostały one oznaczone jako prywatne, poprzez dodanie podkreślnika na początku nazwy. Służy to do oznaczenia, że te atrybuty nie powinny być bezpośrednio modyfikowane lub odczytywane przez użytkownika klasy, lecz powinny być dostępne tylko poprzez odpowiednie metody.

Za pomocą dekoratorów `@property` oraz `@imie.setter` zostały zdefiniowane metody do odczytu oraz modyfikacji atrybutu imie. W momencie próby odczytu wartości atrybutu imie zostanie wyświetlony komunikat "Ktoś próbuje odczytać imię" oraz zostanie zwrócona jego wartość. Podobnie, w momencie próby modyfikacji atrybutu imie zostanie wyświetlony komunikat "Ktoś modyfikuje imię" oraz zostanie zmieniona jego wartość.

#### Pola i metody statyczne

Pola i metody statyczne są używane w programowaniu obiektowym, ale nie należą one do konkretnych obiektów - należą do całej klasy. Pola statyczne to wszystkie pola zdefiniowane w klasie, natomiast metody statyczne są tworzone za pomocą dekoratora `@staticmethod`. Dostęp do pól i metod statycznych możliwy jest zarówno poprzez nazwę klasy, jak i nazwę obiektu klasy.

    class Czlowiek:
      liczba_glow = 1

      @staticmethod
      def wyswietl_glowy():
        print(f'Liczba glow: {Czlowiek.liczba_glow}')

    Czlowiek.wyswietl_glowy() # Liczba glow: 1

    przykladowy_czlowiek = Czlowiek()
    przykladowy_czlowiek.wyswietl_glowy() # Liczba glow: 1

Metody klasowe to rozszerzenie metod statycznych - są tworzone za pomocą dekoratora `@classmethod`. Pierwszym parametrem metod klasowych jest `cls`, a nie `self`, jak w przypadku metod obiektowych. Metody klasowe są przydatne, gdy chcemy uzyskać dostęp do pól klasy lub do innych metod klasy.

    class Czlowiek:
      liczba_glow = 1

      @classmethod
      def wyswietl_glowy(cls):
        print(f'Liczba glow: {Czlowiek.liczba_glow}')

      def zwykla_funkcja(self):
        self.wyswietl_glowy()

    Czlowiek.wyswietl_glowy() # Liczba glow: 1

    przykladowy_czlowiek = Czlowiek()
    przykladowy_czlowiek.wyswietl_glowy() # Liczba glow: 1
    przykladowy_czlowiek.zwykla_funkcja() # Liczba glow: 1

Klasa `Czlowiek` zawiera pole statyczne `liczba_glow` oraz metodę klasową `wyswietl_glowy()`. Metoda ta wyświetla wartość pola `liczba_glow` przy pomocy f-stringów. Metoda `zwykla_funkcja()` jest zwykłą metodą instancyjną i wywołuje metodę klasową `wyswietl_glowy()`. Można się do niej odwołać zarówno poprzez nazwę klasy, jak i nazwę obiektu. W przykładzie są przedstawione trzy sposoby wywołania tej metody: bezpośrednio z poziomu klasy, z poziomu obiektu oraz z poziomu metody instancyjnej. W każdym przypadku wyświetlona zostanie wartość zmiennej `liczba_glow`.

### Referencje i kopiowanie

Dwa niezwykle istotne pojęcia w programowaniu to "referencja" i "kopiowanie". Referencja to odwołanie do oryginalnego obiektu, a kopiowanie to tworzenie nowego obiektu z tą samą zawartością co oryginalny. W języku Python przekazywanie obiektów do funkcji lub przypisywanie ich do nowych nazw odbywa się poprzez referencje. To oznacza, że zarówno oryginalny obiekt, jak i nowy obiekt będą wskazywać na to samo miejsce w pamięci. Wszelkie zmiany wprowadzone w jednym obiekcie będą widoczne również w drugim.  

    lista = [[1, 2, 3], [4, 5, 6]]
    nowa_lista = lista
    
    nowa_lista.append([-1, -2, -3]) # modyfikuje obie listy
    nowa_lista[0].insert(1, 1)      # modyfikuje obie listy
    print(lista)
    
Aby uniknąć takiej sytuacji, możemy skorzystać z kopiowania płytkiego lub głębokiego.
 
 1. Kopiowanie płytkie

Kopiowanie płytkie pozwoli na utworzenie nowego obiektu dla zewnętrznej struktury danych, ale wewnętrzne struktury danych będą przekazywane przez referencję. W naszym przykładzie z listą 2d, kopiowanie płytkie utworzy nowy obiekt dla zewnętrznej listy, ale wewnętrzne listy będą przekazane przez referencję.
    
    import copy
    lista = [[1, 2, 3], [4, 5, 6]]
    nowa_lista = copy.copy(lista)
    
    nowa_lista.append([-1, -2, -3]) # modyfikuje jedynie nowa liste
    nowa_lista[0].insert(1, 1)      # modyfikuje obie listy
    print(lista)

 2. Kopiowanie głębokie 

Kopiowanie głębokie pozwoli natomiast na utworzenie nowych obiektów dla zarówno zewnętrznej, jak i wewnętrznych struktur danych.

    import copy
    lista = [[1, 2, 3], [4, 5, 6]]
    nowa_lista = copy.deepcopy(lista)

    nowa_lista.append([-1, -2, -3]) # modyfikuje jedynie nowa liste
    nowa_lista[0].insert(1, 1)      # modyfikuje jedynie nowa liste
    print(lista)

### Czyste funkcje i skutki uboczne

NW przeciwieństwie do funkcji produkujących skutki uboczne, czyste funkcje nie wpływają na środowisko poza swoim zasięgiem. 

Skutki uboczne to m.in.
* Zmiany w plikach.
* Zmiany w bazie danych.
* Wysyłanie informacji przez sieć.
* Zmiany w globalnych zmiennych.

Przykłady czystych funkcji to:

* Funkcja zwracająca wartość pola trójkąta na podstawie jego boków.
* Funkcja zwracająca iloczyn elementów w liscie.
* Funkcja zwracająca największy element w liscie.
* Funkcja zwracająca nową listę z liczbami parzystymi z oryginalnej listy.
* Funkcja zwracająca nowy słownik z tylko niektórymi kluczami z oryginalnego słownika.
* Funkcja zwracająca nowy napis z dużymi literami z oryginalnego napisu.

Czyste funkcje najlepiej pracują z niemutowalnymi obiektami. Można zaimplementować czystą funkcję także z użyciem mutowalnych obiektów, o ile nie modyfikujemy ich stanu podczas działania funkcji. Ważne jest, aby czysta funkcja nie powodowała żadnych skutków ubocznych, czyli żadnych zmian w stanie obiektów poza wartościami, które zwraca.

Obiekty mutowalne to obiekty, które po utworzeniu można zmienić. W Pythonie obiekty mutowalne to np. listy, słowniki i zbiory (set). Obiekty mutowalne są niebezpieczne, ponieważ ich stan może zostać zmieniony w nieoczekiwany sposób, dlatego lepiej preferować obiekty niemutowalne, które zapewniają większe bezpieczeństwo, choć za cenę mniejszej wydajności. Aby zwiększyć bezpieczeństwo, lepiej stosować funkcje, które zamiast modyfikować stan obiektów mutowalnych, zwracają nowy obiekt, nie ruszając przekazanych jako parametry obiektów.

Przykłady obiektów mutowalnych:

    lista = [1, 2, 3]
    lista.append(4)
    print(lista) # [1, 2, 3, 4]

    slownik = {'klucz': 'wartosc'}
    slownik['nowy_klucz'] = 'nowa_wartosc'
    print(slownik) # {'klucz': 'wartosc', 'nowy_klucz': 'nowa_wartosc'}

    zbior = {1, 2, 3}
    zbior.add(4)
    print(zbior) # {1, 2, 3, 4}

Przykłady obiektów niemutowalnych:

    liczba = 5
    liczba = 6 # możemy zmienić wartość zmiennej, ale nie możemy zmienić samej liczby

    napis = 'napis'
    napis[1] = 'a' # nie możemy zmienić poszczególnych znaków w napisie

    krotka = (1, 2, 3)
    krotka[1] = 4 # nie możemy zmienić wartości elementów w krotce

### Dziedziczenie i kompozycja

Dziedziczenie i kompozycja to dwie techniki pozwalające na użycie kodu z innych klas w nowo tworzonej klasie. Dziedziczenie kopiuje wszystkie elementy z klasy nadrzędnej do klasy podrzędnej i pozwala na bezpośredni dostęp do pól i metod klasy nadrzędnej oraz możliwość zmiany ich definicji w klasie podrzędnej. Jest to używane, gdy nowa klasa jest specjalnym rodzajem już istniejącej klasy.

    class Czlowiek:
        def __init__(self, imie: str, nazwisko: str, miejsce_urodzenia: str, zawod: str):
            self.imie = imie
            self.nazwisko = nazwisko
            self.miejsce_urodzenia = miejsce_urodzenia
            self.zawod = zawod

        def __str__(self):
            return f"{self.imie} {self.nazwisko} {self.miejsce_urodzenia} {self.zawod}"


    class Student(Czlowiek):
        def __init__(self, imie: str, nazwisko: str, miejsce_urodzenia: str, numer_albumu: int, kierunek_studiow: str):
            super().__init__(imie, nazwisko, miejsce_urodzenia, 'student')
            self.numer_albumu = numer_albumu
            self.kierunek_studiow = kierunek_studiow

        def __str__(self):
            return f"{super().__str__()} {self.numer_albumu} {self.kierunek_studiow}"

        def __repr__(self):
            return f"{super().__repr__()} {self.numer_albumu} {self.kierunek_studiow}"

W powyższym przykładzie, klasa `Człowiek` jest klasą nadrzędną, a klasa `Student` jest klasą podrzędną. Klasa `Student` dziedziczy po klasie `Człowiek`, co oznacza, że posiada wszystkie pola i metody zdefiniowane w klasie `Człowiek`. Może również zmienić definicję metod z klasy nadrzędnej poprzez nadpisanie ich w klasie podrzędnej. W tym przykładzie, klasa `Student` nadpisuje metodę `str()` klasy `Człowiek`, aby dodać dodatkowe informacje o numerze albumu i kierunku studiów studenta. Klasa `Student` również nadpisuje metodę `repr()` klasy Człowiek, co oznacza, że jej reprezentacja tekstowa będzie również zawierać te dodatkowe informacje.

Kompozycja zaś polega na umieszczeniu obiektu jednej klasy jako pola w innej klasie. W nowo definiowanej klasie nie ma bezpośredniego dostępu do pól ani metod klasy skomponowanej, ale można do nich dotrzeć poprzez instancję tej klasy. Kompozycja jest używana, gdy nowa klasa reprezentuje całość, której istniejąca klasa jest częścią.
 
    class Pensja:

        def __init__(self, pensja: int, stopa_podwyzki: float):
            self.pensja = pensja
            self.stopa_podwyzki = stopa_podwyzki

        def __str__(self):
            return f"Pensja: {self.pensja}, stopa podwyzki: {self.stopa_podwyzki}"

    class Pracownik:

            def __init__(self, imie: str, nazwisko:str, pensja: Pensja):
                self.imie = imie
                self.nazwisko = nazwisko
                self.pensja = pensja # kompozycja, pensja jest czescia pracownika

            def __str__(self):
                return f"Pracownik: {self.imie} {self.nazwisko}, zarabia rocznie: {self.pensja.roczna_pensja()}"

Ten przykład ilustruje kompozycję, gdzie klasa `Pracownik` zawiera instancję klasy `Pensja` jako jedno z pól. W klasie `Pracownik` mamy metodę `roczna_pensja`, która zwraca wartość zapisaną w polu pensja pomnożoną przez stopę podwyżki. Klasa `Pracownik` nie ma bezpośredniego dostępu do pól lub metod klasy `Pensja`, ale może je użyć poprzez instancję tej klasy zapisaną w polu pensja. W ten sposób nowo definiowana klasa `Pracownik` reprezentuje pewną całość, w której istniejąca klasa `Pensja` jest jej częścią.

### Wyrażenia regularne

Wyrażenia regularne to sposób na wyszukiwanie tekstu w oparciu o wzorce. Możemy używać ich do wyszukiwania wzorców w ciągach znaków, ale także do zastępowania znalezionych wzorców innymi ciągami znaków. Możemy również używać wyrażeń regularnych do sprawdzania, czy ciąg znaków spełnia określone kryteria (np. czy jest to adres e-mail). Typowym zadaniem dla wyrażeń regularnych to Przykładowo znalezienie wszystkich słów zaczynających się od *abc* lub składających się wyłącznie z małych liter oraz cyfr parzystych.

Powiedzmy, że mamy plik gdzie każdy wiersz zawiera trzy informacje oddzielone ukośnikami: nazwisko pracownika, datę odczytu, oraz odczyt licnzika. Jak wyciągnąć datę z każdego wiersza? Używając klasycznych funkcji znanej nam klasy <code>String</code> moglibyśmy to zrobić w taki sposób:

    dane = 'Kowalski/Maj 15, 1983/1721.3'
    pracownik, data, odczyt = dane.split('/')
    miesiac, dzien, rok = data.split(' ')
    if dzien[-1] == ',':
      dzien = dzien[:-1]

    print(f'{miesiac}, {dzien}, {rok}') # Maj, 15, 1983

Rozwiązanie działa, ale nie należy do najpiękniejszych. Co gorsza, jest bardzo kruche. Cokolwiek zmieni się w naszych danych, musimy przerabiać nasz algorytm. Za każdym razem musimy być bardzo uważni i rozumieć każdy wiersz kodu. W takim podejściu bardzo łatwo popełnić błąd. Istnieje jednak inna metoda. Wyrażenia regularne są deklaratywne, tzn. mówimy co chcemy mieć, a nie w jaki sposób.

    import re

    dane = 'Kowalski/Maj 15, 1983/1721.3'
    match = re.search('(.*)/(.*)/(.*)', dane)
    data = match.group(2) # czesc tekstu odpowiadajaca drugiemu nawiasowi
    data = re.sub('[^\w\s]', '', data) # usun znaki interpunkcyjne
    miesiac, dzien, rok = re.split('[\s/]', data) # rozbij przy pomocy spacji

    print(f'{miesiac}, {dzien}, {rok}') # Maj, 15, 1983
    
Aby użyć wyrażeń regularnych, musimy najpierw zaimportować moduł `re`. Następnie możemy użyć różnych funkcji modułu `re`, takich jak `search`, `sub`, `split`, itd. Funkcja `search` służy do wyszukiwania wzorca w ciągu znaków, a funkcja `sub` do zastępowania znalezionych wzorców innymi ciągami znaków. Funkcja `split` służy do podziału ciągu znaków na fragmenty w oparciu o wzorzec.

Wyrażenia regularne składają się z ciągów znaków oraz specjalnych znaków. Specjalne znaki służą do określania rodzaju znaków, które chcemy znaleźć. Na przykład, znak "`.`" oznacza dowolny znak, a znak "`*`" oznacza dowolną ilość powtórzeń poprzedzającego znaku. Możemy również używać nawiasów kwadratowych, by określić zbiór znaków, które chcemy znaleźć. Na przykład, "`[0123456789]`" oznacza dowolną cyfrę, a "`[a-zA-Z]`" oznacza dowolną literę.

#### Znaki specjalne

Oto lista najważniejszych znaków specjalnych, które warto znać:

* <code>.</code> - dowolny znak (oprócz nowego wiersza)
* <code>\d</code> - cyfra
* <code>\D</code> - dowolny znak, który nie jest cyfrą
* <code>\s</code> - biały znak (spacja, tabulacja, nowy wiersz)
* <code>\S</code> - dowolny znak, który nie jest białym znakiem
* <code>\w</code> - dowolny znak alfanumeryczny (małe i duże litery, cyfry, znak podkreślenia)
* <code>\W</code> - dowolny znak, który nie jest znakiem alfanumerycznym
* <code>[]</code> - zbiór, np. <code>[abc]</code> oznacza a, b lub c
* <code>^</code> - początek wiersza
* <code>$</code> - koniec wiersza
* <code>|</code> - lub, np. <code>abc|def</code> oznacza a, b, c lub d, e, f
* <code>()</code> - grupa, np. <code>(abc){3}</code> oznacza a, b, c trzy razy
* <code></code> - powtórzenie dowolne razy, np. <code>a</code> oznacza 0 lub więcej wystąpień a
* <code>+</code> - powtórzenie co najmniej raz, np. <code>a+</code> oznacza 1 lub więcej wystąpień a
* <code>?</code> - powtórzenie 0 lub 1 raz, np. <code>a?</code> oznacza 0 lub 1 wystąpienie a
* <code>{m,n}</code> - powtórzenie od m do n razy, np. <code>a{2,4}</code> oznacza 2, 3 lub 4 wystąpienia a

Oczywiście to tylko wybrane przykłady.

#### Schemat pracy z wyrażeniami regularnymi

Omówimy teraz, jak krok po kroku przeprowadzić wszystkie czynności potrzebne do użycia wyrażeń regularnych w rozwiązaniu danego problemu. Oto krótki opis schematu:

1. Zbuduj najprostszą wersję wyrażenia regularnego pasującą do twojego problemu. 
1. Przetestuj czy wyrażenie regularne znajduje TYLKO to, co chcesz, by zostało znalezione. Łatwo o wynik fałszywie pozytywny.
1. Upewnij się, że wyrażenie regularne zwraca wszystkie niezbędne grupy. Pamiętaj, że grupy są oznaczone przez nawiasy `()`.
1. Poszerz rozwiązanie bazowe o dodatkowe wymogi. 
1. Upewnij się, że twój kod działa poprawnie dla różnych przypadków testowych.

Pamiętaj, że wyrażenia regularne mogą być skomplikowane i trudne do zrozumienia. Ważne jest, aby dobrze zrozumieć schemat pracy z nimi i systematycznie testować działanie wyrażenia przed użyciem go w kodzie.

### Wyjątki
Wyjątkami nazywamy sytuacje, które uniemożliwiają poprawne wykonanie danego bloku kodu. Tym samym terminem określany jest również mechanizm języka Python pozwalający na radzenie sobie z tymi sytuacjami.

W Pythonie istnieje szereg wyjątków zdefiniowanych w standardzie, takich jak <code>ZeroDivisionError</code>, który występuje, gdy próbujemy dzielić liczbę przez 0.

    print(5 / 0)

Możemy również sami wywołać wyjątek, np.: 

    raise ValueError("Podano nieprawidlowa wartosc")
    
Uwaga, nic nie chroni nas przed wywołaniem wyjątku w nieodpowiednim miejscu. Naszym zadaniem jest dbanie o to, aby wywołanie wyjątku było wykonane w odpowiedniej sytuacji.

#### Obsługa wyjątków

Obsługa wyjątków polega na zapobieżeniu zatrzymaniu programu w przypadku wystąpienia nieoczekiwanej sytuacji. Jest to szczególnie ważne w programach, które działają "w tle" i nie są interaktywne.

Aby obsłużyć wyjątek, używamy bloku `try/except`. W bloku try umieszczamy kod, który może spowodować wystąpienie wyjątku. W przypadku wystąpienia wyjątku, wykonywany jest kod znajdujący się w bloku except.

Oto przykład obsługi wyjątku `ZeroDivisionError`:

    try:
        print(5 / 0)
    except ZeroDivisionError:
        print("Nie można dzielić przez zero")

Wyjątek informuje nas o błędzie i nie powinniśmy go ignorować. Z tego powodu nigdy nie umieszczaj `pass` w bloku `except`.

Możemy również obsłużyć wyjątek, który jest podklasą innego wyjątku.

    try:
        print(int("abc"))
    except ValueError:
        print("Nie można zamienić tekstu na liczbę")

Istnieje opcja obsługi kilku różnych wyjątków w jednym bloku `try/except`. W takim wypadku, musimy umieścić osobny blok `except` dla każdego z nich.

    try:
        print(5 / 0)
        print(int("abc"))
    except ZeroDivisionError:
        print("Nie można dzielić przez zero")
    except ValueError:
        print("Nie można zamienić tekstu na liczbę")

Jeśli chcemy obsłużyć wiele różnych wyjątków w jednym bloku, możemy umieścić ich nazwy po przecinku. Możemy też użyć wyjątku ogólnego, np. `Exception`, ale nie jest to zalecane, ponieważ nie wiemy, jaki konkretny wyjątek wystąpił.

    try:
        # kod, ktory moze wywolac wyjatek
    except (ValueError, TypeError):
        # kod, ktory zostanie wykonany w przypadku wystapienia wyjatku ValueError lub TypeError

Możemy również zapisać wyjątek do zmiennej i użyć go w bloku `except`.

    try:
        print(5 / 0)
    except ZeroDivisionError as e:
        print(f"Wystąpił wyjątek: {e}")

Blok `else` jest opcjonalny i wykonywany jest, jeśli nie wystąpił żaden wyjątek w bloku `try`. Możemy go wykorzystać do wykonania kodu, który ma być wykonany po prawidłowym wykonaniu bloku try. W przeciwieństwie do bloku except, blok else nie przyjmuje argumentów.

Blok `finally` jest również opcjonalny, ale zawsze wykonywany bez względu na to, czy wystąpił wyjątek czy nie. Może być używany do wykonania kodu, który ma być wykonany zawsze, niezależnie od tego, czy wystąpił wyjątek czy nie. Może być przydatny, gdy chcemy zamknąć plik lub połączenie z bazą danych po zakończeniu pracy z nim.

#### Własny wyjątek

Możemy również tworzyć własne wyjątki. Nasz wyjątek musi dziedziczyć po klasie <code>Exception</code> lub jednej z jej podklas.

    class MojaWyjatkowaSytuacja(Exception):
        def __init__(self, value):
            self.value = value

        def __str__(self):
            return repr(self.value)

Możemy zgłosić nasz wyjątek za pomocą słowa kluczowego <code>raise</code>.

    raise MojaWyjatkowaSytuacja("To jest moj wyjatek")

Załóżmy, że chcemy sprawdzić czy liczba jest parzysta, gdyż tylko taka liczba może zostać użyta w dalszej części programu.

    def sprawdz_parzystosc(liczba):
        if liczba % 2 != 0:
            raise ValueError("Podano nieparzysta liczbe")
        else:
            return True

Możemy użyć tej funkcji w taki sposób:

    try:
        sprawdz_parzystosc(5)
    except ValueError as v:
        print(v)
    else:
        print("Liczba jest parzysta")

Wyświetlona zostanie informacja o błędzie "Podano nieparzysta liczbe".

#### Wyjątki jako mechanizm przepływu sterowania

Innym zastosowaniem wyjątków jest użycie ich jako mechanizm przepływu sterowania. W poniższym przykładzie używamy wyjątku do sprawdzenia, czy napis reprezentuje liczbę całkowitą:

    def czy_liczba(napis):
      try:
        int(napis)
      except ValueError:
        return False
      return True

### Wątki
Wątki, pozwalają na równoległe wykonywanie się kilku fragmentów kodu. Z tego powodu są szczególnie przydatne do obsługi zadań, które mogą zająć dużo czasu, np. łączenie się z zewnętrznym serwerem lub wczytywanie dużych plików. W ten sposób nie musimy czekać na zakończenie danego zadania, lecz możemy je wykonać równolegle z pozostałymi czynnościami.

Aby skorzystać z wątków, należy najpierw zaimportować moduł <code>threading</code>. Następnie, aby utworzyć nowy wątek, należy utworzyć obiekt klasy <code>Thread</code>. Klasa ta przyjmuje jako argument funkcję, która będzie wykonana jako wątek.

    import threading
    def watek():
        print("Watek")

    w1 = threading.Thread(target=watek)

Aby uruchomić wątek, należy wywołać metodę <code>start</code> na obiekcie klasy <code>Thread</code>.

    w1.start()

Należy pamiętać, że wątki działają równolegle, więc nie ma gwarancji kolejności wykonywania się poszczególnych wątków. 

#### Własny wątek

Aby utworzyć wątek, należy stworzyć klasę dziedziczącą po klasie <code>Thread</code> z modułu <code>threading</code> i zdefiniować metodę <code>run</code>, która zostanie wywołana przy uruchomieniu wątku. Następnie należy utworzyć obiekt tej klasy i wywołać metodę <code>start</code>, aby rozpocząć działanie wątku.

    import threading

    class MyThread(threading.Thread):
        def run(self):
            # kod, ktory zostanie wykonany w watku
            print("Wątek uruchomiony")

    thread = MyThread()
    thread.start()

Możemy również przekazać argumenty do metody <code>run</code> poprzez konstruktor klasy.

    import threading

    class MyThread(threading.Thread):
        def __init__(self, argument):
            self.argument = argument
            super().__init__()

        def run(self):
            # kod, ktory zostanie wykonany w watku
            print(f"Wątek uruchomiony z argumentem: {self.argument}")

    thread = MyThread("Hello World")
    thread.start()
    
#### Zatrzymanie wątku

W Pythonie można zatrzymać wątek poprzez wywołanie metody `Thread.join()`. Ta metoda blokuje wywołujący wątek aż do momentu, gdy wątek do którego została wywołana zakończy swoje działanie. Przykładowo, jeśli chcemy zatrzymać główny wątek programu do momentu, gdy wszystkie wątki zostaną zakończone, możemy użyć pętli for i iterować po liście wątków i dla każdego z nich wywołać metodę `join()`:

    threads = [thread1, thread2, thread3]

    for thread in threads:
        thread.join()

Można również użyć metody `Thread.join(timeout)` z opcjonalnym parametrem `timeout`. Parametr ten określa maksymalny czas oczekiwania na zakończenie wątku. Jeśli wątek nie zakończy działania w ciągu tego czasu, wątek wywołujący metodę `join()` zostanie wznowiony.

Innym sposobem zatrzymania wątku jest użycie zmiennej globalnej `threading.Event` z metodami `wait()` i `set()`. Wątek, który chcemy zatrzymać, może oczekiwać na sygnał za pomocą metody `wait()`, a wątek główny może wysłać sygnał za pomocą metody `set()`. W przypadku użycia tej metody, wątek oczekujący może również ustawić opcjonalny limit czasu oczekiwania.

      import threading

      # utworzenie zmiennej Event
      stop_event = threading.Event()

      def worker_thread():
          while not stop_event.is_set():
              # wątek wykonuje swoje zadania
              do_some_work()
          # po otrzymaniu sygnalu zatrzymujemy watek
          stop_event.clear()

      # ...

      # glowny watek chce zatrzymac worker_thread
      stop_event.set()

Należy pamiętać, że zatrzymanie wątku nie jest powszechnie zalecaną metodą zarządzania wątkami. W wielu przypadkach lepszym rozwiązaniem jest użycie warunków synchronizacyjnych lub zamknięcia wątku za pomocą metody `join()`. Zatrzymanie wątku może powodować nieoczekiwane skutki uboczne i powinno być używane jedynie w wyjątkowych sytuacjach.

#### Dzielenie zasobów między wątkami

Dzielenie zasobów między wątkami polega na umożliwieniu kilku wątkom równoczesnego dostępu do wspólnego zasobu. W przypadku, gdy zasób jest zmienny, konieczne jest zapewnienie bezpieczeństwa jego dostępu, tzn. zapobiegnięcie sytuacji, w której kilka wątków będzie próbowało zmodyfikować ten sam zasób w tym samym czasie. Istnieją mechanizmy umożliwiające bezpieczne dzielenie zasobów między wątkami, takie jak obiekt `Lock`.

Przykład:

    import threading

    # Zmienna globalna, do której będą miały dostęp wątki
    zmienna_globalna = 0

    # Obiekt Lock, który będziemy używali do synchronizacji dostępu do zmiennej globalnej
    lock = threading.Lock()

    def watek1():
      global zmienna_globalna
      for i in range(100):
        # Pobieramy lock, aby mieć pewność, że tylko jeden wątek będzie
        # miał dostęp do zmiennej globalnej w danym momencie
        lock.acquire()
        zmienna_globalna += 1
        lock.release()

    def watek2():
      global zmienna_globalna
      for i in range(100):
        # Pobieramy lock, aby mieć pewność, że tylko jeden wątek będzie
        # miał dostęp do zmiennej globalnej w danym momencie
        lock.acquire()
        zmienna_globalna -= 1
        lock.release()

    # Uruchamiamy wątki
    t1 = threading.Thread(target=watek1)
    t2 = threading.Thread(target=watek2)

    t1.start()
    t2.start()

    # Czekamy na zakończenie obu wątków
    t1.join()
    t2.join()

    # Wypisujemy wartość zmiennej globalnej
    print(zmienna_globalna)

W tym przykładzie mamy dwie funkcje `watek1` i `watek2`, które zmieniają wartość zmiennej globalnej `zmienna_globalna`. Aby zapewnić bezpieczne dzielenie zasobów między wątkami, użyto mechanizmu blokady. 

#### GIL
GIL, czyli Global Interpreter Lock, to mechanizm, który ogranicza możliwość jednoczesnego wykonywania kodu przez wiele wątków. W Pythonie każdy wątek jest obsługiwany przez GIL, który kontroluje dostęp do interpretera. W rezultacie tylko jeden wątek jest w stanie wykonywać kod naraz, a pozostałe są zawieszane aż do momentu, gdy GIL zostanie zwolniony.

GIL jest wbudowanym mechanizmem w Pythonie, który został dodany w celu uniknięcia problemów związanych z współdzieleniem zasobów przez wiele wątków. Chociaż GIL może mieć pewne ograniczenia w przypadku bardzo obciążających procesów wielowątkowych, w większości przypadków jest on wystarczający do obsługi równoległości w Pythonie.

Przykładowo, jeśli chcielibyśmy utworzyć program, który będzie sumował elementy w liście, możemy to zrobić za pomocą wielu wątków. Każdy wątek będzie odpowiedzialny za sumowanie części listy. Niestety, GIL spowoduje, że tylko jeden wątek będzie wykonywany w danym momencie, co spowolni działanie programu.

Oto przykład programu sumującego elementy w liście z użyciem wątków:

      import threading

      def sum_list(numbers):
          # Funkcja sumująca elementy w liście
          total = 0
          for number in numbers:
              total += number
          print(total)

      # Utworzenie wątków
      thread1 = threading.Thread(target=sum_list, args=([1, 2, 3],))
      thread2 = threading.Thread(target=sum_list, args=([4, 5, 6],))
      thread3 = threading.Thread(target=sum_list, args=([7, 8, 9],))

      # Uruchomienie wątków
      thread1.start()
      thread2.start()
      thread3.start()

      # Oczekiwanie na zakończenie wątków
      thread1.join()
      thread2.join()
      thread3.join()

W powyższym przykładzie, chociaż mamy trzy wątki, GIL spowoduje, że tylko jeden z nich będzie wykonywany w danym momencie, co sprawi że użycie wątków nie pomoże z przyspieszeniem działania progrmau.

### Procesy
Procesy to niezależne od siebie instancje programów wykonywane w systemie operacyjnym. Procesy dzielą pamięć i zasoby systemu, takie jak pliki i gniazda sieciowe. W odróżnieniu od wątków, procesy są całkowicie niezależne od siebie i nie mogą udostępniać swoich zmiennych.

W Pythonie mamy moduł <code>multiprocessing</code>, który umożliwia tworzenie procesów. Możemy użyć go, aby uruchomić nasz kod w osobnym procesie.

    import multiprocessing
    import time

    def worker():
        print("Rozpoczynam prace")
        time.sleep(2)
        print("Koncze prace")

    p = multiprocessing.Process(target=worker)
    p.start()

W przeciwieństwie do wątków, procesy nie mogą być zatrzymywane. Jeśli chcemy zatrzymać proces, musimy go zakończyć. W tym celu możemy użyć metody <code>terminate()</code>.

    p.terminate()

Procesy są dobrym wyborem, gdy chcemy uruchamiać kod równolegle, ale nie potrzebujemy udostępniać zmiennych między procesami. Procesy są również dobrym wyborem, gdy chcemy uniknąć problemu GIL, który dotyczy wątków w Pythonie. Należy jednak pamiętać, że procesy są bardziej zasobożerne niż wątki i nie nadają się do wszystkich zastosowań.

### Asyncio

Asyncio to moduł umożliwiający programowanie asynchroniczne. Asynchroniczne programowanie polega na wykonywaniu wielu zadań jednocześnie, bez konieczności blokowania głównego wątku programu. Aby funkcja mogła zostać wykonana asynchronicznie, należy użyć słowa kluczowego async oraz await.

Przykład użycia asyncio:

    import asyncio

    async def main():
        await asyncio.sleep(1)
        print("Hello, world!")

    asyncio.run(main())

W tym przykładzie, funkcja `main` jest oznaczona jako `async`, co oznacza, że będzie wykonywana asynchronicznie. Funkcja `asyncio.sleep(1)` jest funkcją, która zatrzymuje wykonanie wątku na 1 sekundę. Słowo kluczowe `await` jest używane do oznaczenia miejsca, w którym wątek ma czekać na zakończenie wykonywania funkcji `asyncio.sleep(1)`.

Moduł `asyncio` umożliwia tworzenie wielu wątków jednocześnie, co pozwala na lepsze wykorzystanie zasobów komputera. Należy jednak pamiętać, że `asyncio` nie jest rozwiązaniem wszystkich problemów związanych z wielowątkowością. W niektórych przypadkach lepszym rozwiązaniem może być użycie biblioteki `threading` lub `multiprocessing`.

### Lambdy

Wyrażenia lambda to funkcje składające się z jednego wiersza instrukcji, definiowane za pomocą słowa kluczowego lambda. Lambdy nie używają słowa kluczowego return, ponieważ zawsze zwracają wynik wykonania tworzącego je wiersza instrukcji.

    def zwykla_funkcja(liczba: int) -> int:
      return liczba**2
    
    przyklad_lambdy = lambda liczba: liczba**2
    
    wartosc = 2
    
    print(zwykla_funkcja(wartosc)) # 4
    print(przyklad_lambdy(wartosc)) # 4
    print((lambda liczba: liczba**2)(wartosc)) # 4

W porównaniu do pełnoprawnych funkcji definiowanych za pomocą słowa kluczowego def, lambdy są ograniczone:

- Możemy użyć jedynie jednego wiersza instrukcji.
- Możliwe jest sprawdzenie warunku, ale nie można zagnieżdżać warunków.
- Brak możliwości tworzenia zmiennych oraz przypisywania wartości do istniejących zmiennych (dla obiektów możemy użyć <code>setattr()</code>).
- Brak pętli.
  
Lambdy są również przydatne, gdy chcemy dostosować się do wymagań danej funkcji, która przyjmuje jako argument funkcję. W takim przypadku nie musimy tworzyć pełnoprawnej funkcji i jej przekazywać, lecz możemy bezpośrednio podstawić lambda.

Na przykład, jeśli chcemy posortować listę obiektów według pewnego atrybutu, możemy skorzystać z metody `sorted()`, która przyjmuje argument `key` - funkcję, która ma zwracać wartość atrybutu według którego ma być sortowana lista. W takiej sytuacji lambda pozwala nam zdefiniować tę funkcję w miejscy wywołania `sorted()`.

    lista = (('def', 100), ('ghi', 200), ('abc', 300))
    print(sorted(lista, key=lambda x: x[0])) # [('abc', 300), ('def', 100), ('ghi', 200)]
    print(sorted(lista, key=lambda x: x[1])) # [('def', 100), ('ghi', 200), ('abc', 300)]

### Programowanie funkcyjne

Istnieją różne narzędzia służące do transformacji danych. W tym artykule przyjrzymy się kilku z nich: <code>map()</code>, <code>filter()</code> i <code>reduce()</code>. Funkcje te są często używane w programowaniu funkcyjnym. Programowanie funkcyjne to paradygmat programowania, w którym głównym sposobem reprezentowania algorytmów są funkcje. W programowaniu funkcyjnym nacisk kładzie się na transformację danych przy użyciu funkcji, a nie na ich modyfikację w miejscu.

Funkcja <code>map()</code> to narzędzie służące do transformowania elementów jednej listy według określonej reguły. Ma ona dwa parametry: nazwę funkcji przyjmującej jeden argument (może to być też wyrażenie lambda) oraz nazwę listy. Funkcja <code>map()</code> zwraca nową listę, w której elementy są wynikami wywołania funkcji przekazanej jako pierwszy argument dla każdego elementu listy przekazanej jako drugi argument.

Istnieją również inne sposoby na osiągnięcie tego samego efektu, takie jak pętle for lub wyrażenia listowe. Aby lepiej zrozumieć działanie <code>map()</code>, warto porównać je z innymi metodami:

    lista = [5, 10, 15, 20, 25, 30, 35, 40]

    lista_a = [elem // 5 for elem in lista] # [1, 2, 3, 4, 5, 6, 7, 8]
    lista_b = list(map(lambda elem : elem // 5, lista)) # [1, 2, 3, 4, 5, 6, 7, 8]

Podobnie działa funkcja <code>filter()</code>. Jej wynikiem jest również nowa lista, złożona z elementów listy przekazanej jako drugi argument, dla których wywołanie funkcji przekazanej jako pierwszy argument zwróciło wartość logiczną `True`. Także i tutaj możemy porównać działanie <code>filter()</code> z innymi sposobami:

    lista = [5, 10, 15, 20, 25, 30, 35, 40]

    lista_a = [elem // 5 for elem in lista if elem % 2 == 0] # [2, 4, 6, 8]
    lista_b = list(map(lambda elem : elem // 5, filter(lambda elem : elem % 2 == 0, lista))) # [2, 4, 6, 8]

Funkcja `reduce()` jest narzędziem służącym do agregacji elementów sekwencji według określonej reguły. Podobnie jak `map()` i `filter()`, `reduce()` przyjmuje jako argumenty funkcję oraz sekwencję. Różnica polega na tym, że `reduce()` wywołuje funkcję iteracyjnie na elementach sekwencji i zwraca pojedynczy wynik agregacji. W poniższym przykładzie pokazane są dwa sposoby na utworzenie listy składającej się z numerów ASCII odpowiadających wielkim literom otrzymanego słowa:

    napis = 'Python is Love'
    lista_a = [ord(znak) for znak in napis if znak.isupper()]
    lista_b = list(map(lambda znak: ord(znak), filter(lambda znak: znak.isupper(), napis)))

    print(lista_a) # ['p', 'l']
    print(lista_b) # ['p', 'l']

Pętle możemy w naturalny sposób zagnieżdżać. Podobnie możemy również operować na funkcjach <code>map()</code>, <code>filter()</code> i <code>reduce()</code>:

    x = [2, 3, 5]
    y = [1, 2]

    lista_a = [elem_x + elem_y for elem_x in x for elem_y in y] # [3, 4, 4, 5, 6, 7]
    lista_b = list()
    list(map(lambda elem_x: list(map(lambda elem_y: lista_b.append(elem_x + elem_y), y)), x)) # [3, 4, 4, 5, 6, 7]
    
### Klasy danych

Tworzenie klas często wiąże się z powtarzalnym pisaniem elementów, takich jak inicjalizacja zmiennych przy użyciu funkcji specjalnej `__init__` oraz implementacja operatorów porównania. W takich przypadkach klasy danych (ang. data classes) mogą okazać się bardzo przydatne. Są one specjalnym rodzajem klas, które automatyzują proces tworzenia powtarzalnych elementów, takich jak inicjalizacja zmiennych i implementacja operatorów porównania. W celu utworzenia klasy danych wystarczy, że w obrębie klasy zadeklarujemy pola, które chcemy przechowywać. Są one szczególnie przydatne, gdy głównym celem naszej klasy jest grupowanie danych.

    @dataclass(unsafe_hash=True, order=True)
    class RGB:
      czerwony: int
      zielony: int
      niebieski: int
      
W powyższym przykładzie klasa `RGB` jest oznaczona dekoratorem `@dataclass`, co oznacza, że jest to klasa danych. Oznacza to, że automatycznie otrzyma ona metody specjalne, takie jak `__init__`, `__eq__` i `__repr__`, które są zwykle ręcznie implementowane w klasach.

Dekorator @dataclass przyjmuje również dwa dodatkowe argumenty: `unsafe_hash` i `order`. Argument `unsafe_hash` określa, czy instancje tej klasy mają być używane jako elementy słowników lub zbiorów (jeśli argument jest ustawiony na `True`, instancje tej klasy mogą być używane jako elementy słowników lub zbiorów). Argument `order` określa, czy instancje tej klasy będą używane jako elementy posortowanej sekwencji (np. listy). Jeśli argument order jest ustawiony na `True`, instancje tej klasy będą automatycznie posiadać metodę specjalną `__lt__`, która pozwala na porównywanie instancji za pomocą operatora `<`.

|    Funkcjonalność     |                      Przykład                                                           |
----------------------- |---------------------------------------------------------------------------------------- |
| Inicjalizacja pól     |  <code>kolor = RGB(255, 255, 0)</code>                                                  |
| Konwersja na napis    |  <code>print(RGB(255, 255, 0))   # "RGB(czerwony=255, zielony=255, niebieski=0)"</code> |
| Porównanie            |  <code>RGB(255, 255, 0) == RGB(255, 120, 255)</code>                                    |
| Porządkowanie         |  <code>sorted([ RGB(255, 255, 0), RGB(255, 120, 255)])</code>                           |
| Funkcja haszująca     |  <code>slownik = {kolor : "kolor"}</code>                                               |
| Rozpakowanie          |  <code>asdict(RGB(255, 255, 0)).values()</code>                                         |
| Optymalizacja pamięci |  <code>sys.getsizeof(RGB)</code>                                                        |

### Generatory

Generator to specjalny rodzaj funkcji, który zwraca wartości pojedynczo, zamiast zwracać ich wszystkie naraz w postaci listy lub innego iterowalnego obiektu. Generatory są bardziej efektywne pod względem pamięciowym niż listy, ponieważ nie wymagają przechowywania całej listy w pamięci, lecz tylko aktualnie zwracanej wartości. Generatory umożliwiają także klientowi rozpoczęcie przetwarzania zwracanych wartości zanim generator zakończy swoją pracę.

Aby utworzyć generator, wystarczy zamiast słowa kluczowego `return` użyć słowa kluczowego `yield`. Wartości, które generator ma zwracać są umieszczane po słowie kluczowym `yield` w ciele funkcji. Przykłady użycia generatorów znajdują się poniżej.

a) W poniższym przykładzie zwracamy wartości z funkcji <code>foo()</code> przy pomocy słowa kluczowego <code>yield</code>:

    def foo():
      yield 1
      yield 2
      yield 3

    print(list(foo()))
   
   Wynik po przekonwertowaniu na listę daje:
   
      [1, 2, 3]

b) W tym przykładzie zwracamy wartości z funkcji <code>bar()</code> przy pomocy słowa kluczowego <code>return</code>:

    def bar():
      return 1
      return 2 #Martwy kod
      return 3

    print(bar())

  Wynik:
   
      1

### Iteratory

Pętla `for` jest narzędziem, które umożliwia przejście przez kolejne elementy sekwencji, takiej jak lista, ciąg znaków lub tuple. Możemy użyć pętli `for` w następujący sposób:

    for elem in lista:
       print(elem)

Wbudowane kolekcje, takie jak listy, ciągi znaków i tuple, posiadają metodę `__iter__()`, która zwraca iterator dla danej kolekcji. Iterator to obiekt, który umożliwia przejście przez elementy kolekcji po kolei. Możemy wywołać funkcję `next()` z przekazanym jako argument iterator, aby pobrać kolejny element kolekcji. Jeśli iterator nie ma już więcej elementów do zwrócenia, zostanie rzucony wyjątek `StopIteration`.

    lista = [1, 2, 3]
    iterator = iter(lista)
    print(next(iterator)) # wyswietli 1
    print(next(iterator)) # wyswietli 2
    print(next(iterator)) # wyswietli 3
    print(next(iterator)) # zostanie wyrzucony wyjatek

Ten mechanizm jest używany wewnętrznie przez pętlę `for`. Iteratory pozwalają na implementację własnych zasad przechodzenia przez kolekcję. Możemy stworzyć własną klasę iterowalną, implementując metodę `__iter__()` i używając słowa kluczowego `yield` w celu zwracania elementów kolekcji po kolei.

    class ObiektIterowalny:

      def __init__(self):
        self.lista_a = [3, 2, 1]
        self.lista_b = [-1, -2, -3]

      def __iter__(self):
        licznik = 0
        while licznik < len(self.lista_a) and len(self.lista_b):
          yield self.lista_a[licznik], self.lista_b[licznik]
          licznik+=1

    obiekt = ObiektIterowalny()

    for elem in obiekt:
      print(elem)
      
Dzięki temu, że nasz obiekt jest iterowalny, możemy używać go w pętli `for` w taki sam sposób, jak wbudowane kolekcje.

### Dekoratory
Przy pomocy dekoratorów możemy rozszerzać funkcjonalność istniejących funkcji bez ich modyfikowania. Możemy też używać ich jako dodatkowego sposobu na zabezpieczenie funkcji przed nieprawidłowym wykorzystaniem lub po prostu jako mechanizmu ułatwiającego debugowanie.

Aby zachować informacje o funkcji dekorowanej, możemy użyć dekoratora <code>functools.wraps()</code>:

    import functools

    def dekoruj(funkcja):
      @functools.wraps(funkcja)
      def funkcja_wew():
        print('przetwarzam dane')
        funkcja()
      return funkcja_wew

Dzięki temu wszystkie informacje o funkcji <code>foo</code>, takie jak jej nazwa czy dokumentacja, zostaną zachowane po dekoracji.

Możemy też przekazywać argumenty do dekoratora i funkcji dekorowanej:

    def dekoruj(funkcja):
      def funkcja_wew(*args, **kwargs):

### Serializacja

Serializacja to proces konwersji obiektu na strumień bajtów, który może być następnie zapisany, przesłany lub przechowywany w inny sposób. Dzięki serializacji możliwe jest zapisywanie stanu obiektów i ich późniejsze odtwarzanie, co może być przydatne np. w grach, gdzie chcemy zapisać postępy gracza lub w aplikacjach, gdzie chcemy zapisywać dane użytkownika.

Moduł `pickle` służy do serializacji i deserializacji obiektów. Funkcja `dumps()` pozwala na zserializowanie obiektu do strumienia bajtów, który może być następnie zapisany do pliku lub przesłany do innego procesu. Funkcja `loads()` pozwala na odtworzenie obiektu ze strumienia bajtów.

Przykład użycia tych funkcji znajduje się poniżej. W kodzie tworzona jest klasa `Czlowiek` z polami `imie` i `numer`, a następnie serializowana i zapisywana do pliku. Następnie obiekt jest odtwarzany z pliku i wyświetlany na ekranie.

    import pickle

    class Czlowiek:
      def __init__(self, imie, numer):
        self.imie = imie
        self.numer = numer

      def __repr__(self):
        return f'Imie: {self.imie}, numer: {self.numer}'

    sciekza = 'przyklad.pickle'

    with open(sciekza, 'wb') as plik:
      pickle.dump(Czlowiek('James', 10), plik)


    with open(sciekza, 'rb') as plik:
      czlowiek = pickle.load(plik)
      print(czlowiek) #Imie: James, numer: 10

## Inżynieria oprogramowania

Inżynieria oprogramowania to dziedzina zajmująca się procesem tworzenia oprogramowania, od projektowania po implementację i utrzymanie. W tej dziedzinie ważne są takie aspekty jak dobór narzędzi i metodologii, zarządzanie projektem, czy współpraca w zespole.

### Moduły i pakiety

Za każdym razem, gdy używamy instrukcji <code>import</code>, importujemy do skryptu zewnętrzny moduł. Każdy plik Pythona jest modułem, którego nazwa to nazwa pliku bez rozszerzenia .py. <a href="https://docs.python.org/3/library/index.html">Dokumentacja</a> zawiera pełną listę wbudowanych modułów biblioteki standardowej Pythona. Przykładowo, tak możemy zaimporotwać moduł `requests`:
 
    import requests
    print(type(requests)) # <class 'module'>

Pakiety to foldery z modułami, w których znajduje się plik `init.py`. Jest to plik specjalny, który jest potrzebny do odróżnienia pakietu od zwykłego folderu.

    .
    └── nazwa_paczki
        ├── __init__.py
        └── przykladowy_skrypt_a.py
        └── przykladowy_skrypt_b.py
        └── przykladowy_skrypt_c.py
    └── main.py
    
Możemy importować moduły na kilka sposobów:

* Zaimportowanie całego modułu:

      import nazwa_modulu

* Zaimportowanie całego modułu i nadanie mu aliasu:

      import nazwa_modulu as alias

* Zaimportowanie wybranych funkcji z modułu:

      from nazwa_modulu import fun_1, fun_2

* Zaimportowanie wybranych funkcji z modułu i nadanie im aliasów:

      from nazwa_modulu import fun_1 as f1, fun_2 as f2

* Zaimportowanie wszystkich funkcji z modułu:

      from nazwa_paczki.przykladowy_skrypt_a import *

      fun_a()
      fun_b()

Należy uważać z używaniem instrukcji <code>from modul import *</code>, ponieważ zaimportowane zostają wszystkie zmienne i funkcje z modułu, niezależnie od tego czy ich będziemy używać czy nie. Może to prowadzić do konfliktów nazw oraz utrudnić odczytanie kodu.

Uwaga: instrukcje, które nie są częścią definicji żadnej funkcji, zostaną automatycznie wykonane podczas importowania modułu!

Przykład:

    def fun_a():
        ...

    def fun_b():
         ...

    wyslij_rakiety()

Jeśli ten moduł zostanie zaimportowany w innym skrypcie, to funkcja `wyslij_rakiety()` zostanie wywołana podczas importowania modułu.
Aby temu zapobiec, należy umieścić wszystkie instrukcje, które mają być wykonywane poza definicjami funkcji, w ciele następującego warunku <code>if name == "main":</code> :

    def fun_a():
        ...

    def fun_b():
         ...

    if __name__ == "__main__":
      wyslij_rakiety()

### Wersje Pythona

Narzędzie <code>Pyenv</code> służy do izolowania różnych wersji Pythona. Jeśli na przykład chcesz przetestować swój kod w Pythonie 2.5, 3.6 i 3.10, potrzebujesz prostego sposobu na przełączanie się między nimi. <code>Pyenv</code> modyfikuje zmienną środowiskową PATH dodając do niej ścieżkę do specjalnego folderu <code>(pyenv root)/shims</code>. Ponadto <code>Pyenv</code> umożliwia pobieranie i instalowanie różnych wersji Pythona za pomocą polecenia <code>pyenv install</code>.

Linki:

* https://github.com/pyenv/pyenv
* https://github.com/pyenv-win/pyenv-win

Po zainstalowaniu pyenv, możemy użyć polecenia pyenv install aby zainstalować nową wersję Pythona. Na przykład, aby zainstalować wersję Python 3.10, użyjemy polecenia:

    pyenv install 3.10

Aby ustawić wersję Pythona, która będzie używana dla danego katalogu, użyj polecenia pyenv local:

    pyenv local 3.10

Aby ustawić wersję Pythona, która będzie używana dla całego systemu, użyj polecenia pyenv global:

    pyenv global 3.10

Aby wyświetlić listę zainstalowanych wersji Pythona, użyj polecenia pyenv versions:

    pyenv versions

Aby wyświetlić bieżącą wersję Pythona, użyj polecenia pyenv version:

    pyenv version

### PIP i PyPI

PIP to narzędzie umożliwiające instalację pakietów Pythona dostępnych na stronie PyPI (Python Package Index).

Instalacja:

1. Pobierz skrypt <a href="https://bootstrap.pypa.io/get-pip.py">get-pip.py</a>.
1. Uruchom skrypt <code>python get-pip.py</code>.
1. Zweryfikuj poprawność instalcji wpisując w wierszu poleceń następujące komendy: <code>pip help</code>.

Aby zainstalować konkretny pakiet, użyj:

    pip install <nazwa_pakietu>
    
Aby wyświetlić szczegóły zainstalowanego pakietu, użyj:
    
    pip show <nazwa_pakietu>
    
Aby wyświetlić listę wszystkich aktualnie używanych pakietów, użyj:

    pip list
    
Aby zapisać w pliku *requirements.txt* listę wszystkich aktualnie używanych pakietów wraz z wersjami, użyj:

    pip freeze > requirements.txt
    
Aby odinstalować pakiet, użyj:

    pip uninstall <nazwa_pakietu>

Aby zaktualizować program PIP, użyj:
 
    pip install --upgrade pip

Linki:

* https://pypi.org/

### Środowisko wirtualne

Środowisko wirtualne to odizolowane od reszty systemu wersje bibliotek i pakietów Pythona. Instalując daną wersję pakietu w środowisku wirtualnym jest ona dostępna tylko w nim. Gdy usuwamy środowisko wirtualne wraz z nim znika również wszystko to co zostało zainstalowane w jęgo obrębie.

Popularnym narzędziem do tworzenia środowisk wirtualnych jest <code>virtualenv</code>. Narzędzie to tworzy specjalny folder o dowolnej nazwie (np. `env/`) oraz modyfikuje zmienną środowiskową PATH dodając do niej refernecje do podfolderu `bin` znajdującego się w utworzonym folderze (np. `env/bin/`). Wszystkie pakiety i biblioteki instalowane w środowisku wirtualnym wędrują do tego folderu.

Aby zainstalować narzędzie <code>virtualenv</code> przy pomocy menadźera pakietów <code>PIP</code>, użyj:

    pip install virtualenv

Aby utworzyć środowisko wirtualne o nazwie *env* w aktualnym folderze, użyj:

    virtualenv env
    
Jeśli w systemie masz zainstalowane różne wersje Pythona, to możesz powiedzieć środowisku wirtualnemu, z której wersji ma korzystać.
Przykładowo, jeśli mam interpreter Pythona w folderze */usr/bin/python3* i chce, żeby z niego korzystało moje środowisko wirtualne, to używam następującej komendy:

    virtualenv -p /usr/bin/python3 env

Aby wejść do środowiska wirtualnego, użyj:

    source env/bin/activate
    
Aby wyjść ze środowiska wirtualnego, użyj:

    deactivate
    
Aby zapisać do pliku *requirements.txt* wszystkie aktualnie zainstalowane biblioteki wraz z ich wersjami, użyj:

    pip freeze > requirements.txt

Aby zainstalować biblioteki wymienione w pliku *requirements.txt*, użyj:

    pip install -r requirements.txt
    
Linki:

* https://github.com/pypa/virtualenv

### Dbanie o jakość kodu i lintowanie

Poprawny z punktu widzenia interpretera kod można napisać na wiele sposobów. Nawet jedna linia kodu może być zapisana na wiele sposobów. Jedną z przyczyn takiego stanu rzeczy są różnice w formatowaniu. Na przykład w kodzie do oddzielania instrukcji można użyć zarówno spacji, jak i tabów. Definicje funkcji można oddzielać jednym, dwoma lub trzema enterami. Linie kodu mogą być tak długie, że nie zmieszczą się na ekranie. Czy więc należy ograniczać ich długość? Jeśli tak, to ile znaków powinno być górną granicą? Dopóki z kodem pracujemy sami, wszystko wydaje się być w porządku, ale co jeśli ktoś inny będzie musiał czytać nasz kod? Co jeśli ktoś inny będzie musiał go modyfikować? Wtedy ważne staje się, by kod był czytelny i zrozumiały dla innych programistów. Z tych właśnie względów warto przestrzegać konwencji pisania kodu.

Narzędzia, takie jak <code>Pylint</code> i <code>Black</code> pomagają nam uniknąć typowych błędów i niepoprawności, które mogą pojawić się podczas pisania kodu. Narzędzia te sprawdzają, czy kod jest zgodny z zasadami zapisanymi w dokumentach <code>PEP8</code> i <code>PEP257</code>.

Aby użyć narzędzia <code>Pylint</code>, zainstaluj je za pomocą <code>PIP</code>:

    pip install pylint

Aby sprawdzić kod za pomocą <code>Pylint</code>, użyj polecenia:

    pylint <nazwa_pliku.py>

Aby użyć narzędzia <code>Black</code>, zainstaluj je za pomocą <code>PIP</code>:

    pip install black

Aby użyć <code>Black</code> do sformatowania kodu w pliku o nazwie <code>nazwa_pliku.py</code>, użyj polecenia:

    black nazwa_pliku.py

Black to narzędzie do automatycznej reformatowania kodu w celu dostosowania go do wytycznych PEP8. Nie pyta ono o zdanie programisty i zmienia formatowanie kodu bez możliwości konsultacji. Z tego względu Black jest narzędziem bardzo szybkim i prostym w użyciu. Jego główną wadą jest brak możliwości konfiguracji. Black nie pozwala na zmianę domyślnych ustawień ani na wyłączenie poszczególnych zasad formatowania.

Flake8 to narzędzie do sprawdzania jakości kodu. Oprócz formatowania kodu, Flake8 sprawdza także jego poprawność semantyczną oraz brak błędów składniowych. W porównaniu do Blacka, Flake8 oferuje większą ilość opcji konfiguracyjnych. Możliwe jest m.in. wyłączenie poszczególnych zasad sprawdzania lub zmiana ich domyślnych ustawień. Jedną z wad Flake8 jest to, że jest ono wolniejsze od Blacka, ponieważ sprawdza także inne aspekty kodu niż tylko jego formatowanie.

Pylint to narzędzie do sprawdzania jakości kodu podobne do Flake8. Oprócz sprawdzania formatowania kodu i braku błędów składniowych, Pylint sprawdza także nazewnictwo zmiennych i funkcji oraz brak docstringów (komentarzy opisujących kod).

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

Debuger jest bardzo przydatnym narzędziem, zwłaszcza przy pracy nad dużymi projektami. Dzięki niemu możemy zatrzymać program w dowolnym momencie, aby sprawdzić co się w nim dzieje. Możemy też prześledzić kolejne kroki programu, które zostały wykonane do momentu zatrzymania, co pozwala na szybkie i skuteczne znajdowanie błędów.

Dwa główne zastosowania debugera:
- Wyszukiwanie przyczyn bugów w kodzie.
- Analiza działania programu przez zaznajamiających się z nim programistów.

Jedną z mocnych stron debugera jest też to, że pozwala nam zajrzeć "pod maskę" programu i zobaczyć jakie zmienne są zdefiniowane i jakie są ich wartości. Dzięki temu możemy szybciej zrozumieć co dzieje się w kodzie i co jest przyczyną jakichś błędów.

Słabą stroną debugera jest to, że korzystanie z niego może być czasochłonne. Zatrzymywanie programu i przechodzenie przez kolejne kroki wymaga czasu i cierpliwości. Czasem może też być trudno zrozumieć co dzieje się w kodzie, jeśli jest on bardzo skomplikowany lub niezrozumiały.

Większość współczesnych środowisk programistycznych (IDE) ma wbudowany debuger. Debugger w IDE umożliwia ustawienie punktów breakpoint, dzięki którym program zatrzymuje się automatycznie w wybranym miejscu, co ułatwia debugowanie. IDE zazwyczaj posiada również dodatkowe funkcje, takie jak możliwość podglądu zmiennych czy historii wywołań funkcji, które ułatwiają debugowanie.

Jeśli nie korzystamy z IDE, możemy użyć modułu pdb, który jest wbudowanym w Pythonie debugerem. Moduł ten umożliwia kontrolowanie wykonywania kodu z linii poleceń, co pozwala na debugowanie skryptów bez konieczności ich uruchamiania w środowisku programistycznym. Możliwe jest również uruchamianie pdb z poziomu kodu Pythona za pomocą funkcji importowanej z modułu <code>pdb</code>: <code>pdb.set_trace()</code>. Po uruchomieniu tej funkcji program zatrzyma się i będziemy mogli kontrolować jego działanie z linii poleceń.

Linki:

* https://docs.python.org/3/library/pdb.html

### Testy jednostkowe

Testy jednostkowe są ważnym narzędziem w procesie tworzenia oprogramowania, ponieważ pomagają zapewnić, że nasz kod działa poprawnie i jest odporny na błędy. Pozwalają również na szybkie wykrycie błędów, które pojawiły się w wyniku zmian w kodzie, dzięki czemu możemy je szybko naprawić. 

* Czerwone testy, czyli testy, które nie przeszły, pokazują, że coś, co działało wcześniej, aktualnie nie działa. Może to być spowodowane tym, że została wprowadzona jakaś zmiana w kodzie, która spowodowała, że test nie zadziałał poprawnie. Czerwone testy są sygnałem, że coś jest nie tak i konieczne jest przeanalizowanie kodu i znalezienie przyczyny problemu.
* Zielone testy, czyli testy, które przeszły, pokazują, że to, co było sprawdzane w testach działa poprawnie. Nie oznacza to jednak, że cały program działa poprawnie - mogą być jeszcze inne fragmenty kodu, które nie zostały sprawdzone w testach i które mogą działać niepoprawnie. Zielone testy są ważne, ponieważ pozwalają upewnić się, że kod działa zgodnie z założeniami, ale nie są wystarczające do całkowitego zabezpieczenia aplikacji przed błędami.

Ogólnie w Pythonie mamy dwie popularne biblioteki służące do testów jednostkowych: <code>unittest</code> i <code>pytest</code>. Obie biblioteki, dają nam możliwość tworzenia testów jednostkowych i uruchamiania ich automatycznie, co pozwala na skupienie się na kodowaniu i uniknięcie ręcznego testowania kodu. Obie biblioteki są dość proste w użyciu i oferują duże możliwości tworzenia i uruchamiania testów. Ostateczny wybór biblioteki zależy od indywidualnych potrzeb i preferencji programisty.

#### Unittest

Biblioteka ta została zbudowana zgodnie z filozofią programowania obiektowego, co oznacza, że w kodzie tworzymy klasy i korzystamy z dziedziczenia. Unittest oferuje również wiele funkcji assert, które pozwalają na sprawdzenie różnych aspektów działania programu.

Przykład kodu z użyciem unittest:

    import unittest
    
    class TestSMTP(unittest.TestCase):
      
      def smtp_connection(self):
        import smtplib
        return smtplib.SMTP("smtp.gmail.com", 587, timeout=5)

     def test_helo(self):
        response_code, msg = self.smtp_connection().ehlo()
        self.assertEqual(response_code, 250)

W powyższym przykładzie tworzymy klasę TestSMTP, która dziedziczy po klasie TestCase z biblioteki unittest. W tej klasie zdefiniowaliśmy funkcję smtp_connection, która tworzy połączenie z serwerem SMTP, oraz funkcję test_helo, która wywołuje metodę ehlo na połączeniu SMTP i sprawdza, czy otrzymano oczekiwany kod odpowiedzi (250).

Aby uruchomić testy jednostkowe, wystarczy wywołać odpowiednie polecenie w konsoli: 

    python -m unittest

#### Pytest

Pytest to również biblioteka służąca do tworzenia i uruchamiania testów jednostkowych w języku Python. Została zbudowana zgodnie z filozofią "im prościej, tym lepiej", co oznacza, że nie ma w niej klas i dziedziczenia. Pytest pozwala na tworzenie testów poprzez definiowanie funkcji oznaczonych adnotacją @pytest.fixture.

Przykład kodu z użyciem pytest:

    import pytest
    
    @pytest.fixture
    def smtp_connection():
       import smtplib
       return smtplib.SMTP("smtp.gmail.com", 587, timeout=5)
    
    def test_helo(smtp_connection):
       response_code, msg = smtp_connection.ehlo()
       assert response_code == 250

Test składa się z dwóch części: dekoratora <code>@pytest.fixture</code> oraz funkcji testowej <code>test_helo()</code>.

Dekorator <code>@pytest.fixture</code> mówi nam, że funkcja <code>smtp_connection()</code> jest funkcją pomocniczą, która zostanie uruchomiona przed każdą funkcją testową. W tym przypadku <code>smtp_connection()</code> tworzy obiekt <code>SMTP</code> i zwraca go jako wartość. Funkcja ta nie jest testem jednostkowym, ale służy do przygotowania środowiska testowego.

Natomiast funkcja testowa <code>test_helo()</code> jest testem jednostkowym. Funkcja ta przyjmuje jako argument obiekt <code>smtp_connection</code>, który został wcześniej utworzony przez dekorator <code>@pytest.fixture</code>. Funkcja testowa wywołuje na tym obiekcie funkcję <code>ehlo()</code> i sprawdza, czy kod odpowiedzi oraz wiadomość zwracana przez funkcję są takie same, jak oczekiwane wartości. Jeśli tak, to test zostaje zaliczony, w przeciwnym razie test zostaje uznany za nieudany (tzw. "czerwony test").

Aby uruchomić testy jednostkowe, wystarczy wywołać odpowiednie polecenie w konsoli: 

    pytest

#### Korzyści z testów jednostkowych

* Pomagają innym programistom zrozumieć cel danego fragmentu kodu produkcyjnego.
* Gdy programy są małe, programista może ręcznie sprawdzić ich działanie z każdą modyfikacją. Wraz ze wzrostem złożoności, ręczne testowanie wszystkich części programu staje się niemożliwe. Testy jednostkowe można uruchomić automatycznie.
* Wymuszają separację zadań między poszczególnymi fragmentami kodu.
* Pozwalają na szybkie sprawdzenie poprawności działania kodu po dokonaniu zmian w kodzie produkcyjnym.

#### TDD

Technika "test driven development" (TDD) to sposób pisania programów, w którym testy są pisane przed kodem produkcyjnym. Proces tworzenia programu składa się z trzech etapów:

1. Testy jednostkowe.
2. Kod produkcyjny.
3. Refkatoryzajca kodu produkcyjnego.

Programista nigdy nie przechodzi do implementacji nowych funkcjonalności, dopóki wszystkie trzy etapy nie zostały zakończone dla aktualnie implementowanych funkcjonalności.

#### Losowe dane nie mają miejsca w testach

Załóżmy, że masz własną implementację jednego z algorytmów sortowania. Jeśli chcesz porównać wynik jego działania, z wynikiem działania funkcji <code>sorted()</code> z biblioteki standardowej to ręcznie przygotuj listy wejściowe.

    import pytest
    
    def test_wlasne_sortowanie():
       lista_a  = [1, 1, 1]
       lista_b = [3, 5, 2]
       lista_c = [-1, 2, 3, -1, 0]
       # import random
       # lista_d = [random.randint(-10, 10) for _ in range(5)] # ZLE
       
       assert wlasne_sortowanie(lista_a) == sorted(lista_a)
       assert wlasne_sortowanie(lista_b) == sorted(lista_b)
       assert wlasne_sortowanie(lista_c) == sorted(lista_c)

Powyższy fragment kodu zawiera przykład użycia pytest do testowania funkcji <code>wlasne_sortowanie</code>. W tym przypadku, trzy listy są tworzone jako dane wejściowe: <code>lista_a</code>, <code>lista_b</code> i <code>lista_c</code>. Następnie są one porównywane z oczekiwanymi wynikami po wywołaniu funkcji <code>sorted()</code> na tych samych danych wejściowych za pomocą polecenia <code>assert</code>. Jeśli wynik zwrócony przez <code>wlasne_sortowanie()</code> jest różny od oczekiwanego wyniku, zostanie wygenerowany błąd, który poinformuje o niepowodzeniu testu.

#### Od znalezienia buga do poprawnie działającego kodu

Zauważono błąd w twoim programie. Co należy zrobić?

1. Próbuj odtworzyć problematyczną sytuację. Na przykład, jeśli twoja aplikacja zamyka się po wciśnięciu przycisku mającego przenieść użytkownika na inną stronę, najpierw manualnie wykonaj wszystkie kroki prowadzące do pojawienia się niechcianego efektu.
1. Zlokalizuj w kodzie, który fragment jest odpowiedzialny za pojawienie się znalezionego błędu.
1. Dodaj test, który sprawdzi, czy niepożądana sytuacja występuje po wykonaniu zlokalizowanego fragmentu kodu. Na przykład, jeśli błąd pojawia się po wywołaniu funkcji <code>foo()</code>, najpierw znajdź test <code>test_foo()</code> i upewnij się, że funkcja <code>foo()</code> jest wywoływana z parametrami, przy których pojawia się błąd. Dodaj test wykrywający wystąpienie niepożądanej sytuacji. Po uruchomieniu testu otrzymasz czerwony komunikat. 
1. W kolejnym kroku przyjdzie ci naprawić funkcję <code>foo()</code>. Możesz to zrobić na różne sposoby, ale pamiętaj, że celem jest zamienienie czerwonego komunikatu z testu na zielony. Możesz zmienić sposób działania funkcji, zmienić sposób przekazywania argumentów lub wyeliminować jakiś błąd. Ważne, by po zmianach test <code>test_foo()</code> przeszedł pomyślnie.
1. Gdy test przechodzi pomyślnie, możesz przejść do kolejnego etapu, czyli refaktoryzacji kodu. To etap, w którym dbamy o to, by kod był czytelny, elegancki i łatwy do zrozumienia. Może to oznaczać przemianowanie zmiennych, zmianę sposobu ich deklaracji, a nawet usunięcie niepotrzebnych linii kodu. Refaktoryzacja powinna być przeprowadzana zgodnie z zasadami zdrowego rozsądku i nie powinna wpływać na poprawność funkcji.
1. W przyszłości dbaj o to, by test już zawsze pozostał zielony.

#### Inne typy testów

* Testy jednostkowe to testy sprawdzające odizolowane jednostki kodu, najczęściej pojedyncze funkcje.
* Testy integracyjne to testy sprawdzające, jak różne elementy systemu współpracują ze sobą.
* Testy całego systemu (end-to-end) to testy sprawdzające, jak system działa jako całość, od wejścia aż do wyjścia.

Ogólnie rzecz biorąc, im mniej testów jednostkowych, tym więcej testów integracyjnych i testów całego systemu jest potrzebnych, aby zapewnić odpowiedni poziom testowania. Ważne jest, aby zachować odpowiedni balans między różnymi typami testów.

Zgodnie z zaleceniami autora <a href="https://www.oreilly.com/library/view/software-engineering-at/9781492082781/">"Software Engineering at Google"</a> testy należy rozdzielić w następujących proporcjach:

* 80% testy jednostkowe
* 15% testy integracyjne
* 5% testy całego systemu (end-to-end)

#### Generowanie danych testowych automatycznie

Przy tworzeniu aplikacji, warto również zadbać o skrypty generujące dane testowe, które są potrzebne do pracy aplikacji. Na przykład, jeśli piszesz aplikację komunikującą się z bazą danych MySQL, powinieneś mieć skrypt, który automatycznie utworzy taką bazę danych i wypełni ją przykładowymi danymi. Dzięki temu, podczas pisania kodu, możesz od razu sprawdzić, czy działa on poprawnie, bez konieczności czekania na uruchomienie testów w środowisku produkcyjnym. Ponadto, masz możliwość automatycznego testowania całej aplikacji.

#### Organizacja projektu z testami

Aby zachować porządek w projekcie, warto rozdzielić kod produkcyjny i testy jednostkowe do osobnych folderach. W ten sposób łatwiej będzie zarządzać plikami i szybko odnaleźć potrzebne testy.

Przykładowo, struktura projektu może wyglądać następująco:

    projekt
    ├── przykladowy_pakiet
    │   ├── __init__.py
    │   └── modul_a.py
    │   └── modul_b.py
    └── tests
        ├── __init__.py
        └── test_modul_a.py
        └── test_modul_b.py

W ten sposób z jednej strony ograniczymy wielkość plików z testami, a z drugiej strony ułatwimy wszystkim życie, gdyż znacznie łatwiej będzie zlokalizować konkretny test.

#### Automatyzacja testów

W momencie, gdy nasz projekt zaczyna rosnąć w skali, warto zastanowić się nad automatyzacją testów. Możliwe opcje to użycie narzędzi takich jak <a href="https://travis-ci.org/">Travis CI</a>, <a href="https://jenkins.io/">Jenkins</a>, czy <a href="https://circleci.com/">CircleCI</a>. Dzięki temu każdorazowa zmiana w kodzie źródłowym automatycznie uruchamia wszystkie testy, dzięki czemu mamy pewność, że zmiany nie zepsuły istniejącej funkcjonalności.

Automatyzacja testów to także dobre rozwiązanie, gdy nie chcemy tracić czasu na ręczne wykonywanie testów na wszystkich możliwych platformach i przeglądarkach. W takim przypadku warto zainwestować w narzędzia do testowania aplikacji w różnych przeglądarkach i systemach operacyjnych, takie jak <a href="https://www.selenium.dev/">Selenium</a>.

### Dokumentacja

Dokumentacja to ważny element każdego projektu, służący do opisania działania aplikacji oraz jej funkcjonalności. Narzędziem służącym do tworzenia dokumentacji w Pythonie jest SPHINX. Pozwala on na tworzenie dokumentacji w różnych formatach, takich jak HTML, LaTeX, epub, czy zwykły tekst. Możliwe jest również przekształcenie pliku w formacie LaTeX do PDF.

Aby zbudować szkielet dokumentacji, wystarczy uruchomić komendę:

    quickstart

SPHINX zapyta cię o kilka szczegółów dotyczących projektu, na podstawie których wygeneruje odpowiednie pliki startowe i wypełni je treścią.

Aby utworzyć dokumentację z plików konfiguracyjnych, użyj komendy:

    make html

Program poinformuje cię o pomyślnym utworzeniu dokumentacji, jeśli w trakcie procesu nie pojawią się żadne błędy. W przeciwnym razie proces tworzenia dokumentacji zostanie przerwany, a na konsoli zostaną wyświetlone komunikaty o błędach.

#### reStructuredText

Plikiem startowym dokumentacji jest `index.rst`. Zapisany jest on w formacie `reStructuredText`, który jest rozszerzeniem języka markdown. Jego głównym atutem jest możliwość instalowania przydatnych pluginów. Linkowanie plików jest również uproszczone, co jest ważne w dokumentacji. Komenda `make html` generuje na podstawie plików z rozszerzeniem `.rst` odpowiadające im pliki html.

#### Jak pisać dobrą dokumentację?

1. Zacznij od tutoriali.
  - Pokaż użytkownikowi jak zainstalować oraz uruchomić twoją aplikację.
  - Przygotuj scenariusze użycia programu.
  - Zaprezentuj, do czego służy każdy z elementów graficznych.
  - Tutoriale to nie to samo co dokumentacja, ale dobrze przygotowane poradniki pozwolą ci zebrać wiele informacji, które później możesz przetworzyć na dokumentację.
2. Korzystaj z narzędzi automatyzujących pracę.
  - Sphinx pozwala na tworzenie dokumentacji w różnych formatach.
  - Jeśli używasz języka Python, skorzystaj z modułu <code>docstrings</code>, który umożliwia tworzenie dokumentacji bezpośrednio w plikach źródłowych.
3. Pamiętaj o aktualności dokumentacji.
  - Utrzymuj dokumentację w równowadze z aktualną wersją aplikacji.
  - W razie zmian w kodzie, pamiętaj o odpowiednim zaktualizowaniu dokumentacji.
4. Staraj się być zrozumiały.
  - Unikaj skomplikowanych zwrotów i nieznanych szerzej pojęć.
  - Jeśli masz taką możliwość, dodaj przykłady użycia.
5. Dopracuj szczegóły.
  - Zadbaj o poprawność gramatyczną i ortograficzną.
  - Dodaj linki do dokumentacji zewnętrznych bibliotek, jeśli korzystasz z nich w swoim projekcie.
6. Utrzymuj porządek.
  - Dokumentacja powinna być czytelna i przejrzysta.
  - Dziel informacje na krótkie rozdziały i sekcje.
7. Zachęcaj do zgłaszania błędów i propozycji ulepszeń.
  - Jeśli użytkownicy znajdą błędy lub będą mieć propozycje ulepszeń, chętnie przyjmij ich uwagi.

#### Automatyczne generowanie dokumentacji do API

Jeśli tworzysz aplikację z interfejsem API, warto zadbać o automatyczne generowanie dokumentacji, która będzie zawierała wszystkie dostępne endpointy, opis ich działania, a także informacje o przyjmowanych i zwracanych parametrach. W Pythonie jednym z popularnych narzędzi do tego celu jest <a href="https://www.sphinx-doc.org/en/master/">Sphinx</a>.

Aby skorzystać z tej funkcjonalności, należy zainstalować rozszerzenie <code>sphinx-apidoc</code> i uruchomić go z odpowiednimi opcjami. W folderze z dokumentacją należy wywołać polecenie:

    sphinx-apidoc -o docs/source/api/ <ścieżka do katalogu z kodem>

To polecenie utworzy plik <code>api.rst</code> z automatycznie wygenerowaną dokumentacją. Następnie należy dodać go do pliku <code>index.rst</code>, aby pojawił się w głównym menu dokumentacji.

    .. toctree::
       :maxdepth: 2
       :caption: Spis treści:

       api

Po uruchomieniu polecenia <code>make html</code> będzie można zobaczyć wygenerowaną dokumentację na stronie internetowej.

#### Linki

* https://developers.google.com/style

### Pliki wykonywalne i PyInstaller

Jeśli chcesz udostępnić swoją aplikację innym osobom, prawdopodobnie będziesz chciał zapakować ją w plik wykonywalny. W przypadku systemu Windows najprostszym sposobem na stworzenie pliku wykonywalnego jest użycie programu <a href = "https://www.pyinstaller.org/">PyInstaller</a>.

Aby użyć PyInstaller, należy zainstalować go za pomocą pip:

    pip install pyinstaller

Następnie możesz wygenerować plik wykonywalny za pomocą polecenia:

    pyinstaller nazwa_pliku.py

Po wykonaniu polecenia zostanie utworzony folder dist, w którym znajdziesz plik wykonywalny o nazwie nazwa_pliku.exe. Możesz go umieścić w dowolnym miejscu na dysku i uruchomić.

PyInstaller ma również opcje pozwalające na dostosowanie sposobu tworzenia plików wykonywalnych do swoich potrzeb. Przykładowo, możesz wybrać, czy chcesz zawrzeć w pliku wykonywalnym zasoby (np. obrazy, dźwięki), czy też chcesz udostępnić je osobno. Możesz także określić, czy plik wykonywalny ma być uruchamiany w oknie konsoli, czy też w osobnym oknie. Więcej informacji o opcjach dostępnych w PyInstaller znajdziesz w <a href = "https://pyinstaller.readthedocs.io/en/stable/index.html">dokumentacji</a>.

### Kod bajtowy
Moduł `dis` służy do wyświetlania kodu bajtowego dla funkcji lub bloków kodu. Aby wyświetlić kod bajtowy dla funkcji, użyj funkcji `dis()` w nastęþujący sposób:

    from dis import dis

    def suma(a, b):
      return a + b

    dis(suma)

Aby wyświetlić kod bajtowy dla bloku kodu, użyj funkcji `disassemble()`:

    from dis import disassemble

    code = """
    def suma(a, b):
      return a + b
    """

    disassemble(code)

Kod bajtowy jest przydatny w przypadku gdy chcesz zrozumieć, jak interpreter konwertuje kod napisany w Pythonie na instrukcje, które są wykonywane przez maszynę. Może to być również pomocne przy optymalizacji kodu lub tworzeniu wtyczek do Pythona w innych językach.
    
Aby uzyskać kod z zewnętrznych bibliotek musimy użyć modułu <code>inspect</code>. Biblioteka ta umożliwia uzyskanie informacji o strukturze programu. Może być używana do zapisywania lub odczytywania kodu źródłowego, dokumentacji i innych informacji o obiektach.

Niektóre przydatne funkcje w module inspect to:

* `inspect.getsource(object)` - zwraca kod źródłowy obiektu jako string
* `inspect.getdoc(object)` - zwraca dokumentację obiektu jako string
* `inspect.getmembers(object)` - zwraca listę krotek (name, value) dla wszystkich atrybutów obiektu
* `inspect.isclass(object)` - zwraca True, jeśli obiekt jest klasą
* `inspect.isfunction(object)` - zwraca True, jeśli obiekt jest funkcją
* `inspect.ismethod(object)` - zwraca True, jeśli obiekt jest metodą

Przykład użycia:

    import inspect
    import tkinter

    print(inspect.getsource(tkinter.Tk)) # podejzyj kod klasy Tk z modulu tkinter
    print(inspect.getdoc(tkinter.Tk)) # podejzyj docstring klasy Tk z modulu tkinter

## Python w praktyce

W tej części przyjrzymy się różnym aspektom pracy z językiem Python w praktyce. Omówimy wiele narzędzi i bibliotek, które mogą być przydatne podczas tworzenia wszelakiego oprogramowania.

Początkowo skupimy się na obsłudze argumentów linii poleceń i pracy z plikami i folderami. Następnie przyjrzymy się bibliotece Pandas i sposobom obsługi plików CSV. Kolejnym tematem będzie praca z plikami PDF oraz uzyskiwanie informacji o systemie operacyjnym.

Przejdziemy również do tematów związanych z siecią, takich jak HTTP oraz prosty serwer. Nie zabraknie również wprowadzenia do tworzenia API za pomocą biblioteki FastAPI oraz pracy z bazami danych za pomocą SQLite.

Na końcu zapoznamy się z biblioteką Tkinter do tworzenia interfejsu graficznego oraz narzędziem do gromadzenia logów.

### Argumenty linii poleceń

Python obsługuje argumenty linii poleceń. Jeśli chcemy, by nasz skrypt był sterowany przez argumenty przekazywane podczas jego uruchomienia, mamy do dyspozycji kilka narzędzi, które ułatwią nam to zadanie.

Moduł biblioteki standardowej sys zawiera zmienną argv, która przechowuje nazwę programu oraz listę argumentów przekazanych z linii poleceń. Zakłada się, że argumenty są oddzielone spacjami.

Przykładowo, jeśli mamy skrypt o nazwie suma.py i chcemy, by po jego uruchomieniu skrypt wypisał sumę argumentów przekazanych z linii poleceń, możemy to zrobić w następujący sposób:

    import sys
    print(sum(sys.argv[1:]))
    
Dla następującej kombinacji liczb powinniśmy otrzymać następujący wynik:

    $ python suma.py 3 2 1
    6

Jeśli chcielibyśmy używać flag do nazywania dostępnych opcji, możemy nadal użyć sys.argv, ale będziemy musieli napisać parser do obsługi wszystkich możliwych kombinacji flag. Łatwiej skorzystać z gotowego narzędzia. Również w bibliotece standardowej mamy moduł *argparse*. Moduł ten daje nam opcję zdefiniowania możliwych do użycia argumentów.

Załóżmy, że chcemy by nasz skrypt przyjmował nazwę pliku jako argument, a następnie dopisywał na końcu pliku wiersz "nowy wiersz". Możemy to zrobić w następujący sposób:

    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser()
    parser.add_argument("plik", help="sciezka do pliku ktory chcesz zmodyfikowac")
    args = parser.parse_args()

    plik = Path(args.plik)
    nowy_wiersz = "nowy wiersz"
    plik.write_text(plik.read_text() + nowy_wiersz)

Jeśli teraz uruchomimy plik bez argumentu, to zostanie wyświetlony komunikat o błędzie:

    $ python3 script.py 
    usage: script.py [-h] plik
    script.py: error: the following arguments are required: plik

Mamy możliwość wyświetlenia pomocy dla naszego skryptu. Moduł *argparse* generuje pomoc automatycznie na podstawie argumentów, jakie ustawiliśmy.

    $ python3 script.py -h
    usage: script.py [-h] plik

    positional arguments:
      plik        sciezka do pliku ktory chcesz zmodyfikowac

    options:
      -h, --help  show this help message and exit

Jeśli chcemy by argument był opcjonalny to przy dodawaniu go musimy ustawić pole *required* na *False*.

    parser.add_argument("--argument", help="Opcjonalny argument", required=False)

Inne opcje to połączenie argumentu z flagą, nadanie wartości domyślnej oraz ustawienie oczekiwanego typu:

    parser.add_argument("-a", "--argument", help="Argument z wartością domyślną", type=int, default=10, required=False)

### Praca z plikami i folderami

Standardowa biblioteka Pythona zawiera wiele funkcji do pracy z plikami i folderami. Skrypty Pythona mogą być używane do automatyzacji prostych zadań biurowych.

#### Otwarcie pliku 

Do otwierania plików w Pythonie używamy funkcji open(). Funkcja ta przyjmuje ścieżkę do pliku oraz tryb otwarcia. Po użyciu funkcji open() należy pamiętać o wywołaniu funkcji close(), aby zamknąć plik. Możemy to zrobić ręcznie lub skorzystać z konstrukcji with, która automatycznie zamknie plik po jej zakończeniu.

    # otwarcie pliku w trybie odczytu
    plik = open("sciezka/do/pliku.txt", "r")

    ...

    plik.close()

    # lub z wykorzystaniem konstrukcji with
    with open("sciezka/do/pliku.txt", "r") as plik:
        ...

Istnieją 4 standardowe tryby otwarcia pliku:

1. <code>r</code> - odczytywanie.
1. <code>r+</code> - odczytywanie oraz modyfikacja.
1. <code>w</code> - modyfikacja wraz z usunięciem poprzedniej treści.
1. <code>a</code> - modyfikacja wraz z dopisaniem nowej treści do poprzedniej treści pliku.

#### Odczytywanie i zapisywanie danych

Aby odczytać zawartość pliku, możemy skorzystać z funkcji readlines(), która zwraca listę napisów. Każdy napis w liście reprezentuje kolejny wiersz pliku. Aby zapisać dane do pliku, używamy funkcji write. Funkcja ta przyjmuje jeden argument, napis, gdzie kolejne wiersze powinny być oddzielone znakiem *\n*.

    with open("sciezka/do/pliku.txt") as plik:

        # odczytaj tresc pliku
        wiersze = plik.readlines()
        for wiersz in wiersze:
          print(wiersz)

        # zapisz nowa tresc do pliku
        plik.write("nowy tekst\nwiersz nr. 2\n")

#### Moduł pathlib

Moduł pathlib pojawił się w Pythonie w wersji 3.4. Jest to zestaw narzędzi, które umożliwiają pracę z plikami i folderami w sposób bardziej przyjazny dla użytkownika.

Oto kilka przykładów metod z tego modułu:

* `.exists()` - zwraca True jeśli plik lub folder o podanej ścieżce istnieje, w przeciwnym wypadku zwraca False.
* `.is_file()` - zwraca True jeśli obiekt Path reprezentuje plik, w przeciwnym wypadku zwraca False.
* `.is_dir()` - zwraca True jeśli obiekt Path reprezentuje folder, w przeciwnym wypadku zwraca False.
* `.read_text()` - odczytuje zawartość pliku jako napis.
* `.write_text()` - zapisuje napis do pliku.
* `.open()` - otwiera plik w trybie określonym przez drugi argument (domyślnie 'r').

Poniższy przykład pokazuje, jak można wykorzystać te metody:

    from pathlib import Path
    
    sciezka = Path("/sciezka/do/pliku.txt")

    # sprawdzenie, czy plik istnieje
    if sciezka.exists():
      print("Plik istnieje.")
    else:
      print("Plik nie istnieje.")

    # odczytanie zawartości pliku
    zawartosc = sciezka.read_text()
    print(zawartosc)

    # zapisanie nowej zawartości do pliku
    sciezka.write_text("Nowy tekst w pliku.")

Aby uzyskać obiekt reprezentujący folder, należy utworzyć obiekt klasy Path z odpowiednią ścieżką do folderu:

    folder = Path("sciezka/do/folderu")

Następnie możemy użyć metod tego obiektu, takich jak iterdir() do iterowania po plikach i folderach w danym folderze:

    for element in folder.iterdir():
        print(element)

Możemy również sprawdzić, czy obiekt jest plikiem czy folderem za pomocą metod is_file() i is_dir():

    if element.is_file():
        print("To jest plik")
    elif element.is_dir():
        print("To jest folder")

Inne przydatne metody to exists(), która sprawdza, czy dany element istnieje, oraz mkdir(), która tworzy nowy folder.

    if not folder.exists():
        folder.mkdir()

### Pandas i csv

Moduł Pandas to bardzo popularny moduł, używany do pracy z danymi tabelarycznymi. Do zapisywania danych tabelarycznych do pliku csv oraz odczytywania danych z pliku csv, służą nam funkcje <code>to_csv()</code> oraz <code>read_csv()</code>.

Załóżmy, że mamy tabelę przedstawiającą rachunki za prąd w wybranym domu. Chcemy zapisać tę tabelę do pliku csv, a następnie odczytać dane z tego pliku. Możemy to zrobić w następujący sposób:

    import pandas as pd

    # przygotowujemy dane do zapisania
    data = [["2022-01-01", 100], ["2022-02-01", 120], ["2022-03-01", 130]]
    df = pd.DataFrame(data, columns=["data", "kwota"])

    # zapisujemy dane do pliku csv
    df.to_csv("rachunki.csv", index=False)

    # odczytujemy dane z pliku csv
    df_odczytane = pd.read_csv("rachunki.csv")
    print(df_odczytane)

Wynikiem tego kodu będzie tabela o takim wyglądzie:

| data | kwota |
| ---- | ----- |
| 2022-01-01	| 100 |
| 2022-02-01	| 120 |
| 2022-03-01	| 130 |

#### Podstawowe informacje o tabeli

Po wczytaniu tabeli do pamięci, możemy wyświetlić podstawowe informacje o niej za pomocą funkcji `info()`.

    df.info()

Funkcja ta pokazuje nam takie informacje jak:

* ilość wierszy i kolumn,
* typy danych w poszczególnych kolumnach,
* ilość niezapełnionych pól.

#### Podgląd danych

Aby sprawdzić, jakie dane mamy w tabeli, możemy wyświetlić jej fragment za pomocą funkcji `head()` lub `tail()`. Domyślnie obie funkcje wyświetlają 5 pierwszych lub ostatnich wierszy tabeli. Możemy też podać ilość wierszy jaką chcemy wyświetlić jako argument.

    df.head(10) # pierwsze 10 wierszy
    df.tail() # ostatnie 5 wierszy

#### Selekcja kolumn

Aby wybrać konkretne kolumny z tabeli, możemy użyć notacji z nawiasami kwadratowymi.

    df[["kolumna_1", "kolumna_2"]]

#### Filtrowanie danych

Do filtrowania danych służy nam operator `[]`. Możemy użyć go w połączeniu z operatorami logicznymi, takimi jak `&` lub `|`.

Przykładowo, jeśli mamy tabelę zawierającą informacje o użytkownikach i interesują nas tylko ci użytkownicy, którzy mają więcej niż 30 lat, to możemy użyć następującej komendy:

    df.loc[df['Wiek'] > 30]

Jeśli chcemy pokazać użytkowników, którzy mają więcej niż 30 lat i mieszkają w Warszawie, to możemy użyć następującej komendy:

     df.loc[(df['Wiek'] > 30) & (df['Miasto'] == 'Warszawa')]


### Praca z plikami PDF
Istnieje kilka popularnych bibliotek do obsługi plików PDF. Jedną z najczęściej używanych jest biblioteka <code>PyPDF2</code>. Aby ją zainstalować, możemy użyć polecenia <code>pip install pypdf2</code>.

#### Otwieranie pliku PDF

Aby otworzyć plik PDF, używamy funkcji `PdfFileReader` z modułu `PyPDF2`.

    from PyPDF2 import PdfFileReader

    # otworz plik
    with open('plik.pdf', 'rb') as plik:
        reader = PdfFileReader(plik)

#### Wypisywanie informacji o pliku

Aby wyświetlić informacje o pliku, takie jak ilość stron, autor czy tytuł, możemy skorzystać z odpowiednich właściwości obiektu <code>PdfFileReader</code>:

    print(f"Ilość stron: {czytnik.getNumPages()}")
    print(f"Autor: {czytnik.getDocumentInfo().author}")
    print(f"Tytuł: {czytnik.getDocumentInfo().title}")

#### Odczytywanie tekstu

Aby wyświetlić zawartość pliku PDF, możemy użyć metody `getPage()`. Metoda `getPage()` oczekuje obiektu `PageObject` reprezentującego daną stronę. Metoda `getNumPages()` zwraca liczbę stron w pliku.

Poniższy kod wyświetla zawartość wszystkich stron pliku PDF:

    # pobierz liczbe stron
    liczba_stron = reader.getNumPages()

    # dla kazdej strony
    for strona in range(liczba_stron):
        # pobierz tekst strony
        tekst = reader.getPage(strona).extractText()
        # wyswietl tekst
        print(tekst)

#### Modyfikowanie pliku PDF

Aby modyfikować plik PDF, możemy użyć obiektu `PdfFileWriter` z modułu `PyPDF2`. Możemy dodawać nowe strony do pliku lub usuwać istniejące strony.

Poniższy kod dodaje nową stronę z tekstem "Hello, World!" do pliku:

    # utworz obiekt PdfFileWriter
    writer = PdfFileWriter()

    # dodaj nowa strone z tekstem
    writer.addPage(writer.newTextPage("Hello, World!"))

    # otworz plik do zapisu
    with open('nowy_plik.pdf', 'wb') as plik:
        # zapisz plik
        writer.write(plik)

#### Łączenie plików PDF

Możemy użyć poniższego kodu, aby połączyć wszystkie pliki PDF z listy:

    import os
    import glob
    from PyPDF2 import PdfFileMerger

    # utworzenie listy plikow
    pdf_files = []
    for filename in glob.glob('*.pdf'):
        pdf_files.append(filename)

    # utworzenie obiektu merger
    merger = PdfFileMerger()

    # laczenie plikow
    for pdf in pdf_files:
        merger.append(open(pdf, 'rb'))

    # zapis nowego pliku
    with open('sciezka/do/nowego_pliku.pdf', 'wb') as fout:
        merger.write(fout)
    
### Informacje o systemie operacyjnym

Moduł `os` w bibliotece standardowej umożliwia uzyskiwanie informacji o systemie operacyjnym oraz manipulowanie plikami i folderami.

Przykładowo, możemy uzyskać nazwę aktualnie używanego systemu operacyjnego za pomocą `os.name`:

    import os
    print(os.name)

#### Informacje o użytkownikach

Aby uzyskać informacje o użytkownikach systemu oraz grupach, możemy skorzystać z modułu `pwd`:

    import pwd

    # Pobierz informacje o użytkowniku
    user_info = pwd.getpwuid(os.getuid())
    print(f"Nazwa użytkownika: {user_info.pw_name}")
    print(f" ID użytkownika: {user_info.pw_uid}")
    print(f" ID grupy: {user_info.pw_gid}")
    print(f" Katalog domowy: {user_info.pw_dir}")

    # Pobierz informacje o grupie
    group_info = pwd.getgrgid(user_info.pw_gid)
    print(f" Nazwa grupy: {group_info.gr_name}")
    print(f" ID grupy: {group_info.gr_gid}")
    print(f" Lista użytkowników w grupie: {group_info.gr_mem}")

#### Dyski

Aby uzyskać informacje o dostępnych dyskach oraz wolnym miejscu na nich, możemy skorzystać z modułu `os.statvfs`:

    import os

    # Pobierz informacje o dysku
    disk_info = os.statvfs("/")
    print(f" Całkowita pojemność dysku: {disk_info.f_frsize * disk_info.f_blocks:,} bajtów")
    print(f" Wolne miejsce na dysku: {disk_info.f_frsize * disk_info.f_bfree:,} bajtów")

#### Informacje o procesorze

Moduł <code>os</code> z biblioteki standardowej zawiera funkcję <code>cpu_count()</code>, która zwraca liczbę rdzeni procesora. Możemy również uzyskać informacje o mocy obliczeniowej procesora za pomocą modułu <code>psutil</code>. Poniższy przykład pokazuje, jak wyświetlić liczbę rdzeni oraz moc obliczeniową procesora:

    import os
    import psutil

    # Liczba rdzeni procesora
    print(f"Liczba rdzeni procesora: {os.cpu_count()}")

    # Moc obliczeniowa procesora
    print(f"Moc obliczeniowa procesora: {psutil.cpu_freq().max} MHz")

#### Zmienne środowiskowe

Moduł <code>os</code> zawiera również funkcję <code>environ</code>, która zwraca słownik zawierający wszystkie zmienne środowiskowe. Możemy odczytać wartość konkretnej zmiennej środowiskowej, używając notacji słownikowej. Poniższy przykład pokazuje, jak wyświetlić zmienną środowiskową o nazwie SHELL:

    import os

    # Wyświetl zmienną środowiskową SHELL
    print(f"Zmienna środowiskowa SHELL: {os.environ['SHELL']}")

Aby zmienić zmienną środowiskową, można użyć funkcji `os.environ.update()`. Przykładowo, aby ustawić zmienną środowiskową o nazwie `VAR` na wartość value, można użyć następującego kodu:

    import os

    os.environ.update({'VAR': 'value'})

Uwaga: zmiany zmiennych środowiskowych zachodzą tylko w obrębie bieżącego procesu. Po zakończeniu działania skryptu zmiany te nie będą widoczne dla innych procesów. Aby zmiany zmiennych środowiskowych zostały zapisane dla całego systemu, należy je zapisać w odpowiednim pliku konfiguracyjnym (np. `/etc/environment` lub `/etc/bash.bashrc` w systemie Linux).

### HTTP i prosty serwer

HTTP (Hypertext Transfer Protocol) jest protokołem sieciowym używanym do przesyłania danych między klientem a serwerem. Jest to podstawowa technologia używana do przeglądania stron internetowych oraz komunikacji między aplikacjami.

Aby wysłać żądanie HTTP w Pythonie, można użyć modułu `requests`. Poniższy przykład pokazuje, jak wysłać żądanie typu `GET` do strony internetowej i otrzymać odpowiedź z serwera:

    import requests

    url = "https://www.google.com"
    response = requests.get(url)

    print(response.status_code) # sprawdzamy kod odpowiedzi
    print(response.text) # wyświetlamy zawartość odpowiedzi

Możliwe jest również wysyłanie żądań `POST`, `PUT`, `DELETE` itp. oraz dodawanie nagłówków i danych do żądania.

Jeśli chcesz stworzyć prosty serwer HTTP w Pythonie, możesz użyć modułu http.server. Poniższy przykład pokazuje, jak stworzyć serwer, który nasłuchuje na porcie 8000 i wyświetla zawartość pliku `index.html` po otrzymaniu żądania `GET`:

    import http.server
    import socketserver

    PORT = 8000

    Handler = http.server.SimpleHTTPRequestHandler

    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("serving at port", PORT)
        httpd.serve_forever()

Możesz również dostosować handler, aby obsługiwać różne typy żądań i odpowiednio reagować na nie.

### API wraz z FastAPI

FastAPI to nowoczesne i szybkie narzędzie do tworzenia API w Pythonie. Jest oparte na bibliotece Starlette i używa Pydantic do walidacji danych wejściowych.

Aby rozpocząć pracę z FastAPI, należy najpierw zainstalować je za pomocą komendy:

    pip install fastapi

Przykład prostego API z FastAPI:

    from fastapi import FastAPI

    app = FastAPI()

    @app.get("/")
    def read_root():
        return {"Hello": "World"}

API może przyjmować różne metody HTTP (np. `GET`, `POST`, `DELETE`) oraz zwracać różne formaty danych (np. JSON, HTML).

    from fastapi import FastAPI
    from pydantic import BaseModel

    app = FastAPI()

    class Item(BaseModel):
        name: str
        description: str = None
        price: float
        tax: float = None

    @app.post("/items/")
    def create_item(item: Item):
        return item

W powyższym przykładzie zdefiniowano nowy model danych - Item, który jest walidowany przy użyciu Pydantic. Następnie zdefiniowano nową ścieżkę `/items/` dostępną dla metody POST, która przyjmuje obiekt item i zwraca go jako odpowiedź.

FastAPI posiada też mechanizm do automatycznej generacji dokumentacji dla API. Aby skorzystać z tej funkcjonalności, należy użyć dekoratora `@app.docs` i odpowiednio opisać poszczególne ścieżki i modele danych.

    from fastapi import FastAPI
    from pydantic import BaseModel

    app = FastAPI()

    class Item(BaseModel):
        name: str
        description: str = None
        price: float
        tax: float = None

    @app.post("/items/")
    @app.docs(
        summary="Create a new item",
        description="This endpoint allows you to create a new item in the store",
        responses={
            200: {"description": "Success"},
            404: {"description": "Not found"},
        },
    )
    def create_item(item: Item):
        return item

Aby uruchomić aplikację, wystarczy wywołać metodę `run()` na obiekcie reprezentującym aplikację:

    if __name__ == "__main__":
        app.run()

Po uruchomieniu aplikacji możesz otworzyć adres `http://localhost:8000/` w przeglądarce, aby zobaczyć odpowiedź zwróconą przez endpoint.

FastAPI oferuje również możliwość walidacji danych wejściowych i zwracanych przez endpointy. Możesz użyć typów Pythona, takich jak `int` lub `str`, aby opisać argumenty wejściowe oraz typ zwracany przez endpoint. FastAPI automatycznie sprawdzi, czy dane wejściowe są poprawne.

### Bazy danych z SQLite
Istnieje wiele baz danych. Każda ma swoje wady i zalety. Baza danych SQLite jest niezależna od systemu operacyjnego i nie wymaga instalacji żadnego dodatkowego oprogramowania. Zaletą SQLite jest prostota użytku. Nie potrzeba nam żadnego serwera, cała baza danych może zostać sprowadzona do jednego pliku, który w programie jest w całości załadowany do pamięci RAM.

Przykładowe zbiory danych możesz pobrać z następujących stron:
* <a href="https://data.gov/">data.gov</a>
* <a href="https://www.kaggle.com/">kaggle</a>

Moduł sqlite3 pozwala na obsługę bazy danych SQLite. 

#### Połączenie z bazą danych

Do połączenia z bazą danych należy użyć funkcji `connect()` z modułu sqlite3. Funkcja ta przyjmuje jako argument ścieżkę do pliku bazy danych. Jeśli podana baza danych nie istnieje, to zostanie ona utworzona.

    import sqlite3

    connection = sqlite3.connect("baza_danych.db")

#### Tworzenie tabel

Aby utworzyć tabelę w bazie danych, należy wywołać metodę `execute()` na obiekcie połączenia. Metoda ta przyjmuje jako argument polecenie SQL tworzące tabelę.

    connection.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)")

#### Dodawanie rekordów

Aby dodać rekord do tabeli, należy wywołać polecenie `INSERT INTO` za pomocą metody `execute()`.

    connection.execute("INSERT INTO users (username, password) VALUES (?, ?)", ("user1", "pass1"))
    connection.execute("INSERT INTO users (username, password) VALUES (?, ?)", ("user2", "pass2"))

#### Pobieranie danych

Aby pobrać dane z tabeli, należy wywołać polecenie `SELECT` za pomocą metody `execute()`. Metoda ta zwraca obiekt cursor, z którego można pobrać rekordy za pomocą metody `fetchall()`.

    cursor = connection.execute("SELECT * FROM users")
    users = cursor.fetchall()
    print(users)  # [(1, 'user1', 'pass1'), (2, 'user2', 'pass2')]

#### Zamykanie połączenia

Po zakończeniu pracy z bazą danych należy wywołać metodę `close()` na obiekcie połączenia.

    connection.close()

### Tkinter
Tkinter jest modułem biblioteki standardowej, który służy do tworzenia interfejsów graficznych (GUI). Możemy z niego korzystać, aby tworzyć proste aplikacje okienkowe.

Tworzenie okna głównego za pomocą Tkinter wygląda następująco:

    import tkinter as tk

    root = tk.Tk()
    root.mainloop()

Możemy dodać różne elementy interfejsu, takie jak przyciski, etykiety, pola tekstowe i inne. Przykład dodania przycisku:

    import tkinter as tk

    def przycisk_klik():
        print("Kliknięto przycisk")

    root = tk.Tk()
    przycisk = tk.Button(root, text="Kliknij mnie", command=przycisk_klik)
    przycisk.pack()
    root.mainloop()

Możemy również ustawić różne opcje dla elementów interfejsu, takie jak rozmiar, kolor tła, itp. Przykład:

    import tkinter as tk

    root = tk.Tk()
    etykieta = tk.Label(root, text="Witaj w Tkinter", font=("Helvetica", 16), bg="yellow")
    etykieta.pack()
    root.mainloop()

Tkinter oferuje również możliwość tworzenia layoutów za pomocą ramki (frame). Możemy umieścić różne elementy w ramce i ustalić ich położenie za pomocą siatki (grid). Przykład:

    import tkinter as tk

    root = tk.Tk()

    frame = tk.Frame(root)
    frame.pack()

    przycisk1 = tk.Button(frame, text="Przycisk 1")
    przycisk2 = tk.Button(frame, text="Przycisk 2")
    przycisk3 = tk.Button(frame, text="Przycisk 3")

    przycisk1.grid(row=0, column=0)
    przycisk2.grid(row=0, column=1)
    przycisk3.grid(row=0, column=2)

    root.mainloop()
    
#### Zdarzenia

mamy możliwość obsługi zdarzeń za pomocą metody `bind()`. Zdarzenia mogą być generowane przez użytkownika lub system. Do najczęściej używanych zdarzeń należą:

* `<Button-1>` - kliknięcie lewym przyciskiem myszy na komponencie
* `<ButtonRelease-1>` - puszczenie lewego przycisku myszy nad komponentem
* `<Double-Button-1>` - podwójne kliknięcie lewym przyciskiem myszy na komponencie
* `<Enter>` - najechanie myszką na komponent
* `<Leave>` - zjechanie myszką z komponentu
* `<Key>` - naciśnięcie dowolnego klawisza na klawiaturze
* `<Return>` - naciśnięcie klawisza Enter

Aby obsłużyć zdarzenie, wystarczy wywołać metodę `bind()` na obiekcie komponentu, przekazując do niej nazwę zdarzenia oraz funkcję obsługi zdarzenia.

Przykładowo, jeśli chcemy wyświetlić komunikat po najechaniu myszką na przycisk, możemy użyć następującego kodu:

    from tkinter import Button, Tk

    def mouse_over(event):
        print("Myszka najechała na przycisk")

    root = Tk()
    button = Button(root, text="Przycisk")
    button.bind("<Enter>", mouse_over)
    button.pack()
    root.mainloop()

Możemy też użyć dekoratora `@event_decorator` do obsługi zdarzeń. W tym przypadku nie musimy już ręcznie wywoływać metody `bind()`, a dekorator automatycznie połączy funkcję z odpowiednim zdarzeniem.

    from tkinter import Button, Tk

    root = Tk()
    button = Button(root, text="Przycisk")

    @button.event_decorator("<Enter>")
    def mouse_over(event):
        print("Myszka najechała na przycisk")

    button.pack()
    root.mainloop()

### Logi

Większość programów, które tworzyliśmy w obrębie tego kursu, była jednorazowo uruchamiana i od razu zamykana. W prawdziwym świecie programy mogą działać godzinami, dniami lub nawet całymi latami. W takim przypadku wypadałoby poza samym efektem działania programu co jakiś czas otrzymać od programu informacje o tym, co aktualnie robi, wraz z ewentualnymi komunikatami o błędach. Takie informacje, zwane logami, są często zapisywane do osobnego pliku.

Moduł `logging` zawiera wiele przydatnych funkcjonalności do tworzenia logów.

Mamy dostępnych kilka poziomów logów:

| poziom | wartość |
| ------ | ------- | 
| CRITICAL | 50 | 
| ERROR | 40 | 
| WARNING | 30 | 
| INFO | 20 | 
| DEBUG | 10 | 
| NOTSET | 0 | 

Rzućmy okiem na prosty przykład, gdzie wypisujemy na konsoli komunikat "Przykładowa wiadomość":

    import logging

    logging.basicConfig(level=logging.INFO)
    logging.info("Przykladowa wiadomosc.")

Aby zapisać logi do pliku potrzebujemy obiektu do obsługi plików:

    import logging

    logger = logging.getLogger()

    fh = logging.FileHandler('plik.log')
    fh.setLevel(logging.WARNING)
    logger.addHandler(fh)

    logger.warning("Przykladowa wiadomosc.")

## Dodatkowe materiały

* https://docs.python.org/3/tutorial/
* https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/
* https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0002-introduction-to-computational-thinking-and-data-science-fall-2016/
* https://braydie.gitbook.io/how-to-be-a-programmer/
* https://pythontutor.com/visualize.html#mode=edit
* https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/
