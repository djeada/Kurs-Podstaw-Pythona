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

### Korzystanie z API przy użyciu requests

Do komunikacji z API, instalujemy bibliotekę `requests` za pomocą komendy: `pip install requests`.

#### Tworzenie przedmiotu (POST)

- Używając metody `requests.post`, wysyłamy dane w formacie JSON do endpointu `/items/`.
- Przykład: `response = requests.post(url + '/items/', json=item_data)`

```python
import requests

# Tworzenie (POST)
item_data = {"name": "example", "price": 10.0}
response = requests.post("http://127.0.0.1:8000/items/", json=item_data)
print(response.json())
```

#### Pobieranie przedmiotu (GET)

- Korzystając z metody `requests.get`, możemy pobrać dane przedmiotu.
- Przykład: `response = requests.get(url + f'/items/{item_id}')`

```python
# Pobieranie (GET)
response = requests.get("http://127.0.0.1:8000/items/1")
print(response.json())
```

#### Usuwanie przedmiotu (DELETE)

- Metoda `requests.delete` pozwala usunąć przedmiot na podstawie `item_id`.
- Przykład: `response = requests.delete(url + f'/items/{item_id}')`

```python
# Usuwanie (DELETE)
response = requests.delete("http://127.0.0.1:8000/items/1")
print(response.json())
```
