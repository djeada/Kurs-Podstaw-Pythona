## Klasy i obiekty

Programowanie obiektowe (ang. Object-Oriented Programming, OOP) to jeden z najpopularniejszych i najbardziej przemyślanych sposobów tworzenia oprogramowania. Polega na organizowaniu kodu w logiczne jednostki (obiekty), które łączą dane (atrybuty) i funkcje (metody) w jedną spójną całość. Dzięki temu kod staje się łatwiejszy w utrzymaniu, rozbudowie i ponownym wykorzystaniu. Klasy i obiekty są kluczowymi elementami tego paradygmatu: klasa to pewien „przepis” (lub „szablon”), a obiektem nazywamy konkretny egzemplarz stworzony na podstawie takiego przepisu.

Paradygmat obiektowy jest bardzo intuicyjny, ponieważ często odwzorowuje realne sytuacje w kodzie. Można to porównać do planów architektonicznych (klasy), które opisują, jak ma wyglądać i działać budynek, podczas gdy obiekty są już fizycznymi budowlami wzniesionymi według tego planu. Właśnie to rozróżnienie pomiędzy projektem (klasą) a konkretną realizacją (obiektem) stanowi serce OOP.

Klasy pozwalają definiować zarówno dane, które reprezentują stan obiektu (tzw. atrybuty), jak i metody, czyli czynności wykonywane na tych danych. Kiedy tworzony jest obiekt, staje się on instancją danej klasy i „dziedziczy” wszystkie właściwości oraz zachowania zdefiniowane w tej klasie.

Korzyści płynące z tego podejścia to:

1. **Modularność kodu**: możliwość grupowania logicznie powiązanych elementów w jednym miejscu, co sprawia, że kod staje się bardziej czytelny i prostszy w nawigacji.
2. **Możliwość ponownego użycia**: klasy można tworzyć raz i używać w wielu miejscach kodu bez powielania logicznych fragmentów.
3. **Enkapsulacja**: ukrywanie wewnętrznej struktury obiektu przed resztą programu, co pozwala na zmianę implementacji bez wpływu na kod korzystający z obiektów.
4. **Dziedziczenie**: tworzenie nowych klas na bazie już istniejących, co umożliwia rozszerzanie funkcjonalności w sposób bezpieczny i niewymagający powielania kodu.
5. **Polimorfizm**: zdolność do zdefiniowania wspólnego interfejsu (zestawu metod) dla klas o różnej implementacji.

Poniżej przedstawione zostały szczegółowe wyjaśnienia związane z klasami, obiektami oraz pojęciami z nimi powiązanymi. Przedstawione przykłady kodu w Pythonie pozwolą łatwiej zrozumieć, jak w praktyce wykorzystuje się programowanie obiektowe.

### Struktura klasy

Kiedy tworzymy klasę w Pythonie, zazwyczaj definiujemy w niej:

1. **Konstruktor (`__init__`)** – specjalną metodę, która wywoływana jest automatycznie przy tworzeniu nowego obiektu. Służy do inicjowania (nadawania pierwszych wartości) atrybutów.
2. **Atrybuty** – zmienne przechowujące dane opisujące stan obiektu (np. imię, nazwisko, numer ISBN).
3. **Metody** – funkcje zawarte w klasie, które mogą korzystać z atrybutów oraz wykonywać określone zadania związane z obiektem.

Dzięki temu programista może zdefiniować, czym jest obiekt (jakie ma dane, co może robić), a także jakie operacje są na nim dozwolone czy typowe.

### Przykład użycia

Poniżej znajduje się prosty przykład klasy `Osoba`, która przechowuje imię i nazwisko oraz może się przedstawić:

```python
class Osoba:
    # Konstruktor klasy
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko

    # Metoda klasy
    def przedstaw_sie(self):
        print(f"Cześć, jestem {self.imie} {self.nazwisko}")

# Tworzenie obiektów klasy Osoba
osoba1 = Osoba("Jan", "Kowalski")
osoba2 = Osoba("Adam", "Nowak")

# Wywołanie metody dla obiektów
osoba1.przedstaw_sie()
osoba2.przedstaw_sie()
```

