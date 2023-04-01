## Klasy i obiekty
Klasa to abstrakcyjny model, który definiuje jakiś zestaw cech i zachowań. Obiekt to konkretna instancja klasy. Możemy tworzyć dowolne klasy, niemniej jednak należy zastanowić się nad tym, jakie dane najlepiej byłoby trzymać razem pod jednym pojemnikiem oraz jakie funkcje mogą być przydatne do pracy z tymi danymi.

Przykład:

```python
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
```

W powyższym przykładzie tworzymy klasę Osoba, która posiada dwa pola danych: imie i nazwisko. Klasa ta zawiera również funkcję przedstaw_sie, która wyświetla komunikat z imieniem i nazwiskiem osoby. Następnie tworzymy dwa obiekty klasy Osoba i wywołujemy dla nich metodę przedstaw_sie.

### Dostęp do zmiennych w obiektach

W programowaniu obiektowym, zmienne przechowywane są w obiektach. Aby uzyskać dostęp do tych zmiennych, należy podać nazwę obiektu, następnie kropkę i nazwę zmiennej, którą chcemy odczytać.

```python
nazwa_obiektu.nazwa_zmiennej
```

Możliwe jest również modyfikowanie wartości tych zmiennych tak, jak w przypadku zwykłych zmiennych. 

```python
osoba = Osoba("Jan", "Kowalski")
print(osoba.imie) # Zostanie wyswietlone Jan
osoba.imie = "Adam"
print(osoba.imie) # Zostanie wyswietlone Adam
```

Możemy również użyć dekoratorów `@property` i `@nazwa_zmiennej.setter`, aby wywoływać funkcje przy odczycie lub modyfikacji wartości zmiennych przechowywanych w obiektach.

```python
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
```

Klasa Osoba posiada dwa atrybuty - imie oraz nazwisko. Zostały one oznaczone jako prywatne, poprzez dodanie podkreślnika na początku nazwy. Służy to do oznaczenia, że te atrybuty nie powinny być bezpośrednio modyfikowane lub odczytywane przez użytkownika klasy, lecz powinny być dostępne tylko poprzez odpowiednie metody.

Za pomocą dekoratorów `@property` oraz `@imie.setter` zostały zdefiniowane metody do odczytu oraz modyfikacji atrybutu imie. W momencie próby odczytu wartości atrybutu imie zostanie wyświetlony komunikat "Ktoś próbuje odczytać imię" oraz zostanie zwrócona jego wartość. Podobnie, w momencie próby modyfikacji atrybutu imie zostanie wyświetlony komunikat "Ktoś modyfikuje imię" oraz zostanie zmieniona jego wartość.

### Pola i metody statyczne

Pola i metody statyczne są używane w programowaniu obiektowym, ale nie należą one do konkretnych obiektów - należą do całej klasy. Pola statyczne to wszystkie pola zdefiniowane w klasie, natomiast metody statyczne są tworzone za pomocą dekoratora `@staticmethod`. Dostęp do pól i metod statycznych możliwy jest zarówno poprzez nazwę klasy, jak i nazwę obiektu klasy.

```python
class Czlowiek:
    liczba_glow = 1

    @staticmethod
    def wyswietl_glowy():
        print(f'Liczba glow: {Czlowiek.liczba_glow}')

Czlowiek.wyswietl_glowy() # Liczba glow: 1

przykladowy_czlowiek = Czlowiek()
przykladowy_czlowiek.wyswietl_glowy() # Liczba glow: 1
```

Metody klasowe to rozszerzenie metod statycznych - są tworzone za pomocą dekoratora `@classmethod`. Pierwszym parametrem metod klasowych jest `cls`, a nie `self`, jak w przypadku metod obiektowych. Metody klasowe są przydatne, gdy chcemy uzyskać dostęp do pól klasy lub do innych metod klasy.

```python
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
```

Klasa `Czlowiek` zawiera pole statyczne `liczba_glow` oraz metodę klasową `wyswietl_glowy()`. Metoda ta wyświetla wartość pola `liczba_glow` przy pomocy f-stringów. Metoda `zwykla_funkcja()` jest zwykłą metodą instancyjną i wywołuje metodę klasową `wyswietl_glowy()`. Można się do niej odwołać zarówno poprzez nazwę klasy, jak i nazwę obiektu. W przykładzie są przedstawione trzy sposoby wywołania tej metody: bezpośrednio z poziomu klasy, z poziomu obiektu oraz z poziomu metody instancyjnej. W każdym przypadku wyświetlona zostanie wartość zmiennej `liczba_glow`.
