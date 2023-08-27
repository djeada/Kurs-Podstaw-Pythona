## Bazy danych z SQLite

Na rynku dostępnych jest wiele różnorodnych systemów zarządzania bazami danych (DBMS). Każdy z nich posiada specyficzne wady i zalety. Jednym z popularnych, lekkich DBMS jest SQLite. Kluczowe cechy SQLite to:

- **Niezmienność systemu operacyjnego**: SQLite działa na większości dostępnych systemów operacyjnych.
- **Brak wymogu instalacji**: SQLite nie wymaga instalacji dodatkowego oprogramowania ani konfiguracji serwera.
- **Samowystarczalność**: Cała baza danych jest zawarta w jednym pliku, co ułatwia przenoszenie i kopie zapasowe.
- **Wydajność**: W wielu przypadkach, cała baza danych jest ładowana do pamięci RAM, co przyspiesza operacje na niej.

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

Aby zdefiniować strukturę bazy, można utworzyć odpowiednie tabele za pomocą języka SQL.

```python
sql_create_table = """
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    password TEXT NOT NULL
)
"""

connection.execute(sql_create_table)
```

### Dodawanie rekordów

Wprowadzanie danych do tabeli realizowane jest przez polecenie `INSERT INTO`.

```python
data_users = [
    ("user1", "pass1"),
    ("user2", "pass2")
]

for user in data_users:
    connection.execute("INSERT INTO users (username, password) VALUES (?, ?)", user)

# Zatwierdzenie zmian
connection.commit()
```

### Pobieranie danych

Do zapytań o dane z tabeli wykorzystuje się polecenie `SELECT`.

```python
cursor = connection.execute("SELECT * FROM users")
users = cursor.fetchall()

for user in users:
    print(user)
```

### Zamykanie połączenia

Po wszystkich operacjach na bazie danych, konieczne jest zamknięcie połączenia.

```python
connection.close()
```
