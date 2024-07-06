## Tworzenie API przy użyciu FastAPI

FastAPI to nowoczesne, wydajne i łatwe w użyciu narzędzie do tworzenia API w Pythonie. Za jego popularność odpowiada prostota tworzenia aplikacji, wbudowana walidacja danych oraz automatyczne generowanie dokumentacji.

### Instalacja FastAPI

Aby zacząć pracę z FastAPI, musisz najpierw zainstalować odpowiednie pakiety. Oprócz samego FastAPI warto zainstalować serwer ASGI, np. `uvicorn`, który pozwoli na uruchamianie aplikacji:

```bash
pip install fastapi uvicorn
```

### Tworzenie prostego API

Rozpocznij od utworzenia instancji FastAPI i zdefiniowania kilku ścieżek:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}
```

Aby uruchomić powyższe API, zapisz kod do pliku, np. main.py, a następnie uruchom serwer za pomocą uvicorn:

```bash
uvicorn main:app --reload
```

Po uruchomieniu przejdź do przeglądarki i otwórz adres `http://localhost:8000` - zobaczysz odpowiedź z powitaniem.

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

Aby komunikować się z API w Pythonie, potrzebujemy biblioteki `requests`, którą możemy zainstalować za pomocą poniższej komendy:

```bash
pip install requests
```

Poniżej znajdują się przykłady jak używać tej biblioteki do tworzenia, pobierania i usuwania przedmiotów za pomocą API.

#### Tworzenie przedmiotu (POST)

Używając metody `requests.post`, możemy wysłać dane w formacie JSON do endpointu `/items/`, aby utworzyć nowy przedmiot. Poniżej znajduje się przykład kodu:

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
print(response.json())  # Wyświetlenie odpowiedzi w formacie JSON
```

#### Pobieranie przedmiotu (GET)

Aby pobrać dane konkretnego przedmiotu, możemy użyć metody `requests.get` z odpowiednim `item_id`. Poniżej znajduje się przykład kodu:

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

#### Usuwanie przedmiotu (DELETE)

Aby usunąć przedmiot na podstawie `item_id`, możemy użyć metody `requests.delete`. Poniżej znajduje się przykład kodu:

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
