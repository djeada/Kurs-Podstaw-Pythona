# Python w praktyce — quiz

Notatki: [HTTP i prosty serwer](../notatki/04_python_w_praktyce/06_http_i_prosty_serwer.md), [Bazy danych z SQLite](../notatki/04_python_w_praktyce/08_bazy_danych_z_sqlite.md), [Tkinter](../notatki/04_python_w_praktyce/09_tkinter.md), [Argumenty linii poleceń](../notatki/04_python_w_praktyce/01_argumenty_linii_polecen.md), [Praca z plikami i folderami](../notatki/04_python_w_praktyce/02_praca_z_plikami_i_folderami.md), [Informacje o systemie operacyjnym](../notatki/04_python_w_praktyce/05_informacje_o_systemie_operacyjnym.md), [Logi](../notatki/04_python_w_praktyce/10_logi.md)

Sprawdź, czy umiesz korzystać z HTTP, SQLite, Tkintera oraz modułów biblioteki standardowej do argumentów, plików, systemu i logów.

#### Q. Która metoda HTTP zwraca te same nagłówki co `GET`, ale bez treści odpowiedzi?

* [ ] `OPTIONS`
* [x] `HEAD`
* [ ] `PUT`
* [ ] `POST`

> **Wyjaśnienie:** `HEAD` pozwala np. sprawdzić rozmiar lub datę modyfikacji zasobu bez pobierania go. `OPTIONS` pyta serwer o metody dostępne dla zasobu.

#### Q. Jaki kod statusu HTTP oznacza, że żądanie (np. `POST`) utworzyło nowy zasób?

* [ ] `200`
* [ ] `204`
* [x] `201`
* [ ] `302`

> **Wyjaśnienie:** `201 Created` potwierdza utworzenie zasobu. `200 OK` to ogólny sukces, `204 No Content` to sukces bez treści odpowiedzi, a kody 3xx oznaczają przekierowanie.

#### Q. Czym różni się kod `401 Unauthorized` od `403 Forbidden`?

* [ ] `401` oznacza błąd po stronie serwera, a `403` błąd po stronie klienta
* [x] `401` wymaga uwierzytelnienia, a `403` to brak uprawnień mimo niego
* [ ] `401` oznacza brak zasobu, a `403` jego trwałe usunięcie
* [ ] Oba kody znaczą to samo i można ich używać zamiennie

> **Wyjaśnienie:** Przy `401` serwer nie wie, kim jest klient, albo dane logowania są błędne. Przy `403` tożsamość może być znana, ale klient nie ma prawa dostępu do zasobu, więc ponowne logowanie nie pomoże.

#### Q. Co wypisze ten program?

```python
import http.server
import threading
import urllib.request

class Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        body = f"sciezka={self.path}".encode()
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, *args):
        pass

serwer = http.server.HTTPServer(("127.0.0.1", 0), Handler)
threading.Thread(target=serwer.serve_forever, daemon=True).start()
port = serwer.server_address[1]

with urllib.request.urlopen(f"http://127.0.0.1:{port}/raport?rok=2024") as odp:
    print(odp.status, odp.read().decode())
serwer.shutdown()
```

* [ ] `200 sciezka=/raport`
* [x] `200 sciezka=/raport?rok=2024`
* [ ] `200 sciezka=raport?rok=2024`
* [ ] `404 sciezka=/raport?rok=2024`

> **Wyjaśnienie:** Atrybut `self.path` zawiera całą ścieżkę żądania razem z ciągiem zapytania po `?`. Parametry trzeba z niej wyodrębnić samodzielnie, np. przez `urllib.parse.urlsplit` i `parse_qs`.

#### Q. Co wypisze ten program?

```python
import http.server
import threading
import urllib.error
import urllib.request

class Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()

    def log_message(self, *args):
        pass

serwer = http.server.HTTPServer(("127.0.0.1", 0), Handler)
threading.Thread(target=serwer.serve_forever, daemon=True).start()
url = f"http://127.0.0.1:{serwer.server_address[1]}/"

try:
    urllib.request.urlopen(urllib.request.Request(url, data=b"x", method="POST"))
except urllib.error.HTTPError as e:
    print(e.code)
serwer.shutdown()
```

