## Programowanie asynchroniczne

Programowanie asynchroniczne to paradygmat, który umożliwia wykonywanie operacji w sposób nieblokujący, pozwalając na równoczesne przetwarzanie wielu zadań w ramach jednego wątku. W przeciwieństwie do tradycyjnego programowania synchronicznego, gdzie operacje są wykonywane sekwencyjnie i każda musi zakończyć się przed rozpoczęciem kolejnej, programowanie asynchroniczne pozwala na zawieszenie wykonania operacji, która oczekuje na wynik (np. operacji wejścia/wyjścia), i przełączenie się na wykonywanie innej operacji. Dzięki temu zasoby systemowe są wykorzystywane efektywniej, co jest szczególnie ważne w aplikacjach, które są ograniczone przez operacje I/O (tzw. I/O-bound).

### Dlaczego programowanie asynchroniczne jest ważne?

- Pozwala na lepsze wykorzystanie czasu procesora poprzez przełączanie między zadaniami podczas oczekiwania na zakończenie operacji I/O.
- Umożliwia obsługę większej liczby jednoczesnych połączeń czy zadań bez konieczności tworzenia wielu wątków lub procesów.
- Pomaga uniknąć sytuacji, w których program jest zablokowany i nie może kontynuować pracy z powodu oczekiwania na zakończenie czasochłonnej operacji.

#### Problem z GIL w Pythonie

Python posiada mechanizm zwany **Global Interpreter Lock (GIL)**, który ogranicza wykonywanie kodu Pythona do jednego aktywnego wątku w danym momencie, niezależnie od liczby uruchomionych wątków w programie. Oznacza to, że nawet jeśli stworzymy wiele wątków, tylko jeden z nich może jednocześnie wykonywać instrukcje Pythona, co może znacząco ograniczać wydajność aplikacji wielowątkowych, szczególnie tych intensywnie korzystających z procesora. Aby obejść to ograniczenie, programiści mogą skorzystać z biblioteki `asyncio`, która umożliwia asynchroniczne wykonywanie operacji w ramach jednego wątku. Dzięki `asyncio` możliwe jest efektywne zarządzanie wieloma operacjami wejścia/wyjścia bez konieczności tworzenia i synchronizacji wielu wątków, co upraszcza kod, redukuje narzut związany z zarządzaniem wątkami oraz zwiększa wydajność aplikacji w kontekście operacji I/O. W praktyce, wykorzystując `asyncio`, można realizować wiele zadań jednocześnie w jednym wątku, co eliminuje problemy związane z GIL i pozwala na tworzenie bardziej skalowalnych oraz responsywnych programów.

### Wprowadzenie do `asyncio`

`asyncio` to biblioteka standardowa w Pythonie (od wersji 3.4), która wprowadza wsparcie dla programowania asynchronicznego za pomocą korutyn, pętli zdarzeń, zadań i przyszłości (ang. *futures*). Pozwala ona na pisanie jednowątkowego kodu asynchronicznego, który jest zarówno czytelny, jak i wydajny.

- **Korutyny** to specjalne funkcje oznaczone słowem kluczowym `async`, które mogą być zawieszone i wznowione, co umożliwia przełączanie między zadaniami bez blokowania wątku.
- **Pętla zdarzeń** to mechanizm zarządzający wykonywaniem korutyn i obsługą zdarzeń asynchronicznych.
- **Zadania (Tasks)** są abstrakcją reprezentującą wykonywanie korutyn, która może być zarządzana przez pętlę zdarzeń.

