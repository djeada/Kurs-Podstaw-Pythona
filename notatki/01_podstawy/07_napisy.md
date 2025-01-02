## Napisy (łańcuchy znaków)

Napisy, często nazywane łańcuchami znaków, to jeden z najpopularniejszych i najbardziej wszechstronnych typów danych w Pythonie. Pozwalają one na przechowywanie oraz przetwarzanie informacji tekstowych i mogą być wykorzystywane w niemal wszystkich rodzajach aplikacji – od prostych skryptów po rozbudowane systemy. Co więcej, Python udostępnia bogaty zestaw funkcji i metod ułatwiających pracę z napisami, co czyni go niezwykle atrakcyjnym narzędziem do wszelkiego rodzaju operacji na tekstach. 

Poniżej znajduje się przegląd podstawowych zagadnień związanych z napisami w Pythonie – od sposobów ich tworzenia, poprzez indeksowanie i modyfikację, aż po przydatne funkcje i metody formatowania.

#### Podstawy napisów

Napisy można deklarować na kilka sposobów, używając pojedynczych apostrofów, podwójnych cudzysłowów bądź potrójnych cudzysłowów (te ostatnie są szczególnie przydatne przy tworzeniu wieloliniowych łańcuchów znaków). Oto przykładowe deklaracje:

```python
napis1 = 'Hello'
napis2 = "World"
wieloliniowy_napis = '''To jest
wieloliniowy
napis.'''
```

W powyższych przykładach `napis1` i `napis2` zostały zdefiniowane jako proste łańcuchy znaków, natomiast `wieloliniowy_napis` może zawierać tekst rozłożony na wiele linii. W praktyce oznacza to, że jeśli potrzebujemy przechowywać większe bloki tekstu lub wklejać fragmenty dokumentacji do zmiennej, potrójne cudzysłowy okażą się bardzo wygodne.

Warto pamiętać, że niezależnie od tego, czy użyjemy pojedynczych apostrofów (`'`) czy podwójnych cudzysłowów (`"`), Python nie robi między nimi rozróżnienia na poziomie semantyki. Wybór sposobu deklarowania napisów bywa najczęściej kwestią preferencji lub konwencji w danym projekcie.

#### Indeksowanie

Napisy w Pythonie są sekwencjami znaków, które można indeksować. Każdemu znakowi w napisie odpowiada konkretny indeks, przy czym indeksy w Pythonie rozpoczynają się od zera. Oznacza to, że `napis[0]` zwróci pierwszy znak łańcucha, `napis[1]` – drugi, i tak dalej. Dodatkowo, Python obsługuje także indeksy ujemne, które liczone są od końca napisu: `napis[-1]` oznacza ostatni znak, `napis[-2]` – przedostatni itd.

```python
napis = "Python"
print(napis[0])   # P
print(napis[-1])  # n
```

Indeksowanie znaków w ten sposób bywa przydatne chociażby przy wyodrębnianiu pierwszego bądź ostatniego znaku, czy sprawdzaniu konkretnych fragmentów napisu. 

#### Wycinki (ang. slicing)

Operacje na napisach w Pythonie nie ograniczają się do odczytu pojedynczych znaków. Bardzo często potrzebujemy uzyskać dostęp do fragmentu (podciągu) napisu. W tym celu używamy składni wycinka (ang. slice). Możemy w niej określić początkowy i końcowy indeks oraz krok (opcjonalnie), za pomocą którego chcemy przechodzić przez łańcuch.

Najczęstsze postaci wycinków to:

- `napis[start:end]` – zwraca fragment napisu od indeksu `start` (włącznie) do indeksu `end` (bez tego indeksu),
- `napis[:end]` – zwraca fragment od początku napisu do indeksu `end` (bez tego indeksu),
- `napis[start:]` – zwraca fragment od indeksu `start` do końca napisu,
- `napis[start:end:krok]` – zwraca fragment z uwzględnieniem zdefiniowanego kroku.

```python
napis = "Pythonista"
print(napis[0:6])  # Python
print(napis[7:])   # sta
```

