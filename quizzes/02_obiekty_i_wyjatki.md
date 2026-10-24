# Obiekty, wyjątki i serializacja — quiz

Notatki: [Klasy i obiekty](../notatki/02_sredniozawansowane/01_klasy_i_obiekty.md), [Referencje i kopiowanie](../notatki/02_sredniozawansowane/02_referencje_i_kopiowanie.md), [Czyste funkcje i skutki uboczne](../notatki/02_sredniozawansowane/03_czyste_funkcje_i_skutki_uboczne.md), [Dziedziczenie i kompozycja](../notatki/02_sredniozawansowane/04_dziedziczenie_i_kompozycja.md), [Klasy danych](../notatki/02_sredniozawansowane/12_klasy_danych.md), [Wyrażenia regularne](../notatki/02_sredniozawansowane/05_wyrazenia_regularne.md), [Wyjątki](../notatki/02_sredniozawansowane/06_wyjatki.md), [Serializacja](../notatki/02_sredniozawansowane/16_serializacja.md)

Sprawdź, czy rozumiesz klasy, referencje, dziedziczenie, klasy danych, wyrażenia regularne, wyjątki i serializację.

#### Q. Co wypisze ten program?

```python
class Licznik:
    wartosc = 0

a = Licznik()
b = Licznik()
a.wartosc = 5
Licznik.wartosc = 10
print(a.wartosc, b.wartosc)
```

* [ ] `10 10`
* [x] `5 10`
* [ ] `5 0`
* [ ] `5 5`

> **Wyjaśnienie:** `a.wartosc = 5` tworzy atrybut instancji, który przesłania pole klasowe tylko w obiekcie `a`. Obiekt `b` nie ma własnego atrybutu, więc odczytuje zmienione pole klasowe `Licznik.wartosc`.

#### Q. Co się stanie po uruchomieniu tego programu?

```python
class Osoba:
    def __init__(self, imie):
        self._imie = imie

    @property
    def imie(self):
        return self._imie.upper()

o = Osoba("jan")
print(o.imie)
o.imie = "Adam"
```

* [ ] Wypisze `JAN` i zmieni imię na `Adam`
* [x] Wypisze `JAN`, a potem zgłosi `AttributeError`
* [ ] Wypisze `jan`, a potem zgłosi `AttributeError`
* [ ] Zgłosi `TypeError` już przy odczycie `o.imie`

> **Wyjaśnienie:** Odczyt `o.imie` wywołuje metodę oznaczoną `@property`, która zwraca wielkie litery. Bez zdefiniowanego `@imie.setter` właściwość jest tylko do odczytu, więc przypisanie kończy się `AttributeError`.

#### Q. Co jako pierwszy argument automatycznie otrzymuje metoda oznaczona `@classmethod`?

* [ ] Instancję, na rzecz której ją wywołano (`self`)
* [x] Klasę, na rzecz której ją wywołano (`cls`)
* [ ] Nic, zachowuje się jak zwykła funkcja
* [ ] Moduł, w którym zdefiniowano klasę

> **Wyjaśnienie:** Metoda klasowa dostaje referencję do klasy jako `cls`, więc może czytać i zmieniać pola klasowe. Bez żadnego automatycznego argumentu działa `@staticmethod`, a `self` otrzymują zwykłe metody instancyjne.

#### Q. Co wypisze ten program?

```python
class Punkt:
    def __init__(self, x):
        self.x = x

    def __repr__(self):
        return f"Punkt({self.x})"

    def __str__(self):
        return f"<{self.x}>"

p = Punkt(1)
print(p, [p])
```

* [ ] `Punkt(1) [Punkt(1)]`
* [ ] `<1> [<1>]`
* [x] `<1> [Punkt(1)]`
* [ ] `Punkt(1) [<1>]`

> **Wyjaśnienie:** `print(p)` używa czytelnej reprezentacji z `__str__`. Lista przy zamianie na napis pokazuje swoje elementy przez `__repr__`, czyli reprezentację „programistyczną”.

#### Q. Co wypisze ten program?

```python
from dataclasses import dataclass

class A:
    def __init__(self, x):
        self.x = x

@dataclass
class B:
    x: int

print(A(1) == A(1), B(1) == B(1))
```

* [ ] `True True`
* [ ] `False False`
* [ ] `True False`
* [x] `False True`

