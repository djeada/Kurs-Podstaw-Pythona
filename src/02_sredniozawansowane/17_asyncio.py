import asyncio
import time
import random


async def sumuj_czesc_listy(poczatek, koniec, lista):
    wynik = 0
    for i in range(poczatek, koniec):
        wynik += lista[i]
    return wynik


async def sumuj_liste(lista, n):
    # Utworz liste wynikow i zainicjalizuj ja zerami
    wyniki = [0] * n

    # Utworz liste zadan asynchronicznych
    zadania = []
    for i in range(n):
        poczatek = i * len(lista) // n
        end = (i + 1) * len(lista) // n
        # Dodaj zadanie do listy
        zadanie = asyncio.create_task(sumuj_czesc_listy(poczatek, end, lista))
        zadania.append(zadanie)

    # Czekaj na wszystkie zadania
    wyniki = await asyncio.gather(*zadania)

    # Zsumuj wyniki
    return sum(wyniki)


if __name__ == "__main__":
    # utworz liste 30000000 elementow
    lista = [random.random() for i in range(30000000)]

    for n in [1, 5, 10]:
        czas_na_poczatku = time.time()
        wynik = asyncio.run(sumuj_liste(lista, n))
        calkowity_czas = time.time() - czas_na_poczatku
        print(f"Dla {n} taskow czas wynosi {calkowity_czas} sekund")
        print(f"Wynik: {wynik}")
        print()
