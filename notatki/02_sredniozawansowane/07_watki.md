## Wątki

Wątki to jednostki wykonawcze procesu, które umożliwiają równoległe wykonanie różnych fragmentów kodu w obrębie jednego programu. Zastosowanie wątków może znacząco przyspieszyć działanie aplikacji, zwłaszcza gdy mamy do czynienia z operacjami blokującymi, takimi jak łączenie się z zewnętrznymi serwerami, wczytywanie dużych plików czy obliczenia numeryczne.

### Porównanie: wątki vs procesy vs asyncio

| Cecha                    | Wątki (`threading`)    | Procesy (`multiprocessing`) | Asyncio                     |
|--------------------------|------------------------|-----------------------------|-----------------------------|
| Równoległość CPU         | Nie (GIL)              | Tak                         | Nie                         |
| Współbieżność I/O       | Tak                    | Tak                         | Tak                         |
| Wspólna pamięć           | Tak                    | Nie (wymaga IPC)            | Tak (single-thread)         |
| Koszt tworzenia          | Niski                  | Wysoki (fork/spawn)         | Bardzo niski                |
| Synchronizacja           | Lock, Semaphore, Event | Lock, Queue, Pipe           | Nie wymaga (kooperatywny)   |
| Najlepsze dla            | I/O-bound              | CPU-bound                   | Wiele połączeń sieciowych   |
| Ryzyko deadlocka         | Tak                    | Tak                         | Minimalne                   |
| Debugowanie              | Trudne                 | Średnie                     | Łatwiejsze                  |

### Jak działają wątki?

Wątki działają jako lekkie podprocesy wewnątrz głównego procesu programu. Każdy wątek może wykonywać niezależnie fragmenty kodu, współdzieląc zasoby (np. pamięć) z innymi wątkami tego samego procesu. W Pythonie, do zarządzania wątkami używamy modułu `threading`.

Kluczowe aspekty działania wątków:

1. **Tworzenie i uruchamianie wątku**:
    - Wątek jest tworzony jako instancja klasy `Thread`.
    - Do konstrukcji wątku podajemy funkcję, którą wątek ma wykonać.
    - Uruchomienie wątku następuje poprzez wywołanie metody `start`.

2. **Wykonywanie kodu w wątku**:
    - Po wywołaniu `start`, wątek rozpoczyna wykonywanie przypisanej funkcji.
    - Główny program może kontynuować wykonywanie swojego kodu niezależnie od wątku.

3. **Zakończenie wątku**:
    - Wątek kończy się po wykonaniu przypisanej funkcji.
    - Metoda `join` pozwala głównemu programowi czekać na zakończenie wątku, zanim przejdzie dalej.

### Użycie wątków

Aby korzystać z wątków w Pythonie, potrzebujemy modułu `threading`.

```python
import threading

def moja_funkcja():
    print("Rozpoczynam pracę w wątku:", threading.current_thread().name)

# Tworzenie nowego wątku
watek = threading.Thread(target=moja_funkcja, name="Watek-1")

# Uruchamianie wątku
watek.start()

# Oczekiwanie na zakończenie wątku
watek.join()
```

Kilka ważnych uwag na temat wątków w Pythonie:

- **GIL (Global Interpreter Lock)**: W przypadku standardowego interpretera Pythona (CPython), w dowolnym momencie może być aktywny tylko jeden wątek. To oznacza, że wątki nie przyspieszają operacji CPU-intensywnych. Wątki są jednak bardzo przydatne w operacjach I/O-bound, takich jak wczytywanie plików czy żądania sieciowe.
- **Synchronizacja wątków**: Gdy dwa lub więcej wątków ma dostęp do wspólnego zasobu, potrzebna jest synchronizacja, aby uniknąć problemów z dostępem konkurencyjnym. Do tego celu można użyć różnych mechanizmów synchronizacji, takich jak blokady (Lock), semafory (Semaphore) czy warunki (Condition).
- **Bezpieczeństwo wątków**: Przy korzystaniu z wątków istotne jest zapewnienie ich bezpieczeństwa, co często oznacza unikanie potencjalnych sytuacji wyścigowych i innych błędów związanych z wielowątkowością.
- **Zakończenie wątków**: Wątki powinny być zamykane w odpowiedni sposób. Metoda `join` pozwala głównemu wątkowi czekać na zakończenie wątków potomnych.

### Tworzenie własnego wątku

Tworzenie własnego wątku w Pythonie jest stosunkowo proste dzięki modułowi `threading`. Głównym podejściem jest dziedziczenie po klasie `Thread` i nadpisanie metody `run`, która definiuje działania, które mają być wykonane w obrębie tego wątku. Aby uruchomić wątek, po utworzeniu jego instancji, wywołujemy metodę `start`.

