## Wyjątki

Wyjątki w programowaniu to mechanizm pozwalający na obsługę nieoczekiwanych sytuacji, które mogą wystąpić podczas działania programu. W Pythonie są one kluczowe dla tworzenia niezawodnych aplikacji, które potrafią radzić sobie z błędami w sposób elegancki i kontrolowany. Dzięki wyjątkom możemy nie tylko wykrywać błędy, ale także reagować na nie w sposób, który nie zakłóci działania całego programu.

### Czym są wyjątki w Pythonie?

Wyjątki reprezentują błędy, które występują w trakcie wykonywania programu. Mogą być one spowodowane różnymi przyczynami, takimi jak dzielenie przez zero, dostęp do nieistniejącego elementu listy czy próba otwarcia pliku, który nie istnieje. Python posiada bogatą kolekcję wbudowanych wyjątków, które automatycznie informują nas o tego typu problemach.

Na przykład, gdy spróbujemy podzielić liczbę przez zero:

```python
print(10 / 0)
```

Uruchomienie tego kodu spowoduje wystąpienie wyjątku `ZeroDivisionError`. Python natychmiast poinformuje nas o błędzie, przerywając wykonanie programu i wyświetlając komunikat:

```
ZeroDivisionError: division by zero
```

### Dlaczego wyjątki są ważne?

Bez mechanizmu obsługi wyjątków, programy byłyby narażone na niespodziewane zakończenie w momencie wystąpienia błędu. Dzięki wyjątkom możemy przechwytywać te błędy i reagować na nie w kontrolowany sposób, na przykład informując użytkownika o problemie lub podejmując próby jego naprawy.

### Generowanie własnych wyjątków

Czasami chcemy sami zgłosić wyjątek, aby wskazać na problem w naszym kodzie. Możemy to zrobić za pomocą słowa kluczowego `raise`. Na przykład, jeśli chcemy upewnić się, że użytkownik podał nam liczbę dodatnią:

```python
def sprawdz_liczbe(liczba):
    if liczba <= 0:
        raise ValueError("Liczba musi być dodatnia")
    return liczba
```

Jeśli wywołamy tę funkcję z wartością ujemną:

```python
sprawdz_liczbe(-5)
```

Otrzymamy wyjątek `ValueError` z naszym własnym komunikatem:

```
ValueError: Liczba musi być dodatnia
```

### Obsługa wyjątków za pomocą bloków try i except

Aby zapobiec zatrzymaniu programu w momencie wystąpienia wyjątku, możemy użyć konstrukcji `try` i `except`. Pozwala ona na "przechwycenie" wyjątku i podjęcie odpowiednich działań.

Przykład:

```python
try:
    wynik = 10 / 0
except ZeroDivisionError:
    wynik = 0
    print("Nie można dzielić przez zero. Ustawiono wynik na 0.")
```

Po uruchomieniu otrzymamy komunikat:

```
Nie można dzielić przez zero. Ustawiono wynik na 0.
```

Program nie zostanie przerwany, a zmienna `wynik` będzie miała wartość 0.

### Obsługa wielu wyjątków

Możemy obsłużyć różne typy wyjątków w jednym bloku `try`. Jeśli chcemy przechwycić kilka konkretnych wyjątków, możemy je wymienić w nawiasach:

```python
try:
    # Kod, który może wywołać wyjątek
    liczba = int(input("Podaj liczbę: "))
    wynik = 10 / liczba
except (ValueError, ZeroDivisionError) as e:
    print(f"Wystąpił błąd: {e}")
else:
    print(f"Wynik dzielenia: {wynik}")
```

W tym przykładzie:

- Jeśli użytkownik poda wartość, która nie jest liczbą całkowitą, zostanie zgłoszony `ValueError`.
- Jeśli użytkownik poda zero, wystąpi `ZeroDivisionError`.

W obu przypadkach przechwycimy wyjątek i wyświetlimy odpowiedni komunikat.

### Bloki else i finally

- **Blok `else`** jest wykonywany, gdy w bloku `try` nie wystąpi żaden wyjątek.
- **Blok `finally`** jest wykonywany zawsze, niezależnie od tego, czy wyjątek wystąpił czy nie.

Przykład użycia:

```python
try:
    plik = open("dane.txt", "r")
    zawartosc = plik.read()
except FileNotFoundError:
    print("Plik nie został znaleziony.")
else:
    print("Zawartość pliku:")
    print(zawartosc)
finally:
    if 'plik' in locals():
        plik.close()
        print("Plik został zamknięty.")
```

W tym kodzie:

- Jeśli plik istnieje, zostanie odczytany i wyświetlony.
- Jeśli pliku nie ma, wyświetlimy komunikat o błędzie.
- Bez względu na wynik, upewniamy się, że plik zostanie zamknięty w bloku `finally`.