```
--------------------------------------------------------------------------------
|                      Synchroniczne (Blokujące) Wywołanie Funkcji             |
--------------------------------------------------------------------------------

  Oś czasu (od góry do dołu)

   Wywołujący (np. program główny)                      Funkcja Foo (synch)

         |  (1) Wywołujący rozpoczyna
         |
         |  (2) Wywołujący wywołuje Foo()  +--------------------------------+
         |-------------------------------> | Foo() zaczyna wykonywać swoje  |
         |                                 | zadania                        |
         |                                 |    - Możliwe operacje We/Wy    |
         |                                 |    - Lub obliczenia            |
         |                                 +--------------+-----------------+
         |                                                |
         |  (3) Wywołujący jest zablokowany               |
         |      aż Foo() zakończy swoje zadania           |
         |                                                |
         |                                 +--------------v--------------------+
         |                                 | Foo() kończy zadania, zwraca dane |
         |<--------------------------------+ np. wynik lub kod statusu         |
         |                                 +--------------+--------------------+
         |
         |  (4) Wywołujący otrzymuje wynik
         |      i kontynuuje
         |
         V


--------------------------------------------------------------------------------
|                   Asynchroniczne (Niezablokujące) Wywołanie Funkcji          |
--------------------------------------------------------------------------------

  Oś czasu (od góry do dołu)

   Wywołujący (np. program główny)                     Funkcja Bar (async)

         |  (1) Wywołujący rozpoczyna
         |
         |  (2) Wywołujący wywołuje BarAsync()
         |------------------------------------------> +-----------------------------------+
         |                                            | BarAsync() inicjuje swoje zadania |
         |  (3) BarAsync()                            +-----------------------------------+
         |      natychmiast zwraca kontrolę           
         |                                          
         |  (4) Wywołujący NIE jest zablokowany;   
         |      może kontynuować inne zadania
         | 
         | <---- Możliwe wykonywanie dalszej logiki, obsługa interfejsu użytkownika, itp. --+
         |
         |  (5) W międzyczasie, BarAsync() kończy swoje zadanie w tle
         |      (odpowiedź sieciowa, odczyt pliku, itp.)
         |            
         |                           +-----------------------------------------------+
         |<------------------------> | BarAsync() wywołuje zwrotnie Wywołującego     |
         |                           | (np. funkcja zwrotna lub rozwiązanie promise) |
         |                           +-----------------------------------------------+
         |
         |  (6) Wywołujący obsługuje otrzymany wynik
         |      który właśnie nadeszedł
         |
         V
```


#### Zalety `asyncio`:

- Pozwala na obsługę tysięcy jednoczesnych połączeń bez znaczącego obciążenia systemu.
- Umożliwia pisanie asynchronicznego kodu w sposób zbliżony do kodu synchronicznego.
- Łatwo integruje się z innymi bibliotekami i frameworkami asynchronicznymi.

#### Podstawy `asyncio`

Aby funkcja mogła stać się korutyną, należy zadeklarować ją przy użyciu słowa kluczowego `async def`. Taka funkcja zwraca obiekt korutyny, który reprezentuje jej przyszłe wykonanie.

Przykład:

```python
async def moja_korutyna():
    print("Witaj!")
```

#### Co zmienia się, gdy używamy `async def` zamiast `def`?

- Wywołanie funkcji zdefiniowanej jako `async def` nie powoduje jej natychmiastowego wykonania. Zamiast tego zwraca obiekt korutyny, który musi być uruchomiony przez pętlę zdarzeń.
- Wewnątrz korutyn możemy używać `await` do zawieszania ich wykonania, oczekując na zakończenie innych korutyn lub operacji asynchronicznych.
- Korutyny mogą być zawieszane w trakcie działania i wznawiane później, co pozwala na efektywne przełączanie między różnymi zadaniami.

#### Rola pętli zdarzeń

Pętla zdarzeń jest centralnym mechanizmem w `asyncio`, odpowiedzialnym za planowanie i wykonywanie korutyn. Monitoruje ona stan wszystkich zadań i decyduje, które z nich mogą być wykonane w danym momencie. Dzięki temu możliwe jest równoczesne zarządzanie wieloma operacjami asynchronicznymi w jednym wątku.

#### Wywoływanie korutyn

Istnieje kilka sposobów na uruchomienie i zarządzanie korutynami. Omówimy trzy główne metody:

##### I. Wywoływanie za pomocą `await` z innych funkcji asynchronicznych

Najprostszym sposobem uruchomienia korutyny jest użycie `await` wewnątrz innej korutyny. Pozwala to na sekwencyjne wykonywanie operacji asynchronicznych.

Przykład:

```python
import asyncio

async def moja_korutyna():
    print("Początek korutyny")
    await asyncio.sleep(1)  # Zawieszenie korutyny na 1 sekundę
    print("Koniec korutyny po 1 sekundzie")

async def main():
    print("Rozpoczynam")
    await moja_korutyna()  # Czekamy na zakończenie korutyny
    print("Zakończono")

asyncio.run(main())
```

