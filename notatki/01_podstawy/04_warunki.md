## Instrukcje warunkowe

Instrukcje warunkowe są ważnym narzędziem do budowania logiki w programach. Pozwalają one na podejmowanie decyzji w oparciu o sprawdzenie pewnych warunków, które mogą być prawdziwe bądź fałszywe. W praktyce, działanie instrukcji warunkowych przypomina proces myślenia – jeśli coś jest prawdą, to wykonujemy daną część kodu, w przeciwnym razie przechodzimy do innej gałęzi logicznej. Dzięki temu nasz kod potrafi dynamicznie reagować na różne sytuacje i wykonywać odpowiednie operacje w zależności od stanu danych czy innych kryteriów.

W Pythonie kluczowym typem danych służącym do pracy z logiką jest typ `bool`, który może przechowywać jedną z dwóch wartości: `True` albo `False`. Wiele konstrukcji języka, w tym instrukcje warunkowe i pętle, w dużej mierze opiera się na wartościach logicznych, by określić, który fragment kodu powinien zostać wykonany.

### Tworzenie warunków

Aby możliwe było podejmowanie decyzji, musimy najpierw utworzyć wyrażenia (tzw. warunki), które mogą zostać ocenione jako prawdziwe (`True`) lub fałszywe (`False`). W Pythonie operatory porównania (takie jak `==`, `!=`, `>`, `<`, `>=`, `<=`) oraz operatory logiczne (`and`, `or`, `not`) odgrywają tu główną rolę.

Tworzenie warunków w praktyce polega na zestawianiu zmiennych z operatorami. W poniższym przykładzie sprawdzamy, czy osoba o określonym wieku jest pełnoletnia, wykorzystując operator porównania `>=`:

```python
wiek = 18
czy_pelnoletni = wiek >= 18
```

W powyższym przykładzie, zmienna `czy_pelnoletni` będzie miała wartość `True`, ponieważ 18 jest równe 18, a operator `>=` sprawdza, czy `wiek` jest większy lub równy 18. Python zwróci wynik logiczny w postaci `True` bądź `False`, w zależności od tego, czy dany warunek został spełniony.

### Porównania

Operatory porównania w Pythonie umożliwiają zestawianie dwóch wartości i sprawdzanie relacji między nimi. Pozwalają stwierdzić, czy dana wartość jest większa, mniejsza, równa lub różna od innej wartości. Przeprowadzanie porównań jest fundamentalne przy tworzeniu warunków, ponieważ to dzięki nim otrzymujemy wartości logiczne, na których opierają się instrukcje warunkowe.

Poniższa tabela przedstawia podstawowe operatory porównania, wraz z krótkim wyjaśnieniem i przykładowym wynikiem:

| Operator | Opis                  | Przykład      | Wynik    |
|----------|-----------------------|---------------|----------|
| `>`      | większy niż           | `5 > 3`       | `True`   |
| `>=`     | większy lub równy     | `5 >= 5`      | `True`   |
| `<`      | mniejszy niż          | `3 < 5`       | `True`   |
| `<=`     | mniejszy lub równy    | `3 <= 2`      | `False`  |
| `==`     | równy                 | `5 == 5`      | `True`   |
| `!=`     | różny                 | `5 != 3`      | `True`   |

Warto zwrócić uwagę na różnicę pomiędzy `=` a `==`. Pierwszy służy do przypisania wartości do zmiennej, a drugi do porównania dwóch wartości. Jest to często źródłem błędów początkujących programistów, którzy przypadkowo używają `=` zamiast `==` podczas sprawdzania warunku.

W praktyce, porównania mogą być używane nie tylko do liczb, ale również do innych typów danych. Przykładowo możemy porównywać łańcuchy znaków (stringi) czy też obiekty, jeśli zostały do tego odpowiednio przygotowane w kodzie.

### Instrukcja warunkowa

Instrukcje warunkowe w Pythonie służą do wykonania określonego kodu w zależności od spełnienia pewnego warunku. Dzięki nim możemy określić, co ma się stać, gdy warunek jest prawdziwy, a co, gdy jest fałszywy. Najprostszą konstrukcją jest `if-else`, która daje nam możliwość wyboru jednego z dwóch scenariuszy:

```python
if warunek:
    # kod wykonywany, gdy warunek jest prawdziwy
else:
    # kod wykonywany, gdy warunek jest fałszywy
```

Jeśli zatem chcemy, by nasz program zrobił coś konkretnego tylko wtedy, gdy dany warunek jest prawdziwy, używamy `if`. Natomiast jeśli warunek nie jest spełniony (czyli jest fałszywy), przechodzimy do sekcji `else`. Instrukcja `else` nie wymaga własnego warunku – jej kod jest wykonywany w sytuacji, gdy blok `if` nie został wykonany.

W przypadku, gdy mamy do czynienia z wieloma warunkami, można stosować konstrukcję `if-elif-else`. Pozwala ona obsłużyć liczne warianty, z których każdy ma osobny warunek:

```python
if warunek1:
    # kod wykonywany, gdy warunek1 jest prawdziwy
elif warunek2:
    # kod wykonywany, gdy warunek1 jest fałszywy, ale warunek2 jest prawdziwy
else:
    # kod wykonywany, gdy żaden z wcześniejszych warunków nie jest prawdziwy
```

W ten sposób nasz kod staje się bardziej elastyczny i czytelny, ponieważ możemy dokładnie opisać, co powinno się stać przy różnych okolicznościach. Należy pamiętać, że `elif` (skrót od "else if") zawsze sprawdzany jest dopiero wtedy, gdy wcześniejsze warunki okazały się fałszywe.

### Operatory logiczne

