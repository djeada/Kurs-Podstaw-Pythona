## Struktury danych

Mamy do dyspozycji kilka różnych sposobów przechowywania danych. Te sposoby to tzw. struktury danych. Są to narzędzia, dzięki którym możemy zbierać i przechowywać duże ilości danych w sposób uporządkowany, co ułatwia nam pracę z tymi danymi.

Oto najpopularniejsze sturktury danych:

* Listy: Listy to uporządkowane kolekcje elementów, które mogą być różnych typów. Są one modyfikowalne, co oznacza, że możemy dodawać, usuwać oraz modyfikować elementy na liście. W liście mogą występować duplikaty.
* Krotki: Krotki są podobne do list, ale są niemodyfikowalne. Oznacza to, że po ich utworzeniu nie możemy zmieniać ich zawartości. Krotki są często używane tam, gdzie chcemy zachować stałość danych. Podobnie jak listy, krotki mogą zawierać duplikaty.
* Zbiory: Zbiory to nieuporządkowane kolekcje unikalnych elementów. Ze względu na ich unikalność, zbiory są użyteczne tam, gdzie interesują nas jedynie różnorodne wartości.
* Słowniki: Słowniki to kolekcje par klucz-wartość. Klucze w słowniku muszą być unikalne, ale wartości mogą się powtarzać. Słowniki są szczególnie przydatne, gdy chcemy przechowywać dane w sposób zorganizowany, np. informacje o osobie, gdzie kluczem jest nazwa atrybutu (np. "imię"), a wartością jest konkretne dane (np. "Anna").

Każda z tych struktur danych ma swoje zastosowania i cechy, które sprawiają, że jest odpowiednia w określonych sytuacjach. Warto więc znać je wszystkie i umieć wybrać odpowiednią strukturę dla danego problemu.

### Lista

Lista jest strukturą danych służącą do przechowywania kilku wartości pod jedną nazwą.

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

Krotka to struktura danych, podobna do listy, ale niezmienna. To znaczy, że po utworzeniu krotki nie możemy jej zmodyfikować, np. dodając do niej nowe elementy czy usuwając już istniejące.

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

Zbiór (ang. set) to nieuporządkowana kolekcja unikalnych elementów. Zbiory są zazwyczaj używane do eliminowania duplikatów lub do testowania przynależności elementu do kolekcji.

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
Słownik używamy, gdy chcemy mieć kilka wartości dostępnych pod różnymi nazwami (kluczami). Słownik jest nieuporządkowany i indeksowany.

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