1. Funkcja asynchroniczna, która zawiesza swoje wykonanie na 1 sekundę przy użyciu `await asyncio.sleep(1)`.
2. Główna funkcja asynchroniczna, która wywołuje `moja_korutyna` za pomocą `await`.
3. `asyncio.run(main())` inicjuje pętlę zdarzeń i uruchamia korutynę `main`.

**Dlaczego używamy `await`?**

Słowo kluczowe `await` powoduje, że korutyna zostaje zawieszona do momentu zakończenia oczekiwanej operacji. W tym czasie pętla zdarzeń może przydzielić zasoby innym korutynom, co zwiększa efektywność programu.

**Porównanie z kodem synchronicznym:**

```python
import time

def moja_funkcja():
    print("Początek funkcji")
    time.sleep(1)  # Zawieszenie funkcji na 1 sekundę
    print("Koniec funkcji po 1 sekundzie")

def main():
    print("Rozpoczynam")
    moja_funkcja()  # Blokujemy wykonanie do zakończenia funkcji
    print("Zakończono")

if __name__ == "__main__":
    main()
```

W wersji synchronicznej, podczas wykonywania `time.sleep(1)`, program jest zablokowany i nie może wykonywać innych operacji. W wersji asynchronicznej, pętla zdarzeń może przełączać się między różnymi korutynami.

##### II. Uruchamianie korutyn równolegle za pomocą `asyncio.create_task()`

Aby wykonywać korutyny równocześnie (w sensie asynchronicznym), możemy użyć `asyncio.create_task()`, który tworzy zadanie zarządzane przez pętlę zdarzeń.

Przykład:

```python
import asyncio

async def moja_korutyna():
    print("Początek korutyny")
    await asyncio.sleep(1)
    print("Koniec korutyny po 1 sekundzie")

async def main():
    print("Rozpoczynam")
    task = asyncio.create_task(moja_korutyna())  # Tworzymy zadanie asynchroniczne
    print("Inne działania w main()")
    await task  # Czekamy na zakończenie zadania
    print("Zakończono")

asyncio.run(main())
```

- `asyncio.create_task(moja_korutyna())` informuje pętlę zdarzeń o konieczności wykonania `moja_korutyna` w tle.
- Po utworzeniu zadania, korutyna `main` kontynuuje wykonywanie bez oczekiwania na zakończenie `moja_korutyna`.
- `await task` powoduje, że `main` zawiesza się do momentu zakończenia `moja_korutyna`.

**Korzyści z użycia `asyncio.create_task()`:**

- Pozwala na uruchomienie wielu korutyn jednocześnie, co zwiększa efektywność programu.
- Możemy zarządzać zadaniami, np. anulować je, jeśli nie są już potrzebne.

**Przykład z wieloma zadaniami:**

```python
import asyncio

async def zadanie(nr, czas):
    print(f"Zadanie {nr} rozpoczęte")
    await asyncio.sleep(czas)
    print(f"Zadanie {nr} zakończone po {czas} sekundach")

async def main():
    task1 = asyncio.create_task(zadanie(1, 2))
    task2 = asyncio.create_task(zadanie(2, 3))
    task3 = asyncio.create_task(zadanie(3, 1))

    await task1
    await task2
    await task3

asyncio.run(main())
```

**Wynik:**

```
Zadanie 1 rozpoczęte
Zadanie 2 rozpoczęte
Zadanie 3 rozpoczęte
Zadanie 3 zakończone po 1 sekundach
Zadanie 1 zakończone po 2 sekundach
Zadanie 2 zakończone po 3 sekundach
```

W tym przykładzie wszystkie zadania są uruchamiane niemal jednocześnie, a ich zakończenie zależy od czasu trwania poszczególnych zadań.

##### III. Uruchamianie korutyn ze zwykłych funkcji za pomocą pętli zdarzeń

Jeśli chcemy uruchomić korutynę z funkcji synchronicznej (zwykłej funkcji), możemy bezpośrednio użyć pętli zdarzeń.

Przykład:

