## Paradygmaty w programowaniu

Paradygmat w programowaniu to nie tylko sposób myślenia o tworzeniu programów, ale także zestaw konceptów i technik, które kierują projektowaniem i strukturyzacją oprogramowania. Te filozofie wpływają na to, jak programiści definiują problemy oraz jak podejmują decyzje o sposobie ich rozwiązania. Chociaż istnieją dwa główne paradygmaty, imperatywny i deklaratywny, rzeczywistość jest bardziej złożona i wiele języków pozwala korzystać z wielu paradygmatów jednocześnie.

### Paradygmat imperatywny

Paradygmat imperatywny koncentruje się na "jak to zrobić". Opisuje sekwencje instrukcji, które modyfikują stan programu. Działanie programu opiera się na sekwencji operacji zmieniających jego stan.

#### Proceduralny

Paradygmat proceduralny jest podzbiorem paradygmatu imperatywnego i opiera się na organizacji kodu za pomocą funkcji i procedur, które wykonują określone zadania.

Przykład w Pythonie:

```python
def add(a, b):
    return a + b

result = add(2, 3)
print(result)  # 5
```

#### Obiektowy

Paradygmat obiektowy skupia się na jednostkach zwanych obiektami, które są instancjami klas. Klasy definiują zachowanie (metody) i stan (atrybuty) obiektów.

Przykład w Pythonie:

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

### Paradygmat deklaratywny

Paradygmat deklaratywny skupia się na "co chcemy osiągnąć", zamiast na "jak to osiągnąć". Opisuje żądany wynik, nie zajmując się konkretnymi krokami prowadzącymi do jego osiągnięcia.

#### Funkcyjny

W programowaniu funkcyjnym kod jest zbiorem funkcji, które są wzorowane na wyrażeniach matematycznych. Funkcje nie mają efektów ubocznych i nie modyfikują stanu zewnętrznego.

Przykład w Pythonie:

```python
from itertools import accumulate

def move(position, speed, time):
    return position + speed * time

def get_positions(position, speed, time_list):
    positions = accumulate(time_list, lambda pos, time: move(pos, speed, time), initial=position)
    return list(positions)[1:]  # Pomijamy pierwszą pozycję, która jest początkową pozycją

def get_path(position, speed, time_list):
    return get_positions(position, speed, time_list)

print(get_path(0, 10, [1, 0.5]))  # [10, 15]
```

Analogiczny kod w Haskellu:

```haskell
-- Definicja funkcji move
move :: Double -> Double -> Double -> Double
move position speed time = position + speed * time

-- Funkcja getPositions używająca scanl
getPositions :: Double -> Double -> [Double] -> [Double]
getPositions position speed timeList = tail $ scanl (\pos time -> move pos speed time) position timeList

-- Funkcja getPath
getPath :: Double -> Double -> [Double] -> [Double]
getPath = getPositions

-- Przykład użycia
main :: IO ()
main = print $ getPath 0 10 [1, 0.5]  -- [10, 15]
```

#### Logiczny

Paradygmat logiczny skupia się na określaniu relacji i zależności. Programy są zbiorem faktów i reguł, a wykonanie programu polega na poszukiwaniu dowodów czy spełnienia określonych warunków.

Przykład w Prologu:

```prolog
parent(tom, bob).
parent(bob, ann).
ancestor(X, Y) :- parent(X, Y).
ancestor(X, Y) :- parent(X, Z), ancestor(Z, Y).
```

### Współczesne języki programowania

Współczesne języki programowania często łączą różne paradygmaty i oferują elastyczność, pozwalając programistom na mieszanie składni z różnych paradygmatów w jednym programie. Dzięki temu programiści mają swobodę wyboru i mogą stosować najbardziej odpowiednie narzędzia dla konkretnego problemu, co z kolei przekłada się na większą efektywność rozwoju i optymalizację kodu.

Python to język, który z powodzeniem łączy cechy programowania obiektowego oraz funkcyjnego. Oto kilka charakterystycznych elementów dla obu tych paradygmatów w Pythonie:

#### Elementy charakterystyczne dla programowania obiektowego

* **Klasy**: Służą do definiowania nowych typów danych i zawierają zarówno atrybuty (reprezentujące stan obiektu), jak i metody (operujące na tym stanie).
* **Dziedziczenie**: Umożliwia tworzenie klas pochodnych, które dziedziczą atrybuty i metody po klasie bazowej, pozwalając jednocześnie na ich rozszerzanie lub modyfikację.
* **Enkapsulacja**: Ukrywa wewnętrzne szczegóły klasy, dzięki czemu można je modyfikować bez wpływu na kod korzystający z tej klasy.

Przykład enkapsulacji i dziedziczenia w Pythonie:

```python
class Vehicle:
    def __init__(self, make, model):
        self._make = make
        self._model = model

    def display_info(self):
        print(f"Vehicle Make: {self._make}, Model: {self._model}")

class Car(Vehicle):
    def __init__(self, make, model, doors):
        super().__init__(make, model)
        self._doors = doors

    def display_info(self):
        super().display_info()
        print(f"Number of doors: {self._doors}")

my_car = Car("Toyota", "Corolla", 4)
my_car.display_info()
```

