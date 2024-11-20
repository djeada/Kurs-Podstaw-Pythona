# Dziedziczenie i kompozycja

Dziedziczenie i kompozycja to dwa fundamentalne koncepty programowania obiektowego (OOP), które odgrywają kluczową rolę w tworzeniu elastycznego, modularnego i łatwego do utrzymania kodu. Oba podejścia mają swoje zalety i wady, a wybór między nimi zależy od konkretnego kontekstu i wymagań projektu.

## Dziedziczenie

Dziedziczenie to mechanizm, który pozwala jednej klasie (klasie potomnej) przejąć właściwości i zachowania innej klasy (klasy bazowej). Dzięki dziedziczeniu, programiści mogą tworzyć nowe klasy na podstawie istniejących, co pozwala na ponowne wykorzystanie kodu i redukcję jego złożoności.

Przepraszam za wcześniejsze niejasności. Oto poprawione diagramy, które lepiej ilustrują różnice między dziedziczeniem a kompozycją, używając różnych sposobów przedstawienia.

**Dziedziczenie (relacja "jest")**

Przedstawione jako drzewo hierarchii:

```
        [Pojazd]
           |
    ----------------
    |              |
[Samochód]     [Motocykl]
    |
[Samochód Sportowy]
```

W tym diagramie `Samochód` i `Motocykl` dziedziczą po `Pojazd`, a `Samochód Sportowy` dziedziczy po `Samochód`. Każda strzałka reprezentuje relację dziedziczenia, gdzie klasa pochodna **jest** rodzajem klasy bazowej.

### Zalety dziedziczenia

- Dziedziczenie umożliwia **ponowne wykorzystanie kodu**, ponieważ klasy potomne dziedziczą metody i atrybuty klas bazowych, co zmniejsza potrzebę pisania powtarzających się fragmentów kodu.
- Dodatkowo, **łatwe rozszerzanie funkcjonalności** jest możliwe, ponieważ istniejące klasy można rozszerzać bez konieczności modyfikowania oryginalnego kodu, co pozwala na większą elastyczność.

### Wady dziedziczenia

Chociaż dziedziczenie jest potężnym mechanizmem w programowaniu obiektowym, ma swoje ograniczenia i wady, które mogą prowadzić do problemów w bardziej złożonych projektach:

