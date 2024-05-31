## Procesy

Procesy to samodzielne jednostki wykonywane w systemie operacyjnym, każda z własną przestrzenią adresową i zasobami. Każdy proces działa niezależnie i jest izolowany od innych procesów. W związku z tym, komunikacja między procesami wymaga specjalnych mechanizmów, takich jak kolejki czy potoki. Procesy są z reguły cięższe niż wątki pod względem zużycia zasobów, ale mają zaletę lepszej izolacji, co sprawia, że są bardziej odporne na błędy i interferencje.

W Pythonie, dzięki modułowi `multiprocessing`, można łatwo tworzyć i zarządzać procesami:

```python
import multiprocessing
import time

def pracownik():
    print("Rozpoczynam pracę")
    time.sleep(2)
    print("Kończę pracę")

proces = multiprocessing.Process(target=pracownik)
proces.start()
proces.join()  # Oczekuje na zakończenie procesu
```

Aby zatrzymać proces przed jego naturalnym zakończeniem, można użyć metody `terminate()`:

```python
proces.terminate()
```

Jednak korzystanie z `terminate()` powinno być ostrożne, ponieważ może prowadzić do nieprzewidywalnych skutków, takich jak niedokończone operacje czy utrata danych.

### Zalety Procesów

1. **Izolacja**: Procesy mają swoją własną przestrzeń adresową, co oznacza, że błąd w jednym procesie nie wpłynie na inne procesy. To sprawia, że aplikacje są bardziej odporne na błędy.
2. **Równoległość**: Procesy mogą działać równolegle na wielu rdzeniach CPU, co pozwala na pełne wykorzystanie możliwości wielordzeniowych procesorów.
3. **Bezpieczeństwo**: Dzięki izolacji procesów, dane są lepiej chronione przed nieautoryzowanym dostępem i zakłóceniami.

### Wady Procesów

1. **Koszt tworzenia**: Tworzenie nowego procesu jest bardziej zasobożerne niż tworzenie nowego wątku, co może być problematyczne w aplikacjach wymagających wielu krótkotrwałych zadań.
2. **Komunikacja**: Komunikacja między procesami (IPC) może być bardziej skomplikowana i mniej wydajna niż komunikacja między wątkami. Wymaga to użycia dodatkowych mechanizmów, takich jak kolejki, potoki czy pamięć dzielona.
3. **Zużycie zasobów**: Procesy zużywają więcej zasobów systemowych niż wątki, co może prowadzić do większego obciążenia systemu.

### Kiedy używać procesów?

- **Obliczenia intensywnie korzystające z CPU**: Procesy są idealne do wykonywania obliczeń, które intensywnie korzystają z CPU, ponieważ omijają ograniczenia Global Interpreter Lock (GIL) w Pythonie.
- **Izolacja**: Kiedy potrzebna jest izolacja różnych części kodu, aby uniknąć zakłóceń między nimi.
- **Niezależne zadania**: Kiedy chcemy równolegle przetwarzać zadania, które nie wymagają dzielenia się stanem.

### Komunikacja międzyprocesowa (IPC)

Jak wcześniej wspomniano, jednym z wyzwań związanych z procesami jest ich izolacja, co oznacza, że nie mogą one bezpośrednio dzielić się swoim stanem ani zasobami. W związku z tym konieczne jest korzystanie z mechanizmów IPC, aby umożliwić procesom współpracę.

#### Kolejki (multiprocessing.Queue)

Kolejki w module `multiprocessing` działają podobnie jak wątkowe kolejki w module `queue`. Pozwalają one na przesyłanie i odbieranie komunikatów między procesami:

```python
import multiprocessing

def pracownik(kolejka):
    kolejka.put("Proces pozdrawia serdecznie!")

if __name__ == "__main__":
    kolejka = multiprocessing.Queue()
    proces = multiprocessing.Process(target=pracownik, args=(kolejka,))
    proces.start()
    print(kolejka.get())  # Odbieramy komunikat od procesu
    proces.join()
```

W tym przykładzie proces potomny wysyła komunikat do procesu głównego za pomocą kolejki.

#### Potoki (multiprocessing.Pipe)

Potoki to kolejny sposób komunikacji między procesami. Składają się z dwóch połączonych końcówek: jednej do wysyłania, a drugiej do odbierania danych.

```python
import multiprocessing

def pracownik(polaczenie):
    polaczenie.send("Proces pozdrawia serdecznie!")
    polaczenie.close()

if __name__ == "__main__":
    polaczenie_rodzica, polaczenie_dziecka = multiprocessing.Pipe()
    proces = multiprocessing.Process(target=pracownik, args=(polaczenie_dziecka,))
    proces.start()
    print(polaczenie_rodzica.recv())  # Odbieramy komunikat od procesu
    proces.join()
```

#### Menedżery (multiprocessing.Manager)

Dla bardziej złożonych struktur danych, takich jak listy czy słowniki, można użyć `multiprocessing.Manager`, który pozwala na udostępnianie tych struktur między procesami.

```python
import multiprocessing

def pracownik(lista, slownik):
    lista.append("Proces dodał element do listy")
    slownik["klucz"] = "Wartość dodana przez proces"

if __name__ == "__main__":
    with multiprocessing.Manager() as manager:
        lista = manager.list()
        slownik = manager.dict()
        
        proces = multiprocessing.Process(target=pracownik, args=(lista, slownik))
        proces.start()
        proces.join()
        
        print(lista)
        print(slownik)
```

