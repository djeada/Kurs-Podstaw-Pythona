## Programowanie asynchroniczne

Programowanie asynchroniczne to styl programowania, który pozwala na wykonywanie operacji bez blokowania głównego wątku programu. Oznacza to, że operacje mogą być uruchamiane równocześnie, a program może reagować na ich zakończenie w sposób nieblokujący.

`asyncio` to biblioteka w języku Python umożliwiająca pisanie jednowątkowego kodu asynchronicznego za pomocą tzw. `coroutine`. Pozwala to na jednoczesne wykonywanie wielu operacji I/O bez konieczności tworzenia wielu wątków lub procesów, co może prowadzić do zwiększenia wydajności, szczególnie w aplikacjach I/O-bound (gdy głównym czynnikiem ograniczającym jest operacja wejścia/wyjścia).

`asyncio` pozwala na skuteczniejsze wykorzystanie jednego wątku, dzięki czemu unikamy problemów związanych z równoczesnym dostępem do pamięci i GIL (Global Interpreter Lock) w Pythonie.

### Podstawy `asyncio`

Aby funkcja mogła stać się korutyną, należy zadeklarować ją przy użyciu słowa kluczowego `async`. Oto przykład:

```python
async def moja_korutyna():
    print("Witaj!")
```

Co zmienia się, gdy używamy `async def` zamiast tradycyjnego `def`? Zmian jest wiele.

Funkcja zdefiniowana jako `async def` jest funkcją asynchroniczną, zwaną korutyną. Korutyny różnią się od zwykłych funkcji tym, że mogą zostać zawieszone w trakcie swojego działania, co pozwala na wykonywanie innych korutyn w międzyczasie. Dzięki temu możemy efektywnie zarządzać zadaniami, które mogą być czasochłonne, bez blokowania głównego wątku programu. W korutynach wykorzystujemy słowo kluczowe `await` do wskazania miejsc, w których funkcja może zostać zawieszona i wznowiona później. Więcej na ten temat powiemy za chwilę.

Jak można wywołać taką funkcję? Istnieje kilka opcji:

### I. Wywoływanie za pomocą `await` z innych funkcji async

Korutyny można wywoływać bezpośrednio za pomocą `await` z innych funkcji asynchronicznych. `await` służy do wstrzymania wykonania bieżącej korutyny, aż do zakończenia korutyny, na którą czekamy.

Przykład:

```python
import asyncio

async def moja_korutyna():
    print("Początek korutyny")
    await asyncio.sleep(1)  # Korutyna zawiesza swoje działanie na 1 sekundę
    print("Koniec korutyny po 1 sekundzie")

async def main():
    print("Rozpoczynam")
    await moja_korutyna()  # Czekamy na zakończenie korutyny
    print("Zakończono")

asyncio.run(main())
```

Wyjaśnienie:

1. `async def moja_korutyna()`: Definiujemy korutynę, która wykorzystuje `asyncio.sleep(1)`, aby wstrzymać swoje działanie na 1 sekundę.
2. `await moja_korutyna()`: W funkcji `main` używamy `await`, aby wstrzymać wykonanie `main` do momentu zakończenia `moja_korutyna`.
3. `asyncio.run(main())`: Uruchamiamy funkcję `main` jako główną pętlę asynchroniczną.

#### Analogiczny kod synchroniczny:

```python
import time

def moja_funkcja():
    print("Początek funkcji")
    time.sleep(1)  # Funkcja zawiesza swoje działanie na 1 sekundę
    print("Koniec funkcji po 1 sekundzie")

def main():
    print("Rozpoczynam")
    moja_funkcja()  # Czekamy na zakończenie funkcji
    print("Zakończono")

if __name__ == "__main__":
    main()
```

**UWAGA**: W tym prostym przypadku, użycie korutyn nie przynosi bezpośrednich korzyści w porównaniu z kodem synchronicznym. Główna różnica polega na tym, że korutyny pozwalają na równoczesne wykonywanie innych zadań w trakcie oczekiwania.

### II. Wywoływanie funkcji asynchronicznej z innych funkcji async

Funkcję asynchroniczną można wywoływać z innych funkcji async przy użyciu metod takich jak `asyncio.create_task()` lub `asyncio.run()`.

#### Przykład:

