## Wyjątki

W programowaniu, wyjątki są sytuacjami, które występują podczas wykonywania programu, uniemożliwiając jego poprawne działanie. W języku Python, mechanizm wyjątków jest kluczowym elementem obsługi błędów i nieoczekiwanych sytuacji.

### Podstawy wyjątków

Python posiada bogatą listę wbudowanych wyjątków, które można wykorzystać w swoich programach. Przykładem jest `ZeroDivisionError`, który występuje podczas próby dzielenia przez zero:

```python
print(5 / 0)  # Spowoduje wystąpienie wyjątku ZeroDivisionError
```

Możemy też samodzielnie wywołać wyjątek przy użyciu słowa kluczowego `raise`:

```python
raise ValueError("Podano nieprawidłową wartość")
```

Chociaż jesteśmy w stanie wywołać dowolny wyjątek, powinniśmy zawsze dążyć do używania ich w odpowiednich kontekstach, tak aby komunikat błędu był jak najbardziej precyzyjny.

### Obsługa wyjątków

Aby zapobiec zatrzymaniu działania programu w wyniku wyjątku, można skorzystać z bloku `try/except`. Kod, który może spowodować błąd, umieszcza się wewnątrz bloku try, a obsługę błędu realizuje się w bloku except.

Przykład obsługi wyjątku `ZeroDivisionError`:

```python
try:
    print(5 / 0)
except ZeroDivisionError:
    print("Nie można dzielić przez zero")
```

Dla jasności i przejrzystości kodu, warto unikać pustych bloków except (z użyciem `pass`), gdyż może to skutkować ukryciem błędów.

Możemy obsłużyć wiele różnych wyjątków w jednym bloku `try`:

```python
try:
    print(5 / 0)
    print(int("abc"))
except ZeroDivisionError:
    print("Nie można dzielić przez zero")
except ValueError:
    print("Nie można zamienić tekstu na liczbę")
```

Aby obsłużyć kilka wyjątków w jednym bloku `except`, można umieścić ich nazwy po przecinku:

```python
try:
    # kod, który może wywołać wyjątek
except (ValueError, TypeError):
    # kod obsługi dla wyjątków ValueError lub TypeError
```

Za pomocą klauzuli `as` możemy przypisać wyjątek do zmiennej, co pozwala na dostęp do szczegółów błędu:

```python
try:
    print(5 / 0)
except ZeroDivisionError as e:
    print(f"Wystąpił wyjątek: {e}")
```

Oprócz bloków try i except, Python oferuje bloki `else` i `finally`:

- Blok `else`: Wykonywany, gdy nie wystąpi żaden wyjątek w bloku try.
- Blok `finally`: Zawsze jest wykonywany, niezależnie od tego, czy wystąpił wyjątek czy nie. Często używany do sprzątania, takiego jak zamknięcie plików czy połączeń z bazą danych.

```python
try:
    # kod, który może wywołać wyjątek
except ValueError:
    # obsługa wyjątku ValueError
else:
    # kod do wykonania, jeśli nie wystąpił żaden wyjątek
finally:
    # kod do wykonania zawsze, niezależnie od wystąpienia wyjątku
```

Zrozumienie i właściwe wykorzystanie wyjątków jest kluczem do tworzenia niezawodnych i odpornych na błędy aplikacji w Pythonie.

### Własne wyjątki w Pythonie

Tworzenie własnych wyjątków jest przydatne, gdy chcemy obsłużyć specyficzne dla naszej aplikacji sytuacje błędów. Aby stworzyć własny wyjątek, należy stworzyć nową klasę, która dziedziczy po klasie `Exception` lub innej istniejącej klasie wyjątku.

```python
class MojaWyjatkowaSytuacja(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)
```

Aby zgłosić nasz własny wyjątek, korzystamy ze słowa kluczowego `raise`:

```python
raise MojaWyjatkowaSytuacja("To jest mój wyjątek")
```

Przyjmijmy założenie, że w pewnej części naszej aplikacji wymagamy, aby podawane liczby były parzyste. Możemy stworzyć funkcję sprawdzającą parzystość liczby i zgłaszającą błąd przy użyciu wyjątku:

```python
def upewnij_sie_ze_liczba_jest_parzysta(liczba):
    if liczba % 2 != 0:
        raise ValueError("Podano nieparzystą liczbę")
    
    return liczba
```

Aby użyć tej funkcji i odpowiednio obsłużyć ewentualny wyjątek, możemy skorzystać z bloku `try/except`:

```python
try:
    upewnij_sie_ze_liczba_jest_parzysta(5)
except ValueError as v:
    print(v)
else:
    print("Liczba jest parzysta")
```

Jeśli użyjemy powyższego kodu z liczbą 5, zostanie wyświetlony komunikat: "Podano nieparzystą liczbę". Jeśli natomiast użyjemy liczby parzystej, np. 6, zostanie wyświetlony komunikat: "Liczba jest parzysta".

### Wyjątki jako mechanizm przepływu sterowania

Chociaż wyjątki zostały pierwotnie zaprojektowane jako sposób na radzenie sobie z nieoczekiwanymi błędami, w pewnych sytuacjach mogą być używane jako mechanizm przepływu sterowania. Innymi słowy, mogą być stosowane do sterowania logiką programu w miejscach, gdzie tradycyjne metody, takie jak instrukcje warunkowe, mogą być mniej wyraźne lub mniej efektywne.

Jednym z takich zastosowań jest walidacja danych, gdzie wyjątki mogą uprościć kod i uczynić go bardziej czytelnym. Poniżej przedstawiony jest przykład funkcji, która sprawdza, czy dany napis reprezentuje liczbę całkowitą, wykorzystując wyjątki do przepływu sterowania:

```python
def czy_liczba(napis):
    try:
        int(napis)
    except ValueError:
        return False
    return True
```

Gdy podamy do tej funkcji napis, który jest poprawną liczbą, funkcja `int(napis)` zostanie poprawnie wykonana i funkcja zwróci `True`. Jeśli napis nie jest poprawną liczbą, zostanie zgłoszony wyjątek `ValueError`, który zostanie przechwycony i funkcja zwróci `False`.

Powyższy przykład ilustruje, jak wyjątki mogą być używane do kontrolowania przepływu sterowania w programie. W tym przypadku unikamy złożonej logiki warunkowej, sprawdzając poprawność napisu za pomocą prostego bloku `try-except`.

Warto zauważyć, że nadużywanie wyjątków jako mechanizmu przepływu sterowania może prowadzić do mniej czytelnego i trudniejszego do utrzymania kodu. Dlatego należy używać tej techniki z rozwagą i w sytuacjach, gdzie naprawdę przynosi korzyści w postaci uproszczenia logiki programu.
