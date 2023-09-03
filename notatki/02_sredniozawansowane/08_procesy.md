## Procesy

Procesy to samodzielne jednostki wykonywane w systemie operacyjnym, każdy z własną przestrzenią adresową i zasobami. Każdy proces działa niezależnie i jest izolowany od innych procesów. W związku z tym, komunikacja między procesami wymaga specjalnych mechanizmów, takich jak kolejki czy potoki. Procesy są z reguły cięższe niż wątki pod względem zużycia zasobów, ale mają zaletę lepszej izolacji, co sprawia, że są bardziej odporne na błędy i interferencje.

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

Warto zaznaczyć, że obie metody – zarówno kolejki, jak i potoki – powinny być używane z uwagą. Należy pamiętać o możliwych zakleszczeniach (deadlocks) i zapewnić odpowiednie zabezpieczenia, by je unikać.

### Użycie procesów do równoległego obliczenia kwadratów liczb

```python
import multiprocessing

def oblicz_kwadraty(liczby, wynik, indeks):
    print(f"Proces {indeks+1} pracuje z {liczby}")
    for i, liczba in enumerate(liczby):
        wynik[i] = liczba * liczba
    print(f"Proces {indeks+1} zakończony!")

if __name__ == "__main__":
    liczby = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    liczba_procesow = 3
    rozmiar = len(liczby) // liczba_procesow
    procesy = []
    wynik = multiprocessing.Array('i', len(liczby))

    for i in range(liczba_procesow):
        indeks_startowy = rozmiar * i
        indeks_koncowy = None if i == liczba_procesow - 1 else indeks_startowy + rozmiar
        p = multiprocessing.Process(target=oblicz_kwadraty, args=(liczby[indeks_startowy:indeks_koncowy], wynik[indeks_startowy:indeks_koncowy], i))
        procesy.append(p)
        p.start()

    for p in procesy:
        p.join()

    print(f"Kwadraty: {list(wynik)}")
```

W tym kodzie dzielimy listę liczb na mniejsze fragmenty i przekazujemy je do różnych procesów. Każdy proces oblicza kwadraty liczb równolegle z innymi procesami. Używamy wspólnej pamięci (w postaci `multiprocessing.Array`) do przechowywania wyników, więc po zakończeniu wszystkich procesów możemy odczytać wyniki.

W rzeczywistych zastosowaniach warto zwrócić uwagę na wybór odpowiedniej liczby procesów. Najczęściej korzystna liczba to liczba rdzeni dostępnych w systemie (chociaż nie zawsze). Zbyt duża liczba procesów może prowadzić do nadmiernego przełączania kontekstu i spowolnienia obliczeń.
