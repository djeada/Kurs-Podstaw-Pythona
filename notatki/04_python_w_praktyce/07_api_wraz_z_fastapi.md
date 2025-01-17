## Tworzenie API przy użyciu FastAPI

FastAPI to nowoczesne, wydajne i łatwe w użyciu narzędzie do tworzenia API w Pythonie. Za jego popularność odpowiada prostota tworzenia aplikacji, wbudowana walidacja danych oraz automatyczne generowanie dokumentacji.

### Instalacja FastAPI

Aby zacząć pracę z FastAPI, musisz najpierw zainstalować odpowiednie pakiety. Oprócz samego FastAPI warto zainstalować serwer ASGI, np. `uvicorn`, który pozwoli na uruchamianie aplikacji:

```bash
pip install fastapi uvicorn
```

### Tworzenie prostego API

Tworzenie API (Application Programming Interface) pozwala na komunikację między różnymi aplikacjami. W tym przykładzie wykorzystamy **FastAPI**, nowoczesny, szybki framework webowy dla Pythona, który ułatwia tworzenie API.

#### Tworzenie instancji FastAPI i definiowanie ścieżek

Rozpocznij od utworzenia instancji FastAPI i zdefiniowania kilku ścieżek (endpointów), które będą obsługiwać różne żądania HTTP.

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
```

**Wyjaśnienie:**

- `app = FastAPI()` – tworzy instancję aplikacji FastAPI.
- `@app.get("/")` – dekorator definiujący ścieżkę dla żądania GET na endpoint `/`.
- `read_root()` – funkcja obsługująca żądanie GET na `/`, zwracająca prosty słownik.
- `@app.get("/items/{item_id}")` – dynamiczny endpoint, który przyjmuje parametr `item_id`.
- `read_item(item_id: int, q: str = None)` – funkcja obsługująca żądanie, gdzie `item_id` jest wymaganym parametrem, a `q` jest opcjonalnym zapytaniem.

#### Krok 3: Uruchamianie serwera

Aby uruchomić powyższe API, zapisz kod do pliku, np. `main.py`. Następnie masz kilka opcji uruchomienia serwera:

##### Opcja 1: Uruchomienie za pomocą Uvicorn z linii komend

```bash
uvicorn main:app --reload
```

**Wyjaśnienie:**

- `main:app` – odnosi się do obiektu `app` w pliku `main.py`.
- `--reload` – automatycznie restartuje serwer przy zmianach w kodzie (przydatne w trakcie developmentu).

##### Opcja 2: Uruchomienie za pomocą skryptu Pythona

Możesz również uruchomić Uvicorn bezpośrednio z kodu Pythona:

```python
import uvicorn

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
```

**Wyjaśnienie:**

- Importujesz `uvicorn` i wywołujesz `uvicorn.run()` z odpowiednimi parametrami.
- Umożliwia to uruchomienie serwera bezpośrednio z pliku Python, co może być przydatne w niektórych środowiskach lub integracjach.

#### Co to jest Uvicorn?

**Uvicorn** to szybki, asynchroniczny serwer ASGI napisany w Pythonie, używany do uruchamiania aplikacji webowych opartych na ASGI, takich jak FastAPI. Umożliwia obsługę wielu żądań jednocześnie dzięki asynchronicznej naturze.

**Alternatywy dla Uvicorn:**

1. **Hypercorn** – inny serwer ASGI wspierający różne protokoły, takie jak HTTP/1, HTTP/2 i WebSocket.
2. **Daphne** – serwer ASGI rozwijany jako część projektu Django Channels.
3. **Gunicorn** z workerami ASGI (np. `uvicorn.workers.UvicornWorker`) – popularny serwer WSGI, który można skonfigurować do obsługi ASGI.

#### Różnice między uruchamianiem na Windows a Linux

Jeśli planujesz uruchomić serwer z linii komend (cmd), warto zwrócić uwagę na kilka różnic między systemami operacyjnymi:

**Instalacja pakietów:**

- Na Windowsie używasz zazwyczaj `pip` bez dodatkowych modyfikacji.
- Na Linux może być konieczne użycie `sudo` dla instalacji globalnych lub korzystanie z wirtualnych środowisk.

**Ścieżki plików:**

- Windows używa backslash (`\`), podczas gdy Linux używa slash (`/`).
- W kodzie Python, aby zachować kompatybilność, warto używać modułu `os.path` lub `pathlib`.

**Uruchamianie skryptów:**

- Na Windowsie możesz uruchomić skrypt bezpośrednio z `cmd` lub PowerShell.
- Na Linux możesz użyć terminala oraz skryptów bash.

**Zarządzanie procesami:**

- Linux oferuje narzędzia takie jak `systemd` do zarządzania usługami.
- Windows posiada własne mechanizmy zarządzania usługami, ale często używa się dodatkowych narzędzi.

**Co sprawdzić przed uruchomieniem:**

1. Upewnij się, że Python jest zainstalowany i dostępny w zmiennej środowiskowej PATH.
2. Zaleca się używanie wirtualnych środowisk (`venv` lub `virtualenv`) dla izolacji zależności.
3. Upewnij się, że wybrany port (domyślnie 8000) jest dostępny i nie jest blokowany przez zaporę sieciową.
4. Na Linuxie, uruchamianie na portach poniżej 1024 może wymagać uprawnień administratora.

#### Uruchamianie serwera

Po uruchomieniu serwera możesz przejść do przeglądarki i otworzyć adres `http://localhost:8000`. Zobaczysz odpowiedź z powitaniem:

