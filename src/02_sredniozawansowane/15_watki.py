import threading
import time
import random


def sumuj_czesc_listy(poczatek, koniec, lista, wynik):
    wynik[0] = 0
    for i in range(poczatek, koniec):
        wynik[0] += lista[i]
    return wynik[0]


def sumuj_liste(lista, n):
    # Utworz liste wynikow i zainicjalizuj ja zerami
    wyniki = [[0] for _ in range(n)]

    watki = []
    for i in range(n):
        poczatek = i * len(lista) // n
        end = (i + 1) * len(lista) // n
        # Przekaz wynik do watku
        watek = threading.Thread(
            target=sumuj_czesc_listy, args=(poczatek, end, lista, wyniki[i])
        )
        watki.append(watek)
        watek.start()
    for watek in watki:
        watek.join()

    # Zsumuj wyniki
    return int(sum(wynik[0] for wynik in wyniki))


if __name__ == "__main__":
    # utworz liste 30000000 elementow
    lista = [random.random() for i in range(30000000)]

    for n in [1, 5, 10]:
        czas_na_poczatku = time.time()
        wynik = sumuj_liste(lista, n)
        calkowity_czas = time.time() - czas_na_poczatku
        print(f"Dla {n} watkow czas wynosi {calkowity_czas} sekund")
        print(f"Wynik: {wynik}")
        print()
