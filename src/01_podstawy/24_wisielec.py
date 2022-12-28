"""
Wisielec

1. Wylosuj haslo i wyswietl je na ekranie jako ciag podkreslnikow.
2. Ustaw licznik zyc.
3. Pobierz znak od gracza.
4. Sprawdz czy znak jest w hasle.
5. Jesli tak, to podmien odpowiednie podkreslniki na odgadnieta litere.
6. Jesli nie, to zmniejsz licznik zyc.
7. Jesli licznik zyc jest wiekszy od 0, to wracamy do kroku 3.
8. Jesli licznik zyc jest rowny 0, to wyswietl komunikat o przegranej.
9. Jesli haslo zostalo odgadniete, to wyswietl komunikat o wygranej.
"""


import random

lista_hasel = ["robot", "komputer", "programowanie", "python", "kurs"]
haslo = random.choice(lista_hasel)
wyswietlany_napis = "_" * len(haslo)
licznik_zyc = 5


def aktualizuj_wyswietlany_napis(znak):
    global wyswietlany_napis
    nowy_napis = ""
    for i in range(len(haslo)):
        if haslo[i] == znak:
            nowy_napis += znak
        else:
            nowy_napis += wyswietlany_napis[i]
    wyswietlany_napis = nowy_napis


def gra():
    global licznik_zyc
    while licznik_zyc > 0:
        print(f"Licznik zyc: {licznik_zyc}")
        print(f"{wyswietlany_napis}\n")
        znak = input("Podaj znak: \n")

        if znak in haslo:
            aktualizuj_wyswietlany_napis(znak)
            if wyswietlany_napis == haslo:
                print(f"\nWygrales! Haslo to {haslo}.")
                break

        else:
            licznik_zyc -= 1

    if licznik_zyc == 0:
        print("\nPrzegrales!")


if __name__ == "__main__":
    gra()
