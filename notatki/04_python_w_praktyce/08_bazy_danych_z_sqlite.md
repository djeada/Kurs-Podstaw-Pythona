
### Bazy danych z SQLite
Istnieje wiele baz danych. Każda ma swoje wady i zalety. Baza danych SQLite jest niezależna od systemu operacyjnego i nie wymaga instalacji żadnego dodatkowego oprogramowania. Zaletą SQLite jest prostota użytku. Nie potrzeba nam żadnego serwera, cała baza danych może zostać sprowadzona do jednego pliku, który w programie jest w całości załadowany do pamięci RAM.

Przykładowe zbiory danych możesz pobrać z następujących stron:
* <a href="https://data.gov/">data.gov</a>
* <a href="https://www.kaggle.com/">kaggle</a>

Moduł sqlite3 pozwala na obsługę bazy danych SQLite. 

#### Połączenie z bazą danych

Do połączenia z bazą danych należy użyć funkcji `connect()` z modułu sqlite3. Funkcja ta przyjmuje jako argument ścieżkę do pliku bazy danych. Jeśli podana baza danych nie istnieje, to zostanie ona utworzona.

    import sqlite3

    connection = sqlite3.connect("baza_danych.db")

#### Tworzenie tabel

Aby utworzyć tabelę w bazie danych, należy wywołać metodę `execute()` na obiekcie połączenia. Metoda ta przyjmuje jako argument polecenie SQL tworzące tabelę.

    connection.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)")

#### Dodawanie rekordów

Aby dodać rekord do tabeli, należy wywołać polecenie `INSERT INTO` za pomocą metody `execute()`.

    connection.execute("INSERT INTO users (username, password) VALUES (?, ?)", ("user1", "pass1"))
    connection.execute("INSERT INTO users (username, password) VALUES (?, ?)", ("user2", "pass2"))

#### Pobieranie danych

Aby pobrać dane z tabeli, należy wywołać polecenie `SELECT` za pomocą metody `execute()`. Metoda ta zwraca obiekt cursor, z którego można pobrać rekordy za pomocą metody `fetchall()`.

    cursor = connection.execute("SELECT * FROM users")
    users = cursor.fetchall()
    print(users)  # [(1, 'user1', 'pass1'), (2, 'user2', 'pass2')]

#### Zamykanie połączenia

Po zakończeniu pracy z bazą danych należy wywołać metodę `close()` na obiekcie połączenia.

    connection.close()
