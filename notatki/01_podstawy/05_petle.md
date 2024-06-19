## Pętle

Pętle w Pythonie, podobnie jak w wielu innych językach programowania, pozwalają na wielokrotne wykonanie fragmentu kodu. Umożliwiają efektywne przetwarzanie kolekcji danych, takich jak listy czy słowniki, oraz wykonywanie powtarzalnych operacji bez konieczności wielokrotnego pisania tego samego kodu.

### Pętla For

Pętla `for` służy do iteracji po elementach kolekcji (np. listy, krotki, słowniki, ciągi znaków) lub po sekwencji liczb generowanej przez funkcję `range()`.

Podstawowa składnia pętli `for` wygląda następująco:

```python
for element in kolekcja:
    # kod do wykonania dla każdego elementu
```

Funkcja `range()` jest często używana w pętlach for, gdy chcemy wykonać blok kodu określoną liczbę razy. Może przyjmować różną liczbę argumentów:

- `range(n)` - generuje sekwencję od 0 do n-1.
- `range(start, stop)` - generuje sekwencję od start do stop-1.
- `range(start, stop, krok)` - generuje sekwencję zaczynając od start, kończąc na stop-1, zwiększając wartość o krok przy każdej iteracji.

Przykłady:

```python
for i in range(5):
    # powtórzy blok 5 razy (dla i=0, 1, 2, 3, 4)
    print(i)

for i in range(3, 8):
    # powtórzy blok dla i=3, 4, 5, 6, 7
    print(i)

for i in range(0, 10, 2):
    # powtórzy blok dla i=0, 2, 4, 6, 8
    print(i)
```

### Pętla While

Pętla `while` w Pythonie umożliwia wielokrotne wykonanie bloku kodu, dopóki określony warunek jest prawdziwy. W przeciwieństwie do pętli `for`, która iteruje się przez znane wcześniej kolekcje danych, pętla `while` może być używana do tworzenia pętli, których liczba iteracji nie jest znana z góry.

Podstawowa składnia pętli `while` jest następująca:

```python
while warunek:
    # kod do wykonania
```

Każdy obieg pętli rozpoczyna się od sprawdzenia warunku. Jeśli warunek jest prawdziwy, blok kodu wewnątrz pętli jest wykonany. Po wykonaniu bloku, warunek jest ponownie sprawdzany, i jeśli nadal jest prawdziwy, pętla kontynuuje swoje działanie. Proces ten powtarza się, aż warunek stanie się fałszywy, wtedy pętla zostaje zakończona.

Przykład użycia pętli while:

```python
licznik = 0
while licznik < 5:
    print(licznik)
    licznik += 1
```

W powyższym kodzie pętla będzie działała tak długo, jak zmienna licznik jest mniejsza niż 5. W każdej iteracji, wartość licznik jest drukowana, a następnie zwiększana o 1. W efekcie, program wypisuje liczby od 0 do 4 włącznie.

Jest to podstawowe zastosowanie pętli while, ale można ją również używać w bardziej zaawansowanych scenariuszach, na przykład w połączeniu z instrukcjami `break` (do natychmiastowego wyjścia z pętli) i `continue` (do przerwania bieżącej iteracji i przejścia do następnej).

### Polecenia break i continue

Instrukcje sterujące, takie jak `break` i `continue`, pozwalają na bardziej skomplikowaną kontrolę przepływu w pętlach. Pomagają one odpowiednio przerwać działanie pętli lub pominąć pozostałą część bieżącej iteracji.

#### Instrukcja break

Instrukcja `break` kończy działanie bieżącej pętli i przenosi wykonanie do kodu umieszczonego bezpośrednio po niej. Jest szczególnie przydatna, gdy chcemy przerwać działanie pętli na podstawie pewnego warunku.

Przykład:

```python
for i in range(10):
    if i == 5:
        break
    print(i)
```

W powyższym kodzie, pętla for przebiega przez liczby od 0 do 9. Jednakże, gdy wartość i osiągnie 5, instrukcja break zostanie wywołana, przerwając działanie pętli. W efekcie, liczby od 0 do 4 zostaną wypisane na konsoli.

#### Instrukcja continue

Instrukcja `continue` pomija pozostałą część bieżącej iteracji pętli i przechodzi bezpośrednio do kolejnej iteracji. Może być używana, jeśli chcemy pominąć pewne instrukcje w bieżącej iteracji na podstawie pewnego warunku.

Przykład:

```python
for i in range(10):
    if i % 2 == 0:  # jeśli i jest liczbą parzystą
        continue
    print(i)
```