W powyższym przykładzie proces potomny dodaje elementy do współdzielonej listy i słownika.

#### Zabezpieczenia przed zakleszczeniami

Podczas korzystania z mechanizmów IPC należy pamiętać o możliwych zakleszczeniach (deadlocks). Ważne jest, aby:

1. **Unikać cyklicznego oczekiwania**: Upewnij się, że żadne dwa procesy nie oczekują na zasoby zajmowane przez siebie nawzajem.
2. **Używać timeoutów**: W metodach takich jak `get()` czy `recv()` można ustawiać timeouty, aby uniknąć nieskończonego oczekiwania.

```python
import multiprocessing
import queue

def pracownik(kolejka):
    try:
        kolejka.put("Proces pozdrawia serdecznie!", timeout=1)
    except queue.Full:
        print("Kolejka jest pełna")

if __name__ == "__main__":
    kolejka = multiprocessing.Queue(maxsize=1)
    proces = multiprocessing.Process(target=pracownik, args=(kolejka,))
    proces.start()
    try:
        print(kolejka.get(timeout=1))  # Odbieramy komunikat od procesu
    except queue.Empty:
        print("Kolejka jest pusta")
    proces.join()
```

### Użycie procesów do równoległego obliczenia kwadratów liczb

```python
import multiprocessing

# Funkcja obliczająca kwadraty liczb
def oblicz_kwadraty(liczby, wynik, indeks):
    print(f"Proces {indeks + 1} pracuje z {liczby}")
    for i, liczba w enumerate(liczby):
        wynik[i] = liczba * liczba
    print(f"Proces {indeks + 1} zakończony!")

# Główna część programu
if __name__ == "__main__":
    liczby = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    liczba_procesow = 3
    rozmiar = len(liczby) // liczba_procesow
    procesy = []
    wynik = multiprocessing.Array('i', len(liczby))

    # Tworzenie i uruchamianie procesów
    for i in range(liczba_procesow):
        indeks_startowy = rozmiar * i
        indeks_koncowy = len(liczby) if i == liczba_procesow - 1 else indeks_startowy + rozmiar
        p = multiprocessing.Process(target=oblicz_kwadraty, args=(liczby[indeks_startowy:indeks_koncowy], wynik[indeks_startowy:indeks_koncowy], i))
        procesy.append(p)
        p.start()

    # Czekanie na zakończenie wszystkich procesów
    for p in procesy:
        p.join()

    # Wyświetlenie wyników
    print(f"Kwadraty: {list(wynik)}")
```

W tym kodzie dzielimy listę liczb na mniejsze fragmenty i przekazujemy je do różnych procesów. Każdy proces oblicza kwadraty liczb równolegle z innymi procesami. Używamy wspólnej pamięci (w postaci `multiprocessing.Array`) do przechowywania wyników, więc po zakończeniu wszystkich procesów możemy odczytać wyniki.

Kluczowe aspekty:

1. **Podział pracy**: Dzielenie listy na fragmenty, które przetwarzają poszczególne procesy, pozwala na równoległe wykonywanie obliczeń.
2. **Synchronizacja wyników**: Użycie `multiprocessing.Array` umożliwia współdzielenie wyników między procesami. Jest to wspólna pamięć, w której procesy zapisują wyniki swoich obliczeń.
3. **Efektywne użycie zasobów**: Wybór liczby procesów powinien odpowiadać liczbie dostępnych rdzeni procesora, aby zapewnić optymalne wykorzystanie zasobów systemowych.

### Dynamiczne przypisywanie zadań

W bardziej zaawansowanych scenariuszach warto rozważyć dynamiczne przypisywanie zadań procesom za pomocą kolejek. Poniższy przykład ilustruje, jak to zrobić:

```python
import multiprocessing

def oblicz_kwadraty_task(kolejka, wynik):
    while True:
        indeks, liczba = kolejka.get()
        if liczba is None:
            break
        wynik[indeks] = liczba * liczba

if __name__ == "__main__":
    liczby = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    liczba_procesow = 3
    kolejka = multiprocessing.Queue()
    wynik = multiprocessing.Array('i', len(liczby))
    procesy = []

    # Tworzenie procesów
    for _ in range(liczba_procesow):
        p = multiprocessing.Process(target=oblicz_kwadraty_task, args=(kolejka, wynik))
        procesy.append(p)
        p.start()

    # Wysyłanie zadań do kolejki
    for i, liczba w enumerate(liczby):
        kolejka.put((i, liczba))

    # Wysyłanie sygnału zakończenia do procesów
    for _ in range(liczba_procesow):
        kolejka.put((None, None))

    # Czekanie na zakończenie wszystkich procesów
    for p in procesy:
        p.join()

    # Wyświetlenie wyników
    print(f"Kwadraty: {list(wynik)}")
```

W powyższym przykładzie dynamicznie przypisujemy zadania procesom za pomocą kolejki. Jest to bardziej elastyczne podejście, które pozwala lepiej wykorzystać zasoby w przypadku, gdy liczba zadań jest zmienna lub gdy zadania mają różny czas wykonania.