```json
{
  "Hello": "World"
}
```

Dodatkowo, FastAPI automatycznie generuje interaktywną dokumentację API dostępną pod adresami:

- **Swagger UI:** `http://localhost:8000/docs`
- **ReDoc:** `http://localhost:8000/redoc`

Możesz tam przetestować swoje endpointy bezpośrednio z przeglądarki.

### Przykładowe API

#### Model danych

Jednym z popularnych narzędzi do definiowania i walidacji modelu danych jest **Pydantic**. Dzięki niemu możemy w sposób deklaratywny określić strukturę naszych danych oraz oczekiwane typy wartości.

Poniżej mamy przykład modelu **Item**:

```
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

items = {}  # prosty "słownik" do przechowywania danych

class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None
```

Model ten przedstawia przedmiot, który posiada następujące atrybuty:

- `name`: Nazwa przedmiotu. Jest to pole wymagane i powinno być typu `str`.
- `description`: Opis przedmiotu. Jest to pole opcjonalne i również powinno być typu `str`.
- `price`: Cena przedmiotu. Jest to pole wymagane i powinno być typu `float` lub `int`.
- `tax`: Podatek dla danego przedmiotu. Jest to pole opcjonalne i, jeśli podane, powinno być typu `float` lub `int`.

#### Tworzenie przedmiotu (POST)

- Ścieżka: `/items/`
- Przyjmuje dane przedmiotu w formacie JSON.
- Zwraca dane stworzonego przedmiotu.
- Wewnętrznie, przedmiot jest dodawany do słownika (`items`) z unikalnym ID.

```
@app.post("/items/")
def create_item(item: Item):
    item_id = len(items) + 1
    items[item_id] = item
    return {"id": item_id, **item.dict()}
```
  
#### Pobieranie przedmiotu (GET)

- Ścieżka: `/items/{item_id}`
- Na podstawie przekazanego `item_id` zwraca dane przedmiotu.
- Jeśli przedmiot o danym ID nie istnieje, zwraca błąd 404.
     
```
@app.get("/items/{item_id}")
def read_item(item_id: int):
    item = items.get(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item
```

#### Usuwanie przedmiotu (DELETE)

- Ścieżka: `/items/{item_id}`
- Na podstawie przekazanego `item_id` usuwa przedmiot.
- Zwraca informację o sukcesie operacji.
- Jeśli przedmiot o danym ID nie istnieje, zwraca błąd 404.
     
