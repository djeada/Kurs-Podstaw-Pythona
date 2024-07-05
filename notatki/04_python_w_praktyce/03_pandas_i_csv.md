## Praca z plikami CSV w module Pandas

Pandas to potężna biblioteka w języku Python, przeznaczona do analizy i przetwarzania danych. Jednym z kluczowych zastosowań Pandas jest obsługa plików CSV (Comma-Separated Values). Biblioteka ta udostępnia funkcje takie jak `to_csv()` do zapisywania ramki danych (DataFrame) do pliku CSV oraz `read_csv()` do wczytywania danych z pliku CSV.

### Przykład użycia funkcji `to_csv()` i `read_csv()`

Przyjrzyjmy się, jak można wykorzystać te funkcje na praktycznym przykładzie. Załóżmy, że mamy następujące dane dotyczące rachunków za prąd w wybranym okresie:

```python
import pandas as pd

# Przygotowanie danych
data = {
    "Data": ["2022-01-01", "2022-02-01", "2022-03-01"],
    "Kwota": [100, 120, 130]
}
df = pd.DataFrame(data)

# Zapis danych do pliku CSV
nazwa_pliku = "rachunki.csv"
df.to_csv(nazwa_pliku, index=False, sep=';', encoding='utf-8')

print(f"Dane zapisane do {nazwa_pliku}!")

# Odczyt danych z pliku CSV
df_odczytane = pd.read_csv(nazwa_pliku, sep=';', encoding='utf-8')
print("\nOdczytane dane z pliku CSV:")
print(df_odczytane)
```

Po wykonaniu powyższego kodu, w pliku `rachunki.csv` znajdą się dane:

| Data       | Kwota |
|------------|-------|
| 2022-01-01 | 100   |
| 2022-02-01 | 120   |
| 2022-03-01 | 130   |

Kilka uwag:

- Parametr `sep=';'` określa separator używany w pliku CSV. W niektórych regionach standardowo używa się przecinka, ale w wielu krajach, gdzie przecinek jest używany jako separator dziesiętny, używa się średnika.
- Parametr `encoding='utf-8'` zapewnia, że plik będzie zakodowany w formacie UTF-8, co jest szczególnie ważne, jeśli dane zawierają znaki spoza ASCII, np. polskie litery.

Pandas udostępnia również wiele dodatkowych opcji dla `read_csv()`, pozwalających na bardziej zaawansowaną kontrolę nad procesem wczytywania danych, takich jak określenie typów kolumn, przetwarzanie brakujących danych i wiele innych.

### Eksploracja danych w Pandas

Gdy wczytujemy dane w formie tabeli przy użyciu biblioteki Pandas, często chcemy najpierw przeprowadzić ich podstawową analizę i wstępne przetwarzanie. Oto kilka przydatnych funkcji i technik, które ułatwią ten proces.

#### Przykładowy zestaw danych

Przykładowy zestaw danych, na którym będziemy wykonywać operacje, wygląda następująco:

| Imię     | Wiek | Miasto   | Wynagrodzenie |
|----------|------|----------|---------------|
| Jan      | 28   | Warszawa | 4500          |
| Anna     | 22   | Kraków   | 3900          |
| Piotr    | 34   | Warszawa | 5200          |
| Maria    | 45   | Gdańsk   | 6100          |
| Tomasz   | 30   | Wrocław  | 4700          |

Kod wczytujący te dane do Pandas:

```python
import pandas as pd

data = {
    'Imię': ['Jan', 'Anna', 'Piotr', 'Maria', 'Tomasz'],
    'Wiek': [28, 22, 34, 45, 30],
    'Miasto': ['Warszawa', 'Kraków', 'Warszawa', 'Gdańsk', 'Wrocław'],
    'Wynagrodzenie': [4500, 3900, 5200, 6100, 4700]
}

df = pd.DataFrame(data)
```

#### Informacje o strukturze danych

Aby uzyskać ogólny przegląd wczytanej tabeli, można użyć funkcji `info()`. Dostarcza ona informacje na temat liczby wierszy i kolumn, typów danych w poszczególnych kolumnach oraz ilości brakujących wartości.

```python
df.info()
```

