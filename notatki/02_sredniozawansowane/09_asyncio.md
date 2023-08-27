## Programowanie asynchroniczne

`asyncio` to biblioteka w języku Python umożliwiająca pisanie jednowątkowego kodu asynchronicznego za pomocą tzw. `coroutine`. Pozwala to na jednoczesne wykonywanie wielu operacji I/O bez konieczności tworzenia wielu wątków lub procesów, co może prowadzić do zwiększenia wydajności, szczególnie w aplikacjach I/O-bound (gdy głównym czynnikiem ograniczającym jest operacja wejścia/wyjścia).

`asyncio` pozwala na skuteczniejsze wykorzystanie jednego wątku, dzięki czemu unikamy problemów związanych z równoczesnym dostępem do pamięci i GIL (Global Interpreter Lock) w Pythonie.

Aby użyć `asyncio`, kluczowym elementem jest deklaracja funkcji jako `async`:

```python
async def my_coroutine():
    print("Start")
    await asyncio.sleep(1)
    print("End after 1 second")
```

W powyższym kodzie używamy `await`, której można używać tylko wewnątrz funkcji zadeklarowanej jako `async`. `await` wskazuje, że w tym miejscu funkcja może zostać "zawieszona", co pozwala na wykonanie innej aktywnej korutyny.

```python

import asyncio

async def main():
    print("Starting")
    await my_coroutine()
    print("Finished")

asyncio.run(main())
```

### Równoległe wykonanie korutyn

Dzięki `asyncio` możemy także łatwo uruchamiać wiele korutyn równolegle:

```python
import asyncio

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def main():
    print("Started")
    
    task1 = asyncio.create_task(say_after(1, "Hello"))
    task2 = asyncio.create_task(say_after(2, "World"))

    await task1
    await task2

    print("Finished")

asyncio.run(main())
```

W powyższym kodzie `asyncio.create_task()` uruchamia korutynę, nie czekając na jej zakończenie. Dzięki temu `say_after(1, "Hello")` i `say_after(2, "World")` są uruchamiane równolegle.

## Jak `asyncio` zwiększa wydajność

Załóżmy, że masz do zrobienia wiele żądań sieciowych do różnych serwisów API. W podejściu synchronicznym żądanie za żądaniem zostanie obsłużone pojedynczo, a każde kolejne żądanie będzie czekać, aż poprzednie się zakończy.

W podejściu asynchronicznym, podczas gdy jedno żądanie czeka na odpowiedź, inne żądania mogą być inicjowane. Gdy żądanie kończy oczekiwanie i otrzymuje odpowiedź, kod kontynuuje działanie z punktu, w którym został zawieszony. Dzięki temu wiele operacji I/O może "czekać" jednocześnie, bez blokowania całego programu.

Przyjrzyjmy się prostemu porównaniu wydajności między podejściem synchronicznym a asynchronicznym przy użyciu żądań HTTP.

**Synchroniczne podejście**:

```python
import requests
import time

urls = ["http://example.com" for _ in range(10)]

start_time = time.time()

for url in urls:
    response = requests.get(url)
    print(response.status_code)

end_time = time.time()
print(f"Synchronicznie: {end_time - start_time} sekund")
```

Asynchroniczne podejście:

```python
import aiohttp
import asyncio
import time

urls = ["http://example.com" for _ in range(10)]

async def fetch(url, session):
    async with session.get(url) as response:
        print(response.status)
        return await response.text()

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(url, session) for url in urls]
        await asyncio.gather(*tasks)

start_time = time.time()
asyncio.run(main())
end_time = time.time()

print(f"Asynchronicznie: {end_time - start_time} sekund")
```

Dla wielu żądań różnica w czasie wykonywania między tymi dwoma podejściami będzie znacząca. Wersja asynchroniczna zwykle będzie znacznie szybsza, ponieważ może jednocześnie inicjować wiele żądań, zamiast czekać na zakończenie każdego z nich osobno.

### Wyzwania 

Używanie `asyncio` w Pythonie, chociaż potężne, może przynieść pewne wyzwania. Aby lepiej zilustrować te trudności, przyjrzyjmy się kilku konkretnym przykładom:

#### 1. Integracja z kodem synchronicznym

**Problem:**  
Załóżmy, że używasz asynchronicznej korutyny do obsługi operacji sieciowej, ale potrzebujesz skorzystać z biblioteki, która działa synchronicznie.

```python
import asyncio
import requests

async def fetch_data():
    response = requests.get("http://example.com")  # synchroniczna operacja
    return response.text

asyncio.run(fetch_data())
```

Trudność:
Wywołanie synchronicznej funkcji requests.get w korutynie blokuje cały loop zdarzeń, co uniemożliwia równoczesne wykonywanie innych korutyn.

#### 2. Debugowanie

**Problem:**
Podczas debugowania napotkasz błąd w jednej z wielu korutyn, które są jednocześnie uruchomione.

```python
async def broken_coroutine():
    await asyncio.sleep(1)
    raise ValueError("Oops!")

async def main():
    task1 = asyncio.create_task(broken_coroutine())
    task2 = asyncio.create_task(another_coroutine())
    await task1
    await task2

asyncio.run(main())
```

**Trudność:**
Zdiagnozowanie, która korutyna jest problematyczna i dlaczego, może być trudniejsze ze względu na asynchroniczne zachowanie i brak tradycyjnego stosu wywołań.

#### 3. Poprawne zarządzanie zasobami

**Problem:**
Tworzenie wielu połączeń bez ich odpowiedniego zamykania.

```python
async def fetch_many():
    urls = ["http://example.com"] * 100
    for url in urls:
        response = await aiohttp.request("GET", url)
        # brak zamknięcia połączenia

asyncio.run(fetch_many())
```

**Trudność:**
Niezamknięte połączenia mogą prowadzić do wycieków zasobów, co obciąża system i może prowadzić do błędów.

#### 4. Asynchroniczne operacje ograniczone przez CPU

**Problem:**
Używanie asynchroniczności do operacji ograniczonych przez CPU.

```python
async def cpu_bound_task(data):
    result = sum([x*x for x in data])
    return result

asyncio.run(cpu_bound_task(range(1000000)))
```

**Trudność:**
Choć asyncio jest doskonałe do operacji ograniczonych przez I/O, nie przyspiesza to operacji ograniczonych przez CPU i może wprowadzać niepotrzebny narzut.
