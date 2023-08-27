## Instrukcje warunkowe

Typ logiczny (`bool`) w Pythonie może przyjmować jedną z dwóch wartości: `True` lub `False`. Jest to kluczowe dla działania instrukcji warunkowych, które decydują o przebiegu programu w zależności od spełnienia określonych kryteriów.

### Tworzenie warunków

```python
wiek = 18
czy_pelnoletni = wiek >= 18
```

W powyższym przykładzie, zmienna `czy_pelnoletni` będzie miała wartość `True`, ponieważ 18 jest równe 18.

### Porównania w Pythonie

| Operator | Opis                  | Przykład      | Wynik    |
|----------|-----------------------|---------------|----------|
| `>`      | większy niż           | `5 > 3`       | `True`   |
| `>=`     | większy lub równy     | `5 >= 5`      | `True`   |
| `<`      | mniejszy niż           | `3 < 5`       | `True`   |
| `<=`     | mniejszy lub równy     | `3 <= 2`      | `False`  |
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

Do łączenia i modyfikacji warunków w Pythonie stosuje się operatory logiczne:

- `and` - oba warunki muszą być prawdziwe
- `or` - przynajmniej jeden warunek musi być prawdziwy
- `not` - neguje warunek

Przykład zastosowania operatorów logicznych:

```python
a = 5
b = 10
if a > 0 and b < 20:
    print("Obie wartości spełniają warunek.")
```

W kontekście operatora `or`, istotne jest dodatkowe wyjaśnienie działania wyrażenia:

```python
odpowiedz = "TAK"
print(odpowiedz == "tak" or "TAK")
```

Wyrażenie to jest mylące. W rzeczywistości kod sprawdza, czy odpowiedz jest równa "tak", co jest fałszywe. Jednak drugi warunek (po operatorze or) jest po prostu wartością string "TAK", która jest zawsze traktowana jako prawdziwa w kontekście logicznym. Dlatego całe wyrażenie zwraca "TAK", ale nie z powodu spełnienia warunku porównania, tylko dlatego, że string "TAK" jest "prawdziwy".
