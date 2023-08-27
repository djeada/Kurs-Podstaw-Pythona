## Praca z plikami CSV w module Pandas

Pandas to potężna biblioteka w języku Python, przeznaczona do analizy i przetwarzania danych. Jednym z kluczowych zastosowań Pandas jest obsługa plików CSV (Comma-Separated Values). Biblioteka ta udostępnia funkcje takie jak `to_csv()` do zapisywania ramki danych (DataFrame) do pliku CSV oraz `read_csv()` do wczytywania danych z pliku CSV.

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

Po wykonaniu powyższego kodu, w pliku rachunki.csv znajdą się dane:

| data | kwota |
| ---- | ----- |
| 2022-01-01	| 100 |
| 2022-02-01	| 120 |
| 2022-03-01	| 130 |

Kilka uwag:

- Parametr sep=';' określa separator używany w pliku CSV. W niektórych regionach standardowo używa się przecinka, ale w wielu krajach, gdzie przecinek jest używany jako separator dziesiętny, używa się średnika.
- Parametr encoding='utf-8' zapewnia, że plik będzie zakodowany w formacie UTF-8, co jest szczególnie ważne, jeśli dane zawierają znaki spoza ASCII, np. polskie litery.

Pandas udostępnia również wiele dodatkowych opcji dla read_csv(), pozwalających na bardziej zaawansowaną kontrolę nad procesem wczytywania danych, takich jak określenie typów kolumn, przetwarzanie brakujących danych i wiele innych.

### Eksploracja danych w Pandas

Gdy wczytujemy dane w formie tabeli przy użyciu biblioteki Pandas, często chcemy najpierw przeprowadzić ich podstawową analizę i wstępne przetwarzanie. Oto kilka przydatnych funkcji i technik, które ułatwią ten proces:

#### Informacje o strukturze danych

Aby uzyskać ogólny przegląd wczytanej tabeli, można użyć funkcji `info()`. Dostarcza ona informacje na temat:

* Liczby wierszy i kolumn.
* Typów danych w poszczególnych kolumnach.
* Ilości brakujących wartości.

```python
df.info()
```

#### Podgląd zawartości

Jeśli chcemy rzucić okiem na początkowe lub końcowe wiersze tabeli, przydadzą się funkcje `head()` oraz `tail()`. Domyślnie zwracają one 5 wierszy, ale można zmienić ten limit, podając odpowiednią liczbę jako argument:

```python
df.head(10) # pierwsze 10 wierszy
df.tail(3)  # ostatnie 3 wiersze
```

#### Wybieranie kolumn

Jeśli chcemy skupić się na konkretnych kolumnach, możemy je łatwo wybrać:

```python
df_selected = df[["kolumna_1", "kolumna_2"]]
```

#### Filtrowanie wierszy

Aby przefiltrować wiersze w tabeli na podstawie pewnych kryteriów, korzystamy z metody `loc[]`:

- Wybieranie wierszy, w których wartość w kolumnie "Wiek" jest większa niż 30:

```python
starsi_niz_30 = df.loc[df['Wiek'] > 30]
```

- Wybieranie wierszy, w których wiek użytkownika przekracza 30 lat i mieszka w Warszawie:

```python
starsi_warszawianie = df.loc[(df['Wiek'] > 30) & (df['Miasto'] == 'Warszawa')]
```

#### Statystyki opisowe

Jeśli chcemy szybko poznać podstawowe statystyki dotyczące kolumn numerycznych, możemy użyć funkcji `describe()`:

```python
df.describe()
```

Ta funkcja dostarczy informacji na temat średniej, mediany, odchylenia standardowego i innych podstawowych statystyk dla każdej kolumny numerycznej w tabeli.

Eksploracja danych to kluczowy krok w każdym projekcie analizy danych, a Pandas oferuje wiele narzędzi ułatwiających ten proces.
