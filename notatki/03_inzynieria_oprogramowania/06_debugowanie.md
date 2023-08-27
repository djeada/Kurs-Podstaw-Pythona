## Debugowanie w Pythonie

Debuger to nieocenione narzędzie w rękach programisty. Służy do analizy i diagnozy kodu, pomagając identyfikować i naprawiać błędy, a także zrozumieć, jak działają poszczególne fragmenty programu.

### Zalety korzystania z debugera
- **Wgląd w działanie kodu**: Pozwala na zatrzymanie programu w dowolnym miejscu, obserwację wartości zmiennych i prześledzenie krok po kroku działania kodu.
- **Diagnostyka błędów**: Ułatwia identyfikację miejsc, w których pojawiają się błędy oraz ich przyczyn.
- **Nauka i analiza**: Pomaga nowym programistom w zrozumieniu działania nieznanego kodu poprzez interaktywną analizę.

### Wady korzystania z debugera
- **Czasochłonność**: Mimo że debuger pomaga szybko zidentyfikować błędy, proces ten może być czasochłonny, zwłaszcza w dużych projektach.
- **Potrzeba doświadczenia**: Skomplikowane błędy lub kod mogą wymagać doświadczenia i wiedzy, aby skutecznie korzystać z debugera.

### Debugger w środowiskach programistycznych (IDE)
Większość IDE zapewnia wbudowane narzędzia debugowania, które oferują zaawansowane funkcje, takie jak ustawianie punktów zatrzymania (breakpoints) czy podgląd wartości zmiennych w czasie rzeczywistym. Dzięki integracji z IDE, debugowanie staje się bardziej intuicyjne i efektywne.

### Debugger wbudowany w Pythona - `pdb`:

`pdb` (Python Debugger) to wbudowane w Pythonie narzędzie do debugowania, które działa w linii poleceń. Jest doskonałym wyborem dla programistów, którzy nie korzystają z IDE z zintegrowanym debuggerem lub tych, którzy szukają minimalistycznego i natywnego dla Pythona narzędzia do debugowania.

#### Uruchomienie debuggera w kodzie
Aby zainicjować `pdb` w określonym miejscu w kodzie, wystarczy zaimportować moduł i umieścić wywołanie funkcji `set_trace()` w miejscu, w którym chcemy zatrzymać działanie programu:

```python
import pdb
pdb.set_trace()
```

#### Kontrolowanie wykonania programu
Po uruchomieniu `set_trace()`, działanie programu zostanie zatrzymane, a konsola przejdzie w tryb debugowania. Oto kilka podstawowych poleceń, które możesz użyć:

- `n` lub `next`: Przejście do następnej linii kodu.
- `s` lub `step`: Wejście do funkcji lub metody.
- `c` lub `continue`: Kontynuowanie wykonania programu aż do następnego punktu przerwania.
- `l` lub `list`: Wyświetlenie aktualnego fragmentu kodu.
- `q` lub `quit`: Zakończenie debugowania i zatrzymanie programu.
    
##### Podgląd i edycja zmiennych
Możesz podglądać wartość zmiennej po prostu wpisując jej nazwę w trybie debugowania. Aby przypisać nową wartość do zmiennej, użyj standardowej składni przypisania w Pythonie.

#### Ustawianie dodatkowych punktów zatrzymania
W trakcie debugowania możesz dynamicznie dodawać nowe punkty zatrzymania przy użyciu polecenia `break` (lub `b` w skrócie), podając numer linii kodu, w której chcesz zatrzymać wykonanie.

Dzięki pdb, nawet w skomplikowanych programach, masz możliwość zrozumienia, co dokładnie dzieje się w Twoim kodzie, krok po kroku, co jest nieocenione podczas diagnozowania i naprawiania błędów.
