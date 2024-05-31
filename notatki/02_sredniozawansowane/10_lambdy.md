## Funkcje Lambda

Lambda to anonimowa funkcja, która może być używana w wielu językach programowania. Funkcje te są nazywane "anonimowymi", ponieważ nie mają przypisanej nazwy. Lambdy są używane, gdy potrzebujemy krótkiej funkcji, którą można zdefiniować w jednym wierszu.

## Dlaczego warto używać lambd?

Funkcje lambda mają kilka zalet:

1. **Zwięzłość**: Pozwalają na definiowanie krótkich funkcji w jednym wierszu, co może uprościć kod.
2. **Anonimowość**: Nie wymagają nazwy, co jest przydatne, gdy funkcja jest używana tylko raz i nie ma potrzeby jej ponownego wywołania.
3. **Funkcyjność**: Umożliwiają programowanie funkcyjne, gdzie funkcje są traktowane jako obiekty pierwszej klasy i mogą być przekazywane jako argumenty, zwracane z innych funkcji, itp.

### Składnia funkcji lambda

Składnia funkcji lambda zależy od języka programowania, ale zazwyczaj jest zbliżona do poniższego schematu:

```
lambda argumenty: wyrażenie
```

- `lambda`: Słowo kluczowe do stworzenia funkcji anonimowej.
- `argumenty`: Lista argumentów wejściowych, które mogą być dowolną liczbą argumentów oddzielonych przecinkami.
- `wyrażenie`: Wyrażenie, które jest zwracane przez funkcję lambda.

### Przykład

Oto podstawowy przykład wyrażenia lambda w porównaniu do standardowej funkcji:

```python
def zwykla_funkcja(liczba: int) -> int:
    return liczba**2

przyklad_lambdy = lambda liczba: liczba**2

wartosc = 2

print(zwykla_funkcja(wartosc)) # 4
print(przyklad_lambdy(wartosc)) # 4
print((lambda liczba: liczba**2)(wartosc)) # 4
```

### Ograniczenia wyrażeń lambda

Chociaż wyrażenia lambda są wygodne, mają pewne ograniczenia w porównaniu do standardowych funkcji:

- Można zdefiniować tylko jedno wyrażenie.
- Nie jest możliwe używanie instrukcji, takich jak `if`, `for` czy `while`.
- Nie można definiować ani przypisywać zmiennych (chociaż można używać `setattr()` dla obiektów).
- Są one mniej czytelne w przypadku skomplikowanych operacji.

### Zastosowania

Wyrażenia lambda są szczególnie przydatne w miejscach, gdzie funkcja wymaga jednego wyrażenia jako argumentu. Typowym zastosowaniem jest sortowanie listy według określonego kryterium:

```python
lista = [('def', 100), ('ghi', 200), ('abc', 300)]
print(sorted(lista, key=lambda x: x[0])) # [('abc', 300), ('def', 100), ('ghi', 200)]
print(sorted(lista, key=lambda x: x[1])) # [('def', 100), ('ghi', 200), ('abc', 300)]
```

W powyższym przykładzie, wyrażenie lambda zostało użyte do zdefiniowania funkcji klucza dla metody `sorted()`, co pozwala na elastyczne sortowanie listy bez konieczności tworzenia dodatkowych funkcji.
