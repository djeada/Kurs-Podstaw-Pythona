## Czyste funkcje i skutki uboczne

Czyste funkcje są jednym z fundamentów programowania funkcyjnego. W przeciwieństwie do funkcji powodujących skutki uboczne, czyste funkcje są deterministyczne i nie wpływają na środowisko poza ich zasięgiem.

### Skutki uboczne w programowaniu

Skutki uboczne w programowaniu odnoszą się do działań funkcji lub metody, które wpływają na stan zewnętrznego świata – czyli na coś poza jej lokalnym zakresem.

Typowe skutki uboczne obejmują:

* Modyfikacje plików.
* Zmiany w bazach danych.
* Wysyłanie informacji przez sieć.
* Modyfikacje globalnych zmiennych.
* Wydruk na ekranie lub w innych urządzeniach wyjścia.
* Zmiana stanu aplikacji lub komponentów zewnętrznych.

### Czyste funkcje w kontekście skutków ubocznych:

Czyste funkcje, inaczej nazywane funkcjami czysto matematycznymi, są pozbawione skutków ubocznych. Ich wynik jest wyłącznie determinowany przez argumenty, które do nich wprowadzamy, a nie przez jakiekolwiek zewnętrzne stany.

### Przykłady czystych funkcji:

1. **Funkcja obliczająca pole trójkąta** na podstawie jego boków. Niezależnie od kontekstu zawsze da taki sam wynik dla tych samych argumentów.
2. **Funkcja zwracająca iloczyn elementów listy**. Jej wynik zależy wyłącznie od zawartości listy.
3. **Funkcja znajdująca największy element w liście**. Działa na podstawie dostarczonych danych.
4. **Funkcja generująca nową listę** zawierającą tylko liczby parzyste z danej listy.
5. **Funkcja tworząca nowy słownik** z wybranymi kluczami z oryginalnego słownika.
6. **Funkcja konwertująca ciąg znaków na wielkie litery**. 

### Korzyści stosowania czystych funkcji:

1. **Testowalność**: łatwość w testowaniu wynika z braku zewnętrznych zależności czy stanów.
2. **Czytelność**: skoro nie ma skutków ubocznych, możemy być pewni, że funkcja robi dokładnie to, co jest opisane w jej definicji.
3. **Przewidywalność**: zawsze zwraca taki sam wynik dla tych samych danych wejściowych.
4. **Łatwiejsze równoczesne wykonanie**: brak skutków ubocznych ułatwia równoległe wykonywanie kodu.
5. **Możliwość ponownego użycia**: brak zewnętrznych zależności sprawia, że łatwo jest używać funkcji w różnych miejscach.

Chociaż czyste funkcje mogą korzystać z obiektów mutowalnych jako swoich argumentów, nie modyfikują one tych obiektów. Zamiast tego, jeśli jest potrzeba "zmiany" obiektu, czysta funkcja zwróci nowy obiekt z pożądanymi zmianami.

## Mutowalność vs Niemutowalność

W programowaniu mutowalność odnosi się do zdolności obiektu do zmiany jego stanu po jego utworzeniu. Niemutowalność to cecha obiektu, która nie pozwala na modyfikację jego stanu po utworzeniu.

### Mutowalne obiekty

W Pythonie obiekty takie jak listy, słowniki i zbiory są mutowalne.

```python
# Przykład z listą:
lista = [1, 2, 3]
lista.append(4)
print(lista)  # [1, 2, 3, 4]

# Przykład ze słownikiem:
slownik = {'klucz': 'wartosc'}
slownik['nowy_klucz'] = 'nowa_wartosc'
print(slownik)  # {'klucz': 'wartosc', 'nowy_klucz': 'nowa_wartosc'}

# Przykład ze zbiorem:
zbior = {1, 2, 3}
zbior.add(4)
print(zbior)  # {1, 2, 3, 4}
```

### Niemutowalne obiekty

Niemutowalne obiekty w Pythonie to m.in. liczby, napisy i krotki.

```python
# Przykład z liczbą:
liczba = 5
liczba = 6  # Tutaj dokonujemy przypisania nowej wartości do zmiennej, ale nie modyfikujemy samej liczby

# Przykład z napisem:
napis = 'napis'
# napis[1] = 'a'  # Błąd! Napisów nie można modyfikować.

# Przykład z krotką:
krotka = (1, 2, 3)
# krotka[1] = 4  # Błąd! Krotek nie można modyfikować.
```

Korzystanie z niemutowalnych obiektów ma wiele korzyści, takich jak zwiększona czytelność, bezpieczeństwo i łatwość w debugowaniu. Jednak obiekty mutowalne są nieuniknione w wielu przypadkach, gdy potrzebujemy zmieniać stan obiektu w czasie. Kluczem jest rozumienie tych różnic i stosowanie odpowiedniego typu obiektu w odpowiednich sytuacjach.


