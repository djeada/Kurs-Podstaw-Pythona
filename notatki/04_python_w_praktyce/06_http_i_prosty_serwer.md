## HTTP i prosty serwer

HTTP (Hypertext Transfer Protocol) to protokół sieciowy używany do przesyłania danych między klientem (zwykle przeglądarką internetową) a serwerem. Umożliwia on przesyłanie różnych rodzajów danych, takich jak strony internetowe, obrazy, filmy czy inne zasoby.

### Wysyłanie żądań HTTP w Pythonie

W Pythonie istnieje wiele narzędzi do obsługi żądań HTTP, ale jednym z najpopularniejszych i najłatwiejszych w użyciu jest moduł `requests`. Pozwala on na wykonywanie różnych rodzajów żądań HTTP, takich jak `GET`, `POST`, `PUT`, `DELETE` i innych. 

Poniżej przedstawiam przykład, jak wykonać żądanie `GET`:

```python
import requests

url = "https://www.google.com"
response = requests.get(url)

print(response.status_code) # Kod odpowiedzi (np. 200 oznacza sukces)
print(response.text)       # Zawartość odpowiedzi
```

Moduł requests umożliwia również dodawanie nagłówków, parametrów czy danych do żądań, co czyni go bardzo elastycznym narzędziem.

### Serwer HTTP

Python oferuje narzędzia pozwalające na łatwe i szybkie uruchomienie serwera HTTP dzięki wbudowanemu modułowi `http.server`.

#### Prosty serwer

Domyślnie, serwując pliki z bieżącego katalogu (takie jak `index.html`), można użyć poniższego kodu, aby uruchomić serwer nasłuchujący na porcie 8000:

```python
import http.server
import socketserver

PORT = 8000
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving files from the current directory at port {PORT}")
    httpd.serve_forever()
```

Aby ustawić konkretną ścieżkę (katalog) do serwowania plików zamiast domyślnego bieżącego katalogu, można skorzystać z klasy `SimpleHTTPRequestHandler` i zmienić wartość atrybutu `directory`.

#### Zaawansowane dostosowywanie:

Dla bardziej złożonych wymagań, klasy SimpleHTTPRequestHandler można rozszerzyć, dostosowując metody do obsługi różnych typów żądań HTTP:

```python
class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Obsługa niestandardowych żądań GET
        pass

    def do_POST(self):
        # Obsługa niestandardowych żądań POST
        pass

# ...

with socketserver.TCPServer(("", PORT), CustomHTTPRequestHandler) as httpd:
    print(f"Serving with custom request handling at port {PORT}")
    httpd.serve_forever()
```

Tak dostosowany serwer umożliwia precyzyjne obsługiwanie żądań klienta, umożliwiając tworzenie aplikacji internetowych i API z wykorzystaniem czystego Pythona.

Uwaga: Prosty serwer HTTP jest odpowiedni do celów testowych lub deweloperskich, ale nie jest zalecany do użycia w środowisku produkcyjnym.
