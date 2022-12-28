### Warunki

Typ logiczny (bool) może przyjmować jedną z dwóch wartości: <code>True</code> lub <code>False</code>. Typ logiczny ma istotne znaczenie dla instrukcji warunkowej.

Prosta zmienna typu logicznego:

    wiek = 18 # zmienna typu int
    warunek = wiek > 18 # zmienna typu bool
    
Oto tabela z porównaniami dostępnymi w języku Python:

| Symbol | Opis |
| ------ | ---- |
| >	| większy niż |
| >=	| większy lub równy |
| <	| mniejszy niż |
| <=	| mniejszy lub równy |
| ==	| równy |
| !=	| różny |

Początkujący programiści często mylą pojedynczy znak równości (<code>=</code>) z podwójnym znakiem równości (<code>==</code>).

- <code>x = 5</code> oznacza przypisanie wartości 5 do zmiennej x.
- <code>x == 5</code> oznacza sprawdzenie, czy zmienna x jest równa 5.

Instrukcja warunkowa (if-else) ma następującą postać:

    if warunek:
        kod
    else:
        kod

Część kodu umieszczona w pierwszym wcięciu po instrukcji warunkowej <code>if</code> zostanie wykonana jedynie, gdy warunek zostanie oceniony na prawdziwy. Gdy warunek nie jest spełniony, ta część kodu zostanie całkowicie pominięta, a zamiast niej wykonany zostanie kod umieszczony w drugim wcięciu (pod
instrukcjami sterującymi.

Operatory logiczne służą do łączenia warunków. W Pythonie mamy do dyspozycji trzy operatory logiczne: <code>and</code>, <code>or</code> i <code>not</code>:

* <code>and</code> – aby wyrażenie było prawdziwe, oba warunki muszą być prawdziwe.
* <code>or</code> – aby wyrażenie było prawdziwe, tylko jeden warunek musi być prawdziwy.
* <code>not</code> – zaprzeczenie wyrażenia.

Na przykład, wyrażenie <code>a != 0 and b == 5</code> będzie prawdziwe, jeśli oba warunki są spełnione, tzn. jeśli a jest różne od 0 i jednocześnie b jest równe 5.

Natomiast wyrażenie <code>x % 2 == 0 or x % 7 == 0</code> będzie prawdziwe, jeśli jeden z warunków jest spełniony, tzn. jeśli x jest podzielne przez 2 lub x jest podzielne przez 7.

Być może zastanawiasz się, co zostanie wypisane na konsoli w poniższym przykładzie:
    
    odpowiedz = "TAK"
    print(odpowiedz == "tak" or "TAK")

Wyjaśnienie: operator <code>or</code> zwraca pierwszą wartość prawdziwą, jeśli taka istnieje, w przeciwnym razie zwraca drugą wartość. W tym przypadku pierwszy warunek jest fałszywy, ale drugi jest prawdziwy (bo "TAK" jest różne od fałszu). Z tego powodu całe wyrażenie zwraca drugi warunek, czyli wartość "TAK".
