
## API wraz z FastAPI

FastAPI to nowoczesne i szybkie narzędzie do tworzenia API w Pythonie. Jest oparte na bibliotece Starlette i używa Pydantic do walidacji danych wejściowych.

Aby rozpocząć pracę z FastAPI, należy najpierw zainstalować je za pomocą komendy:

```python
pip install fastapi
```

Przykład prostego API z FastAPI:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}
```

API może przyjmować różne metody HTTP (np. `GET`, `POST`, `DELETE`) oraz zwracać różne formaty danych (np. JSON, HTML).

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

@app.post("/items/")
def create_item(item: Item):
    return item
```

W powyższym przykładzie zdefiniowano nowy model danych - Item, który jest walidowany przy użyciu Pydantic. Następnie zdefiniowano nową ścieżkę `/items/` dostępną dla metody POST, która przyjmuje obiekt item i zwraca go jako odpowiedź.

FastAPI posiada też mechanizm do automatycznej generacji dokumentacji dla API. Aby skorzystać z tej funkcjonalności, należy użyć dekoratora `@app.docs` i odpowiednio opisać poszczególne ścieżki i modele danych.

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

@app.post("/items/")
@app.docs(
    summary="Create a new item",
    description="This endpoint allows you to create a new item in the store",
    responses={
        200: {"description": "Success"},
        404: {"description": "Not found"},
    },
)
def create_item(item: Item):
    return item
```

Aby uruchomić aplikację, wystarczy wywołać metodę `run()` na obiekcie reprezentującym aplikację:

```python
if __name__ == "__main__":
    app.run()
```

Po uruchomieniu aplikacji możesz otworzyć adres `http://localhost:8000/` w przeglądarce, aby zobaczyć odpowiedź zwróconą przez endpoint.

FastAPI oferuje również możliwość walidacji danych wejściowych i zwracanych przez endpointy. Możesz użyć typów Pythona, takich jak `int` lub `str`, aby opisać argumenty wejściowe oraz typ zwracany przez endpoint. FastAPI automatycznie sprawdzi, czy dane wejściowe są poprawne.