```python
import asyncio

async def moja_korutyna():
    print("Początek korutyny")
    await asyncio.sleep(1)  # Korutyna zawiesza swoje działanie na 1 sekundę
    print("Koniec korutyny po 1 sekundzie")

async def main():
    print("Rozpoczynam")
    task = asyncio.create_task(moja_korutyna())  # Tworzymy zadanie asynchroniczne
    print("Inne działania w main()")
    await task  # Czekamy na zakończenie zadania
    print("Zakończono")

asyncio.run(main())
```

Wyjaśnienie:

1. `asyncio.create_task(moja_korutyna())`: Tworzymy zadanie asynchroniczne, które będzie wykonywane równolegle z innymi zadaniami.
2. `await task`: Czekamy na zakończenie tego zadania.
3. `asyncio.run(main())`: Uruchamiamy funkcję `main` jako główną pętlę asynchroniczną.

W powyższym przykładzie, `asyncio.create_task()` pozwala na wykonywanie innych operacji w `main()` w czasie, gdy `moja_korutyna` jest zawieszona.

### III. Wywoływanie za pomocą pętli zdarzeń `loop` ze zwykłej funkcji

Korutyny mogą być również wywoływane ze zwykłych funkcji, przy użyciu pętli zdarzeń `loop`.

#### Przykład:

```python
import asyncio

async def moja_korutyna():
    print("Początek korutyny")
    await asyncio.sleep(1)  # Korutyna zawiesza swoje działanie na 1 sekundę
    print("Koniec korutyny po 1 sekundzie")

def main():
    loop = asyncio.get_event_loop()  # Uzyskujemy pętlę zdarzeń
    loop.run_until_complete(moja_korutyna())  # Uruchamiamy korutynę i czekamy na jej zakończenie

main()
```

Wyjaśnienie:

1. `asyncio.get_event_loop()`: Pobieramy bieżącą pętlę zdarzeń.
2. `loop.run_until_complete(moja_korutyna())`: Uruchamiamy korutynę i czekamy, aż zakończy swoje działanie.

Ten sposób jest użyteczny, gdy chcemy uruchomić korutynę z kodu, który nie jest asynchroniczny, np. w zwykłej funkcji.

### Co zmienia `async`? Wykonywanie synchroniczne vs asynchroniczne

Aby lepiej zrozumieć różnice między kodem synchronicznym a asynchronicznym, przyjrzyjmy się dwóm przykładom.

#### Kod synchroniczny:

```python
import time

def proste_zadanie():
    print("Pracownik przetwarza zadania...")
    time.sleep(3)  # Symulujemy czasochłonne zadanie
    print("Pracownik skończył zadanie.")
    return 42

def main():
    print("Rozpoczynamy główne zadanie.")
    wynik = proste_zadanie()  # Czekamy, aż zadanie się zakończy
    print("Menadżer musiał czekać!")
    print(f"Pracownik odpowiedział, że ukończył {wynik} zadań.")

if __name__ == "__main__":
    main()
```

Wynik:

```
Rozpoczynamy główne zadanie.
Pracownik przetwarza zadania...
Pracownik skończył zadanie.
Menadżer musiał czekać!
Pracownik odpowiedział, że ukończył 42 zadań.
```

Wyjaśnienie:

W powyższym przykładzie, funkcja `main` wywołuje `proste_zadanie`, które symuluje czasochłonne zadanie za pomocą `time.sleep(3)`. W trakcie wykonywania `time.sleep`, cały program jest zablokowany, co oznacza, że nie może wykonywać żadnych innych operacji. Dopiero po zakończeniu zadania, `main` kontynuuje swoje działanie, co sprawia, że menadżer musi czekać na pracownika, zanim będzie mógł zająć się czymś innym.

#### Kod asynchroniczny:

```python
import asyncio

async def proste_zadanie():
    print("Pracownik przetwarza zadania...")
    await asyncio.sleep(3)  # Symulujemy czasochłonne zadanie w sposób asynchroniczny
    print("Pracownik skończył zadanie.")
    return 42

async def main():
    print("Menadżer pyta Pracownika, ile zadań zostało przetworzonych.")
    task = asyncio.create_task(proste_zadanie())  # Tworzymy zadanie asynchroniczne
    print("Menadżer może robić inne rzeczy, czekając na wynik...")
    wynik = await task  # Czekamy na zakończenie zadania, ale nie blokujemy pętli
    print(f"Pracownik odpowiedział, że ukończył {wynik} zadań.")

if __name__ == "__main__":
    asyncio.run(main())
```

Wynik:

