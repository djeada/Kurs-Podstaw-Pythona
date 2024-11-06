## Programowanie funkcyjne

Programowanie funkcyjne, znane również pod angielską nazwą *functional programming*, to paradygmat programowania, który może wydawać się nieco odmienny od tradycyjnych metod. Zamiast skupiać się na sekwencji kroków i zmianie stanu programu, jak to ma miejsce w programowaniu imperatywnym, programowanie funkcyjne traktuje obliczenia jako ewaluację funkcji matematycznych. W tym podejściu unika się zmiany stanu oraz używania danych mutowalnych, co oznacza, że dane nie są modyfikowane po ich utworzeniu. Zamiast tego, tworzy się nowe dane na podstawie istniejących, co prowadzi do kodu bardziej przewidywalnego i łatwiejszego w utrzymaniu.

W programowaniu funkcyjnym funkcje są traktowane jako obywatelki pierwszej klasy. Oznacza to, że funkcje mogą być przekazywane jako argumenty do innych funkcji, zwracane jako wyniki, a nawet przechowywane w strukturach danych. Dzięki temu możliwe jest tworzenie bardziej elastycznego i modularnego kodu. Ponadto, funkcje są zazwyczaj *czyste*, co znaczy, że nie mają efektów ubocznych i dla tych samych argumentów zawsze zwracają ten sam wynik. To sprawia, że kod jest bardziej przewidywalny i łatwiejszy do testowania.

Kolejną istotną cechą jest niezmienność danych. Po utworzeniu obiektu jego stan nie jest zmieniany; jeśli potrzebujemy zmodyfikowanej wersji danych, tworzymy nowy obiekt na podstawie istniejącego. To podejście pomaga unikać błędów związanych z nieoczekiwaną zmianą stanu i ułatwia równoległe przetwarzanie danych.

Zamiast tradycyjnych pętli iteracyjnych, programowanie funkcyjne często wykorzystuje rekurencję do realizacji powtarzających się operacji. Rekurencja polega na tym, że funkcja wywołuje samą siebie z nowymi argumentami, aż do osiągnięcia warunku bazowego.

### Transformacja danych z użyciem `map()`

Wyobraź sobie, że masz listę liczb i chcesz przekształcić każdą z nich według określonej reguły, na przykład podzielić przez pewną wartość. Funkcja `map()` w Pythonie umożliwia to w prosty i elegancki sposób. Przyjmuje ona funkcję i kolekcję jako argumenty, a następnie zwraca nową kolekcję z przekształconymi elementami.

Przykład:

```python
lista = [5, 10, 15, 20, 25, 30, 35, 40]
```

Chcemy podzielić każdą liczbę przez 5 i otrzymać nową listę wyników. Możemy to osiągnąć na dwa sposoby.

Pierwszy sposób to użycie wyrażenia listowego:

```python
lista_a = [elem // 5 for elem in lista]
# Wynik: [1, 2, 3, 4, 5, 6, 7, 8]
```

Drugi sposób to zastosowanie funkcji `map()`:

```python
lista_b = list(map(lambda elem: elem // 5, lista))
# Wynik: [1, 2, 3, 4, 5, 6, 7, 8]
```

Oba podejścia dają ten sam rezultat. Funkcja `map()` stosuje podaną funkcję do każdego elementu kolekcji, tworząc nową kolekcję z wynikami. Jest to szczególnie przydatne, gdy chcemy zastosować bardziej złożoną funkcję przekształcającą lub gdy zależy nam na zachowaniu stylu funkcyjnego w naszym kodzie.

### Selekcja danych z użyciem `filter()`

Czasami potrzebujemy wybrać z kolekcji tylko te elementy, które spełniają określone kryterium. Funkcja `filter()` służy właśnie do tego celu. Przyjmuje funkcję i kolekcję jako argumenty, a następnie zwraca nową kolekcję zawierającą tylko te elementy, dla których funkcja zwróciła wartość prawdziwą.