```python
import asyncio

async def moja_korutyna():
    print("Początek korutyny")
    await asyncio.sleep(1)
    print("Koniec korutyny po 1 sekundzie")

def main():
    loop = asyncio.get_event_loop()  # Pobieramy bieżącą pętlę zdarzeń
    loop.run_until_complete(moja_korutyna())  # Uruchamiamy korutynę i czekamy na jej zakończenie

main()
```

- `asyncio.get_event_loop()` zwraca bieżącą pętlę zdarzeń lub tworzy nową, jeśli żadna nie istnieje.
- `loop.run_until_complete(moja_korutyna())` uruchamia korutynę i blokuje wykonanie do jej zakończenia.

Uwaga:

- Od Pythona 3.7 zaleca się używanie `asyncio.run()` zamiast bezpośredniego manipulowania pętlą zdarzeń, chyba że istnieje konkretny powód.
- Bezpośrednie użycie pętli zdarzeń jest przydatne w bardziej złożonych scenariuszach, np. w aplikacjach GUI czy serwerach, gdzie pętla zdarzeń jest zarządzana ręcznie.

#### Co zmienia `async`? Wykonywanie synchroniczne vs asynchroniczne

Aby zrozumieć różnice między kodem synchronicznym a asynchronicznym, przeanalizujmy dwa przykłady ilustrujące ich działanie.

##### Kod synchroniczny

```python
import time

def proste_zadanie():
    print("Pracownik przetwarza zadania...")
    time.sleep(3)  # Symulacja czasochłonnego zadania
    print("Pracownik skończył zadanie.")
    return 42

def main():
    print("Rozpoczynamy główne zadanie.")
    wynik = proste_zadanie()  # Blokujemy wykonanie do zakończenia zadania
    print("Menadżer musiał czekać!")
    print(f"Pracownik odpowiedział, że ukończył {wynik} zadań.")

if __name__ == "__main__":
    main()
```

**Wynik:**

```
Rozpoczynamy główne zadanie.
Pracownik przetwarza zadania...
Pracownik skończył zadanie.
Menadżer musiał czekać!
Pracownik odpowiedział, że ukończył 42 zadań.
```

- Podczas wykonywania `time.sleep(3)`, program jest zablokowany i nie może wykonywać innych operacji.
- Menadżer musi czekać, aż pracownik skończy zadanie, zanim może kontynuować.

##### Kod asynchroniczny

```python
import asyncio

async def proste_zadanie():
    print("Pracownik przetwarza zadania...")
    await asyncio.sleep(3)  # Asynchroniczna symulacja czasochłonnego zadania
    print("Pracownik skończył zadanie.")
    return 42

async def main():
    print("Menadżer pyta pracownika o postęp.")
    task = asyncio.create_task(proste_zadanie())  # Uruchamiamy zadanie asynchronicznie
    print("Menadżer może wykonywać inne zadania w międzyczasie...")
    wynik = await task  # Oczekujemy na zakończenie zadania
    print(f"Pracownik odpowiedział, że ukończył {wynik} zadań.")

asyncio.run(main())
```

**Wynik:**

```
Menadżer pyta pracownika o postęp.
Menadżer może wykonywać inne zadania w międzyczasie...
Pracownik przetwarza zadania...
Pracownik skończył zadanie.
Pracownik odpowiedział, że ukończył 42 zadań.
```

- Menadżer nie jest zablokowany podczas wykonywania `proste_zadanie` i może wykonywać inne operacje.
- Asynchroniczność pozwala na efektywne wykorzystanie czasu oczekiwania.

##### Różnice między kodem synchronicznym a asynchronicznym

- W kodzie synchronicznym `time.sleep(3)` blokuje cały wątek. W kodzie asynchronicznym `await asyncio.sleep(3)` zawiesza tylko korutynę, pozwalając pętli zdarzeń na wykonywanie innych zadań.
- Asynchroniczność pozwala na lepsze wykorzystanie czasu procesora przez przełączanie między zadaniami podczas oczekiwania na operacje I/O.
- Kod asynchroniczny jest bardziej skalowalny w kontekście obsługi wielu jednoczesnych zadań.

##### Przykład z wieloma pracownikami

Rozszerzmy przykład, aby pokazać, jak asynchroniczność pozwala na równoczesne wykonywanie wielu zadań.

