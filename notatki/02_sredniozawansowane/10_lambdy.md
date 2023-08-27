## Wyrażenia Lambda w Pythonie

W Pythonie wyrażenia lambda to krótkie, anonimowe funkcje, które można zdefiniować w jednym wierszu przy użyciu słowa kluczowego `lambda`. Są one często stosowane w miejscach, gdzie krótka, prostota funkcja jest wymagana na chwilę, bez potrzeby definiowania pełnoprawnej funkcji.

### Podstawy

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
