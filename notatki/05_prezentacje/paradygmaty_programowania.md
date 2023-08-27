## Paradygmaty w programowaniu

Paradygmat w programowaniu to nie tylko sposób myślenia o tworzeniu programów, ale także zestaw konceptów i technik, które kierują projektowaniem i strukturyzacją oprogramowania. Te filozofie wpływają na to, jak programiści definiują problemy oraz jak podejmują decyzje o sposobie ich rozwiązania. Chociaż istnieją dwa główne paradygmaty, imperatywny i deklaratywny, rzeczywistość jest bardziej złożona i wiele języków pozwala korzystać z wielu paradygmatów jednocześnie.

### Paradygmat imperatywny

Paradygmat imperatywny koncentruje się na "jak to zrobić". Opisuje sekwencje instrukcji, które modyfikują stan programu. Działanie programu oparte jest na sekwencji operacji zmieniających jego stan.

- **Proceduralny**: Opiera się na organizacji kodu za pomocą funkcji i procedur, które wykonują określone zadania.
- **Obiektowy**: Skupia się na jednostkach zwanych obiektami, które są instancjami klas. Klasy definiują zachowanie (metody) i stan (atrybuty) obiektów.

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

- Funkcyjny: Kod jest zbiorem funkcji, które są wzorowane na wyrażeniach matematycznych. Nie mają one efektów ubocznych i nie modyfikują stanu zewnętrznego.
- Logiczny: Skupia się na określaniu relacji i zależności. Programy są zbiorem faktów i reguł, a wykonanie programu polega na poszukiwaniu dowodów czy spełnienia określonych warunków.

```python
# Definicja funkcji czystej do obliczania nowej pozycji
def move(position, speed, time):
    return position + speed * time

# Rekursywna funkcja, która oblicza pozycje dla listy czasu
def get_positions_recursive(position, speed, time_list):
    if not time_list:
        return []
    return [move(position, speed, time_list[0])] + get_positions_recursive(move(position, speed, time_list[0]), speed, time_list[1:])

# Funkcja do generowania listy ścieżek na podstawie pozycji początkowej, prędkości i listy czasu
def get_path(position, speed, time_list):
    return get_positions_recursive(position, speed, time_list)

# Wykorzystanie powyższych funkcji
print(get_path(0, 10, [1, 0.5]))  # [10, 15]
```

### Współczesne języki programowania

Współczesne języki programowania często łączą różne paradygmaty i oferują elastyczność, pozwalając programistom na mieszanie składni z różnych paradygmatów w jednym programie. Dzięki temu programiści mają swobodę wyboru i mogą stosować najbardziej odpowiednie narzędzia dla konkretnego problemu, co z kolei przekłada się na większą efektywność rozwoju i optymalizację kodu.

Python to język, który z powodzeniem łączy cechy programowania obiektowego oraz funkcyjnego. Oto kilka charakterystycznych elementów dla obu tych paradygmatów w Pythonie:

**Elementy charakterystyczne dla programowania obiektowego**:

* **Klasy**: Służą do definiowania nowych typów danych i zawierają zarówno atrybuty (reprezentujące stan obiektu) jak i metody (operujące na tym stanie).
* **Dziedziczenie**: Umożliwia tworzenie klas pochodnych, które dziedziczą atrybuty i metody po klasie bazowej, pozwalając jednocześnie na ich rozszerzanie lub modyfikację.
* **Enkapsulacja**: Ukrywa wewnętrzne szczegóły klasy, dzięki czemu można je modyfikować bez wpływu na kod korzystający z tej klasy.

**Elementy charakterystyczne dla programowania funkcyjnego**:

* **First-class functions**: W Pythonie funkcje są obiektami pierwszej klasy, co oznacza, że można je przekazywać jako argumenty, zwracać z innych funkcji czy przypisywać do zmiennych.
* **Higher-order functions**: Są to funkcje, które przyjmują inne funkcje jako argumenty lub zwracają je. Przykładem może być funkcja `map` lub `filter`.
* **Funkcje lambda**: Umożliwiają szybkie tworzenie anonimowych funkcji na potrzeby jednorazowego użycia.

W rzeczywistości Python, jak wiele współczesnych języków programowania, jest językiem hybrydowym. Oznacza to, że nie ogranicza się do jednego paradygmatu, ale pozwala na ich mieszanie w zależności od potrzeb i preferencji programisty. Taka elastyczność czyni Pythona niezwykle wszechstronnym i adaptowalnym do różnorodnych zastosowań, od analizy danych, przez rozwój aplikacji webowych, aż po skomplikowane systemy wbudowane.

### Ewolucja OOP (Programowania Obiektowego)

Programowanie obiektowe (OOP) stało się dominującym paradygmatem w ciągu ostatnich dekad, ale jak każdy paradygmat, rozwijało się i dostosowywało do nowych wyzwań i koncepcji.

* **Enkapsulacja, Abstrakcja, i Polimorfizm**: Enkapsulacja odnosi się do praktyki ograniczania dostępu do pewnych składników obiektu i łączenia danych z zachowaniami. Abstrakcja pozwala na reprezentację złożonych systemów w bardziej ogólnej formie, ukrywając szczegóły. Polimorfizm daje możliwość definiowania wielu form dla funkcji lub metod, dzięki czemu można je używać w różnorodny sposób.

* **Klasy i Złożoność**: Chociaż klasy są podstawowym budulcem OOP, mogą prowadzić do złożonych hierarchii i zależności. Ważne jest, aby zachować prostotę, unikając zbytniego powiązania i zagnieżdżenia.

* **Kolekcje w OOP**: Tablice haszujące i wektory są często używane w OOP, ale nie każda kolekcja musi być "obiektowo zorientowana". Ważne jest, aby wybierać odpowiednie struktury danych dla konkretnych zastosowań.

* **Wyzwania OOP**: Nadmierne poleganie na dziedziczeniu i głębokich hierarchiach klas może prowadzić do trudności w utrzymaniu kodu. Szczególnie w dużych systemach, gdzie zmiana w jednym miejscu może wpłynąć na wiele innych.

* **Funkcyjne podejście do OOP**: Techniki programowania funkcyjnego, takie jak closure czy funkcje wyższego rzędu, mogą być użyte do realizacji niektórych koncepcji obiektowych, takich jak enkapsulacja czy polimorfizm, oferując jednocześnie większą elastyczność i prostotę.

* **OOP w Rust i Go**: Zarówno Rust, jak i Go oferują podejście do enkapsulacji oparte na modułach, gdzie metody i pola są ograniczone do konkretnego zakresu. Chociaż różni się to od klasycznego OOP, nadal jest zgodne z jego głównymi założeniami.

* **Struktury zamiast klas**: W językach takich jak Rust i Go, zamiast klas mamy do czynienia ze strukturami. Struktury te służą do reprezentowania danych i, w przeciwieństwie do klas, nie mają wbudowanej koncepcji dziedziczenia.

* **Modularność w Rust**: W praktyce, większość modułów w standardowej bibliotece Rust koncentruje się na jednym lub kilku ściśle powiązanych typach, co sprzyja przejrzystości, izolacji odpowiedzialności i ogólnej jakości kodu.

Ostatecznie, OOP jest narzędziem - tak jak każdy paradygmat programowania. Kluczową kwestią jest umiejętność wyboru właściwych narzędzi i technik w zależności od konkretnego problemu.


* https://cs.lmu.edu/~ray/notes/paradigms/
* https://homes.cs.aau.dk/~normark/prog3-03/html/notes/paradigms-book.html
