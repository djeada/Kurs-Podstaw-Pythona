## Wyrażenia regularne

Wyrażenia regularne to potężne narzędzie do wyszukiwania, analizy i manipulacji tekstem. Umożliwiają one definiowanie wzorców tekstowych, które można następnie odnaleźć w ciągach znaków. Wyrażenia regularne są często wykorzystywane do:

- Wyszukiwania określonych ciągów znaków w tekście.
- Weryfikacji poprawności formatu danych (np. adresy e-mail).
- Zastępowania fragmentów tekstu innymi ciągami.

### Przykład

Wyszukiwanie wszystkich słów zaczynających się od *abc* lub składających się wyłącznie z małych liter oraz cyfr parzystych.

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

I. Zdefiniowanie wzorca wyrażenia regularnego:

- `pattern = r'([^/]*)/([^,]*), ([^/]*)/([^/]*)'` - wzorzec do dopasowania czterech grup:
- `([^/]*)` - wszystko przed pierwszym ukośnikiem,
- `([^,]*),` - wszystko przed przecinkiem,
- ` ([^/]*)` - wszystko przed drugim ukośnikiem,
- `([^/]*)` - wszystko przed końcem napisu.

II. Dopasowanie wzorca do danych: `match = re.match(pattern, dane)` 

III. Rozdzielenie daty na części: `miesiac, dzien, rok = match.group(2).split()`

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

### Przykłady użycia znaków specjalnych

```python
import re

tekst = "Przykładowy tekst z cyframi 123 i znakami specjalnymi !@#."

# Dopasowanie dowolnego znaku
pattern = r'.'
matches = re.findall(pattern, tekst)
print(matches)  # ['P', 'r', 'z', 'y', ... , '3', ' ', 'i', ' ', 'z', 'n', ...]

# Dopasowanie wszystkich cyfr
pattern = r'\d'
matches = re.findall(pattern, tekst)
print(matches)  # ['1', '2', '3']

# Dopasowanie wszystkich znaków niebędących cyframi
pattern = r'\D'
matches = re.findall(pattern, tekst)
print(matches)  # ['P', 'r', 'z', 'y', 'k', 'ł', 'a', 'd', 'o', 'w', 'y', ' ', 't', 'e', 'k', ...]

# Dopasowanie wszystkich białych znaków
pattern = r'\s'
matches = re.findall(pattern, tekst)
print(matches)  # [' ', ' ', ' ', ' ', ' ']

# Dopasowanie wszystkich znaków niebędących białymi znakami
pattern = r'\S'
matches = re.findall(pattern, tekst)
print(matches)  # ['P', 'r', 'z', 'y', 'k', 'ł', 'a', 'd', 'o', 'w', 'y', 't', 'e', 'k', 's', ...]

# Dopasowanie wszystkich znaków alfanumerycznych
pattern = r'\w'
matches = re.findall(pattern, tekst)
print(matches)  # ['P', 'r', 'z', 'y', 'k', 'ł', 'a', 'd', 'o', 'w', 'y', 't', 'e', 'k', ...]

# Dopasowanie wszystkich znaków niebędących alfanumerycznymi
pattern = r'\W'
matches = re.findall(pattern, tekst)
print(matches)  # [' ', ' ', ' ', ' ', ' ', ' ', '!', '@', '#', '.']
```

### Schemat pracy z wyrażeniami regularnymi

Praca z wyrażeniami regularnymi może być skomplikowana. Aby uprościć ten proces, warto postępować zgodnie z następującym schematem:

1. **Definiowanie wzorca**: Zacznij od stworzenia najprostszej wersji wyrażenia regularnego pasującą do twojego problemu. 
2. **Testowanie**: Upewnij się, że twój wzorzec znajduje dokładnie to, co chcesz, bez wyników fałszywie pozytywnych.
3. **Grupowanie**: Jeśli potrzebujesz odwoływać się do konkretnych fragmentów dopasowania, wykorzystaj nawiasy `()` do utworzenia grup.
4. **Rozszerzenie wzorca**: W miarę potrzeb, rozbudowuj swój wzorzec, dodając kolejne elementy i specjalne znaki.
5. **Przeprowadzanie testów**: Przetestuj wyrażenie na różnych przypadkach testowych, zarówno tych typowych, jak i skrajnych.

### Przykłady bardziej zaawansowanych zastosowań wyrażeń regularnych

#### Weryfikacja adresu e-mail

```python
import re

def czy_poprawny_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email) is not None

print(czy_poprawny_email("test@example.com"))  # True
print(czy_poprawny_email("test@.com"))  # False
```