> **Wyjaśnienie:** Zwykła klasa bez `__eq__` porównuje tożsamość obiektów, a dwa wywołania `A(1)` tworzą różne obiekty. `@dataclass` generuje `__eq__`, które porównuje wartości pól.

#### Q. Którą metodę specjalną trzeba zdefiniować, aby obiekt można było wywołać jak funkcję, np. `obj()`?

* [ ] `__init__`
* [ ] `__new__`
* [x] `__call__`
* [ ] `__enter__`

> **Wyjaśnienie:** Wywołanie `obj(...)` uruchamia `obj.__call__(...)`. `__init__` i `__new__` działają przy tworzeniu obiektu, a `__enter__` przy wejściu do bloku `with`.

#### Q. Co wypisze ten program?

```python
a = [1, [2, 3]]
b = a[:]
b[0] = 100
b[1].append(4)
print(a)
```

* [ ] `[1, [2, 3]]`
* [x] `[1, [2, 3, 4]]`
* [ ] `[100, [2, 3, 4]]`
* [ ] `[100, [2, 3]]`

> **Wyjaśnienie:** Wycinek `a[:]` tworzy kopię płytką: nowa jest tylko zewnętrzna lista, a wewnętrzna lista jest wspólna. Podmiana `b[0]` nie dotyczy `a`, ale `append` na wspólnej liście jest widoczny w obu.

#### Q. Co wypisze ten program?

```python
import copy

a = [[1], [2]]
b = copy.copy(a)
c = copy.deepcopy(a)
print(a[0] is b[0], a[0] is c[0], a == c)
```

* [x] `True False True`
* [ ] `False False True`
* [ ] `True True True`
* [ ] `True False False`

> **Wyjaśnienie:** Kopia płytka współdzieli wewnętrzne listy, więc `a[0] is b[0]`. Kopia głęboka tworzy nowe wewnętrzne obiekty, które nie są tymi samymi obiektami, ale mają równe wartości.

#### Q. Co wypisze ten program?

```python
def dodaj(x, lista=[]):
    lista.append(x)
    return lista

dodaj(1)
dodaj(2)
print(dodaj(3))
```

* [ ] `[3]`
* [ ] `[1, 3]`
* [x] `[1, 2, 3]`
* [ ] `[[1], [2], [3]]`

> **Wyjaśnienie:** Wartość domyślna jest wyliczana raz, przy definicji funkcji, więc wszystkie wywołania bez drugiego argumentu dzielą tę samą listę. Bezpieczny wzorzec to `lista=None` i utworzenie nowej listy w środku funkcji.

#### Q. Co wypisze ten program?

```python
def zmien(lista):
    lista.append(4)
    lista = [0]
    lista.append(5)

dane = [1, 2, 3]
zmien(dane)
print(dane)
```

* [ ] `[1, 2, 3]`
* [ ] `[0, 5]`
* [ ] `[1, 2, 3, 4, 5]`
* [x] `[1, 2, 3, 4]`

> **Wyjaśnienie:** Funkcja dostaje referencję do tej samej listy, więc pierwsze `append` zmienia `dane`. Przypisanie `lista = [0]` wiąże tylko lokalną nazwę z nowym obiektem i nie zmienia listy na zewnątrz.

#### Q. Co wypisze ten program?

```python
t = (1, [2, 3])
t[1].append(4)
print(t)
```

* [ ] Zgłosi `TypeError`
* [x] `(1, [2, 3, 4])`
* [ ] `(1, [2, 3])`
* [ ] `(1, [2, 3], 4)`

> **Wyjaśnienie:** Krotka jest niemutowalna w tym sensie, że nie można podmienić jej elementów. Przechowuje jednak referencję do listy, a samą listę można modyfikować, np. metodą `append`.

#### Q. Która funkcja jest czysta?

* [x] `def f(x): return x * 2`
* [ ] `def f(x): print(x); return x`
* [ ] `def f(t): t.sort(); return t`
* [ ] `def f(): return random.random()`

> **Wyjaśnienie:** Czysta funkcja zależy tylko od argumentów i nie ma skutków ubocznych. `print` to operacja wyjścia, `sort()` zmienia przekazaną listę, a `random.random()` daje różne wyniki przy każdym wywołaniu.

#### Q. Dlaczego wyniki czystej funkcji można bezpiecznie zapamiętywać (memoizować)?

