# Programowanie

## Co to jest program?

Program to precyzyjnie sformułowany zestaw instrukcji lub poleceń, które komputer wykonuje w celu rozwiązania konkretnego problemu lub realizacji określonego zadania. Instrukcje te są napisane w języku programowania, który jest zrozumiały dla programistów i może być przetworzony na język zrozumiały dla maszyny. 

Programowanie jest procesem tworzenia tych instrukcji i wymaga od programisty umiejętności analitycznego myślenia, rozwiązywania problemów oraz znajomości składni i semantyki wybranego języka programowania. Kluczowym elementem jest zrozumienie algorytmów, czyli krok po kroku procedur prowadzących do rozwiązania problemu.

Zależnie od złożoności zadania, program może składać się z kilku linii kodu, realizujących proste operacje, lub z milionów linii skomplikowanego kodu, tworzących zaawansowane systemy operacyjne, aplikacje biznesowe czy gry komputerowe. Programy mogą być tworzone do różnych celów, takich jak automatyzacja zadań, przetwarzanie danych, komunikacja czy sterowanie urządzeniami.

### Języki programowania

Języki programowania to formalne języki zaprojektowane do komunikowania instrukcji do maszyny, szczególnie komputera. Składają się z zestawu reguł składniowych i semantycznych, które określają, jak pisać programy. Wybór języka programowania zależy od wielu czynników, takich jak:

- W projektach związanych z analizą danych i statystyką, **język R** jest powszechnie używany ze względu na swoje zaawansowane narzędzia analityczne.
- Do tworzenia aplikacji na platformy iOS, **Swift** jest preferowanym wyborem, ze względu na swoją optymalizację pod kątem systemu Apple.
- **Preferencje programisty** często wpływają na wybór języka, zwłaszcza jeśli programista ma doświadczenie z określoną technologią lub czuje się komfortowo z danym środowiskiem programistycznym.
- Przy wyborze języka istotne jest również, jaka jest **docelowa platforma**, ponieważ niektóre języki są stworzone z myślą o konkretnych systemach operacyjnych lub platformach. Na przykład, **C#** jest często wykorzystywany w tworzeniu aplikacji na platformę Windows, dzięki swojej integracji z .NET.

Przykłady popularnych języków programowania:

- **C** to język o niskim poziomie abstrakcji, który daje dużą kontrolę nad pamięcią, co jest kluczowe w przypadku tworzenia systemów operacyjnych i sterowników.
- **Python** wyróżnia się swoją wszechstronnością oraz czytelną składnią, co czyni go popularnym wyborem w analizie danych, uczeniu maszynowym, a także w automatyzacji.
- **Java** dzięki maszynie wirtualnej JVM jest niezależna od platformy, co sprawia, że jest szeroko stosowana w aplikacjach korporacyjnych oraz mobilnych, szczególnie na urządzeniach z systemem Android.

Każdy język programowania ma swoje unikalne cechy, zalety i obszary zastosowań. Wybór odpowiedniego języka jest kluczowy dla efektywnego i wydajnego tworzenia oprogramowania.

### Proces działania programu

**Wejście** i **wyjście** z programu są podstawowymi elementami interakcji programu z otoczeniem. Programy przetwarzają dane wejściowe, wykonują na nich określone operacje i generują dane wyjściowe.

```
   Wejście
      ⬇
     Kod
      ⬇
   Sprzęt
      ⬇
   Wyjście
```

- Program otrzymuje różne informacje jako **wejście**, które mogą pochodzić z wielu źródeł.
- Dane mogą być wprowadzane przez **użytkownika**, na przykład poprzez tekst wpisany z klawiatury, kliknięcia myszy, czy wybory dokonywane w interfejsie użytkownika.
- Program może odczytywać **dane z plików**, takich jak pliki tekstowe, bazy danych, lub inne zewnętrzne źródła danych.
- Innym rodzajem wejścia są **sygnały z urządzeń**, takie jak dane z czujników, sygnały sieciowe, czy informacje przesyłane z innych programów.
- **Kod** programu to zestaw instrukcji, które programista pisze, aby określić, jak przetwarzać dane wejściowe.
- W kodzie mogą znajdować się **operacje arytmetyczne i logiczne**, takie jak obliczenia matematyczne czy porównywanie wartości.
- Również **struktury kontrolne**, takie jak pętle czy instrukcje warunkowe, które decydują o przepływie programu, mają kluczowe znaczenie.
- Ważnym elementem są także **funkcje i procedury**, czyli zorganizowane bloki kodu, które realizują konkretne zadania w programie.
- Komponenty **sprzętu** są nieodzowną częścią procesu wykonywania kodu. Procesor (CPU) jest odpowiedzialny za przetwarzanie instrukcji, **pamięć RAM** przechowuje zarówno dane, jak i kod, a urządzenia wejścia/wyjścia umożliwiają interakcję z otoczeniem.
- Wynik działania programu jest nazywany **wyjściem**, które może przybierać różne formy.
- Często są to **wyniki wyświetlane na ekranie**, w formie tekstu, grafiki lub interfejsów użytkownika.
- Program może również zapisywać **dane do plików**, takich jak raporty, logi czy wyniki przeprowadzonych obliczeń.
- Inną formą wyjścia są **sygnały wysyłane do innych urządzeń lub programów**, na przykład w celu komunikacji sieciowej lub sterowania urządzeniami.

