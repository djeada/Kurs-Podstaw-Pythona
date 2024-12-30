## Pętle

Pętle stanowią jeden z fundamentalnych elementów każdego języka programowania, umożliwiając wielokrotne wykonywanie wybranych instrukcji. Dzięki nim możemy powtarzać określone operacje na danych, co pozwala na znaczne uproszczenie i skrócenie kodu. W praktyce, bez pętli musielibyśmy wielokrotnie powtarzać te same fragmenty kodu, co prowadziłoby do niepotrzebnej redundancji i zwiększało ryzyko popełnienia błędów. 

Zasadniczo, pętle dzielimy na dwa główne rodzaje: pętle oparte na liczbie wykonywanych iteracji (np. `for`) oraz pętle, które działają tak długo, aż dany warunek przestanie być spełniony (np. `while`). Oba te podejścia mają swoje zastosowanie i pozwalają na pisanie bardziej elastycznego kodu, z łatwością dostosowującego się do różnych zadań, takich jak przeglądanie elementów listy, przetwarzanie plików, czy budowanie wielowymiarowych struktur danych.

Pętle w Pythonie wyróżniają się prostą i czytelną składnią, która sprzyja utrzymaniu czytelności kodu. Dodatkowo, poprzez użycie instrukcji takich jak `break` i `continue`, możemy z łatwością sterować przebiegiem wykonywania pętli, skracając ich działanie w odpowiednim momencie lub pomijając bieżącą iterację. W tej sekcji przyjrzymy się bliżej pętlom `for` i `while`, a także sposobom wykorzystywania ich w różnych zastosowaniach, w tym zagnieżdżaniu pętli i praktycznym przykładowi ich użycia w bardziej rozbudowanych operacjach.

### Pętla For

Pętla `for` służy do iteracji po elementach kolekcji (np. listy, krotki, słowniki, ciągi znaków) lub po sekwencji liczb generowanej przez funkcję `range()`. W codziennej pracy programisty jest to jedno z najczęściej używanych narzędzi, ponieważ iterowanie po listach czy słownikach to bardzo powszednia operacja w Pythonie. 

Z pętlą `for` nierozerwalnie wiąże się funkcja `range()`, która generuje sekwencję liczb wykorzystywaną do kontrolowania liczby iteracji. Dzięki niej można w prosty sposób określić, ile razy chcemy powtórzyć kod, lub też iterować od określonego punktu startowego do punktu końcowego, z ustalonym krokiem.

Podstawowa składnia pętli `for` wygląda następująco:

```python
for element in kolekcja:
    # kod do wykonania dla każdego elementu
```

Funkcja `range()` jest często używana w pętlach for, gdy chcemy wykonać blok kodu określoną liczbę razy. Może przyjmować różną liczbę argumentów:

| Sposób użycia           | Opis                                                                                     |
|-------------------------|------------------------------------------------------------------------------------------|
| `range(n)`              | Generuje sekwencję liczb od 0 do n-1.                                                    |
| `range(start, stop)`    | Generuje sekwencję liczb od `start` do `stop - 1`.                                       |
| `range(start, stop, krok)` | Generuje sekwencję liczb zaczynając od `start`, kończąc na `stop - 1`, zwiększając wartość o `krok` przy każdej iteracji. | 

W praktyce, pętla `for` w połączeniu z `range()` daje nam duże możliwości w zakresie automatyzacji powtarzalnych zadań. Możemy np. kilkukrotnie otwierać pliki, iterować po zbiorze indeksów lub tworzyć różnego rodzaju sekwencje danych do dalszych obliczeń. Dodatkowo, kiedy łączymy pętlę `for` z listami czy słownikami, mamy szybki wgląd w każdy element kolekcji, co sprawdza się doskonale przy analizie danych, filtrowaniu czy transformacji elementów.

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

Warto pamiętać, że pętla `for` w Pythonie może też służyć do iteracji po listach czy napisach bez użycia `range()`. Dzięki temu możemy np. przejść przez każdy znak w łańcuchu znaków lub każdy element listy, bezpośrednio operując na tych elementach.

### Pętla While

Pętla `while` w Pythonie umożliwia wielokrotne wykonanie bloku kodu, dopóki określony warunek jest prawdziwy. W przeciwieństwie do pętli `for`, która iteruje się przez znane wcześniej kolekcje danych, pętla `while` może być używana do tworzenia pętli, których liczba iteracji nie jest znana z góry. Jest to często stosowane przy zadaniach wymagających czekania na pewne zdarzenie (np. przy odpytywaniu zasobu sieciowego) albo wtedy, gdy nasza pętla powinna zakończyć się dopiero po spełnieniu pewnego nietrywialnego warunku.

Podstawowa składnia pętli `while` jest następująca:

```python
while warunek:
    # kod do wykonania
```