1. Dziedziczenie prowadzi do **ścisłego powiązania** między klasami bazowymi a pochodnymi. Zmiana w klasie bazowej może nieoczekiwanie wpłynąć na wszystkie klasy pochodne, co może utrudnić utrzymanie kodu, szczególnie w dużych systemach. Takie powiązanie może również ograniczać możliwość ponownego użycia kodu w różnych kontekstach, gdyż klasy pochodne są mocno związane z określoną implementacją klasy bazowej.
2. W miarę rozbudowywania hierarchii klas, struktura kodu staje się bardziej złożona i trudniejsza do zrozumienia oraz utrzymania. Głęboka hierarchia dziedziczenia może prowadzić do tzw. „fragile base class problem”, gdzie **każda zmiana w klasie bazowej może powodować nieprzewidywalne skutki w klasach pochodnych**. Co więcej, im więcej poziomów dziedziczenia, tym trudniej jest śledzić, które metody i właściwości są używane lub nadpisywane na poszczególnych poziomach.
3. Dziedziczenie jest podejściem statycznym, co oznacza, że relacja między klasą bazową a pochodną jest ustalona na etapie kompilacji lub w trakcie pisania kodu. **Ogranicza to elastyczność** w porównaniu z kompozycją, gdzie relacje między obiektami mogą być dynamicznie zmieniane w trakcie działania programu. Z tego względu dziedziczenie może być trudniejsze do zastosowania w systemach, które wymagają częstych modyfikacji lub skalowalności.
4. **Wielokrotne dziedziczenie**, chociaż dostępne w Pythonie i kilku innych językach, często prowadzi do problemów takich jak „diamentowa struktura” (diamond problem). Problem ten występuje, gdy klasa dziedziczy po dwóch (lub więcej) klasach pochodzących z tej samej klasy bazowej, co prowadzi do potencjalnych konfliktów nazw metod lub właściwości oraz trudności w ustaleniu, z której klasy baza powinna pochodzić implementacja. Rozwiązania tego problemu (np. metoda rozwiązywania kolejności MRO – Method Resolution Order) wprowadzają dodatkową złożoność do kodu.
5. Jeśli projekt wymaga modyfikacji hierarchii klas, może to być bardzo kosztowne i czasochłonne. Dodanie nowej klasy lub zmiana istniejącej relacji dziedziczenia może wymagać wielu zmian w różnych częściach systemu. W przypadku dziedziczenia rozproszonych po całym systemie klas, modyfikacje jednej klasy mogą powodować kaskadowe zmiany, co zwiększa ryzyko wprowadzenia błędów.
6. Dziedziczenie często prowadzi do nadużywania dostępu do metod i właściwości klasy bazowej. Klasy potomne mają dostęp do wszystkich publicznych i chronionych atrybutów klasy bazowej, co może naruszać **zasady hermetyzacji** (enkapsulacji). Może to prowadzić do sytuacji, w której klasy potomne mają nadmierny dostęp do wewnętrznych szczegółów implementacyjnych klasy bazowej, co utrudnia jej dalszy rozwój i utrzymanie.
7. **Testowanie klas** z rozbudowaną hierarchią dziedziczenia może być trudne. Jeśli klasy pochodne zależą od implementacji klasy bazowej, zmiana lub błąd w klasie bazowej może prowadzić do nieoczekiwanych rezultatów w testach klas pochodnych. W takich przypadkach jednostkowe testowanie klas potomnych może wymagać skomplikowanych stubbów lub mocków.

### Gdzie używane jest dziedziczenie?

Dziedziczenie znajduje zastosowanie w wielu dziedzinach programowania obiektowego, gdzie organizowanie kodu w postaci hierarchii klas prowadzi do większej czytelności, elastyczności i ponownego użycia kodu. Oto kilka przykładowych scenariuszy:

1. **W systemach zarządzania treścią (CMS)**, klasy reprezentujące różne typy treści mogą dziedziczyć po wspólnej klasie bazowej, np. `Content`. Na przykład, klasy `Artykul`, `Strona` czy `Obraz` mogą dziedziczyć wspólne atrybuty, takie jak `tytul`, `autor`, czy `data_publikacji`, dzięki czemu można je wspólnie zarządzać i prezentować.
2. W aplikacjach **GUI**, różne elementy interfejsu, takie jak przyciski, pola tekstowe, czy etykiety, mogą dziedziczyć po klasie bazowej `Widget`. Dzięki dziedziczeniu wspólnych cech (np. możliwość rysowania na ekranie, obsługi zdarzeń), każda specyficzna klasa widżetu może dodawać unikalne zachowania, jednocześnie korzystając z podstawowych funkcji klasy bazowej.
3. W **grach** dziedziczenie jest powszechnie stosowane do modelowania obiektów, które mają podobne cechy. Na przykład, klasa `Postac` może być klasą bazową dla innych klas, takich jak `Bohater` i `Przeciwnik`. Klasy potomne mogą dziedziczyć wspólne atrybuty, takie jak `punkty_zycia`, `atak`, i `obrona`, a jednocześnie dodawać specyficzne funkcje, np. `umiejetnosc_specjalna`.
4. W aplikacjach, które **zarządzają użytkownikami** (np. w systemach ERP), możemy mieć hierarchię użytkowników, gdzie klasa `Uzytkownik` jest klasą bazową, a klasy takie jak `Administrator`, `Redaktor`, czy `UzytkownikZwykly` dziedziczą po niej. Każda z klas potomnych może mieć dodatkowe uprawnienia lub funkcjonalności specyficzne dla swojej roli.
5. W **systemach finansowych**, różne typy transakcji mogą dziedziczyć po wspólnej klasie bazowej `Transakcja`. Na przykład, `Przelew`, `Wplata`, i `Wyplata` mogą dziedziczyć wspólne cechy takie jak `kwota`, `data`, czy `konto`, a jednocześnie dodawać specyficzne zachowania, np. obsługę opłat bankowych lub walidację danych.
6. W aplikacjach opartych o **REST API**, klasy obsługujące różne zasoby mogą dziedziczyć wspólną logikę w klasach bazowych. Na przykład, klasa `Resource` może implementować wspólne metody dla operacji HTTP (GET, POST, PUT, DELETE), a poszczególne zasoby, takie jak `UzytkownikResource`, `ProduktResource` i `ZamowienieResource`, mogą dziedziczyć tę funkcjonalność, dostosowując ją do konkretnych zasobów.
7. W **systemach e-commerce** produkty mogą dziedziczyć po klasie `Produkt`. Na przykład, `Ksiazka`, `Odziez`, i `Elektronika` mogą dziedziczyć podstawowe atrybuty, takie jak `nazwa`, `cena`, i `opis`, ale dodawać specyficzne pola, np. `autor` dla książki lub `rozmiar` dla odzieży.

