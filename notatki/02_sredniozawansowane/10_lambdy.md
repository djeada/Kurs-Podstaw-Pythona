
## Lambdy

Wyrażenia lambda to funkcje składające się z jednego wiersza instrukcji, definiowane za pomocą słowa kluczowego lambda. Lambdy nie używają słowa kluczowego return, ponieważ zawsze zwracają wynik wykonania tworzącego je wiersza instrukcji.

```python
def zwykla_funkcja(liczba: int) -> int:
  return liczba**2

przyklad_lambdy = lambda liczba: liczba**2

wartosc = 2

print(zwykla_funkcja(wartosc)) # 4
print(przyklad_lambdy(wartosc)) # 4
print((lambda liczba: liczba**2)(wartosc)) # 4
```

W porównaniu do pełnoprawnych funkcji definiowanych za pomocą słowa kluczowego def, lambdy są ograniczone:

- Możemy użyć jedynie jednego wiersza instrukcji.
- Możliwe jest sprawdzenie warunku, ale nie można zagnieżdżać warunków.
- Brak możliwości tworzenia zmiennych oraz przypisywania wartości do istniejących zmiennych (dla obiektów możemy użyć <code>setattr()</code>).
- Brak pętli.
  
Lambdy są również przydatne, gdy chcemy dostosować się do wymagań danej funkcji, która przyjmuje jako argument funkcję. W takim przypadku nie musimy tworzyć pełnoprawnej funkcji i jej przekazywać, lecz możemy bezpośrednio podstawić lambda.

Na przykład, jeśli chcemy posortować listę obiektów według pewnego atrybutu, możemy skorzystać z metody `sorted()`, która przyjmuje argument `key` - funkcję, która ma zwracać wartość atrybutu według którego ma być sortowana lista. W takiej sytuacji lambda pozwala nam zdefiniować tę funkcję w miejscy wywołania `sorted()`.

```python
lista = (('def', 100), ('ghi', 200), ('abc', 300))
print(sorted(lista, key=lambda x: x[0])) # [('abc', 300), ('def', 100), ('ghi', 200)]
print(sorted(lista, key=lambda x: x[1])) # [('def', 100), ('ghi', 200), ('abc', 300)]
```