Każdy obieg pętli rozpoczyna się od sprawdzenia warunku. Jeśli warunek jest prawdziwy, blok kodu wewnątrz pętli jest wykonany. Po wykonaniu bloku, warunek jest ponownie sprawdzany, i jeśli nadal jest prawdziwy, pętla kontynuuje swoje działanie. Proces ten powtarza się, aż warunek stanie się fałszywy, wtedy pętla zostaje zakończona.

Ta konstrukcja jest niezwykle przydatna w sytuacjach, w których nie możemy z góry określić, ile razy chcemy wykonać nasz blok kodu — np. w przypadku pobierania danych z zewnętrznych źródeł, gdzie czekamy, aż pewna wartość osiągnie zadane kryterium. Warto jednak pamiętać o konieczności zmiany warunków w pętli (np. inkrementacji licznika lub modyfikacji danych), aby uniknąć nieskończonego działania programu.

Przykład użycia pętli while:

```python
licznik = 0
while licznik < 5:
    print(licznik)
    licznik += 1
```

W powyższym kodzie pętla będzie działała tak długo, jak zmienna `licznik` jest mniejsza niż 5. W każdej iteracji wartość `licznik` jest drukowana, a następnie zwiększana o 1. W efekcie, program wypisuje liczby od 0 do 4 włącznie.

Jest to podstawowe zastosowanie pętli while, ale można ją również używać w bardziej zaawansowanych scenariuszach, na przykład w połączeniu z instrukcjami `break` (do natychmiastowego wyjścia z pętli) i `continue` (do przerwania bieżącej iteracji i przejścia do następnej).

### Polecenia break i continue

Instrukcje sterujące, takie jak `break` i `continue`, pozwalają na bardziej skomplikowaną kontrolę przepływu w pętlach. Pomagają one odpowiednio przerwać działanie pętli lub pominąć pozostałą część bieżącej iteracji. To szczególnie przydatne narzędzia w sytuacjach, gdy musimy natychmiast zareagować na pewne warunki w trakcie działania pętli — np. gdy odnajdziemy poszukiwany element albo chcemy z jakiegoś powodu pominąć dane w konkretnej iteracji.

#### Instrukcja break

Instrukcja `break` kończy działanie bieżącej pętli i przenosi wykonanie do kodu umieszczonego bezpośrednio po niej. Jest szczególnie przydatna, gdy chcemy przerwać działanie pętli na podstawie pewnego warunku. Użycie `break` może znacząco skrócić czas wykonania programu, jeśli nie chcemy już analizować dalszej części danych.

Przykład:

```python
for i in range(10):
    if i == 5:
        break
    print(i)
```

W powyższym kodzie, pętla `for` przebiega przez liczby od 0 do 9. Jednakże, gdy wartość `i` osiągnie 5, instrukcja `break` zostanie wywołana, przerwając działanie pętli. W efekcie, liczby od 0 do 4 zostaną wypisane na konsoli, a pętla nie przechodzi do kolejnych wartości.

#### Instrukcja continue

Instrukcja `continue` pomija pozostałą część bieżącej iteracji pętli i przechodzi bezpośrednio do kolejnej iteracji. Może być używana, jeśli chcemy pominąć pewne instrukcje w bieżącej iteracji na podstawie pewnego warunku. Zamiast więc przerywać całe działanie pętli, przechodzimy do następnego obiegu.

Przykład:

```python
for i in range(10):
    if i % 2 == 0:  # jeśli i jest liczbą parzystą
        continue
    print(i)
```

W tym przykładzie, pętla `for` iteruje przez liczby od 0 do 9. Gdy `i` jest liczbą parzystą, instrukcja `continue` jest wywołana, pomijając instrukcję `print(i)`. Dzięki temu na konsoli zostaną wypisane tylko liczby nieparzyste, tj. 1, 3, 5, 7 oraz 9.

### Zagnieżdżone pętle

Pętle można również zagnieżdżać, co oznacza, że jedna pętla jest umieszczona wewnątrz innej. Jest to przydatne, gdy chcemy iterować przez wielowymiarowe struktury danych, takie jak listy list. Zagnieżdżanie pętli pozwala również na budowanie bardziej złożonych algorytmów, gdzie dla każdego elementu zewnętrznej sekwencji przechodzimy przez całą sekwencję wewnętrzną.

Warto zwrócić uwagę, że zagnieżdżone pętle mogą znacząco zwiększyć złożoność obliczeniową. Jeśli na przykład zewnętrzna pętla wykonuje się N razy, a wewnętrzna M razy, łączna liczba iteracji może sięgnąć N*M, co dla dużych wartości N i M może być nieefektywne. Jednak w wielu przypadkach, zwłaszcza przy przetwarzaniu i analizie bardziej złożonych struktur, zagnieżdżone pętle są nieodzownym narzędziem.

Poniższy przykład obrazuje podstawowe wykorzystanie zagnieżdżenia pętli:

```python
for i in range(3):
    for j in range(3):
        print(f'i={i}, j={j}')
```