W tym przykładzie:

- Zdefiniowaliśmy klasę `Osoba` z dwoma atrybutami (`imie` i `nazwisko`) oraz jedną metodą (`przedstaw_sie`).
- Stworzyliśmy dwa różne obiekty: `osoba1` i `osoba2`. Każdy z nich ma swój własny stan (różne imię i nazwisko).
- Za pomocą metody `przedstaw_sie` każdy obiekt może wyświetlić swoją unikalną charakterystykę.

### Dostęp i modyfikacja atrybutów w obiektach

Atrybuty w obiektach odczytujemy i modyfikujemy za pomocą notacji kropkowej. Oznacza to, że do atrybutu docieramy przez `nazwa_obiektu.atrybut`. Możemy je także zmieniać, przypisując do nich nową wartość:

```python
osoba = Osoba("Jan", "Kowalski")
print(osoba.imie)  # Wyświetli: Jan
osoba.imie = "Adam"
print(osoba.imie)  # Wyświetli: Adam
```

W powyższym przykładzie tworzymy obiekt `osoba`, a następnie uzyskujemy do niego dostęp przez pole `imie`. Zmieniamy jego wartość na `"Adam"` i ponownie wyświetlamy, co dowodzi, że atrybut został zaktualizowany. W praktyce jest to niezwykle wygodne, jednak nie zawsze chcemy, aby atrybuty były modyfikowane dowolnie z zewnątrz. Dlatego w Pythonie istnieją mechanizmy takie jak dekoratory `@property` oraz `@setter`, które umożliwiają kontrolę nad tym, w jaki sposób atrybut może być zmieniany (lub odczytywany).

### Dekoratory @property i @nazwa_atrybutu.setter

W przypadku, gdy chcemy mieć większą kontrolę nad dostępem do atrybutów, możemy skorzystać z tzw. „właściwości” (properties). Dzięki dekoratorom `@property` oraz `@nazwa_atrybutu.setter` tworzymy specjalne metody wywoływane przy odczycie i zapisie atrybutu. Jest to elegancki i zalecany sposób, by uniknąć bezpośredniego modyfikowania atrybutów obiektu.

```python
class Osoba:
    def __init__(self, imie, nazwisko):
        self._imie = imie  # Konwencja z podkreślnikiem wskazuje na "chronione" atrybuty
        self._nazwisko = nazwisko

    @property
    def imie(self):
        print('Ktoś próbuje odczytać imię')
        return self._imie

    @imie.setter
    def imie(self, nowa_wartosc):
        print('Ktoś modyfikuje imię')
        self._imie = nowa_wartosc

osoba = Osoba("Jan", "Kowalski")
print(osoba.imie)  # Ktoś próbuje odczytać imię, wyświetli: Jan
osoba.imie = "Adam"  # Ktoś modyfikuje imię
print(osoba.imie)  # Ktoś próbuje odczytać imię, wyświetli: Adam
```

Dzięki temu mechanizmowi możemy również dodać logikę walidującą czy kontrolną w setterze (np. sprawdzanie, czy nowe imię jest ciągiem znaków i spełnia konkretne warunki). W praktyce pozwala to zabezpieczyć dane obiektu przed niepożądanymi wartościami.

### Potrzeba używania klas i obiektów

Klasy i obiekty nie służą wyłącznie do porządkowania kodu. Zastosowanie programowania obiektowego niesie ze sobą szereg zalet w kontekście rozwijania większych projektów, pracy zespołowej czy ponownego wykorzystania już istniejących rozwiązań w przyszłości.

#### Modularność i organizacja kodu

Klasy umożliwiają sensowne grupowanie atrybutów i metod w jednym miejscu, co sprzyja organizacji kodu i ułatwia odnalezienie potrzebnych fragmentów. Dzięki temu, gdy chcemy np. dodać nowe funkcjonalności lub naprawić błąd, szybko zlokalizujemy odpowiednią sekcję kodu.

Przykład: W aplikacji do zarządzania biblioteką możemy mieć klasę `Ksiazka`, która łączy atrybuty (tytuł, autor, ISBN) z metodami (wypożycz, zwróć). Dzięki temu dokładnie wiadomo, gdzie szukać logiki związanej z obsługą książek.