```python
import asyncio

async def pracownik(nr, czas):
    print(f"Pracownik {nr} rozpoczął zadanie.")
    await asyncio.sleep(czas)
    print(f"Pracownik {nr} skończył zadanie po {czas} sekundach.")
    return nr * 10

async def main():
    print("Menadżer zleca zadania pracownikom.")
    tasks = [
        asyncio.create_task(pracownik(1, 2)),
        asyncio.create_task(pracownik(2, 3)),
        asyncio.create_task(pracownik(3, 1)),
    ]
    print("Menadżer może wykonywać inne zadania w międzyczasie...")
    wyniki = await asyncio.gather(*tasks)
    print(f"Pracownicy ukończyli zadania z wynikami: {wyniki}")

asyncio.run(main())
```

**Wynik:**

```
Menadżer zleca zadania pracownikom.
Menadżer może wykonywać inne zadania w międzyczasie...
Pracownik 1 rozpoczął zadanie.
Pracownik 2 rozpoczął zadanie.
Pracownik 3 rozpoczął zadanie.
Pracownik 3 skończył zadanie po 1 sekundach.
Pracownik 1 skończył zadanie po 2 sekundach.
Pracownik 2 skończył zadanie po 3 sekundach.
Pracownicy ukończyli zadania z wynikami: [10, 20, 30]
```

#### Wykonywanie wielu korutyn równocześnie

Asynchroniczność w Pythonie, za pomocą biblioteki `asyncio`, pozwala na równoczesne wykonywanie wielu korutyn. Jest to szczególnie przydatne, gdy mamy wiele niezależnych zadań, które mogą być wykonywane jednocześnie, takich jak żądania sieciowe, operacje na plikach czy interakcje z bazami danych. Dzięki temu możemy znacząco zwiększyć efektywność i wydajność naszej aplikacji.

##### Uruchamianie wielu korutyn za pomocą `asyncio.gather`

Funkcja `asyncio.gather` umożliwia jednoczesne uruchomienie wielu korutyn i oczekiwanie na ich zakończenie. Przyjrzyjmy się temu na konkretnym przykładzie.

**Przykład:**

```python
import asyncio

async def zadanie(numer, czas):
    print(f"Zadanie {numer} rozpoczęte...")
    await asyncio.sleep(czas)
    print(f"Zadanie {numer} zakończone po {czas} sekundach.")
    return f"Wynik zadania {numer}"

async def main():
    print("Rozpoczynamy wykonywanie wielu zadań równocześnie.")
    wyniki = await asyncio.gather(
        zadanie(1, 2),
        zadanie(2, 3),
        zadanie(3, 1)
    )
    print("Wszystkie zadania zostały zakończone.")
    for wynik in wyniki:
        print(wynik)

if __name__ == "__main__":
    asyncio.run(main())
```

Korutyna `zadanie`:

- Funkcja `zadanie` przyjmuje dwa argumenty: `numer` i `czas`.
- Wyświetla komunikat o rozpoczęciu zadania.
- Używa `await asyncio.sleep(czas)`, aby symulować czasochłonne operacje (np. żądania sieciowe).
- Po upływie określonego czasu wyświetla komunikat o zakończeniu zadania.
- Zwraca wynik w postaci napisu.

Funkcja `main`:

- Wyświetla komunikat o rozpoczęciu wykonywania zadań.
- Używa `asyncio.gather` do równoczesnego uruchomienia trzech instancji korutyny `zadanie` z różnymi argumentami.
- `asyncio.gather` zwraca listę wyników po zakończeniu wszystkich korutyn.
- Po otrzymaniu wyników, wyświetla komunikaty o zakończeniu i wypisuje wyniki poszczególnych zadań.

**Działanie programu:**

- Wszystkie trzy zadania są uruchamiane niemal jednocześnie.
- Korutyny są wykonywane równolegle (w ramach jednego wątku), co oznacza, że czas wykonania całego zestawu zadań jest zbliżony do czasu najdłuższego pojedynczego zadania (w tym przypadku 3 sekundy).
- W trakcie oczekiwania na zakończenie jednego zadania, inne zadania mogą być wykonywane.

**Wynik działania programu:**

