
## Wątki
Wątki, pozwalają na równoległe wykonywanie się kilku fragmentów kodu. Z tego powodu są szczególnie przydatne do obsługi zadań, które mogą zająć dużo czasu, np. łączenie się z zewnętrznym serwerem lub wczytywanie dużych plików. W ten sposób nie musimy czekać na zakończenie danego zadania, lecz możemy je wykonać równolegle z pozostałymi czynnościami.

Aby skorzystać z wątków, należy najpierw zaimportować moduł <code>threading</code>. Następnie, aby utworzyć nowy wątek, należy utworzyć obiekt klasy <code>Thread</code>. Klasa ta przyjmuje jako argument funkcję, która będzie wykonana jako wątek.

```python
import threading
def watek():
    print("Watek")

w1 = threading.Thread(target=watek)
```

Aby uruchomić wątek, należy wywołać metodę <code>start</code> na obiekcie klasy <code>Thread</code>.

```python
w1.start()
```

Należy pamiętać, że wątki działają równolegle, więc nie ma gwarancji kolejności wykonywania się poszczególnych wątków. 

### Własny wątek

Aby utworzyć wątek, należy stworzyć klasę dziedziczącą po klasie <code>Thread</code> z modułu <code>threading</code> i zdefiniować metodę <code>run</code>, która zostanie wywołana przy uruchomieniu wątku. Następnie należy utworzyć obiekt tej klasy i wywołać metodę <code>start</code>, aby rozpocząć działanie wątku.

```python
import threading

class MyThread(threading.Thread):
    def run(self):
        # kod, ktory zostanie wykonany w watku
        print("Wątek uruchomiony")

thread = MyThread()
thread.start()
```

Możemy również przekazać argumenty do metody <code>run</code> poprzez konstruktor klasy.

```python
import threading

class MyThread(threading.Thread):
    def __init__(self, argument):
        self.argument = argument
        super().__init__()

    def run(self):
        # kod, ktory zostanie wykonany w watku
        print(f"Wątek uruchomiony z argumentem: {self.argument}")

thread = MyThread("Hello World")
thread.start()
```

### Zatrzymanie wątku

W Pythonie można zatrzymać wątek poprzez wywołanie metody `Thread.join()`. Ta metoda blokuje wywołujący wątek aż do momentu, gdy wątek do którego została wywołana zakończy swoje działanie. Przykładowo, jeśli chcemy zatrzymać główny wątek programu do momentu, gdy wszystkie wątki zostaną zakończone, możemy użyć pętli for i iterować po liście wątków i dla każdego z nich wywołać metodę `join()`:

```python
threads = [thread1, thread2, thread3]

for thread in threads:
    thread.join()
```

Można również użyć metody `Thread.join(timeout)` z opcjonalnym parametrem `timeout`. Parametr ten określa maksymalny czas oczekiwania na zakończenie wątku. Jeśli wątek nie zakończy działania w ciągu tego czasu, wątek wywołujący metodę `join()` zostanie wznowiony.

Innym sposobem zatrzymania wątku jest użycie zmiennej globalnej `threading.Event` z metodami `wait()` i `set()`. Wątek, który chcemy zatrzymać, może oczekiwać na sygnał za pomocą metody `wait()`, a wątek główny może wysłać sygnał za pomocą metody `set()`. W przypadku użycia tej metody, wątek oczekujący może również ustawić opcjonalny limit czasu oczekiwania.

```python
import threading

# utworzenie zmiennej Event
stop_event = threading.Event()

def worker_thread():
    while not stop_event.is_set():
        # wątek wykonuje swoje zadania
        do_some_work()
    # po otrzymaniu sygnalu zatrzymujemy watek
    stop_event.clear()

# ...

# glowny watek chce zatrzymac worker_thread
stop_event.set()
```

Należy pamiętać, że zatrzymanie wątku nie jest powszechnie zalecaną metodą zarządzania wątkami. W wielu przypadkach lepszym rozwiązaniem jest użycie warunków synchronizacyjnych lub zamknięcia wątku za pomocą metody `join()`. Zatrzymanie wątku może powodować nieoczekiwane skutki uboczne i powinno być używane jedynie w wyjątkowych sytuacjach.

