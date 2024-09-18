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
