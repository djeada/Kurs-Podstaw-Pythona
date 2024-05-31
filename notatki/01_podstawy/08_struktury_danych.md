## Struktury danych

Mamy do dyspozycji kilka różnych sposobów przechowywania danych, które nazywamy strukturami danych. Są to narzędzia, dzięki którym możemy zbierać i przechowywać duże ilości danych w sposób uporządkowany, co znacząco ułatwia pracę z tymi danymi.

Oto najpopularniejsze struktury danych:

- **Listy**: Są najbardziej uniwersalne i mogą być używane wszędzie tam, gdzie potrzebujemy dynamicznej, modyfikowalnej kolekcji elementów. Doskonale nadają się do przechowywania sekwencyjnych danych, które mogą się zmieniać. Przykładowe zastosowania to:
  - Przechowywanie listy zakupów.
  - Gromadzenie wyników pomiarów w eksperymencie.
  - Przechowywanie obiektów w grze komputerowej.

- **Krotki**: Idealne do przechowywania zestawów danych, które nie powinny się zmieniać po ich utworzeniu. Często używane jako klucze w słownikach lub jako elementy zwracane przez funkcje, które zwracają wiele wartości. Przykłady zastosowań to:
  - Przechowywanie współrzędnych punktu (x, y).
  - Zwracanie wielu wartości z funkcji (np. status i wynik operacji).
  - Przechowywanie danych konfiguracyjnych, które nie powinny być modyfikowane.

- **Zbiory**: Używane tam, gdzie potrzebujemy unikalnych elementów i nie zależy nam na ich kolejności. Przydatne w operacjach matematycznych takich jak sumy, przecięcia i różnice zbiorów. Przykłady zastosowań to:
  - Przechowywanie unikalnych identyfikatorów.
  - Realizacja operacji zbiorowych, takich jak unia czy przecięcie.
  - Filtrowanie duplikatów z listy.

- **Słowniki**: Najlepsze do przechowywania danych w formie klucz-wartość, co pozwala na szybki dostęp do wartości na podstawie klucza. Idealne do przechowywania ustrukturyzowanych danych, takich jak rekordy bazy danych czy konfiguracje. Przykłady zastosowań to:
  - Przechowywanie konfiguracji aplikacji.
  - Indeksowanie danych na podstawie unikalnych kluczy (np. numerów identyfikacyjnych).
  - Przechowywanie słownika językowego (tłumaczenia słów).

Każda z tych struktur danych ma swoje unikalne zastosowania i cechy, które sprawiają, że jest odpowiednia w określonych sytuacjach. Poniżej znajdują się bardziej szczegółowe opisy zastosowań poszczególnych struktur danych:

### Lista

Listy to uporządkowane kolekcje elementów, które mogą być różnych typów. Są one modyfikowalne, co oznacza, że możemy dodawać, usuwać oraz modyfikować elementy na liście. W liście mogą występować duplikaty.

Przykład listy złożonej z kilku liczb całkowitych:

```python
lista = [3, 2, 3, 9, 10]
```

Elementy listy nie muszą być tego samego typu:

```python
lista = ['a', True, 0.3]
```

Aby poznać liczbę elementów listy, należy użyć funkcji `len`:

```python
n = len(lista)
```
   
Aby dodać element a na końcu listy, użyj metody `append`:

```python
lista.append(a)
```

Aby dodać wszystkie elementy z listy lista2 na końcu listy lista1, użyj metody `extend`:

```python
lista1.extend(lista2)
```

Aby wstawić element a na pozycję i, użyj metody `insert`:

```python
lista.insert(i,a)
```

Aby usunąć pierwsze wystąpienie elementu a z listy, użyj metody `remove`:

```python
lista.remove(a)
```

Aby usunąć element z listy znajdujący się na pozycji i oraz zwrócić go jako wynik, użyj metody `pop`:

```python
element = lista.pop([i])
```

Aby znaleźć liczbę wystąpień elementu a w liście, użyj metody `count`:

```python
licznik = lista.count(a)
```

Aby posortować listę, użyj metody `sort`:

```python
lista.sort()
```

Aby odwrócić kolejność elementów w liście, użyj metody `reverse`:

```python
lista.reverse()
```

Aby przy pomocy pętli przejść przez elementy listy, użyj słowa kluczowego `for`:


```python
for element in lista: 
    print(element)
```  

Aby otrzymać element i indeks, użyj funkcji `enumerate`:

```python
for indeks, element in enumerate(lista): 
    print(f'{indeks}: {element}')
```

Aby przy pomocy pętli przejść przez elementy dwóch list równej długości, użyj funckji `zip`:

```python
for elem_a, elem_b in zip(lista_a, lista_b): 
    print(f'element a: {elem_a}; element b: {elem_b}')
```

### Krotka

Krotki są podobne do list, ale są niemodyfikowalne. Oznacza to, że po ich utworzeniu nie możemy zmieniać ich zawartości. Krotki są często używane tam, gdzie chcemy zachować stałość danych. Podobnie jak listy, krotki mogą zawierać duplikaty.