Przykładowo, chcemy z listy liczb wybrać tylko liczby parzyste:

```python
lista = [5, 10, 15, 20, 25, 30, 35, 40]
```

Możemy to zrobić za pomocą wyrażenia listowego:

```python
lista_a = [elem for elem in lista if elem % 2 == 0]
# Wynik: [10, 20, 30, 40]
```

Lub używając funkcji `filter()`:

```python
lista_b = list(filter(lambda elem: elem % 2 == 0, lista))
# Wynik: [10, 20, 30, 40]
```

Funkcja `filter()` przechodzi przez każdy element kolekcji i przepuszcza tylko te, dla których podana funkcja zwraca wartość prawdziwą. Jest to użyteczne narzędzie do filtrowania danych bez konieczności pisania dodatkowych pętli czy warunków.

### Redukcja danych z użyciem `reduce()`

Zdarza się, że potrzebujemy zredukować kolekcję do pojedynczej wartości, na przykład sumując wszystkie jej elementy. Funkcja `reduce()`, dostępna w module `functools`, jest do tego idealna. Działa ona poprzez iteracyjne stosowanie funkcji do elementów kolekcji, przekazując wynik poprzedniego wywołania jako pierwszy argument do kolejnego.

Aby skorzystać z `reduce()`, najpierw ją importujemy:

```python
from functools import reduce
```

Przykład sumowania listy liczb:

```python
liczby = [1, 2, 3, 4, 5]
suma = reduce(lambda x, y: x + y, liczby)
# Wynik: 15
```

W tym przypadku `reduce()` sumuje kolejno elementy listy:

1. Dodaje pierwsze dwa elementy: `1 + 2 = 3`.
2. Następnie dodaje wynik do kolejnego elementu: `3 + 3 = 6`.
3. Kontynuuje ten proces aż do ostatniego elementu.

W rezultacie otrzymujemy sumę wszystkich elementów listy.

### Łączenie funkcji `map()`, `filter()` i `reduce()`

Funkcje `map()`, `filter()` i `reduce()` można łączyć, aby wykonywać bardziej złożone operacje na danych. Dzięki temu możemy przetwarzać kolekcje w sposób deklaratywny i czytelny.

Przykład:

Mamy napis:

```python
napis = 'Python is Love'
```

Chcemy z tego napisu:

1. Wybrać wszystkie wielkie litery.
2. Zamienić je na ich kody ASCII.
3. Zsumować te kody.

Krok po kroku:

**Wybieranie wielkich liter za pomocą `filter()`:**

```python
wielkie_litery = filter(lambda znak: znak.isupper(), napis)
# Wynik: iterator zawierający 'P' i 'L'
```

Funkcja `znak.isupper()` zwraca `True` dla wielkich liter, więc `filter()` przepuszcza tylko te znaki.

**Zamiana liter na kody ASCII za pomocą `map()`:**

```python
kody_ascii = map(lambda znak: ord(znak), wielkie_litery)
# Wynik: iterator zawierający 80 i 76
```

Funkcja `ord()` zwraca kod ASCII znaku.

**Sumowanie kodów za pomocą `reduce()`:**

```python
from functools import reduce
suma_kodow = reduce(lambda x, y: x + y, kody_ascii)
# Wynik: 156
```

`reduce()` sumuje kody ASCII, dając ostateczny wynik.

Możemy to wszystko połączyć w jedno wyrażenie:

```python
suma_kodow = reduce(
    lambda x, y: x + y,
    map(
        lambda znak: ord(znak),
        filter(lambda znak: znak.isupper(), napis)
    )
)
# Wynik: 156
```

To połączenie funkcji pokazuje, jak można w sposób deklaratywny i zwięzły przetwarzać dane, łącząc proste operacje w potężne narzędzia. Dzięki temu kod jest czytelny i łatwy do modyfikacji, a także zgodny z zasadami programowania funkcyjnego.