W powyższym przykładzie `napis[0:6]` wycina znaki od indeksu 0 do 5, a `napis[7:]` zwraca od znaku o indeksie 7 aż do końca, omijając pozostałą część.

### Niemutowalność napisów

Napisy w Pythonie są **niemutowalne** (ang. *immutable*), co oznacza, że nie możemy zmienić pojedynczych znaków w istniejącym obiekcie typu `str`. Jeżeli chcemy wprowadzić modyfikacje, zazwyczaj tworzymy nowy łańcuch znaków, na przykład poprzez konkatenację (łączenie) napisów:

```python
oryginalny_napis = "Hello"
# oryginalny_napis[0] = 'M'  # To spowoduje błąd, ponieważ napisy są niemutowalne
nowy_napis = oryginalny_napis + ", World!"
print(nowy_napis)  # Hello, World!
```

Takie podejście warto mieć na uwadze zwłaszcza w sytuacjach, gdy często dokonujemy zmian na bardzo długich łańcuchach, ponieważ operacje tworzące nowe napisy mogą okazać się kosztowne pod względem pamięci. W praktyce, przy bardziej złożonych przekształceniach, często wykorzystuje się inne typy danych, np. listy znaków, a potem dopiero konwertuje się je z powrotem do typu `str`.

### Formatowanie napisów za pomocą f-string

Jednym z wygodnych sposobów formatowania napisów są **f-stringi**. Pojawiły się one w Pythonie 3.6 i od tego czasu stały się bardzo popularnym narzędziem do tworzenia czytelnych i elastycznych łańcuchów tekstowych. Dzięki f-stringom możemy wstawić wartości zmiennych lub wyniki wyrażeń bezpośrednio do nawiasów klamrowych w napisie.

```python
imie = "Anna"
wiek = 25
informacja = f"Nazywam się {imie} i mam {wiek} lat."
print(informacja)  # Nazywam się Anna i mam 25 lat.
```

Co ciekawe, nie trzeba ograniczać się jedynie do wstawiania zmiennych. Możemy np. wykonać proste działania matematyczne w obrębie tych klamr:

```python
a = 5
b = 3
wynik = f"{a} plus {b} równa się {a+b}."
print(wynik)  # 5 plus 3 równa się 8.
```

Dzięki f-stringom oszczędzamy sobie konieczności korzystania ze starszych konstrukcji, takich jak `str.format()` czy operator `%`. Dodatkowo f-stringi oferują szerokie możliwości formatowania liczb, dat, czy precyzyjnego ustawiania szerokości pól tekstowych. W większych projektach przyczynia się to do utrzymania wysokiej czytelności i estetyki kodu.

### Operacje na napisach

Python oferuje szeroki wachlarz wbudowanych funkcji oraz metod przeznaczonych do pracy z łańcuchami znaków. Są one wywoływane najczęściej w postaci: `napis.metoda()`, a każda z nich może zwracać zmodyfikowaną wersję napisu lub informację o jego zawartości. Poniżej opisano kilka najpopularniejszych metod i operacji, dzięki którym praca z tekstem w Pythonie staje się przyjemna i intuicyjna.

#### Zmiana wielkości liter

Jeśli chcemy ujednolicić zapis albo przetworzyć napisy w taki sposób, by wszystkie litery były duże lub małe, możemy użyć następujących metod:

- `upper()` – konwertuje wszystkie znaki w napisie na wielkie litery,
- `lower()` – konwertuje wszystkie znaki na małe litery.

```python
napis = "Python Jest Świetny"
print(napis.upper())  # PYTHON JEST ŚWIETNY
print(napis.lower())  # python jest świetny
```

W praktyce bywa to szczególnie przydatne przy porównywaniu napisów (np. usuwanie rozróżnień między wielkością liter) lub do wyświetlania komunikatów w zdefiniowanej formie (np. całych na wielkich literach).

#### Formatowanie tytułów