Poniżej przedstawiono przykład tworzenia prostego wątku:

```python
import threading

class MojWatek(threading.Thread):
    def run(self):
        # kod, który zostanie wykonany w wątku
        print("Wątek uruchomiony")

watek = MojWatek()
watek.start()
```

Jeżeli chcemy przekazać argumenty do naszego wątku, możemy to zrobić poprzez konstruktor klasy. Pamiętajmy, aby w konstruktorze wywołać konstruktor klasy nadrzędnej przy użyciu `super()`.

```python
import threading

class MojWatek(threading.Thread):
    def __init__(self, argument):
        super().__init__()
        self.argument = argument

    def run(self):
        # kod, który zostanie wykonany w wątku
        print(f"Wątek uruchomiony z argumentem: {self.argument}")

watek = MojWatek("Hello World")
watek.start()
```

Ważne jest, aby pamiętać o potencjalnych problemach związanych z wielowątkowością, takich jak konkurencyjny dostęp do wspólnych zasobów czy potencjalne sytuacje wyścigowe. W przypadku potrzeby synchronizacji wątków warto skorzystać z mechanizmów dostarczanych przez moduł `threading`, takich jak `Lock` czy `Semaphore`.

### Kontrola i zatrzymanie wątku

Kontrolowanie i zatrzymywanie wątków w Pythonie może być nieco skomplikowane, ale dzięki narzędziom dostarczanym przez moduł `threading` jest to możliwe do osiągnięcia.

#### Metoda `join()`

Głównym sposobem oczekiwania na zakończenie wątku jest użycie metody `Thread.join()`. Blokuje ona wywołujący wątek do momentu zakończenia wątku, na którym została wywołana.

```python
watki = [watek1, watek2, watek3]

for watek in watki:
    watek.join()
```

Można również określić maksymalny czas oczekiwania za pomocą parametru `timeout` w metodzie `join()`. Jeśli po tym czasie wątek nie zakończył pracy, główny wątek zostanie wznowiony.

#### Zmienna `Event`

Zmienna `Event` w module `threading` umożliwia komunikację między wątkami. Wątek może oczekiwać na sygnał (metoda `wait()`) i inny wątek może wysłać ten sygnał (metoda `set()`).

```python
import threading

stop_event = threading.Event()

def worker_thread():
    while not stop_event.is_set():
        # wątek wykonuje swoje zadania
        do_some_work()
    # po otrzymaniu sygnału wątek jest zatrzymywany
    stop_event.clear()

# ...

# główny wątek chce zatrzymać worker_thread
stop_event.set()
```

Uwagi:

- Zatrzymanie wątku (zwłaszcza przez wymuszanie) nie jest zalecane, ponieważ może prowadzić do nieprzewidywalnych skutków ubocznych. Zamiast tego powinno się zastosować mechanizmy synchronizacji lub pozwolić wątkowi zakończyć pracę naturalnie.
- W przypadku korzystania z globalnych zmiennych lub zasobów współdzielonych, zawsze pamiętaj o synchronizacji dostępu, aby uniknąć zjawiska wyścigu lub naruszeń integralności danych.
- W praktyce lepiej unikać używania stałych pętli, które sprawdzają pewien warunek (jak `stop_event.is_set()`) w nieskończoność, gdyż mogą one powodować niepotrzebne obciążenie procesora.

### Dzielenie zasobów między wątkami

W wielowątkowych aplikacjach często występuje potrzeba korzystania ze współdzielonych zasobów, takich jak zmienne czy struktury danych. Jednak równoczesny dostęp wielu wątków do tych zasobów może prowadzić do nieprzewidywalnych i niepożądanych skutków, takich jak sytuacje wyścigowe. Aby uniknąć tych problemów, konieczne jest użycie mechanizmów synchronizacji.

#### Blokada

Obiekt `Lock` z modułu `threading` pozwala na zapewnienie, że tylko jeden wątek na raz może wykonywać określony fragment kodu.

Przykład:

```python
import threading

# Globalna zmienna dostępna dla wielu wątków
zmienna_globalna = 0

# Obiekt Zamek do synchronizacji dostępu do zmienna_globalna
blokada = threading.Lock()

def funkcja_watek1():
    global zmienna_globalna
    for _ in range(100):
        with blokada:  # Zastosowanie kontekstu zamiast manualnego pobierania i zwalniania blokady
            zmienna_globalna += 1

def funkcja_watek2():
    global zmienna_globalna
    for _ in range(100):
        with blokada:
            zmienna_globalna -= 1

# Tworzenie i uruchamianie wątków
watek1 = threading.Thread(target=funkcja_watek1)
watek2 = threading.Thread(target=funkcja_watek2)

watek1.start()
watek2.start()

# Czekanie na zakończenie wątków
watek1.join()
watek2.join()

# Wyświetlenie wyniku
print(zmienna_globalna)
```