Wejście i wyjście są kluczowymi elementami interfejsu programu, a ich prawidłowa obsługa jest niezbędna dla poprawnego funkcjonowania programu. Program musi być zaprojektowany tak, aby prawidłowo interpretować dane wejściowe i generować oczekiwane wyjście, nawet w przypadku nieprzewidzianych lub błędnych danych wejściowych.

### Relacja między kodem a sprzętem

Kod programu jest zbiorem instrukcji, które muszą zostać przetworzone i wykonane przez sprzęt komputerowy. Ta relacja jest kluczowa dla zrozumienia, jak programy działają na poziomie maszyny.

- **Kod źródłowy** to napisany przez programistę tekst w języku programowania, który jest zrozumiały dla człowieka i zawiera instrukcje opisujące działanie programu.
- Proces **kompilacji lub interpretacji** przekształca ten kod źródłowy na formę zrozumiałą dla komputera, czyli na kod maszynowy lub kod pośredni, zależnie od języka programowania.
- **Kod maszynowy** to sekwencja instrukcji w postaci binarnej, którą procesor może bezpośrednio zrozumieć i wykonać, dzięki czemu komputer wykonuje określone operacje.
- **Procesor (CPU)** odgrywa kluczową rolę w wykonywaniu tych instrukcji, przetwarzając dane i sterując innymi komponentami systemu, co jest niezbędne dla funkcjonowania programów.
- **Pamięć i urządzenia peryferyjne** przechowują zarówno dane, jak i kod programu, a także umożliwiają interakcję z otoczeniem, np. za pomocą urządzeń wejścia i wyjścia.

Relacja między kodem a sprzętem opiera się na kilku istotnych aspektach:

- **Warstwa abstrakcji** w językach wysokiego poziomu pozwala programistom skupić się na pisaniu logiki programu, bez konieczności zagłębiania się w szczegóły techniczne związane z działaniem sprzętu.
- **Optymalizacja wydajności** staje się możliwa, gdy programista rozumie, jak kod źródłowy jest przetwarzany przez sprzęt, co pozwala na tworzenie bardziej efektywnych rozwiązań.
- **Bezpieczeństwo i niezawodność** kodu mogą być poprawione, gdy programista zna interakcje między kodem a sprzętem, co umożliwia unikanie potencjalnych błędów, takich jak przepełnienia bufora czy wycieki pamięci.

Dlatego ważne jest, aby programiści mieli świadomość, jak ich kod zostanie przetworzony i wykonany przez sprzęt, co pozwala na tworzenie bardziej efektywnych i niezawodnych programów.

## Kompilator i Interpreter

Kod napisany przez programistę jest zrozumiały dla człowieka, ale musi zostać przetłumaczony na język zrozumiały dla maszyny. Istnieją dwa główne sposoby tego tłumaczenia: kompilacja i interpretacja.

```
kod źródłowy => kompilacja/interpretacja => kod maszynowy
```

### Kompilator

Kompilator to program, który przekształca kod źródłowy napisany w języku programowania wysokiego poziomu na kod maszynowy lub kod pośredni. Proces ten odbywa się przed uruchomieniem programu i składa się z kilku etapów:

- Proces **analizy leksykalnej** polega na podziale kodu źródłowego na tokeny, czyli podstawowe elementy języka, takie jak słowa kluczowe, identyfikatory czy operatory.
- **Analiza składniowa** ma na celu sprawdzenie, czy kod jest zgodny z regułami gramatyki danego języka programowania oraz tworzy strukturę zwaną drzewem składniowym, która odzwierciedla hierarchię operacji.
- W **analizie semantycznej** program sprawdza poprawność znaczeniową kodu, na przykład czy operacje wykonywane są na odpowiednich typach danych i czy zmienne są poprawnie używane.
- **Optymalizacja kodu** polega na poprawieniu jego wydajności poprzez eliminację zbędnych instrukcji lub przekształcenie fragmentów kodu w bardziej efektywne operacje, co ma na celu przyspieszenie działania programu.
- **Generowanie kodu maszynowego** to ostatni etap, w którym kod źródłowy zostaje przekształcony w instrukcje zrozumiałe dla procesora, co umożliwia ich bezpośrednie wykonanie przez sprzęt.