Operatory logiczne w Pythonie umożliwiają łączenie i modyfikowanie warunków w bardziej złożone wyrażenia. Dzięki nim możemy sprawdzić więcej niż jeden warunek jednocześnie albo zmienić sens warunku na przeciwny. 

Istnieją trzy podstawowe operatory logiczne:
- **`and`** - oba warunki muszą być prawdziwe, aby całe wyrażenie było prawdziwe.
- **`or`** - przynajmniej jeden warunek musi być prawdziwy, aby całe wyrażenie było prawdziwe.
- **`not`** - neguje warunek, zamieniając `True` na `False` i odwrotnie.

W praktyce często łączymy je z operatorami porównań, aby skonstruować bardziej szczegółowe kryteria decydujące o przebiegu programu. Warto również pamiętać, że Python dokonuje tzw. krótkiego spięcia (short-circuit evaluation), co oznacza, że w przypadku operatora `and` lub `or` wykonanie wyrażenia może zostać zakończone wcześniej, jeśli dalsza część nie jest potrzebna do ustalenia wyniku logicznego.

#### Operator `and`

Operator `and` jest używany, gdy chcemy, aby oba (lub wszystkie połączone) warunki były prawdziwe. Oznacza to, że wyrażenie zwróci `True` tylko wtedy, gdy wszystkie sprawdzane elementy się zgadzają. W przeciwnym razie wynik będzie `False`.

```python
a = 5
b = 10
if a > 0 and b < 20:
    print("Obie wartości spełniają warunek.")
```

W powyższym przykładzie, komunikat zostanie wydrukowany, ponieważ oba warunki są prawdziwe (`a > 0` oraz `b < 20`). Gdyby jedna z wartości nie spełniała warunku, instrukcja `if` zostałaby pominięta.

#### Operator `or`

Operator `or` jest używany, gdy chcemy, aby przynajmniej jeden z warunków był prawdziwy. Dzięki temu nawet jeśli jedna część wyrażenia nie jest spełniona, to całość może wciąż dać wynik `True`, jeśli inny warunek jest prawdziwy.

```python
a = 5
b = 10
if a > 0 or b > 20:
    print("Przynajmniej jeden warunek jest prawdziwy.")
```

W powyższym przykładzie, komunikat zostanie wydrukowany, ponieważ pierwszy warunek jest prawdziwy (`a > 0`), mimo że drugi jest fałszywy (`b > 20`). Wystarczy więc, że spełniony jest jeden z nich, by całość wyrażenia była prawdziwa.

#### Operator `not`

Operator `not` służy do negacji warunku. Oznacza to, że jeśli warunek jest `True`, wówczas `not` zamieni go na `False`, a jeśli był `False`, to `not` go odwróci na `True`. Zastosowanie `not` bywa przydatne, gdy chcemy wyrazić: „wykonaj coś, jeśli warunek jest fałszywy”.

```python
a = 5
if not a > 10:
    print("Warunek jest fałszywy.")
```

W powyższym przykładzie, komunikat zostanie wydrukowany, ponieważ `a > 10` jest fałszywe, a operator `not` zmienia to na `True`. Dzięki temu możemy obsłużyć sytuację, w której główny warunek nie jest spełniony, ale chcemy jednak wykonać pewną akcję.

### Przykład zastosowania operatorów logicznych

Korzystanie z operatorów logicznych pozwala budować złożone warunki, które precyzyjnie określają, kiedy dany fragment kodu powinien się wykonać. Poniższy przykład ilustruje kilka różnych zastosowań tych operatorów:

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
- Trzecia instrukcja `if` używa operatora `not` do sprawdzenia, czy `a` nie jest równe 10. Jeśli warunek jest fałszywy (czyli `a` nie równa się 10), kod się wykona i drukuje odpowiedni komunikat.

W ten sposób, korzystając z różnych kombinacji operatorów, możemy wyrazić szeroką gamę kryteriów, które decydują o przepływie wykonania naszego programu.

### Zastosowanie operatora `or`

W kontekście operatora `or`, dodatkowe wyjaśnienie działania wyrażenia:

```python
odpowiedz = "TAK"
print(odpowiedz == "tak" or "TAK")
```

Wyrażenie to może być mylące. W rzeczywistości kod sprawdza, czy `odpowiedz` jest równa `"tak"`, co jest fałszywe. Jednak drugi „warunek” (po operatorze `or`) jest po prostu wartością typu string `"TAK"`, która – jak każda niepusta wartość – jest w Pythonie traktowana jako prawdziwa w kontekście logicznym. W efekcie całe wyrażenie zwraca `"TAK"`, ale nie dlatego, że porównanie `odpowiedz == "TAK"` zostało wykonane, lecz z powodu interpretacji niepustego łańcucha znaków jako wartości prawdziwej.

Prawidłowe użycie powinno być:

```python
odpowiedz = "TAK"
print(odpowiedz == "tak" or odpowiedz == "TAK")
```

W ten sposób oba warunki są poprawnie sprawdzane, a wynik jest `True` tylko wtedy, gdy `odpowiedz` jest równa `"tak"` lub `"TAK"`. Taka konstrukcja zapobiega nieporozumieniom i pozwala w czytelny sposób wyrazić, że akceptujemy obie wersje odpowiedzi.

Warto pamiętać, że operator `or` nie tylko przerywa sprawdzanie, gdy pierwszy warunek da wynik `True` (tzw. krótkie spięcie), ale także zwraca wartość, która faktycznie zadecydowała o ocenie wyrażenia logicznego. Stąd wynika istotna różnica między porównaniem (zwracającym `True`/`False`) a po prostu wstawieniem niepustego obiektu (również ocenianego w kontekście logicznym, lecz nie będącego stricte wartością `True` lub `False`).
