
### Generatory

Generator to specjalny rodzaj funkcji, który zwraca wartości pojedynczo, zamiast zwracać ich wszystkie naraz w postaci listy lub innego iterowalnego obiektu. Generatory są bardziej efektywne pod względem pamięciowym niż listy, ponieważ nie wymagają przechowywania całej listy w pamięci, lecz tylko aktualnie zwracanej wartości. Generatory umożliwiają także klientowi rozpoczęcie przetwarzania zwracanych wartości zanim generator zakończy swoją pracę.

Aby utworzyć generator, wystarczy zamiast słowa kluczowego `return` użyć słowa kluczowego `yield`. Wartości, które generator ma zwracać są umieszczane po słowie kluczowym `yield` w ciele funkcji. Przykłady użycia generatorów znajdują się poniżej.

a) W poniższym przykładzie zwracamy wartości z funkcji <code>foo()</code> przy pomocy słowa kluczowego <code>yield</code>:

```python
def foo():
  yield 1
  yield 2
  yield 3

print(list(foo()))
```

Wynik po przekonwertowaniu na listę daje:

```
[1, 2, 3]
```

b) W tym przykładzie zwracamy wartości z funkcji <code>bar()</code> przy pomocy słowa kluczowego <code>return</code>:

```python
def bar():
  return 1
  return 2 #Martwy kod
  return 3

print(bar())
```

Wynik:

```
1
```