**Zalety kompilacji:**

- Skompilowany kod jest zazwyczaj szybszy w wykonaniu.
- Błędy syntaktyczne i semantyczne są wykrywane przed uruchomieniem.

**Wady kompilacji:**

- Długi czas kompilacji może być uciążliwy w dużych projektach.
- Trudniejsze testowanie fragmentów kodu w locie.

### Interpreter

Interpreter to program, który analizuje i wykonuje kod źródłowy linia po linii w czasie rzeczywistym. Nie tworzy on oddzielnego pliku wykonywalnego.

**Zalety interpretacji:**

- Możliwość natychmiastowego testowania kodu.
- Kod może być łatwiej uruchamiany na różnych platformach.

**Wady interpretacji:**

- Wolniejsze wykonanie ze względu na narzut interpretacji.
- Błędy mogą pojawić się dopiero podczas działania programu.

#### C#

```
kod źródłowy C#.NET ---> kompilator C#.NET ---> CIL (.exe/.dll) ---> kompilator JIT (just-in-time) ---> kod maszynowy
```

1. Kod źródłowy jest kompilowany do Common Intermediate Language (CIL), niezależnego od platformy.
2. Podczas uruchomienia, kompilator JIT tłumaczy CIL na kod maszynowy specyficzny dla danej platformy.
3. Kod maszynowy jest wykonywany przez sprzęt.

Ta hybryda kompilacji i interpretacji pozwala na optymalizację wydajności i przenośność kodu.

#### Język C z GCC

```
kod źródłowy C ---> kompilator GCC ---> kod wynikowy (plik wykonywalny) -> linker -> program
```

1. Kod źródłowy jest przetwarzany przez GCC do kodu maszynowego.
2. Łączenie z bibliotekami tworzy plik wykonywalny.
3. Program jest uruchamiany bezpośrednio przez system operacyjny.

Ten proces tworzy wydajny kod, ale zależny od platformy.

#### Python

```
kod źródłowy Python ---> interpreter Python ---> wynik działania kodu
```

1. Kod źródłowy jest przetwarzany przez interpreter.
2. Interpreter kompiluje kod do bytecode (kod bajtowy).
3. Bytecode jest wykonywany przez maszynę wirtualną Pythona.

Python łączy interpretację z kompilacją do bytecode, co przyspiesza działanie programu w porównaniu z czystą interpretacją.

### Podsumowanie

Różne języki programowania wykorzystują różne metody tłumaczenia kodu źródłowego na kod wykonywalny. Wybór między kompilacją a interpretacją wpływa na wydajność, przenośność i interaktywność języka. Niektóre języki, takie jak Java czy C#, używają podejścia hybrydowego, łącząc zalety obu metod.

## Syntaktyka (reguły) i semantyka (znaczenie)

Podczas programowania ważne jest zrozumienie zarówno składni (syntaktyki), jak i znaczenia (semantyki) kodu. Błędy w jednym lub drugim mogą prowadzić do nieprawidłowego działania programu lub uniemożliwić jego uruchomienie.

### Syntaktyka

Syntaktyka dotyczy reguł składniowych języka programowania. Obejmuje ona zasady dotyczące struktury kodu, takie jak użycie nawiasów, średników, poprawnej kolejności instrukcji. Błędy syntaktyczne są zazwyczaj wykrywane przez kompilator lub interpreter i uniemożliwiają uruchomienie programu.

**Przykłady błędów syntaktycznych:**

I. **Brak nawiasu zamykającego:**

```python
def funkcja():
    print("Hello World!"
```

Błąd: "SyntaxError: unexpected EOF while parsing".

II. **Brak dwukropka po instrukcji warunkowej:**

```python
if x > 5
    print("x jest większe od 5")
```

Błąd: "SyntaxError: invalid syntax".

III. **Nieprawidłowa identacja (wcięcie) w Pythonie:**

```python
def funkcja():
print("Hello World!")
```

Błąd: "IndentationError: expected an indented block".

Poprawna składnia jest niezbędna, aby kompilator lub interpreter mógł poprawnie zrozumieć i przetworzyć kod.

### Semantyka

Semantyka odnosi się do znaczenia instrukcji w kodzie. Dotyczy tego, co kod faktycznie robi podczas wykonania. Błędy semantyczne występują, gdy kod jest poprawny składniowo, ale nie działa zgodnie z zamierzeniami programisty.