### Prosty przykład dziedziczenia

W podstawowym przypadku dziedziczenie pozwala klasie podrzędnej (ang. subclass) na przejęcie atrybutów i metod klasy bazowej (ang. superclass). W poniższym przykładzie klasa `Student` dziedziczy po klasie `Czlowiek`, co pozwala na użycie wszystkich atrybutów i metod klasy bazowej, a jednocześnie umożliwia dodanie własnych, specyficznych dla klasy `Student`.

```python
class Czlowiek:
    def __init__(self, imie: str, nazwisko: str, miejsce_urodzenia: str, zawod: str):
        self.imie = imie
        self.nazwisko = nazwisko
        self.miejsce_urodzenia = miejsce_urodzenia
        self.zawod = zawod

    def __str__(self):
        return f"{self.imie} {self.nazwisko}, Urodzony w: {self.miejsce_urodzenia}, Zawód: {self.zawod}"

class Student(Czlowiek):
    def __init__(self, imie: str, nazwisko: str, miejsce_urodzenia: str, numer_albumu: int, kierunek_studiow: str):
        super().__init__(imie, nazwisko, miejsce_urodzenia, 'student')
        self.numer_albumu = numer_albumu
        self.kierunek_studiow = kierunek_studiow

    def __str__(self):
        return f"{super().__str__()}, Numer albumu: {self.numer_albumu}, Kierunek: {self.kierunek_studiow}"
```

W tym przykładzie klasa `Student` dziedziczy konstruktor i metodę `__str__` z klasy `Czlowiek`. Za pomocą `super()` odwołujemy się do klasy bazowej, by zainicjalizować jej atrybuty, a następnie dodajemy dodatkowe atrybuty specyficzne dla klasy `Student`. Dzięki temu, obiekt `Student` posiada pełną funkcjonalność klasy `Czlowiek`, jednocześnie rozszerzoną o własne cechy.

### Przykład wielokrotnego dziedziczenia

W Pythonie możemy tworzyć klasy, które dziedziczą po więcej niż jednej klasie bazowej. Taka elastyczność pozwala na łączenie różnych funkcjonalności w jednej klasie podrzędnej. Poniżej przedstawiamy przykład wielokrotnego dziedziczenia:

```python
class Sportowiec:
    def __init__(self, dyscyplina: str):
        self.dyscyplina = dyscyplina

    def __str__(self):
        return f"Dyscyplina: {self.dyscyplina}"

class StudentSportowiec(Student, Sportowiec):
    def __init__(self, imie: str, nazwisko: str, miejsce_urodzenia: str, numer_albumu: int, kierunek_studiow: str, dyscyplina: str):
        Student.__init__(self, imie, nazwisko, miejsce_urodzenia, numer_albumu, kierunek_studiow)
        Sportowiec.__init__(self, dyscyplina)

    def __str__(self):
        return f"{Student.__str__(self)}, {Sportowiec.__str__(self)}"
```

