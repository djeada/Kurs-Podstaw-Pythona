## Programowanie asynchroniczne

Programowanie asynchroniczne to styl programowania, który pozwala na wykonywanie operacji bez blokowania głównego wątku programu. Oznacza to, że operacje mogą być uruchamiane równocześnie, a program może reagować na ich zakończenie w sposób nieblokujący.

`asyncio` to biblioteka w języku Python umożliwiająca pisanie jednowątkowego kodu asynchronicznego za pomocą tzw. `coroutine`. Pozwala to na jednoczesne wykonywanie wielu operacji I/O bez konieczności tworzenia wielu wątków lub procesów, co może prowadzić do zwiększenia wydajności, szczególnie w aplikacjach I/O-bound (gdy głównym czynnikiem ograniczającym jest operacja wejścia/wyjścia).

`asyncio` pozwala na skuteczniejsze wykorzystanie jednego wątku, dzięki czemu unikamy problemów związanych z równoczesnym dostępem do pamięci i GIL (Global Interpreter Lock) w Pythonie.

### Podstawy `asyncio`

Aby użyć `asyncio`, kluczowym elementem jest deklaracja funkcji jako `async`:

```python
async def moja_korutyna():
    print("Początek")
    await asyncio.sleep(1)
    print("Koniec po 1 sekundzie")
```

W powyższym kodzie używamy `await`, której można używać tylko wewnątrz funkcji zadeklarowanej jako `async`. `await` wskazuje, że w tym miejscu funkcja może zostać "zawieszona", co pozwala na wykonanie innej aktywnej korutyny.

### Przykład użycia `asyncio`

```python
import asyncio

async def moja_korutyna():
    print("Początek korutyny")
    await asyncio.sleep(1)
    print("Koniec korutyny po 1 sekundzie")

async def main():
    print("Rozpoczynam")
    await moja_korutyna()
    print("Zakończono")

asyncio.run(main())
```

W tym przykładzie funkcja `main` uruchamia `moja_korutyna`, używając `await`, aby poczekać na jej zakończenie bez blokowania głównego wątku.

### Wykonywanie wielu korutyn równocześnie

`asyncio` umożliwia uruchamianie wielu korutyn równocześnie, co jest szczególnie przydatne przy operacjach I/O-bound. Można to osiągnąć za pomocą funkcji `asyncio.gather`:

```python
import asyncio

async def korutyna1():
    print("Start korutyna1")
    await asyncio.sleep(1)
    print("Koniec korutyna1")

async def korutyna2():
    print("Start korutyna2")
    await asyncio.sleep(2)
    print("Koniec korutyna2")

async def main():
    await asyncio.gather(
        korutyna1(),
        korutyna2()
    )

asyncio.run(main())

# Wynik:
# Start korutyna1
# Start korutyna2
# Koniec korutyna1
# Koniec korutyna2
```

W tym przykładzie `korutyna1` i `korutyna2` są uruchamiane równocześnie, co pozwala na wykonanie dwóch operacji w tym samym czasie.

## Jak `asyncio` zwiększa wydajność

Załóżmy, że masz do zrobienia wiele żądań sieciowych do różnych serwisów API. W podejściu synchronicznym żądanie za żądaniem zostanie obsłużone pojedynczo, a każde kolejne żądanie będzie czekać, aż poprzednie się zakończy.

W podejściu asynchronicznym, podczas gdy jedno żądanie czeka na odpowiedź, inne żądania mogą być inicjowane. Gdy żądanie kończy oczekiwanie i otrzymuje odpowiedź, kod kontynuuje działanie z punktu, w którym został zawieszony. Dzięki temu wiele operacji I/O może "czekać" jednocześnie, bez blokowania całego programu.

Przyjrzyjmy się prostemu porównaniu wydajności między podejściem synchronicznym a asynchronicznym przy użyciu żądań HTTP.

### Synchroniczne podejście

```python
import requests
import time

adresy_url = ["http://example.com" for _ in range(10)]

czas_startu = time.time()

for adres in adresy_url:
    odpowiedz = requests.get(adres)
    print(odpowiedz.status_code)

czas_konca = time.time()
print(f"Synchronicznie: {czas_konca - czas_startu} sekund")
```

### Asynchroniczne podejście

```python
import aiohttp
import asyncio
import time

adresy_url = ["http://example.com" for _ in range(10)]

async def pobierz(adres, sesja):
    async with sesja.get(adres) as odpowiedz:
        print(odpowiedz.status)
        return await odpowiedz.text()

async def main():
    async with aiohttp.ClientSession() as sesja:
        zadania = [pobierz(adres, sesja) for adres w adresy_url]
        await asyncio.gather(*zadania)

czas_startu = time.time()
asyncio.run(main())
czas_konca = time.time()

print(f"Asynchronicznie: {czas_konca - czas_startu} sekund")
```

### Analiza wyników

Dla wielu żądań różnica w czasie wykonywania między tymi dwoma podejściami będzie znacząca. Wersja asynchroniczna zwykle będzie znacznie szybsza, ponieważ może jednocześnie inicjować wiele żądań, zamiast czekać na zakończenie każdego z nich osobno.

### Dlaczego `asyncio` jest szybsze?

