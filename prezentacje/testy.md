## Testy

* Bugi są realnym problemem dla twórców oprogramowania.
* Testy mają na celu zmniejszenie ilości bugów w programach dostępnych dla klientów.
* Istnieje kilka sposobów klasyfikacji testów.
* Testy można klasyfikować względem zakresu kodu, jaki mają sprawdzać na: a) jednostkowe b) integracyjne c) systemowe.

## Przykłady bugów

* Rakieta Ariane 5 ECA (2002 r.) uległa samozniszczeniu kilka sekund po starcie. Przyczyną awarii był bug w systemie sterującym chłodzeniem.
* Niedokładność przy zaokrąglaniu spowodowała, że w 25 lutego 1991 roku systemy antyrakietowe nie zadziałały tak jak powinny i w wyniku ostrzału zostało zabitych 28 amerykańskich żołnierzy. <a href="https://www-users.cse.umn.edu/~arnold/455.f96/disasters.html">linkiem</a>.

## Proces testowania

Ogólne kroki dla wszystkich testów:

1. Przygotuj dane wejściowe i/lub konfigurację programu.
2. Zdefiniuj spodziewany efekt.
3. Wywołaj funkcję/uruchom program.
4. Porównaj otrzymany efekt ze spodziewanym i wyświetl informację dla programisty.

## Testy jednostkowe

* Mają na celu sprawdzenie jednostki kodu (najczęściej funkcji).
* Ich wykonanie nie powinno zajmować dużo czasu. Programista powinien natychmiastowo otrzymać informację zwrotną o poprawności swojej implementacji.
* Testy przekładają wymagania klienta na kod.
* Najlepsze testy to takie, które można napisać nie znając implementacji w kodzie produkcyjnym.
* Największą wartość mają w regresji.

## Przykład

Załóżmy, że w kodzie produkcyjnym znajduje się funkcja znajdz_klucz(lista, klucz) zwracająca indeks pierwszego wystąpienia klucza w liście.

* Zachowanie podstawowe: klucz znajduje się w liście.
* Skrajny przypadek: klucz nie znajduje się w liście.

## Pokrycie kodu produkcyjnego (code coverage)

  *1* def fun(a, b):
  *2*   a += 1
  *3*   b += 2
  *4*   if a + b > 22:
  *5*     a += 1
  *6*   return a + b
   
Jeśli testujemy *fun(a,b)* jedynie dla a oraz b, których suma jest mniejsza niż 20, to nigdy nie wykonamy wiersza numer 5.

## Czy zielone testy są gwarancją poprawności?

* Czerwone testu mówią nam, że kod nie spełnia przynajmniej części wymogów sprawdzanych testach. Wiemy na pewno, że mamy problem, który powinniśmy naprawić.
* Zielone testy mówią nam, że kod spełnia wszystkie wymogi sprawdzane w testach. Nie znaczy to, że wszystkie teoretyczne wymogi zostały przeniesione na testy.
* Bug w systemie Klarna doprowadził do wycieku danych użytkowników, mimo że 100% testów było zielonych. Więcej możesz dowiedzieć się pod tym <a href="https://www.klarna.com/se/blogg/detailed-incident-report-incorrect-cache-configuration-leading-to-klarna-app-exposing-personal-information/">linkiem</a>.
