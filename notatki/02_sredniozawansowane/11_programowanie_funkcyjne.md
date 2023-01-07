### Programowanie funkcyjne

Istnieją różne narzędzia służące do transformacji danych. W tym artykule przyjrzymy się kilku z nich: <code>map()</code>, <code>filter()</code> i <code>reduce()</code>. Funkcje te są często używane w programowaniu funkcyjnym. Programowanie funkcyjne to paradygmat programowania, w którym głównym sposobem reprezentowania algorytmów są funkcje. W programowaniu funkcyjnym nacisk kładzie się na transformację danych przy użyciu funkcji, a nie na ich modyfikację w miejscu.

Funkcja <code>map()</code> to narzędzie służące do transformowania elementów jednej listy według określonej reguły. Ma ona dwa parametry: nazwę funkcji przyjmującej jeden argument (może to być też wyrażenie lambda) oraz nazwę listy. Funkcja <code>map()</code> zwraca nową listę, w której elementy są wynikami wywołania funkcji przekazanej jako pierwszy argument dla każdego elementu listy przekazanej jako drugi argument.

Istnieją również inne sposoby na osiągnięcie tego samego efektu, takie jak pętle for lub wyrażenia listowe. Aby lepiej zrozumieć działanie <code>map()</code>, warto porównać je z innymi metodami:

```python
lista = [5, 10, 15, 20, 25, 30, 35, 40]

lista_a = [elem // 5 for elem in lista] # [1, 2, 3, 4, 5, 6, 7, 8]
lista_b = list(map(lambda elem : elem // 5, lista)) # [1, 2, 3, 4, 5, 6, 7, 8]
```

Podobnie działa funkcja <code>filter()</code>. Jej wynikiem jest również nowa lista, złożona z elementów listy przekazanej jako drugi argument, dla których wywołanie funkcji przekazanej jako pierwszy argument zwróciło wartość logiczną `True`. Także i tutaj możemy porównać działanie <code>filter()</code> z innymi sposobami:

```python
lista = [5, 10, 15, 20, 25, 30, 35, 40]

lista_a = [elem // 5 for elem in lista if elem % 2 == 0] # [2, 4, 6, 8]
lista_b = list(map(lambda elem : elem // 5, filter(lambda elem : elem % 2 == 0, lista))) # [2, 4, 6, 8]
```

Funkcja `reduce()` jest narzędziem służącym do agregacji elementów sekwencji według określonej reguły. Podobnie jak `map()` i `filter()`, `reduce()` przyjmuje jako argumenty funkcję oraz sekwencję. Różnica polega na tym, że `reduce()` wywołuje funkcję iteracyjnie na elementach sekwencji i zwraca pojedynczy wynik agregacji. W poniższym przykładzie pokazane są dwa sposoby na utworzenie listy składającej się z numerów ASCII odpowiadających wielkim literom otrzymanego słowa:

```python
napis = 'Python is Love'
lista_a = [ord(znak) for znak in napis if znak.isupper()]
lista_b = list(map(lambda znak: ord(znak), filter(lambda znak: znak.isupper(), napis)))

print(lista_a) # ['p', 'l']
print(lista_b) # ['p', 'l']
```

Pętle możemy w naturalny sposób zagnieżdżać. Podobnie możemy również operować na funkcjach <code>map()</code>, <code>filter()</code> i <code>reduce()</code>:

```python
x = [2, 3, 5]
y = [1, 2]

lista_a = [elem_x + elem_y for elem_x in x for elem_y in y] # [3, 4, 4, 5, 6, 7]
lista_b = list()
list(map(lambda elem_x: list(map(lambda elem_y: lista_b.append(elem_x + elem_y), y)), x)) # [3, 4, 4, 5, 6, 7]
```