W tym przykładzie, pętla for iteruje przez liczby od 0 do 9. Gdy i jest liczbą parzystą, instrukcja continue jest wywołana, pomijając instrukcję print(i). Dzięki temu na konsoli zostaną wypisane tylko liczby nieparzyste, tj. 1, 3, 5, 7 oraz 9.

### Zagnieżdżone pętle

Pętle można również zagnieżdżać, co oznacza, że jedna pętla jest umieszczona wewnątrz innej. Jest to przydatne, gdy chcemy iterować przez wielowymiarowe struktury danych, takie jak listy list.

Przykład zagnieżdżonej pętli:

```python
for i in range(3):
    for j in range(3):
        print(f'i={i}, j={j}')
```

W powyższym przykładzie, pętla zewnętrzna `for i in range(3)` będzie wykonywana trzy razy, a dla każdej iteracji tej pętli, pętla wewnętrzna `for j in range(3)` również będzie wykonywana trzy razy. W efekcie, na konsoli zostanie wypisane dziewięć linii, pokazujących wszystkie możliwe kombinacje wartości i oraz j.


### Pętle zagnieżdżone

Zagnieżdżanie pętli polega na umieszczaniu jednej pętli wewnątrz innej, co pozwala na tworzenie bardziej złożonych struktur kontroli przepływu. W praktyce, iteracja pętli zewnętrznej powoduje wykonanie całej pętli wewnętrznej przed przejściem do następnej iteracji pętli zewnętrznej.

Kiedy zagnieżdżamy pętle, warto pamiętać o następujących zasadach:

1. Pętla zewnętrzna kontroluje "makro" iteracje, np. wiersze.
2. Pętla wewnętrzna kontroluje "mikro" iteracje, np. kolumny.

Przykład:

```python
for y in range(3):  # wiersze
    for x in range(4):  # kolumny
        print("(", y, ",", x, ")", end=" ")
    print()
```

W tym przykładzie, dla każdej iteracji pętli zewnętrznej, pętla wewnętrzna zostanie wykonana w całości. Wydrukowany zostanie układ współrzędnych dla prostokąta o wymiarach 3x4.

Aby lepiej zrozumieć działanie pętli zagnieżdżonych, przyjrzyjmy się w jaki sposób można je wykorzystać do generowania prostych wzorów graficznych:

#### Prostokąt

```python
for i in range(5):
    for j in range(5):
        print("*", end="")
    print()
```

Wynik:

```
*****
*****
*****
*****
*****
```

#### Trójkąt prostokątny

```python
for i in range(5):
    for j in range(i + 1):
        print("*", end="")
    print()
```

Wynik:

```
*
**
***
****
*****
```

#### Choinka

```python
for i in range(5):
    for j in range(5 - i - 1):  # Dla spacji
        print(" ", end="")
    for k in range(2 * i + 1):  # Dla gwiazdek
        print("*", end="")
    print()
```

Wynik:

```

    *
   ***
  *****
 *******
*********
```

### Zaawansowane zastosowanie pętli zagnieżdżonych

Pętle zagnieżdżone mogą być również używane do bardziej zaawansowanych operacji, takich jak przetwarzanie macierzy czy generowanie skomplikowanych wzorów. Poniżej przedstawiono kilka dodatkowych przykładów:

#### Macierz

```python
macierz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for wiersz in macierz:
    for element in wiersz:
        print(element, end=" ")
    print()
```

Wynik:

```
1 2 3
4 5 6
7 8 9
```

#### Tabliczka mnożenia

```python
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i * j:4}", end="")
    print()
```

Wynik:

```

   1   2   3   4   5   6   7   8   9  10
   2   4   6   8  10  12  14  16  18  20
   3   6   9  12  15  18  21  24  27  30
   4   8  12  16  20  24  28  32  36  40
   5  10  15  20  25  30  35  40  45  50
   6  12  18  24  30  36  42  48  54  60
   7  14  21  28  35  42  49  56  63  70
   8  16  24  32  40  48  56  64  72  80
   9  18  27  36  45  54  63  72  81  90
  10  20  30  40  50  60  70  80  90 100
```

#### Przeszukiwanie dwuwymiarowej listy

```python
macierz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

szukana_wartosc = 5
znaleziono = False

for wiersz in macierz:
    for element in wiersz:
        if element == szukana_wartosc:
            znaleziono = True
            break
    if znaleziono:
        break

if znaleziono:
    print(f"Znaleziono wartość {szukana_wartosc} w macierzy.")
else:
    print(f"Nie znaleziono wartości {szukana_wartosc} w macierzy.")
```

Pętle zagnieżdżone pozwalają na realizację wielu złożonych operacji i są kluczem do tworzenia bardziej zaawansowanych programów. Poprzez łączenie prostych pętli w złożone struktury, możemy przetwarzać dane w sposób efektywny i elastyczny.
