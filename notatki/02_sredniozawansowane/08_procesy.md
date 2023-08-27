## Procesy

Procesy to samodzielne jednostki wykonywane w systemie operacyjnym, każdy z własną przestrzenią adresową i zasobami. Każdy proces działa niezależnie i jest izolowany od innych procesów. W związku z tym, komunikacja między procesami wymaga specjalnych mechanizmów, takich jak kolejki czy potoki. Procesy są z reguły cięższe niż wątki pod względem zużycia zasobów, ale mają zaletę lepszej izolacji, co sprawia, że są bardziej odporne na błędy i interferencje.

W Pythonie, dzięki modułowi `multiprocessing`, można łatwo tworzyć i zarządzać procesami:

```python
import multiprocessing
import time

def worker():
    print("Rozpoczynam prace")
    time.sleep(2)
    print("Kończę prace")

p = multiprocessing.Process(target=worker)
p.start()
p.join()  # Oczekuje na zakończenie procesu
```

Aby zatrzymać proces przed jego naturalnym zakończeniem, można użyć metody terminate():

```python
p.terminate()
```

Jednak korzystanie z terminate() powinno być ostrożne, ponieważ może prowadzić do nieprzewidywalnych skutków, takich jak niedokończone operacje czy utrata danych.

### Kiedy używać procesów?

- Gdy chcemy osiągnąć równoległość w obliczeniach intensywnie korzystających z CPU, omijając ograniczenia GIL w Pythonie.
- Gdy potrzebujemy izolacji, aby uniknąć zakłóceń pomiędzy różnymi częściami kodu.
- Gdy chcemy równolegle przetwarzać niezależne zadania bez potrzeby dzielenia się stanem.

Pomimo zalet procesów, tworzenie nowego procesu jest bardziej kosztowne niż wątku. Dlatego też, w zastosowaniach wymagających dużej ilości lekkich, krótkotrwałych zadań, wątki mogą być bardziej efektywne.

Dodatkowo, komunikacja międzyprocesowa (Inter-Process Communication, IPC) może być bardziej skomplikowana i mniej wydajna niż komunikacja międzywątkowa. 

### Komunikacja międzyprocesowa (IPC)

Jak wcześniej wspomniano, jednym z wyzwań związanych z procesami jest ich izolacja, co oznacza, że nie mogą one bezpośrednio dzielić się swoim stanem ani zasobami. W związku z tym konieczne jest korzystanie z mechanizmów IPC, aby umożliwić procesom współpracę.

#### Kolejki (multiprocessing.Queue)

Kolejki w module `multiprocessing` działają podobnie jak wątkowe kolejki w module `queue`. Pozwalają one na przesyłanie i odbieranie komunikatów między procesami:

```python
import multiprocessing

def worker(q):
    q.put("Hello from process!")

if __name__ == "__main__":
    q = multiprocessing.Queue()
    p = multiprocessing.Process(target=worker, args=(q,))
    p.start()
    print(q.get())  # Odbieramy komunikat od procesu
    p.join()
```

W tym przykładzie proces potomny wysyła komunikat do procesu głównego za pomocą kolejki.

#### Potoki (multiprocessing.Pipe)

Potoki to kolejny sposób komunikacji między procesami. Składają się z dwóch połączonych końcówek: jednej do wysyłania, a drugiej do odbierania danych.

```python
import multiprocessing

def worker(conn):
    conn.send("Hello from process!")
    conn.close()

if __name__ == "__main__":
    parent_conn, child_conn = multiprocessing.Pipe()
    p = multiprocessing.Process(target=worker, args=(child_conn,))
    p.start()
    print(parent_conn.recv())  # Odbieramy komunikat od procesu
    p.join()
```

Warto zaznaczyć, że obie metody – zarówno kolejki, jak i potoki – powinny być używane z uwagą. Należy pamiętać o możliwych zakleszczeniach (deadlocks) i zapewnić odpowiednie zabezpieczenia, by je unikać.

### Użycie procesów do równoległego obliczenia kwadratów liczb

```python
import multiprocessing

def compute_squares(numbers, result, index):
    print(f"Process {index+1} working with {numbers}")
    for i, num in enumerate(numbers):
        result[i] = num * num
    print(f"Process {index+1} done!")

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    n_processes = 3
    size = len(numbers) // n_processes
    processes = []
    result = multiprocessing.Array('i', len(numbers))

    for i in range(n_processes):
        start_index = size * i
        end_index = None if i == n_processes - 1 else start_index + size
        p = multiprocessing.Process(target=compute_squares, args=(numbers[start_index:end_index], result[start_index:end_index], i))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    print(f"Squares: {list(result)}")
```

W tym kodzie dzielimy listę liczb na mniejsze fragmenty i przekazujemy je do różnych procesów. Każdy proces oblicza kwadraty liczb równolegle z innymi procesami. Używamy wspólnej pamięci (w postaci `multiprocessing.Array`) do przechowywania wyników, więc po zakończeniu wszystkich procesów możemy odczytać wyniki.

W rzeczywistych zastosowaniach warto zwrócić uwagę na wybór odpowiedniej liczby procesów. Najczęściej korzystna liczba to liczba rdzeni dostępnych w systemie (chociaż nie zawsze). Zbyt duża liczba procesów może prowadzić do nadmiernego przełączania kontekstu i spowolnienia obliczeń.
