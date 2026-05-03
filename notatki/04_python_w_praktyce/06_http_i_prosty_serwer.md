## HTTP i prosty serwer

HTTP (Hypertext Transfer Protocol) to **protokół warstwy aplikacji** w modelu OSI, używany głównie do przesyłania danych między klientem (zwykle przeglądarką internetową) a serwerem. Protokół ten opiera się na modelu **żądanie-odpowiedź**, gdzie klient wysyła zapytanie HTTP, a serwer zwraca odpowiedź. HTTP jest **protokółem bezstanowym**, co oznacza, że każde żądanie jest niezależne i serwer nie utrzymuje informacji o poprzednich żądaniach.

### Typy żądań HTTP

HTTP definiuje kilka metod, które określają, jak klient komunikuje się z serwerem:

| Metoda  | Opis                                                                                       |
|---------|---------------------------------------------------------------------------------------------|
| **GET** | Służy do pobierania danych. Powinno być idempotentne, co oznacza, że nie zmienia stanu.     |
| **POST**| Używane do wysyłania danych na serwer, np. tworzenia nowych zasobów. Nie jest idempotentne. |
| **PUT** | Służy do aktualizacji istniejących zasobów lub ich tworzenia, jeśli nie istnieją.           |
| **DELETE** | Usuwa wskazany zasób z serwera.                                                         |
| **HEAD** | Podobne do GET, ale zwraca tylko nagłówki odpowiedzi bez treści.                          |
| **OPTIONS** | Pyta serwer o dostępne metody dla danego zasobu.                                        |

#### Statusy odpowiedzi HTTP

Każda odpowiedź HTTP zawiera kod statusu, który wskazuje na wynik żądania:

| Kod     | Opis                                                                                  |
|---------|----------------------------------------------------------------------------------------|
| **200 OK**           | Żądanie zakończyło się sukcesem.                                           |
| **201 Created**       | Zasób został pomyślnie stworzony (np. przez POST).                        |
| **204 No Content**    | Żądanie zakończyło się sukcesem, ale odpowiedź nie zawiera treści.        |
| **400 Bad Request**   | Żądanie było niepoprawne lub niemożliwe do zrealizowania.                 |
| **401 Unauthorized**  | Klient musi się uwierzytelnić.                                            |
| **403 Forbidden**     | Klient nie ma uprawnień do dostępu do zasobu.                             |
| **404 Not Found**     | Zasób nie został znaleziony.                                              |
| **500 Internal Server Error** | Wewnętrzny błąd serwera.                                          |

### Wysyłanie żądań HTTP w Pythonie

W Pythonie jednym z najczęściej używanych modułów do obsługi żądań HTTP jest `requests`. Jest on prosty w użyciu, a jednocześnie potężny, umożliwiając wykonywanie skomplikowanych operacji HTTP z łatwością. 

Poniżej rozszerzony przykład, który pokazuje, jak wykonać żądanie `GET` oraz jak zarządzać nagłówkami i parametrami:

```python
import requests

url = "https://jsonplaceholder.typicode.com/posts"
headers = {
    'User-Agent': 'my-app/0.0.1',
    'Accept': 'application/json'
}
params = {
    'userId': 1
}

response = requests.get(url, headers=headers, params=params)

print(f'Status code: {response.status_code}')  # Sprawdzenie statusu odpowiedzi
print(f'Response headers: {response.headers}')  # Nagłówki odpowiedzi
print(f'Response JSON: {response.json()}')      # Zawartość odpowiedzi w formacie JSON
```

W powyższym przykładzie dodano nagłówki oraz parametry zapytania, co pokazuje elastyczność modułu `requests`. Dzięki temu można modyfikować żądania w zależności od potrzeb aplikacji.

### Serwer HTTP

Python dostarcza moduł `http.server`, który umożliwia uruchomienie prostego serwera HTTP. Jest to szczególnie przydatne w fazie rozwoju, kiedy chcemy przetestować naszą stronę lub aplikację lokalnie. Serwer ten jest jednak **prosty i nie powinien być używany w środowisku produkcyjnym**, ponieważ nie zapewnia zabezpieczeń ani wydajności odpowiedniej dla rzeczywistych aplikacji.

#### Prosty serwer HTTP

Poniższy przykład pokazuje, jak uruchomić prosty serwer HTTP, który serwuje pliki z bieżącego katalogu:

```python
import http.server
import socketserver

PORT = 8000
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving files from the current directory at port {PORT}")
    httpd.serve_forever()
```

- `http.server.SimpleHTTPRequestHandler`: Domyślna klasa obsługująca żądania GET i HEAD, serwująca pliki z katalogu, w którym uruchomiono serwer.
- `socketserver.TCPServer`: Klasa obsługująca nasłuchiwanie na porcie TCP. W powyższym przykładzie serwer nasłuchuje na porcie 8000.

#### Dostosowywanie serwera

Aby dostosować serwer do specyficznych potrzeb, można rozszerzyć klasę `SimpleHTTPRequestHandler`, np. aby obsługiwać dodatkowe metody HTTP, takie jak POST. Poniżej przedstawiam przykład niestandardowej obsługi żądań:

