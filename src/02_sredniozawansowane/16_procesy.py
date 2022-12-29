import multiprocessing
import time
import random


def sumuj_czesc_listy(poczatek, koniec, lista, wynik):
    # Modify the element of the list instead of the list itself
    pom = 0
    for i in range(poczatek, koniec):
        pom += lista[i]
    wynik.send(pom)


def sumuj_liste(lista, n):
    # Uzyj pipe do przekazania wyniku
    wyniki = [multiprocessing.Pipe() for _ in range(n)]

    procesy = []
    for i in range(n):
        poczatek = i * len(lista) // n
        end = (i + 1) * len(lista) // n
        # Przekaz wynik do watku
        proces = multiprocessing.Process(
            target=sumuj_czesc_listy, args=(poczatek, end, lista, wyniki[i][0])
        )
        procesy.append(proces)
        proces.start()
    for proces in procesy:
        proces.join()

    # Zsumuj wyniki
    return int(sum(wynik[1].recv() for wynik in wyniki))


if __name__ == "__main__":
    # utworz liste 30000000 elementow
    lista = [random.random() for i in range(30000000)]

    for n in [1, 5, 10]:
        czas_na_poczatku = time.time()
        wynik = sumuj_liste(lista, n)
        calkowity_czas = time.time() - czas_na_poczatku
        print(f"Dla {n} procesow czas wynosi {calkowity_czas} sekund")
        print(f"Wynik: {wynik}")
        print()