```
Menadżer pyta Pracownika, ile zadań zostało przetworzonych.
Menadżer może robić inne rzeczy, czekając na wynik...
Pracownik przetwarza zadania...
Pracownik skończył zadanie.
Pracownik odpowiedział, że ukończył 42 zadań.
```

Wyjaśnienie:

W wersji asynchronicznej, funkcje `proste_zadanie` i `main` są zdefiniowane jako asynchroniczne za pomocą `async def`. Kiedy `main` tworzy zadanie asynchroniczne `task` za pomocą `asyncio.create_task(proste_zadanie())`, `proste_zadanie` zaczyna działać w tle. W tym czasie `main` może wykonywać inne operacje. Dopiero gdy użyjemy `await task`, `main` czeka na zakończenie `proste_zadanie`, ale nie blokuje całego programu, co pozwala na wykonywanie innych zadań w międzyczasie.

Asynchroniczność poprawia efektywność programu poprzez umożliwienie wykonywania innych operacji podczas oczekiwania na zakończenie czasochłonnych zadań. W praktyce oznacza to, że menadżer (główny wątek) nie musi czekać bezczynnie na zakończenie pracy pracownika (korutyny), lecz może zająć się innymi obowiązkami, co zwiększa ogólną produktywność.

### Wykonywanie wielu korutyn równocześnie

Asynchroniczność w Pythonie pozwala na wykonywanie wielu korutyn równocześnie, co znacząco zwiększa efektywność przetwarzania zadań. Możemy to osiągnąć za pomocą funkcji takich jak `asyncio.gather` lub `asyncio.create_task`.

#### Przykład z `asyncio.gather`:

```python
import asyncio

async def zadanie(numer, czas):
    print(f"Zadanie {numer} rozpoczęte...")
    await asyncio.sleep(czas)
    print(f"Zadanie {numer} zakończone po {czas} sekundach.")
    return numer

async def main():
    print("Rozpoczynamy wykonywanie wielu zadań równocześnie.")
    wynik1, wynik2, wynik3 = await asyncio.gather(
        zadanie(1, 2),
        zadanie(2, 3),
        zadanie(3, 1)
    )
    print(f"Wyniki zadań: {wynik1}, {wynik2}, {wynik3}")

if __name__ == "__main__":
    asyncio.run(main())
```

Wynik:

```
Rozpoczynamy wykonywanie wielu zadań równocześnie.
Zadanie 1 rozpoczęte...
Zadanie 2 rozpoczęte...
Zadanie 3 rozpoczęte...
Zadanie 3 zakończone po 1 sekundach.
Zadanie 1 zakończone po 2 sekundach.
Zadanie 2 zakończone po 3 sekundach.
Wyniki zadań: 1, 2, 3
```

Wyjaśnienie:

1. `asyncio.gather(zadanie(1, 2), zadanie(2, 3), zadanie(3, 1))`: `asyncio.gather` uruchamia wszystkie zadania równocześnie i czeka na ich zakończenie.
2. `await asyncio.sleep(czas)`: Każde zadanie wstrzymuje swoje wykonanie na określony czas, symulując czasochłonne operacje.
3. `print(f"Wyniki zadań: {wynik1}, {wynik2}, {wynik3}")`: Po zakończeniu wszystkich zadań, wyniki są wyświetlane.

#### Przykład z `asyncio.create_task`:

```python
import asyncio

async def zadanie(numer, czas):
    print(f"Zadanie {numer} rozpoczęte...")
    await asyncio.sleep(czas)
    print(f"Zadanie {numer} zakończone po {czas} sekundach.")
    return numer

async def main():
    print("Rozpoczynamy wykonywanie wielu zadań równocześnie.")
    task1 = asyncio.create_task(zadanie(1, 2))
    task2 = asyncio.create_task(zadanie(2, 3))
    task3 = asyncio.create_task(zadanie(3, 1))
    
    wynik1 = await task1
    wynik2 = await task2
    wynik3 = await task3
    
    print(f"Wyniki zadań: {wynik1}, {wynik2}, {wynik3}")

if __name__ == "__main__":
    asyncio.run(main())
```

Wynik:

```
Rozpoczynamy wykonywanie wielu zadań równocześnie.
Zadanie 1 rozpoczęte...
Zadanie 2 rozpoczęte...
Zadanie 3 rozpoczęte...
Zadanie 3 zakończone po 1 sekundach.
Zadanie 1 zakończone po 2 sekundach.
Zadanie 2 zakończone po 3 sekundach.
Wyniki zadań: 1, 2, 3
```

Wyjaśnienie:

