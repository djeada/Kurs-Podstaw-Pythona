
### HTTP i prosty serwer

HTTP (Hypertext Transfer Protocol) jest protokołem sieciowym używanym do przesyłania danych między klientem a serwerem. Jest to podstawowa technologia używana do przeglądania stron internetowych oraz komunikacji między aplikacjami.

Aby wysłać żądanie HTTP w Pythonie, można użyć modułu `requests`. Poniższy przykład pokazuje, jak wysłać żądanie typu `GET` do strony internetowej i otrzymać odpowiedź z serwera:

    import requests

    url = "https://www.google.com"
    response = requests.get(url)

    print(response.status_code) # sprawdzamy kod odpowiedzi
    print(response.text) # wyświetlamy zawartość odpowiedzi

Możliwe jest również wysyłanie żądań `POST`, `PUT`, `DELETE` itp. oraz dodawanie nagłówków i danych do żądania.

Jeśli chcesz stworzyć prosty serwer HTTP w Pythonie, możesz użyć modułu http.server. Poniższy przykład pokazuje, jak stworzyć serwer, który nasłuchuje na porcie 8000 i wyświetla zawartość pliku `index.html` po otrzymaniu żądania `GET`:

    import http.server
    import socketserver

    PORT = 8000

    Handler = http.server.SimpleHTTPRequestHandler

    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("serving at port", PORT)
        httpd.serve_forever()

Możesz również dostosować handler, aby obsługiwać różne typy żądań i odpowiednio reagować na nie.