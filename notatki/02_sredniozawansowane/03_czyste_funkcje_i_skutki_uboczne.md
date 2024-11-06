## Czyste i Nieczyste Funkcje oraz Mutowalne i Niemutowalne Obiekty

Czyste funkcje i niemutowalne obiekty pomagają tworzyć bardziej przewidywalne, łatwe do testowania i debugowania oprogramowanie, co redukuje ryzyko błędów i ułatwia utrzymanie kodu. Zrozumienie efektów ubocznych pozwala programistom unikać nieprzewidzianych problemów, które mogą wynikać z niezamierzonych zmian stanu. Natomiast wiedza o mutowalnych i niemutowalnych obiektach pomaga zarządzać danymi w sposób efektywny i bezpieczny, szczególnie w kontekście programowania wielowątkowego i współbieżności.

### Czyste i nieczyste funkcje

**Czyste funkcje** to funkcje, które zawsze zwracają ten sam wynik dla tych samych argumentów i nie mają efektów ubocznych. Oznacza to, że ich wynik jest deterministyczny, a ich zachowanie jest przewidywalne. Dzięki temu są one łatwe do testowania, debugowania oraz mogą być bezpiecznie wykonywane równolegle. Przykłady czystych funkcji to większość funkcji matematycznych, które przekształcają dane bez ich modyfikowania.

**Nieczyste funkcje** mogą zwracać różne wyniki dla tych samych argumentów lub mieć efekty uboczne, takie jak modyfikowanie stanu programu, operacje wejścia/wyjścia (I/O) czy zmiany globalnych zmiennych. Efekty uboczne sprawiają, że nieczyste funkcje są trudniejsze do testowania i debugowania. Przykłady nieczystych funkcji to operacje na plikach, funkcje generujące losowe liczby czy funkcje modyfikujące globalne zmienne.

#### Skutki uboczne w programowaniu

Skutki uboczne w programowaniu odnoszą się do działań funkcji lub metody, które wpływają na stan zewnętrznego świata – czyli na coś poza jej lokalnym zakresem.

Typowe skutki uboczne obejmują:

- Modyfikacje plików.
- Zmiany w bazach danych.
- Wysyłanie informacji przez sieć.
- Modyfikacje globalnych zmiennych.
- Wydruk na ekranie lub w innych urządzeniach wyjścia.
- Zmiana stanu aplikacji lub komponentów zewnętrznych.

#### Czyste funkcje w kontekście skutków ubocznych

Czyste funkcje, inaczej nazywane funkcjami czysto matematycznymi, są pozbawione skutków ubocznych. Ich wynik jest wyłącznie determinowany przez argumenty, które do nich wprowadzamy, a nie przez jakiekolwiek zewnętrzne stany.

#### Przykłady czystych funkcji

I. Funkcja obliczająca pole trójkąta na podstawie jego boków. Niezależnie od kontekstu zawsze da taki sam wynik dla tych samych argumentów.

```python
def pole_trojkata(podstawa, wysokosc):
    return 0.5 * podstawa * wysokosc
```
II. Funkcja zwracająca iloczyn elementów listy. Jej wynik zależy wyłącznie od zawartości listy.

```python
def iloczyn_listy(lista):
    wynik = 1
    for element w lista:
        wynik *= element
    return wynik
```

III. Funkcja znajdująca największy element w liście. Działa na podstawie dostarczonych danych.

```python
def max_element(lista):
    return max(lista)
```

IV. Funkcja generująca nową listę zawierającą tylko liczby parzyste z danej listy.

```python
def filtruj_parzyste(lista):
    return [element for element w lista jeśli element % 2 == 0]
```

V. Funkcja tworząca nowy słownik z wybranymi kluczami z oryginalnego słownika.

```python
def filtruj_slownik(slownik, klucze):
    return {klucz: slownik[klucz] for klucz w klucze jeśli klucz w slownik}
```

VI. Funkcja konwertująca ciąg znaków na wielkie litery.

```python
def na_wielkie_litery(napis):
    return napis.upper()
```

#### Przykłady nieczystych funkcji

I. Funkcja zapisująca dane do pliku. Może powodować skutki uboczne w postaci zmian na dysku.

```python
def zapisz_do_pliku(nazwa_pliku, dane):
    with open(nazwa_pliku, 'w') as plik:
        plik.write(dane)
```

II. Funkcja generująca losowe liczby. Wynik zależy od stanu generatora liczb losowych.

```python
import random
def losowa_liczba():
    return random.randint(1, 100)
```

III. Funkcja modyfikująca globalną zmienną. Wpływa na stan programu poza lokalnym zakresem funkcji.

```python
globalna_zmienna = 0

def modyfikuj_globalna():
    global globalna_zmienna
    globalna_zmienna += 1
```

IV. Funkcja wysyłająca dane przez sieć. Może wpływać na zewnętrzne systemy i jest zależna od stanu sieci.

```python
import requests

def wyslij_zapytanie(url, dane):
    odpowiedz = requests.post(url, json=dane)
    return odpowiedz.status_code
```

#### Korzyści stosowania czystych funkcji

1. Jednym z głównych atutów jest **testowalność**, ponieważ funkcje, które nie mają zewnętrznych zależności ani stanów, są znacznie łatwiejsze do przetestowania.
2. Dzięki temu, że funkcje nie mają skutków ubocznych, możemy być pewni, że robią dokładnie to, co jest określone w ich definicji, co poprawia **czytelność**.
3. Funkcje te charakteryzują się również dużą **przewidywalnością**, ponieważ zawsze zwracają ten sam wynik dla tych samych danych wejściowych.
4. **Łatwiejsze równoczesne wykonanie** to kolejna zaleta, ponieważ brak skutków ubocznych umożliwia bezproblemowe uruchamianie kodu równolegle.
5. Dodatkowo, funkcje bez zewnętrznych zależności są bardziej uniwersalne i można je łatwo ponownie używać w różnych miejscach, co zwiększa **możliwość ponownego użycia**.