- `pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'` - wzorzec do dopasowania poprawnych adresów email:
- `^` - początek napisu,
- `[a-zA-Z0-9_.+-]+` - jedna lub więcej liter, cyfr, podkreślników, kropek, plusów lub myślników,
- `@` - znak małpy (at),
- `[a-zA-Z0-9-]+` - jedna lub więcej liter, cyfr lub myślników (część przed kropką),
- `\.` - dosłowna kropka,
- `[a-zA-Z0-9-.]+` - jedna lub więcej liter, cyfr, kropek lub myślników (domena),
- `$` - koniec napisu.

#### Zastępowanie tekstu

```python
import re

tekst = "To jest stary tekst."
pattern = r'stary'
nowy_tekst = re.sub(pattern, 'nowy', tekst)
print(nowy_tekst)  # To jest nowy tekst.
```

#### Wyciąganie numerów telefonów

```python
import re

tekst = "Moje numery to: 123-456-7890 i (123) 456-7890."
pattern = r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}'
numery = re.findall(pattern, tekst)
print(numery)  # ['123-456-7890', '(123) 456-7890']
```

- `pattern = r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}'` - wzorzec do dopasowania numerów telefonów w różnych formatach:
- `\(?` - opcjonalny nawias otwierający,
- `\d{3}` - trzy cyfry,
- `\)?` - opcjonalny nawias zamykający,
- `[-.\s]?` - opcjonalny myślnik, kropka lub spacja,
- `\d{3}` - trzy cyfry,
- `[-.\s]?` - opcjonalny myślnik, kropka lub spacja,
- `\d{4}` - cztery cyfry.

Zawsze testuj dokładnie wyrażenia regularne przed wdrożeniem w produkcyjnym kodzie, aby upewnić się, że działają zgodnie z oczekiwaniami i są wydajne.

### Funkcje modułu `re`

Moduł `re` udostępnia kilka kluczowych funkcji:

| Funkcja                  | Opis                                                                |
|--------------------------|---------------------------------------------------------------------|
| `re.match(p, s)`         | Dopasowanie tylko na początku napisu                                |
| `re.search(p, s)`        | Dopasowanie pierwszego wystąpienia w dowolnym miejscu               |
| `re.findall(p, s)`       | Lista wszystkich dopasowań (jako napisy)                            |
| `re.finditer(p, s)`      | Iterator obiektów `Match` dla wszystkich dopasowań                  |
| `re.sub(p, r, s)`        | Zamiana dopasowań na `r`                                            |
| `re.split(p, s)`         | Podział napisu w miejscach dopasowań                                |
| `re.compile(p)`          | Kompilacja wzorca do wielokrotnego użycia (szybsze)                 |
| `re.fullmatch(p, s)`     | Dopasowanie całego napisu do wzorca                                 |

```python
import re

tekst = "Cena: 12.50 zł, rabat: 2.00 zł"

# findall — lista dopasowań
ceny = re.findall(r'\d+\.\d+', tekst)
print(ceny)  # ['12.50', '2.00']

# finditer — iterator z pozycjami
for dopasowanie in re.finditer(r'\d+\.\d+', tekst):
    print(f"Znaleziono: {dopasowanie.group()} na pozycji {dopasowanie.start()}")
# Znaleziono: 12.50 na pozycji 6
# Znaleziono: 2.00 na pozycji 25

# split — podział wg wzorca
zdanie = "jabłko,  banan;gruszka  śliwka"
owoce = re.split(r'[,;\s]+', zdanie)
print(owoce)  # ['jabłko', 'banan', 'gruszka', 'śliwka']
```

### Kompilacja wzorców

Jeśli ten sam wzorzec jest używany wielokrotnie, warto go skompilować za pomocą `re.compile()`. Skompilowany wzorzec jest szybszy przy wielu dopasowaniach:

```python
import re

# Kompilacja wzorca raz
wzorzec = re.compile(r'\b[A-Z][a-z]+\b')   # Słowo zaczynające się wielką literą

teksty = [
    "Python jest świetny",
    "Jan i Anna programują",
    "Warszawa to piękne miasto",
]

for tekst in teksty:
    dopasowania = wzorzec.findall(tekst)
    print(dopasowania)

# ['Python']
# ['Jan', 'Anna']
# ['Warszawa']
```

Flagi kompilacji:

```python
# re.IGNORECASE — ignorowanie wielkości liter
wzorzec = re.compile(r'python', re.IGNORECASE)
print(wzorzec.findall("Python PYTHON python"))   # ['Python', 'PYTHON', 'python']

# re.MULTILINE — ^ i $ dopasowują też do początku/końca każdej linii
tekst = "linia1\nlinia2\nlinia3"
wzorzec = re.compile(r'^\w+', re.MULTILINE)
print(wzorzec.findall(tekst))   # ['linia1', 'linia2', 'linia3']

# re.DOTALL — . dopasowuje też nową linię
wzorzec = re.compile(r'<.+>', re.DOTALL)
html = "<div>\nzawartość\n</div>"
print(wzorzec.findall(html))   # ['<div>\nzawartość\n</div>']
```