```python
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    del items[item_id]
    return {"status": "success"}
```
### Pełny kod API do zarządzania przedmiotami

Poniżej znajduje się pełny, wykonywalny przykład API do zarządzania przedmiotami, wykorzystujący biblioteki FastAPI oraz Pydantic do definicji modelu danych. Zawiera definicję modelu oraz funkcje do tworzenia, odczytywania i usuwania przedmiotów przechowywanych w prostym słowniku.

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn

app = FastAPI()

# Przechowywanie danych w słowniku
items = {}

# Definicja modelu danych przy użyciu Pydantic
class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

# Endpoint do tworzenia przedmiotu (POST)
@app.post("/items/")
def create_item(item: Item):
    item_id = len(items) + 1
    items[item_id] = item
    return {"id": item_id, **item.dict()}

# Endpoint do odczytywania przedmiotu (GET)
@app.get("/items/{item_id}")
def read_item(item_id: int):
    item = items.get(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

# Endpoint do usuwania przedmiotu (DELETE)
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    del items[item_id]
    return {"status": "success"}

# Uruchomienie serwera
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
```

### Uruchomienie serwera

Funkcja `uvicorn.run(app, host="127.0.0.1", port=8000)` określa, że aplikacja ma być dostępna pod adresem localhost (127.0.0.1) na porcie 8000.

Aby uruchomić ten serwer, wystarczy, że uruchomisz ten plik bezpośrednio z Pythona, używając polecenia:

```bash
python nazwa_pliku.py
```

Gdzie `nazwa_pliku.py` to nazwa pliku, w którym umieściłeś powyższy kod.

### Swagger UI

Swagger UI jest automatycznie generowanym interfejsem użytkownika dla dokumentacji API, dostępnym w FastAPI dzięki integracji z OpenAPI. Dostarcza on przeglądarkę dokumentacji, która pozwala na interaktywne eksplorowanie API, wykonywanie żądań i przeglądanie odpowiedzi bezpośrednio z przeglądarki internetowej.

- Po uruchomieniu serwera (jak opisano wcześniej), Swagger UI jest dostępny pod adresem: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).
- Strona będzie zawierać interfejs z wszystkimi zdefiniowanymi endpointami, jak na poniższym zrzucie ekranu:

![Swagger UI Example](https://github.com/djeada/Kurs-Podstaw-Pythona/assets/37275728/c3b57b80-b724-4f3b-ad51-566d465eda62)

#### Funkcjonalności Swagger UI

- Możesz wysyłać żądania do swojego API bezpośrednio z Swagger UI, co ułatwia testowanie i debugowanie.
- Dla każdego endpointu, możesz zobaczyć oczekiwane parametry, odpowiedzi oraz statusy HTTP.
- Swagger UI generuje dokumentację na podstawie kodu źródłowego i komentarzy, więc jest zawsze aktualna z najnowszymi zmianami w API.

#### Korzyści z używania Swagger UI

- Swagger UI jest wbudowany w FastAPI i nie wymaga dodatkowej konfiguracji poza standardowym uruchomieniem aplikacji.
- Dzięki czytelnej dokumentacji, inni programiści mogą łatwiej korzystać z Twojego API i integrować je z własnymi aplikacjami.

### Korzystanie z API przy użyciu requests

Aby komunikować się z API w Pythonie, potrzebujemy biblioteki `requests`, która upraszcza proces wysyłania żądań HTTP i obsługi odpowiedzi. Bibliotekę tę możemy zainstalować za pomocą poniższej komendy:

```bash
pip install requests
```

Biblioteka `requests` jest niezwykle popularna ze względu na swoją prostotę i elastyczność. Umożliwia łatwe wysyłanie różnych typów żądań HTTP (GET, POST, PUT, DELETE itp.), zarządzanie nagłówkami, obsługę parametrów zapytań oraz przetwarzanie odpowiedzi w formatach takich jak JSON.

Poniżej znajdują się przykłady, jak używać tej biblioteki do tworzenia, pobierania i usuwania przedmiotów za pomocą API.

#### Tworzenie przedmiotu (POST)

Metoda `requests.post` pozwala na wysłanie danych w formacie JSON do określonego endpointu API, co zazwyczaj służy do tworzenia nowych zasobów na serwerze. W tym przypadku tworzymy nowy przedmiot w systemie.

**Przykład kodu:**

```python
import requests

# URL API
url = "http://127.0.0.1:8000/items/"

# Dane przedmiotu
item_data = {
    "name": "example",
    "description": "This is an example item",
    "price": 10.0,
    "tax": 2.0
}

# Wysłanie żądania POST
response = requests.post(url, json=item_data)

# Wyświetlenie odpowiedzi
print(response.status_code)  # Sprawdzenie statusu odpowiedzi
print(response.json())       # Wyświetlenie odpowiedzi w formacie JSON
```

**Szczegółowe wyjaśnienie:**

1. Najpierw importujemy bibliotekę `requests`, która umożliwia nam interakcję z API.
2. `url` wskazuje na endpoint API, do którego wysyłamy żądanie. W tym przypadku jest to lokalny serwer działający na porcie 8000.
3. `item_data` to słownik zawierający dane nowego przedmiotu, które chcemy utworzyć. Dane te zostaną automatycznie przekształcone do formatu JSON przez parametr `json` w metodzie `post`.
4. Metoda `requests.post` wysyła żądanie POST do określonego URL z przekazanymi danymi.
5. `response.status_code` pozwala na sprawdzenie, czy żądanie zakończyło się sukcesem (np. status 201 Created), a `response.json()` zwraca odpowiedź serwera w formacie JSON, co może zawierać szczegóły utworzonego przedmiotu.

#### Pobieranie przedmiotu (GET)

Aby pobrać dane konkretnego przedmiotu, używamy metody `requests.get` z odpowiednim `item_id`. Żądanie GET służy do odczytywania danych z serwera bez ich modyfikacji.

**Przykład kodu:**

```python
import requests

# URL API z dodanym item_id
url = "http://127.0.0.1:8000/items/1"

# Wysłanie żądania GET
response = requests.get(url)

# Wyświetlenie odpowiedzi
if response.status_code == 200:
    print(response.json())  # Wyświetlenie danych przedmiotu
else:
    print("Item not found")  # Wyświetlenie informacji, jeśli przedmiot nie został znaleziony
```

**Szczegółowe wyjaśnienie:**

1. Podobnie jak wcześniej, importujemy `requests`.
2. `url` zawiera endpoint API wraz z identyfikatorem przedmiotu, który chcemy pobrać (w tym przypadku `1`).
3. Metoda `requests.get` wysyła żądanie GET do określonego URL.
4. Sprawdzamy status odpowiedzi. Jeśli status to `200 OK`, oznacza to, że przedmiot został znaleziony i możemy wyświetlić jego dane. W przeciwnym razie informujemy użytkownika, że przedmiot nie został znaleziony.

**Dodatkowe informacje:**

I. Parametry zapytania: 

Jeśli API obsługuje filtrowanie lub paginację, możemy przekazać dodatkowe parametry za pomocą argumentu `params`. Przykład:

```python
params = {'category': 'electronics', 'limit': 10}
response = requests.get(url, params=params)
```

II. Nagłówki: 

Możemy również dodać nagłówki do żądania, takie jak autoryzacja czy specyficzne formaty odpowiedzi.

```python
headers = {'Authorization': 'Bearer YOUR_TOKEN'}
response = requests.get(url, headers=headers)
```

#### Usuwanie przedmiotu (DELETE)

Aby usunąć przedmiot na podstawie `item_id`, używamy metody `requests.delete`. Żądanie DELETE służy do usuwania zasobów z serwera.

**Przykład kodu:**

```python
import requests

# URL API z dodanym item_id
url = "http://127.0.0.1:8000/items/1"

# Wysłanie żądania DELETE
response = requests.delete(url)

# Wyświetlenie odpowiedzi
if response.status_code == 200:
    print(response.json())  # Wyświetlenie statusu usunięcia
else:
    print("Item not found")  # Wyświetlenie informacji, jeśli przedmiot nie został znaleziony
```

**Szczegółowe wyjaśnienie:**

1. Importujemy `requests`.
2. `url` zawiera endpoint API wraz z identyfikatorem przedmiotu do usunięcia.
3. Metoda `requests.delete` wysyła żądanie DELETE do określonego URL.
4. Jeśli status odpowiedzi to `200 OK`, oznacza to, że przedmiot został pomyślnie usunięty, a serwer może zwrócić potwierdzenie w formacie JSON. Jeśli przedmiot nie został znaleziony, informujemy o tym użytkownika.

**Dodatkowe informacje:**

- Usuwanie zasobów jest operacją potencjalnie niebezpieczną. Upewnij się, że masz odpowiednie uprawnienia oraz że operacja jest chroniona przed nieautoryzowanym dostępem.
- Metoda DELETE jest **idempotentna**, co oznacza, że wielokrotne wykonanie tego samego żądania DELETE nie zmieni stanu serwera po pierwszym usunięciu zasobu.

#### Dodatkowe wskazówki dotyczące korzystania z biblioteki requests

I. Obsługa błędów:

Biblioteka `requests` pozwala na łatwą obsługę błędów poprzez sprawdzanie statusów odpowiedzi. Możemy również użyć wyjątków do zarządzania nieoczekiwanymi sytuacjami.

```python
try:
   response = requests.get(url)
   response.raise_for_status()  # Podniesie wyjątek dla statusów błędu
   data = response.json()
except requests.exceptions.HTTPError as err:
   print(f"HTTP error occurred: {err}")
except requests.exceptions.RequestException as err:
   print(f"Other error occurred: {err}")

```

II. Autoryzacja:

Jeśli API wymaga uwierzytelnienia, możemy dodać odpowiednie nagłówki lub użyć mechanizmów takich jak tokeny Bearer.

```python
headers = {
   'Authorization': 'Bearer YOUR_ACCESS_TOKEN',
   'Content-Type': 'application/json'
}
response = requests.get(url, headers=headers)
```

III. Wysyłanie danych w innych formatach:

Chociaż JSON jest najczęściej używanym formatem, `requests` umożliwia wysyłanie danych w innych formatach, takich jak formy HTML czy pliki.

```python
# Wysyłanie danych jako formularz

form_data = {'field1': 'value1', 'field2': 'value2'}
response = requests.post(url, data=form_data)

# Wysyłanie pliku

files = {'file': open('report.xls', 'rb')}
response = requests.post(url, files=files)

```

IV. Parametryzacja URL:

Dla bardziej dynamicznych URL-ów możemy użyć funkcji formatowania stringów lub modułu `urllib.parse`.

```python
item_id = 1
url = f"http://127.0.0.1:8000/items/{item_id}"
# lub
from urllib.parse import urljoin
base_url = "http://127.0.0.1:8000/items/"
url = urljoin(base_url, str(item_id))
```

V. Timeouts:

Aby zapobiec zawieszaniu się programu w przypadku braku odpowiedzi z serwera, warto ustawić limit czasu dla żądań.

```python
response = requests.get(url, timeout=5)  # Timeout po 5 sekundach
```

VI. Sesje:

Używanie obiektów sesji (`requests.Session`) pozwala na utrzymanie pewnych parametrów między żądaniami, takich jak nagłówki czy ciasteczka.

```python
session = requests.Session()
session.headers.update({'Authorization': 'Bearer YOUR_ACCESS_TOKEN'})

response = session.get(url)
response = session.post(url, json=item_data)
```