```python
class Ksiazka:
    def __init__(self, tytul, autor, isbn):
        self.tytul = tytul
        self.autor = autor
        self.isbn = isbn

    def wypozycz(self):
        print(f'Książka "{self.tytul}" została wypożyczona.')

    def zwroc(self):
        print(f'Książka "{self.tytul}" została zwrócona.')
```

#### Możliwość ponownego użycia kodu

Klasy można traktować jak uniwersalne „matryce”. Raz zdefiniowaną klasę da się wykorzystać wielokrotnie, tworząc dowolną liczbę obiektów o podobnym wzorcu, ale różniących się konkretnymi wartościami atrybutów. Minimalizuje to duplikację kodu i ułatwia jego konserwację.

```python
ksiazka1 = Ksiazka("Pan Tadeusz", "Adam Mickiewicz", "1234567890")
ksiazka2 = Ksiazka("Lalka", "Bolesław Prus", "0987654321")
ksiazka1.wypozycz()
ksiazka2.zwroc()
```

#### Enkapsulacja (ukrywanie szczegółów implementacji)

Klasy dają możliwość ukrywania wewnętrznych szczegółów implementacji, tzn. to, jak dokładnie coś jest zrobione w środku, może być niedostępne lub niewidoczne dla zewnętrznego kodu. Dzięki temu możemy modyfikować wnętrze klasy, nie narażając istniejącego kodu na błędy z powodu zmian. Użytkownicy klasy nadal będą się nią posługiwać w taki sam sposób (ten sam interfejs).

```python
class Ksiazka:
    def __init__(self, tytul, autor, isbn):
        self.tytul = tytul
        self.autor = autor
        self.isbn = isbn
        self._wypozyczona = False

    def wypozycz(self):
        if not self._wypozyczona:
            self._wypozyczona = True
            print(f'Książka "{self.tytul}" została wypożyczona.')
        else:
            print(f'Książka "{self.tytul}" jest już wypożyczona.')

    def zwroc(self):
        if self._wypozyczona:
            self._wypozyczona = False
            print(f'Książka "{self.tytul}" została zwrócona.')
        else:
            print(f'Książka "{self.tytul}" nie była wypożyczona.')
```

W tym kodzie klasa sama decyduje, jaką logikę zastosować przy wypożyczeniu lub zwróceniu książki. Zewnętrzny kod jedynie wywołuje odpowiednie metody, nie martwiąc się o status wewnętrznych pól obiektu.

#### Dziedziczenie

Dziedziczenie pozwala tworzyć nowe klasy na podstawie już istniejących. Nowa klasa (klasa pochodna) „dziedziczy” atrybuty i metody po klasie bazowej, co pozwala uniknąć dublowania kodu. Można wtedy dodawać nowe funkcjonalności lub nadpisywać już istniejące.

```python
class Ebook(Ksiazka):
    def __init__(self, tytul, autor, isbn, rozmiar_pliku):
        super().__init__(tytul, autor, isbn)
        self.rozmiar_pliku = rozmiar_pliku

    def pobierz(self):
        print(f'Pobieranie e-booka "{self.tytul}". Rozmiar pliku: {self.rozmiar_pliku}MB')
```

Dzięki temu klasa `Ebook` przejmuje już istniejącą logikę z klasy `Ksiazka` (jak np. metody `wypozycz` czy `zwroc`), a oprócz tego wprowadza nowe metody i atrybuty specyficzne dla e-booków (np. rozmiar pliku, metoda pobierania).

#### Polimorfizm

Polimorfizm oznacza, że różne obiekty mogą udostępniać wspólny interfejs, ale realizować go na swój własny sposób. Możemy wyobrazić sobie dwie klasy: `Ksiazka` i `Ebook`. Obie mogą mieć metodę `wypozycz`, która zachowuje się podobnie z punktu widzenia wywołującego kod, ale w praktyce może wykonywać nieco inne operacje (np. weryfikować dostępność egzemplarza fizycznego lub cyfrowego pliku).