**Przykłady błędów semantycznych:**

I. **Użycie nieistniejącej zmiennej:**

```python
x = 10
print(y)
```

Błąd: "NameError: name 'y' is not defined".

II. **Błędna logika warunku:**

```python
x = 10
if x < 5:
    print("x jest większe od 5")
```

Kod działa, ale nie wyświetli komunikatu, mimo że x jest większe od 5.

III. **Nieprawidłowe operacje na typach danych:**

```python
a = "5"
b = 10
c = a + b
```

Błąd: "TypeError: can only concatenate str (not 'int') to str".

Błędy semantyczne są często trudniejsze do wykrycia, ponieważ nie zawsze prowadzą do natychmiastowych błędów. Mogą powodować nieprawidłowe wyniki lub zachowanie programu.

### Różnica między błędami syntaktycznymi a semantycznymi

- **Błędy syntaktyczne** są wykrywane podczas kompilacji lub interpretacji. Uniemożliwiają uruchomienie programu. Są zazwyczaj łatwiejsze do zlokalizowania i naprawienia dzięki komunikatom o błędach.
- **Błędy semantyczne** pojawiają się podczas wykonywania programu. Program może się uruchomić, ale działa niepoprawnie. Wymagają dokładnej analizy kodu i logiki programu.

### Znaczenie testowania i debugowania

Aby zapewnić poprawne działanie programu, programiści muszą:

- Tworzyć testy jednostkowe i integracyjne, które sprawdzą poprawność działania poszczególnych części programu.
- Używać narzędzi do debugowania w celu śledzenia wykonania programu i lokalizowania błędów.
- Regularnie przeglądać i analizować kod w celu wykrycia potencjalnych problemów.

Poprawne zrozumienie syntaktyki i semantyki jest kluczowe dla tworzenia niezawodnego i efektywnego oprogramowania.

## Typowanie

Typowanie odnosi się do systemu typów używanego w języku programowania, który definiuje rodzaje danych, jakie mogą być przechowywane i manipulowane w programie. System typów wpływa na sposób, w jaki programiści piszą kod i jak kompilator lub interpreter przetwarza ten kod.

### Typowanie statyczne

W językach z typowaniem statycznym typy zmiennych są określane w czasie kompilacji. Programista musi zadeklarować typ zmiennej przed jej użyciem, a raz zadeklarowany typ nie może być zmieniony.

**Zalety:**

- Błędy typów są wykrywane podczas kompilacji.
- Kompilator może optymalizować kod na podstawie znanych typów.
- Zapobiega niezamierzonym konwersjom typów.

**Przykłady języków o statycznym typowaniu:**

- **Java:** Wymaga deklaracji typów dla wszystkich zmiennych.
- **C#:** Podobnie jak Java, z możliwością użycia `var` dla inferencji typów.
- **C++:** Umożliwia silne typowanie z możliwością przeciążania operatorów.
- **Go:** Wymaga deklaracji typów, ale wspiera inferencję typów.
- **Swift:** Silne, statyczne typowanie z inferencją typów.

### Typowanie dynamiczne

W językach z typowaniem dynamicznym typy zmiennych są określane w czasie wykonania. Zmienna może przechowywać wartości różnych typów w trakcie działania programu.

**Zalety:**

- Pozwala na większą swobodę w pisaniu kodu.
- Mniej formalności przy deklaracji zmiennych.

**Wady:**

- Błędy typów mogą pojawić się podczas działania programu.
- Dodatkowy narzut na sprawdzanie typów w czasie wykonania.

**Przykłady języków o dynamicznym typowaniu:**

- **Python:** Typy są przypisywane w czasie wykonania.
- **Ruby:** Wszystko jest obiektem, typy są dynamiczne.
- **JavaScript:** Zmienne mogą zmieniać typy w trakcie działania programu.
- **PHP:** Typowanie dynamiczne z możliwością deklaracji typów od wersji 7.

### Wskazówki dotyczące typów

Chociaż Python jest językiem o dynamicznym typowaniu, w wersji 3.5 wprowadzono "type hints" (wskazówki dotyczące typów), które pozwalają na określenie oczekiwanych typów zmiennych, argumentów funkcji i wartości zwracanych.

**Przykład użycia type hints:**

```python
def greet(name: str) -> str:
    return "Hello, " + name
```

**Zalety użycia type hints:**

- Ułatwiają zrozumienie, jakie typy danych są oczekiwane.
- Narzędzia takie jak mypy mogą sprawdzać typy statycznie.
- Służą jako dokumentacja dla innych programistów.

**Ograniczenia:**

- Interpreter Pythona nie wymusza zgodności typów, chyba że użyje się zewnętrznych narzędzi.