W tym przypadku klasa `StudentSportowiec` dziedziczy po dwóch klasach bazowych: `Student` i `Sportowiec`. W konstruktorze klasy podrzędnej wywołujemy osobno konstruktory obu klas bazowych, by zainicjalizować ich atrybuty. Dzięki temu, obiekt `StudentSportowiec` łączy cechy zarówno studenta, jak i sportowca.

## Kompozycja

Kompozycja to technika, w której klasy są tworzone z instancji innych klas, co pozwala na budowanie złożonych obiektów poprzez łączenie mniejszych, bardziej wyspecjalizowanych obiektów. Kompozycja promuje luźne powiązanie i lepszą modularność kodu.

**Kompozycja (relacja "ma")**

Przedstawione jako klasa z elementami składowymi w środku:

```
+-----------------+
|    Samochód     |
|-----------------|
| - Silnik        |
| - Koła          |
| - Nadwozie      |
| - Wnętrze       |
+-----------------+
```

Tutaj `Samochód` **ma** różne komponenty, takie jak `Silnik`, `Koła`, `Nadwozie` i `Wnętrze`. Elementy te są zawarte **wewnątrz** klasy `Samochód`, co ilustruje relację kompozycji.

### Zalety kompozycji

- Kompozycja oferuje dużą **elastyczność**, ponieważ można łatwo zmieniać zachowanie klasy poprzez wymianę jej komponentów, co pozwala na dostosowanie funkcjonalności bez potrzeby modyfikowania struktury całej klasy.
- Ponadto, **ponowne wykorzystanie kodu** jest znaczące, ponieważ komponenty używane w jednej klasie mogą być wielokrotnie wykorzystywane w innych kontekstach.
- Dzięki **luźnemu powiązaniu** między obiektami, kompozycja ułatwia modyfikacje oraz utrzymanie kodu, co zwiększa jego stabilność i czytelność.

### Wady kompozycji

Chociaż kompozycja ma wiele zalet, istnieją pewne wyzwania, które mogą się pojawić podczas jej stosowania:

1. Kompozycja wymaga budowania obiektów z wielu komponentów, co może prowadzić do **większej ilości kodu inicjalizacyjnego**. Na przykład, tworzenie obiektu złożonego z kilku komponentów może wymagać wcześniejszej inicjalizacji każdego z nich, co może wydłużać kod i sprawiać, że będzie mniej przejrzysty. Dodatkowo, zarządzanie stanem wielu współpracujących obiektów może być bardziej skomplikowane niż w przypadku dziedziczenia, gdzie mamy do czynienia z jednolitą strukturą klas.
2. W złożonych systemach, gdzie obiekty składają się z wielu komponentów, może być **trudniej zrozumieć zależności** i interakcje między nimi. W przypadku kompozycji relacje między obiektami są bardziej dynamiczne, co oznacza, że programiści muszą śledzić, jak te obiekty ze sobą współpracują. Może to prowadzić do większego wysiłku przy analizowaniu, jak poszczególne komponenty współdziałają, co z kolei utrudnia debugowanie i utrzymanie kodu.
3. W przypadku kompozycji, dostęp do metod i atrybutów obiektów składnikowych musi być zapewniony za pośrednictwem interfejsów, co może wymagać **dodatkowego kodu delegującego**. Może to wprowadzać pewne opóźnienia w rozwoju oprogramowania, ponieważ wymaga bardziej świadomego zarządzania komunikacją między obiektami, w przeciwieństwie do dziedziczenia, gdzie metody klasy bazowej są dostępne bezpośrednio w klasie potomnej.
4. Kompozycja, w odróżnieniu od dziedziczenia, **nie wspiera polimorfizmu** w naturalny sposób. Aby uzyskać polimorfizm (możliwość traktowania różnych obiektów w ten sam sposób), konieczne jest napisanie dodatkowego kodu, np. implementacja wspólnych interfejsów lub metod delegujących. To może skomplikować projektowanie systemu, szczególnie w bardziej złożonych przypadkach.
5. W niektórych przypadkach, gdy kompozycja jest stosowana na dużą skalę, może to prowadzić do **nadmiaru kodu**, zwłaszcza przy tworzeniu wielu obiektów składających się z różnych komponentów. Każdy z tych komponentów wymaga dokładnego zaprojektowania, a następnie właściwej obsługi, co może zwiększyć ilość kodu w porównaniu do prostszych hierarchii dziedziczenia.

