### Dziedziczenie i kompozycja

Dziedziczenie i kompozycja to dwa fundamentalne koncepty programowania obiektowego (OOP), które odgrywają kluczową rolę w tworzeniu elastycznego, modularnego i łatwego do utrzymania kodu. Oba podejścia mają swoje zalety i wady, a wybór między nimi zależy od konkretnego kontekstu i wymagań projektu.

## Dziedziczenie

Dziedziczenie to mechanizm, który pozwala jednej klasie (klasie potomnej) przejąć właściwości i zachowania innej klasy (klasy bazowej). Dzięki dziedziczeniu, programiści mogą tworzyć nowe klasy na podstawie istniejących, co pozwala na ponowne wykorzystanie kodu i redukcję jego złożoności.

### Zalety dziedziczenia
- **Ponowne wykorzystanie kodu**: Klasy potomne dziedziczą metody i atrybuty klas bazowych, co redukuje potrzebę pisania powtarzalnego kodu.
- **Łatwe rozszerzanie funkcjonalności**: Można łatwo rozszerzać istniejące klasy bez potrzeby modyfikacji oryginalnego kodu.

### Wady dziedziczenia
- **Zwiększona złożoność**: Zbyt głęboka hierarchia dziedziczenia może prowadzić do trudnego do zrozumienia i utrzymania kodu.
- **Ścisłe powiązanie**: Klasy potomne są ściśle związane z klasami bazowymi, co może utrudniać modyfikacje.

### Gdzie używane jest dziedziczenie?
- **Systemy zarządzania treścią (CMS)**: Klasy reprezentujące różne typy treści mogą dziedziczyć z klasy bazowej `Content`.
- **Aplikacje GUI**: Klasy reprezentujące różne typy widżetów (np. przyciski, etykiety) mogą dziedziczyć z klasy bazowej `Widget`.

### Przykład w Pythonie

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

W tym przykładzie, klasa `Student` dziedziczy po klasie `Czlowiek`. Dzięki temu `Student` dziedziczy wszystkie atrybuty i metody klasy `Czlowiek` i może je rozszerzyć lub modyfikować.

### Przykład wielokrotnego dziedziczenia

Python umożliwia również wielokrotne dziedziczenie, gdzie klasa podrzędna może dziedziczyć po więcej niż jednej klasie bazowej.

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

W powyższym przykładzie klasa `StudentSportowiec` dziedziczy zarówno po `Student`, jak i po `Sportowiec`, łącząc funkcjonalności obu klas.

## Kompozycja

Kompozycja to technika, w której klasy są tworzone z instancji innych klas, co pozwala na budowanie złożonych obiektów poprzez łączenie mniejszych, bardziej wyspecjalizowanych obiektów. Kompozycja promuje luźne powiązanie i lepszą modularność kodu.

### Zalety kompozycji
- **Elastyczność**: Łatwo można zmieniać zachowanie klasy poprzez wymianę jej komponentów.
- **Ponowne wykorzystanie kodu**: Komponenty mogą być wielokrotnie używane w różnych kontekstach.
- **Luźne powiązanie**: Kompozycja pozwala na luźniejsze powiązanie między obiektami, co ułatwia modyfikacje i utrzymanie kodu.

### Wady kompozycji
- **Złożoność konstrukcji obiektów**: Tworzenie i zarządzanie złożonymi obiektami może być trudniejsze i wymagać więcej kodu niż w przypadku dziedziczenia.

### Gdzie używana jest kompozycja?
- **Systemy zarządzania projektami**: Projekty mogą składać się z wielu zadań, gdzie każde zadanie jest oddzielnym obiektem.
- **Aplikacje multimedialne**: Obiekty reprezentujące media mogą składać się z komponentów takich jak dźwięk, obraz, napisy.

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


### Porównanie

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
