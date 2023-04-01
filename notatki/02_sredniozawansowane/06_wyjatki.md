## Wyjątki
Wyjątkami nazywamy sytuacje, które uniemożliwiają poprawne wykonanie danego bloku kodu. Tym samym terminem określany jest również mechanizm języka Python pozwalający na radzenie sobie z tymi sytuacjami.

W Pythonie istnieje szereg wyjątków zdefiniowanych w standardzie, takich jak <code>ZeroDivisionError</code>, który występuje, gdy próbujemy dzielić liczbę przez 0.

```python
print(5 / 0)
```

Możemy również sami wywołać wyjątek, np.: 

```python
raise ValueError("Podano nieprawidlowa wartosc")
```
  
Uwaga, nic nie chroni nas przed wywołaniem wyjątku w nieodpowiednim miejscu. Naszym zadaniem jest dbanie o to, aby wywołanie wyjątku było wykonane w odpowiedniej sytuacji.

### Obsługa wyjątków

Obsługa wyjątków polega na zapobieżeniu zatrzymaniu programu w przypadku wystąpienia nieoczekiwanej sytuacji. Jest to szczególnie ważne w programach, które działają "w tle" i nie są interaktywne.

Aby obsłużyć wyjątek, używamy bloku `try/except`. W bloku try umieszczamy kod, który może spowodować wystąpienie wyjątku. W przypadku wystąpienia wyjątku, wykonywany jest kod znajdujący się w bloku except.

Oto przykład obsługi wyjątku `ZeroDivisionError`:

```python
try:
    print(5 / 0)
except ZeroDivisionError:
    print("Nie można dzielić przez zero")
```

Wyjątek informuje nas o błędzie i nie powinniśmy go ignorować. Z tego powodu nigdy nie umieszczaj `pass` w bloku `except`.

Możemy również obsłużyć wyjątek, który jest podklasą innego wyjątku.

```python
try:
    print(int("abc"))
except ValueError:
    print("Nie można zamienić tekstu na liczbę")
```

Istnieje opcja obsługi kilku różnych wyjątków w jednym bloku `try/except`. W takim wypadku, musimy umieścić osobny blok `except` dla każdego z nich.

```python
try:
    print(5 / 0)
    print(int("abc"))
except ZeroDivisionError:
    print("Nie można dzielić przez zero")
except ValueError:
    print("Nie można zamienić tekstu na liczbę")
```

Jeśli chcemy obsłużyć wiele różnych wyjątków w jednym bloku, możemy umieścić ich nazwy po przecinku. Możemy też użyć wyjątku ogólnego, np. `Exception`, ale nie jest to zalecane, ponieważ nie wiemy, jaki konkretny wyjątek wystąpił.

```python
try:
    # kod, ktory moze wywolac wyjatek
except (ValueError, TypeError):
    # kod, ktory zostanie wykonany w przypadku wystapienia wyjatku ValueError lub TypeError
```

Możemy również zapisać wyjątek do zmiennej i użyć go w bloku `except`.

```python
try:
    print(5 / 0)
except ZeroDivisionError as e:
    print(f"Wystąpił wyjątek: {e}")
```

Blok `else` jest opcjonalny i wykonywany jest, jeśli nie wystąpił żaden wyjątek w bloku `try`. Możemy go wykorzystać do wykonania kodu, który ma być wykonany po prawidłowym wykonaniu bloku try. W przeciwieństwie do bloku except, blok else nie przyjmuje argumentów.

Blok `finally` jest również opcjonalny, ale zawsze wykonywany bez względu na to, czy wystąpił wyjątek czy nie. Może być używany do wykonania kodu, który ma być wykonany zawsze, niezależnie od tego, czy wystąpił wyjątek czy nie. Może być przydatny, gdy chcemy zamknąć plik lub połączenie z bazą danych po zakończeniu pracy z nim.

### Własny wyjątek

Możemy również tworzyć własne wyjątki. Nasz wyjątek musi dziedziczyć po klasie <code>Exception</code> lub jednej z jej podklas.

```python
class MojaWyjatkowaSytuacja(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)
```

Możemy zgłosić nasz wyjątek za pomocą słowa kluczowego <code>raise</code>.

```python
raise MojaWyjatkowaSytuacja("To jest moj wyjatek")
```

Załóżmy, że chcemy sprawdzić czy liczba jest parzysta, gdyż tylko taka liczba może zostać użyta w dalszej części programu.

```python
def upewnij_sie_ze_liczba_jest_parzysta(liczba):
    if liczba % 2 != 0:
        raise ValueError("Podano nieparzysta liczbe")
    
    return liczba
```

Możemy użyć tej funkcji w taki sposób:

```python
try:
    sprawdz_parzystosc(5)
except ValueError as v:
    print(v)
else:
    print("Liczba jest parzysta")
```else:
        return True

Wyświetlona zostanie informacja o błędzie "Podano nieparzysta liczbe".

### Wyjątki jako mechanizm przepływu sterowania

Innym zastosowaniem wyjątków jest użycie ich jako mechanizm przepływu sterowania. W poniższym przykładzie używamy wyjątku do sprawdzenia, czy napis reprezentuje liczbę całkowitą:

```python
def czy_liczba(napis):
    try:
        int(napis)
    except ValueError:
        return False
    return True
```