W powyższym przykładzie, pętla zewnętrzna `for i in range(3)` będzie wykonywana trzy razy, a dla każdej iteracji tej pętli, pętla wewnętrzna `for j in range(3)` również będzie wykonywana trzy razy. W efekcie, na konsoli zostanie wypisane dziewięć linii, pokazujących wszystkie możliwe kombinacje wartości `i` oraz `j`.

### Pętle zagnieżdżone

Zagnieżdżanie pętli polega na umieszczaniu jednej pętli wewnątrz innej, co pozwala na tworzenie bardziej złożonych struktur kontroli przepływu. W praktyce, iteracja pętli zewnętrznej powoduje wykonanie całej pętli wewnętrznej przed przejściem do następnej iteracji pętli zewnętrznej.

Kiedy zagnieżdżamy pętle, warto pamiętać o następujących zasadach:

1. Pętla zewnętrzna kontroluje "makro" iteracje, np. wiersze.
2. Pętla wewnętrzna kontroluje "mikro" iteracje, np. kolumny.

Zarządzanie zagnieżdżonymi pętlami staje się szczególnie istotne w sytuacjach, gdy mamy do czynienia z danymi w formie tablic, macierzy czy różnego typu tabel. Dzięki ich wykorzystaniu, łatwiej możemy manipulować strukturami wielowymiarowymi lub generować różnego rodzaju wzorce (np. kształty z gwiazdek, tabliczki mnożenia, tabele z danymi itp.).

Przykład:

```python
for y in range(3):  # wiersze
    for x in range(4):  # kolumny
        print("(", y, ",", x, ")", end=" ")
    print()
```

W tym przykładzie, dla każdej iteracji pętli zewnętrznej, pętla wewnętrzna zostanie wykonana w całości. Wydrukowany zostanie układ współrzędnych dla prostokąta o wymiarach 3x4.

Aby lepiej zrozumieć działanie pętli zagnieżdżonych, przyjrzyjmy się, w jaki sposób można je wykorzystać do generowania prostych wzorów graficznych:

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

W tym przykładzie mamy dwie pętle `for`. Zewnętrzna pętla (`for i in range(5)`) odpowiada za liczbę wierszy, które zostaną wydrukowane. Dla każdego przebiegu tej pętli wewnętrzna pętla (`for j in range(5)`) drukuje pięć gwiazdek w jednym wierszu, nie przechodząc do nowej linii dzięki `end=""`. Po zakończeniu wewnętrznej pętli następuje `print()`, który przeskakuje do nowej linii, co tworzy kwadratowy kształt z gwiazdek.

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

Tutaj zewnętrzna pętla kontroluje liczbę wierszy, a każda kolejna iteracja dodaje jedną gwiazdkę więcej niż poprzednia. Wewnętrzna pętla (`for j in range(i + 1)`) drukuje gwiazdki, zaczynając od jednej gwiazdki i zwiększając ich liczbę w kolejnych wierszach. Takie działanie tworzy trójkątny wzór.

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

Aby utworzyć kształt przypominający choinkę, używamy dwóch pętli zagnieżdżonych dla każdego wiersza. Pierwsza pętla (`for j in range(5 - i - 1)`) generuje odpowiednią liczbę spacji, aby wyrównać wzór pośrodku. Druga pętla (`for k in range(2 * i + 1)`) tworzy gwiazdki, które składają się na kolejne poziomy choinki, zwiększając ich liczbę w każdym kolejnym wierszu.

Generowanie takich wzorów za pomocą zagnieżdżonych pętli to świetny sposób na naukę planowania struktury kodu oraz logicznego myślenia o problemach. Każdy dodatkowy poziom komplikacji (np. kolejne pętle) pozwala nam rozwiązywać coraz trudniejsze zadania związane z wizualizacją czy obróbką danych.

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

W tym przykładzie zagnieżdżone pętle są używane do przejścia przez dwuwymiarową listę, czyli macierz. Zewnętrzna pętla przechodzi przez każdy wiersz w macierzy, a wewnętrzna pętla wypisuje każdy element w wierszu. Dzięki `print(element, end=" ")` elementy są wypisywane w jednym wierszu, a `print()` po zakończeniu każdego wiersza tworzy nową linię.

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

Powyższy kod generuje tabliczkę mnożenia za pomocą zagnieżdżonych pętli. Zewnętrzna pętla `for i in range(1, 11)` odpowiada za wiersze, a wewnętrzna pętla `for j in range(1, 11)` generuje wartości dla poszczególnych kolumn, mnożąc `i * j`. Dzięki `f"{i * j:4}"` każda liczba jest odpowiednio formatowana, aby zachować równy odstęp między kolumnami.

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

W tym przykładzie, zagnieżdżone pętle są używane do przeszukiwania dwuwymiarowej listy (`macierz`). Zewnętrzna pętla przechodzi przez każdy wiersz, a wewnętrzna pętla sprawdza każdy element w wierszu, porównując go z `szukana_wartosc`. Jeśli element jest równy szukanej wartości, ustawiamy `znaleziono = True` i przerywamy dalsze przeszukiwanie. Na końcu program informuje, czy wartość została znaleziona w macierzy.