* [ ] Bo czyste funkcje zawsze wykonują się szybciej od nieczystych
* [x] Bo czysta funkcja dla tych samych argumentów daje ten sam wynik
* [ ] Bo czyste funkcje nie przyjmują argumentów
* [ ] Bo ich wynik jest zawsze obiektem niemutowalnym

> **Wyjaśnienie:** Memoizacja zakłada, że ponowne wywołanie z tymi samymi argumentami da ten sam wynik, a pominięcie go nie zgubi żadnego skutku ubocznego. Dla funkcji zależnych od stanu zewnętrznego (czasu, plików, zmiennych globalnych) zapamiętany wynik może być nieaktualny.

#### Q. Co wypisze ten program?

```python
def podwoj(lista):
    for i in range(len(lista)):
        lista[i] *= 2
    return lista

a = [1, 2]
b = podwoj(a)
print(a, b is a)
```

* [ ] `[1, 2] False`
* [ ] `[2, 4] False`
* [x] `[2, 4] True`
* [ ] `[1, 2] True`

> **Wyjaśnienie:** Funkcja modyfikuje przekazaną listę w miejscu i zwraca ten sam obiekt, więc ma skutek uboczny. Czysta wersja zwróciłaby nową listę, np. `[x * 2 for x in lista]`.

#### Q. Co wypisze ten program?

```python
class A:
    def opis(self):
        return "A"

class B(A):
    def opis(self):
        return "B+" + super().opis()

class C(B):
    pass

print(C().opis())
```

* [ ] `A`
* [ ] `B`
* [x] `B+A`
* [ ] `C+B+A`

> **Wyjaśnienie:** `C` nie definiuje `opis`, więc dziedziczy metodę z `B`. Ta dokleja wynik metody klasy bazowej `A`, wywołanej przez `super()`.

#### Q. Co wypisze ten program?

```python
class A:
    def kto(self):
        return "A"

class B(A):
    def kto(self):
        return "B"

class C(A):
    def kto(self):
        return "C"

class D(B, C):
    pass

print(D().kto())
```

* [x] `B`
* [ ] `C`
* [ ] `A`
* [ ] Zgłosi `TypeError` z powodu konfliktu

> **Wyjaśnienie:** Przy wielokrotnym dziedziczeniu Python szuka metody według MRO, które dla `D(B, C)` ma kolejność `D, B, C, A, object`. Pierwsza znaleziona implementacja pochodzi z `B`.

#### Q. Co się stanie po uruchomieniu tego programu?

```python
from abc import ABC, abstractmethod

class Ksztalt(ABC):
    @abstractmethod
    def pole(self):
        pass

class Kwadrat(Ksztalt):
    def __init__(self, a):
        self.a = a

k = Kwadrat(2)
```

* [ ] Utworzy obiekt, a `k.pole()` zwróci `None`
* [ ] Utworzy obiekt; błąd pojawi się przy `k.pole()`
* [x] Zgłosi `TypeError` przy tworzeniu `Kwadrat(2)`
* [ ] Zgłosi `NotImplementedError` przy tworzeniu obiektu

> **Wyjaśnienie:** Klasa, która nie implementuje wszystkich metod abstrakcyjnych, sama pozostaje abstrakcyjna. Próba utworzenia jej instancji kończy się od razu `TypeError`.

#### Q. Które zdanie opisuje relację typową dla kompozycji, a nie dziedziczenia?

* [ ] Samochód jest pojazdem
* [x] Samochód ma silnik
* [ ] Student jest człowiekiem
* [ ] Kwadrat jest kształtem

> **Wyjaśnienie:** Kompozycja modeluje relację „ma” (obiekt składa się z innych obiektów), a dziedziczenie relację „jest rodzajem”. Silnik jest częścią samochodu, a nie jego nadklasą.

#### Q. Co wypisze ten program?

```python
class Kaczka:
    def kwacz(self):
        return "Kwa"

class Robot:
    def kwacz(self):
        return "Bip"

class Kot:
    pass

for x in [Kaczka(), Robot(), Kot()]:
    try:
        print(x.kwacz(), end=" ")
    except AttributeError:
        print("?", end=" ")
```

* [ ] `Kwa ? ?`
* [x] `Kwa Bip ?`
* [ ] `Kwa Bip Kwa`
* [ ] `? ? ?`

