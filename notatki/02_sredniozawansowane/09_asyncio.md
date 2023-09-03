## Programowanie asynchroniczne

`asyncio` to biblioteka w języku Python umożliwiająca pisanie jednowątkowego kodu asynchronicznego za pomocą tzw. `coroutine`. Pozwala to na jednoczesne wykonywanie wielu operacji I/O bez konieczności tworzenia wielu wątków lub procesów, co może prowadzić do zwiększenia wydajności, szczególnie w aplikacjach I/O-bound (gdy głównym czynnikiem ograniczającym jest operacja wejścia/wyjścia).

`asyncio` pozwala na skuteczniejsze wykorzystanie jednego wątku, dzięki czemu unikamy problemów związanych z równoczesnym dostępem do pamięci i GIL (Global Interpreter Lock) w Pythonie.

Aby użyć `asyncio`, kluczowym elementem jest deklaracja funkcji jako `async`:

```python
async def moja_korutyna():
    print("Początek")
    await asyncio.sleep(1)
    print("Koniec po 1 sekundzie")
```

W powyższym kodzie używamy `await`, której można używać tylko wewnątrz funkcji zadeklarowanej jako `async`. `await` wskazuje, że w tym miejscu funkcja może zostać "zawieszona", co pozwala na wykonanie innej aktywnej korutyny.

```python
import asyncio

async def main():
    print("Rozpoczynam")
    await moja_korutyna()
    print("Zakończono")

asyncio.run(main())
```

### Równoległe wykonanie korutyn

Dzięki `asyncio` możemy także łatwo uruchamiać wiele korutyn równolegle:

```python
import asyncio

async def powiedz_po(opoznienie, co):
    await asyncio.sleep(opoznienie)
    print(co)

async def main():
    print("Rozpoczęto")
    
    zadanie1 = asyncio.create_task(powiedz_po(1, "Cześć"))
    zadanie2 = asyncio.create_task(powiedz_po(2, "Świecie"))

    await zadanie1
    await zadanie2

    print("Zakończono")

asyncio.run(main())
```

W powyższym kodzie `asyncio.create_task()` uruchamia korutynę, nie czekając na jej zakończenie. Dzięki temu `powiedz_po(1, "Cześć")` i `powiedz_po(2, "Świecie")` są uruchamiane równolegle.

## Jak asyncio zwiększa wydajność

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
        zadania = [pobierz(adres, sesja) for adres in adresy_url]
        await asyncio.gather(*zadania)

czas_startu = time.time()
asyncio.run(main())
czas_konca = time.time()

print(f"Asynchronicznie: {czas_konca - czas_startu} sekund")
```

Dla wielu żądań różnica w czasie wykonywania między tymi dwoma podejściami będzie znacząca. Wersja asynchroniczna zwykle będzie znacznie szybsza, ponieważ może jednocześnie inicjować wiele żądań, zamiast czekać na zakończenie każdego z nich osobno.

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

Trudność: Wywołanie synchronicznej funkcji requests.get w korutynie blokuje cały loop zdarzeń, co uniemożliwia równoczesne wykonywanie innych korutyn.

#### Debugowanie

**Problem:** Podczas debugowania napotkasz błąd w jednej z wielu korutyn, które są jednocześnie uruchomione.

```python
async def zepsuta_korutyna():
    await asyncio.sleep(1)
    raise ValueError("Ups!")

async def main():
    zadanie1 = asyncio.create_task(zepsuta_korutyna())
    zadanie2 = asyncio.create_task(inna_korutyna())
    await zadanie1
    await zadanie2

asyncio.run(main())
```

**Trudność:** Zdiagnozowanie, która korutyna jest problematyczna i dlaczego, może być trudniejsze ze względu na asynchroniczne zachowanie i brak tradycyjnego stosu wywołań.

#### Poprawne zarządzanie zasobami

**Problem:** Tworzenie wielu połączeń bez ich odpowiedniego zamykania.

```python
async def pobierz_wiele():
    adresy_url = ["http://example.com"] * 100
    for adres in adresy_url:
        odpowiedz = await aiohttp.request("GET", adres)
        # brak zamknięcia połączenia

asyncio.run(pobierz_wiele())
```

**Trudność:** Niezamknięte połączenia mogą prowadzić do wycieków zasobów, co obciąża system i może prowadzić do błędów.

#### Asynchroniczne operacje ograniczone przez CPU

**Problem:** Używanie asynchroniczności do operacji ograniczonych przez CPU.

```python
async def zadanie_obciazajace_cpu(dane):
    wynik = sum([x*x for x in dane])
    return wynik

asyncio.run(zadanie_obciazajace_cpu(range(1000000)))
```

**Trudność:** Choć asyncio jest doskonałe do operacji ograniczonych przez I/O, nie przyspiesza to operacji ograniczonych przez CPU i może wprowadzać niepotrzebny narzut.
