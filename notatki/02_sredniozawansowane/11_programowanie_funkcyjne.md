## Programowanie funkcyjne

Programowanie funkcyjne (ang. functional programming) to paradygmat programowania, który traktuje obliczenia jako ewaluację funkcji matematycznych i unika zmiany stanu oraz danych mutowalnych. Jest to podejście odmienne od programowania imperatywnego, gdzie kod składa się z serii instrukcji zmieniających stan programu. 

Cechy programowania funkcyjnego:

1. **Funkcje jako obywatele pierwszej klasy**: Funkcje mogą być przekazywane jako argumenty do innych funkcji, zwracane jako wyniki innych funkcji i przypisywane do zmiennych.
2. **Niezmienność**: Dane są niemutowalne, co oznacza, że po utworzeniu obiektu jego stan nie może być zmieniony.
3. **Brak efektów ubocznych**: Funkcje w programowaniu funkcyjnym nie powinny modyfikować stanu programu ani wprowadzać efektów ubocznych.
4. **Rekurencja**: Programowanie funkcyjne często wykorzystuje rekurencję zamiast pętli iteracyjnych do realizacji powtarzających się operacji.

### Transformacja z `map()`

Funkcja `map()` umożliwia przekształcenie każdego elementu kolekcji. Przyjmuje funkcję oraz kolekcję jako argumenty, a następnie zwraca nową kolekcję, której elementy są wynikami zastosowania podanej funkcji do każdego elementu wejściowej kolekcji.

```python
lista = [5, 10, 15, 20, 25, 30, 35, 40]

# Przekształcenie za pomocą wyrażeń listowych
lista_a = [elem // 5 for elem in lista]  # [1, 2, 3, 4, 5, 6, 7, 8]

# Przekształcenie za pomocą funkcji map()
lista_b = list(map(lambda elem: elem // 5, lista))  # [1, 2, 3, 4, 5, 6, 7, 8]
```

### Filtrowanie z `filter()`

Funkcja `filter()` służy do wybierania elementów kolekcji, które spełniają określone kryterium. Przyjmuje funkcję oraz kolekcję jako argumenty, a następnie zwraca nową kolekcję zawierającą tylko te elementy, dla których funkcja zwróciła wartość prawdziwą.

```python
lista = [5, 10, 15, 20, 25, 30, 35, 40]

# Filtrowanie za pomocą wyrażeń listowych
lista_a = [elem for elem in lista if elem % 2 == 0]  # [10, 20, 30, 40]

# Filtrowanie za pomocą funkcji filter()
lista_b = list(filter(lambda elem: elem % 2 == 0, lista))  # [10, 20, 30, 40]
```

### Agregacja z `reduce()`

Funkcja `reduce()` z modułu `functools` jest używana do redukowania kolekcji do jednej wartości poprzez iteracyjne stosowanie określonej funkcji. Aby korzystać z `reduce()`, należy ją najpierw zaimportować.

```python
from functools import reduce

liczby = [1, 2, 3, 4, 5]
suma = reduce(lambda x, y: x + y, liczby)  # 15
```

### Złożone operacje z wykorzystaniem `map()`, `filter()` i `reduce()`

Funkcje `map()`, `filter()` i `reduce()` można łączyć, aby tworzyć bardziej złożone operacje na kolekcjach. Przykład poniżej demonstruje ich zastosowanie w jednym ciągu operacji.

```python
napis = 'Python is Love'

# Zwraca listę kodów ASCII wielkich liter w ciągu
lista = list(map(lambda znak: ord(znak), filter(lambda znak: znak.isupper(), napis)))  # [80, 76]
```

W powyższym przykładzie:
- `filter()` wybiera tylko wielkie litery z napisu.
- `map()` przekształca wybrane litery na ich kody ASCII.
