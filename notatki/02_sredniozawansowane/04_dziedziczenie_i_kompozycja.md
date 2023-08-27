### Dziedziczenie i kompozycja

Dziedziczenie i kompozycja to dwie fundamentalne techniki obiektowo zorientowanego projektowania w programowaniu. Pomagają one w organizacji i ponownym użyciu kodu.

## Dziedziczenie

Dziedziczenie pozwala na tworzenie nowej klasy na podstawie istniejącej klasy, dziedzicząc jej atrybuty i metody. Nowa klasa, nazywana klasą podrzędną, może nadpisywać lub rozszerzać funkcje klasy nadrzędnej.

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

W tym przykładzie, klasa `Student` dziedziczy po klasie `Człowiek`. Dzięki temu `Student` dziedziczy wszystkie atrybuty i metody klasy `Człowiek` i może je rozszerzyć lub modyfikować.

### Kompozycja

Kompozycja polega na tworzeniu złożonych obiektów poprzez "komponowanie" ich z innych obiektów. Jest to technika tworzenia klasy przez umieszczenie obiektów innych klas jako jej atrybutów.

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
    def __init__(self, imie: str, nazwisko:str, pensja: Pensja):
        self.imie = imie
        self.nazwisko = nazwisko
        self.pensja = pensja # kompozycja: obiekt Pensja jest częścią obiektu Pracownik

    def __str__(self):
        return f"Pracownik: {self.imie} {self.nazwisko}, Zarabia rocznie: {self.pensja.roczna_pensja()} PLN"
```

W powyższym przykładzie klasa `Pracownik` korzysta z kompozycji, umieszczając obiekt klasy `Pensja` jako jej atrybut. Dzięki temu `Pracownik` może korzystać z metod zdefiniowanych w klasie Pensja poprzez instancję tej klasy.

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