> **Wyjaśnienie:** To duck typing: liczy się to, czy obiekt ma metodę `kwacz`, a nie po jakiej klasie dziedziczy. `Robot` ją ma, choć nie jest kaczką, a `Kot` jej nie ma, więc pojawia się `AttributeError`.

#### Q. Dlaczego w klasie danych pole z listą definiuje się jako `field(default_factory=list)`, a nie `= []`?

* [x] Aby każda instancja dostała własną, nową listę
* [ ] Aby lista stała się niemutowalna po utworzeniu
* [ ] Aby pole zostało pominięte w `__repr__`
* [ ] Bo pole z listą nie może mieć adnotacji typu

> **Wyjaśnienie:** Jedna lista jako wartość domyślna byłaby współdzielona przez wszystkie instancje, dlatego `dataclass` nawet odrzuca `= []` błędem. `default_factory` wywołuje `list()` osobno dla każdego nowego obiektu.

#### Q. Co wypisze ten program?

```python
from dataclasses import dataclass

@dataclass(order=True)
class Wersja:
    glowna: int
    poboczna: int

wersje = sorted([Wersja(1, 10), Wersja(1, 2), Wersja(0, 99)])
print([(w.glowna, w.poboczna) for w in wersje])
```

* [ ] `[(1, 2), (1, 10), (0, 99)]`
* [ ] `[(0, 99), (1, 10), (1, 2)]`
* [x] `[(0, 99), (1, 2), (1, 10)]`
* [ ] Zgłosi `TypeError`

> **Wyjaśnienie:** `order=True` generuje metody porównania, które porównują obiekty jak krotki pól w kolejności definicji. Najpierw decyduje `glowna`, a przy remisie `poboczna`.

#### Q. Co wypisze ten program?

```python
from dataclasses import dataclass, replace

@dataclass(frozen=True)
class Punkt:
    x: int
    y: int

p = Punkt(1, 2)
q = replace(p, y=5)
print(p, q)
```

* [x] `Punkt(x=1, y=2) Punkt(x=1, y=5)`
* [ ] `Punkt(x=1, y=5) Punkt(x=1, y=5)`
* [ ] Zgłosi `FrozenInstanceError`
* [ ] `Punkt(x=1, y=2) Punkt(x=5, y=2)`

> **Wyjaśnienie:** `replace()` nie zmienia oryginału, tylko tworzy nową instancję z podmienionymi polami, więc działa także dla klas `frozen=True`. Błąd pojawiłby się dopiero przy próbie przypisania, np. `p.y = 5`.

#### Q. Co wypisze ten program?

```python
from dataclasses import dataclass, field

@dataclass
class Prostokat:
    a: float
    b: float
    pole: float = field(init=False)

    def __post_init__(self):
        self.pole = self.a * self.b

print(Prostokat(2, 3))
```

* [ ] `Prostokat(a=2, b=3)`
* [x] `Prostokat(a=2, b=3, pole=6)`
* [ ] Zgłosi `TypeError`: brak argumentu `pole`
* [ ] `Prostokat(a=2, b=3, pole=None)`

> **Wyjaśnienie:** `field(init=False)` usuwa pole z parametrów `__init__`, a `__post_init__` uruchamia się zaraz po wygenerowanym konstruktorze i je wylicza. Pole nadal jest widoczne w `__repr__`.

#### Q. Co wypisze ten program?

```python
import re

print(re.match(r"\d+", "abc 123"), re.search(r"\d+", "abc 123").group())
```

* [ ] `123 123`
* [ ] `None None`
* [ ] `abc 123`
* [x] `None 123`

> **Wyjaśnienie:** `re.match` szuka dopasowania tylko na początku napisu, a tam jest litera, więc zwraca `None`. `re.search` przeszukuje cały napis i znajduje `123`.

#### Q. Co wypisze ten program?

```python
import re

print(re.findall(r"<.+>", "<a><b>"))
```

* [x] `['<a><b>']`
* [ ] `['<a>', '<b>']`
* [ ] `['a', 'b']`
* [ ] `[]`

> **Wyjaśnienie:** Kwantyfikator `+` jest zachłanny: `.+` pochłania jak najwięcej znaków, a potem cofa się tylko do ostatniego `>`. Osobne tagi daje wzorzec `<[^>]+>` albo leniwy `<.+?>`.

#### Q. Co wypisze ten program?

```python
import re

print(re.findall(r"\d{2,3}", "1 12 1234 56789"))
```