### Dzielenie zasobów między wątkami

Dzielenie zasobów między wątkami polega na umożliwieniu kilku wątkom równoczesnego dostępu do wspólnego zasobu. W przypadku, gdy zasób jest zmienny, konieczne jest zapewnienie bezpieczeństwa jego dostępu, tzn. zapobiegnięcie sytuacji, w której kilka wątków będzie próbowało zmodyfikować ten sam zasób w tym samym czasie. Istnieją mechanizmy umożliwiające bezpieczne dzielenie zasobów między wątkami, takie jak obiekt `Lock`.

Przykład:

```python
import threading

# Zmienna globalna, do której będą miały dostęp wątki
zmienna_globalna = 0

# Obiekt Lock, który będziemy używali do synchronizacji dostępu do zmiennej globalnej
lock = threading.Lock()

def watek1():
    global zmienna_globalna
    for i in range(100):
    # Pobieramy lock, aby mieć pewność, że tylko jeden wątek będzie
    # miał dostęp do zmiennej globalnej w danym momencie
    lock.acquire()
    zmienna_globalna += 1
    lock.release()

def watek2():
    global zmienna_globalna
    for i in range(100):
    # Pobieramy lock, aby mieć pewność, że tylko jeden wątek będzie
    # miał dostęp do zmiennej globalnej w danym momencie
    lock.acquire()
    zmienna_globalna -= 1
    lock.release()

# Uruchamiamy wątki
t1 = threading.Thread(target=watek1)
t2 = threading.Thread(target=watek2)

t1.start()
t2.start()

# Czekamy na zakończenie obu wątków
t1.join()
t2.join()

# Wypisujemy wartość zmiennej globalnej
print(zmienna_globalna)
```

W tym przykładzie mamy dwie funkcje `watek1` i `watek2`, które zmieniają wartość zmiennej globalnej `zmienna_globalna`. Aby zapewnić bezpieczne dzielenie zasobów między wątkami, użyto mechanizmu blokady. 

### GIL
GIL, czyli Global Interpreter Lock, to mechanizm, który ogranicza możliwość jednoczesnego wykonywania kodu przez wiele wątków. W Pythonie każdy wątek jest obsługiwany przez GIL, który kontroluje dostęp do interpretera. W rezultacie tylko jeden wątek jest w stanie wykonywać kod naraz, a pozostałe są zawieszane aż do momentu, gdy GIL zostanie zwolniony.

GIL jest wbudowanym mechanizmem w Pythonie, który został dodany w celu uniknięcia problemów związanych z współdzieleniem zasobów przez wiele wątków. Chociaż GIL może mieć pewne ograniczenia w przypadku bardzo obciążających procesów wielowątkowych, w większości przypadków jest on wystarczający do obsługi równoległości w Pythonie.

Przykładowo, jeśli chcielibyśmy utworzyć program, który będzie sumował elementy w liście, możemy to zrobić za pomocą wielu wątków. Każdy wątek będzie odpowiedzialny za sumowanie części listy. Niestety, GIL spowoduje, że tylko jeden wątek będzie wykonywany w danym momencie, co spowolni działanie programu.

Oto przykład programu sumującego elementy w liście z użyciem wątków:

```python
import threading

def sum_list(numbers):
    # Funkcja sumująca elementy w liście
    total = 0
    for number in numbers:
        total += number
    print(total)

# Utworzenie wątków
thread1 = threading.Thread(target=sum_list, args=([1, 2, 3],))
thread2 = threading.Thread(target=sum_list, args=([4, 5, 6],))
thread3 = threading.Thread(target=sum_list, args=([7, 8, 9],))

# Uruchomienie wątków
thread1.start()
thread2.start()
thread3.start()

# Oczekiwanie na zakończenie wątków
thread1.join()
thread2.join()
thread3.join()
```

W powyższym przykładzie, chociaż mamy trzy wątki, GIL spowoduje, że tylko jeden z nich będzie wykonywany w danym momencie, co sprawi że użycie wątków nie pomoże z przyspieszeniem działania progrmau.