Krotek zamiast list, używamy gdy:

* Liczy się szybkość.
* Chcemy zabezpieczyć dane przed nadpisaniem.

Przykład krotki składającej się z kilku liczb całkowitych:

```python
krotka = (3, 2, 3, 9, 10)
```

Elementy krotki nie muszą być tego samego typu:

```python
krotka = ('a', True, 0.3)
```

Aby rozpakować krotkę składającą się z trzech elementów i zapisać je w trzech zmiennych, użyj:

```python
a, b, c = krotka
```

Aby znaleźć liczbę elementów krotki, użyj:

```python
len(krotka)
```

Aby przy pomocy pętli przejść przez elementy krotki, użyj:

```python
for element in krotka: 
    print(element)
```

Aby otrzymać element i indeks, użyj funkcji `enumerate`:

```python
for indeks, element in enumerate(krotka): 
    print(f'{indeks}: {element}')
```

Aby przy pomocy pętli przejść przez elementy dwóch krotek równej długości, użyj funckji `zip`:

```python
for elem_a, elem_b in zip(krotka_a, krotka_b): 
    print(f'element a: {elem_a}; element b: {elem_b}')
```

### Zbiór

Zbiory to nieuporządkowane kolekcje unikalnych elementów. Ze względu na ich unikalność, zbiory są użyteczne tam, gdzie interesują nas jedynie różnorodne wartości.

Aby utworzyć pusty zbiór, użyj:

```python
zbior = set()
```

Aby utworzyć zbiór z elementów podanych jako argumenty, użyj:

```python
zbior = set([element1, element2, element3])
```

Aby utworzyć zbiór z elementów występujących w iterowalnym obiekcie (np. liście), użyj:

```python
zbior = set(iterowalny_obiekt)
```

Aby sprawdzić, czy element jest w zbiorze, użyj:

```python
element in zbior
```

Aby dodać element do zbioru, użyj:

```python
zbior.add(element)
```

Aby usunąć element ze zbioru, użyj:

```python
zbior.remove(element)
```

Aby usunąć element ze zbioru, jeśli istnieje, bez generowania błędu, użyj:

```python
zbior.discard(element)
```

Aby usunąć losowy element ze zbioru, użyj:

```python
zbior.pop()
```

Aby usunąć wszystkie elementy ze zbioru, użyj:

```python
zbior.clear()
```

Aby znaleźć liczbę elementów w zbiorze, użyj:

```python
len(zbior)
```

Aby złączyć zbiory, użyj operatora `|`:

```python
zbior1 | zbior2
```

Aby wyświetlić elementy wspólne dla dwóch zbiorów, użyj operatora `&`:

```python
zbior1 & zbior2
```

Aby wyświetlić elementy występujące w jednym zbiorze, ale nie w drugim, użyj operatora `^`:

```python
zbior1 ^ zbior2
```

Aby wyświetlić elementy z pierwszego zbioru, ale nie z drugiego, użyj operatora `-`:

```python
zbior1 - zbior2
```

Aby sprawdzić, czy zbiór jest podzbiorem innego zbioru, użyj operatora `<=`:

```python
zbior1 <= zbior2
```

### Słownik

Słowniki to kolekcje par klucz-wartość. Klucze w słowniku muszą być unikalne, ale wartości mogą się powtarzać. Słowniki są szczególnie przydatne, gdy chcemy przechowywać dane w sposób zorganizowany, np. informacje o osobie, gdzie kluczem jest nazwa atrybutu (np. "imię"), a wartością jest konkretne dane (np. "Anna").

W słowniku można używać jako kluczy dowolnych typów danych, które są niemutowalne (tj. nie mogą być zmieniane). Do niemutowalnych typów danych w Pythonie zaliczają się:

* liczby całkowite (int)
* liczby zmiennoprzecinkowe (float)
* napisy (str)
* krotki (tuple)

Nie można natomiast używać jako kluczy mutowalnych typów danych, takich jak listy, zbiory lub słowniki, ponieważ nie spełniają one wymogu niemutowalności.

Przykłady poprawnych kluczy:

* liczba całkowita: `slownik[42]`
* napis: `slownik['klucz']`
* krotka: `slownik[(1, 2, 3)]`

Przykłady niepoprawnych kluczy:

* lista: `slownik[[1, 2, 3]]`
* zbiór: `slownik{1, 2, 3}`
* słownik: `slownik{'klucz': 'wartosc'}`

Przykład słownika zawierającego kilka par klucz-wartość:

```python
slownik = {'klucz1': 3, 'klucz2': 2, 'klucz3': 3}
```

Elementy słownika nie muszą być tego samego typu:

```python
slownik = {'klucz1': 'a', 'klucz2': True, 'klucz3': 0.3}
```

Aby znaleźć liczbę elementów słownika, użyj:

```python
len(slownik)
```

Aby dodać element a pod kluczem 'klucz4', użyj:

```python
slownik['klucz4'] = a
```

Aby zmienić wartość pod kluczem 'klucz4', użyj:

```python
slownik['klucz4'] = nowa_wartosc
```

