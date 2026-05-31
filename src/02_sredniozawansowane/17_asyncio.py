"""
Modul demonstracyjny: Programowanie asynchroniczne z asyncio.

Omawiane zagadnienia:
- Korutyny (async/await)
- Uruchamianie zadan rownoleglych (asyncio.gather)
- asyncio.create_task
- Symulacja operacji I/O (asyncio.sleep)
- Timeout i obsluga bledow
- Semafory (ograniczanie wspolbieznosci)
- Kolejki asynchroniczne (asyncio.Queue)
- Porownanie wydajnosci sekwencyjnej vs asynchronicznej
"""

import asyncio
import time
import random


# =============================================================================
# 1. Podstawy: korutyny i await
# =============================================================================

async def powitanie(imie, opoznienie):
    """Prosta korutyna z opoznieniem."""
    await asyncio.sleep(opoznienie)
    print(f"  Witaj, {imie}! (po {opoznienie}s)")
    return f"gotowe: {imie}"


# =============================================================================
# 2. Rownolegle wykonywanie zadan (gather)
# =============================================================================

async def pobierz_dane(url, czas_odpowiedzi):
    """Symuluje pobieranie danych z serwera."""
    print(f"  Rozpoczynam pobieranie: {url}")
    await asyncio.sleep(czas_odpowiedzi)
    dane = f"Dane z {url} ({czas_odpowiedzi}s)"
    print(f"  Zakonczono: {url}")
    return dane


async def pobierz_wszystkie():
    """Pobiera dane z wielu zrodel rownolegle."""
    zrodla = [
        ("https://api.example.com/users", 1.0),
        ("https://api.example.com/posts", 1.5),
        ("https://api.example.com/comments", 0.8),
        ("https://api.example.com/albums", 1.2),
    ]

    zadania = [pobierz_dane(url, czas) for url, czas in zrodla]
    wyniki = await asyncio.gather(*zadania)
    return wyniki


# =============================================================================
# 3. Timeout - ograniczanie czasu oczekiwania
# =============================================================================

async def wolna_operacja():
    """Symuluje bardzo wolna operacje."""
    await asyncio.sleep(10)
    return "wynik wolnej operacji"


async def z_timeoutem():
    """Demonstruje uzycie asyncio.wait_for z timeoutem."""
    try:
        wynik = await asyncio.wait_for(wolna_operacja(), timeout=2.0)
        print(f"  Wynik: {wynik}")
    except asyncio.TimeoutError:
        print("  Operacja przekroczyla limit czasu (2s)!")


# =============================================================================
# 4. Semafor - ograniczanie liczby rownoczesnych operacji
# =============================================================================

async def przetworz_zadanie(nazwa, semafor):
    """Przetwarza zadanie z ograniczeniem wspolbieznosci."""
    async with semafor:
        print(f"  START: {nazwa}")
        await asyncio.sleep(random.uniform(0.5, 1.5))
        print(f"  KONIEC: {nazwa}")
        return nazwa


async def demo_semafor():
    """Uruchamia wiele zadan z semaforem (max 3 jednoczesnie)."""
    semafor = asyncio.Semaphore(3)
    zadania = [
        przetworz_zadanie(f"Zadanie-{i}", semafor)
        for i in range(8)
    ]
    wyniki = await asyncio.gather(*zadania)
    return wyniki


# =============================================================================
# 5. Kolejka asynchroniczna (producent-konsument)
# =============================================================================

async def producent(kolejka, id_producenta, ile_elementow):
    """Produkuje elementy i umieszcza je w kolejce."""
    for i in range(ile_elementow):
        element = f"P{id_producenta}-elem{i}"
        await asyncio.sleep(random.uniform(0.1, 0.3))
        await kolejka.put(element)
        print(f"  Producent {id_producenta} dodal: {element}")
    print(f"  Producent {id_producenta} zakonczyl prace.")


