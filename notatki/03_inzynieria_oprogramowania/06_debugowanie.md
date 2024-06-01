## Debugowanie

Debugger to narzędzie używane przez programistów do testowania i usuwania błędów z kodu programu. Umożliwia ono wykonywanie programu krok po kroku, co pozwala na dokładne obserwowanie działania programu i jego stanu w różnych momentach wykonania. Debugger pomaga zidentyfikować i naprawić błędy w kodzie, takie jak nieprawidłowe działanie, błędy logiczne, czy problemy z zarządzaniem pamięcią.

### Główne funkcje debuggera

Debugger oferuje wiele funkcji, które ułatwiają identyfikację i rozwiązywanie problemów w kodzie:

- **Przerwanie wykonania programu (breakpoints)**: Umożliwia zatrzymanie programu w wybranych punktach, aby sprawdzić stan zmiennych, warunki wykonania itp.
  
- **Kroki**: Wykonanie programu krok po kroku, co pozwala na obserwację zmian w stanach zmiennych i logice działania programu.
  
- **Inspekcja stanu**: Oglądanie wartości zmiennych, stanu stosu wywołań i innych danych wewnętrznych programu.
  
- **Modyfikacja stanu**: Zmiana wartości zmiennych podczas wykonywania programu, aby zobaczyć, jak te zmiany wpłyną na działanie programu.

### Zalety korzystania z debuggera

- **Wgląd w działanie kodu**: Pozwala na zatrzymanie programu w dowolnym miejscu, obserwację wartości zmiennych i prześledzenie krok po kroku działania kodu.
- **Diagnostyka błędów**: Ułatwia identyfikację miejsc, w których pojawiają się błędy oraz ich przyczyn.
- **Nauka i analiza**: Pomaga nowym programistom w zrozumieniu działania nieznanego kodu poprzez interaktywną analizę.

### Debugger w środowiskach programistycznych (IDE)

Większość zintegrowanych środowisk programistycznych (IDE) zapewnia wbudowane narzędzia debugowania, które oferują zaawansowane funkcje, takie jak:

- **Ustawianie punktów zatrzymania (breakpoints)**: Pozwala na definiowanie miejsc, gdzie wykonanie kodu zostanie zatrzymane.
  
- **Podgląd wartości zmiennych w czasie rzeczywistym**: Umożliwia oglądanie wartości zmiennych w czasie, gdy program jest zatrzymany na punkcie przerwania.

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

#### Kontrolowanie wykonania programu

Po uruchomieniu `set_trace()`, działanie programu zostanie zatrzymane, a konsola przejdzie w tryb debugowania. Oto kilka podstawowych poleceń, które możesz użyć w trybie `pdb`:

- `n` (next): Przejście do następnej linii kodu bez wchodzenia do wnętrza funkcji.
- `s` (step): Wejście do wnętrza funkcji lub metody.
- `c` (continue): Kontynuowanie wykonania programu aż do następnego punktu przerwania lub zakończenia.
- `l` (list): Wyświetlenie fragmentu kodu wokół aktualnej linii wykonania.
- `q` (quit): Zakończenie debugowania i wyjście z programu.

##### Podgląd i edycja zmiennych

W trakcie sesji debugowania, możesz podglądać wartości zmiennych po prostu wpisując ich nazwy. Aby zmienić wartość zmiennej, użyj standardowej składni przypisania:

```python
count = 10  # Przypisanie nowej wartości do zmiennej 'count'
```

#### Ustawianie dodatkowych punktów zatrzymania

Możesz także ustawiać dodatkowe punkty zatrzymania (breakpoints) dynamicznie podczas sesji `pdb`, używając polecenia `break`:

```python
b 120  # Ustawienie breakpointa na linii 120
```

Jeśli chcesz usunąć breakpoint, możesz użyć polecenia `cl` z numerem breakpointa, który chcesz usunąć.

#### Warunkowe zatrzymywanie

`pdb` pozwala również na ustawianie warunkowych breakpointów, które aktywują się tylko, gdy spełniony jest określony warunek:

```python
b 150, count > 5  # Breakpoint na linii 150, który aktywuje się tylko gdy wartość 'count' jest większa niż 5
```

Dzięki tym możliwościom, `pdb` staje się nieocenionym narzędziem w trakcie debugowania bardziej złożonych błędów, zapewniając głęboki wgląd w działanie programu i pozwalając na interaktywne testowanie hipotez dotyczących przyczyn problemów.