```python
ksiazka = Ksiazka("Pan Tadeusz", "Adam Mickiewicz", "1234567890")
ebook = Ebook("Lalka", "Bolesław Prus", "0987654321", 5)
ksiazka.wypozycz()
ebook.wypozycz()
ebook.pobierz()
```

W przykładzie widać, że z punktu widzenia zewnętrznego kodu obiekty `ksiazka` i `ebook` zachowują się w podobny sposób przy wypożyczaniu, choć wewnętrznie mogą funkcjonować inaczej.

### Pola i metody statyczne oraz klasowe

W programowaniu obiektowym, oprócz typowych metod instancyjnych, mamy też metody i pola statyczne oraz klasowe. Podstawowa różnica polega na tym, że:

- **Metody/pola instancyjne** są przypisane do konkretnego obiektu i mogą odnosić się do jego stanu.
- **Metody/pola klasowe** przynależą do samej klasy i współdzielą dane pomiędzy wszystkie instancje (lub nie potrzebują odwoływać się do żadnej konkretnej instancji).
- **Metody statyczne** nie odwołują się ani do stanu instancji, ani do stanu klasy – są w pewnym sensie „zwykłymi funkcjami” zdefiniowanymi w obrębie klasy.

#### Pola i metody statyczne

W Pythonie metody statyczne oznaczamy dekoratorem `@staticmethod`. Takie metody nie przyjmują jako pierwszego parametru `self` ani `cls`. Mogą być wywoływane zarówno poprzez nazwę klasy, jak i poprzez instancję:

```python
class Czlowiek:
    liczba_glow = 1

    @staticmethod
    def wyswietl_glowy():
        print(f'Liczba głów: {Czlowiek.liczba_glow}')

Czlowiek.wyswietl_glowy()  # Liczba głów: 1

przykladowy_czlowiek = Czlowiek()
przykladowy_czlowiek.wyswietl_glowy()  # Liczba głów: 1
```

W tym przykładzie:

- `liczba_glow` jest polem klasowym (jest przypisane do klasy `Czlowiek`, a nie do konkretnego obiektu).
- `wyswietl_glowy` jest metodą statyczną, która bezpośrednio sięga do `Czlowiek.liczba_glow`.

#### Metody klasowe

Metody klasowe wykorzystują dekorator `@classmethod` i otrzymują jako pierwszy argument `cls`, czyli referencję do samej klasy (odpowiednik `self` dla instancji). Metody klasowe mogą zatem modyfikować pola klasowe i wywoływać inne metody klasowe:

```python
class Czlowiek:
    liczba_glow = 1

    @classmethod
    def wyswietl_glowy(cls):
        print(f'Liczba głów: {cls.liczba_glow}')  # Używamy `cls`, zamiast nazwy klasy

    def zwykla_funkcja(self):
        self.wyswietl_glowy()

Czlowiek.wyswietl_glowy()             # Liczba głów: 1
przykladowy_czlowiek = Czlowiek()
przykladowy_czlowiek.wyswietl_glowy() # Liczba głów: 1
przykladowy_czlowiek.zwykla_funkcja() # Liczba głów: 1
```

Jak widać, metoda klasowa może być wywoływana zarówno poprzez klasę, jak i przez obiekt. W praktyce najczęściej używa się jej bezpośrednio z poziomu klasy.

### Różnice między metodami instancyjnymi, klasowymi i statycznymi

#### Metody instancyjne

- Powiązane z daną instancją klasy.
- Mają dostęp do jej atrybutów za pomocą `self`.
- Mogą korzystać z atrybutów klasowych, np. przez `self.__class__`.

Przykład:

```python
class Samochod:
    def __init__(self, marka, model):
        self.marka = marka
        self.model = model

    def przedstaw_sie(self):
        print(f"Samochód: {self.marka} {self.model}")

auto = Samochod("Toyota", "Corolla")
auto.przedstaw_sie()  # Samochód: Toyota Corolla
```

#### Metody klasowe

- Związane z klasą, a nie z konkretną instancją.
- Pierwszy argument to `cls`, będący referencją do klasy.
- Mogą odwoływać się do pól i metod klasowych.

