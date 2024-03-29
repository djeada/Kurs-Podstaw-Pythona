## Klasy i obiekty w Pythonie

Klasy w programowaniu obiektowym stanowią podstawowy środek do tworzenia struktury danych, które łączą atrybuty (zmienne) z operacjami (metodami), które mogą na nich działać. Klasa jest jak "szablon" lub "projekt", a obiekty są jej konkretne instancje.

### Struktura klasy:

1. **Konstruktor (`__init__`)**: Specjalna metoda wywoływana, kiedy tworzony jest nowy obiekt klasy. Służy do inicjowania atrybutów obiektu.
2. **Atrybuty**: To zmienne związane z klasą. Przechowują informacje o stanie obiektu. W przykładzie atrybutami są `imie` i `nazwisko`.
3. **Metody**: To funkcje związane z klasą, które mogą operować na atrybutach lub wykonywać inne operacje powiązane z obiektem.

### Przykład użycia:

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

- Zdefiniowaliśmy klasę Osoba z dwoma atrybutami i jedną metodą.
- Używając klasy, stworzyliśmy dwa obiekty: osoba1 i osoba2.
- Dla każdego obiektu wywołaliśmy metodę przedstaw_sie.

Kluczem jest to, że obiekty osoba1 i osoba2 są od siebie niezależne. Mimo że oba pochodzą z tej samej klasy, mają różne wartości atrybutów.

Programowanie obiektowe sprzyja modularności, ponieważ pozwala grupować powiązane funkcje i dane razem. Dzięki temu kod jest łatwiejszy do zrozumienia, modyfikacji i testowania.

### Dostęp i modyfikacja atrybutów w obiektach

W programowaniu obiektowym atrybuty (zmienne) są przechowywane w obiektach. Aby uzyskać dostęp do tych atrybutów, korzysta się z notacji kropkowej, czyli:

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

Aby wprowadzić kontrolę nad dostępem do atrybutów oraz modyfikacją ich wartości, w Pythonie można używać dekoratorów @property oraz @nazwa_atrybutu.setter. Te dekoratory pozwalają na tworzenie funkcji, które są wywoływane podczas odczytu i modyfikacji atrybutu.

```python
class Osoba:
    def __init__(self, imie, nazwisko):
        self._imie = imie          # Konwencja z podkreślnikiem wskazuje na "chronione" atrybuty
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

W klasie Osoba, atrybuty `_imie` i `_nazwisko` są oznaczone jednym podkreślnikiem, co jest konwencją wskazującą, że atrybuty te są "chronione" i nie powinny być modyfikowane bezpośrednio z zewnątrz klasy.

Dekoratory `@property` i `@imie.setter` umożliwiają odpowiednio odczyt i modyfikację wartości atrybutu _imie. Dzięki nim, podczas próby dostępu do atrybutu imie, wywoływane są odpowiednie metody, które mogą dodatkowo wykonywać pewne operacje, takie jak wyświetlanie komunikatów w tym przypadku.

Dekoratory te umożliwiają też wprowadzenie dodatkowej logiki, takiej jak walidacja danych czy reagowanie na zmiany wartości, co czyni je przydatnym narzędziem w programowaniu obiektowym.

### Pola i metody statyczne oraz klasowe

W programowaniu obiektowym często korzysta się z pól i metod statycznych oraz klasowych. Różnią się one od standardowych pól i metod instancji.

**Pola i metody statyczne** są związane z klasą, a nie z konkretnymi obiektami tej klasy. W Pythonie metody statyczne są tworzone przy użyciu dekoratora `@staticmethod`. Dostęp do nich jest możliwy zarówno poprzez nazwę klasy, jak i przez obiekt tej klasy.

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

Metody klasowe stanowią rozszerzenie metod statycznych. Są one tworzone przy użyciu dekoratora `@classmethod` i ich pierwszym parametrem jest `cls`, który reprezentuje samą klasę (podobnie jak self reprezentuje instancję). Metody klasowe mogą dostępować do pól klasowych oraz do innych metod klasowych.

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

W klasie Czlowiek mamy pole klasowe liczba_glow, metodę klasową `wyswietl_glowy()`, która korzysta z tego pola oraz metodę instancyjną `zwykla_funkcja()`. W przykładzie pokazano różne sposoby wywoływania metody klasowej, zarówno bezpośrednio z poziomu klasy, jak i z poziomu instancji. Kluczową różnicą jest to, że w metodach klasowych używa się `cls` do odwoływania się do klasowych atrybutów i metod, podczas gdy w metodach instancyjnych używa się `self`.
