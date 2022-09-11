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
    - [Organizacja-projektu-z-testami](#Organizacja-projektu-z-testami)
    - [Dokumentacja](#Dokumentacja)
    - [Pliki-wykonywalne-i-PyInstaller](#Pliki-wykonywalne-i-PyInstaller)
    - [Kod-bajtowy](#Kod-bajtowy)
  - [Python-w-Praktyce](#Python-w-Praktyce)
    - [Praca-z-plikami-i-folderami](#Praca-z-plikami-i-folderami)
    - [Pandas-i-csv](#Pandas-i-csv)
    - [Praca-z-plikami-PDF](#Praca-z-plikami-PDF)
    - [Informacje-o-systemie-operacyjnym](#Informacje-o-systemie-operacyjnym)
    - [HTTP-i-prosty-serwer](#HTTP-i-prosty-serwer)
    - [API-wraz-z-FastAPI](#API-wraz-z-FastAPI)
    - [Bazy-danych-z-SQLite](#Bazy-danych-z-SQLite)
    - [Tkinter](#Tkinter)
    - [Logi](#Logi)
    - [Kompresja-i-szyfrowanie-danych](#Kompresja-i-szyfrowanie-danych)
  - [Dodatkowe-materiały](#Dodatkowe-materiały)

<!--te-->

## Podstawy

Fundamenty języka Python. Nauka budowania programów. Podstawy algorytmiki.

### Instalacja w systemie Windows

Aby zainstalować Pythona w systemie Windows, należy wykonać następujące kroki:

1. Odwiedź stronę [Python.org](https://www.python.org/downloads/).
2. Wybierz odpowiednią wersję Pythona.
3. Pobierz instalator i przejdź przez proces instalacji.

### Interaktywna konsola

Otwórz konsolę Pythona i wpisz:

    >>> python
    python 2.7.13 (default, Sep  2 2019, 20:42:59)

Zostanie wyświetlona informacja o wersji Pythona dostępnej w systemie.

Z poziomu konsoli masz dostęp do wszystkich komend zdefiniowanych w danej wersji Pythona. Po wpisaniu komendy i naciśnięciu klawisza *Enter*, zostanie od razu zwrócony wynik wykonania danej instrukcji.

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
- Liczby całkowite (*int*) 
- Liczby zmiennoprzecinkowe (*float*) 
- Napisy (*string*) 
- Typ logiczny (*bool*) 

Zmienne są podstawą każdego języka programowania. Nazwa zmiennej może składać się z liter i cyfr, ale nie może zaczynać się od cyfry. Python nie ogranicza długości nazw. Dobry programista nadaje zmiennym nazwy reprezentujące ich zadanie w kodzie. Dzięki temu program jest czytelny, a co za tym idzie łatwiejszy w utrzymaniu.

Czy wiesz jaka liczba zostanie wypisana na konsoli w poniższym przykładzie?

    a = 3
    b = a
    b = 5
    print(a) # ???

### Warunki

Typ logiczny może przyjmować jedną z dwóch wartości <code>True</code> lub <code>False</code>. Typ logiczny ma istotne znaczenie dla instrukcji warunkowej. 

Przy porównaniach początkujący programiści często zapominają, że pojedynczy znak równości to przypisanie.

- <code>x = 5</code> w taki sposób zapiszemy w zmiennej x wartość 5.
- <code>x == 5</code> w taki sposób sprawdzimy czy zmienna x przechowuje wartość 5.

Instrukcja warunkowa ma następującą postać:

    if warunek:
        kod
    else:
        kod

Część kodu umieszczona w pierwszym wcięciu po instrukcji warunkowej <code>if</code> zostanie wykonana jedynie, gdy warunek zostanie oceniony na prawdziwy. Gdy warunek nie jest spełniony, ta część kodu zostanie całkowicie pominięta, a zamiast niej wykonany zostanie kod umieszczony w drugim wcięciu (pod słowem kluczowym <code>else</code>). Instrukcje warunkowe zwane są też czasami instrukcjami sterującymi.

Operatory logiczne służą do łączenia warunków. W Pythonie mamy do dyspozycji trzy operatory logiczne: <code>and</code>, <code>or</code> i <code>not</code>: 

* <code>and</code> – aby wyrażenie było prawdziwe, oba warunki muszą być prawdziwe.
* <code>or</code> – aby wyrażenie było prawdziwe, tylko jeden warunek musi być prawdziwy.
* <code>not</code> – zaprzeczenie wyrażenia.

Wyrażenie <code>a != 0 and b == 5</code> będzie prawdziwe, jeśli oba warunki są spełnione, tzn. jeśli *a* jest różne od 0 i jednocześnie *b* jest równe 5.

Wyrażenie <code>x % 2 == 0 or x % 7 == 0</code> będzie prawdziwe, jeśli jeden z warunków jest spełniony, tzn. jeśli *x* jest podzielne przez 2 lub *x* jest podzielne przez 7.

Czy wiesz co zostanie wypisane na konsoli w poniższym przykładzie? 

    odpowiedz = "TAK"
    print(odpowiedz == "tak" or "TAK")

### Pętle

Pętle wraz z instrukcjami warunkowymi to podstawa wszystkich języków programowania. Pętla umożliwia wielokrotne wykonanie pojedynczej instrukcji lub całego bloku instrukcji. Oprócz bloku instrukcji każda pętla ma również warunek zakończenia. Pętla powtarza blok instrukcji, dopóki nie zostanie spełniony warunek kończący pętlę. W Pythonie mamy dwie pętle <code>For</code> oraz <code>While</code>. 

#### For
Pętla <code>For</code> ogólnie ma postać:

    for element in kolekcja: 
        kod

Na razie do tworzenia pętli będziemy używać funkcji <code>range()</code>. Funkcja ta może przyjmować jeden, dwa lub trzy parametry.

1. <code>range(10)</code> utworzy ciąg *(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)*, tak więc pętla: <code>for x in range(10)</code> zostanie wykonana 10 razy.
2. <code>range(5, 12)</code> utworzy ciąg *(5, 6, 7, 8, 9, 10, 11)*, tak więc pętla: <code>for x in range(5, 12)</code> zostanie wykonana 7 razy.
3. <code>range(0, 50, 10)</code> utworzy ciąg *(0, 10, 20, 30, 40)*, tak więc pętla: <code>for x in range(0, 50, 10)</code> zostanie wykonana 5 razy.

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

Funkcje to zamknięty pod jedną nazwą blok instrukcji. Blok teb może być sterowany z zewnątrz poprzez przekazywanie argumentów. Definicja funkcji polega na określeniu, jakie instrukcje należą do ciała funkcji, ile argumentów funkcja oczekuje oraz za pomocą jakiej nazwy będzie wywoływana w innych miejscach kodu. Sama definicja nie uruchamia jeszcze żadnych instrukcji. Dopiero użycie nazwy funkcji wraz z wartościami argumentów w innym miejscu kodu sprawia, że instrukcje zostają wykonane. Funkcja ma następującą postać:

    def nazwa_funkcji(argumenty):
        kod # cialo funkcji

Ciało funkcji może być dowolnie rozbudowane, ale zaleca się, by większe funkcje rozbijać na mniejsze, każdą o jednym, jasno określonym celu. W taki sposób zmniejszana jest złożoność kodu, przez co staje się on czytelniejszy.

Zdefiniowaną funkcję wywołujemy w kodzie poprzez jej nazwę. Przykład:

    # w tym miejscu definiuje funkcje
    def ryba():
       print('rybka')

    # w tym miejscu wywoluje funkcje
    ryba()

Funkcje mogą mieć dowolną ilość argumentów. Możliwe jest zarówno stworzenie funkcji bez argumentów, jak i funkcji z 10 argumentami. Przykład:

    def ryba(argument):
        # oczekujemy, że argument będzie liczbą naturalną
        for i in range(argument):
            print('ryba')

Użycie słowa kluczowego <code>return</code> spowoduje wyjście z funkcji (instrukcje umieszczone poniżej nie zostaną wykonane). Poprzez <code>return</code> możemy również przekazać do reszty programu wartość z wnętrza funkcji. Taka wartość po wywołaniu funkcji jest często zapisywana w zmiennej w innym miejscu programu.

    def suma_trzech(a, b, c):
        return a + b + c

    suma_a = suma_trzech(3, 6, 2)
    suma_b = suma_trzech(4, 1, 7)

### Napisy

<code>String</code> to tekstowy typ danych. Tutaj będziemy nazywali go napisem. Napis składa się z ciągu znaków. Znakami mogą być litery, znaki interpunkcyjne, jak również i cyfry.

W Pythonie napis deklarujemy, używając apostrofów bądź cudzysłowów. 

    napis = 'James' 
    napis = "James" 
    napis = '''James''' 

Nie ma oddzielnego typu dla pojedynczego znaku. Pojedynczy znak to napis o długości równej 1. Napisy są indeksowane od 0 tak jak i listy. Do konkretnego znaku w danym napisie możemy odwołać się poprzez jego indeks. 

Przykładowo dla kodu <code>James = 'Lubie go'</code>, wywołanie <code>James[0]</code> zwróci literę 'L'. Wywołanie <code>James[2]</code> zwróci literę 'b'. 

Zainicjalizowany napis nie może jest modyfikowalny. To znaczy, nie możemy zrobić czegoś takiego: <code>James[0]='z'</code>. Jeśli chcemy wprowadzić zmiany do napisu, musimy aktualny napis nadpisać nowym napisem.

    napis = "pierwotny"
    napis = "nowy"
    
Aby w napisie użyć, wartości innej zmiennej musimy przed cudzysłowami postawić literkę <code>f</code>, a w cudzysłowie w odpowiednim miejscu między nawiasami klamrowymi nazwę zmiennej, której chcemy użyć.

    liczba = 3
    nspid = f"twoja liczba to: {liczba}"

### Struktury danych

Algorytm to skończona lista kroków (instrukcji). Kroki te sprawdzają, kopiują, usuwają, czy w inny sposób manipulują danymi.
Struktury danych to sposoby na przechowywanie danych w pamięci komputera. Dzięki ich implementacjom w Pythonie możemy do całej kolekcji danych (a nie tylko pojedynczej zmiennej) odnosić się przy pomocy jednej nazwy. Istnieje bardzo wiele struktur danych, które różnią się oferowanymi funkcjonalnościami oraz szybkością ich wykonania.

* Listy: elementy są uporządkowane i można je zmieniać. W liście mogą występować duplikaty.
* Krotki: elementy są uporządkowane i nie można ich zmieniać. W krotce mogą występować duplikaty.
* Zbiory: elementy są nieuporządkowane, nieindeksowane i nie można ich zmieniać. W zbiorze mogą występować duplikaty.
* Słowniki: elementy są nieuporządkowane, indeksowane i można je zmieniać. Wszystkie klucze w słowniku są unikalne. Wśród wartości mogą występować duplikaty.

#### Lista

List używamy, gdy chcemy mieć kilka wartości dostępnych pod jedną nazwą.

Przykład listy składającej się z kilku liczb całkowitych:

    lista = [3, 2, 3, 9, 10]
    
Elementy listy nie muszą być tego samego typu:

    lista = ['a', True, 0.3]

Aby znaleźć liczbę elementów listy, użyj: 
       
    len(lista)
       
Aby dodać element *a* na koniec listy, użyj:

    lista.append(a)

Aby dodać wszystkie elementy z lista2 na koniec lista1, użyj:

    lista1.extend(lista2)

Aby wstawić element *a* na pozycję i, użyj:

    lista.insert(i,a)

Aby usunąć pierwsze wystąpienie elementu *a* w liście, użyj:

    lista.remove(a)

Aby usunąć element z listy znajdujący się na pozycji i oraz zwrócić go jako wynik, użyj:

    lista.pop([i])

Aby znaleźć liczbę wystąpień elementu *a* w liście, użyj:

    lista.count(a)

Aby posortować listę, użyj:

    lista.sort()

Aby odwrócić kolejność elementów w liście, użyj:

    lista.reverse()

Aby przy pomocy pętli przejść przez elementy listy, użyj:

    for element in lista: 
        print(element)
        
 Aby otrzymać element i indeks, użyj funkcji enumerate:
 
     for indeks, element in enumerate(lista): 
        print(f'{indeks}: {element}')

Aby przy pomocy pętli przejść przez elementy dwóch list równej długości, użyj:

     for elem_a, elem_b in zip(lista_a, lista_b): 
        print(f'element a: {elem_a}; element b: {elem_b}')

#### Krotka

Krotek zamiast list, używamy gdy:
* Liczy się szybkość.
* Chcemy zabezpieczyć dane przed nadpisaniem.

Przykład krotki składającej się z kilku liczb całkowitych:

    krotka = (3, 2, 3, 9, 10)
    
Aby znaleźć liczbę elementów krotki, użyj:

    len(krotka)

Aby dodać element *a* na koniec krotki, użyj:

    krotka = krotka + (a,)

Aby dodać wszystkie elementy z krotka2 na koniec krotka1, użyj:

    krotka1 = krotka1 + krotka2

Aby znaleźć indeks pierwszego wystąpienia elementu *a* w krotce, użyj:

    krotka.index(a)

Aby sprawdzić, czy element *a* występuje w krotce, użyj:

    a in krotka

Aby otrzymać wartość elementu z krotki znajdującego się na pozycji i, użyj:

    krotka[i]

Aby rozpakować krotkę składającą się z trzech elementów i zapisać je w trzech zmiennych, użyj:

    a, b, c = krotka

#### Zbiór

Zbiory są przydatne, gdy chcemy, by wszystkie elementy w kolekcji były unikalne. Dodatkowo dla zbiorów mamy zaimplementowane wiele przydatnych funkcji, pozwalających w prosty sposób pracować na kilku zbiorach jednocześnie.

Przykład zbioru składającego się z kilku liczb całkowitych:

    zbior = {3, 2, 3, 9, 10}

Aby znaleźć liczbę elementów zbioru, użyj:

    len(zbior)

Aby dodać element *a* do zbioru, użyj:

    zbior.add(a)

Aby usunąć element *a* ze zbioru, użyj:

    zbior.remove(a)

Aby sprawdzić, czy element *a* występuje w zbiorze, użyj:

    a in zbior

Aby sprawdzić, czy zbiór zawiera w sobie wszystkie elementy zbioru zbior2, użyj:

    zbior.issuperset(zbior2)

Aby znaleźć część wspólną dwóch zbiorów, użyj:

    zbior.intersection(zbior2)

Aby znaleźć elementy zbioru zbior1, które nie są w zbiorze zbior2, użyj:

    zbior1.difference(zbior2)

#### Słownik

Słowniki przydatne są, gdy chcemy użyć innych indeksów niż numeryczne. Dodatkowo słowniki są mega szybkie.

Przykład słownika, którego kluczami są napisy a wartościami liczby całkowite:

    slownik = {'a': 3, 'k': -2, 'b': 10}

Aby znaleźć liczbę elementów słownika, użyj:

    len(slownik)

Aby dodać element b do słownika i zapisać go pod kluczem a, użyj:

    slownik[a] = b

Aby usunąć element ze słownika pod kluczem a, użyj:

    del slownik[a]

Aby sprawdzić, czy klucz występuje w słowniku, użyj:

    a in slownik

Aby sprawdzić, czy wartość występuje w słowniku, użyj:

    b in slownik.values()

Aby wypisać klucze i wartości słownika, użyj:

    for klucz, wartosc in slownik.items():
        print(klucz, wartosc)

Aby klucze i wartości posortować wg kluczy, użyj:

    for klucz, wartosc in sorted(slownik.items(), key=lambda x: x[0]):
        print(klucz, wartosc)

Aby klucze i wartości posortować wg wartości, użyj:

    for klucz, wartosc in sorted(slownik.items(), key=lambda x: x[1]):
        print(klucz, wartosc)

Uwaga nie wszystkie typy możemy domyślnie użyć jako kluczy w słowniku! Kluczami mogą być jedynie obiekty haszowalne, czyli takie, które posiadają metodę <code>__hash__()</code>. Przykładowo kluczem słownika nie może być lista, ale może być napis.

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

- instrukcja <code>random.random()</code> wylosuje liczbę zmiennoprzecinkową z przedziału od *0* do *1*.
- <code>random.uniform(a,b)</code> wylosuje liczbę zmiennoprzecinkową z przedziału od *a* do *b*.
- instrukcja <code>random.randint(a,b)</code> wylosuje liczbę całkowitą z przedziału od *a* do *b*.

Najprostszy przykład rozkładu prawdopodobieństwa to rozkład jednostajny. Dla jednostajnego rozkładu prawdopodobieństwa mamy stałą wartość gęstości prawdopodobieństwa na danym przedziale <code>[a,b]</code>. Poza tym przedziałem wartość gęstości prawdopodobieństwa wynosi 0. 

Dla rozkładu Gaussa wartości zbliżone do średniej mają znacznie większe prawdopodobieństwo wystąpienia niż te oddalone od średniej. Jeśli na jakąś wielkość wpływa dostatecznie wiele czynników, to rozkład prawdopodobieństwa będzie zbliżony do krzywej Gaussa. Dokładniej mówi o tym centralne twierdzenie graniczne. 

## Średniozaawansowane

Zaawansowane konstrukcje języka Python. Programowanie zorientowane obiektowo. Implementacja własnych struktur danych.

### Klasy i obiekty
Klasa to otoczka dla grupy danych oraz funkcji pracujących na tych danych. Obiekt to instancja klasy. Mamy całkowitą dowolność w tworzeniu klas, możemy użyć dowolnej kombinacji danych lub nawet stworzyć klasę, która nie trzyma żadnych danych. Nie oznacza to, że każda klasa ma sens. Przy projektowaniu klasy musimy zastanowić się jakie dane powinny być trzymane wspólnie pod jedną nazwą oraz jakie funkcje przydałby się do pracy z tymi danymi.

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

#### Dostęp do zmiennych w obiektach

Dostęp do zmiennych odbywa się poprzez podanie nazwy obiektu, następnie kropki oraz nazwy zmiennej, którą chcemy odczytać:

    nazwa_obiektu.nazwa_zmiennej
    
Modyfikacja wartości przechowanych w zmiennych odbywa się tak samo, jak dla zwykłych zmiennych.

    osoba = Osoba("Jan", "Kowalski")
    print(osoba.imie) # Zostanie wyswietlone Jan
    osoba.imie = "Adam"
    print(osoba.imie) # Zostanie wyswietlone Adam

Mamy również możliwość przy każdym odczycie i modyfikacji wartości zmiennych przechowywanych w obiektach wywołać zdefiniowaną przez nas funkcję. Do tego celu służą dekoratory <code>@property</code> oraz <code>@nazwa_zmiennej.setter</code>.

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
       
#### Pola i metody statyczne

Pola i metody statyczne w odróżnieniu od zwykłych pól i metod nie należą do konkretnych obiektów tylko do całej klasy. Pola statyczne to wszystkie pola zdefiniowane z poziomu klasy. Przy ich definicji nie używamy parametru <code>self</code> ani żadnych specjalnych słów kluczowych. Przy definiowaniu metod statycznych musimy natomiast użyć dekoratora <code>@staticmethod</code>. Dostęp do pól i metod statycznych odbywa się zarówno poprzez nazwę klasy, jak i nazwy obiektów klasy.

    class Czlowiek:
      liczba_glow = 1

      @staticmethod
      def wyswietl_glowy():
        print(f'Liczba glow: {Czlowiek.liczba_glow}')

    Czlowiek.wyswietl_glowy() # Liczba glow: 1

    przykladowy_czlowiek = Czlowiek()
    przykladowy_czlowiek.wyswietl_glowy() # Liczba glow: 1

Metody klasowe to poszerzone metody statyczne. Przy definiowaniu metod klasowy używamy dekoratora <code>@classmethod</code>. Pierwszym parametrem metod klasowych jest nazwa klasy, klasycznie zwana <code>cls</code>. Dzięki temu możemy metody klasowe wywoływać w zwykłych metodach należących do tej samej klasy.

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

### Referencje i kopiowanie

Przekazując obiekt do funkcji, przekazujemy go poprzez referencję. Podobnie przypisując obiekt do nowej nazwy, przypisujemy referencję do pierwotnego obiektu. Wszelkie zmiany na nowym obiekcie będą miały odzwierciedlenie również na pierwotnym obiekcie i vice versa.

    lista = [[1, 2, 3], [4, 5, 6]]
    nowa_lista = lista
    
    nowa_lista.append([-1, -2, -3]) # modyfikuje obie listy
    nowa_lista[0].insert(1, 1)      # modyfikuje obie listy
    print(lista)
    
 Mamy jeszcze dwa inne sposoby na kopiowanie wartosci z oryginalnego obiektu do nowego obiektu:
 
 1. Kopiowanie płytkie

Na naszym poprzednim przykładzie z listą 2d, kopiowanie płytkie utworzy nowy obiekt dla zewnętrznej listy, ale wewnętrzne listy będą przekazane przez referencję.
    
    import copy
    lista = [[1, 2, 3], [4, 5, 6]]
    nowa_lista = copy.copy(lista)
    
    nowa_lista.append([-1, -2, -3]) # modyfikuje jedynie nowa liste
    nowa_lista[0].insert(1, 1)      # modyfikuje obie listy
    print(lista)

 2. Kopiowanie głębokie 

Jeśli chcemy utworzyć nowe obiekty zarówno dla zewnętrznej listy, jak i wewnętrznych list musimy użyć kopiowania głębokiego.

    import copy
    lista = [[1, 2, 3], [4, 5, 6]]
    nowa_lista = copy.deepcopy(lista)

    nowa_lista.append([-1, -2, -3]) # modyfikuje jedynie nowa liste
    nowa_lista[0].insert(1, 1)      # modyfikuje jedynie nowa liste
    print(lista)

### Czyste funkcje i skutki uboczne

Nad funkcje produkujące skutki uboczne preforowane są czyste funkcje.

Skutki uboczne to m.in.:

* Zmiany w plikach.
* Zmiany w bazie danych.
* Wysyłanie informacji przez sieć.
* Zmiany w globalnych zmiennych.

Obiekty mutowalne mogą łatwo zostać zmienione w niepożądany sposób (np. przy zmianie kolejności wywoływania funkcji). Preferujemy więc obiekty niemutowalne, które dają nam większe poczucie bezpieczeństwa kosztem zwiększonego wydajności.

Bezpieczniejsze funkcje to takie, które zamiast modyfikować stan obiektów mutowalnych, zwracają nowy obiekt, nie dotykając się do obiektów przekazanych jako parametry.

### Dziedziczenie i kompozycja

Dziedziczenie i kompozycja to dwa mechanizmy pozwalające na użycie w jednej klasie kodu z innej klasy. 

Dziedziczenie kopiuje z klasy nadrzędnej wszystkie elementy do klasy podrzędnej. W klasie podrzędnej mamy bezpośredni dostęp do wszystkich pól klasy nadrzędnej i możemy również wywoływać jej wszystkie metody, tak jakby były wywoływane w klasie, która je zdefiniowała. Istnieje możliwość zmiany definicji metod klasy nadrzędnej w klasie podrzędnej. Dziedziczenie jest używane, gdy nowa klasa jest szczególnym rodzajem już istniejącej klasy.

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


Istnieje kilka rodzajów kompozycji. Najprostszym przykładem jest zapisanie obiektu jednej klasy jako pole innej klasy. Definiowana klasa zawiera w sobie inną klasę. W nowo definiowanej klasie nie mamy bezpośredniego dostępu do pól oraz metod innej klasy, ale możemy się do nich dostać poprzez instancję tej klasy. Nie możemy zmienić definicji metod klasy zawartej w naszej klasie. Kompozycji używamy, gdy nowa klasa reprezentuje pewną całość, której istniejąca klasa jest częścią.

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

### Wyrażenia regularne

Pracując z tekstem niejednokrotnie chcemy wyszukać słowo, wiersz bądź zdanie, ale nie mamy jednego sztywnego klucza tylko wzorzec. Przykładowo chcemy znaleźć wszystkie słowo zaczynające się od *abc* lub składające się wyłącznie z małych liter oraz cyfr parzystych. Filtrowanie to następny przykład zadania do którego wykorzystywane są wzorce. Przykładowo chcemy usunąć z tekstu wszystkie liczby. 

Powiedzmy, że mamy plik gdzie każdy wiersz zawiera trzy informacje oddzielone ukośnikami: nazwisko pracownika, datę odczytu, oraz odczyt licnzika. Jak wyciągnąć datę z wiersza? Używając klasycznych funkcji znanej nam klasy <code>String</code> moglibyśmy to zrobić w ten sposób:

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

#### Schemat pracy z wyrażeniami regularnymi

1. Zbuduj najprostszą wersję wyrażenia regularnego pasującą do twojego problemu. 
1. Zawsze testuj czy wyrażenie regularne znajduje TYLKO to, co chcesz, by zostało znalezione. Łatwo o wynik fałszywie pozytywny.
1. Rozszerz wyrażenie regularne o inne przypadki.

### Wyjątki
Wyjątkami nazywamy sytuacje, które uniemożliwiają poprawne wykonanie danego bloku kodu. Tym samym terminem określany jest również mechanizm języka Python pozwalający na radzenie sobie z tymi sytuacjami. 

Istnieje szereg wyjątków zdefiniowanych w standardzie Pythona. Przykładowo jeśli spróbujemy podzielić liczbę przez 0, zostanie wywołane wyjątek <code>ZeroDivisionError</code>.

    print(5 / 0)

Tak, więc wyjątki możemy spotkać, jeśli niepoprawnie użyjemy funkcji bądź operatorów zdefiniowanych w standardzie języka. Możemy również sami wywołać wyjątki. Uwaga, nic nie chroni nas przed wywołaniem wyjątku w nieodpowiednim miejscu. Naszym zadaniem jest dbanie o to, aby wywołanie wyjątku było wykonane w odpowiedniej sytuacji. 

    raise ValueError("Podano nieprawidlowa wartosc")

#### Obsługa wyjątków

Nieobsłużony wyjątek zamyka program i wyświetla informację o błędzie. Mechanizm try/except pozwala na obsługę wyjątków.

    try:
        # kod, ktory moze wywolac wyjatek
    except:
        # kod, ktory zostanie wykonany w przypadku wystapienia wyjatku
    else:
        # kod, ktory zostanie wykonany gdy wyjatek nie wystapil
    finally:
        # kod, ktory zawsze zostanie wykonany

W mechanizmie try/except szczególnie ważny jest kod, który wykonuje się w przypadku wystąpienia wyjątku. Wyjątek informuje nas o błędzie i nie powinniśmy go ignorować. Z tego powodu nie umieszczaj <code>pass</code> w bloku except.

Dodatkowo <code>except</code> pozwala nam sprecyzować typ wyjątku jaki ma zostać obsłużony. Jeśli w bloku <code>try</code> może wystąpić więcej niż jeden typ wyjątku to należy przygotować odpowiednią liczbę bloków <code>except</code>. 

    try:
        # kod, ktory moze wywolac wyjatek
    except ValueError:
        # kod, ktory zostanie wykonany w przypadku wystapienia wyjatku ValueError
    except TypeError:
        # kod, ktory zostanie wykonany w przypadku wystapienia wyjatku TypeError

Nie należy próbować łapać ogólnego wyjątku, gdyż wszystkie wyjątki dziedziczą po klasie <code>Exception</code>. 

#### Własny wyjątek

W Pythonie mamy możliwość tworzenia włanych wyjątków. Aby utworzyć własny wyjątek, należy dziedziczyć po klasie <code>Exception</code>.

    class WlasnyWyjatek(Exception):
        def __init__(self, *args, **kwargs):
            komunikat = "Opis błędu jaki wystąpił"
            super().__init__(komunikat, *args, **kwargs)

#### Wyjątki jako mechanizm przepływu sterowania

Innym zastosowaniem wyjątków jest użycie ich jako mechanizm przepływu sterowania. W poniższym przykładzie używamy wyjątku do sprawdzenia, czy napis reprezentuje liczbę całkowitą:

    def czy_liczba(napis):
      try:
        int(napis)
      except ValueError:
        return False
      return True

### Wątki
### Procesy
### Asyncio
### Lambdy

Wyrażenia lambda to funkcje składające się wyłącznie z jednego wiersza instrukcji definiowane przy pomocy słowo kluczowego <code>lambda</code>. Lambdy nie używają słowa kluczowego <code>return</code>, gdyż zawsze zwracają wynik wykonania tworzącego je wiersza instrukcji. 

    def zwykla_funkcja(liczba: int) -> int:
      return liczba**2
    
    przyklad_lambdy = lambda liczba: liczba**2
    
    wartosc = 2
    
    print(zwykla_funkcja(wartosc)) # 4
    print(przyklad_lambdy(wartosc)) # 4
    print((lambda liczba: liczba**2)(wartosc)) # 4

W porównaniu do znanych nam pełnoprawnych funkcji definiowanych poprzez słowo kluczowe <code>def</code>, lambdy są znacznie ograniczone:
  - mamy do dyspozycji jedynie jeden wiersz instrukcji.
  - jest możliwość sprawdzenia warunku, ale nie można zagnieżdżać warunków.
  - brak opcji tworzenia zmiennych, jak i przypisania wartości do zmiennych już istniejących (dla obiektów możemy użyć <code>setattr()</code>).
  - brak pętli.
  
Nasuwa się pytanie, po co tworzyć nowy mechanizm będący ograniczoną wersją już istniejącego? Otóż dzięki lambdom możemy znacznie ograniczyć liczbę wierszy kodu, a co za tym idzie poprawić czytelność kodu. Niejednokrotnie chcemy wykorzystać funkcję jedynie raz, zamiast tworzyć nową pełnoprawną funkcję przy użyciu słowa kluczowego <code>def</code>, możemy użyć lambdy.

    lista = (('def', 100), ('ghi', 200), ('abc', 300))
    print(sorted(lista, key=lambda x: x[0])) # [('abc', 300), ('def', 100), ('ghi', 200)]
    print(sorted(lista, key=lambda x: x[1])) # [('def', 100), ('ghi', 200), ('abc', 300)]

### Programowanie funkcyjne

Funkcja <code>map()</code> ma dwa parametry:
  1. Nazwa funkcji przyjmującej jeden argument (może to być też wyrażenie lambda).
  2. Nazwa listy.

Wynikiem działania <code>map()</code> jest nowa lista, której elementy to wyniki wywołania funkcji przekazanej jako pierwszy argument dla każdego elementu listy przekazanej jako drugi argument.

Alternatywnymi konstrukcjami do funkcji <code>map()</code> są:
  1. Pętla for.
  2. Wyrażenia listowe.

Porównajmy wyrażenia listowe i funkcję <code>map()</code>:

    lista = [5, 10, 15, 20, 25, 30, 35, 40]

    lista_a = [elem // 5 for elem in lista] # [1, 2, 3, 4, 5, 6, 7, 8]
    lista_b = list(map(lambda elem : elem // 5, lista)) # [1, 2, 3, 4, 5, 6, 7, 8]

Funkcja <code>filter()</code> działa podobnie jak funkcja <code>map()</code> z tym że jej wynikiem jest nowa lista, której elementy to elementy listy przekazanej jako drugi argument dla których wywołania funkcji przekazanej jako pierwszy argument zwróciły wartość logiczną True.

Porównajmy wyrażenia listowe i funkcję <code>filter()</code>:

    lista = [5, 10, 15, 20, 25, 30, 35, 40]

    lista_a = [elem // 5 for elem in lista if elem % 2 == 0] # [2, 4, 6, 8]
    lista_b = list(map(lambda elem : elem // 5, filter(lambda elem : elem % 2 == 0, lista))) # [2, 4, 6, 8]

W poniższym przykładzie pokazane są dwa sposoby na utworzenie listy składającej się z numerów ASCII odpowiadających wielkim literom otrzymanego słowa:

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

Tworzenie klas niejednokrotnie wiąże się z pisaniem wielu powtarzalnych elementów, takich jak inicjalizacja zmiennych argumentami funkcji __init__ oraz operatory porównania. Klasy danych (data classes) automatyzują te powtarzalne procesy i jedyne czego potrzebujemy, to deklaracja pól w obrębie klasy. Są one szczególnie przydatne, gdy klasa, którą piszemy ma na celu głównie grupowanie danych.

    @dataclass(unsafe_hash=True, order=True)
    class RGB:
      czerwony: int
      zielony: int
      niebieski: int


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

Generator jest bardzo podobny do funkcji zwracającej listę. Zamiast w jednym ruchu zwracać pełną tablicę, to zwraca on wartości pojedynczo. Dzięki temu  generatory wymagają mniej pamięci, a co więcej daje to klientowi możliwość rozpoczęcia przetwarzania pierwszych zwróconych wartości, za nim jeszcze generator ukończy swoją pracę.

Przyjrzyjmy się dwóm programom:

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

Wiemy już, że przy pomocy pętli <code>for</code> możemy przejść przez kolejne elementy listy:

    for elem in lista:
       print(elem)

Standardowo wszystkie kolekcje w Pythonie mają zaimplementowaną funkcję It <code>__iter__()</code> zwracjącą ich iterator. Wywołanie funckji <code>next()</code> z przekazanym jako argument iteratorem da nam kolejny w sekwencji element kolekcji. Ostatni element wyrzuca wyjątek <code>StopIteration</code>,

    lista = [1, 2, 3]
    iterator = iter(lista)
    print(next(iterator)) # wyswietli 1
    print(next(iterator)) # wyswietli 2
    print(next(iterator)) # wyswietli 3
    print(next(iterator)) # zostanie wyrzucony wyjatek

Ten mechanizm jest używany wewnętrznie przez pętlę for. Iteratory pozwalają na implementacje własnych zasad przechodzenia przez kolekcję.

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
      
### Dekoratory

Dekorator to funkcja, która przyjmuje inną funkcję jako argument. Dekorator może przetworzyć funkcję przekazaną jako argument, połączyć ją z inną funkcją (funkcjami) lub podmienić ją na inną funkcję. Połączenie funkcji z dekoratorem spowoduje wywołanie dekoratora w momencie wywołania funkcji.

Przykład dekoratora dodającego <code>print('przetwarzam dane')</code> przed wywołaniem funkcji dekorowanej:

    def dekoruj(funkcja):
      def funkcja_wew():
        print('przetwarzam dane')
        funkcja()
      return funkcja_wew

Mamy dwa równoważne sposoby na połączenie dekoratora z funkcją, którą chcemy dekorować:

    # sposob 1:
    @dekoruj
    def foo():
     print('funkcja foo()')

    # sposob 2:
    def foo():
     print('funkcja foo()')

    foo = dekoruj(foo)

### Serializacja

Załóżmy, że napisałeś prostą grę, w której gracz może zdobywać punkty doświadczenia. Jeśli chcesz, żeby po ponownym uruchomieniu programu gracz mógł wznowić grę w dokładnie tym samym miejscu, gdzie poprzednio ją zakończył, to musisz w jakiś sposób zapisać tę informację. Serializacja to proces konwertowania obiektu na strumień bajtów w celu otworzenia jego stanu.

Popularnym modułem do serializacji i deserializacji obiektów w Pythonie jest <code>pickle</code>.

Funkcja <code>dumps()</code> służy do serjalizacji obiektu na strumień bajtów. Strumień ten można według życzenia zapisać do pliku, wysłać do innego procesu lub wrzucić na serwer.

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

Funkcja <code>loads()</code> służy do odtwarzania stanu obiektów ze strumienia bajtów.

    with open(sciekza, 'rb') as plik:
      czlowiek = pickle.load(plik)
      print(czlowiek) #Imie: James, numer: 10

## Inżynieria oprogramowania

Poza znajomością samego języka programowania, do tworzenia oprogramowania programista musi jeszcze poznać szereg konwencji oraz narzędzi używanych w profesjonalnym środowisku.

### Moduły i pakiety

Za każdym razem, gdy używamy instrukcji <code>import</code>, to importujemy do naszego skryptu zewnętrzny moduł. Dzięki temu zabiegowi wszystkie funkcje, klasy oraz zmienne globalne z danego modułu są dostępne w skrypcie, który go importuje. <a href="https://docs.python.org/3/library/index.html">Dokumentacja</a> zawiera pełną listę wbudowanych modułów biblioteki standardowej Pythona. Moduły możemy również tworzyć sami.

    import requests
    print(type(requests)) # <class 'module'>

Każdy plik Pythona jest modułem, którego nazwa to nazwa pliku bez rozszerzenia *.py*. Pakiet jest folderem z modułami zawierającym dodatkowy plik *__init__.py*, który potrzebny jest, aby odróżnić pakiet od zwykłego folderu.

    .
    └── nazwa_paczki
        ├── __init__.py
        └── przykladowy_skrypt_a.py
        └── przykladowy_skrypt_b.py
        └── przykladowy_skrypt_c.py

### Wersje Pythona

<code>Pyenv</code> używany jest do izolowania różnych wersji Pythona. Na przykład jeśli chcesz przetestować swój kod w Pythonie 2.5, 3.6 i 3.10, potrzebujesz łatwego sposobu na przełączanie się między nimi. <code>Pyenv</code> modyfikuje zmienną środowiskową PATH dodając do niej ścieżkę do specjalnego folderu <code>(pyenv root)/shims</code>. <code>Pyenv</code> ułatwia również proces pobierania i instalowania różnych wersji Pythona za pomocą polecenia <code>pyenv install</code>.

Linki:

* https://github.com/pyenv/pyenv
* https://github.com/pyenv-win/pyenv-win

### PIP i PyPI

PIP to program, który pozwala na instalację pakietów Pythona dostępnych na stronie <a href="https://pypi.org/">PyPI</a>.

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

Poprawny z punktu widzenia interpretera kod można często napisać na wiele sposobów. Mało tego nawet jedna linia kodu może być zazwyczaj zapisana na więcej niż jeden sposób. Jedną z możliwych przyczyn różnic jest formatowanie. Przykładowo w kodzie do oddzielania instrukcji można użyć zarówno spacji, jak i tabów. Definicje funkcji można oddzielać jednym, dwoma lub trzema enterami. Linie kodu mogą być tak długie, że nie zmieszczą się na ekranie. Czy więc należy ograniczać ich długość? Jeśli tak, to ile dokładnie znaków powinno być górną granicą? Dopóki z kodem pracujemy sami, wszystkie te przykłady nie mają dla nas znaczenia. Sami możemy podejmować decyzje i w dowolnej chwili zmienić zdanie. Co ma jednak zrobić grupa programistów pracująca wspólnie nad jednym projektem? Czy powinni oni debatować jakie reguły są najlepsze i tracić w ten sposób cenny czas? Całe szczęście istnieje lista konwencji pisania kodu przygotowana przez twórców Pythona. Dwa główne dokumenty przedstawiające te konwencje to <code>PEP8</code> i <code>PEP257</code>. Dokumenty te definiują wytyczne do wszystkich poruszonych przez nas zagadnień, ale również wielu innych. Poza samymi suchymi regułami dokumenty te zawierają również wiele przykładów poprawnie, jak i niepoprawnie napisanego kodu.

Istnieje wiele narzędzi (tak zwanych linterów) sprawdzających, czy kod przestrzega wytycznych twórców Pythona.

<code>Black</code> nie pyta o zdanie, automatycznie zmienia formatowanie kodu na zgodne z PEP8.

<code>Pylint</code> to jeden z najpopularniejszych linterów Pythona. Daje nam trochę więcej wskazówek niż <code>Black</code>, który interesuje się jedynie formatowaniem. <code>Pylint</code> zwróci również uwagę na niepoprawne nazwy zmiennych (np. *a* lub *bb*), czy funkcje i klasy pozostawione bez objaśniających komentarzy (docstrings). Dodatkowo wiele narzędzi do CI/CD (np. Team City, czy Github Actions) zintegrowało <code>Pylint</code> ze swoim interfejsem graficznym. Wskazówki od <code>Pylint</code> nie modyfikują kodu automatycznie i trzeba wprowadzać je ręcznie.

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

Testowanie to proces, w którym uruchamiamy program (bądź jego część) z zamiarem sprawdzenia poprawności jego działania. Testy jednostkowe mają na celu weryfikację poprawności odizolowanej jednostki programu, najczęściej jednej funkcji.

* czerwone testy pokazują, że coś, co działało wcześniej, aktualnie nie działa.
* zielone testy nie oznaczają, że wszystko działa poprawnie, tylko że to, co było sprawdzane w testach działa poprawnie.
* więcej nie zawsze znaczy lepiej (ważenie się 10 razy dziennie nie sprawi, że szybciej schudniesz).

Ogólnie w Pythonie mamy dwie popularne biblioteki służące do testów jednostkowych: <code>unittest</code> i <code>pytest</code>.

#### Unittest

Zbudowany zgodnie z filozofią programowania obiektowego. Mamy klasy, dziedziczenie i tysiąc różnych funkcji <code>assert</code>. 
 
    import unittest
    
    class TestSMTP(unittest.TestCase):
      
      def smtp_connection(self):
        import smtplib
        return smtplib.SMTP("smtp.gmail.com", 587, timeout=5)

     def test_helo(self):
        response_code, msg = self.smtp_connection().ehlo()
        self.assertEqual(response_code, 250)

#### Pytest

Zbudowany zgodnie z filozofią im prościej, tym lepiej. Nie ma żadnych klas. Jest jedna funkcja <code>assert</code>. 

    import pytest
    
    @pytest.fixture
    def smtp_connection():
       import smtplib
       return smtplib.SMTP("smtp.gmail.com", 587, timeout=5)
    
    def test_helo(smtp_connection):
       response_code, msg = smtp_connection.ehlo()
       assert response_code == 250

#### Korzyści z testów jednostkowych

* Pomagają innym programistom zrozumieć, co miał robić dany fragment kodu produkcyjnego.
* Gdy programy są małe, programista może ręcznie sprawdzić ich działanie z każda modyfikacja. Wraz ze wzrostem złożoności, ręczne testowanie wszystkich części programu staje się niemożliwe.
* Testy jednostkowe wymuszają przynajmniej minimalną separację zadań między fragmentami kodu.

#### TDD

Technika "test driven development" to sposób pisania programów gdzie testy pisane są przed kodem produkcyjnym. Program pisany jest w trzyetapowych cyklach:

1. Testy jednostkowe.
2. Kod produkcyjny.
3. Refkatoryzajca kodu produkcyjnego.

Programista nigdy nie przechodzi do implementacji nowych funkcjonalności, dopóki wszystkie trzy etapy nie zostały zakończone dla funkcjonalności aktualnie implementowanych.

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

#### Od znalezienia buga do poprawnie działającego kodu

Znaleziono bug w twoim programie. Co robić?

1. Spróbuj odtworzyć problematyczną sytuację. Przykładowo powiedzmy, że twoja aplikacja zamyka się po wciśnięciu na przycisk mający przenieść użytkownika na inną stronę. Najpierw manualnie wykonaj wszystkie kroki prowadzące do pojawienia się niechcianego efektu.
1. Wytrop w kodzie, który fragment jest odpowiedzialny za pojawienie się znalezionego błędu.
1. Dodaj test mający sprawdzić, czy niepożądana sytuacja występuje po wykonaniu wytropionego fragmentu kodu. Przykładowo, jeśli błąd pojawia się po wywołaniu funkcji <code>foo()</code>, to najpierw znajdź test <code>test_foo()</code> i upewnij się, że funkcja <code>foo()</code> wywoływana jest wraz z parametrami, przy których pojawia się błąd. Dodaj test wykrywający wystąpienie niepożądanej sytuacji. Po uruchomieniu testu otrzymasz czerwony komunikat. 
1. W kolejnym kroku przyjdzie ci naprawić funkcję <code>foo()</code>. Test z czerwonego powinien stać się zielony. W przyszłości dbaj o to, by test już zawsze pozostał zielony.
1. Zanim wyślesz zmiany do centralnego repozytorium, rzuć raz jeszcze na nie okiem. Zastanów się, czy twoja łatka mogłaby być napisana inaczej, być może wpadniesz na prostsze rozwiązanie. 

#### Inne typy testów

Zgodnie z zaleceniami autora <a href="https://www.oreilly.com/library/view/software-engineering-at/9781492082781/">"Software Engineering at Google"</a> testy należy rozdzielić na trzy kategorie w następujących proporcjach:

* 80% testy jednostkowe
* 15% testy integracyjne
* 5% testy całego systemu (end-to-end)

#### Automatyczna generacja danych na potrzeby testów

Staraj się obok kodu aplikacji tworzyć skrypty generujące zasoby potrzebna aplikacji. Przykładowo załóżmy, że piszesz aplikację, która w tle komunikuje się z bazą danych MySQL. Powinieneś mieć dostępny pod ręką skrypt, który automatycznie zbuduje taką bazę danych i wypełni ją przykładowymi tabelami. Dzięki temu nie musisz czekać na testy w środowisku produkcyjnym i już w czasie pisania programu, możesz od razu upewnić się, że twój kod działa poprawnie. Dodatkowo masz możliwość automatycznego testowania całego programu.

### Organizacja projektu z testami

Typowe projekty progamistyczne podzielone są na kilka pakietów oraz podmodułów. Przykładowo nasza aplikacja może wyglądać w ten sposób:

    projekt
    ├── przykladowy_pakiet
    │   ├── __init__.py
    │   └── modul_a.py
    │   └── modul_b.py
    └── tests
        ├── __init__.py
        └── test_modul_a.py
        └── test_modul_b.py

Testy powinny być rozdzielone między różne moduły podobnie jak pliki źródłowe. W ten sposób z jednej strony ograniczymy wielkość plików  z testami, a z drugiej strony ułatwimy wszystkim życie, gdyż znacznie łatwiej będzie zlokalizować konkretny test.

Aby wywołać wszystkie testy, użyj:

a) Dla modułu <code>unittest</code>:

    $ python -m unittest discover
    
b) Dla modułu <code>pytest</code>:

    $ pytest tests/

Aby wywołać tylko testy z konkretnego modułu, użyj:

a) Dla modułu <code>unittest</code>:

    $ python -m unittest tests.test_modul_a

b) Dla modułu <code>pytest</code>:

    $ pytest tests/test_modul_a.py

### Dokumentacja

Jednym z najpopularniejszych narzędzi do zarządzania dokumentacją w Pythonie jest <a href ="https://www.sphinx-doc.org/en/master/">SPHINX</a>. Jego głównymi zaletami są prostota obsługi oraz ogrom dostępnych opcji. Z pomocą tego narzędzia możesz tworzyć dokumentację w różnych formatach, takich jak HTML, LaTeX, epub, czy zwykły tekst. Można również łatwo dokonać konwersji pliku w formacie LaTeX na PDF.

Użyj komendy <code>quickstart</code>, aby zbudować szkielet dokumentacji. Będziesz musiał odpowiedzieć na kilka pytań (tak lub nie), a na podstawie twoich odpowiedzi SPHINX wygeneruje odpowiednie pliki startowe i wypełni je treścią.

    quickstart

Aby utworzyć dokumentację z plików konfiguracyjnych, należy użyć komendy <code>make</code> wraz z formatem, w jakim chcemy, aby zapisana została dokumentacja.

    make html

Program poinformuje cię o pomyślnym utworzeniu dokumentacji, jeśli w trakcie procesu <code>make</code> nie napotkał żadnych problemów. W przeciwnym razie proces tworzenia dokumentacji zostanie przerwany, a na konsoli zostaną wyświetlone komunikaty o błędach. Przykładową przyczyną wystąpienia błędu może być umieszczenie linku do nieistniejącego pliku.

#### reStructuredText

Plikiem startowym dokumentacji jest <code>index.rst</code>. Plik ten zapisany jest w formacie zwanym reStructuredText, a w skrócie rst. Jest to rozszerzenie języka mark down, innego języka znaczników. Jego głównym atutem jest możliwość instalowania przydatnych pluginów. Uproszczony został również proces linkowania plików, co jest znaczące dla dokumentacji.  Komenda <code>make html</code> generuje na podstawie wszystkich plików z rozszerzeniem *.rst* odpowiadające im pliki html.

#### Jak pisać dobrą dokumentację?

1. Zacznij od tutoriali.
  - Pokaż użytkownikowi jak zainstalować oraz uruchomić twoją aplikację.
  - Przygotuj scenariusze użycia programu. 
  - Opisz dokładnie wszystkie dostępne funkcje. 
  - Zaprezentuj, do czego służy każdy z elementów graficznych.
  - Tutoriale to nie to samo co dokumentacja, ale dobrze przygotowane poradniki pozwolą ci zebrać wiele informacji, które po przekształceniu do ściślejszej formy mogą stanowić bazę dokumentacji.
2. Wyjaśnij, jak działa twój program za kulisami. Odpowiedz na następujące pytania: 
  - Jakie technologie zostały użyte oraz w jakim celu?
  - Jakie elementy składowe tworzą aplikację?
  - Jakie trudności zostały napotkane przy pisaniu kodu oraz jak zostały rozwiązane?
  - Jakie decyzje zostały podjęte przy projektowaniu aplikacji?
3. Na koniec warto również dodać referencje do komentarzy (docstrings) umieszczonych w naszym kodzie. W szczególności szczegółowo opisane powinno zostać wszelkie zewnętrzne API (interfejs programistyczny aplikacji).

#### Automatyczne generowanie dokumentacji do API

Jeśli opisujesz swoje funkcje, klasy oraz moduły w kodzie to te komentarze (docstrings) mogą zostać wykorzystane do automatycznego generowania dokumentacji.

#### Linki

* https://developers.google.com/style

### Pliki wykonywalne i PyInstaller

Instalacja

    pip install pyinstaller
    
Przykład użycia z wiersza poleceń:

    pyinstaller --onefile sciezka_do_pliku.py

### Kod bajtowy

Do wyświetlania kodu bajtowego służy moduł <code>dis</code>:

    from dis import dis

    def suma(a, b):
      return a + b

    dis(suma)
    
Aby wyświetlić kod funkcji użyj modułu <code>inspect</code>:

    import inspect
    import tkinter

    print(inspect.getsource(tkinter.Tk)) # podejzyj kod klasy Tk z modulu tkinter
    print(inspect.getdoc(tkinter.Tk)) # podejzyj docstring klasy Tk z modulu tkinter

## Python w Praktyce

### Praca z plikami i folderami
### Pandas i csv
### Praca z plikami PDF
### Informacje o systemie operacyjnym

* zmienne środowiskowe

### HTTP i prosty serwer
### API wraz z FastAPI
### Bazy danych z SQLite
Istnieje wiele baz danych. Każda swoje wady i zalety. Zaletą SQLite jest prostota użytku. Nie potrzeba nam żadnego serwera, cała baza danych może zostać sprowadzona do jednego pliku, który w programie możemy w całości załadować do pamięci RAM.

Przykładowe zbiory danych możesz pobrać z następujących stron:
* <a href="https://data.gov/">data.gov</a>
* <a href="https://www.kaggle.com/">kaggle</a>

Do pracy z bazą danych SQLite służy moduł <code>sqlite3</code>.

Wiele funkcji z modułu <code>sqlite3</code> wymaga od nas by najpierw utworzyć obiekt <code>Connection</code> reprezentujący bazę danych.
W poniższym przykładzie ścieżka do bazy danych to 'przykladowa_baza_danych.db':

    import sqlite3
    polaczenie = sqlite3.connect('przykladowa_baza_danych.db')

Następnie wszystkie operacje wykounjemy przy pomocy kursora:

    kursor = conn.cursor()

Przykładowo chcemy utworzyć tabelę pracownicy:

    kursor.execute('''CREATE TABLE pracownicy (imie, nazwisko, stanowisko)''')
    kursor.execute("INSERT INTO stocks pracownicy ('Adam', 'Nowak', 'Programista')")

Aby zmiany zostały zapisane, musimy wysłać je do bazy danych:

    polaczenie.commit()

Pod koniec pracy z bazą danych zamykamy połączenie:

    polaczenie.close()

### Tkinter
### Logi

Większość programów, które tworzyliśmy w obrębie tego kursu były przez nas jednokrotnie uruchomiane i od razu zamykane. W prawdziwym świecie programy mogą działać godzinami, dniami lub nawet całymi latami. W takim przypadku wypadałoby poza samym efektem działania programu co jakiś czas otrzymać od programu informacje o tym, co aktualnie robi wraz z ewentualnymi komunikatami o błędach. Takie informacje zwane logami, są często zapisywane do osobnego pliku.

Moduł <code>logging</code> zawiera wiele przydatnych funkcjonalności do tworzenia logów. 

Mamy dostępnych kilka poziomów logów:

| poziom | wartość |
| ------ | ------- | 
| CRITICAL | 50 | 
| ERROR | 40 | 
| WARNING | 30 | 
| INFO | 20 | 
| DEBUG | 10 | 
| NOTSET | 0 | 

Rzućmy okiem na prosty przykład, gdzie wypisujemy na konsoli komunikat "Przykladowa wiadomosc":

    import logging

    logging.basicConfig(level=logging.INFO)
    logging.info("Przykladowa wiadomosc.")

Aby zapisać logi do pliku potrzebujemy obiektu do obsługi pików:

    import logging

    logger = logging.getLogger()

    fh = logging.FileHandler('plik.log')
    fh.setLevel(logging.WARNING)
    logger.addHandler(fh)

    logger.warning("Przykladowa wiadomosc.")

### Kompresja i szyfrowanie danych

## Dodatkowe materiały

* https://docs.python.org/3/tutorial/
* https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/
* https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0002-introduction-to-computational-thinking-and-data-science-fall-2016/
* https://braydie.gitbook.io/how-to-be-a-programmer/
* https://pythontutor.com/visualize.html#mode=edit
* https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/