* [ ] `405`
* [ ] `404`
* [ ] `500`
* [x] `501`

> **Wyjaśnienie:** `BaseHTTPRequestHandler` szuka metody `do_<METODA>`; gdy jej brak, sam odpowiada `501 Unsupported method`. Aby obsłużyć `POST`, trzeba zdefiniować `do_POST`.

#### Q. Co robi metoda `raise_for_status()` obiektu odpowiedzi w bibliotece `requests`?

* [ ] Ponawia żądanie, dopóki serwer nie zwróci kodu 200
* [x] Zgłasza `HTTPError` dla kodów 4xx i 5xx, a dla 2xx nic nie robi
* [ ] Zamienia liczbowy kod statusu na jego opis tekstowy, np. `"Not Found"`
* [ ] Zgłasza wyjątek, gdy odpowiedź nie zawiera danych JSON

> **Wyjaśnienie:** `requests` domyślnie nie zgłasza wyjątków dla błędnych kodów HTTP, więc odpowiedź 404 wygląda jak każda inna. `raise_for_status()` zamienia błąd HTTP w wyjątek, który można obsłużyć w `except`.

#### Q. Co robi wywołanie `requests.post(url, json=dane)`, gdzie `dane` to słownik?

* [ ] Wysyła słownik jako parametry w adresie URL
* [ ] Wysyła słownik jako formularz HTML typu `application/x-www-form-urlencoded`
* [x] Wysyła słownik jako JSON z nagłówkiem `Content-Type: application/json`
* [ ] Oczekuje, że serwer odeśle dane w formacie JSON

> **Wyjaśnienie:** Parametr `json=` sam zamienia obiekt na tekst JSON i ustawia odpowiedni nagłówek. Parametry w adresie URL podaje się przez `params=`, a dane formularza przez `data=`.

#### Q. Dlaczego warto podawać argument `timeout` w wywołaniach takich jak `requests.get(url, timeout=5)`?

* [ ] Bo bez niego `requests` nie obsługuje połączeń HTTPS
* [x] Bo bez niego żądanie może czekać na odpowiedź bez końca
* [ ] Bo określa, jak długo odpowiedź ma być przechowywana w pamięci
* [ ] Bo ogranicza liczbę ponownych prób wysłania żądania

> **Wyjaśnienie:** Domyślnie `requests` nie ma limitu czasu, więc zawieszony serwer może zablokować program na zawsze. Po przekroczeniu `timeout` biblioteka zgłasza `requests.exceptions.Timeout`, który można obsłużyć.

#### Q. Która cecha najlepiej wyróżnia SQLite na tle baz takich jak PostgreSQL?

* [ ] Wymaga uruchomienia osobnego serwera bazy danych
* [x] Cała baza to jeden plik i nie trzeba serwera
* [ ] Działa wyłącznie w systemie Linux
* [ ] Nie obsługuje transakcji, kluczy obcych ani klauzuli `JOIN`

> **Wyjaśnienie:** SQLite to biblioteka wbudowana w aplikację: baza mieści się w jednym pliku, który łatwo skopiować lub przenieść. W Pythonie obsługuje ją moduł `sqlite3` z biblioteki standardowej.

#### Q. Dlaczego wartości do zapytania SQL przekazuje się przez znaczniki `?`, a nie wkleja f-stringiem?

* [ ] Bo f-stringi nie działają z modułem `sqlite3`
* [ ] Bo zapytania ze znacznikami `?` zawsze wykonują się szybciej
* [x] Bo chroni to przed SQL injection i poprawnie cytuje wartości
* [ ] Bo SQLite nie akceptuje napisów w poleceniu `execute`

> **Wyjaśnienie:** Przy wklejaniu tekstu dane od użytkownika mogą zmienić znaczenie zapytania, np. `' OR 1=1 --`. Parametry przekazane osobno sterownik traktuje zawsze jako wartości, nigdy jako fragment SQL.

#### Q. Co wypisze ten program?

```python
import sqlite3

con = sqlite3.connect(":memory:")
con.execute("CREATE TABLE users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT NOT NULL)")
con.executemany("INSERT INTO users (username) VALUES (?)", [("ala",), ("ola",)])
print(con.execute("SELECT username FROM users WHERE id = ?", (2,)).fetchone())
```

