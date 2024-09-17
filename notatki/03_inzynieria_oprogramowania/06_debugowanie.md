## **Debugowanie**

*Debugowanie* to fundamentalny proces w tworzeniu oprogramowania, polegający na identyfikowaniu, analizowaniu i usuwaniu błędów (bugów) w kodzie źródłowym programu. Błędy te mogą prowadzić do nieprawidłowego działania aplikacji, awarii systemu lub nieoczekiwanych rezultatów. Debugowanie umożliwia programistom dokładne prześledzenie działania programu, co pozwala na zrozumienie, dlaczego program nie działa zgodnie z oczekiwaniami.

Proces ten jest niezbędny na każdym etapie cyklu życia oprogramowania, od fazy rozwoju po utrzymanie i aktualizacje. Dzięki debugowaniu programiści mogą:

- **Zidentyfikować błędy logiczne**, takie jak nieprawidłowe warunki w instrukcjach sterujących czy błędne algorytmy.
- **Usunąć błędy runtime'owe**, takie jak dzielenie przez zero, odwołania do niezainicjalizowanych zmiennych czy przekroczenia zakresu tablic.
- **Poprawić wydajność** identyfikując i optymalizując fragmenty kodu, które spowalniają działanie aplikacji.
- **Zrozumieć przepływ sterowania**, szczególnie w złożonych systemach z wieloma modułami i zależnościami.

### **Główne funkcje debuggera**

Debugger to narzędzie oferujące zaawansowane funkcje ułatwiające analizę i naprawę kodu. Oto szczegółowy opis jego głównych funkcji:

**Punkty przerwania (breakpoints):** 

- Punkty w kodzie, w których wykonanie programu zostanie zatrzymane.
- Pozwalają na zatrzymanie programu przed wykonaniem podejrzanego fragmentu kodu lub po nim, aby sprawdzić stan programu.
- Można ustawić warunek, który musi być spełniony, aby program się zatrzymał, np. `if (count == 10)`.

**Krokowanie (stepping):**

- *Step Into*, wchodzi w wywołania funkcji, umożliwiając analizę ich wnętrza.
- *Step Over*, wykonuje funkcję jako całość, nie wchodząc w jej szczegóły.
- *Step Out*, kontynuuje wykonanie do momentu wyjścia z bieżącej funkcji.

**Inspekcja stanu:** 

- Możliwość *sprawdzenia wartości zmiennych* lokalnych i globalnych.
- *Stos wywołań (call stack)* wyświetla sekwencję wywołań funkcji prowadzącą do bieżącego punktu, co pomaga zrozumieć przepływ sterowania.
- *Śledzenie wskaźników i referencji*, szczególnie ważne w językach takich jak C++ czy Java, gdzie zarządzanie pamięcią jest kluczowe.

**Modyfikacja stanu:**

- *Zmiana wartości zmiennych*, pozwala na eksperymentowanie z różnymi scenariuszami bez modyfikacji kodu źródłowego.
- Niektóre debugery umożliwiają *modyfikację kodu* w czasie rzeczywistym (tzw. hot swapping).

### **Zalety korzystania z debuggera**

Korzystanie z debuggera przynosi wiele korzyści, zarówno dla początkujących, jak i doświadczonych programistów:

- Możliwość zatrzymania programu w dokładnym miejscu wystąpienia błędu ułatwia jego identyfikację i naprawę.
- Zamiast dodawać tymczasowe instrukcje wyświetlające stan programu (np. `print`), debugger pozwala na bezpośredni podgląd i interakcję.
- Unika się ryzyka wprowadzenia nowych błędów podczas dodawania tymczasowych instrukcji do kodu.
- Szczególnie w przypadku pracy z kodem napisanym przez innych lub z zewnętrznymi bibliotekami.
- Debugger umożliwia wspólną analizę problemów podczas sesji pair programming lub code review.

### **Debugger w środowiskach programistycznych (IDE)**

Zintegrowane środowiska programistyczne (IDE) oferują zaawansowane narzędzia debugowania, które są nieodłączną częścią nowoczesnego procesu tworzenia oprogramowania. Oto niektóre z ich funkcji:

- Kliknięcie na marginesie edytora kodu pozwala szybko dodać lub usunąć breakpoint.
- Możliwość ustawienia breakpointów warunkowych bezpośrednio w interfejsie.
- Wartości zmiennych są wyświetlane podczas najechania kursorem na ich nazwy.
- Okna Watch i Variables umożliwiają śledzenie wybranych zmiennych i wyrażeń.
- Wizualizacja stosu wywołań, wątków czy nawet struktur danych (np. drzewa, listy).
- Interaktywne diagramy pomagające zrozumieć zależności między obiektami.
- Połączenie z systemami kontroli wersji, testowania czy profilowania.
- Możliwość debugowania aplikacji zdalnych, np. na serwerach czy urządzeniach mobilnych.
- Ustawienia dostosowane do konkretnego języka programowania czy frameworka.
- Makra i skrypty automatyzujące rutynowe czynności.

### **Debugger wbudowany w Pythonie - `pdb`**

`pdb` jest wbudowanym debuggerem Pythona, który, mimo swojej prostoty, oferuje ma wiele do zaoferowania:

- Nie wymaga instalacji dodatkowego oprogramowania.
- Dostępny na wszystkich platformach obsługujących Pythona.
- Może być używany zarówno w skryptach uruchamianych lokalnie, jak i na zdalnych serwerach przez SSH.
- Integruje się z innymi narzędziami i bibliotekami Pythona.

#### **Uruchomienie debuggera w kodzie**

Istnieje kilka sposobów na rozpoczęcie sesji debugowania z użyciem `pdb`:

**Bezpośrednie wywołanie z linii poleceń:**

```bash
python -m pdb script.py
```

**Wstawienie punktu przerwania w kodzie:**

Od Pythona 3.7 można użyć wbudowanej funkcji:

```python
breakpoint()  # Automatycznie uruchamia domyślny debugger
```

Lub tradycyjnie:

```python
import pdb
pdb.set_trace()
```

**Debugowanie wyjątków:**

Aby debugger uruchamiał się automatycznie przy nieobsłużonych wyjątkach:

```python
import sys
import pdb

def excepthook(type, value, traceback):
    pdb.post_mortem(traceback)

sys.excepthook = excepthook
```

### **Kontrolowanie wykonania programu w `pdb`**

Podczas sesji z `pdb` masz dostęp do szeregu poleceń:

**Nawigacja:**

- `n` / `next`: Przejście do następnej linii w bieżącej funkcji.
- `s` / `step`: Wejście do funkcji wywoływanej w bieżącej linii.
- `r` / `return`: Kontynuacja wykonania do momentu powrotu z bieżącej funkcji.
- `c` / `continue`: Kontynuacja wykonania do następnego breakpointa.

**Informacje o stanie:**

- `l` / `list`: Wyświetla kod źródłowy wokół bieżącej linii.
- `w` / `where`: Wyświetla stos wywołań (call stack).
- `p` / `print`: Wyświetla wartość wyrażenia.
- `pp` / `pprint`: Wyświetla wartość wyrażenia w sposób sformatowany.

**Zarządzanie breakpointami:**

- `b` / `break`: Ustawia breakpoint.
- `cl` / `clear`: Usuwa breakpoint.
- `disable` / `enable`: Dezaktywuje/aktywuje breakpoint.

**Pomoc i wyjście:**

- `h` / `help`: Wyświetla pomoc dla poleceń.
- `q` / `quit`: Kończy sesję debugowania.

### **Podgląd i edycja zmiennych w `pdb`**

`pdb` pozwala na interaktywną pracę z kodem:

**Wyświetlanie wartości:**

```python
p variable_name  # Wyświetla wartość zmiennej
```

**Zmiana wartości:**

```python
variable_name = new_value  # Ustawia nową wartość zmiennej
```

**Wykonywanie wyrażeń:**

Możesz wykonywać dowolne wyrażenia Pythona:

```python
p len(my_list)  # Wyświetla długość listy
```

**Wywoływanie funkcji:**

Uważaj jednak na skutki uboczne wywoływanych funkcji:

```python
p my_function()  # Wywołuje funkcję i wyświetla jej wynik
```

### **Ustawianie dodatkowych punktów zatrzymania**

Podczas debugowania możesz potrzebować zatrzymać program w nowych miejscach:

**Ustawianie breakpointów:**

```python
b 25  # Ustawia breakpoint na linii 25 bieżącego pliku
b my_module.py:10  # Ustawia breakpoint w pliku 'my_module.py' na linii 10
b my_function  # Ustawia breakpoint na początku funkcji 'my_function'
```

**Warunkowe breakpointy:**

```python
b 30, x > 5  # Zatrzyma program na linii 30, gdy 'x' jest większe od 5
```

**Wyświetlanie breakpointów:**

```python
b  # Wyświetla listę wszystkich breakpointów
```

**Usuwanie breakpointów:**

```python
cl  # Usuwa wszystkie breakpointy
cl 2  # Usuwa breakpoint numer 2
```


### Warunkowe zatrzymywanie

Warunkowe breakpointy są niezwykle przydatne w sytuacjach, gdy błąd występuje tylko przy określonych wartościach zmiennych lub w specyficznych warunkach.

**Przykład zastosowania:**

Jeśli pętla iteruje 1000 razy, ale błąd występuje tylko dla `i == 500`, ustawienie breakpointa warunkowego pozwala na zatrzymanie programu dokładnie w tym momencie:

```python
b loop.py:45, i == 500
```

**Debugowanie złożonych warunków:**

Możesz używać złożonych wyrażeń logicznych:

```python
b process_data, len(data) > 100 and error_flag
```

### Praktyczne wskazówki

- Jeśli używasz `pdb.set_trace()` w kodzie, warto dodawać komentarze, aby nie pozostawić ich przypadkowo w wersji produkcyjnej.
- Możesz tworzyć skrypty inicjalizacyjne dla `pdb`, aby automatyzować powtarzające się czynności.
- `pdb` można integrować z narzędziami takimi jak `pytest` czy `unittest`, aby debugować testy jednostkowe.
- Istnieją rozszerzone wersje `pdb`, takie jak `ipdb` czy `pudb`, oferujące dodatkowe funkcje i interfejsy.