### Gdzie używana jest kompozycja?

Kompozycja jest szeroko stosowana w różnych obszarach programowania, szczególnie tam, gdzie elastyczność, modularność i ponowne użycie komponentów są kluczowe. Oto przykłady zastosowań kompozycji:

1. W **systemach zarządzania projektami**** kompozycja jest często używana do tworzenia hierarchii zadań. Projekt może składać się z wielu zadań, a każde zadanie może mieć podzadania. Zamiast używać dziedziczenia, każda instancja projektu może zawierać wiele obiektów reprezentujących różne zadania. Zadania mogą być zarządzane niezależnie od siebie, co umożliwia bardziej modularne podejście do zarządzania projektem.
2. W **aplikacjach multimedialnych** obiekty reprezentujące różne rodzaje mediów (np. dźwięk, obraz, tekst) są często komponowane z mniejszych elementów, które mogą być ze sobą łączone na różne sposoby. Na przykład, film może być złożony z komponentów odpowiadających za dźwięk, obraz i napisy. Każdy z tych komponentów może być łatwo wymieniany lub modyfikowany bez wpływu na resztę systemu.
3. W **architekturze MVC** kompozycja jest wykorzystywana do budowania widoków (interfejsów użytkownika) oraz modeli (logiki biznesowej) z mniejszych komponentów. Na przykład, kontroler może składać się z modeli, które dostarczają dane, oraz widoków, które prezentują te dane użytkownikowi. Dzięki kompozycji różne modele i widoki mogą być ze sobą łączone w elastyczny sposób.
4. W nowoczesnych **silnikach gier** kompozycja jest preferowana nad dziedziczeniem do budowy złożonych postaci i obiektów. Postać w grze może być złożona z różnych komponentów, takich jak grafika, fizyka, sztuczna inteligencja czy animacja. Każdy z tych komponentów może być rozwijany niezależnie, a postać może łatwo zmieniać swoje cechy, wymieniając lub modyfikując komponenty, bez zmiany ogólnej struktury postaci.
5. Kompozycja jest kluczowa w systemach, które są oparte na **modułach**. Na przykład, systemy wtyczek (plugins) często korzystają z kompozycji, umożliwiając dodawanie nowych funkcji do aplikacji bez konieczności modyfikowania jej głównej struktury. Każda wtyczka może być oddzielnym komponentem, który dodaje określone funkcje do większego systemu.
6. W **systemach IoT** kompozycja jest używana do budowania złożonych urządzeń z mniejszych komponentów. Na przykład, inteligentny dom może składać się z różnych urządzeń, takich jak termostaty, oświetlenie, kamery i zamki, które współpracują ze sobą. Każde urządzenie może być rozwijane i zarządzane niezależnie, a system jako całość jest elastyczny i skalowalny.
7. W systemach **zarządzania zasobami ludzkimi**, kompozycja jest stosowana do modelowania pracowników. Każdy pracownik może być reprezentowany jako złożony obiekt, który składa się z różnych komponentów, takich jak dane osobowe, historia zatrudnienia, kompetencje czy harmonogram pracy. Te komponenty mogą być używane niezależnie od siebie, co pozwala na łatwe zarządzanie danymi w różnych kontekstach.
8. Kompozycja jest często wykorzystywana do tworzenia złożonych **produktów finansowych**. Na przykład, konto bankowe może składać się z różnych komponentów, takich jak saldo, historia transakcji, karty debetowe i kredytowe oraz limity. Dzięki kompozycji każdy z tych komponentów może być rozwijany niezależnie, a zmiany w jednym komponencie nie wpływają na inne.