* [ ] `ola`
* [x] `('ola',)`
* [ ] `['ola']`
* [ ] `(2, 'ola')`

> **Wyjaśnienie:** Każdy wiersz wyniku to krotka, nawet gdy zawiera tylko jedną kolumnę. `fetchone()` zwraca jeden taki wiersz (albo `None`), a `AUTOINCREMENT` nadał drugiemu rekordowi `id` równe 2.

#### Q. Tabela `t` istnieje. Co się stanie, gdy wywołasz `con.execute("SELECT * FROM t WHERE id = ?", (2))`?

* [ ] Zapytanie zadziała tak samo jak z `(2,)`
* [ ] Zapytanie zwróci pusty wynik
* [x] Zostanie zgłoszony `ProgrammingError`, bo `(2)` to `int`
* [ ] Znacznik `?` zostanie po cichu zastąpiony napisem `"2"`

> **Wyjaśnienie:** Nawiasy bez przecinka nie tworzą krotki, więc `(2)` to po prostu `int`. Parametry muszą być sekwencją (lub słownikiem), dlatego jednoelementową krotkę zapisuje się jako `(2,)`.

#### Q. Co wypisze ten program?

```python
import sqlite3

con = sqlite3.connect(":memory:")
con.execute("CREATE TABLE orders (user TEXT, amount REAL)")
con.executemany("INSERT INTO orders VALUES (?, ?)", [("ala", 10.0), ("ola", 5.0), ("ala", 2.5)])
print(con.execute("SELECT user, SUM(amount) FROM orders GROUP BY user ORDER BY user").fetchall())
```

* [ ] `[('ala', 10.0), ('ola', 5.0), ('ala', 2.5)]`
* [ ] `[('ala', 17.5)]`
* [x] `[('ala', 12.5), ('ola', 5.0)]`
* [ ] `[('ala', 2), ('ola', 1)]`

> **Wyjaśnienie:** `GROUP BY user` łączy wiersze o tej samej wartości kolumny `user` w jedną grupę, a `SUM` sumuje kwoty w każdej z nich. `fetchall()` zwraca listę krotek.

#### Q. Co wypisze ten program?

```python
import sqlite3

con = sqlite3.connect(":memory:")
con.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT)")
con.execute("CREATE TABLE orders (id INTEGER PRIMARY KEY, user_id INTEGER)")
con.executemany("INSERT INTO users VALUES (?, ?)", [(1, "ala"), (2, "ola"), (3, "ewa")])
con.executemany("INSERT INTO orders (user_id) VALUES (?)", [(1,), (1,), (2,)])
sql = """
SELECT users.username, COUNT(orders.id)
FROM users LEFT JOIN orders ON users.id = orders.user_id
GROUP BY users.id ORDER BY users.id
"""
print(con.execute(sql).fetchall())
```

* [ ] `[('ala', 2), ('ola', 1)]`
* [ ] `[('ala', 2), ('ola', 1), ('ewa', None)]`
* [x] `[('ala', 2), ('ola', 1), ('ewa', 0)]`
* [ ] `[('ala', 2), ('ola', 1), ('ewa', 1)]`

> **Wyjaśnienie:** `LEFT JOIN` zachowuje każdego użytkownika, a brakujące zamówienia uzupełnia wartościami `NULL`. `COUNT(kolumna)` pomija `NULL`, więc dla `ewa` daje 0; `INNER JOIN` w ogóle by jej nie zwrócił.

#### Q. Co wypisze ten program?

```python
import sqlite3

con = sqlite3.connect("test.db")
con.execute("CREATE TABLE t (x INTEGER)")
con.commit()
con.execute("INSERT INTO t VALUES (1)")
con.close()

con = sqlite3.connect("test.db")
print(con.execute("SELECT COUNT(*) FROM t").fetchone()[0])
```

* [x] `0`
* [ ] `1`
* [ ] Zgłosi `OperationalError`: brak tabeli `t`
* [ ] Zgłosi `ProgrammingError` przy `close()`

> **Wyjaśnienie:** `sqlite3` otwiera transakcję przed `INSERT`, a `close()` bez `commit()` ją wycofuje. Tabela przetrwała, bo jej utworzenie zostało zatwierdzone, ale wstawiony wiersz przepadł.

