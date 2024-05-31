## Klasy i obiekty

Programowanie obiektowe (ang. Object-Oriented Programming, OOP) to paradygmat programowania, który opiera się na koncepcji "obiektów". Obiekty są instancjami klas, które łączą dane (atrybuty) i funkcje (metody) w jedną jednostkę. Klasy i obiekty są podstawowymi elementami tego paradygmatu i przynoszą wiele korzyści w tworzeniu skalowalnego, zrozumiałego i łatwego do utrzymania kodu.

- **Klasa**: Szablon lub projekt definiujący strukturę i zachowanie obiektów. Określa, jakie atrybuty i metody będą miały obiekty tej klasy.

- **Obiekt**: Konkretna instancja klasy, która posiada rzeczywiste wartości atrybutów zdefiniowanych przez klasę.

### Struktura klasy

1. **Konstruktor (`__init__`)**: Specjalna metoda wywoływana, kiedy tworzony jest nowy obiekt klasy. Służy do inicjowania atrybutów obiektu.
2. **Atrybuty**: To zmienne związane z klasą. Przechowują informacje o stanie obiektu.
3. **Metody**: To funkcje związane z klasą, które mogą operować na atrybutach lub wykonywać inne operacje powiązane z obiektem.

### Przykład użycia

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

W powyższym kodzie:
- Zdefiniowaliśmy klasę `Osoba` z dwoma atrybutami (`imie` i `nazwisko`) oraz jedną metodą (`przedstaw_sie`).
- Używając klasy, stworzyliśmy dwa obiekty: `osoba1` i `osoba2`.
- Dla każdego obiektu wywołaliśmy metodę `przedstaw_sie`.

### Dostęp i modyfikacja atrybutów w obiektach

W programowaniu obiektowym atrybuty (zmienne) są przechowywane w obiektach. Aby uzyskać dostęp do tych atrybutów, korzysta się z notacji kropkowej:

```python
nazwa_obiektu.atrybut
```

Atrybuty mogą być modyfikowane podobnie jak zwykłe zmienne:

```python
osoba = Osoba("Jan", "Kowalski")
print(osoba.imie)  # Wyświetli: Jan
osoba.imie = "Adam"
print(osoba.imie)  # Wyświetli: Adam
```

### Dekoratory @property i @nazwa_atrybutu.setter

Aby wprowadzić kontrolę nad dostępem do atrybutów oraz modyfikacją ich wartości, w Pythonie można używać dekoratorów `@property` oraz `@nazwa_atrybutu.setter`. Te dekoratory pozwalają na tworzenie funkcji, które są wywoływane podczas odczytu i modyfikacji atrybutu.

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
```

W klasie `Osoba`, atrybuty `_imie` i `_nazwisko` są oznaczone jednym podkreślnikiem, co jest konwencją wskazującą, że atrybuty te są "chronione" i nie powinny być modyfikowane bezpośrednio z zewnątrz klasy. Dekoratory `@property` i `@imie.setter` umożliwiają odpowiednio odczyt i modyfikację wartości atrybutu `_imie`.

```python
osoba = Osoba("Jan", "Kowalski")
print(osoba.imie)  # Ktoś próbuje odczytać imię, wyświetli: Jan
osoba.imie = "Adam"  # Ktoś modyfikuje imię
print(osoba.imie)  # Ktoś próbuje odczytać imię, wyświetli: Adam
```

### Potrzeba używania klas i obiektów

1. **Modularność i organizacja kodu**:
   - Klasy pozwalają na grupowanie powiązanych danych i funkcji, co pomaga w organizacji kodu. Kod staje się bardziej modularny, co ułatwia jego zrozumienie i utrzymanie.
   - Przykład: W aplikacji do zarządzania biblioteką możemy mieć klasę `Ksiazka`, która łączy atrybuty (tytuł, autor, ISBN) z metodami (wypożycz, zwróć).

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

2. **Reużywalność kodu**:
   - Klasy umożliwiają tworzenie obiektów o podobnej strukturze i zachowaniu, co zapobiega duplikacji kodu.
   - Przykład: Możemy utworzyć wiele obiektów klasy `Ksiazka` bez konieczności wielokrotnego definiowania tych samych atrybutów i metod.

    ```python
    ksiazka1 = Ksiazka("Pan Tadeusz", "Adam Mickiewicz", "1234567890")
    ksiazka2 = Ksiazka("Lalka", "Bolesław Prus", "0987654321")
    ksiazka1.wypozycz()
    ksiazka2.zwroc()
    ```

3. **Enkapsulacja (ukrywanie szczegółów implementacji)**:
   - Klasy umożliwiają ukrywanie wewnętrznych szczegółów implementacji przed użytkownikami obiektów. Dzięki temu użytkownicy mogą korzystać z obiektów bez znajomości ich wewnętrznej struktury.
   - Przykład: W klasie `Ksiazka` możemy ukryć wewnętrzne szczegóły dotyczące statusu wypożyczenia książki.

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

4. **Dziedziczenie**:
   - Dziedziczenie pozwala na tworzenie nowych klas na podstawie istniejących klas, co umożliwia ponowne użycie kodu i rozszerzanie jego funkcjonalności.
   - Przykład: Możemy stworzyć klasę `Ebook`, która dziedziczy po klasie `Ksiazka` i dodaje nowe atrybuty oraz metody specyficzne dla e-booków.

    ```python
    class Ebook(Ksiazka):
        def __init__(self, tytul, autor, isbn, rozmiar_pliku):
            super().__init__(tytul, autor, isbn)
            self.rozmiar_pliku = rozmiar_pliku

        def pobierz(self):
            print(f'Pobieranie e-booka "{self.tytul}". Rozmiar pliku: {self.rozmiar_pliku}MB')
    ```

5. **Polimorfizm**:
   - Polimorfizm pozwala na traktowanie obiektów różnych klas w ten sam sposób, pod warunkiem że klasy te dzielą wspólny interfejs (np. dziedziczą po tej samej klasie bazowej).
   - Przykład: Możemy używać tej samej metody `wypozycz` dla obiektów klasy `Ksiazka` i `Ebook`.

    ```python
    ksiazka = Ksiazka("Pan Tadeusz", "Adam Mickiewicz", "1234567890")
    ebook = Ebook("Lalka", "Bolesław Prus", "0987654321", 5)
    ksiazka.wypozycz()
    ebook.wypozycz()
    ebook.pobierz()
    ```

### Pola i metody statyczne oraz klasowe

W programowaniu obiektowym często korzysta się z pól i metod statycznych oraz klasowych. Różnią się one od standardowych pól i metod instancji, gdyż są powiązane bezpośrednio z klasą, a nie z jej instancjami.

#### Pola i metody statyczne

Pola i metody statyczne są związane z klasą, a nie z konkretnymi obiektami tej klasy. W Pythonie metody statyczne są tworzone przy użyciu dekoratora `@staticmethod`. Dostęp do nich jest możliwy zarówno poprzez nazwę klasy, jak i przez obiekt tej klasy. Metody statyczne nie mają dostępu do atrybutów instancji ani do atrybutów klasy, ponieważ nie przyjmują jako pierwszego argumentu `self` ani `cls`.

Przykład:

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

W powyższym przykładzie, metoda `wyswietl_glowy` jest metodą statyczną. Można ją wywołać zarówno poprzez klasę `Czlowiek`, jak i przez jej instancję `przykladowy_czlowiek`.

#### Metody klasowe

Metody klasowe stanowią rozszerzenie metod statycznych. Są one tworzone przy użyciu dekoratora `@classmethod` i ich pierwszym parametrem jest `cls`, który reprezentuje samą klasę (podobnie jak `self` reprezentuje instancję). Metody klasowe mogą dostępować do pól klasowych oraz do innych metod klasowych.

Przykład:

```python
class Czlowiek:
    liczba_glow = 1

    @classmethod
    def wyswietl_glowy(cls):
        print(f'Liczba głów: {cls.liczba_glow}')  # Uwaga: używamy `cls`, a nie nazwy klasy!

    def zwykla_funkcja(self):
        self.wyswietl_glowy()