1. `asyncio.create_task(zadanie(1, 2))`: `asyncio.create_task` tworzy zadanie asynchroniczne, które jest uruchamiane równolegle z innymi zadaniami.
2. `wynik1 = await task1`: Każde zadanie jest wykonywane równocześnie, a `await` wstrzymuje wykonanie `main` do momentu zakończenia danego zadania.

#### Różnice między `asyncio.gather` a `asyncio.create_task`

- `asyncio.gather`: Umożliwia uruchomienie i czekanie na zakończenie wielu zadań równocześnie w jednej operacji. Jest użyteczne, gdy chcemy uruchomić wiele zadań i zbiorczo oczekiwać na ich zakończenie.
- `asyncio.create_task`: Tworzy oddzielne zadania, które mogą być kontrolowane i oczekiwane indywidualnie. Jest bardziej elastyczne, gdy chcemy mieć większą kontrolę nad poszczególnymi zadaniami.

### Jak `asyncio` zwiększa wydajność

Załóżmy, że masz do wysłania wiele żądań sieciowych do różnych serwisów API. W podejściu synchronicznym każde żądanie jest obsługiwane pojedynczo, a każde kolejne żądanie czeka, aż poprzednie się zakończy.

W podejściu asynchronicznym, gdy jedno żądanie czeka na odpowiedź, inne żądania mogą być inicjowane. Gdy żądanie otrzyma odpowiedź, kod kontynuuje działanie od miejsca, w którym został zawieszony. Dzięki temu wiele operacji I/O może "czekać" jednocześnie, bez blokowania całego programu.

Przyjrzyjmy się prostemu porównaniu wydajności między podejściem synchronicznym a asynchronicznym przy użyciu żądań HTTP.

Dla celów tego przykładu, użyjemy publicznego API `https://jsonplaceholder.typicode.com/posts/1` jako celu naszych żądań HTTP.

#### Synchroniczne podejście

```python
import requests
import time

adresy_url = ["https://jsonplaceholder.typicode.com/posts/1" for _ in range(10)]

czas_startu = time.time()

for adres in adresy_url:
    odpowiedz = requests.get(adres)
    print(odpowiedz.status_code)

czas_konca = time.time()
print(f"Synchronicznie: {czas_konca - czas_startu} sekund")
```

Przykładowy wynik:

```
200
200
200
200
200
200
200
200
200
200
Synchronicznie: 5.4 sekund
```

#### Asynchroniczne podejście

```python
import aiohttp
import asyncio
import time

adresy_url = ["https://jsonplaceholder.typicode.com/posts/1" for _ in range(10)]

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

Przykładowy wynik:

```
200
200
200
200
200
200
200
200
200
200
Asynchronicznie: 1.2 sekund
```

Porównanie

- W podejściu **synchronicznym** każde żądanie jest obsługiwane jedno po drugim, co prowadzi do dłuższego czasu wykonania całego procesu. Wykonywanie żądań HTTP w sposób synchroniczny może powodować, że program czeka na zakończenie jednego żądania, zanim rozpocznie kolejne, co jest nieefektywne, gdy mamy do czynienia z wieloma operacjami I/O.
- W podejściu **asynchronicznym** wiele żądań jest obsługiwanych równocześnie, co znacząco skraca czas oczekiwania na odpowiedzi. Asynchroniczność pozwala na wykonywanie innych zadań podczas oczekiwania na odpowiedzi z serwera, dzięki czemu zasoby są wykorzystywane bardziej efektywnie.

### Dlaczego `asyncio` jest szybsze?

- `asyncio` pozwala na wykonywanie wielu operacji równocześnie. Kiedy jedno żądanie czeka na odpowiedź, inne mogą być realizowane.
- Asynchroniczność pozwala na lepsze wykorzystanie zasobów systemowych, unikając niepotrzebnego blokowania.
- W przeciwieństwie do tworzenia wielu wątków czy procesów, które są bardziej zasobożerne, asynchroniczne podejście korzysta z jednego wątku, co zmniejsza narzut związany z przełączaniem kontekstu.

### Kiedy używać `asyncio`?

- Kiedy aplikacja wykonuje wiele operacji I/O, takich jak żądania HTTP, operacje na plikach czy bazach danych.
- Serwery HTTP, WebSocket czy inne serwery sieciowe mogą obsługiwać wiele połączeń jednocześnie bez blokowania.
- W aplikacjach czasu rzeczywistego, gdzie ważne jest szybkie reagowanie na zdarzenia i interakcje.