#### Q. Co wypisze ten program?

```python
import sqlite3

con = sqlite3.connect(":memory:")
print(con.execute("SELECT NULL, 1 + 1, 'a' || 'b'").fetchone())
```

* [ ] `('NULL', 2, 'ab')`
* [x] `(None, 2, 'ab')`
* [ ] `(None, '2', 'a||b')`
* [ ] `(None, 2, 'a b')`

> **Wyjaśnienie:** Moduł `sqlite3` zamienia `NULL` na `None`, a liczby całkowite na `int`. Operator `||` w SQL łączy napisy, podobnie jak `+` dla napisów w Pythonie.

#### Q. Co robi wywołanie `root.mainloop()` w programie z Tkinterem?

* [ ] Tworzy główne okno aplikacji
* [ ] Odświeża okno jeden raz i od razu kończy działanie
* [x] Uruchamia pętlę zdarzeń, która działa do zamknięcia okna
* [ ] Uruchamia interfejs w osobnym wątku, a program idzie dalej

> **Wyjaśnienie:** `mainloop()` obsługuje kliknięcia, klawisze i odświeżanie okna, blokując dalsze wykonanie skryptu. Kod umieszczony po nim wykona się dopiero po zamknięciu okna, np. przez `root.destroy()`.

#### Q. Co wypisze ten program?

```python
import tkinter as tk

root = tk.Tk()
klikniecia = []

def zapisz():
    klikniecia.append("klik")

przycisk = tk.Button(root, text="OK", command=zapisz())
przycisk.invoke()
print(klikniecia)
root.destroy()
```

* [ ] `[]`
* [x] `['klik']`
* [ ] `['klik', 'klik']`
* [ ] Zgłosi `TypeError`

> **Wyjaśnienie:** Zapis `command=zapisz()` wywołuje funkcję od razu przy tworzeniu przycisku i przekazuje jej wynik, czyli `None`. Przycisk nie ma więc akcji, a `invoke()` nic nie robi; poprawnie jest `command=zapisz`.

#### Q. Co się stanie, gdy w tym samym oknie jeden widżet ułożysz przez `pack()`, a drugi przez `grid()`?

* [ ] Tkinter automatycznie zamieni `grid()` na `pack()`
* [ ] Oba widżety zostaną wyświetlone jeden na drugim w lewym górnym rogu
* [x] Zostanie zgłoszony `TclError` o konflikcie menedżerów układu
* [ ] Drugi widżet zostanie po cichu pominięty

> **Wyjaśnienie:** W jednym kontenerze nie można łączyć `pack` i `grid`, bo rozmieszczają elementy według sprzecznych zasad (`place` może z nimi współistnieć). Różne metody można łączyć, umieszczając widżety w osobnych ramkach (`Frame`).

#### Q. Co robi parametr `columnspan=2` w wywołaniu `widget.grid(row=3, column=0, columnspan=2)`?

* [ ] Dodaje 2 piksele odstępu po lewej i po prawej stronie widżetu
* [x] Sprawia, że widżet zajmuje dwie sąsiednie kolumny siatki
* [ ] Tworzy dwie kopie widżetu w kolejnych kolumnach
* [ ] Przesuwa widżet o dwie kolumny w prawo

> **Wyjaśnienie:** `columnspan` rozciąga komórkę widżetu na kilka kolumn, co przydaje się np. dla paska stanu pod formularzem. Odstępy ustawia się parametrami `padx` i `pady`.

#### Q. Jak metodą `place()` umieścić przycisk dokładnie na środku okna, niezależnie od jego rozmiaru?

* [ ] `place(x=0.5, y=0.5)`
* [ ] `place(relx=50, rely=50, anchor="center")`
* [ ] `place(relx=0.5, rely=0.5)`
* [x] `place(relx=0.5, rely=0.5, anchor="center")`

> **Wyjaśnienie:** `relx` i `rely` podają położenie jako ułamek wymiarów okna, a `anchor="center"` sprawia, że w tym punkcie wypada środek przycisku. Bez `anchor` w środku okna znalazłby się lewy górny róg widżetu.

