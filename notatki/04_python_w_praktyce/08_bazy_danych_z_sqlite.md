## Bazy danych z SQLite

Na rynku dostępnych jest wiele różnorodnych systemów zarządzania bazami danych (DBMS). Każdy z nich posiada specyficzne wady i zalety. Jednym z popularnych, lekkich DBMS jest SQLite. Kluczowe cechy SQLite to:

- SQLite działa na większości dostępnych systemów operacyjnych.
- SQLite nie wymaga instalacji dodatkowego oprogramowania ani konfiguracji serwera.
- Cała baza danych jest zawarta w jednym pliku, co ułatwia przenoszenie i kopie zapasowe.
- W wielu przypadkach, cała baza danych jest ładowana do pamięci RAM, co przyspiesza operacje na niej.

Jeżeli poszukujesz zestawów danych do wykorzystania w projektach czy do nauki, polecam następujące źródła:

* [data.gov](https://data.gov/)
* [kaggle](https://www.kaggle.com/)

### Połączenie (Connection)

W kontekście baz danych, połączenie odnosi się do sesji między aplikacją a bazą danych. Gdy mówimy o "połączeniu z bazą danych", mamy na myśli nawiązanie komunikacji pomiędzy aplikacją (w naszym przypadku programem w Pythonie) a serwerem bazy danych (w tym przypadku plikiem bazy SQLite).

`connection` w naszym przykładzie jest instancją klasy, która reprezentuje to połączenie. Za pomocą tego obiektu możemy:

- Wykonywać operacje na bazie danych, takie jak tworzenie tabeli czy dodawanie rekordów.
- Zarządzać transakcjami (czyli grupami operacji, które mają być traktowane jako jedna całość; możemy je "zatwierdzać" (`commit`) lub "cofać" (`rollback`)).
- Zamykać połączenie z bazą danych.

### Kursor

W kontekście baz danych, kursor to specjalny obiekt, który umożliwia przechodzenie przez wyniki zapytania oraz odzyskiwanie kolejnych wierszy danych. W skrócie, kursor to narzędzie, które pozwala "przeszukiwać" wyniki zapytań krok po kroku.

W module `sqlite3` w Pythonie, kursor jest używany do:

- Wykonywania zapytań do bazy danych.
- Pobierania wyników zapytań (np. za pomocą metod `fetchone()` do pobierania jednego wiersza, `fetchall()` do pobierania wszystkich wierszy czy `fetchmany(size)` do pobierania określonej liczby wierszy).
- Obsługi błędów i wyjątków powiązanych z operacjami na bazie danych.

### Otwarcie połączenia z bazą danych

Połączenie z bazą danych lub jej utworzenie (jeśli nie istnieje) realizuje się za pomocą funkcji `connect()`.

```python
import sqlite3

connection = sqlite3.connect("baza_danych.db")
```

### Tworzenie tabel

Aby zdefiniować strukturę bazy, można utworzyć odpowiednie tabele za pomocą języka SQL. Tworzenie tabeli polega na zdefiniowaniu jej nazwy oraz kolumn, które będą się w niej znajdować, wraz z odpowiednimi typami danych i opcjonalnymi ograniczeniami.

#### Przykład tworzenia tabeli `users`

```python
import sqlite3

# Połączenie z bazą danych (lub utworzenie nowej)
connection = sqlite3.connect('example.db')

# Definicja polecenia SQL do utworzenia tabeli
sql_create_table = """
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL
)
"""

# Wykonanie polecenia SQL
connection.execute(sql_create_table)
```

Powyższy kod tworzy tabelę `users` z trzema kolumnami:
- `id`: Klucz główny tabeli, wartość unikalna dla każdego rekordu, automatycznie zwiększana.
- `username`: Nazwa użytkownika, pole tekstowe, wartość nie może być pusta.
- `password`: Hasło użytkownika, pole tekstowe, wartość nie może być pusta.

### Dodawanie rekordów

Wprowadzanie danych do tabeli realizowane jest przez polecenie `INSERT INTO`. Możemy wprowadzać pojedyncze rekordy lub wiele rekordów naraz.

#### Przykład dodawania rekordów do tabeli `users`

```python
# Połączenie z bazą danych
connection = sqlite3.connect('example.db')

# Dane do wprowadzenia
data_users = [
    ("user1", "pass1"),
    ("user2", "pass2")
]

# Wprowadzanie danych
for user in data_users:
    connection.execute("INSERT INTO users (username, password) VALUES (?, ?)", user)

# Zatwierdzenie zmian
connection.commit()
```

Powyższy kod dodaje dwa rekordy do tabeli `users`. Wartości dla `username` i `password` są pobierane z listy `data_users`, a następnie wstawiane do tabeli za pomocą zapytania `INSERT INTO`.

### Pobieranie danych

Do zapytań o dane z tabeli wykorzystuje się polecenie `SELECT`. Możemy pobierać wszystkie kolumny, wybrane kolumny lub filtrować dane za pomocą klauzuli `WHERE`.

#### Przykład pobierania wszystkich rekordów z tabeli `users`

```python
# Połączenie z bazą danych
connection = sqlite3.connect('example.db')

# Wykonanie zapytania SELECT
cursor = connection.execute("SELECT * FROM users")
users = cursor.fetchall()

# Wyświetlenie wyników
for user in users:
    print(user)
```

Powyższy kod pobiera wszystkie rekordy z tabeli `users` i wyświetla je. Funkcja `fetchall()` zwraca wszystkie wyniki zapytania jako listę krotek, gdzie każda krotka reprezentuje jeden rekord z bazy danych.

#### Przykład pobierania wybranych kolumn i filtrowania danych

```python
# Połączenie z bazą danych
connection = sqlite3.connect('example.db')

# Wykonanie zapytania SELECT z filtrowaniem
cursor = connection.execute("SELECT username FROM users WHERE id = ?", (1,))
user = cursor.fetchone()

# Wyświetlenie wyniku
if user:
    print(user)
```

Powyższy kod pobiera nazwę użytkownika dla rekordu, który ma `id` równe 1. Funkcja `fetchone()` zwraca pierwszy wynik zapytania jako krotkę. Jeśli wyników brak, zwraca `None`.

### Łączenie tabel (JOIN)

Do łączenia danych z różnych tabel wykorzystujemy polecenie `JOIN`.

#### Przykład: Inner Join

Aby pobrać dane użytkowników wraz z ich zamówieniami, możemy użyć INNER JOIN:

```python
# Połączenie z bazą danych
connection = sqlite3.connect('example.db')

# Wykonanie zapytania INNER JOIN
sql = """
SELECT users.username, orders.amount, orders.order_date
FROM users
INNER JOIN orders ON users.id = orders.user_id
"""
cursor = connection.execute(sql)
results = cursor.fetchall()

# Wyświetlenie wyników
for row in results:
    print(row)
```

Wynik:

```
('user1', 250.5, '2023-01-01')
('user1', 300.75, '2023-01-02')
('user2', 450.0, '2023-01-03')
```

#### Przykład: Left Join

Aby pobrać wszystkie dane użytkowników, niezależnie od tego, czy mają zamówienia, możemy użyć LEFT JOIN:

```python
# Połączenie z bazą danych
connection = sqlite3.connect('example.db')

# Wykonanie zapytania LEFT JOIN
sql = """
SELECT users.username, orders.amount, orders.order_date
FROM users
LEFT JOIN orders ON users.id = orders.user_id
"""
cursor = connection.execute(sql)
results = cursor.fetchall()

# Wyświetlenie wyników
for row in results:
    print(row)
```

Wynik:

```
('user1', 250.5, '2023-01-01')
('user1', 300.75, '2023-01-02')
('user2', 450.0, '2023-01-03')
```

### Grupowanie danych (GROUP BY)

Grupowanie danych pozwala na agregowanie wyników według określonego kryterium.

#### Przykład: Grupowanie według użytkownika i sumowanie zamówień

```python
# Połączenie z bazą danych
connection = sqlite3.connect('example.db')

# Wykonanie zapytania GROUP BY
sql = """
SELECT users.username, SUM(orders.amount) as total_amount
FROM users
INNER JOIN orders ON users.id = orders.user_id
GROUP BY users.username
"""
cursor = connection.execute(sql)
results = cursor.fetchall()

# Wyświetlenie wyników
for row in results:
    print(row)
```

Wynik:

```
('user1', 551.25)
('user2', 450.0)
```

### Sortowanie danych (ORDER BY)

Sortowanie wyników zapytań SQL realizowane jest przez polecenie `ORDER BY`.

#### Przykład: Sortowanie wyników według daty zamówienia

```python
# Połączenie z bazą danych
connection = sqlite3.connect('example.db')

# Wykonanie zapytania ORDER BY
sql = """
SELECT users.username, orders.amount, orders.order_date
FROM users
INNER JOIN orders ON users.id = orders.user_id
ORDER BY orders.order_date DESC
"""
cursor = connection.execute(sql)
results = cursor.fetchall()

# Wyświetlenie wyników
for row in results:
    print(row)
```

Wynik:

```
('user2', 450.0, '2023-01-03')
('user1', 300.75, '2023-01-02')
('user1', 250.5, '2023-01-01')
```

### Zamykanie połączenia

Po wszystkich operacjach na bazie danych, konieczne jest zamknięcie połączenia.

```python
connection.close()
```