Wynik:
```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 5 entries, 0 to 4
Data columns (total 4 columns):
 #   Column         Non-Null Count  Dtype 
---  ------         --------------  ----- 
 0   Imię           5 non-null      object
 1   Wiek           5 non-null      int64 
 2   Miasto         5 non-null      object
 3   Wynagrodzenie  5 non-null      int64 
dtypes: int64(2), object(2)
memory usage: 288.0+ bytes
```

#### Podgląd zawartości

Jeśli chcemy rzucić okiem na początkowe lub końcowe wiersze tabeli, przydadzą się funkcje `head()` oraz `tail()`. Domyślnie zwracają one 5 wierszy, ale można zmienić ten limit, podając odpowiednią liczbę jako argument.

```python
df.head(10) # pierwsze 10 wierszy
df.tail(3)  # ostatnie 3 wiersze
```

Wynik dla `df.head(3)`:
```
     Imię  Wiek    Miasto  Wynagrodzenie
0     Jan    28  Warszawa          4500
1    Anna    22    Kraków          3900
2   Piotr    34  Warszawa          5200
```

#### Wybieranie kolumn

Jeśli chcemy skupić się na konkretnych kolumnach, możemy je łatwo wybrać. Na przykład, jeśli chcemy wybrać tylko kolumny "Imię" i "Wiek":

```python
df_selected = df[['Imię', 'Wiek']]
```

Wynik:
```
     Imię  Wiek
0     Jan    28
1    Anna    22
2   Piotr    34
3   Maria    45
4  Tomasz    30
```

#### Filtrowanie wierszy

Aby przefiltrować wiersze w tabeli na podstawie pewnych kryteriów, korzystamy z metody `loc[]`. Na przykład, wybieranie wierszy, w których wartość w kolumnie "Wiek" jest większa niż 30:

```python
starsi_niz_30 = df.loc[df['Wiek'] > 30]
```

Wynik:
```
    Imię  Wiek    Miasto  Wynagrodzenie
2  Piotr    34  Warszawa          5200
3  Maria    45    Gdańsk          6100
```

Aby wybrać wiersze, w których wiek użytkownika przekracza 30 lat i mieszka w Warszawie:

```python
starsi_warszawianie = df.loc[(df['Wiek'] > 30) & (df['Miasto'] == 'Warszawa')]
```

Wynik:
```
    Imię  Wiek    Miasto  Wynagrodzenie
2  Piotr    34  Warszawa          5200
```

#### Statystyki opisowe

Jeśli chcemy szybko poznać podstawowe statystyki dotyczące kolumn numerycznych, możemy użyć funkcji `describe()`:

```python
# Przykładowe dane
data = {
    "Data": ["2022-01-01", "2022-02-01", "2022-03-01"],
    "Kwota": [100, 120, 130]
}
df = pd.DataFrame(data)

# Obliczenie statystyk opisowych
statystyki = df.describe()
print(statystyki)
```

Ta funkcja dostarczy informacji na temat średniej, mediany, odchylenia standardowego i innych podstawowych statystyk dla każdej kolumny numerycznej w tabeli.

Przykładowy wynik działania powyższego kodu:

```plaintext
            Kwota
count    3.000000
mean   116.666667
std     15.275252
min    100.000000
25%    110.000000
50%    120.000000
75%    125.000000
max    130.000000
```

Opis wyników:

- **count**: liczba niepustych wartości w kolumnie.
- **mean**: średnia arytmetyczna wartości w kolumnie.
- **std**: odchylenie standardowe, miara dyspersji wartości w kolumnie.
- **min**: najmniejsza wartość w kolumnie.
- **25%**: pierwszy kwartyl, wartość poniżej której znajduje się 25% danych.
- **50%**: mediana, wartość środkowa (drugi kwartyl).
- **75%**: trzeci kwartyl, wartość poniżej której znajduje się 75% danych.
- **max**: największa wartość w kolumnie.
### Agregacja danych

Pandas pozwala na łatwą agregację danych, na przykład obliczenie średniej, sumy czy liczby wystąpień. Dzięki temu możemy szybko uzyskać kluczowe informacje statystyczne na temat naszych danych.

#### Przykładowy zestaw danych

Przykładowy zestaw danych, na którym będziemy wykonywać operacje, wygląda następująco:

