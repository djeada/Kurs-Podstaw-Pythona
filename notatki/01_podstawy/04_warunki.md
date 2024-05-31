## Instrukcje warunkowe

Typ logiczny (`bool`) w Pythonie może przyjmować jedną z dwóch wartości: `True` lub `False`. Jest to kluczowe dla działania instrukcji warunkowych, które decydują o przebiegu programu w zależności od spełnienia określonych kryteriów.

### Tworzenie warunków

Instrukcje warunkowe w Pythonie są podstawą do podejmowania decyzji w kodzie. Można tworzyć warunki, które sprawdzają różne kryteria i na ich podstawie wykonują określone działania.

```python
wiek = 18
czy_pelnoletni = wiek >= 18
```

W powyższym przykładzie, zmienna `czy_pelnoletni` będzie miała wartość `True`, ponieważ 18 jest równe 18.

### Porównania w Pythonie

Python oferuje różne operatory porównania, które mogą być używane do tworzenia warunków:

| Operator | Opis                  | Przykład      | Wynik    |
|----------|-----------------------|---------------|----------|
| `>`      | większy niż           | `5 > 3`       | `True`   |
| `>=`     | większy lub równy     | `5 >= 5`      | `True`   |
| `<`      | mniejszy niż          | `3 < 5`       | `True`   |
| `<=`     | mniejszy lub równy    | `3 <= 2`      | `False`  |
| `==`     | równy                 | `5 == 5`      | `True`   |
| `!=`     | różny                 | `5 != 3`      | `True`   |

Warto zwrócić uwagę na różnicę pomiędzy `=` a `==`. Pierwszy służy do przypisania wartości do zmiennej, a drugi do porównania dwóch wartości.

### Instrukcja warunkowa

Instrukcje warunkowe w Pythonie służą do wykonania określonego kodu w zależności od spełnienia pewnego warunku.

Podstawowa struktura to `if-else`:

```python
if warunek:
    # kod wykonywany, gdy warunek jest prawdziwy
else:
    # kod wykonywany, gdy warunek jest fałszywy
```

W przypadku wielu warunków, można używać `elif` (skrót od "else if"):

```python
if warunek1:
    # kod wykonywany, gdy warunek1 jest prawdziwy
elif warunek2:
    # kod wykonywany, gdy warunek1 jest fałszywy, ale warunek2 jest prawdziwy
else:
    # kod wykonywany, gdy żaden z wcześniejszych warunków nie jest prawdziwy
```


### Operatory logiczne

Operatory logiczne w Pythonie są niezwykle przydatne do łączenia i modyfikowania warunków. Poniżej przedstawiono główne operatory logiczne:

- **`and`** - oba warunki muszą być prawdziwe, aby całe wyrażenie było prawdziwe.
- **`or`** - przynajmniej jeden warunek musi być prawdziwy, aby całe wyrażenie było prawdziwe.
- **`not`** - neguje warunek, zamieniając `True` na `False` i odwrotnie.

#### Operator `and`

Operator `and` jest używany, gdy chcemy, aby oba warunki były prawdziwe:

    ```python
    a = 5
    b = 10
    if a > 0 and b < 20:
        print("Obie wartości spełniają warunek.")
    ```

W powyższym przykładzie, komunikat zostanie wydrukowany, ponieważ oba warunki są prawdziwe (`a > 0` oraz `b < 20`).

#### Operator `or`

Operator `or` jest używany, gdy chcemy, aby przynajmniej jeden z warunków był prawdziwy:

```python
a = 5
b = 10
if a > 0 or b > 20:
    print("Przynajmniej jeden warunek jest prawdziwy.")
```

W powyższym przykładzie, komunikat zostanie wydrukowany, ponieważ pierwszy warunek jest prawdziwy (`a > 0`), mimo że drugi jest fałszywy (`b > 20`).

#### Operator `not`

Operator `not` jest używany do negacji warunku:

```python
a = 5
if not a > 10:
    print("Warunek jest fałszywy.")
```

W powyższym przykładzie, komunikat zostanie wydrukowany, ponieważ `a > 10` jest fałszywe, a `not` zmienia to na `True`.

### Przykład zastosowania operatorów logicznych:

```python
a = 5
b = 10
c = 15

if a < b and b < c:
    print("a jest mniejsze od b, a b jest mniejsze od c.")

if a == 5 or b == 5:
    print("Przynajmniej jedna z wartości a lub b jest równa 5.")

if not a == 10:
    print("a nie jest równe 10.")
```

W tym przykładzie:

- Pierwsza instrukcja `if` sprawdza, czy `a` jest mniejsze od `b` i `b` jest mniejsze od `c`. Jeśli oba warunki są prawdziwe, drukuje komunikat.
- Druga instrukcja `if` sprawdza, czy `a` jest równe 5 lub `b` jest równe 5. Jeśli przynajmniej jeden z tych warunków jest prawdziwy, drukuje komunikat.
- Trzecia instrukcja `if` używa operatora `not` do sprawdzenia, czy `a` nie jest równe 10. Jeśli warunek jest fałszywy, drukuje komunikat.

### Zastosowanie operatora `or` w kontekście:

W kontekście operatora `or`, dodatkowe wyjaśnienie działania wyrażenia:

```python
odpowiedz = "TAK"
print(odpowiedz == "tak" or "TAK")
```

Wyrażenie to może być mylące. W rzeczywistości kod sprawdza, czy `odpowiedz` jest równa `"tak"`, co jest fałszywe. Jednak drugi warunek (po operatorze `or`) jest po prostu wartością string `"TAK"`, która jest zawsze traktowana jako prawdziwa w kontekście logicznym. Dlatego całe wyrażenie zwraca `"TAK"`, ale nie z powodu spełnienia warunku porównania, tylko dlatego, że string `"TAK"` jest "prawdziwy".

Prawidłowe użycie powinno być:

```python
odpowiedz = "TAK"
print(odpowiedz == "tak" or odpowiedz == "TAK")
```

W ten sposób oba warunki są poprawnie sprawdzane, a wynik jest `True` tylko wtedy, gdy `odpowiedz` jest równa `"tak"` lub `"TAK"`.
