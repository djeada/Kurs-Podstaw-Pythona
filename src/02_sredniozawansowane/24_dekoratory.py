import time
import random

# dekorator liczacy czas wykonania funkcji
def licz_czas(funkcja):
    def wrapper(*args, **kwargs):
        poczatek = time.time()
        wynik = funkcja(*args, **kwargs)
        czas = time.time() - poczatek
        print(f"Czas wykonania funkcji: {czas} sekund")
        return wynik

    return wrapper


# dekorator wypisujacy nazwe funkcji
def wyswietl_nazwe(func):
    def wrapper(*args, **kwargs):
        print(f"Nazwa funkcji: {func.__name__}")
        return func(*args, **kwargs)

    return wrapper


@licz_czas
@wyswietl_nazwe
def sumuj_liste(lista):
    suma = 0
    for element in lista:
        suma += element
    return suma


if __name__ == "__main__":
    lista = [random.random() for i in range(30000000)]
    sumuj_liste(lista)
