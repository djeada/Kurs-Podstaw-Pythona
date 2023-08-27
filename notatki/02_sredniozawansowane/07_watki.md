## Wątki

Wątki to jednostki wykonawcze procesu, które umożliwiają równoległe wykonanie się różnych fragmentów kodu w obrębie jednego programu. Zastosowanie wątków może znacząco przyspieszyć działanie aplikacji, zwłaszcza gdy mamy do czynienia z operacjami blokującymi, takimi jak łączenie się z zewnętrznymi serwerami, wczytywanie dużych plików, czy obliczenia numeryczne.

### Użycie wątków

Aby korzystać z wątków w Pythonie, potrzebujemy modułu `threading`.

```python
import threading

def moja_funkcja():
    print("Rozpoczynam prace w wątku:", threading.current_thread().name)

# Tworzenie nowego wątku
watek1 = threading.Thread(target=moja_funkcja, name="Watek-1")

# Uruchamianie wątku
watek1.start()

# Oczekiwanie na zakończenie wątku
watek1.join()
```

Kilka ważnych uwag na temat wątków w Pythonie:

- GIL (Global Interpreter Lock): W przypadku standardowego interpretera Pythona (CPython), w dowolnym momencie może być aktywny tylko jeden wątek. To oznacza, że wątki nie przyspieszają operacji CPU-intensywnych. Wątki są jednak bardzo przydatne w operacjach I/O-bound, takich jak wczytywanie plików czy żądania sieciowe.
- Synchronizacja wątków: Gdy dwa lub więcej wątków mają dostęp do wspólnego zasobu, potrzebna jest synchronizacja, aby uniknąć problemów z dostępem konkurencyjnym. Do tego celu można użyć różnych mechanizmów synchronizacji, takich jak blokady (Lock), semafory (Semaphore) czy warunki (Condition).
- Bezpieczeństwo wątków: Przy korzystaniu z wątków istotne jest zapewnienie ich bezpieczeństwa, co często oznacza unikanie potencjalnych sytuacji wyścigowych i innych błędów związanych z wielowątkowością.
- Zakończenie wątków: Wątki powinny być zamykane w odpowiedni sposób. Metoda join pozwala głównemu wątkowi czekać na zakończenie wątków potomnych.

### Tworzenie własnego wątku

Tworzenie własnego wątku w Pythonie jest stosunkowo proste dzięki modułowi `threading`. Głównym podejściem jest dziedziczenie po klasie `Thread` i nadpisanie metody `run`, która definiuje działania, które mają być wykonane w obrębie tego wątku. Aby uruchomić wątek, po utworzeniu jego instancji, wywołujemy metodę `start`.

Poniżej przedstawiono przykład tworzenia prostego wątku:

```python
import threading

class MyThread(threading.Thread):
    def run(self):
        # kod, który zostanie wykonany w wątku
        print("Wątek uruchomiony")

thread = MyThread()
thread.start()
```

Jeżeli chcemy przekazać argumenty do naszego wątku, możemy to zrobić poprzez konstruktor klasy. Pamiętajmy, aby w konstruktorze wywołać konstruktor klasy nadrzędnej przy użyciu super().

```python
import threading

class MyThread(threading.Thread):
    def __init__(self, argument):
        super().__init__()
        self.argument = argument

    def run(self):
        # kod, który zostanie wykonany w wątku
        print(f"Wątek uruchomiony z argumentem: {self.argument}")

thread = MyThread("Hello World")
thread.start()
```

Ważne jest, aby pamiętać o potencjalnych problemach związanych z wielowątkowością, takich jak konkurencyjny dostęp do wspólnych zasobów czy potencjalne sytuacje wyścigowe. W przypadku potrzeby synchronizacji wątków warto skorzystać z mechanizmów dostarczanych przez moduł threading, takich jak Lock czy Semaphore.

### Kontrola i zatrzymanie wątku

Kontrolowanie i zatrzymywanie wątków w Pythonie może być nieco skomplikowane, ale dzięki narzędziom dostarczanym przez moduł `threading` jest to możliwe do osiągnięcia.

1. **Metoda `join()`**: 
    Głównym sposobem oczekiwania na zakończenie wątku jest użycie metody `Thread.join()`. Blokuje ona wywołujący wątek do momentu zakończenia wątku, na którym została wywołana.
    ```python
    threads = [thread1, thread2, thread3]

    for thread in threads:
        thread.join()
    ```
    Można również określić maksymalny czas oczekiwania za pomocą parametru `timeout` w metodzie `join()`. Jeśli po tym czasie wątek nie zakończył pracy, główny wątek zostanie wznowiony.

2. **Zmienna `Event` w module `threading`**:
    Umożliwia komunikację między wątkami. Wątek może oczekiwać na sygnał (metoda `wait()`) i inny wątek może wysłać ten sygnał (metoda `set()`).
    ```python
    import threading

    stop_event = threading.Event()

    def worker_thread():
        while not stop_event.is_set():
            # wątek wykonuje swoje zadania
            do_some_work()
        # po otrzymaniu sygnalu wątek jest zatrzymywany
        stop_event.clear()

    # ...

    # główny wątek chce zatrzymać worker_thread
    stop_event.set()
    ```