* [ ] `['12', '1234', '56789']`
* [ ] `['12', '123', '567']`
* [x] `['12', '123', '567', '89']`
* [ ] `['12', '123', '234', '567', '789']`

> **Wyjaśnienie:** `{2,3}` dopasowuje od dwóch do trzech cyfr, zachłannie, a kolejne dopasowanie zaczyna się tam, gdzie skończyło się poprzednie. Z `1234` zostaje samotna `4`, która nie spełnia minimum dwóch cyfr.

#### Q. Co wypisze ten program?

```python
import re

print(re.sub(r"(?P<r>\d{4})-(?P<m>\d{2})", r"\g<m>/\g<r>", "2024-03"))
```

* [ ] `2024/03`
* [x] `03/2024`
* [ ] `m/r`
* [ ] `\g<m>/\g<r>`

> **Wyjaśnienie:** W napisie zastępczym `\g<nazwa>` wstawia tekst dopasowany przez grupę nazwaną. Grupa `m` złapała `03`, a grupa `r` złapała `2024`.

#### Q. Co wypisze ten program?

```python
import re

print(bool(re.match(r"\d{3}", "1234")), bool(re.fullmatch(r"\d{3}", "1234")))
```

* [ ] `False False`
* [ ] `True True`
* [ ] `False True`
* [x] `True False`

> **Wyjaśnienie:** `re.match` wymaga dopasowania od początku, ale nie do końca napisu, więc `123` wystarcza. `re.fullmatch` wymaga, by wzorzec objął cały napis, a czwarta cyfra zostaje niedopasowana.

#### Q. Co wypisze ten program?

```python
import re

print(re.findall(r"\d+(?=\s*zł)", "5 USD, 10 zł, 20zł"))
```

* [ ] `['10 zł', '20zł']`
* [ ] `['5', '10', '20']`
* [x] `['10', '20']`
* [ ] `['5']`

> **Wyjaśnienie:** Lookahead `(?=...)` sprawdza, co następuje po dopasowaniu, ale nie dołącza tego do wyniku. Dlatego zwracane są same liczby, i tylko te, po których następuje `zł`.

#### Q. Co wypisze ten program?

```python
def f():
    try:
        print("try", end=" ")
        return 1
    finally:
        print("finally", end=" ")

print(f())
```

* [ ] `try 1`
* [ ] `try 1 finally`
* [x] `try finally 1`
* [ ] `finally try 1`

> **Wyjaśnienie:** Blok `finally` wykonuje się zawsze, także gdy `try` kończy się instrukcją `return`. Funkcja zwraca 1 dopiero po wykonaniu `finally`, a zewnętrzny `print` wypisuje wynik na końcu.

#### Q. Co wypisze ten program?

```python
try:
    x = int("12")
except ValueError:
    print("błąd")
else:
    print("ok", x)
finally:
    print("koniec")
```

* [x] `ok 12`, a w następnej linii `koniec`
* [ ] Tylko `ok 12`
* [ ] `błąd`, a w następnej linii `koniec`
* [ ] Tylko `koniec`

> **Wyjaśnienie:** Konwersja się udała, więc `except` jest pomijany, a wykonuje się `else`, przeznaczone na kod zależny od sukcesu. `finally` działa zawsze, niezależnie od wyniku.

#### Q. Co wypisze ten program?

```python
try:
    [1, 2][5]
except LookupError:
    print("lookup")
except IndexError:
    print("index")
```

* [ ] `index`
* [x] `lookup`
* [ ] `lookup` i `index`
* [ ] Zgłosi nieobsłużony `IndexError`

> **Wyjaśnienie:** `IndexError` dziedziczy po `LookupError`, a Python wybiera pierwszy pasujący blok `except`. Bardziej szczegółowe wyjątki należy więc obsługiwać przed ogólnymi.

#### Q. Który z wyjątków nie dziedziczy po `Exception`?

* [ ] `ZeroDivisionError`
* [ ] `FileNotFoundError`
* [ ] `StopIteration`
* [x] `KeyboardInterrupt`

> **Wyjaśnienie:** `KeyboardInterrupt` (podobnie jak `SystemExit`) dziedziczy bezpośrednio po `BaseException`, dzięki czemu `except Exception` nie blokuje przerwania programu przez Ctrl+C.

#### Q. Co wypisze ten program?