### Tworzenie własnych klas wyjątków

W Pythonie możemy definiować własne klasy wyjątków, dziedzicząc po klasie `Exception`. Pozwala to na tworzenie bardziej precyzyjnych i specyficznych dla naszej aplikacji komunikatów o błędach.

Przykład:

```python
class NiedozwolonaOperacjaError(Exception):
    def __init__(self, operacja):
        super().__init__(f"Operacja '{operacja}' jest niedozwolona.")
```

Możemy teraz użyć naszego wyjątku:

```python
def wykonaj_operacje(operacja):
    if operacja not in ['dodaj', 'usun']:
        raise NiedozwolonaOperacjaError(operacja)
    print(f"Wykonywanie operacji: {operacja}")

try:
    wykonaj_operacje('edytuj')
except NiedozwolonaOperacjaError as e:
    print(e)
```

Po uruchomieniu otrzymamy:

```
Operacja 'edytuj' jest niedozwolona.
```

### Wyjątki w kontroli przepływu programu

Wyjątki mogą być używane nie tylko do obsługi błędów, ale także jako mechanizm sterujący przepływem programu. Na przykład, podczas parsowania danych możemy użyć wyjątków do przerwania pętli, gdy napotkamy określoną sytuację.

Przykład:

```python
def znajdz_pierwsza_litere(napis):
    for znak in napis:
        if znak.isalpha():
            return znak
    raise ValueError("Brak litery w napisie")

try:
    litera = znajdz_pierwsza_litere("1234!")
    print(f"Pierwsza litera to: {litera}")
except ValueError as e:
    print(e)
```

W tym przypadku, jeśli napis nie zawiera żadnej litery, zgłosimy wyjątek `ValueError`.

### Dobre praktyki przy obsłudze wyjątków

- **Nie przechwytuj ogólnych wyjątków bez potrzeby.** Używanie pustego `except` lub `except Exception` może ukryć nieoczekiwane błędy i utrudnić debugowanie.
- **Używaj specyficznych wyjątków.** Przechwytuj konkretne typy wyjątków, aby lepiej kontrolować reakcję programu na różne sytuacje.
- **Zadbaj o czytelność kodu.** Wyjątki powinny ułatwiać zrozumienie przepływu programu, a nie go komplikować.
- **Unikaj nadużywania wyjątków do sterowania logiką programu.** Choć mogą być pomocne, nadużywanie ich może prowadzić do mniej czytelnego kodu.

### Łańcuchowanie wyjątków (exception chaining)

Gdy obsługujemy wyjątek i chcemy zgłosić inny (wyżej poziomowy), możemy zachować oryginalny wyjątek w łańcuchu za pomocą `raise ... from ...`:

```python
class BladBazyDanych(Exception):
    pass

def pobierz_uzytkownika(user_id):
    try:
        # symulacja błędu połączenia
        raise ConnectionError("Serwer bazy danych niedostępny")
    except ConnectionError as e:
        raise BladBazyDanych(f"Nie można pobrać użytkownika {user_id}") from e

try:
    pobierz_uzytkownika(42)
except BladBazyDanych as e:
    print(f"Błąd: {e}")
    print(f"Przyczyna: {e.__cause__}")
```

Wynik:

```
Błąd: Nie można pobrać użytkownika 42
Przyczyna: Serwer bazy danych niedostępny
```

Aby celowo ukryć oryginalny wyjątek, używamy `raise ... from None`:

```python
try:
    int("abc")
except ValueError:
    raise RuntimeError("Błąd parsowania") from None
```

### Menedżer kontekstu i wyjątki (`with`)

Instrukcja `with` gwarantuje wykonanie kodu sprzątającego (np. zamknięcia pliku) nawet przy wystąpieniu wyjątku:

```python
# Zamiast jawnego try/finally:
try:
    plik = open("dane.txt")
    zawartosc = plik.read()
finally:
    plik.close()

# Zalecane — z użyciem with:
with open("dane.txt") as plik:
    zawartosc = plik.read()
# plik zostaje zamknięty automatycznie, nawet jeśli wystąpi wyjątek
```

Można otworzyć wiele kontekstów naraz:

```python
with open("wejscie.txt") as wejscie, open("wyjscie.txt", "w") as wyjscie:
    for linia in wejscie:
        wyjscie.write(linia.upper())
```

### Hierarchia wbudowanych wyjątków

Python posiada bogatą hierarchię wbudowanych klas wyjątków. Znajomość tej hierarchii pozwala przechwytywać całe grupy wyjątków:

