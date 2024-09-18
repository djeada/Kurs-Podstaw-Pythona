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

### Tworzenie tabeli `users`

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
connection.commit()
```

Powyższy kod tworzy tabelę `users` z trzema kolumnami:

- `id`: Klucz główny tabeli, wartość unikalna dla każdego rekordu, automatycznie zwiększana.
- `username`: Nazwa użytkownika, pole tekstowe, wartość nie może być pusta.
- `password`: Hasło użytkownika, pole tekstowe, wartość nie może być pusta.

### Tworzenie tabeli `orders`

```python
# Definicja polecenia SQL do utworzenia tabeli
sql_create_orders_table = """
CREATE TABLE orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    amount REAL,
    order_date TEXT,
    FOREIGN KEY (user_id) REFERENCES users (id)
)
"""

# Wykonanie polecenia SQL
connection.execute(sql_create_orders_table)
connection.commit()
```

Powyższy kod tworzy tabelę `orders` z czterema kolumnami:

- `id`: Klucz główny tabeli, wartość unikalna dla każdego rekordu, automatycznie zwiększana.
- `user_id`: Id użytkownika, klucz obcy odnoszący się do `id` w tabeli `users`.
- `amount`: Kwota zamówienia, pole numeryczne.
- `order_date`: Data zamówienia, pole tekstowe.

### Dodawanie rekordów do tabeli `users`

```python
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

# Sprawdzenie wyników
cursor = connection.execute("SELECT * FROM users")
print(cursor.fetchall())
```

Powyższy kod dodaje dwa rekordy do tabeli `users`. Wartości dla `username` i `password` są pobierane z listy `data_users`, a następnie wstawiane do tabeli za pomocą zapytania `INSERT INTO`.

Wynik:

```
[(1, 'user1', 'pass1'), (2, 'user2', 'pass2')]
```

### Dodawanie rekordów do tabeli `orders`

```python
# Dane do wprowadzenia
data_orders = [
    (1, 250.5, '2023-01-01'),
    (1, 300.75, '2023-01-02'),
    (2, 450.0, '2023-01-03')
]

# Wprowadzanie danych
for order in data_orders:
    connection.execute("INSERT INTO orders (user_id, amount, order_date) VALUES (?, ?, ?)", order)

# Zatwierdzenie zmian
connection.commit()

# Sprawdzenie wyników
cursor = connection.execute("SELECT * FROM orders")
print(cursor.fetchall())
```

Powyższy kod dodaje trzy rekordy do tabeli `orders`. Wartości dla `user_id`, `amount` i `order_date` są pobierane z listy `data_orders`, a następnie wstawiane do tabeli za pomocą zapytania `INSERT INTO`.

Wynik:

```
[(1, 1, 250.5, '2023-01-01'), (2, 1, 300.75, '2023-01-02'), (3, 2, 450.0, '2023-01-03')]
```

### Pobieranie wszystkich rekordów z tabeli `users`

```python
# Wykonanie zapytania SELECT
cursor = connection.execute("SELECT * FROM users")
users = cursor.fetchall()

# Wyświetlenie wyników
for user in users:
    print(user)
```

- `SELECT * FROM users`: Pobiera wszystkie kolumny i wiersze z tabeli `users`.
- `cursor.fetchall()`: Pobiera wszystkie wyniki zapytania i zwraca je jako listę krotek.
- `for user in users`: Iteruje przez listę użytkowników i drukuje każdą krotkę.

Wynik:

```
(1, 'user1', 'pass1')
(2, 'user2', 'pass2')
```

### Pobieranie wybranych kolumn i filtrowanie danych

```python
# Wykonanie zapytania SELECT z filtrowaniem
cursor = connection.execute("SELECT username FROM users WHERE id = ?", (1,))
user = cursor.fetchone()

# Wyświetlenie wyniku
if user:
    print(user)
```

- `SELECT username FROM users WHERE id = ?`: Pobiera kolumnę `username` z tabeli `users`, gdzie `id` jest równe 1.
- `cursor.fetchone()`: Pobiera pierwszy wynik zapytania.
- `if user`: Sprawdza, czy wynik nie jest pusty i drukuje nazwę użytkownika.

Wynik:

```
('user1',)
```

### Łączenie tabel (JOIN)

#### Przykład: Inner Join

```python
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

- `INNER JOIN`: Łączy wiersze z dwóch tabel, gdzie istnieje dopasowanie w obu tabelach.
- `ON users.id = orders.user_id`: Warunek łączenia, gdzie `id` z tabeli `users` musi być równe `user_id` z tabeli `orders`.

Wynik:

```
('user1', 250.5, '2023-01-01')
('user1', 300.75, '2023-01-02')
('user2', 450.0, '2023-01-03')
```

#### Przykład: Left Join

```python
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

`LEFT JOIN`: Łączy wszystkie wiersze z tabeli `users` i dopasowane wiersze z tabeli `orders`. Jeśli nie ma dopasowania, wynikiem są wartości NULL w kolumnach tabeli `orders`.

Wynik:

```
('user1', 250.5, '2023-01-01')
('user1', 300.75, '2023-01-02')
('user2', 450.0, '2023-01-03')
```

### Grupowanie danych (GROUP BY)

#### Przykład: Grupowanie według użytkownika i sumowanie zamówień

```python
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

- `GROUP BY users.username`: Grupuje wyniki według nazwy użytkownika.
- `SUM(orders.amount) as total_amount`: Oblicza sumę zamówień dla każdego użytkownika.

Wynik:

```
('user1', 551.25)
('user2', 450.0)
```

### Sortowanie danych (ORDER BY)

#### Przykład: Sortowanie wyników według daty zamówienia

```python
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

`ORDER BY orders.order_date DESC`: Sortuje wyniki według daty zamówienia w kolejności malejącej.

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