#### Elementy charakterystyczne dla programowania funkcyjnego

* **First-class functions**: W Pythonie funkcje są obiektami pierwszej klasy, co oznacza, że można je przekazywać jako argumenty, zwracać z innych funkcji czy przypisywać do zmiennych.
* **Higher-order functions**: Są to funkcje, które przyjmują inne funkcje jako argumenty lub zwracają je. Przykładem może być funkcja `map` lub `filter`.
* **Funkcje lambda**: Umożliwiają szybkie tworzenie anonimowych funkcji na potrzeby jednorazowego użycia.

Przykład użycia funkcji pierwszej klasy, funkcji wyższego rzędu i funkcji lambda w Pythonie:

```python
# First-class function
def square(x):
    return x * x

def apply_function(func, value):
    return func(value)

print(apply_function(square, 5))  # 25

# Higher-order function with lambda
numbers = [1, 2, 3, 4, 5]
squared_numbers = map(lambda x: x * x, numbers)
print(list(squared_numbers))  # [1, 4, 9, 16, 25]

# Filter with lambda
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))  # [2, 4]
```

### Ewolucja OOP (Programowania Obiektowego)

Programowanie obiektowe (OOP) stało się dominującym paradygmatem w ciągu ostatnich dekad, ale jak każdy paradygmat, rozwijało się i dostosowywało do nowych wyzwań i koncepcji. W poniższym tekście omówimy kluczowe aspekty ewolucji OOP oraz ich znaczenie w współczesnym programowaniu.

#### Enkapsulacja, Abstrakcja, i Polimorfizm

* **Enkapsulacja**: Enkapsulacja odnosi się do praktyki ograniczania dostępu do pewnych składników obiektu i łączenia danych z zachowaniami. Chroni to integralność danych i ułatwia zarządzanie złożonością systemów. Przykładem enkapsulacji jest ukrywanie szczegółów implementacji klasy, co pozwala na modyfikację kodu bez wpływu na resztę programu.

* **Abstrakcja**: Abstrakcja pozwala na reprezentację złożonych systemów w bardziej ogólnej formie, ukrywając szczegóły. Dzięki abstrakcji, programiści mogą skupić się na wysokopoziomowych aspektach projektu, zamiast na szczegółach implementacyjnych. Na przykład, interfejsy i klasy abstrakcyjne w Java umożliwiają definiowanie ogólnych zachowań, które mogą być konkretyzowane przez klasy pochodne.

* **Polimorfizm**: Polimorfizm daje możliwość definiowania wielu form dla funkcji lub metod, dzięki czemu można je używać w różnorodny sposób. Umożliwia to tworzenie bardziej elastycznego i rozszerzalnego kodu. Przykładami polimorfizmu są metody przeciążone oraz interfejsy umożliwiające różne implementacje tej samej funkcji.

#### Klasy i Złożoność

Chociaż klasy są podstawowym budulcem OOP, mogą prowadzić do złożonych hierarchii i zależności. Ważne jest, aby zachować prostotę, unikając zbytniego powiązania i zagnieżdżenia. Dobre praktyki projektowe, takie jak wzorce projektowe (np. wzorzec projektowy Strategia, Dekorator czy Fabryka), pomagają zarządzać tą złożonością, promując modularność i ponowne użycie kodu.

#### Kolekcje w OOP

Tablice haszujące, listy i wektory są często używane w OOP, ale nie każda kolekcja musi być "obiektowo zorientowana". Ważne jest, aby wybierać odpowiednie struktury danych dla konkretnych zastosowań. Przykładowo, w Pythonie mamy do dyspozycji różne typy kolekcji, takie jak listy, sety i słowniki, które mogą być używane w ramach klas do zarządzania stanem obiektów.

#### Wyzwania OOP

Nadmierne poleganie na dziedziczeniu i głębokich hierarchiach klas może prowadzić do trudności w utrzymaniu kodu, szczególnie w dużych systemach, gdzie zmiana w jednym miejscu może wpłynąć na wiele innych. Alternatywą dla dziedziczenia jest kompozycja, która polega na budowaniu klas poprzez łączenie obiektów innych klas. Podejście to często prowadzi do bardziej elastycznych i łatwiejszych w utrzymaniu systemów.

#### Funkcyjne podejście do OOP

Techniki programowania funkcyjnego, takie jak closure czy funkcje wyższego rzędu, mogą być użyte do realizacji niektórych koncepcji obiektowych, takich jak enkapsulacja czy polimorfizm, oferując jednocześnie większą elastyczność i prostotę. Na przykład, w Pythonie funkcje wyższego rzędu mogą być używane do tworzenia bardziej modularnych i łatwych do testowania jednostek kodu.

#### OOP w Rust i Go

Zarówno Rust, jak i Go oferują podejście do enkapsulacji oparte na modułach, gdzie metody i pola są ograniczone do konkretnego zakresu. Chociaż różni się to od klasycznego OOP, nadal jest zgodne z jego głównymi założeniami. Rust, na przykład, używa struktur (structs) i implementacji (impl blocks) do definiowania metod, zachowując przy tym kontrolę nad prywatnością pól i metod.