W powyższym przykładzie:
- Zamiast korzystać z manualnego pobierania (`acquire()`) i zwalniania blokady (`release()`), użyto konstrukcji `with blokada:`, która jest bardziej elegancka i automatycznie zwalnia blokadę nawet w przypadku wystąpienia błędów.
- Zmniejszono ryzyko wystąpienia zjawiska wyścigu i zapewniono, że zmienne globalne są aktualizowane w sposób kontrolowany.

#### Semafora

Semafory to kolejny mechanizm synchronizacji, który może być użyty, gdy potrzebujemy kontrolować dostęp do zasobu przez określoną liczbę wątków jednocześnie.

Przykład użycia semafora:

```python
import threading
import time

# Semafor z limitem 2 wątków
semafora = threading.Semaphore(2)

def funkcja_watek(numer):
    with semafora:
        print(f"Wątek {numer} rozpoczął pracę")
        time.sleep(2)
        print(f"Wątek {numer} zakończył pracę")

# Tworzenie i uruchamianie wątków
watki = [threading.Thread(target=funkcja_watek, args=(i,)) for i in range(5)]

for watek in watki:
    watek.start()

for watek in watki:
    watek.join()
```

W powyższym przykładzie:

- Semafora pozwala maksymalnie dwóm wątkom jednocześnie wykonywać kod w bloku `with semafora:`.
- Inne wątki muszą czekać, aż semafor zostanie zwolniony przez jeden z aktywnych wątków.

### GIL (Global Interpreter Lock)

GIL, czyli Global Interpreter Lock, to mechanizm obecny w standardowej implementacji Pythona (CPython), który zapewnia, że w danej chwili tylko jeden wątek może wykonywać kod bajtowy Pythona. GIL został wprowadzony, aby rozwiązać problemy związane z zarządzaniem pamięcią w kontekście wielowątkowości, zapewniając jednocześnie efektywność jednowątkowego kodu.

#### Główne aspekty GIL:

1. **Działa tylko w CPython:** Inne implementacje języka, takie jak Jython (Python na JVM) czy IronPython (Python na .NET), nie mają GIL, co pozwala im na pełną równoległość.
2. **Nie wpływa na procesy wielordzeniowe:** GIL wpływa tylko na kod wielowątkowy. Jeżeli kod korzysta z procesów (np. za pomocą modułu `multiprocessing`), każdy proces posiada własną instancję interpretera i własny GIL, dzięki czemu może działać równolegle.
3. **Nie wpływa na operacje we/wy:** Gdy wątek wykonuje operacje we/wy, takie jak czytanie z dysku czy pobieranie danych z sieci, GIL jest zwalniany, co pozwala innym wątkom na działanie.

#### Przykład ilustrujący działanie GIL

Przykład z sumowaniem elementów listy jest dość prosty i niekoniecznie pokazuje faktyczne ograniczenia GIL. Bardziej zaawansowane operacje, takie jak obliczenia CPU, mogą naprawdę odczuwać negatywne skutki GIL w wielowątkowym środowisku.

```python
import threading

def suma_listy(liczby):
    suma = sum(liczby)  # Uproszczony sposób sumowania
    print(suma)

# Utworzenie wątków
watki = [
    threading.Thread(target=suma_listy, args=([1, 2, 3],)),
    threading.Thread(target=suma_listy, args=([4, 5, 6],)),
    threading.Thread(target=suma_listy, args=([7, 8, 9],))
]

# Uruchomienie wątków
for watek in watki:
    watek.start()

# Oczekiwanie na zakończenie wątków
for watek in watki:
    watek.join()
```

W powyższym przykładzie wszystkie wątki mogą wykonywać operacje sumowania, ale ze względu na GIL, tylko jeden wątek na raz wykonuje kod Pythona. W rzeczywistości, sumowanie w każdym wątku odbywa się sekwencyjnie, a nie równolegle.

#### Rozwiązania ograniczeń GIL

W przypadkach, gdy chcemy maksymalnie wykorzystać wielordzeniowość procesora w Pythonie, warto rozważyć użycie procesów zamiast wątków lub użycie innych narzędzi:

1. **Użycie procesów:** Moduł `multiprocessing` pozwala tworzyć procesy, z których każdy ma własną instancję Pythona i własny GIL, umożliwiając rzeczywistą równoległość.