Aby usunąć element pod kluczem 'klucz4', użyj:

```python
del slownik['klucz4']
```

Aby sprawdzić czy klucz 'klucz4' istnieje w słowniku, użyj:

```python
'klucz4' in slownik
```

Aby przy pomocy pętli przejść przez elementy słownika, użyj:

```python
for klucz, wartosc in slownik.items(): 
    print(f'{klucz}: {wartosc}')
```
    
Aby przy pomocy pętli przejść tylko przez klucze słownika, użyj:

```python
for klucz in slownik: 
    print(klucz)
```

Aby przy pomocy pętli przejść tylko przez wartości słownika, użyj:

```python
for wartosc in slownik.values(): 
    print(wartosc)
```

### Podsumowanie metod dostępnych dla struktur danych

| Struktura danych | Metoda                  | Opis                                                                              | Przykład                                               |
|------------------|-------------------------|-----------------------------------------------------------------------------------|--------------------------------------------------------|
| **Lista**        | `append()`              | Dodaje element na końcu listy.                                                    | `lista.append(5)`                                      |
|                  | `extend()`              | Dodaje wszystkie elementy z podanej kolekcji do listy.                            | `lista.extend([6, 7, 8])`                              |
|                  | `insert()`              | Wstawia element na określonej pozycji.                                            | `lista.insert(1, 'a')`                                 |
|                  | `remove()`              | Usuwa pierwsze wystąpienie określonego elementu.                                  | `lista.remove('a')`                                    |
|                  | `pop()`                 | Usuwa i zwraca element z określonej pozycji (domyślnie ostatni element).          | `lista.pop()`                                          |
|                  | `clear()`               | Usuwa wszystkie elementy z listy.                                                 | `lista.clear()`                                        |
|                  | `index()`               | Zwraca indeks pierwszego wystąpienia określonego elementu.                        | `lista.index(5)`                                       |
|                  | `count()`               | Zwraca liczbę wystąpień określonego elementu.                                     | `lista.count(5)`                                       |
|                  | `sort()`                | Sortuje elementy listy w miejscu.                                                 | `lista.sort()`                                         |
|                  | `reverse()`             | Odwraca kolejność elementów listy.                                                | `lista.reverse()`                                      |

| **Krotka**       | `count()`               | Zwraca liczbę wystąpień określonego elementu.                                     | `krotka.count(5)`                                      |
|                  | `index()`               | Zwraca indeks pierwszego wystąpienia określonego elementu.                        | `krotka.index(5)`                                      |

| **Zbiór**        | `add()`                 | Dodaje element do zbioru.                                                         | `zbior.add(5)`                                         |
|                  | `remove()`              | Usuwa element ze zbioru; wyrzuca błąd, jeśli element nie istnieje.                 | `zbior.remove(5)`                                      |
|                  | `discard()`             | Usuwa element ze zbioru, jeśli istnieje.                                          | `zbior.discard(5)`                                     |
|                  | `pop()`                 | Usuwa i zwraca losowy element ze zbioru.                                          | `zbior.pop()`                                          |
|                  | `clear()`               | Usuwa wszystkie elementy ze zbioru.                                               | `zbior.clear()`                                        |
|                  | `union()`               | Zwraca nowy zbiór będący sumą zbiorów.                                            | `zbior.union(inny_zbior)`                             |
|                  | `intersection()`        | Zwraca nowy zbiór będący przecięciem zbiorów.                                     | `zbior.intersection(inny_zbior)`                      |
|                  | `difference()`          | Zwraca nowy zbiór będący różnicą zbiorów.                                         | `zbior.difference(inny_zbior)`                        |
|                  | `symmetric_difference()`| Zwraca nowy zbiór będący symetryczną różnicą zbiorów.                             | `zbior.symmetric_difference(inny_zbior)`              |

| **Słownik**      | `get()`                 | Zwraca wartość dla określonego klucza.                                            | `slownik.get('klucz')`                                |
|                  | `keys()`                | Zwraca widok wszystkich kluczy w słowniku.                                        | `slownik.keys()`                                       |
|                  | `values()`              | Zwraca widok wszystkich wartości w słowniku.                                      | `slownik.values()`                                     |
|                  | `items()`               | Zwraca widok wszystkich par klucz-wartość w słowniku.                             | `slownik.items()`                                      |
|                  | `pop()`                 | Usuwa i zwraca wartość dla określonego klucza.                                    | `slownik.pop('klucz')`                                 |
|                  | `popitem()`             | Usuwa i zwraca ostatnią parę klucz-wartość.                                       | `slownik.popitem()`                                    |
|                  | `clear()`               | Usuwa wszystkie elementy ze słownika.                                             | `slownik.clear()`                                      |
|                  | `update()`              | Aktualizuje słownik o podane pary klucz-wartość.                                  | `slownik.update({'klucz2': 'wartosc2'})`              |
|                  | `setdefault()`          | Zwraca wartość dla określonego klucza, jeśli klucz nie istnieje dodaje go z wartością domyślną. | `slownik.setdefault('klucz', 'domyslna_wartosc')`     |