#### Struktury zamiast klas

W językach takich jak Rust i Go, zamiast klas mamy do czynienia ze strukturami. Struktury te służą do reprezentowania danych i, w przeciwieństwie do klas, nie mają wbudowanej koncepcji dziedziczenia. Zamiast tego, programiści używają kompozycji i innych mechanizmów do osiągnięcia podobnych efektów.

Przykład struktury w Rust:

```rust
struct Car {
    position: i32,
    speed: i32,
}

impl Car {
    fn move(&mut self, time: i32) {
        self.position += self.speed * time;
    }
}

let mut car = Car { position: 0, speed: 10 };
car.move(1);
println!("{}", car.position);  // 10
car.move(0.5 as i32);
println!("{}", car.position);  // 15
```

#### Modularność w Rust

W praktyce, większość modułów w standardowej bibliotece Rust koncentruje się na jednym lub kilku ściśle powiązanych typach, co sprzyja przejrzystości, izolacji odpowiedzialności i ogólnej jakości kodu. Rust promuje również użycie traitów do definiowania wspólnych zachowań dla różnych typów, co zwiększa elastyczność i możliwości ponownego użycia kodu.

### Dalsza lektura

Aby zgłębić temat programowania obiektowego (OOP) i innych paradygmatów programowania, warto zapoznać się z poniższymi zasobami:

1. **Podstawy i koncepcje OOP**:
   - [Programowanie obiektowe - Wikipedia](https://pl.wikipedia.org/wiki/Programowanie_obiektowe) - Artykuł na Wikipedii przedstawiający podstawowe koncepcje OOP, takie jak klasy, obiekty, dziedziczenie i polimorfizm.
   - [Object-Oriented Programming Concepts](https://docs.oracle.com/javase/tutorial/java/concepts/index.html) - Przewodnik po podstawowych koncepcjach OOP na stronie Oracle.

2. **Enkapsulacja, Abstrakcja, i Polimorfizm**:
   - [Understanding OOP Encapsulation](https://www.geeksforgeeks.org/encapsulation-in-java/) - Artykuł na GeeksforGeeks omawiający enkapsulację w Java.
   - [Abstraction in Object-Oriented Programming](https://www.baeldung.com/java-abstraction) - Przewodnik po abstrakcji w OOP na Baeldung.
   - [Polymorphism in OOP](https://www.tutorialspoint.com/java/java_polymorphism.htm) - Artykuł na TutorialsPoint omawiający polimorfizm w Java.

3. **Kolekcje w OOP**:
   - [Data Structures in Object-Oriented Programming](https://www.javatpoint.com/data-structures-in-java) - Artykuł na JavaTpoint omawiający różne struktury danych używane w OOP.
   - [Using Collections in Java](https://www.geeksforgeeks.org/collections-in-java-2/) - Przewodnik po kolekcjach w Java na GeeksforGeeks.

4. **Wyzwania OOP**:
   - [Challenges of Object-Oriented Programming](https://www.codingninjas.com/codestudio/library/challenges-of-object-oriented-programming) - Artykuł omawiający wyzwania i trudności związane z OOP.
   - [Avoiding Common OOP Pitfalls](https://www.thoughtworks.com/insights/articles/avoiding-common-oop-pitfalls) - Przewodnik po unikaniu powszechnych pułapek w OOP na ThoughtWorks.

5. **Funkcyjne podejście do OOP**:
   - [Functional Programming vs. Object-Oriented Programming](https://www.freecodecamp.org/news/object-oriented-programming-vs-functional-programming-2fa4a7602390/) - Artykuł na FreeCodeCamp porównujący OOP i programowanie funkcyjne.
   - [Using Functional Programming Techniques in OOP](https://www.smashingmagazine.com/2019/05/functional-programming-oop-javascript/) - Przewodnik po technikach funkcyjnych w OOP na Smashing Magazine.

6. **OOP w Rust i Go**:
   - [Object-Oriented Programming in Rust](https://doc.rust-lang.org/book/ch17-00-oop.html) - Rozdział z oficjalnej dokumentacji Rust poświęcony OOP.
   - [Object-Oriented Programming in Go](https://golangbot.com/oops-part1/) - Przewodnik po OOP w Go na GolangBot.

7. **Struktury zamiast klas**:
   - [Structs in Rust](https://doc.rust-lang.org/book/ch05-00-structs.html) - Rozdział z oficjalnej dokumentacji Rust omawiający struktury.
   - [Structs in Go](https://tour.golang.org/moretypes/2) - Oficjalny przewodnik po strukturach w Go.

8. **Modularność w Rust**:
   - [Modules in Rust](https://doc.rust-lang.org/book/ch07-00-modules.html) - Rozdział z oficjalnej dokumentacji Rust poświęcony modułom.
   - [Building Modular Applications in Rust](https://blog.logrocket.com/building-modular-applications-rust/) - Artykuł na LogRocket o tworzeniu modularnych aplikacji w Rust.
