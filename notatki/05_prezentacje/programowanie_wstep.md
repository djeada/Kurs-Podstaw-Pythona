# Programowanie

## Co to jest program?

Program to uporządkowana sekwencja instrukcji, które mają zostać wykonane przez komputer w celu wykonania określonego zadania. Zależnie od złożoności zadania, program może składać się z kilku linii kodu lub z tysięcy linii skomplikowanego kodu.

### Języki programowania

Program może być napisany w wielu językach programowania. Wybór języka zwykle zależy od specyfiki projektu, preferencji programisty i docelowej platformy wykonawczej. Przykłady popularnych języków programowania to:

- **C:** Język o niskim poziomie, często używany do programowania systemowego.
- **Python:** Wszechstronny język o wysokim poziomie, znany z łatwości pisania i czytelności kodu.
- **Java:** Język obiektowy, który jest niezależny od platformy, co oznacza, że napisane w nim programy mogą działać na różnych systemach operacyjnych.

### Proces działania programu

**Wejście** i **wyjście** z programu są podstawowymi elementami interakcji programu z otoczeniem. 

```
   Wejście
      ⬇
     Kod
      ⬇
   Sprzęt
      ⬇
   Wyjście
```

- **Wejście:** Informacje, które program otrzymuje. Może to być tekst wprowadzany przez użytkownika, dane z pliku czy sygnały z innych urządzeń.
  
- **Wyjście:** Rezultaty pracy programu, które są przekazywane do otoczenia. Mogą to być wyniki wyświetlane na ekranie, zapisywane do pliku czy przekazywane innym programom czy urządzeniom.

Wejście i wyjście są kluczowymi elementami interfejsu programu, a ich prawidłowa obsługa jest kluczowa dla funkcjonowania programu.

### Relacja między kodem a sprzętem

Chociaż kod programu jest odpowiedzialny za logiczne operacje i przetwarzanie danych, to jednak bez odpowiedniego sprzętu, na którym jest uruchamiany, nie mógłby działać. Sprzęt komputerowy, tak jak procesor czy pamięć, wykonuje fizyczne operacje, które reprezentuje kod. Dlatego ważne jest zrozumienie, że za skuteczne działanie programu odpowiadają zarówno dobrze napisany kod, jak i sprzęt, na którym jest uruchamiany.

## Kompilator i Interpreter

Kod napisany przez programistę, zrozumiały dla człowieka, musi być przetłumaczony na język zrozumiały dla maszyny, by mógł być efektywnie wykonywany przez komputer.

```
kod => interpretajca/komiplacja => inny kod
```

### Kompilator

Kompilator to narzędzie, które przetwarza kod źródłowy napisany w danym języku programowania do kodu binarnego, zrozumiałego dla komputera. Ten proces kompilacji zwykle odbywa się przed uruchomieniem programu. Wynikiem jest wykonywalny plik, który można uruchomić na komputerze.

### Interpreter

Z kolei interpreter to narzędzie, które analizuje i wykonuje kod programu "w locie", linia po linii, bez potrzeby tworzenia oddzielnego wykonywalnego pliku. Dzięki temu interpreter pozwala na bardziej interaktywny rozwój i testowanie programu.

#### C#

```
kod źródłowy C#.NET ---> kompilator C#.NET ---> CIL (.exe/.dll) ---> kompilator JIT (just-in-time) ---> kod maszynowy
```

1. Kod źródłowy C#.NET jest przetwarzany przez kompilator C#.NET do postaci CIL (Common Intermediate Language).
2. Następnie CIL jest przetwarzany przez kompilator JIT na kod maszynowy.
3. Kod maszynowy jest następnie wykonywany przez sprzęt komputerowy.

### Język C z GCC

```
kod źródłowy C ---> kompilator Gcc ---> kod wynikowy (na przykład plik wykonywalny lub biblioteka) -> linker -> program
```

1. Kod źródłowy języka C jest przetwarzany przez kompilator GCC do postaci kodu asemblera.
2. Kod asemblera jest następnie przetwarzany przez asembler do postaci kodu binarnego.
3. Kod binarny jest linkowany przez linker z odpowiednimi bibliotekami i plikami nagłówkowymi, tworząc program wykonywalny.
4. Program wykonywalny jest następnie uruchamiany przez sprzęt komputerowy.

### Python

```
kod źródłowy Python ---> interpreter Python ---> wynik działania kodu (np. wyświetlenie na ekranie lub zapisanie do pliku)
```