#### Q. Czym różni się funkcja podpięta przez `command=` przycisku (`Button`) od funkcji podpiętej przez `bind("<Button-1>", ...)`?

* [ ] Funkcja z `command=` musi przyjmować obiekt zdarzenia jako pierwszy argument
* [x] Funkcja z `bind()` dostaje obiekt `event`, a z `command=` nic
* [ ] Funkcja z `bind()` może być podpięta tylko do okna głównego
* [ ] Obie funkcje są wywoływane bez argumentów

> **Wyjaśnienie:** `bind()` przekazuje obiekt `event` z informacjami o zdarzeniu, np. pozycją kursora (`event.x`) czy znakiem klawisza (`event.char`). `command=` przycisku wywołuje funkcję bez argumentów.

#### Q. Które zdarzenie Tkintera oznacza kliknięcie prawym przyciskiem myszy w systemach Windows i Linux?

* [ ] `<Button-1>`
* [ ] `<Button-2>`
* [x] `<Button-3>`
* [ ] `<Double-Button-1>`

> **Wyjaśnienie:** Numery przycisków to 1 dla lewego, 2 dla środkowego i 3 dla prawego. `<Double-Button-1>` to podwójne kliknięcie lewym przyciskiem.

#### Q. Co wypisze ten program uruchomiony z katalogu, w którym może utworzyć plik?

```python
import pathlib
import subprocess
import sys

pathlib.Path("skrypt.py").write_text("import sys\nprint(sys.argv[1:], len(sys.argv))\n")
wynik = subprocess.run([sys.executable, "skrypt.py", "3", "2", "1"], capture_output=True, text=True)
print(wynik.stdout.strip())
```

* [ ] `[3, 2, 1] 3`
* [ ] `['3', '2', '1'] 3`
* [x] `['3', '2', '1'] 4`
* [ ] `['skrypt.py', '3', '2', '1'] 4`

> **Wyjaśnienie:** `sys.argv[0]` to nazwa skryptu, więc lista ma o jeden element więcej niż argumentów. Wszystkie argumenty są napisami i trzeba je jawnie przekonwertować, np. `int()`.

#### Q. Co wypisze ten program?

```python
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("plik")
parser.add_argument("-l", "--liczba", type=int, default=10)
parser.add_argument("-v", "--verbose", action="store_true")
args = parser.parse_args(["dane.txt", "-l", "5"])
print(args.plik, args.liczba + 1, args.verbose)
```

* [ ] `dane.txt 51 False`
* [ ] `dane.txt 11 False`
* [x] `dane.txt 6 False`
* [ ] `dane.txt 6 None`

> **Wyjaśnienie:** `type=int` konwertuje tekst `"5"` na liczbę, więc dodawanie działa arytmetycznie. Flaga z `action="store_true"` ma wartość `False`, gdy jej nie podano.

#### Q. Co wypisze ten program?

```python
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--num", type=int, action="append")
print(parser.parse_args(["--num", "1", "--num", "2"]).num, parser.parse_args([]).num)
```

* [ ] `2 None`
* [ ] `[1, 2] []`
* [x] `[1, 2] None`
* [ ] `['1', '2'] None`

> **Wyjaśnienie:** `action="append"` dokłada każdą wartość do listy, a `type=int` konwertuje ją przed dodaniem. Bez podania opcji i bez `default` atrybut ma wartość `None`, a nie pustą listę.

#### Q. Co zrobi `argparse`, gdy użytkownik nie poda wymaganego argumentu pozycyjnego?

* [ ] Przypisze argumentowi wartość `None` i będzie działać dalej
* [ ] Zapyta użytkownika o brakującą wartość
* [x] Wypisze komunikat o błędzie i zakończy program kodem 2
* [ ] Zgłosi `ValueError`, który trzeba obsłużyć w `try`

> **Wyjaśnienie:** `parse_args()` przy błędnych argumentach wypisuje na `stderr` składnię wywołania i opis błędu, a potem wywołuje `sys.exit(2)`. Dzięki temu nie trzeba ręcznie sprawdzać obecności wymaganych argumentów.

#### Q. Co wypisze ten program?