3. **Uwagi**:
    - Zatrzymanie wątku (zwłaszcza przez wymuszanie) nie jest zalecane, ponieważ może prowadzić do nieprzewidywalnych skutków ubocznych. Zamiast tego powinno się zastosować mechanizmy synchronizacji lub pozwolić wątkowi zakończyć pracę naturalnie.
    - W przypadku korzystania z globalnych zmiennych lub zasobów współdzielonych, zawsze pamiętaj o synchronizacji dostępu, aby uniknąć zjawiska wyścigu lub naruszeń integralności danych.
    - Należy unikać używania stałych pętli, które sprawdzają pewien warunek (jak `stop_event.is_set()`) w nieskończoność, gdyż mogą one powodować niepotrzebne obciążenie procesora.
   
### Dzielenie zasobów między wątkami

W wielowątkowych aplikacjach często występuje potrzeba korzystania z współdzielonych zasobów, takich jak zmienne czy struktury danych. Jednak równoczesny dostęp wielu wątków do tych zasobów może prowadzić do nieprzewidywalnych i niepożądanych skutków, takich jak sytuacje wyścigowe. Aby uniknąć tych problemów, konieczne jest użycie mechanizmów synchronizacji.

#### Mechanizm blokady (`Lock`)

Obiekt `Lock` z modułu `threading` pozwala na zapewnienie, że tylko jeden wątek na raz może wykonywać określony fragment kodu.

Przykład:

```python
import threading

# Zmienna globalna dostępna dla wielu wątków
zmienna_globalna = 0

# Obiekt Lock do synchronizacji dostępu do zmiennej_globalnej
lock = threading.Lock()

def watek1():
    global zmienna_globalna
    for _ in range(100):
        with lock:  # Zastosowanie kontekstu zamiast manualnego pobierania i zwalniania blokady
            zmienna_globalna += 1

def watek2():
    global zmienna_globalna
    for _ in range(100):
        with lock:
            zmienna_globalna -= 1

# Tworzenie i uruchamianie wątków
t1 = threading.Thread(target=watek1)
t2 = threading.Thread(target=watek2)

t1.start()
t2.start()

# Czekanie na zakończenie wątków
t1.join()
t2.join()

# Wyświetlenie wyniku
print(zmienna_globalna)
```

W powyższym przykładzie:
- Zamiast korzystać z manualnego pobierania (`acquire()`) i zwalniania blokady (`release()`), użyto konstrukcji `with lock:`, która jest bardziej elegancka i automatycznie zwalnia blokadę nawet w przypadku wystąpienia błędów.
- Zmniejszono ryzyko wystąpienia zajwiska wyścigu i zapewniono, że zmienne globalne są aktualizowane w sposób kontrolowany.

Pamiętaj jednak, że nadmierne korzystanie z blokad może prowadzić do spadku wydajności aplikacji, dlatego warto stosować je rozsądnie i tylko tam, gdzie są naprawdę potrzebne.

### GIL (Global Interpreter Lock)

GIL, czyli Global Interpreter Lock, to mechanizm obecny w standardowej implementacji Pythona (CPython), który zapewnia, że w danej chwili tylko jeden wątek może wykonywać kod bajtowy Pythona. GIL został wprowadzony, aby rozwiązać problemy związane z zarządzaniem pamięcią w kontekście wielowątkowości, zapewniając jednocześnie efektywność jednowątkowego kodu.

Główne aspekty GIL:

1. **Działa tylko w CPython:** Inne implementacje języka, takie jak Jython (Python na JVM) czy IronPython (Python na .NET), nie mają GIL, co pozwala im na pełną równoległość.
2. **Nie wpływa na procesy wielordzeniowe:** GIL wpływa tylko na kod wielowątkowy. Jeżeli kod korzysta z procesów (np. za pomocą modułu `multiprocessing`), każdy proces posiada własną instancję interpretera i własny GIL, dzięki czemu może działać równolegle.
3. **Nie wpływa na operacje we/wy:** Gdy wątek wykonuje operacje we/wy, takie jak czytanie z dysku czy pobieranie danych z sieci, GIL jest zwalniany, co pozwala innym wątkom na działanie.

Przykład z sumowaniem elementów listy jest dość prosty i niekoniecznie pokazuje faktyczne ograniczenia GIL. Bardziej zaawansowane operacje, takie jak obliczenia CPU, mogą naprawdę odczuwać negatywne skutki GIL w wielowątkowym środowisku.

Rozwiązanie? W przypadkach, gdy chcemy maksymalnie wykorzystać wielordzeniowość procesora w Pythonie, warto zastanowić się nad użyciem procesów zamiast wątków lub rozważyć użycie innych implementacji Pythona lub narzędzi takich jak Cython do przyspieszenia intensywnych obliczeniowo fragmentów kodu.

```python
import threading

def sum_list(numbers):
    total = sum(numbers)  # Uproszczony sposób sumowania
    print(total)

# Utworzenie wątków
threads = [
    threading.Thread(target=sum_list, args=([1, 2, 3],)),
    threading.Thread(target=sum_list, args=([4, 5, 6],)),
    threading.Thread(target=sum_list, args=([7, 8, 9],))
]

# Uruchomienie wątków
for thread in threads:
    thread.start()

# Oczekiwanie na zakończenie wątków
for thread in threads:
    thread.join()
```

Ostateczna uwaga: Gdy chcemy przyspieszyć operacje w Pythonie, warto też rozważyć użycie bibliotek specjalizujących się w równoległości, takich jak `Dask` czy `Joblib`.