Przykład:

```python
class Samochod:
    liczba_kol = 4

    @classmethod
    def wyswietl_liczbe_kol(cls):
        print(f"Samochody mają {cls.liczba_kol} koła")

Samochod.wyswietl_liczbe_kol()  # Samochody mają 4 koła
```

#### Metody statyczne

- Umiejscowione wewnątrz klasy, ale nie posiadają dostępu do `self` czy `cls`.
- Są wywoływane jak zwykłe funkcje (ale w obrębie klasy).
- Przydają się np. do grupowania funkcji logicznie powiązanych z daną klasą, ale nieoperujących bezpośrednio na stanie klasy lub obiektów.

Przykład:

```python
class Samochod:
    @staticmethod
    def informacje_o_samochodach():
        print("Samochody to pojazdy mechaniczne służące do transportu")

Samochod.informacje_o_samochodach()  # Samochody to pojazdy mechaniczne służące do transportu
```

### Zastosowanie w praktyce

Wykorzystanie pól i metod statycznych/klasowych jest szczególnie przydatne, gdy chcemy:

- Utrzymywać pewne globalne informacje w obrębie klasy (np. licznik tworzonych obiektów).
- Zapewnić wspólny dostęp do pewnych zasobów dla wszystkich instancji (np. do jednego połączenia z bazą danych).
- Implementować wzorce projektowe, w których logika inicjalizacji obiektu (lub jego brak) leży po stronie klasy.

#### Zliczanie liczby instancji

Poniższy przykład pokazuje, jak używając metody klasowej, można zliczać liczbę utworzonych instancji:

```python
class Osoba:
    liczba_instancji = 0

    def __init__(self, imie):
        self.imie = imie
        Osoba.liczba_instancji += 1

    @classmethod
    def ile_instancji(cls):
        return cls.liczba_instancji

osoba1 = Osoba("Jan")
osoba2 = Osoba("Anna")

print(Osoba.ile_instancji())  # 2
```

Tutaj każdorazowe stworzenie nowej osoby zwiększa licznik instancji. Metoda `ile_instancji` jest metodą klasową i pozwala w prosty sposób odczytać, ile obiektów powstało.

#### Zarządzanie wspólnymi zasobami

Przykładem może być klasa zarządzająca dostępem do bazy danych. Zamiast za każdym razem tworzyć nowe połączenie, klasa może mieć jedną statyczną lub klasową zmienną, z której będą korzystać wszystkie instancje. Dzięki temu unika się wielokrotnych, kosztownych operacji na zasobach.

```python
class BazaDanych:
    polaczenie = None

    @classmethod
    def polacz(cls):
        if cls.polaczenie is None:
            cls.polaczenie = "Połączenie do bazy danych"
        return cls.polaczenie

polaczenie1 = BazaDanych.polacz()
polaczenie2 = BazaDanych.polacz()

print(polaczenie1)  # Połączenie do bazy danych
print(polaczenie1 is polaczenie2)  # True
```

W tym kodzie metoda klasowa `polacz` sprawdza, czy połączenie już istnieje. Jeśli nie, tworzy je. W przeciwnym wypadku zwraca istniejące połączenie. Dzięki temu zaoszczędzamy zasoby i zapobiegamy niekontrolowanemu namnażaniu połączeń.

#### Wzorce projektowe

Wzorce projektowe, takie jak Singleton, często korzystają z cech języka obiektowego (w tym pól lub metod statycznych i klasowych), by kontrolować powstawanie nowych instancji klas. Poniższy przykład pokazuje klasyczną implementację wzorca Singleton w Pythonie:

```python
class Singleton:
    _instancja = None

    def __new__(cls, *args, **kwargs):
        if not cls._instancja:
            cls._instancja = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instancja

s1 = Singleton()
s2 = Singleton()

print(s1 is s2)  # True
```

W momencie tworzenia nowego obiektu `Singleton` sprawdza, czy `_instancja` już istnieje. Jeśli nie, tworzy ją, a jeśli tak, zwraca referencję do istniejącego obiektu. W efekcie w całym programie istnieje tylko jeden obiekt tej klasy.