```
Rozpoczynamy wykonywanie wielu zadań równocześnie.
Zadanie 1 rozpoczęte...
Zadanie 2 rozpoczęte...
Zadanie 3 rozpoczęte...
Zadanie 3 zakończone po 1 sekundach.
Zadanie 1 zakończone po 2 sekundach.
Zadanie 2 zakończone po 3 sekundach.
Wszystkie zadania zostały zakończone.
Wynik zadania 1
Wynik zadania 2
Wynik zadania 3
```

##### Uruchamianie wielu korutyn za pomocą `asyncio.create_task`

Alternatywnym sposobem jest użycie funkcji `asyncio.create_task`, która tworzy zadania asynchroniczne z korutyn. Pozwala to na większą kontrolę nad poszczególnymi zadaniami, np. możliwość ich anulowania czy monitorowania stanu.

**Przykład:**

```python
import asyncio

async def zadanie(numer, czas):
    print(f"Zadanie {numer} rozpoczęte...")
    await asyncio.sleep(czas)
    print(f"Zadanie {numer} zakończone po {czas} sekundach.")
    return f"Wynik zadania {numer}"

async def main():
    print("Rozpoczynamy wykonywanie wielu zadań równocześnie.")
    task1 = asyncio.create_task(zadanie(1, 2))
    task2 = asyncio.create_task(zadanie(2, 3))
    task3 = asyncio.create_task(zadanie(3, 1))

    # W tym miejscu możemy wykonywać inne operacje
    print("Wykonuję inne operacje w main()...")

    # Oczekiwanie na zakończenie zadań
    wynik1 = await task1
    wynik2 = await task2
    wynik3 = await task3

    print("Wszystkie zadania zostały zakończone.")
    print(wynik1)
    print(wynik2)
    print(wynik3)

if __name__ == "__main__":
    asyncio.run(main())
```

- Tworzymy zadania za pomocą `asyncio.create_task`, co natychmiast planuje ich wykonanie w pętli zdarzeń.
- Możemy w międzyczasie wykonywać inne operacje w funkcji `main`.
- Każde zadanie jest oczekiwane indywidualnie za pomocą `await taskX`, co daje możliwość kontrolowania kolejności oczekiwania na wyniki.

**Zalety użycia `asyncio.create_task`:**

- Możemy kontrolować każde zadanie z osobna.
- Zadania można anulować za pomocą metody `cancel()`.
- Możemy sprawdzać stan zadania (np. czy jest w trakcie wykonywania, zakończone czy anulowane).

**Różnice między `asyncio.gather` a `asyncio.create_task`**

| Cechy                        | `asyncio.gather`                                                                                   | `asyncio.create_task`                                                                   |
|------------------------------|---------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| Sposób Uruchamiania Korutyn   | Uruchamia wszystkie korutyny równocześnie i czeka na ich zakończenie.                             | Tworzy zadanie (`Task`) do wykonania w pętli zdarzeń.                                   |
| Kolejność Wyników             | Zwraca listę wyników w tej samej kolejności, w jakiej korutyny zostały przekazane.                | Brak gwarantowanej kolejności wyników, zadania są wykonywane niezależnie.               |
| Obsługa Wyjątków              | Przerywa działanie i propaguje wyjątek, chyba że użyto `return_exceptions=True`, wtedy zwraca wyjątki jako wyniki. | Wyjątki w korutynach muszą być obsługiwane ręcznie, nie przerywa to działania innych zadań. |
| Kontrola Zadania              | Brak bezpośredniej kontroli nad zadaniami, oczekuje na zakończenie wszystkich korutyn.            | Pozwala na anulowanie, sprawdzanie stanu zadania i dodawanie callbacków.                |

**Praktyczne zastosowania**

- Gdy potrzebujemy **prostego sposobu na równoczesne uruchomienie wielu korutyn i zebranie wyników** używamy `asyncio.gather`.
- Gdy potrzebujemy **większej kontroli nad zadaniami** używamy `asyncio.create_task`.
- Np. gdy chcemy anulować zadanie po określonym czasie lub gdy chcemy reagować na jego zakończenie za pomocą callbacków.

#### Jak `asyncio` zwiększa wydajność

Wykorzystanie asynchroniczności pozwala na efektywniejsze zarządzanie czasem procesora i operacjami I/O. W tradycyjnym podejściu synchronicznym, gdy program napotka operację I/O, taką jak żądanie sieciowe czy odczyt pliku, musi czekać na jej zakończenie, zanim przejdzie do kolejnej instrukcji. Oznacza to, że czas procesora jest marnowany na bezczynne oczekiwanie.

