## Paradygmaty w programowaniu

Paradygmat w programowaniu to sposób myślenia o tworzeniu programów, oparty na zbiorze mechanizmów dostępnych w danym języku programowania. Istnieją dwa główne paradygmaty: imperatywny i deklaratywny.

## Paradygmat imperatywny

Paradygmat imperatywny opiera się na sekwencji instrukcji, które modyfikują stan programu. Jest to podejście bottom-up, czyli skupiające się na krokach prowadzących do osiągnięcia pożądanego stanu. Podparadygmaty imperatywne to:

* Proceduralny: oparty na koncepcji procedur i funkcji, pozwala na pogrupowanie kodu w funkcje.
* Obiektowy: oparty na koncepcji klas i obiektów, pozwala na pogrupowanie kodu w klasy zbudowane z pól (określających stan) oraz metod (modyfikujących stan).

```python
class Car:
    def __init__(self, position, speed):
        self.position = position
        self.speed = speed

    def move(self, time):
        self.position += self.speed * time

car = Car(0, 10)
car.move(1)
print(car.position)  # 10
car.move(0.5)
print(car.position)  # 15
```

## Paradygmat deklaratywny

Paradygmat deklaratywny polega na wskazaniu pożądanego stanu programu bez konieczności definiowania wszystkich kroków prowadzących do niego. Jest to podejście top-down, czyli skupiające się na osiągnięciu pożądanego rezultatu poprzez określenie zależności i reguł. Podparadygmaty deklaratywne to:

* Funkcyjny: kod składa się z funkcji, które są wzorowane na wyrażeniach matematycznych i nie modyfikują zewnętrznych danych.
* Logiczny: kod składa się z zestawu zależności i obliczenia są dowodem pewnego twierdzenia na podstawie tych zależności.

```python
from functools import reduce

def move(position, speed, time):
  return position + speed * time

def get_positions(position, speed, time_list):
  return list(map(lambda time: move(position, speed, time), time_list))

def get_prefix_sums(lst):
  return list(reduce(lambda x, y: x + [x[-1] + y], lst, [0]))

def get_path(position, speed, time_list):
  return get_prefix_sums(get_positions(position, speed, time_list))[1:]

print(get_path(0, 10, [1, 0.5]))  # [10, 15]
```

## Współczesne języki programowania

Współczesne języki programowania często łączą różne paradygmaty i pozwalają na mieszanie składni z różnych paradygatów w jednym programie. Dzięki temu programiści mogą wybierać najlepsze rozwiązanie dla konkretnego problemu i optymalizować swój kod.

Poniżej przedstawiono kilka elementów Pythona, które można uznać za charakterystyczne dla programowania obiektowego oraz funkcyjnego:
Elementy charakterystyczne dla programowania obiektowego:

* Klasy: służą do definiowania nowych typów danych, zawierają pola (określające stan obiektu) oraz metody (modyfikujące stan obiektu).
* Dziedziczenie: pozwala na tworzenie nowych klas, które rozszerzają istniejące klasy o dodatkowe funkcjonalności.
* Enkapsulacja: polega na ukrywaniu szczegółów implementacji w obrębie klasy, co umożliwia użytkownikom korzystanie z obiektów bez konieczności znajomości ich wewnętrznej struktury.

Elementy charakterystyczne dla programowania funkcyjnego:

* First-class functions: funkcje są traktowane jako zwykłe obiekty, co oznacza, że można je przekazywać jako argumenty do innych funkcji, zwracać je jako wartości z funkcji itp.
* Higher-order functions: funkcje, które jako argumenty przyjmują inne funkcje lub zwracają je jako wartość.
* Funkcje lambda: krótkie funkcje, które są często używane do tworzenia anonimowych funkcji w programowaniu funkcyjnym.

Oczywiście powyższe elementy to tylko wybrane przykłady i nie wyczerpują wszystkich elementów charakterystycznych dla programowania obiektowego i funkcyjnego w Pythonie. W rzeczywistości Python jest językiem hybrydowym,

