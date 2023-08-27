## Napisy (łańcuchy znaków)

Napisy, często nazywane łańcuchami znaków, to jeden z podstawowych typów danych w Pythonie. Reprezentują one ciąg znaków i są niezwykle przydatne w różnego rodzaju operacjach na tekście.

### Podstawy napisów

Napisy można deklarować na kilka sposobów, używając apostrofów, cudzysłowów czy potrójnych cudzysłowów (które umożliwiają wieloliniowe łańcuchy):

```python
napis1 = 'Hello'
napis2 = "World"
wieloliniowy_napis = '''To jest
wieloliniowy
napis.'''
```

Napisy są indeksowane, co oznacza, że możemy odwoływać się do poszczególnych znaków w napisie używając ich indeksów:

```python
napis = "Python"
print(napis[0])  # P
print(napis[-1]) # n
```

Używając składni wycinka (`slice`) możemy wyodrębnić fragmenty napisu:

```python
napis = "Pythonista"
print(napis[0:6])   # Python
print(napis[7:])   # sta
```

Chociaż napisy są niemutowalne (nie można zmienić ich zawartości), możemy je modyfikować tworząc nowe napisy na ich podstawie:

```python
oryginalny_napis = "Hello"
nowy_napis = oryginalny_napis + ", World!"
print(nowy_napis)  # Hello, World!
```

### Formatowanie napisów za pomocą f-string

f-stringi to nowoczesny mechanizm formatowania napisów w Pythonie. Pozwala on na wstawianie wartości zmiennych bezpośrednio do napisów w bardzo czytelny sposób.

Przykład:

```python
imie = "Anna"
wiek = 25
informacja = f"Nazywam się {imie} i mam {wiek} lat."
print(informacja)  # Nazywam się Anna i mam 25 lat.
```

f-stringi umożliwiają także używanie wyrażeń bezpośrednio w napisie:

```python
a = 5
b = 3
wynik = f"{a} plus {b} równa się {a+b}."
print(wynik)  # 5 plus 3 równa się 8.
```

Oprócz podstawowego formatowania, f-stringi oferują wiele zaawansowanych opcji, takich jak formatowanie liczb, dat czy operacje na napisach.

## Operacje na napisach

Python oferuje bogaty zestaw wbudowanych funkcji i metod, które ułatwiają manipulację i przetwarzanie napisów. Poniżej przedstawiamy kilka podstawowych operacji, które można wykonać na napisach:

### Zmiana wielkości liter

Metody `upper()` i `lower()` pozwalają odpowiednio na zamianę wszystkich liter napisu na wielkie lub małe litery:

```python
napis = "Python Jest Świetny"
print(napis.upper())  # PYTHON JEST ŚWIETNY
print(napis.lower())  # python jest świetny
```

### Formatowanie tytułów

Metoda `title()` zmienia pierwszą literę każdego słowa w napisie na wielką, a pozostałe na małe:

```python
napis = "python jest świetny"
print(napis.title())  # Python Jest Świetny
```

### Zastępowanie fragmentów napisu

Metoda `replace()` pozwala zastąpić fragment napisu innym tekstem:

```python
tekst = "Lubię programować w Javie."
nowy_tekst = tekst.replace("Javie", "Pythonie")
print(nowy_tekst)  # Lubię programować w Pythonie.
```

### Podział napisu

Metoda `split()` dzieli napis na listę słów w oparciu o podany separator (domyślnie jest to spacja):

```python
zdanie = "Python to język programowania."
slowa = zdanie.split()
print(slowa)  # ['Python', 'to', 'język', 'programowania.']
```

### Łączenie napisów

Odwrotnością metody `split()` jest `join()`, która łączy elementy listy w jeden napis, używając określonego separatora:

```python
slowa = ['Python', 'to', 'świetny', 'język']
zdanie = " ".join(slowa)
print(zdanie)  # Python to świetny język
```

Oprócz powyższych, istnieje wiele innych użytecznych metod przeznaczonych do operacji na napisach, takich jak `strip()`, `startswith()`, `endswith()`, `find()` i wiele innych. Dzięki nim praca z napisami w Pythonie jest intuicyjna i wydajna.
