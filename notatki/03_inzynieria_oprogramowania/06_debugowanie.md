## Debugowanie

Debugger to narzędzie używane przez programistów do testowania i usuwania błędów z kodu programu. Umożliwia ono wykonywanie programu krok po kroku, co pozwala na dokładne obserwowanie działania programu i jego stanu w różnych momentach wykonania. Debugger pomaga zidentyfikować i naprawić błędy w kodzie, takie jak nieprawidłowe działanie, błędy logiczne, czy problemy z zarządzaniem pamięcią.

### Główne funkcje debuggera

Debugger oferuje wiele funkcji, które ułatwiają identyfikację i rozwiązywanie problemów w kodzie:

- Przerwanie wykonania programu, czyli **breakpoints**, pozwala zatrzymać program w wybranych punktach, aby sprawdzić stan zmiennych, warunki wykonania i inne aspekty.
  
- **Kroki** umożliwiają wykonanie programu krok po kroku, co pozwala na obserwację zmian w stanach zmiennych i logice działania programu.
  
- **Inspekcja stanu** pozwala na oglądanie wartości zmiennych, stanu stosu wywołań i innych danych wewnętrznych programu.
  
- **Modyfikacja stanu** umożliwia zmianę wartości zmiennych podczas wykonywania programu, aby zobaczyć, jak te zmiany wpłyną na działanie programu.

### Zalety korzystania z debuggera

- Pozwala na zatrzymanie programu w dowolnym miejscu, obserwację wartości zmiennych i prześledzenie krok po kroku działania kodu.
- Ułatwia identyfikację miejsc, w których pojawiają się błędy oraz ich przyczyn.
- Pomaga nowym programistom w zrozumieniu działania nieznanego kodu poprzez interaktywną analizę.

### Debugger w środowiskach programistycznych (IDE)

Większość zintegrowanych środowisk programistycznych (IDE) zapewnia wbudowane narzędzia debugowania, które oferują zaawansowane funkcje, takie jak:

- Ustawianie punktów zatrzymania (breakpoints), pozwala na definiowanie miejsc, gdzie wykonanie kodu zostanie zatrzymane.
  
- Podgląd wartości zmiennych w czasie rzeczywistym, umożliwia oglądanie wartości zmiennych w czasie, gdy program jest zatrzymany na punkcie przerwania.

Dzięki integracji z IDE, debugowanie staje się bardziej intuicyjne i efektywne, co znacząco przyspiesza proces rozwoju oprogramowania oraz identyfikację i rozwiązywanie błędów.

### Debugger wbudowany w Pythonie - `pdb`:

`pdb` (Python Debugger) to wbudowane w Pythonie narzędzie do debugowania, które działa w linii poleceń. Jest doskonałym wyborem dla programistów, którzy nie korzystają z IDE z zintegrowanym debuggerem lub tych, którzy szukają minimalistycznego i natywnego dla Pythona narzędzia do debugowania. `pdb` oferuje pełną kontrolę nad wykonaniem programu, umożliwiając precyzyjne śledzenie i analizę kodu.

#### Uruchomienie debuggera w kodzie

Aby zainicjować `pdb` w określonym miejscu w kodzie, wystarczy zaimportować moduł i umieścić wywołanie funkcji `set_trace()` w miejscu, w którym chcemy zatrzymać działanie programu:

```python
import pdb
pdb.set_trace()
```

Po dodaniu tej linii, każde wykonanie programu dojść do tego punktu zostanie zatrzymane, a kontrola zostanie przekazana do interaktywnego promptu `pdb`.

### Kontrolowanie wykonania programu

Po uruchomieniu komendy `set_trace()`, program zatrzyma swoje działanie, a konsola przejdzie w tryb debugowania. W tym trybie masz dostęp do różnych poleceń, które umożliwiają kontrolowanie przebiegu programu. Oto kilka podstawowych poleceń, które możesz użyć w trybie `pdb`:

- `n` (next): Przejście do następnej linii kodu bez zagłębiania się w funkcje. To polecenie pozwala kontynuować wykonanie programu, przechodząc do kolejnych instrukcji.
- `s` (step): Wejście do wnętrza funkcji lub metody. Użyj tego polecenia, aby przeanalizować szczegółowo, co dzieje się wewnątrz danej funkcji.
- `c` (continue): Kontynuowanie wykonania programu aż do napotkania kolejnego punktu przerwania (breakpoint) lub zakończenia programu. To polecenie pozwala pominąć szczegółowe śledzenie kodu aż do momentu, który Cię interesuje.
- `l` (list): Wyświetlenie fragmentu kodu wokół aktualnej linii wykonania. Dzięki temu możesz zobaczyć kontekst, w którym aktualnie znajduje się program.
- `q` (quit): Zakończenie sesji debugowania i wyjście z programu. Użyj tego polecenia, aby przerwać debugowanie i zakończyć działanie programu.

### Podgląd i edycja zmiennych

Podczas sesji debugowania możesz łatwo sprawdzać wartości zmiennych, wpisując ich nazwy bezpośrednio w konsoli debugera. Na przykład, wpisanie nazwy zmiennej `count` wyświetli jej bieżącą wartość. Jeśli chcesz zmienić wartość zmiennej, możesz to zrobić, używając standardowej składni przypisania:

```python
count = 10  # Przypisanie nowej wartości do zmiennej 'count'
```

### Ustawianie dodatkowych punktów zatrzymania

W trakcie sesji debugowania możesz dynamicznie ustawiać dodatkowe punkty zatrzymania (breakpoints), używając polecenia `break`:

```python
b 120  # Ustawienie breakpointa na linii 120
```

Aby usunąć istniejący punkt zatrzymania, użyj polecenia `cl` (clear) z numerem punktu, który chcesz usunąć:

```python
cl 1  # Usunięcie pierwszego breakpointa
```

### Warunkowe zatrzymywanie

`pdb` pozwala także na ustawianie warunkowych punktów zatrzymania, które aktywują się tylko wtedy, gdy spełniony jest określony warunek. Na przykład:

```python
b 150, count > 5  # Breakpoint na linii 150, który aktywuje się tylko gdy wartość 'count' jest większa niż 5
```

To polecenie ustawia punkt zatrzymania na linii 150, ale program zatrzyma się tam tylko wtedy, gdy wartość zmiennej `count` będzie większa niż 5. Dzięki temu możesz bardziej precyzyjnie kontrolować przebieg debugowania, koncentrując się na istotnych warunkach i sytuacjach w kodzie.