Metoda `title()` zmienia pierwszą literę każdego słowa na wielką, a pozostałe na małe. Takie formatowanie przydaje się np. przy generowaniu spójnych tytułów czy nazw produktów:

```python
napis = "python jest świetny"
print(napis.title())  # Python Jest Świetny
```

Z kolei `capitalize()` zmienia pierwszą literę napisu na wielką, pozostałe na małe (ale dotyczy tylko pierwszego słowa, nie wszystkich w zdaniu). Drobne różnice między `title()` a `capitalize()` mogą być istotne w zależności od zastosowania.

### Zastępowanie fragmentów napisu

Gdy chcemy podmienić fragment tekstu na inny (np. zmienić nazwę technologii w dokumentacji), możemy posłużyć się metodą `replace()`:

```python
tekst = "Lubię programować w Javie."
nowy_tekst = tekst.replace("Javie", "Pythonie")
print(nowy_tekst)  # Lubię programować w Pythonie.
```

Warto zauważyć, że `replace()` nie modyfikuje oryginalnego napisu (pamiętamy, że jest on niemutowalny), tylko zwraca nowy napis. W efekcie należy go przypisać do zmiennej (tak jak w przykładzie) albo od razu wykorzystać w dalszych obliczeniach lub wyświetleniu.

#### Podział napisu

Często zdarza się, że musimy rozbić jakiś łańcuch znaków na mniejsze elementy (np. chcemy oddzielić słowa od siebie lub podzielić linie w pliku CSV). W tym celu używamy metody `split()`. Domyślnym separatorem jest spacja, ale możemy też podać inny dowolny separator, np. przecinek.

```python
zdanie = "Python to język programowania."
slowa = zdanie.split()
print(slowa)  # ['Python', 'to', 'język', 'programowania.']
```

Po takim podziale otrzymujemy listę słów, na której możemy wykonać wiele innych operacji (np. przetworzyć każde słowo, posortować listę czy przefiltrować duplikaty).

#### Łączenie napisów

Odwrotność `split()` stanowi metoda `join()`. Jej zadaniem jest połączenie elementów listy (zawierającej napisy) w jeden łańcuch znaków przy użyciu określonego separatora. Wywołujemy ją na separatorze, a jako argument przekazujemy listę napisów:

```python
slowa = ['Python', 'to', 'świetny', 'język']
zdanie = " ".join(slowa)
print(zdanie)  # Python to świetny język
```

W tym przykładzie elementy listy `slowa` zostały złączone w jeden napis, a pomiędzy nimi wstawiono pojedynczą spację. W analogiczny sposób można używać innych separatorów, np. przecinka z odstępem `", "`, czy ukośnika `"/"`.

#### Inne przydatne metody

Powyżej opisano jedynie niewielki wycinek możliwości, jakie daje Python w zakresie pracy z napisami. Oprócz nich istnieje wiele innych metod, które warto znać:

- **`strip()`, `lstrip()`, `rstrip()`** – usuwają białe znaki (np. spacje, tabulatory, znaki nowej linii) z końców napisu (odpowiednio z obu stron, tylko z lewej, tylko z prawej).
- **`startswith()`, `endswith()`** – sprawdzają, czy napis zaczyna się lub kończy określonym fragmentem.
- **`find()`, `index()`** – szukają podanego ciągu znaków w napisie i zwracają pozycję pierwszego wystąpienia (przy czym `find()` zwraca `-1` w przypadku braku wyniku, a `index()` wywoła błąd).
- **`count()`** – zlicza liczbę wystąpień danego podciągu.
- **`isalnum()`, `isalpha()`, `isdigit()`, `isspace()`** – pozwalają sprawdzić, czy napis składa się odpowiednio z liter i cyfr, tylko liter, tylko cyfr lub tylko ze znaków białych (spacje, tabulatory, itp.).

Dzięki temu rozbudowanemu zestawowi metod Python pozwala łatwo rozwiązywać problemy związane z przetwarzaniem danych tekstowych, począwszy od szybkich zmian formatowania aż po wyrafinowane wyszukiwanie i zamianę konkretnych fragmentów.
