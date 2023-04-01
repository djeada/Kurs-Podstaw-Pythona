## Pandas i csv

Moduł Pandas to bardzo popularny moduł, używany do pracy z danymi tabelarycznymi. Do zapisywania danych tabelarycznych do pliku csv oraz odczytywania danych z pliku csv, służą nam funkcje <code>to_csv()</code> oraz <code>read_csv()</code>.

Załóżmy, że mamy tabelę przedstawiającą rachunki za prąd w wybranym domu. Chcemy zapisać tę tabelę do pliku csv, a następnie odczytać dane z tego pliku. Możemy to zrobić w następujący sposób:

```python
import pandas as pd

# przygotowujemy dane do zapisania
data = [["2022-01-01", 100], ["2022-02-01", 120], ["2022-03-01", 130]]
df = pd.DataFrame(data, columns=["data", "kwota"])

# zapisujemy dane do pliku csv
df.to_csv("rachunki.csv", index=False)

# odczytujemy dane z pliku csv
df_odczytane = pd.read_csv("rachunki.csv")
print(df_odczytane)
```

Wynikiem tego kodu będzie tabela o takim wyglądzie:

| data | kwota |
| ---- | ----- |
| 2022-01-01	| 100 |
| 2022-02-01	| 120 |
| 2022-03-01	| 130 |

### Podstawowe informacje o tabeli

Po wczytaniu tabeli do pamięci, możemy wyświetlić podstawowe informacje o niej za pomocą funkcji `info()`.

```python
df.info()
```

Funkcja ta pokazuje nam takie informacje jak:

* ilość wierszy i kolumn,
* typy danych w poszczególnych kolumnach,
* ilość niezapełnionych pól.

### Podgląd danych

Aby sprawdzić, jakie dane mamy w tabeli, możemy wyświetlić jej fragment za pomocą funkcji `head()` lub `tail()`. Domyślnie obie funkcje wyświetlają 5 pierwszych lub ostatnich wierszy tabeli. Możemy też podać ilość wierszy jaką chcemy wyświetlić jako argument.

```python
df.head(10) # pierwsze 10 wierszy
df.tail() # ostatnie 5 wierszy
```

### Selekcja kolumn

Aby wybrać konkretne kolumny z tabeli, możemy użyć notacji z nawiasami kwadratowymi.

```python
df[["kolumna_1", "kolumna_2"]]
```

### Filtrowanie danych

Do filtrowania danych służy nam operator `[]`. Możemy użyć go w połączeniu z operatorami logicznymi, takimi jak `&` lub `|`.

Przykładowo, jeśli mamy tabelę zawierającą informacje o użytkownikach i interesują nas tylko ci użytkownicy, którzy mają więcej niż 30 lat, to możemy użyć następującej komendy:

```python
df.loc[df['Wiek'] > 30]
```

Jeśli chcemy pokazać użytkowników, którzy mają więcej niż 30 lat i mieszkają w Warszawie, to możemy użyć następującej komendy:

```python
df.loc[(df['Wiek'] > 30) & (df['Miasto'] == 'Warszawa')]
```