async def konsument(kolejka, id_konsumenta):
    """Pobiera i przetwarza elementy z kolejki."""
    przetworzone = 0
    while True:
        try:
            element = await asyncio.wait_for(kolejka.get(), timeout=1.0)
            print(f"  Konsument {id_konsumenta} przetwarza: {element}")
            await asyncio.sleep(random.uniform(0.2, 0.5))
            kolejka.task_done()
            przetworzone += 1
        except asyncio.TimeoutError:
            break
    print(f"  Konsument {id_konsumenta} przetworzyl {przetworzone} elementow.")
    return przetworzone


async def demo_kolejka():
    """Demonstruje wzorzec producent-konsument."""
    kolejka = asyncio.Queue(maxsize=5)

    producenci = [
        producent(kolejka, 1, 4),
        producent(kolejka, 2, 3),
    ]
    konsumenci = [
        konsument(kolejka, 1),
        konsument(kolejka, 2),
    ]

    await asyncio.gather(*producenci, *konsumenci)


# =============================================================================
# 6. Sumowanie listy (porownanie wydajnosci)
# =============================================================================

async def sumuj_czesc_listy(poczatek, koniec, lista):
    """Sumuje fragment listy (symulacja pracy asynchronicznej)."""
    wynik = 0
    for i in range(poczatek, koniec):
        wynik += lista[i]
    return wynik


async def sumuj_liste_async(lista, n_zadan):
    """Dzieli sumowanie listy na n rownoczesnych zadan."""
    dlugosc = len(lista)
    zadania = []
    for i in range(n_zadan):
        poczatek = i * dlugosc // n_zadan
        koniec = (i + 1) * dlugosc // n_zadan
        zadanie = asyncio.create_task(sumuj_czesc_listy(poczatek, koniec, lista))
        zadania.append(zadanie)

    wyniki = await asyncio.gather(*zadania)
    return sum(wyniki)


# =============================================================================
# 7. Porownanie sekwencyjne vs asynchroniczne
# =============================================================================

async def sekwencyjne_pobieranie():
    """Pobiera dane sekwencyjnie (jedno po drugim)."""
    start = time.time()
    for i in range(5):
        await asyncio.sleep(0.5)  # symulacja I/O
    czas = time.time() - start
    return czas


async def rownolegle_pobieranie():
    """Pobiera dane rownolegle (wszystkie naraz)."""
    start = time.time()
    zadania = [asyncio.sleep(0.5) for _ in range(5)]
    await asyncio.gather(*zadania)
    czas = time.time() - start
    return czas


# =============================================================================
# Program glowny
# =============================================================================

async def main():
    print("=== 1. Podstawy korutyn ===")
    wynik = await powitanie("Python", 0.5)
    print(f"  Zwrocono: {wynik}")

    print("\n=== 2. Rownolegle pobieranie (gather) ===")
    start = time.time()
    wyniki = await pobierz_wszystkie()
    print(f"  Laczny czas: {time.time() - start:.2f}s (zamiast ~4.5s sekwencyjnie)")
    for w in wyniki:
        print(f"    {w}")

    print("\n=== 3. Timeout ===")
    await z_timeoutem()

    print("\n=== 4. Semafor (max 3 jednoczesnie) ===")
    await demo_semafor()

    print("\n=== 5. Kolejka producent-konsument ===")
    await demo_kolejka()

    print("\n=== 6. Porownanie: sekwencyjne vs rownolegle ===")
    czas_sekw = await sekwencyjne_pobieranie()
    czas_rown = await rownolegle_pobieranie()
    print(f"  Sekwencyjne (5 x 0.5s): {czas_sekw:.2f}s")
    print(f"  Rownolegle  (5 x 0.5s): {czas_rown:.2f}s")
    print(f"  Przyspieszenie: {czas_sekw / czas_rown:.1f}x")

    print("\n=== 7. Sumowanie listy ===")
    lista = [random.random() for _ in range(1_000_000)]
    start = time.time()
    wynik = await sumuj_liste_async(lista, 4)
    czas = time.time() - start
    print(f"  Suma ({len(lista)} elementow, 4 zadania): {wynik:.2f}")
    print(f"  Czas: {czas:.4f}s")


if __name__ == "__main__":
    asyncio.run(main())