```python
from multiprocessing import Process

def suma_listy(liczby):
    suma = sum(liczby)
    print(suma)

# Utworzenie procesów
procesy = [
    Process(target=suma_listy, args=([1, 2, 3],)),
    Process(target=suma_listy, args=([4, 5, 6],)),
    Process(target=suma_listy, args=([7, 8, 9],))
]

# Uruchomienie procesów
for proces in procesy:
    proces.start()

# Oczekiwanie na zakończenie procesów
for proces in procesy:
    proces.join()
```

2. **Użycie bibliotek specjalizujących się w współbieżności:** Biblioteki takie jak `Dask` czy `Joblib` mogą uprościć równoległe przetwarzanie danych i zarządzanie zadaniami w Pythonie.

3. **Użycie Cython:** Cython pozwala na kompilację kodu Pythona do kodu C, co może znacznie przyspieszyć wykonywanie obliczeń intensywnych pod względem CPU i umożliwić lepsze wykorzystanie wielordzeniowości.

Ostateczna uwaga: Gdy chcemy przyspieszyć operacje w Pythonie, warto również rozważyć zastosowanie odpowiednich algorytmów i struktur danych, które mogą wpłynąć na wydajność kodu niezależnie od użycia wątków czy procesów.

### ThreadPoolExecutor — nowoczesne API

Od Pythona 3.2 dostępny jest moduł `concurrent.futures`, który oferuje wysokopoziomowy interfejs do pracy z wątkami (i procesami). `ThreadPoolExecutor` zarządza pulą wątków automatycznie:

```python
from concurrent.futures import ThreadPoolExecutor, as_completed
import time

def pobierz_dane(url):
    """Symulacja pobierania danych."""
    time.sleep(1)
    return f"Dane z {url}"

adresy = [f"http://example.com/page/{i}" for i in range(5)]

# Użycie ThreadPoolExecutor
with ThreadPoolExecutor(max_workers=3) as executor:
    # submit — uruchomienie zadań
    futures = {executor.submit(pobierz_dane, url): url for url in adresy}
    
    # as_completed — iteracja po wynikach w kolejności kończenia
    for future in as_completed(futures):
        url = futures[future]
        wynik = future.result()
        print(f"{url} → {wynik}")
```

#### `map()` — prostsza składnia dla jednorodnych zadań

```python
from concurrent.futures import ThreadPoolExecutor

def przetworz(n):
    return n ** 2

with ThreadPoolExecutor(max_workers=4) as executor:
    wyniki = list(executor.map(przetworz, range(10)))

print(wyniki)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

### Dobre praktyki i typowe pułapki

| Pułapka                              | Problem                                      | Rozwiązanie                                         |
|--------------------------------------|----------------------------------------------|-----------------------------------------------------|
| Brak synchronizacji                  | Wyścig danych (race condition)               | Użyj `Lock` lub `Queue`                            |
| Deadlock                             | Dwa wątki czekają na siebie nawzajem         | Zawsze pobieraj blokady w tej samej kolejności      |
| Użycie wątków dla CPU-bound          | GIL blokuje równoległość                     | Użyj `multiprocessing` lub `ProcessPoolExecutor`   |
| Mutowalny argument domyślny          | Współdzielony stan między wywołaniami        | Używaj niemutowalnych wartości domyślnych           |
| Brak `join()`                        | Program kończy się przed wątkami             | Zawsze czekaj na zakończenie wątków                |
| Print w wielu wątkach                | Wymieszane linie w konsoli                   | Użyj `logging` lub `Lock` na `print`              |

### Queue — bezpieczna komunikacja między wątkami

`queue.Queue` to struktura FIFO bezpieczna wątkowo (thread-safe), idealna do wzorca producent-konsument:

```python
import threading
import queue
import time

def producent(q, n):
    for i in range(n):
        item = f"element-{i}"
        q.put(item)
        print(f"Producent dodał: {item}")
        time.sleep(0.1)
    q.put(None)  # sygnał zakończenia

def konsument(q):
    while True:
        item = q.get()
        if item is None:
            break
        print(f"Konsument przetworzył: {item}")
        q.task_done()

kolejka = queue.Queue(maxsize=5)

p = threading.Thread(target=producent, args=(kolejka, 5))
k = threading.Thread(target=konsument, args=(kolejka,))

p.start()
k.start()
p.join()
k.join()
```

### Timer — opóźnione wykonanie

```python
import threading

def przypomnienie():
    print("Minęło 5 sekund!")

timer = threading.Timer(5.0, przypomnienie)
timer.start()
# Można anulować: timer.cancel()
```