```python
with open("plik.txt", "w") as f:
    f.write("a\n")
with open("plik.txt", "w") as f:
    f.write("b\n")
with open("plik.txt", "a") as f:
    f.write("c\n")

with open("plik.txt") as f:
    print(f.read().split())
```

* [ ] `['a', 'b', 'c']`
* [x] `['b', 'c']`
* [ ] `['c']`
* [ ] `['a', 'c']`

> **Wyjaśnienie:** Tryb `"w"` czyści istniejący plik przed zapisem, więc drugie otwarcie usuwa linię `a`. Tryb `"a"` dopisuje na końcu, nie ruszając dotychczasowej zawartości.

#### Q. Przy którym trybie `open()` próba otwarcia nieistniejącego pliku zgłosi `FileNotFoundError`?

* [x] `"r"`
* [ ] `"w"`
* [ ] `"a"`
* [ ] `"w+"`

> **Wyjaśnienie:** Tryb odczytu wymaga istniejącego pliku. Tryby `"w"`, `"a"` i `"w+"` tworzą plik, jeśli go nie ma, przy czym `"w"` i `"w+"` czyszczą istniejący.

#### Q. Co wypisze ten program?

```python
from pathlib import Path

for p in ["projekt/a.py", "projekt/sub/b.py", "projekt/c.txt"]:
    Path(p).parent.mkdir(parents=True, exist_ok=True)
    Path(p).touch()

print(len(list(Path("projekt").glob("*.py"))), len(list(Path("projekt").rglob("*.py"))))
```

* [ ] `2 2`
* [ ] `1 1`
* [x] `1 2`
* [ ] `2 3`

> **Wyjaśnienie:** `glob("*.py")` przeszukuje tylko wskazany katalog, a `rglob("*.py")` także wszystkie podkatalogi. Plik `c.txt` nie pasuje do żadnego z wzorców.

#### Q. Co wypisze ten program w systemie Linux?

```python
import os

print(os.path.join("katalog", "/etc", "plik.txt"))
```

* [ ] `katalog/etc/plik.txt`
* [x] `/etc/plik.txt`
* [ ] `katalog//etc/plik.txt`
* [ ] `katalog/plik.txt`

> **Wyjaśnienie:** Gdy któryś fragment jest ścieżką bezwzględną, `os.path.join` odrzuca wszystkie wcześniejsze fragmenty i zaczyna od niego. Dlatego dołączanych fragmentów nie zaczyna się od ukośnika.

#### Q. Jak usunąć katalog razem z całą jego zawartością?

* [ ] `os.rmdir("katalog")`
* [ ] `os.remove("katalog")`
* [x] `shutil.rmtree("katalog")`
* [ ] `Path("katalog").unlink()`

> **Wyjaśnienie:** `os.rmdir` i `Path.rmdir` usuwają tylko puste katalogi, a `os.remove` i `unlink` służą do plików. Rekurencyjne usuwanie drzewa katalogów zapewnia `shutil.rmtree`, którego trzeba używać ostrożnie.

#### Q. Co wypisze ten program?

```python
import os

os.environ["MOJA_ZMIENNA"] = "42"
print(os.environ.get("MOJA_ZMIENNA") + "1", os.environ.get("NIE_MA_TAKIEJ_ZMIENNEJ_XYZ"))
```

* [ ] `43 None`
* [x] `421 None`
* [ ] `421 ''`
* [ ] Zgłosi `KeyError`

> **Wyjaśnienie:** Wartości zmiennych środowiskowych są zawsze napisami, więc `+` je łączy. Metoda `get()` dla brakującej zmiennej zwraca `None`, a `os.environ["..."]` zgłosiłoby `KeyError`.

#### Q. Skrypt wykonuje `os.environ["TRYB"] = "test"`. Gdzie ta zmienna będzie widoczna?

* [ ] W terminalu, z którego uruchomiono skrypt, także po jego zakończeniu
* [x] W bieżącym procesie i w procesach przez niego uruchomionych
* [ ] We wszystkich procesach w systemie aż do restartu
* [ ] Tylko w funkcji, w której wykonano przypisanie

> **Wyjaśnienie:** Zmiana `os.environ` dotyczy środowiska bieżącego procesu, które dziedziczą jego procesy potomne, np. uruchomione przez `subprocess`. Proces nadrzędny, czyli powłoka, nie widzi tej zmiany.