W asynchroniczności, podczas gdy jedno zadanie czeka na operację I/O, pętla zdarzeń `asyncio` może przełączać się na wykonywanie innych korutyn, które są gotowe do działania. Dzięki temu maksymalizujemy wykorzystanie dostępnego czasu procesora i skracamy ogólny czas wykonywania programu.

##### Przykład: Porównanie wydajności żądań HTTP

Załóżmy, że chcemy wysłać 10 żądań HTTP do tego samego adresu URL.

**Podejście synchroniczne:**

```python
import requests
import time

adresy_url = ["https://jsonplaceholder.typicode.com/posts/1" for _ in range(10)]

start = time.time()

for adres in adresy_url:
    odpowiedz = requests.get(adres)
    print(f"Status: {odpowiedz.status_code}")

end = time.time()
print(f"Synchronicznie: {end - start:.2f} sekund")
```

- Każde żądanie jest wysyłane po zakończeniu poprzedniego.
- Całkowity czas wykonania to suma czasów poszczególnych żądań.
- Jeśli każde żądanie trwa około 0.5 sekundy, to 10 żądań zajmie około 5 sekund.

**Podejście asynchroniczne:**

```python
import aiohttp
import asyncio
import time

adresy_url = ["https://jsonplaceholder.typicode.com/posts/1" for _ in range(10)]

async def pobierz(adres, sesja):
    async with sesja.get(adres) as odpowiedz:
        print(f"Status: {odpowiedz.status}")
        return await odpowiedz.text()

async def main():
    async with aiohttp.ClientSession() as sesja:
        zadania = [asyncio.create_task(pobierz(adres, sesja)) for adres in adresy_url]
        await asyncio.gather(*zadania)

start = time.time()
asyncio.run(main())
end = time.time()

print(f"Asynchronicznie: {end - start:.2f} sekund")
```

- Wszystkie żądania są wysyłane niemal jednocześnie.
- Całkowity czas wykonania zbliża się do czasu najdłuższego pojedynczego żądania.
- Jeśli każde żądanie trwa około 0.5 sekundy, to 10 żądań zajmie około 0.5-1 sekundy.

**Wnioski:**

- **Asynchroniczność** znacząco skraca czas wykonania operacji I/O, gdyż pozwala na równoczesne oczekiwanie na wyniki wielu żądań.
- Program nie marnuje czasu na bezczynne oczekiwanie, lecz wykorzystuje go na wykonywanie innych zadań.
- Asynchroniczne programy mogą obsługiwać więcej zadań bez proporcjonalnego zwiększania zapotrzebowania na zasoby.

##### Dlaczego `asyncio` jest szybsze?

- Podczas gdy jedno zadanie czeka na operację I/O, inne mogą być wykonywane.
- Asynchroniczność nie wymaga tworzenia nowych wątków czy procesów, co zmniejsza narzut związany z przełączaniem kontekstu i zużyciem pamięci.
- `asyncio` zarządza kolejnością wykonywania zadań, optymalizując wykorzystanie czasu procesora.

##### Kiedy używać `asyncio`?

- Gdy aplikacja wysyła wiele żądań sieciowych lub obsługuje wiele połączeń (np. serwery HTTP, klienty API).
- Gdy potrzebujemy równocześnie czytać lub zapisywać wiele plików.
- Przy równoczesnym wykonywaniu wielu zapytań do bazy danych.
- Gdy wymagana jest szybka reakcja na zdarzenia (np. aplikacje IoT, komunikatory).
- Gdy głównym ograniczeniem jest czas oczekiwania na operacje I/O, a nie moc obliczeniowa CPU.

**Przykłady zastosowań:**

- Frameworki takie jak `aiohttp`, `FastAPI` czy `Sanic` wykorzystują asynchroniczność do obsługi wielu żądań HTTP jednocześnie.
- Pisanie klienta, który komunikuje się z wieloma serwisami API w sposób efektywny.
- Obsługa połączeń WebSocket, gdzie utrzymujemy otwarte połączenia z wieloma klientami.
- Równoczesne pobieranie treści z wielu stron internetowych.