Czlowiek.wyswietl_glowy()  # Liczba głów: 1

przykladowy_czlowiek = Czlowiek()
przykladowy_czlowiek.wyswietl_glowy()  # Liczba głów: 1
przykladowy_czlowiek.zwykla_funkcja()  # Liczba głów: 1
```

W klasie `Czlowiek` mamy pole klasowe `liczba_glow`, metodę klasową `wyswietl_glowy()`, która korzysta z tego pola, oraz metodę instancyjną `zwykla_funkcja()`. W przykładzie pokazano różne sposoby wywoływania metody klasowej, zarówno bezpośrednio z poziomu klasy, jak i z poziomu instancji. Kluczową różnicą jest to, że w metodach klasowych używa się `cls` do odwoływania się do klasowych atrybutów i metod, podczas gdy w metodach instancyjnych używa się `self`.

### Różnice między metodami instancyjnymi, klasowymi i statycznymi

1. **Metody instancyjne**:
   - Są powiązane z instancją klasy.
   - Mają dostęp do atrybutów instancji przez `self`.
   - Mają dostęp do atrybutów klasy przez `self.__class__` lub bezpośrednio przez nazwę klasy.

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

2. **Metody klasowe**:
   - Są powiązane z klasą, nie z instancją.
   - Mają dostęp do atrybutów klasy przez `cls`.
   - Nie mają dostępu do atrybutów instancji bezpośrednio.

   Przykład:

    ```python
    class Samochod:
        liczba_kol = 4

        @classmethod
        def wyswietl_liczbe_kol(cls):
            print(f"Samochody mają {cls.liczba_kol} koła")

    Samochod.wyswietl_liczbe_kol()  # Samochody mają 4 koła
    ```

3. **Metody statyczne**:
   - Nie są powiązane ani z instancją, ani z klasą.
   - Nie mają dostępu do atrybutów instancji ani klasy.
   - Są używane do wykonywania zadań, które są związane z klasą, ale nie wymagają dostępu do jej stanu.

   Przykład:

    ```python
    class Samochod:
        @staticmethod
        def informacje_o_samochodach():
            print("Samochody to pojazdy mechaniczne służące do transportu")

    Samochod.informacje_o_samochodach()  # Samochody to pojazdy mechaniczne służące do transportu
    ```

### Zastosowanie w praktyce

Pola i metody statyczne oraz klasowe są szczególnie przydatne w sytuacjach, gdzie operacje dotyczą samej klasy, a nie konkretnej instancji. Na przykład, mogą być używane do zliczania liczby instancji klasy, zarządzania wspólnymi zasobami czy implementowania wzorców projektowych takich jak Singleton.

1. **Zliczanie liczby instancji klasy**:

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

2. **Zarządzanie wspólnymi zasobami**:

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

3. **Wzorce projektowe**:

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