### Przykład kompozycji w Pythonie

```python
class Pensja:
    def __init__(self, pensja: int, stopa_podwyzki: float):
        self.pensja = pensja
        self.stopa_podwyzki = stopa_podwyzki

    def roczna_pensja(self):
        return self.pensja * (1 + self.stopa_podwyzki)

    def __str__(self):
        return f"Pensja: {self.pensja}, Stopa podwyżki: {self.stopa_podwyzki*100}%"

class Pracownik:
    def __init__(self, imie: str, nazwisko: str, pensja: Pensja):
        self.imie = imie
        self.nazwisko = nazwisko
        self.pensja = pensja # kompozycja: obiekt Pensja jest częścią obiektu Pracownik

    def __str__(self):
        return f"Pracownik: {self.imie} {self.nazwisko}, Zarabia rocznie: {self.pensja.roczna_pensja()} PLN"
```

W powyższym przykładzie klasa `Pracownik` korzysta z kompozycji, umieszczając obiekt klasy `Pensja` jako jej atrybut. Dzięki temu `Pracownik` może korzystać z metod zdefiniowanych w klasie `Pensja` poprzez instancję tej klasy.

### Przykład zaawansowanej kompozycji

Kompozycja może być używana do tworzenia bardziej złożonych struktur, które są trudne do osiągnięcia za pomocą samego dziedziczenia.

```python
class Adres:
    def __init__(self, ulica: str, miasto: str, kod_pocztowy: str):
        self.ulica = ulica
        self.miasto = miasto
        self.kod_pocztowy = kod_pocztowy

    def __str__(self):
        return f"{self.ulica}, {self.miasto}, {self.kod_pocztowy}"

class Osoba:
    def __init__(self, imie: str, nazwisko: str, adres: Adres):
        self.imie = imie
        self.nazwisko = nazwisko
        self.adres = adres

    def __str__(self):
        return f"{self.imie} {self.nazwisko}, Adres: {self.adres}"

adres = Adres("ul. Kwiatowa 15", "Warszawa", "00-001")
osoba = Osoba("Jan", "Kowalski", adres)

print(osoba)  # Jan Kowalski, Adres: ul. Kwiatowa 15, Warszawa, 00-001
```

W tym przykładzie `Osoba` ma obiekt `Adres` jako jeden ze swoich atrybutów. Umożliwia to bardziej elastyczne i modularne projektowanie kodu, ponieważ możemy łatwo zmieniać adresy, nie zmieniając samej klasy `Osoba`.

## Porównanie

| Cecha                   | Dziedziczenie                                        | Kompozycja                                          |
|-------------------------|------------------------------------------------------|-----------------------------------------------------|
| Relacja                 | "Jest rodzajem" (is-a relationship)                  | "Ma" lub "Składa się z" (has-a relationship)       |
| Elastyczność            | Mniej elastyczne (hierarchia klas jest sztywna)      | Bardziej elastyczne (łatwo dodawać/usuwać komponenty)|
| Reużywalność            | Może prowadzić do problemów z ponownym użyciem kodu  | Wysoka reużywalność komponentów                     |
| Dostęp do atrybutów     | Bezpośredni dostęp do atrybutów klasy nadrzędnej     | Dostęp przez instancje składników                   |
| Zmienność               | Zmiany w klasie bazowej mogą wpłynąć na klasy pochodne| Zmiany w jednej klasie nie wpłyną na inne           |
| Kiedy używać?           | Gdy istnieje wyraźna relacja hierarchiczna           | Gdy chcemy modelować relacje pomiędzy częściami     |
| Skomplikowanie kodu     | Może prowadzić do nadmiernego rozproszenia kodu      | Może prowadzić do większej ilości kodu              |
| Polimorfizm             | Wspierany                                            | Wymaga dodatkowego kodu                             |