#### Q. Jaką wartość ma `os.name` w systemie Windows?

* [ ] `'win32'`
* [x] `'nt'`
* [ ] `'windows'`
* [ ] `'posix'`

> **Wyjaśnienie:** `os.name` zwraca ogólną rodzinę systemu: `'nt'` dla Windows i `'posix'` dla Linuksa i macOS. Wartość `'win32'` ma inny atrybut, `sys.platform`, a szczegóły podaje `platform.system()`.

#### Q. Co wypisze ten program?

```python
import logging
import sys

logging.basicConfig(level=logging.WARNING, stream=sys.stdout, format="%(levelname)s:%(message)s")
logging.debug("a")
logging.info("b")
logging.warning("c")
logging.error("d")
```

* [ ] `DEBUG:a`, `INFO:b`, `WARNING:c`, `ERROR:d`
* [x] `WARNING:c`, `ERROR:d`
* [ ] `ERROR:d`
* [ ] `INFO:b`, `WARNING:c`, `ERROR:d`

> **Wyjaśnienie:** Ustawiony poziom działa jak próg: przechodzą komunikaty o poziomie równym lub wyższym. `WARNING` (30) przepuszcza więc `WARNING` i `ERROR`, a odrzuca `DEBUG` (10) i `INFO` (20).

#### Q. Co wypisze ten program?

```python
import logging
import sys

logger = logging.getLogger("app")
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.ERROR)
handler.setFormatter(logging.Formatter("%(levelname)s %(message)s"))
logger.addHandler(handler)

logger.info("start")
logger.warning("uwaga")
logger.error("błąd")
```

* [ ] `INFO start`, `WARNING uwaga`, `ERROR błąd`
* [ ] `WARNING uwaga`, `ERROR błąd`
* [x] `ERROR błąd`
* [ ] Nic nie wypisze

> **Wyjaśnienie:** Komunikat musi przejść przez dwa filtry: poziom loggera (`DEBUG`) i poziom handlera (`ERROR`). Handler odrzuca wszystko poniżej `ERROR`, więc do konsoli trafia tylko ostatni komunikat.

#### Q. Ile razy ten program wypisze `formatuję!`?

```python
import logging

logging.basicConfig(level=logging.WARNING)

class Drogi:
    def __str__(self):
        print("formatuję!")
        return "obiekt"

logging.debug("Dane: %s", Drogi())
logging.debug(f"Dane: {Drogi()}")
```

* [ ] Ani razu
* [x] Raz
* [ ] Dwa razy
* [ ] Cztery razy

> **Wyjaśnienie:** Z `%s` moduł `logging` formatuje komunikat dopiero wtedy, gdy ma go zapisać, a `DEBUG` jest tu odrzucany. f-string jest budowany przed wywołaniem funkcji, więc `__str__` działa niezależnie od poziomu logowania.

#### Q. Jaki poziom ma root logger, jeśli program w ogóle nie konfiguruje modułu `logging`?

* [ ] `DEBUG`
* [ ] `INFO`
* [x] `WARNING`
* [ ] `NOTSET`, więc nic nie jest wypisywane

> **Wyjaśnienie:** Domyślnie root logger ma poziom `WARNING`, dlatego `logging.info()` bez konfiguracji niczego nie wypisuje, a `logging.warning()` trafia na `stderr`. Zmienia to np. `logging.basicConfig(level=logging.INFO)`.

#### Q. Co oznaczają parametry `RotatingFileHandler("app.log", maxBytes=1024, backupCount=3)`?

* [ ] Program zapisze najwyżej 1024 komunikaty, a potem przestanie logować
* [x] Po przekroczeniu 1 KB plik jest rotowany; zostają 3 starsze kopie
* [ ] Co 1024 sekundy powstaje nowy plik, a pliki są trzymane 3 dni
* [ ] Każdy komunikat jest zapisywany do trzech plików jednocześnie

> **Wyjaśnienie:** Gdy `app.log` urośnie ponad `maxBytes`, zmienia nazwę na `app.log.1` (starsze przesuwają się dalej), a najstarsza kopia ponad `backupCount` jest usuwana. Rotację według czasu zapewnia `TimedRotatingFileHandler`.
