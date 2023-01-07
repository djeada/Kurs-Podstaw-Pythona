## Testy

Testy to mechanizm służący do sprawdzenia poprawności działania oprogramowania. Są one szczególnie ważne, ponieważ bugi (błędy) w oprogramowaniu mogą prowadzić do poważnych problemów i strat. Dlatego ważne jest, aby testować oprogramowanie tak dokładnie, jak to tylko możliwe, aby zmniejszyć ryzyko wystąpienia bugów w wersji produkcyjnej.

Istnieje wiele sposobów klasyfikacji testów, ale najczęściej stosuje się podział na:

1. Testy jednostkowe - sprawdzają działanie pojedynczych funkcji lub modułów kodu
2. Testy integracyjne - sprawdzają działanie kilku modułów lub całego systemu, ale nie sprawdzają interakcji z zewnętrznymi systemami
3. Testy systemowe - sprawdzają działanie całego systemu z uwzględnieniem wszystkich jego interakcji z zewnętrznymi systemami

## Przykłady bugów

* W 2002 roku rakieta Ariane 5 ECA uległa samozniszczeniu kilka sekund po starcie. Awarii towarzyszył błąd w systemie sterującym chłodzeniem.
* W lutym 1991 roku niedokładność przy zaokrąglaniu spowodowała, że systemy antyrakietowe nie zadziałały w należyty sposób, a w wyniku ostrzału zginęło 28 amerykańskich żołnierzy. Więcej informacji można znaleźć pod tym <a href="https://www-users.cse.umn.edu/~arnold/455.f96/disasters.html">linkiem</a>.

## Proces testowania

Ogólne kroki dla wszystkich testów:

1. Zdefiniuj cel testu i spodziewane wyniki.
1. Przygotuj dane wejściowe i/lub konfigurację programu.
1. Wywołaj funkcję lub uruchom program z podanymi danymi wejściowymi.
1. Porównaj otrzymany wynik ze spodziewanym.
1. Wyświetl wynik testu i ewentualne znalezione błędy.

## Testy jednostkowe

* Testy jednostkowe są rodzajem testów, które sprawdzają pojedyncze funkcje lub fragmenty kodu.
* Celem tych testów jest zapewnienie, że pojedyncze elementy kodu działają prawidłowo i zgodnie z oczekiwaniami.
* Testy jednostkowe powinny być szybkie w wykonaniu, dzięki czemu programista otrzymuje natychmiastową informację zwrotną o poprawności swojej implementacji.
* Najlepsze testy jednostkowe to takie, które można napisać nie znając implementacji kodu produkcyjnego.
* Testy jednostkowe są szczególnie przydatne w regresji, czyli sprawdzeniu, czy zmiany w kodzie nie wpłynęły negatywnie na już działające elementy.

## Przykład Testu

Załóżmy, że w kodzie produkcyjnym znajduje się funkcja `znajdz_klucz(lista, klucz)` zwracająca indeks pierwszego wystąpienia klucza w liście.
Aby przetestować funkcję `znajdz_klucz(lista, klucz)` możemy napisać następujące testy:

1. Sprawdzenie dla podstawowego zachowania. W tym przypadku sprawdzamy czy funkcja zwraca oczekiwany indeks dla przypadku, gdy klucz znajduje się w liście.
1. Sprawdzenie dla skrajnego przypadku. W tym przypadku sprawdzamy czy funkcja zwraca oczekiwany wynik, gdy klucz nie znajduje się w liście.

Przykłady testów:

```python
def test_find_key():
    assert find_key([1,2,3,4,5], 3) == 2
    assert find_key([1,2,3,4,5], 6) == -1
```

## Pokrycie kodu produkcyjnego (code coverage)

Pokrycie kodu produkcyjnego to miernik tego, jaki procent kodu został wykonany podczas testów. Może być używane jako wskaźnik, czy testy są wystarczające, czy też powinno się dodać nowe testy.

Przykład:

```
#1# def fun(a, b):
#2#   a += 1
#3#   b += 2
#4#   if a + b > 22:
#5#   a += 1
#6#   return a + b
```

Jeśli testujemy `fun(a,b)` z danymi wejściowymi, które sprawiają, że warunek w linii `#4#` nie jest spełniony, pokrycie kodu nie będzie wynosić 100%. Jeśli dodamy testy z danymi wejściowymi, które sprawiają, że warunek jest spełniony, pokrycie kodu wzrośnie i zbliży się do 100%.

## Czy zielone testy są gwarancją poprawności?

Zielone testy (czyli testy, które przechodzą pomyślnie) to bardzo ważna część procesu testowania, ale samo ich przejście nie gwarantuje, że nasz program jest wolny od błędów. Dlaczego?

* Możemy nie przetestować wszystkich możliwych przypadków. Zielone testy są gwarancją poprawności dla przypadków, które zostały przetestowane, ale nie oznacza to, że program działa poprawnie dla wszystkich przypadków.
* Być może dane które używamy w testach są zbyt małe i system zawodzi dopiero gdy zostanie obciążony zacznie większymi danymi.
* Bug w systemie Klarna doprowadził do wycieku danych użytkowników, mimo że 100% testów było zielonych. Więcej możesz dowiedzieć się pod tym <a href="https://www.klarna.com/se/blogg/detailed-incident-report-incorrect-cache-configuration-leading-to-klarna-app-exposing-personal-information/">linkiem</a>.

## TDD 

Test Driven Development (TDD) to sposób pisania kodu oprogramowania, w którym najpierw tworzymy testy, a potem implementujemy kod produkcyjny.

### Kroki w procesie TDD

1. Napisz test, który opisuje nową funkcjonalność, którą chcesz dodać do programu.
1. Uruchom test. Powinien zostać oznaczony jako niezaliczony, ponieważ nie została jeszcze napisana odpowiednia implementacja.
1. Napisz najmniejszy kod produkcyjny, który spowoduje, że test zostanie zaliczony.
1. Uruchom wszystkie testy. Jeśli wszystkie są zaliczane, oznacza to, że nowa funkcjonalność działa poprawnie i można przejść do kolejnego kroku. Jeśli któryś test jest niezaliczony, należy go poprawić.
1. Ulepsz kod produkcyjny, tak aby był czytelniejszy i bardziej efektywny. Uruchom ponownie wszystkie testy, aby upewnić się, że zmiany nie wpłynęły negatywnie na poprawność działania.

### Zalety

* Zmusza programistę do myślenia o tym, jak będzie testować kod.
* Pomaga wcześnie wykrywać bugi.
* Chroni przed pisaniem kodu produkcyjnego niespełniającego swojego zdania.
* Pokazuje, co robi testowany fragment kodu (efekty są widoczne).
* Umożliwia testowanie regresyjne.

### Wady

* Zwiększa złożoność projektu i czas potrzebny na jego rozwój.
* Może być trudne do zastosowania w projektach, które są bardzo złożone i mają dużo zależności.
* Zmiany są kosztowniejsze do wprowadzenia (musisz zmienić zarówno kod produkcyjny, jak i testy).
* Nadgorliwi wyznawcy mogą zaśmiecać bazę kodu niepotrzebnymi i/lub powielanymi testami.