## Stan

W programowaniu możemy mówić o dwóch rodzajach stanu: stateful i stateless. Stateful oznacza, że program zachowuje swój stan po wykonaniu określonej operacji i może go odczytać w późniejszym czasie. Stateless oznacza, że program nie zapamiętuje stanu po wykonaniu operacji i każde jej wywołanie traktowane jest jako odrębne zdarzenie.

Przykład funkcji trzymającej stan:

```python
counter = 0

def increment_counter():
  global counter
  counter += 1

increment_counter()
print(counter)  # 1
increment_counter()
print(counter)  # 2
```

Przykład funkcji nie zapamiętującej stanu:

```python
def increment_counter(counter):
  return counter + 1

counter = 0
counter = increment_counter(counter)
print(counter)  # 1
counter = increment_counter(counter)
print(counter)  # 2
```

## Zmienność danych

W programowaniu mówimy o dwóch rodzajach zmienności danych: mutowalność (mutability) i niezmienność (immutability). Mutowalność oznacza, że dane są zmienne i mogą być zmodyfikowane przez program. Niezmienność oznacza, że raz przypisane dane są niezmienne i nie mogą być zmodyfikowane przez program.

Przykłady mutowalnych wartości:

* listy: [1, 2, 3]
* słowniki: {'a': 1, 'b': 2}
* obiekty zdefiniowane przez użytkownika za pomocą klas

Przykłady niemutowalnych wartości:

* liczby: 1, 2, 3
* krotki: (1, 2, 3)
* napisy: 'abc'
* obiekty frozenset (niezmienne zbiory)

Po dodaniu elementu do listy (mutowalnej wartości), identyfikator obiektu pozostaje taki sam:

```python
# mutowalna lista
numbers = [1, 2, 3]
print(id(numbers))  # wyświetla unikalny identyfikator obiektu
numbers.append(4)
print(id(numbers))  # ten sam identyfikator
```

Natomiast po zmianie wartości niemutowalnej liczby, identyfikator obiektu ulega zmianie:

```python
# niemutowalna liczba
number = 1
print(id(number))  # wyświetla unikalny identyfikator obiektu
number += 1
print(id(number))  # inny identyfikator
```

## Czystość

Funkcja jest czysta, jeśli nie modyfikuje danych, których nie jest właścicielem. Czystość ma wiele zalet, takich jak czytelność kodu, optymalizacja kodu w czasie kompilacji oraz brak zjawiska wyścigu w programowaniu współbieżnym.

Przykłady czystych funkcji:

1. Funkcja zwracająca stałą wartość bez względu na jej argumenty:

```python
def stala(x):
    return 5
```

2. Funkcja zwracająca wartość zależną tylko od jednego z argumentów:

```python
def identity(x, y):
    return x
```

3. Funkcja zwracająca sumę dwóch argumentów:

```python
def suma(x, y):
    return x + y
```

Przykłady nieczystych funkcji:

1. Funkcja zmieniająca wartość zmiennej globalnej:

```python
licznik = 0
def dodaj_do_licznika(x):
    global licznik
    licznik += x
    return licznik
```

2. Funkcja modyfikująca elementy listy przekazanej jako argument:
def zapisz_do_pliku(dane, nazwa_pliku):
    with open(nazwa_pliku, "w") as f:
        f.write(dane)
    return nazwa_pliku
```python
def modyfikuj_liste(lst):
    lst[0] = 5
    return lst
```

3. Funkcja zapisująca dane do pliku:

```python
def zapisz_do_pliku(dane, nazwa_pliku):
    with open(nazwa_pliku, "w") as f:
        f.write(dane)
    return nazwa_pliku
```

## Literatura

* https://web.mit.edu/6.005/www/fa15/classes/09-immutability/
* https://cs.lmu.edu/~ray/notes/paradigms/
* https://homes.cs.aau.dk/~normark/prog3-03/html/notes/paradigms-book.html
