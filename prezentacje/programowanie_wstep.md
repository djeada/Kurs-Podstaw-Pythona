## Programowanie

Program to sekwencja instrukcji i kodu, która ma być wykonana przez komputer. Program może być napisany w różnych językach programowania, takich jak C, Python, Java itp. Język programowania jest narzędziem do komunikowania się z komputerem i określania sposobu wykonania określonych zadań.

    kod => sprzet => wyjscie
             ||
           wejscie
           
Wejście i wyjście z programu odnoszą się do sposobu, w jaki program komunikuje się z resztą systemu. Wejście to informacje, które program otrzymuje od innych elementów systemu, natomiast wyjście to informacje, które program wysyła do innych elementów systemu. Wejście i wyjście mogą mieć różne formy, takie jak dane zapisane w pliku, dane przesłane przez sieć, dane przechowywane w pamięci komputera lub dane wprowadzane przez użytkownika za pomocą klawiatury lub innego urządzenia wejścia.

Wejście i wyjście są ściśle związane z kodem programu oraz sprzętem. Kod programu określa sposób, w jaki program przetwarza wejście i generuje wyjście, natomiast sprzęt jest odpowiedzialny za fizyczne przekazywanie danych między programem a resztą systemu. 

## Kompilator i interpreter

Kod zrozumiały dla człowieka musimy przetłumaczyć na kod zrozumiały dla komputera.

    kod => interpretajca/komiplacja => inny kod

Kompilator to narzędzie, które przekształca kod napisany w języku programowania na kod binarny, który jest zrozumiały dla komputera. Kompilator zazwyczaj pracuje w momencie tworzenia programu i wytwarza wykonywalny plik, który może być uruchomiony przez komputer.

Interpreter to narzędzie, które interpretuje kod programu i wykonuje go w locie, bez tworzenia wykonywalnego pliku. Dzięki temu interpreter jest w stanie natychmiast reagować na zmiany w kodzie i umożliwia interaktywne testowanie programu.

Oto kilka przykładów:

C#:

    kod źródłowy C#.NET ---> kompilator C#.NET ---> CIL (.exe/.dll) ---> kompilator JIT (just-in-time) ---> kod maszynowy

1. Kod źródłowy C#.NET jest przetwarzany przez kompilator C#.NET do postaci CIL (Common Intermediate Language).
1. Następnie CIL jest przetwarzany przez kompilator JIT na kod maszynowy.
1. Kod maszynowy jest wykonywany przez sprzęt.

Przy kompilacji w języku C z Gcc przebieg procesu wygląda następująco:

    kod źródłowy C ---> kompilator Gcc ---> kod wynikowy (na przykład plik wykonywalny lub biblioteka) -> linker -> program

1. Kod źródłowy C jest przetwarzany przez kompilator GCC do postaci kodu asemblera.
1. Kod asemblera jest przetwarzany przez asembler do postaci kodu binarnego.
1. Kod binarny jest linkowany przez linker z odpowiednimi bibliotekami i plikami nagłówkowymi. Linker tworzy plik wykonywalny lub bibliotekę dynamiczną.
1. Plik wykonywalny lub biblioteka dynamiczna są uruchamiane przez sprzęt.

Natomiast proces interpretacji w Pythonie przebiega następująco:

    kod źródłowy Python ---> interpreter Python ---> wynik działania kodu (np. wyświetlenie na ekranie lub zapisanie do pliku)

1. Kod źródłowy Python jest interpretowany przez interpreter Python.
1. Interpreter wykonuje kod w czasie rzeczywistym, odczytując go wiersz po wierszu.
1. Wynik jest zwracany do użytkownika.

## Syntaktyka (reguły) i semantyka (znaczenie)

Syntaktyka to zestaw reguł dotyczących poprawności składniowej kodu programu. Jeśli kod jest niepoprawny pod względem składni, kompilator lub interpreter zwróci błąd.

Semantyka to znaczenie kodu programu, tj. to, co kod ma robić. Jeśli kod jest poprawny składniowo, ale nie działa tak, jak powinien, może to być spowodowane błędami semantycznymi.

Przykłady błędów syntaktycznych to:

1. brak nawiasu zamykającego funkcji:

        def funkcja(
          print("Hello World!")

2. brak dwukropka na końcu wyrażenia warunkowego:

        x = 10

        if x > 5
          print("x jest większe od 5")

Przykłady błędów semantycznych to:

1. użycie nieistniejącej zmiennej:

        x = 10
        print(y) # NameError: name 'y' is not defined


2. niepoprawne użycie operatora:

        a = "Hello"
        b = "World"
        c = a * b # TypeError: can't multiply sequence by non-int of type 'str'

## Typowanie

Typowanie to określenie rodzaju danych, które mogą być przechowywane w zmiennych lub przekazywane do funkcji w programie. Może być ono statyczne lub dynamiczne.

### Typowanie statyczne

Typowanie statyczne oznacza, że typy zmiennych są nadawane w czasie kompilacji programu. Oznacza to, że jeśli chcemy przypisać daną wartość do zmiennej, musimy określić jej typ przed uruchomieniem programu. W przypadku typowania statycznego, błędy typów są zazwyczaj wykrywane już w czasie kompilacji, co ułatwia debugowanie i zapobiega nieoczekiwanym błędom podczas działania programu.

### Typowanie dynamiczne

Typowanie dynamiczne oznacza, że typy zmiennych są przypisywane do wartości przechowywanych w zmiennych w trakcie działania programu. Oznacza to, że możemy przypisać dowolną wartość do zmiennej, niezależnie od jej typu, i nie będziemy musieli określać jej typu przed uruchomieniem programu. W przypadku typowania dynamicznego, błędy typów są zazwyczaj wykrywane dopiero podczas działania programu, co może utrudniać debugowanie i prowadzić do nieoczekiwanych błędów podczas działania programu.

### Type hints 

Type hints są dodatkiem do kodu, który pozwala na podanie typów zmiennych i argumentów funkcji. Umożliwiają one narzędziom statycznego typowania (takim jak Mypy) oraz innym narzędziom programistycznym na zgłaszanie błędów i ostrzeżeń w kodzie w czasie kompilacji. Type hints nie są obowiązkowe i są ignorowane przez interpreter, dlatego Python pozostaje językiem o dynamicznym typowaniu.

Przykład użycia type hints:

    def greet(name: str) -> str:
      return "Hello, " + name

W tym przykładzie podano, że argument `name` jest typu `str` oraz że funkcja również zwraca wartość typu `str`. Narzędzia takie jak Mypy mogą wykryć, kiedy do funkcji `greet()` zostanie przekazana wartość innego typu niż `str` i wyświetlić odopowiedni komunikat o błędzie.

Type hints są szczególnie przydatne w dużych projektach, gdzie kod jest współdzielony pomiędzy wielu programistów i gdzie istnieje ryzyko, że mogą pojawić się błędy spowodowane niezgodnościami typów. Type hints są również przydatne w dokumentowaniu kodu, w szczególności gdy korzysta się z automatycznych generatorów dokumentacji.