| Data       | Klient  | Kwota |
|------------|---------|-------|
| 2023-01-01 | Jan     | 250   |
| 2023-01-02 | Anna    | 300   |
| 2023-01-03 | Piotr   | 450   |
| 2023-02-01 | Maria   | 500   |
| 2023-02-02 | Tomasz  | 600   |

Kod wczytujący te dane do Pandas:

```python
import pandas as pd

data = {
    'Data': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-02-01', '2023-02-02'],
    'Klient': ['Jan', 'Anna', 'Piotr', 'Maria', 'Tomasz'],
    'Kwota': [250, 300, 450, 500, 600]
}

df = pd.DataFrame(data)
df['Data'] = pd.to_datetime(df['Data'])
```

#### Obliczenie średniej i sumy

Aby obliczyć średnią i sumę wartości w kolumnie `Kwota`, możemy użyć funkcji `mean()` i `sum()`:

```python
# Średnia wartość w kolumnie Kwota
srednia_kwota = df['Kwota'].mean()
print(f"Średnia wartość rachunku: {srednia_kwota}")

# Suma wartości w kolumnie Kwota
suma_kwot = df['Kwota'].sum()
print(f"Suma wartości rachunków: {suma_kwot}")
```

Wyniki:
```
Średnia wartość rachunku: 420.0
Suma wartości rachunków: 2100
```

### Grupowanie danych

Często przydatne jest grupowanie danych według określonych kryteriów. Pandas umożliwia to za pomocą metody `groupby()`, która pozwala na grupowanie danych według jednej lub kilku kolumn i wykonywanie agregacji na tych grupach.

#### Grupowanie według miesiąca i obliczenie średniej wartości rachunku

Aby grupować dane według miesiąca i obliczyć średnią wartość rachunku, możemy skorzystać z poniższego kodu:

```python
# Dodanie kolumny Miesiąc
df['Miesiąc'] = df['Data'].dt.month

# Grupowanie danych według miesiąca i obliczenie średniej wartości rachunku
srednia_miesieczna = df.groupby('Miesiąc')['Kwota'].mean()
print(srednia_miesieczna)
```

Wynik:
```
Miesiąc
1    333.333333
2    550.000000
Name: Kwota, dtype: float64
```

### Przetwarzanie brakujących danych

W praktycznych zastosowaniach często spotykamy się z brakującymi danymi. Pandas oferuje funkcje takie jak `fillna()` i `dropna()`, które pomagają w radzeniu sobie z brakami.

#### Przykładowy zestaw danych z brakującymi wartościami

| Data       | Klient  | Kwota |
|------------|---------|-------|
| 2023-01-01 | Jan     | 250   |
| 2023-01-02 | Anna    | NaN   |
| 2023-01-03 | Piotr   | 450   |
| 2023-02-01 | Maria   | 500   |
| 2023-02-02 | Tomasz  | NaN   |

Kod wczytujący te dane do Pandas:

```python
import numpy as np

data = {
    'Data': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-02-01', '2023-02-02'],
    'Klient': ['Jan', 'Anna', 'Piotr', 'Maria', 'Tomasz'],
    'Kwota': [250, np.nan, 450, 500, np.nan]
}

df = pd.DataFrame(data)
df['Data'] = pd.to_datetime(df['Data'])
```

#### Uzupełnianie brakujących wartości średnią

Aby uzupełnić brakujące wartości średnią z kolumny `Kwota`, możemy użyć funkcji `fillna()`:

```python
# Uzupełnianie brakujących wartości średnią
df_filled = df.fillna(df['Kwota'].mean())
print(df_filled)
```

Wynik:
```
        Data  Klient  Kwota
0 2023-01-01     Jan  250.0
1 2023-01-02    Anna  400.0
2 2023-01-03   Piotr  450.0
3 2023-02-01   Maria  500.0
4 2023-02-02  Tomasz  400.0
```

#### Usuwanie wierszy z brakującymi wartościami

Aby usunąć wiersze z brakującymi wartościami, używamy funkcji `dropna()`:

```python
# Usuwanie wierszy z brakującymi wartościami
df_dropped = df.dropna()
print(df_dropped)
```

Wynik:
```
        Data Klient  Kwota
0 2023-01-01    Jan  250.0
2 2023-01-03  Piotr  450.0
3 2023-02-01  Maria  500.0
```
