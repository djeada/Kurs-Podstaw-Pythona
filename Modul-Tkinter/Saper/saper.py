import tkinter as tk
import random

N = 15
M = 30

CZAS = 0
LICZBA_MIN = 2
POZOSTALA_LICZBA_FLAG = LICZBA_MIN
LICZBA_TRAFIONYCH_MIN = 0

CZY_KONIEC_GRY = False


def inicjalizacjaOkienka():
    root = tk.Tk()
    root.geometry("900x600")
    root.title("saper")

    return root


def inicjalizacjaGornegoPanela(root, ikonki):

    licznik_min = tk.Label(root, bg="black", fg="red", font=("Digital-7", 40))
    licznik_min.grid(row=0, column=0, columnspan=7, ipadx=10, pady=30)
    aktualizujLicznikMin(licznik_min)

    buzka = tk.Button(root)
    buzka.grid(row=0, column=M // 2 - 1, columnspan=3, pady=30)
    buzka["image"] = ikonki["buzki"][0]

    zegar = tk.Label(root, bg="black", fg="red", font=("Digital-7", 40))
    zegar.grid(row=0, column=M - 6, columnspan=7, ipadx=10, pady=30)
    aktualizujZegar(root, zegar)

    gorny_panel = [licznik_min, buzka, zegar]

    return gorny_panel


def inicjalizacjaPlanszy(root, gorny_panel, ikonki):
    przyciski = [tk.Button(root) for i in range(N * M)]

    tablica_gry = inicjalizacjaTablicyGry()

    for i in range(N):
        for j in range(M):
            wstawPrzyciskNaKrate(przyciski, j, i)
            przyciski[i * M + j].bind(
                "<Button-1>",
                lambda event, p=przyciski[i * M + j]: lewyKlik(
                    przyciski, p, gorny_panel, tablica_gry, ikonki
                ),
            )
            przyciski[i * M + j].bind(
                "<Button-3>",
                lambda event, p=przyciski[i * M + j]: prawyKlik(
                    przyciski, p, gorny_panel, tablica_gry, ikonki
                ),
            )
            przyciski[i * M + j].bind(
                "<ButtonRelease>", lambda event: zwyklaBuzka(gorny_panel[1])
            )

    return przyciski


def znajdzSasiadow(tablica, x, y):

    sasiedzi = []

    for i in range(-1, 2):
        for j in range(-1, 2):
            if not (i == 0 and j == 0):
                if y + i >= 0 and y + i < N:
                    if x + j >= 0 and x + j < M:
                        sasiedzi.append((x + j, y + i))

    return sasiedzi


def inicjalizacjaTablicyGry():
    tablica_gry = [[0 for j in range(M)] for i in range(N)]

    l_min = LICZBA_MIN

    while l_min:
        x = random.randint(0, M - 1)
        y = random.randint(0, N - 1)

        if tablica_gry[y][x] == 0:
            tablica_gry[y][x] = "x"
            l_min -= 1

    for i in range(N):
        for j in range(M):
            if tablica_gry[i][j] == 0:
                sasiedzi = znajdzSasiadow(tablica_gry, j, i)

                l_min = 0

                for x, y in sasiedzi:
                    if tablica_gry[y][x] == "x":
                        l_min += 1

                tablica_gry[i][j] = l_min

    return tablica_gry


def aktualizujZegar(root, zegar):
    global CZAS
    CZAS += 1
    zegar["text"] = "0" * (4 - len(str(CZAS))) + str(CZAS)
    root.after(1000, aktualizujZegar, root, zegar)


def aktualizujLicznikMin(licznik_min):
    licznik_min["text"] = "0" * (4 - len(str(LICZBA_MIN))) + str(LICZBA_MIN)


def zwyklaBuzka(buzka):

    if not CZY_KONIEC_GRY:
        gorny_panel[1]["image"] = ikonki["buzki"][0]


def wczytajIkonki():
    ikonki = {}

    ikonki["cyfry"] = [tk.PhotoImage(file=str(i) + ".png") for i in range(1, 9)]
    ikonki["buzki"] = [
        tk.PhotoImage(file="buzka" + str(i) + ".png") for i in range(1, 5)
    ]
    ikonki["flaga"] = tk.PhotoImage(file="flaga.png")
    ikonki["miny"] = [
        tk.PhotoImage(file="mina.png"),
        tk.PhotoImage(file="pierwsza.png"),
    ]

    return ikonki


def wstawPrzyciskNaKrate(przyciski, x, y):
    if x == 0:
        przyciski[y * M + x].grid(row=y + 1, column=x, padx=(30, 0))

    else:
        przyciski[y * M + x].grid(row=y + 1, column=x)


def przegranaGra(przyciski, tablica_gry, ikonki):
    global CZY_KONIEC_GRY

    CZY_KONIEC_GRY = True

    for i in range(N):
        for j in range(M):
            if (
                isinstance(przyciski[i * M + j], tk.Button)
                and przyciski[i * M + j]["state"] != "disabled"
            ):
                przyciski[i * M + j]["state"] = "disabled"
                przyciski[i * M + j].unbind("<Button-1>")
                przyciski[i * M + j].unbind("<Button-3>")

                if tablica_gry[i][j] == "x":
                    przyciski[i * M + j] = tk.Label(root, image=ikonki["miny"][0])
                    wstawPrzyciskNaKrate(przyciski, j, i)


def wygranaGra(przyciski, tablica_gry):
    global CZY_KONIEC_GRY

    CZY_KONIEC_GRY = True

    for i in range(N):
        for j in range(M):
            if (
                isinstance(przyciski[i * M + j], tk.Button)
                and przyciski[i * M + j]["state"] != "disabled"
            ):
                przyciski[i * M + j]["state"] = "disabled"
                przyciski[i * M + j].unbind("<Button-1>")
                przyciski[i * M + j].unbind("<Button-3>")


def aktualizujPrzycisk(przyciski, przycisk, indeks, pole, tablica_gry, ikonki):

    przyciski[indeks].configure(state="disabled", border=1, highlightbackground="black")
    przyciski[indeks].unbind("<Button-1>")
    przyciski[indeks].unbind("<Button-3>")

    if pole != "x":
        if pole != 0:
            przyciski[indeks] = tk.Label(root, image=ikonki["cyfry"][pole - 1])
            wstawPrzyciskNaKrate(przyciski, indeks % M, indeks // M)

        else:
            sasiedzi = znajdzSasiadow(tablica_gry, indeks % M, indeks // M)

            for x, y in sasiedzi:
                if (
                    isinstance(przyciski[y * M + x], tk.Button)
                    and przyciski[y * M + x]["state"] != "disabled"
                ):
                    aktualizujPrzycisk(
                        przyciski,
                        przycisk,
                        y * M + x,
                        tablica_gry[y][x],
                        tablica_gry,
                        ikonki,
                    )


def lewyKlik(przyciski, przycisk, gorny_panel, tablica_gry, ikonki):
    gorny_panel[1]["image"] = ikonki["buzki"][1]

    indeks = przyciski.index(przycisk)
    pole = tablica_gry[indeks // M][indeks % M]

    if pole == "x":
        gorny_panel[1]["image"] = ikonki["buzki"][2]
        przegranaGra(przyciski, tablica_gry, ikonki)

    else:
        aktualizujPrzycisk(przyciski, przycisk, indeks, pole, tablica_gry, ikonki)


def prawyKlik(przyciski, przycisk, gorny_panel, tablica_gry, ikonki):
    gorny_panel[1]["image"] = ikonki["buzki"][1]

    indeks = przyciski.index(przycisk)
    pole = tablica_gry[indeks // M][indeks % M]

    global POZOSTALA_LICZBA_FLAG
    global LICZBA_TRAFIONYCH_MIN

    if przycisk.cget("image"):
        przycisk["image"] = ""
        POZOSTALA_LICZBA_FLAG += 1
        if pole == "x":
            LICZBA_TRAFIONYCH_MIN -= 1

    else:
        przycisk["image"] = ikonki["flaga"]
        POZOSTALA_LICZBA_FLAG -= 1
        if pole == "x":
            LICZBA_TRAFIONYCH_MIN += 1
            if LICZBA_TRAFIONYCH_MIN == LICZBA_MIN:
                gorny_panel[1]["image"] = ikonki["buzki"][3]
                wygranaGra(przyciski, tablica_gry)

    aktualizujLicznikMin(gorny_panel[0])


def resetujGre(root, gorny_panel, ikonki):
    gorny_panel[1]["image"] = ikonki["buzki"][0]
    przyciski = inicjalizacjaPlanszy(root, gorny_panel, ikonki)

    global CZY_KONIEC_GRY
    CZY_KONIEC_GRY = False

    global CZAS
    CZAS = 0

    global POZOSTALA_LICZBA_FLAG
    POZOSTALA_LICZBA_FLAG = LICZBA_MIN
    aktualizujLicznikMin(gorny_panel[0])


if __name__ == "__main__":

    root = inicjalizacjaOkienka()

    ikonki = wczytajIkonki()

    gorny_panel = inicjalizacjaGornegoPanela(root, ikonki)

    przyciski = inicjalizacjaPlanszy(root, gorny_panel, ikonki)

    gorny_panel[1].bind(
        "<Button-1>", lambda event: resetujGre(root, gorny_panel, ikonki)
    )

    root.mainloop()