### Grupy nazwane

Zwykłe grupy `()` numeruje się od 1. Grupy nazwane (`(?P<nazwa>...)`) pozwalają odwoływać się do nich po nazwie:

```python
import re

# Parsowanie daty
wzorzec = re.compile(r'(?P<rok>\d{4})-(?P<miesiac>\d{2})-(?P<dzien>\d{2})')
m = wzorzec.match("2024-03-15")

if m:
    print(m.group("rok"))      # 2024
    print(m.group("miesiac"))  # 03
    print(m.group("dzien"))    # 15
    print(m.groupdict())       # {'rok': '2024', 'miesiac': '03', 'dzien': '15'}

# Zamiana z odwołaniem do grupy nazwanej
tekst = "2024-03-15"
nowy = re.sub(r'(?P<rok>\d{4})-(?P<miesiac>\d{2})-(?P<dzien>\d{2})',
              r'\g<dzien>.\g<miesiac>.\g<rok>', tekst)
print(nowy)  # 15.03.2024
```

### Lookahead i lookbehind (asercje)

Asercje pozwalają sprawdzać kontekst wokół dopasowania, **nie konsumując** znaków:

| Składnia       | Nazwa               | Znaczenie                                                  |
|----------------|---------------------|------------------------------------------------------------|
| `(?=...)`      | Lookahead pozytywny | Co dalej musi pasować, ale nie jest przechwytywane         |
| `(?!...)`      | Lookahead negatywny | Co dalej NIE może pasować                                  |
| `(?<=...)`     | Lookbehind pozytywny| Co przed musi pasować, ale nie jest przechwytywane         |
| `(?<!...)`     | Lookbehind negatywny| Co przed NIE może pasować                                  |

```python
import re

# Lookahead pozytywny — ceny w złotych (tylko liczby przed "zł")
tekst = "5 USD, 10 zł, 15 EUR, 20 zł"
ceny_pln = re.findall(r'\d+(?=\s*zł)', tekst)
print(ceny_pln)   # ['10', '20']

# Lookahead negatywny — liczby które nie są przed "zł"
pozostale = re.findall(r'\d+(?!\s*zł)', tekst)
print(pozostale)  # ['5', '15']

# Lookbehind pozytywny — wartości po "cena: "
tekst2 = "cena: 99.99, masa: 50kg"
wartosci = re.findall(r'(?<=cena: )\d+\.\d+', tekst2)
print(wartosci)   # ['99.99']
```

### Zamiana z funkcją (`re.sub` + callable)

`re.sub()` może przyjąć funkcję zamiast napisu zastępczego:

```python
import re

def zamien_na_wielkie(m):
    return m.group(0).upper()

tekst = "hello world foo bar"
wynik = re.sub(r'\b\w{4}\b', zamien_na_wielkie, tekst)
print(wynik)   # "hello WORLD foo BAR" — zamieniono 4-literowe słowa

# Zamiana liczb na ich kwadraty
def kwadrat(m):
    n = int(m.group(0))
    return str(n ** 2)

tekst = "2 razy 3 to 6"
print(re.sub(r'\d+', kwadrat, tekst))  # "4 razy 9 to 36"
```

### Tabela najczęstszych wzorców

| Cel                     | Wzorzec                                         |
|-------------------------|-------------------------------------------------|
| Adres e-mail            | `r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'` |
| URL                     | `r'https?://[^\s]+'`                            |
| Liczba całkowita        | `r'-?\d+'`                                      |
| Liczba zmiennoprzecinkowa | `r'-?\d+\.\d+'`                               |
| Polski numer telefonu   | `r'(\+48)?[\s-]?\d{3}[\s-]?\d{3}[\s-]?\d{3}'` |
| Data YYYY-MM-DD         | `r'\d{4}-\d{2}-\d{2}'`                         |
| Czas HH:MM              | `r'\d{2}:\d{2}'`                               |
| Kod pocztowy (PL)       | `r'\d{2}-\d{3}'`                               |
| Tag HTML                | `r'<[^>]+>'`                                    |
| Słowo                   | `r'\b\w+\b'`                                    |
| Puste linie             | `r'^\s*$'`                                      |
| IPv4                    | `r'\b\d{1,3}(\.\d{1,3}){3}\b'`                 |