```python
try:
    try:
        1 / 0
    except ZeroDivisionError as e:
        raise ValueError("zła wartość") from e
except ValueError as err:
    print(type(err.__cause__).__name__)
```

* [ ] `ValueError`
* [ ] `NoneType`
* [ ] `ArithmeticError`
* [x] `ZeroDivisionError`

> **Wyjaśnienie:** `raise ... from e` łączy wyjątki w łańcuch i zapisuje pierwotny wyjątek w atrybucie `__cause__` nowego. Dzięki temu nie ginie informacja o rzeczywistej przyczynie błędu.

#### Q. Co wypisze ten program?

```python
class BladAplikacji(Exception):
    def __init__(self, kod):
        self.kod = kod
        super().__init__(f"Kod błędu: {kod}")

try:
    raise BladAplikacji(404)
except Exception as e:
    print(e, e.kod)
```

* [x] `Kod błędu: 404 404`
* [ ] `BladAplikacji 404`
* [ ] `404 404`
* [ ] `Kod błędu: 404 None`

> **Wyjaśnienie:** Komunikat przekazany do `super().__init__()` staje się tekstem wyjątku zwracanym przez `str(e)`. `except Exception` łapie też klasy pochodne, a złapany obiekt to nadal `BladAplikacji` z atrybutem `kod` ustawionym w `__init__`.

#### Q. Co wypisze ten program?

```python
import json

dane = {"krotka": (1, 2), "klucz": None, 1: True}
print(json.dumps(dane))
```

* [ ] `{"krotka": (1, 2), "klucz": None, 1: True}`
* [x] `{"krotka": [1, 2], "klucz": null, "1": true}`
* [ ] `{"krotka": [1, 2], "klucz": null, 1: true}`
* [ ] Zgłosi `TypeError` z powodu krotki

> **Wyjaśnienie:** JSON nie ma krotek ani `None`, więc krotka staje się tablicą, a `None` wartością `null`. Klucze obiektów JSON muszą być napisami, dlatego liczba `1` zamienia się w `"1"`.

#### Q. Co wypisze ten program?

```python
import json

print(json.dumps({"imię": "Łukasz"}))
```

* [ ] `{"imię": "Łukasz"}`
* [x] `{"imi\u0119": "\u0141ukasz"}`
* [ ] `{'imię': 'Łukasz'}`
* [ ] Zgłosi `UnicodeEncodeError`

> **Wyjaśnienie:** Domyślnie `json.dumps` używa `ensure_ascii=True` i zamienia znaki spoza ASCII na sekwencje `\uXXXX`. Aby zachować polskie litery, trzeba przekazać `ensure_ascii=False`.

#### Q. Dlaczego nie należy wczytywać plików `pickle` z niezaufanego źródła?

* [ ] Bo `pickle` gubi typy liczbowe przy odczycie
* [ ] Bo pliki `pickle` działają tylko w systemie, w którym je utworzono
* [x] Bo deserializacja może wykonać dowolny kod
* [ ] Bo `pickle.load` trwale zmienia wczytywany plik

> **Wyjaśnienie:** Format `pickle` może opisywać wywołania dowolnych funkcji przy odtwarzaniu obiektów, więc spreparowany plik uruchomi złośliwy kod. Do danych z zewnątrz lepiej użyć JSON, który nie wykonuje kodu.

#### Q. W jakim trybie trzeba otworzyć plik, aby zapisać do niego obiekt przez `pickle.dump`?

* [ ] `"w"`
* [x] `"wb"`
* [ ] `"a"`
* [ ] `"r+"`

> **Wyjaśnienie:** `pickle` produkuje bajty, więc plik musi być otwarty w trybie binarnym: `"wb"` do zapisu i `"rb"` do odczytu. W trybie tekstowym `"w"` zapis kończy się `TypeError`.

#### Q. Co wypisze ten program?

```python
import xml.etree.ElementTree as ET

root = ET.fromstring("<osoba><imie>Ola</imie><wiek>30</wiek></osoba>")
print(root.find("wiek").text + "1")
```

* [ ] `31`
* [x] `301`
* [ ] `None`
* [ ] Zgłosi `TypeError`

> **Wyjaśnienie:** Atrybut `.text` elementu XML jest zawsze napisem, więc `+` łączy napisy zamiast dodawać liczby. Dlatego przy deserializacji trzeba jawnie konwertować wartości, np. `int(...)`.