1. Kod źródłowy Python jest bezpośrednio interpretowany przez interpreter Python.
2. Interpreter analizuje i wykonuje kod w czasie rzeczywistym, odczytując go linia po linii.
3. Wynik działania kodu jest natychmiast zwracany użytkownikowi.

To tylko kilka przykładów ilustrujących różnice między kompilacją a interpretacją. W rzeczywistości istnieją też języki, które łączą oba podejścia, takie jak Java.

## Syntaktyka (reguły) i semantyka (znaczenie)

Podczas programowania nie tylko musimy zadbać o to, aby kod był poprawny składniowo, ale również o to, aby miał odpowiednie znaczenie i osiągał zamierzone cele.

### Syntaktyka

Syntaktyka dotyczy reguł składniowych konkretnego języka programowania. Błędy syntaktyczne zazwyczaj prowadzą do komunikatów o błędach podczas kompilacji lub interpretacji kodu.

Przykłady błędów syntaktycznych:

1. Brak nawiasu zamykającego funkcji:

```python
def funkcja(
    print("Hello World!")
```

2. Brak dwukropka na końcu wyrażenia warunkowego:

```python
x = 10

if x > 5
    print("x jest większe od 5")
```

### Semantyka

Semantyka koncentruje się na znaczeniu kodu. Błędy semantyczne występują, gdy kod jest poprawny składniowo, ale nie działa tak, jak zamierzono. W przeciwieństwie do błędów syntaktycznych, błędy semantyczne mogą nie prowadzić do komunikatów o błędach podczas kompilacji lub interpretacji, ale manifestują się nieoczekiwanym zachowaniem podczas działania programu.

Przykłady błędów semantycznych:

1. Użycie nieistniejącej zmiennej:

```python
x = 10
print(y) # NameError: name 'y' is not defined
```

2. Niepoprawne użycie operatora:

```python
a = "Hello"
b = "World"
c = a * b # TypeError: can't multiply sequence by non-int of type 'str'
```

Chociaż komunikaty o błędach mogą pomóc w zidentyfikowaniu i naprawieniu błędów syntaktycznych, błędy semantyczne często wymagają dokładnej analizy i testowania, aby zostały wykryte i naprawione.

## Typowanie

Typowanie odnosi się do mechanizmu określania rodzaju danych, które zmienne lub funkcje mogą przechowywać lub przyjmować. Mechanizmy typowania różnią się w zależności od języka programowania i mają duży wpływ na sposób projektowania, debugowania oraz wydajność programu.

### Typowanie statyczne

Typowanie statyczne to mechanizm, w którym typy zmiennych są określane w czasie kompilacji programu. Typy zmiennych muszą być zazwyczaj zadeklarowane przed ich użyciem i raz zadeklarowane, nie mogą być zmienione.

**Zalety:**
* Błędy typów są wykrywane wczesnie, co ułatwia debugowanie.
* Zazwyczaj prowadzi do bardziej wydajnego kodu binarnego.

**Przykłady języków o statycznym typowaniu:**
* Java
* C#
* C++
* Go
* Swift

### Typowanie dynamiczne

W systemach z dynamicznym typowaniem typ zmiennej jest określany w trakcie działania programu. Zmienna może przechowywać wartości różnych typów w trakcie jej istnienia w programie.

**Zalety:**
* Elastyczność - łatwiejsze do prototypowania.
* Mniej boilerplate'u - deklaracje typów nie są wymagane.

**Wady:**
* Błędy typów są wykrywane dopiero podczas wykonania, co może prowadzić do trudnych do znalezienia błędów.

**Przykłady języków o dynamicznym typowaniu:**
* Python
* Ruby
* JavaScript
* PHP

### Wskazówki dotyczące typów

Choć Python jest językiem o dynamicznym typowaniu, zostały wprowadzone "type hints" (wskazówki dotyczące typów) dla zmiennych, argumentów funkcji i wartości zwracanych. Pozwalają one programistom na określenie oczekiwanych typów, co ułatwia czytelność kodu i umożliwia korzystanie z narzędzi do statycznego sprawdzania typów, takich jak Mypy.

**Przykład użycia type hints:**

```python
def greet(name: str) -> str:
    return "Hello, " + name
```

Chociaż wskazówki dotyczące typów są pomocne, nie są one obowiązkowe i nie wpływają na działanie interpretera Pythona. Są one głównie przeznaczone dla programistów i narzędzi do analizy kodu, a nie dla samego interpretera.

Warto zaznaczyć, że wskazówki dotyczące typów w Pythonie są stosunkowo nowym dodatkiem (wprowadzonym w wersji 3.5) i są nadal rozwijane, z nowymi funkcjami i możliwościami dodawanymi w kolejnych wersjach języka.