Chociaż czyste funkcje mogą korzystać z obiektów mutowalnych jako swoich argumentów, nie modyfikują one tych obiektów. Zamiast tego, jeśli jest potrzeba "zmiany" obiektu, czysta funkcja zwróci nowy obiekt z pożądanymi zmianami.

#### Podsumowanie

| Aspekt                  | Czyste funkcje                     | Nieczyste funkcje               |
|-------------------------|------------------------------------|---------------------------------|
| Definicja               | Funkcje, które zawsze zwracają ten sam wynik dla tych samych argumentów i nie mają efektów ubocznych. | Funkcje, które mogą zwracać różne wyniki dla tych samych argumentów lub mają efekty uboczne. |
| Efekty uboczne          | Brak                               | Mogą modyfikować stan programu lub mieć efekty uboczne (np. zapis do pliku, modyfikacja globalnych zmiennych). |
| Determinizm             | Deterministyczne                   | Niedeterministyczne             |
| Testowalność            | Łatwe do testowania                | Trudniejsze do testowania z powodu efektów ubocznych. |
| Przykłady               | Funkcje matematyczne (np. obliczanie wartości funkcji), konwersja danych | Funkcje operujące na plikach, wprowadzanie/wyprowadzanie danych (I/O), modyfikacja zmiennych globalnych |
| Korzyści                | Przewidywalność, łatwość debugowania i testowania, możliwość równoległego wykonywania | Elastyczność w interakcji z systemem operacyjnym, możliwość wykonywania operacji I/O |

### Mutowalność vs Niemutowalność

W programowaniu mutowalność odnosi się do zdolności obiektu do zmiany jego stanu po jego utworzeniu. Niemutowalność to cecha obiektu, która nie pozwala na modyfikację jego stanu po utworzeniu.

#### Mutowalne obiekty

**Mutowalne obiekty** to obiekty, które można zmieniać po ich utworzeniu. Oznacza to, że ich zawartość lub stan mogą być modyfikowane w miejscu. Przykłady mutowalnych obiektów to listy, słowniki, zbiory oraz `bytearray`. Mutowalne obiekty są elastyczne i wygodne do pracy z danymi, które wymagają częstych zmian, ale mogą prowadzić do błędów, jeśli nie są odpowiednio zarządzane.

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

Mutowalne obiekty pozwalają na efektywne zarządzanie stanem danych w aplikacjach, ale mogą wprowadzać złożoność, gdy wiele części programu modyfikuje te same dane.

#### Niemutowalne obiekty

**Niemutowalne obiekty** to obiekty, których nie można zmieniać po ich utworzeniu. Każda próba zmiany takiego obiektu prowadzi do utworzenia nowego obiektu. Przykłady niemutowalnych obiektów to krotki, stringi, liczby (int, float), boolean oraz `frozenset`. Niemutowalne obiekty są bezpieczne do użycia w środowiskach wielowątkowych, ponieważ ich stan nie może być zmieniony po utworzeniu, co czyni je bardziej przewidywalnymi i mniej podatnymi na błędy.

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

#### Korzyści z używania niemutowalnych obiektów

1. Stan **niemutowalnych obiektów** nie może się zmieniać po ich utworzeniu, co sprawia, że są one **bezpieczne w środowiskach wielowątkowych**, ponieważ brak zmian eliminuje ryzyko konfliktów między wątkami.
2. Dzięki przewidywalnemu stanowi niemutowalnych obiektów, **debugowanie** staje się prostsze, gdyż łatwiej jest śledzić potencjalne błędy.
3. **Większa czytelność kodu** wynika z faktu, że niemutowalne obiekty nie zmieniają swojego stanu w różnych częściach programu, co ułatwia zrozumienie logiki działania kodu.
4. Dodatkowo, **optymalizacja pamięci** jest możliwa, ponieważ niemutowalne obiekty mogą być współdzielone w wielu miejscach programu bez obawy o ich modyfikację.

#### Podsumowanie

W Pythonie typy danych można podzielić na dwie główne kategorie: mutowalne i niemutowalne. Oto tabela podsumowująca kluczowe różnice między obiektami mutowalnymi i niemutowalnymi.

| Aspekt                  | Obiekty mutowalne                  | Obiekty niemutowalne            |
|-------------------------|------------------------------------|---------------------------------|
| Definicja               | Obiekty, które można modyfikować po utworzeniu. | Obiekty, których nie można modyfikować po utworzeniu. |
| Przykłady               | Lista, Słownik, Zbiór, Bytearray   | Krotka, String, Integer, Float, Boolean, Frozenset |
| Przydział pamięci       | Może zmieniać adres pamięci w przypadku zmiany rozmiaru. | Stały adres pamięci.             |
| Metody                  | Metody, które zmieniają obiekt (np. append, remove). | Metody, które zwracają nowy obiekt (np. konkatenacja stringów). |
| Wydajność               | Zwykle wolniejsze z powodu potencjalnej potrzeby zmiany rozmiaru i ponownego przydziału pamięci. | Szybsze, ponieważ rozmiar jest stały i nie ma potrzeby ponownego przydziału pamięci. |
| Przypadki użycia        | Odpowiednie dla zbiorów danych, które muszą być często zmieniane. | Odpowiednie dla wartości, które powinny pozostać niezmienne przez cały program. |
| Przykłady użycia        | `list1 = [1, 2, 3]`<br>`list1.append(4)` | `tuple1 = (1, 2, 3)`<br>`tuple2 = tuple1 + (4,)` |
