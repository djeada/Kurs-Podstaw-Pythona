
## Wyrażenia regularne

Wyrażenia regularne to sposób na wyszukiwanie tekstu w oparciu o wzorce. Możemy używać ich do wyszukiwania wzorców w ciągach znaków, ale także do zastępowania znalezionych wzorców innymi ciągami znaków. Możemy również używać wyrażeń regularnych do sprawdzania, czy ciąg znaków spełnia określone kryteria (np. czy jest to adres e-mail). Typowym zadaniem dla wyrażeń regularnych to Przykładowo znalezienie wszystkich słów zaczynających się od *abc* lub składających się wyłącznie z małych liter oraz cyfr parzystych.

Powiedzmy, że mamy plik gdzie każdy wiersz zawiera trzy informacje oddzielone ukośnikami: nazwisko pracownika, datę odczytu, oraz odczyt licnzika. Jak wyciągnąć datę z każdego wiersza? Używając klasycznych funkcji znanej nam klasy <code>String</code> moglibyśmy to zrobić w taki sposób:

```python
dane = 'Kowalski/Maj 15, 1983/1721.3'
pracownik, data, odczyt = dane.split('/')
miesiac, dzien, rok = data.split(' ')
if dzien[-1] == ',':
  dzien = dzien[:-1]

print(f'{miesiac}, {dzien}, {rok}') # Maj, 15, 1983
```

Rozwiązanie działa, ale nie należy do najpiękniejszych. Co gorsza, jest bardzo kruche. Cokolwiek zmieni się w naszych danych, musimy przerabiać nasz algorytm. Za każdym razem musimy być bardzo uważni i rozumieć każdy wiersz kodu. W takim podejściu bardzo łatwo popełnić błąd. Istnieje jednak inna metoda. Wyrażenia regularne są deklaratywne, tzn. mówimy co chcemy mieć, a nie w jaki sposób.

```python
import re

dane = 'Kowalski/Maj 15, 1983/1721.3'
match = re.search('(.*)/(.*)/(.*)', dane)
data = match.group(2) # czesc tekstu odpowiadajaca drugiemu nawiasowi
data = re.sub('[^\w\s]', '', data) # usun znaki interpunkcyjne
miesiac, dzien, rok = re.split('[\s/]', data) # rozbij przy pomocy spacji

print(f'{miesiac}, {dzien}, {rok}') # Maj, 15, 1983
```

Aby użyć wyrażeń regularnych, musimy najpierw zaimportować moduł `re`. Następnie możemy użyć różnych funkcji modułu `re`, takich jak `search`, `sub`, `split`, itd. Funkcja `search` służy do wyszukiwania wzorca w ciągu znaków, a funkcja `sub` do zastępowania znalezionych wzorców innymi ciągami znaków. Funkcja `split` służy do podziału ciągu znaków na fragmenty w oparciu o wzorzec.

Wyrażenia regularne składają się z ciągów znaków oraz specjalnych znaków. Specjalne znaki służą do określania rodzaju znaków, które chcemy znaleźć. Na przykład, znak "`.`" oznacza dowolny znak, a znak "`*`" oznacza dowolną ilość powtórzeń poprzedzającego znaku. Możemy również używać nawiasów kwadratowych, by określić zbiór znaków, które chcemy znaleźć. Na przykład, "`[0123456789]`" oznacza dowolną cyfrę, a "`[a-zA-Z]`" oznacza dowolną literę.

### Znaki specjalne

Oto lista najważniejszych znaków specjalnych, które warto znać:

* <code>.</code> - dowolny znak (oprócz nowego wiersza)
* <code>\d</code> - cyfra
* <code>\D</code> - dowolny znak, który nie jest cyfrą
* <code>\s</code> - biały znak (spacja, tabulacja, nowy wiersz)
* <code>\S</code> - dowolny znak, który nie jest białym znakiem
* <code>\w</code> - dowolny znak alfanumeryczny (małe i duże litery, cyfry, znak podkreślenia)
* <code>\W</code> - dowolny znak, który nie jest znakiem alfanumerycznym
* <code>[]</code> - zbiór, np. <code>[abc]</code> oznacza a, b lub c
* <code>^</code> - początek wiersza
* <code>$</code> - koniec wiersza
* <code>|</code> - lub, np. <code>abc|def</code> oznacza a, b, c lub d, e, f
* <code>()</code> - grupa, np. <code>(abc){3}</code> oznacza a, b, c trzy razy
* <code></code> - powtórzenie dowolne razy, np. <code>a</code> oznacza 0 lub więcej wystąpień a
* <code>+</code> - powtórzenie co najmniej raz, np. <code>a+</code> oznacza 1 lub więcej wystąpień a
* <code>?</code> - powtórzenie 0 lub 1 raz, np. <code>a?</code> oznacza 0 lub 1 wystąpienie a
* <code>{m,n}</code> - powtórzenie od m do n razy, np. <code>a{2,4}</code> oznacza 2, 3 lub 4 wystąpienia a

Oczywiście to tylko wybrane przykłady.

### Schemat pracy z wyrażeniami regularnymi

Omówimy teraz, jak krok po kroku przeprowadzić wszystkie czynności potrzebne do użycia wyrażeń regularnych w rozwiązaniu danego problemu. Oto krótki opis schematu:

1. Zbuduj najprostszą wersję wyrażenia regularnego pasującą do twojego problemu. 
1. Przetestuj czy wyrażenie regularne znajduje TYLKO to, co chcesz, by zostało znalezione. Łatwo o wynik fałszywie pozytywny.
1. Upewnij się, że wyrażenie regularne zwraca wszystkie niezbędne grupy. Pamiętaj, że grupy są oznaczone przez nawiasy `()`.
1. Poszerz rozwiązanie bazowe o dodatkowe wymogi. 
1. Upewnij się, że twój kod działa poprawnie dla różnych przypadków testowych.

Pamiętaj, że wyrażenia regularne mogą być skomplikowane i trudne do zrozumienia. Ważne jest, aby dobrze zrozumieć schemat pracy z nimi i systematycznie testować działanie wyrażenia przed użyciem go w kodzie.