1. **Równoczesność**: `asyncio` pozwala na wykonywanie wielu operacji równocześnie. Kiedy jedno żądanie czeka na odpowiedź, inne mogą być realizowane.
2. **Efektywne zarządzanie zasobami**: Asynchroniczność pozwala na lepsze wykorzystanie zasobów systemowych, unikając niepotrzebnego blokowania.
3. **Mniejsze obciążenie**: W przeciwieństwie do tworzenia wielu wątków czy procesów, które są bardziej zasobożerne, asynchroniczne podejście korzysta z jednego wątku, co zmniejsza narzut związany z przełączaniem kontekstu.

### Kiedy używać `asyncio`?

- **Operacje I/O-bound**: Kiedy aplikacja wykonuje wiele operacji I/O, takich jak żądania HTTP, operacje na plikach czy bazach danych.
- **Serwery sieciowe**: Serwery HTTP, WebSocket czy inne serwery sieciowe mogą obsługiwać wiele połączeń jednocześnie bez blokowania.
- **Aplikacje czasu rzeczywistego**: Gdzie ważne jest szybkie reagowanie na zdarzenia i interakcje.

### Wyzwania 

Używanie `asyncio` w Pythonie, chociaż potężne, może przynieść pewne wyzwania. Aby lepiej zilustrować te trudności, przyjrzyjmy się kilku konkretnym przykładom:

#### Integracja z kodem synchronicznym

**Problem:** Załóżmy, że używasz asynchronicznej korutyny do obsługi operacji sieciowej, ale potrzebujesz skorzystać z biblioteki, która działa synchronicznie.

```python
import asyncio
import requests

async def pobierz_dane():
    odpowiedz = requests.get("http://example.com")  # synchroniczna operacja
    return odpowiedz.text

asyncio.run(pobierz_dane())
```

**Trudność:** Wywołanie synchronicznej funkcji `requests.get` w korutynie blokuje cały loop zdarzeń, co uniemożliwia równoczesne wykonywanie innych korutyn.

**Rozwiązanie:** Można użyć `loop.run_in_executor`, aby uruchomić blokujący kod w osobnym wątku.

```python
import asyncio
import requests

async def pobierz_dane():
    loop = asyncio.get_event_loop()
    odpowiedz = await loop.run_in_executor(None, requests.get, "http://example.com")
    return odpowiedz.text

asyncio.run(pobierz_dane())
```

#### Debugowanie

**Problem:** Podczas debugowania możesz napotkać błąd w jednej z wielu korutyn, które są jednocześnie uruchomione.

```python
import asyncio

async def zepsuta_korutyna():
    await asyncio.sleep(1)
    raise ValueError("Ups!")

async def inna_korutyna():
    await asyncio.sleep(2)
    print("Inna korutyna zakończona")

async def main():
    zadanie1 = asyncio.create_task(zepsuta_korutyna())
    zadanie2 = asyncio.create_task(inna_korutyna())
    await zadanie1
    await zadanie2

asyncio.run(main())
```

**Trudność:** Zdiagnozowanie, która korutyna jest problematyczna i dlaczego, może być trudniejsze ze względu na asynchroniczne zachowanie i brak tradycyjnego stosu wywołań.

**Rozwiązanie:** Używanie bardziej rozbudowanych narzędzi do debugowania, takich jak `asyncio.Task.all_tasks()`, lub logowanie, aby śledzić przepływ wykonania.

#### Poprawne zarządzanie zasobami

**Problem:** Upewnienie się, że wszystkie zasoby, takie jak pliki czy połączenia sieciowe, są poprawnie zamykane.

```python
import asyncio
import aiohttp

async def pobierz_dane(url):
    async with aiohttp.ClientSession() as sesja:
        async with sesja.get(url) as odpowiedz:
            return await odpowiedz.text()

async def main():
    urls = ["http://example.com" for _ in range(10)]
    zadania = [pobierz_dane(url) for url in urls]
    await asyncio.gather(*zadania)

asyncio.run(main())
```

**Trudność:** Używanie kontekstu `async with` jest konieczne, aby zapewnić poprawne zamknięcie zasobów.

#### Asynchroniczne operacje ograniczone przez CPU

**Problem:** Używanie asynchroniczności do operacji ograniczonych przez CPU.

```python
import asyncio

async def zadanie_obciazajace_cpu(dane):
    wynik = sum([x*x for x in dane])
    return wynik

asyncio.run(zadanie_obciazajace_cpu(range(1000000)))
```

**Trudność:** Choć asyncio jest doskonałe do operacji ograniczonych przez I/O, nie przyspiesza to operacji ograniczonych przez CPU i może wprowadzać niepotrzebny narzut.

**Rozwiązanie:** Używanie `concurrent.futures` lub `multiprocessing` do wykonywania operacji CPU-bound w osobnych wątkach lub procesach.

```python
import asyncio
from concurrent.futures import ProcessPoolExecutor

def zadanie_obciazajace_cpu(dane):
    return sum([x*x for x in dane])

async def main():
    loop = asyncio.get_event_loop()
    with ProcessPoolExecutor() as executor:
        wynik = await loop.run_in_executor(executor, zadanie_obciazajace_cpu, range(1000000))
        print(wynik)

asyncio.run(main())
```
