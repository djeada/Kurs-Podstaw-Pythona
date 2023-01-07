### Pętle

Pętle wraz z instrukcjami warunkowymi są podstawą wszystkich języków programowania. Pętle pozwalają na wielokrotne wykonanie pojedynczej instrukcji lub całego bloku instrukcji. Oprócz bloku instrukcji, każda pętla ma również warunek zakończenia. Pętla powtarza blok instrukcji, dopóki warunek kończący pętlę nie zostanie spełniony. W Pythonie mamy dwie pętle: <code>For</code> i <code>While</code>.

#### For
Pętla <code>For</code> umożliwia wielokrotne wykonanie bloku instrukcji dla każdego elementu z danej kolekcji. Kolekcją może być np. lista, zbiór lub krotka. W przypadku pętli <code>For</code> mamy pewność, że blok instrukcji zostanie wykonany określoną ilość razy, równą liczbie elementów w kolekcji. Pętla <code>For</code> ogólnie ma postać:

```python
    for element in kolekcja: 
        kod
```

Na początek do tworzenia pętli będziemy używać funkcji range(). Funkcja ta może przyjmować jeden, dwa lub trzy parametry.

1. <code>range(10)</code> tworzy ciąg (0, 1, 2, 3, 4, 5, 6, 7, 8, 9), więc pętla: <code>for x in range(10)</code> zostanie wykonana 10 razy.
1. <code>range(5, 12)</code> tworzy ciąg (5, 6, 7, 8, 9, 10, 11), więc pętla: <code>for x in range(5, 12)</code> zostanie wykonana 7 razy.
1. <code>range(0, 50, 10)</code> tworzy ciąg (0, 10, 20, 30, 40), więc pętla: <code>for x in range(0, 50, 10)</code> zostanie wykonana 5 razy.

Przykład użycia pętli <code>For</code> z listą:

```python
dni_tygodnia = ['Poniedziałek', 'Wtorek', 'Środa', 'Czwartek', 'Piątek', 'Sobota', 'Niedziela']
for dzien in dni_tygodnia:
    print(dzien)
```

Wynikiem wykonania powyższego kodu będzie wypisanie na konsoli nazw wszystkich dni tygodnia.

#### While

Pętla <code>While</code> jest podobna w działaniu do pętli <code>For</code>, ale istnieją również istotne różnice między obiema konstrukcjami. W przypadku pętli <code>While</code> warunek zakończenia pętli jest sprawdzane przed każdym przejściem do kolejnej iteracji. Jeśli warunek nie jest spełniony, pętla zostaje zakończona. Dzięki temu pętla <code>While</code> może być używana do wykonywania pewnych instrukcji w nieskończoność (jeśli warunek kończący pętlę zawsze jest prawdziwy). 

Pętla <code>While</code> ma postać:

```python
while warunek konczacy petle: 
        kod
```

Poniżej przedstawiony został prosty przykład użycia pętli <code>While</code>:

```python
licznik = 0
while licznik < 5:
    print(licznik)
    licznik += 1
```

W powyższym przykładzie pętla <code>While</code> będzie wykonywana do momentu, aż zmienna licznik będzie mniejsza od 5. W każdym obiegu pętli wyświetlana jest aktualna wartość zmiennej licznik, a następnie jej wartość zostaje zwiększona o 1.

W rezultacie, na konsoli zostaną wyświetlone kolejno liczby od 0 do 4.

#### Polecenia break i continue

Instrukcja <code>break</code> służy do natychmiastowego przerwania działania pętli. Jeśli jest ona wywołana wewnątrz pętli, natychmiast przechodzi do kodu znajdującego się po pętli. Może być ona używana w połączeniu z instrukcjami warunkowymi, aby natychmiastowo zakończyć działanie pętli.

Przykład:

```python
for i in range(10):
    if i == 5:
        break
    print(i)
```

W tym przykładzie pętla będzie wykonywana dla wartości zmiennej *i* od 0 do 4, a następnie zostanie przerwana przez instrukcję <code>break</code>.

Instrukcja <code>continue</code> jest używana w pętlach i powoduje przejście do następnego obiegu pętli. Wszystkie instrukcje umieszczone poniżej instrukcji <code>continue</code> w bloku pętli nie zostaną wykonane po jej wywołaniu. Przykład użycia instrukcji <code>continue</code>:

```python
for i in range(10):
    if i % 2 == 0:  # jeśli i jest podzielne przez 2
        continue  # przejdź do następnego obiegu pętli
    print(i)  # wypisz i
```

W powyższym przykładzie pętla zostanie wykonana dla wszystkich liczb z zakresu od 0 do 9, ale zostaną one wyświetlone jedynie w przypadku, gdy są nieparzyste. W rezultacie na konsoli zostaną wypisane liczby: 1, 3, 5, 7, 9.

#### Pętle zagnieżdżone

Podobnie jak możemy zagnieżdżać instrukcje warunkowe, możemy również zagnieżdżać pętle. Pętle zagnieżdżone to pętle znajdujące się w ciele innych pętli. 

Istnieją dwie zasady zagnieżdżania pętli:

1. pętla zewnętrzna pilnuje wysokości,
1. pętla wewnętrzna pilnuje szerokości.

```python
for y in range(10): # wysokosc
    for x in range(5): # szerokosc
        kod
```

Pętla zewnętrzna ustawi nas w odpowiednim rzędzie, a pętla wewnętrzna na odpowiednim miejscu w danym rzędzie. Przykładowo, jeśli idziemy do sali kinowej i nasz bilet mówi, że przysługuje nam miejsce numer 5 w rzędzie numer 2, pętle zewnętrzna ustawi nas w odpowiednim rzędzie, a pętla wewnętrzna na odpowiednim miejscu.

W celu lepszego zobrazowania działania takiej konstrukcji posłużymy się graficznymi przykładami i będziemy wypisywać na konsoli różne kształty. Przykład zagnieżdżonej pętli z kształtami może być zapisany w następujący sposób:

```python
for i in range(5):
    for j in range(5):
        print("*", end="")
    print()
```

W wyniku wykonania tego kodu zostanie wypisany na konsoli prostokąt z gwiazdek:

```
*****
*****
*****
*****
*****
```

Możemy również użyć zagnieżdżonych pętli, aby narysować bardziej skomplikowane kształty, takie jak trójkąty lub choinkę.

```python
for i in range(5):
    for j in range(i+1):
        print("*", end="")
    print()
```

W wyniku wykonania tego kodu zostanie wypisany na konsoli trójkąt z gwiazdek:

```
*
**
***
****
*****
```