```
BaseException
 ├── SystemExit
 ├── KeyboardInterrupt
 ├── GeneratorExit
 └── Exception
      ├── StopIteration
      ├── ArithmeticError
      │    ├── ZeroDivisionError
      │    ├── OverflowError
      │    └── FloatingPointError
      ├── LookupError
      │    ├── IndexError
      │    └── KeyError
      ├── TypeError
      ├── ValueError
      │    └── UnicodeError
      ├── OSError (IOError, EnvironmentError)
      │    ├── FileNotFoundError
      │    ├── PermissionError
      │    └── TimeoutError
      ├── RuntimeError
      │    └── RecursionError
      ├── NameError
      │    └── UnboundLocalError
      ├── AttributeError
      ├── ImportError
      │    └── ModuleNotFoundError
      └── NotImplementedError
```

Przykład przechwytywania grupy:

```python
try:
    lista = [1, 2, 3]
    print(lista[10])
except LookupError as e:
    print(f"Błąd wyszukiwania: {type(e).__name__}: {e}")
# Przechwytuje zarówno IndexError jak i KeyError
```

### Moduł `warnings` — ostrzeżenia

Oprócz wyjątków, Python udostępnia moduł `warnings` do sygnalizowania potencjalnych problemów, które nie przerywają działania programu:

```python
import warnings

def przestarzala_funkcja():
    warnings.warn(
        "Funkcja jest przestarzała. Użyj nowej_funkcji() zamiast niej.",
        DeprecationWarning,
        stacklevel=2
    )
    return 42

wynik = przestarzala_funkcja()
# UserWarning: Funkcja jest przestarzała...
```

Zarządzanie ostrzeżeniami:

```python
import warnings

# Ignorowanie konkretnego ostrzeżenia
warnings.filterwarnings("ignore", category=DeprecationWarning)

# Zamiana ostrzeżenia na błąd
warnings.filterwarnings("error", category=UserWarning)

# Pokazanie wszystkich ostrzeżeń (resetowanie filtrów)
warnings.resetwarnings()
```

### Sprawdzanie kontekstu wyjątku

Obiekt wyjątku zawiera dodatkowe informacje:

```python
try:
    1 / 0
except ZeroDivisionError as e:
    print(type(e))       # <class 'ZeroDivisionError'>
    print(e.args)        # ('division by zero',)
    print(str(e))        # division by zero
    import traceback
    traceback.print_exc()  # pełny traceback
```

Aby ponownie zgłosić przechwycony wyjątek bez modyfikacji:

```python
try:
    ryzykowna_operacja()
except ValueError:
    print("Logowanie błędu...")
    raise   # ponownie zgłasza ValueError bez zmian
```

### Dobre praktyki obsługi wyjątków

1. **Łap konkretne wyjątki** — unikaj pustego `except:` lub `except Exception:`, które mogą ukryć nieoczekiwane błędy.

```python
# ❌ Źle: łapie zbyt wiele
try:
    wynik = operacja()
except:
    pass

# ✅ Dobrze: łapie konkretny wyjątek
try:
    wynik = int(tekst)
except ValueError:
    wynik = 0
```

2. **Używaj `else` do kodu zależnego od sukcesu** — kod w `else` wykona się tylko jeśli `try` zakończyło się bez wyjątku.

```python
try:
    plik = open("dane.txt")
except FileNotFoundError:
    print("Plik nie istnieje")
else:
    dane = plik.read()
    plik.close()
```

3. **Używaj `finally` do sprzątania** — lub lepiej: menedżerów kontekstu (`with`).

```python
# Zamiast try/finally:
with open("dane.txt") as f:
    dane = f.read()
# Plik zostanie zamknięty automatycznie
```

4. **Twórz własne wyjątki** gdy wbudowane nie opisują wystarczająco dobrze błędu w kontekście Twojej aplikacji.

```python
class BladAutoryzacji(Exception):
    """Użytkownik nie ma uprawnień do wykonania operacji."""
    def __init__(self, uzytkownik, operacja):
        self.uzytkownik = uzytkownik
        self.operacja = operacja
        super().__init__(f"Użytkownik '{uzytkownik}' nie może wykonać: {operacja}")
```

5. **Loguj wyjątki** zamiast je ignorować — ciche błędy utrudniają debugowanie.

### Hierarchia wyjątków wbudowanych (wybrane)

```
BaseException
├── SystemExit
├── KeyboardInterrupt
├── GeneratorExit
└── Exception
    ├── ArithmeticError
    │   ├── ZeroDivisionError
    │   └── OverflowError
    ├── LookupError
    │   ├── IndexError
    │   └── KeyError
    ├── OSError
    │   ├── FileNotFoundError
    │   ├── PermissionError
    │   └── ConnectionError
    ├── ValueError
    ├── TypeError
    ├── AttributeError
    ├── ImportError
    ├── RuntimeError
    │   └── RecursionError
    └── StopIteration
```
