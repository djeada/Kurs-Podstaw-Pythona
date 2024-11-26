## Wyjątki

Wyjątki w programowaniu to mechanizm pozwalający na obsługę nieoczekiwanych sytuacji, które mogą wystąpić podczas działania programu. W Pythonie są one kluczowe dla tworzenia niezawodnych aplikacji, które potrafią radzić sobie z błędami w sposób elegancki i kontrolowany. Dzięki wyjątkowym możemy nie tylko wykrywać błędy, ale także reagować na nie w sposób, który nie zakłóci działania całego programu.

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

Bez mechanizmu obsługi wyjątków, programy byłyby narażone na niespodziewane zakończenie w momencie wystąpienia błędu. Dzięki wyjątkowym możemy przechwytywać te błędy i reagować na nie w kontrolowany sposób, na przykład informując użytkownika o problemie lub podejmując próby jego naprawy.

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
