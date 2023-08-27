## Wyrażenia regularne

Wyrażenia regularne to potężne narzędzie do wyszukiwania, analizy i manipulacji tekstem. Umożliwiają one definiowanie wzorców tekstowych, które można następnie odnaleźć w ciągach znaków. Wyrażenia regularne są często wykorzystywane do:

- Wyszukiwania określonych ciągów znaków w tekście.
- Weryfikacji poprawności formatu danych (np. adresy e-mail).
- Zastępowania fragmentów tekstu innymi ciągami.

**Przykład**: Wyszukiwanie wszystkich słów zaczynających się od *abc* lub składających się wyłącznie z małych liter oraz cyfr parzystych.

Rozważmy sytuację, w której mamy plik tekstowy, gdzie każdy wiersz zawiera trzy informacje oddzielone ukośnikami: nazwisko pracownika, datę odczytu oraz odczyt licznika. Chcemy wyciągnąć datę z każdego wiersza:

```python
dane = 'Kowalski/Maj 15, 1983/1721.3'

# Klasyczne podejście z wykorzystaniem funkcji klasy String:
pracownik, data, odczyt = dane.split('/')
miesiac, dzien, rok = data.split(' ')
dzien = dzien.rstrip(',')
print(f'{miesiac}, {dzien}, {rok}')  # Maj, 15, 1983
```

Chociaż rozwiązanie działa, jest dość kruche. Jeżeli struktura danych się zmieni, musimy dostosować algorytm. Wyrażenia regularne oferują bardziej uniwersalne podejście:

```python
import re

dane = 'Kowalski/Maj 15, 1983/1721.3'
pattern = r'([^/]*)/([^,]*), ([^/]*)/([^/]*)'
match = re.match(pattern, dane)
miesiac, dzien, rok = match.group(2).split()
print(f'{miesiac}, {dzien}, {rok}')  # Maj, 15, 1983
```

Moduł `re` w Pythonie udostępnia funkcje do pracy z wyrażeniami regularnymi, takie jak `match`, `search`, `split`, czy `sub`. Specjalne znaki w wyrażeniach regularnych, takie jak `.` (dowolny znak), `*` (dowolna liczba powtórzeń), czy `[a-z]` (dowolna mała litera), pozwalają na definiowanie skomplikowanych wzorców do wyszukiwania tekstu.

### Znaki specjalne w wyrażeniach regularnych

Wyrażenia regularne wykorzystują różne znaki specjalne, aby definiować skomplikowane wzorce tekstu. Poniżej przedstawiam najważniejsze z nich:

* `.` - Reprezentuje dowolny znak, z wyjątkiem nowego wiersza.
* `\d` - Oznacza jedną cyfrę.
* `\D` - Oznacza dowolny znak, który nie jest cyfrą.
* `\s` - Reprezentuje biały znak (np. spacja, tabulacja, nowy wiersz).
* `\S` - Oznacza dowolny znak, który nie jest białym znakiem.
* `\w` - Oznacza dowolny znak alfanumeryczny, co obejmuje litery, cyfry oraz znak podkreślenia (_).
* `\W` - Oznacza dowolny znak, który nie jest znakiem alfanumerycznym.
* `[]` - Określa zbiór znaków. Na przykład, `[abc]` pasuje do każdego z znaków: a, b, lub c.
* `^` - Oznacza początek wiersza.
* `$` - Oznacza koniec wiersza.
* `|` - Reprezentuje operator "lub". Na przykład, `abc|def` pasuje do ciągu "abc" lub "def".
* `()` - Tworzy grupę. Może być używane do izolowania fragmentów wzorca, na przykład `(abc){3}` pasuje do "abcabcabc".
* `*` - Oznacza zero lub więcej powtórzeń poprzedniego znaku lub grupy. Na przykład, `a*` może pasować do "", "a", "aa", "aaa" itp.
* `+` - Oznacza jedno lub więcej powtórzeń.
* `?` - Oznacza zero lub jedno powtórzenie.
* `{m,n}` - Określa zakres powtórzeń od m do n. Na przykład, `a{2,4}` pasuje do "aa", "aaa" lub "aaaa".

### Schemat pracy z wyrażeniami regularnymi

Praca z wyrażeniami regularnymi może być skomplikowana. Aby uprościć ten proces, warto postępować zgodnie z następującym schematem:

1. **Definiowanie wzorca**: Zacznij od stworzenia najprostszej wersji wyrażenia regularnego pasującą do twojego problemu. 
2. **Testowanie**: Upewnij się, że twój wzorzec znajduje dokładnie to, co chcesz, bez wyników fałszywie pozytywnych.
3. **Grupowanie**: Jeśli potrzebujesz odwoływać się do konkretnych fragmentów dopasowania, wykorzystaj nawiasy `()` do utworzenia grup.
4. **Rozszerzenie wzorca**: W miarę potrzeb, rozbudowuj swój wzorzec, dodając kolejne elementy i specjalne znaki.
5. **Przeprowadzanie testów**: Przetestuj wyrażenie na różnych przypadkach testowych, zarówno tych typowych, jak i skrajnych.

Zawsze testuj dokładnie wyrażenia regularne przed wdrożeniem w produkcyjnym kodzie.