```python
class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"Custom GET response")

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        print(f"Received POST data: {post_data.decode('utf-8')}")

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"POST received")

PORT = 8000
with socketserver.TCPServer(("", PORT), CustomHTTPRequestHandler) as httpd:
    print(f"Serving custom responses at port {PORT}")
    httpd.serve_forever()
```

- Metoda `do_GET`: Przykład niestandardowej odpowiedzi na żądanie GET, w której ręcznie wysyłamy nagłówki oraz zawartość odpowiedzi.
- Metoda `do_POST`: Odbiera dane z żądania POST, przetwarza je, a następnie zwraca odpowiedź. 

Takie podejście daje pełną kontrolę nad tym, jak serwer ma odpowiadać na różne typy żądań, co może być szczególnie przydatne podczas tworzenia API lub prostych aplikacji webowych bez konieczności korzystania z zewnętrznych frameworków.

#### Wady prostego serwera

Mimo że serwer dostarczany przez moduł `http.server` jest wygodny, jego ograniczenia sprawiają, że nie nadaje się do użytku produkcyjnego:

- Serwer ten nie obsługuje HTTPS, co czyni go nieodpowiednim dla aplikacji wymagających bezpiecznego połączenia.
- Prosty serwer nie radzi sobie z większą liczbą jednoczesnych połączeń.
- Domyślnie serwer działa w trybie jednoprocesowym, co oznacza, że każde żądanie jest obsługiwane sekwencyjnie.

### Zaawansowane użycie modułu `requests`

#### POST, PUT, DELETE i obsługa danych JSON

```python
import requests

base_url = "https://jsonplaceholder.typicode.com"

# POST — tworzenie nowego zasobu
nowy_post = {
    "title": "Nowy post",
    "body": "Treść posta",
    "userId": 1
}
odpowiedz = requests.post(f"{base_url}/posts", json=nowy_post)
print(odpowiedz.status_code)   # 201 Created
print(odpowiedz.json())

# PUT — aktualizacja zasobu
aktualizacja = {"title": "Zmieniony tytuł", "body": "Nowa treść", "userId": 1}
odpowiedz = requests.put(f"{base_url}/posts/1", json=aktualizacja)
print(odpowiedz.status_code)   # 200 OK

# DELETE — usunięcie zasobu
odpowiedz = requests.delete(f"{base_url}/posts/1")
print(odpowiedz.status_code)   # 200 OK
```

#### Obsługa błędów i timeouty

```python
import requests
from requests.exceptions import Timeout, ConnectionError, HTTPError

try:
    odpowiedz = requests.get("https://example.com/api/data", timeout=5)
    odpowiedz.raise_for_status()   # Rzuca HTTPError dla 4xx i 5xx
    print(odpowiedz.json())
except Timeout:
    print("Żądanie przekroczyło limit czasu")
except ConnectionError:
    print("Błąd połączenia — brak internetu lub błędny host")
except HTTPError as e:
    print(f"Błąd HTTP: {e.response.status_code}")
```

#### Sesje — wielokrotne żądania z tymi samymi parametrami

Sesja (`Session`) zachowuje cookies i nagłówki między żądaniami:

```python
import requests

with requests.Session() as sesja:
    # Ustawienie wspólnych nagłówków dla wszystkich żądań w sesji
    sesja.headers.update({
        "Authorization": "Bearer moj-token",
        "Accept": "application/json"
    })

    # Pierwsze żądanie — logowanie
    odpowiedz = sesja.post("https://api.example.com/login",
                           json={"user": "jan", "password": "tajne"})

    # Kolejne żądania używają tych samych cookies i nagłówków
    profil = sesja.get("https://api.example.com/profile")
    print(profil.json())
```

### Moduł `urllib` — standardowa biblioteka

Dla prostych przypadków nie potrzebujemy `requests` — wystarczy wbudowany `urllib.request`:

```python
import urllib.request
import urllib.parse
import json

# GET
with urllib.request.urlopen("https://jsonplaceholder.typicode.com/posts/1") as resp:
    dane = json.loads(resp.read().decode())
    print(dane["title"])

# POST
dane_post = json.dumps({"title": "test", "body": "treść", "userId": 1}).encode()
req = urllib.request.Request(
    "https://jsonplaceholder.typicode.com/posts",
    data=dane_post,
    headers={"Content-Type": "application/json"},
    method="POST"
)
with urllib.request.urlopen(req) as resp:
    print(resp.status)   # 201
```

### Nagłówki i uwierzytelnianie

```python
import requests
from requests.auth import HTTPBasicAuth, HTTPDigestAuth

# Basic Auth
odpowiedz = requests.get("https://httpbin.org/basic-auth/user/pass",
                         auth=HTTPBasicAuth("user", "pass"))
print(odpowiedz.status_code)   # 200

# Token Bearer (JWT)
headers = {"Authorization": "Bearer eyJhbGci..."}
odpowiedz = requests.get("https://api.example.com/secure", headers=headers)

# API Key w parametrach zapytania
odpowiedz = requests.get("https://api.example.com/data",
                         params={"api_key": "moj-klucz-api"})
```
