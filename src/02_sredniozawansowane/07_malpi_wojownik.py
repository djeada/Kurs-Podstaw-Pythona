import random
from time import sleep


class Postac:
    def __init__(self, imie, punkty_zycia, sila):
        self.imie = imie
        self.punkty_zycia = punkty_zycia
        self.sila = sila

    def atakuj(self):
        atak = random.randint(0, self.sila)
        return atak

    def czy_zyje(self):
        return self.punkty_zycia > 0


class MalpiWojownik(Postac):
    def __init__(self, imie):
        super().__init__(imie, 20, 10)


class Rycerz(Postac):
    def __init__(self, imie):
        super().__init__(imie, 50, 30)
        self.poziom = 1
        self._doswiadczenie = 0

    def atakuj(self):
        atak = super().atakuj()
        atak = +random.randint(0, self.poziom)
        return atak

    def dodaj_doswiadczenie(self, doswiadczenie):
        self._doswiadczenie += doswiadczenie
        if self._doswiadczenie >= 100:
            self.poziom += 1
            self._doswiadczenie = 0


def walka(postac_a, postac_b):

    # losowanie kto zaczyna
    if random.randint(0, 1) == 0:
        postac_a, postac_b = postac_b, postac_a

    for postac in [postac_a, postac_b]:
        atak = postac.atakuj()
        print(f"{postac.imie} atakuje i zadaje {atak} obrazen")
        postac_b.punkty_zycia -= atak
        print(f"{postac_b.imie} ma {postac_b.punkty_zycia} punktow zycia")


def symulacja(rycerz, malpi_wojownicy):

    print(f"Rycerz {rycerz.imie} wchodzi na arene")
    print(f"Na arenie czeka {len(malpi_wojownicy)} malpich wojownikow")

    while rycerz.czy_zyje() and len(malpi_wojownicy) > 0:
        print()
        malpi_wojownik = random.choice(malpi_wojownicy)

        while malpi_wojownik.czy_zyje() and rycerz.czy_zyje():
            walka(rycerz, malpi_wojownik)

        if not malpi_wojownik.czy_zyje():
            print(f"Malpi wojownik {malpi_wojownik.imie} ginie")
            malpi_wojownicy.remove(malpi_wojownik)
            rycerz.dodaj_doswiadczenie(100)
            print(
                f"Rycerz {rycerz.imie} ma {rycerz.poziom} poziom i {rycerz._doswiadczenie} doswiadczenia"
            )

        if not rycerz.czy_zyje():
            print(f"Rycerz {rycerz.imie} ginie")
            break

        sleep(1)

    if rycerz.czy_zyje():
        print(f"\nRycerz {rycerz.imie} wygrywa")
    else:
        print("\nMalpi wojownicy swietuja zwyciestwo")


if __name__ == "__main__":
    rycerz = Rycerz("James")
    malpie_imiona = [
        "Coco",
        "Barney",
        "Maple",
        "Tarzan",
        "Simba",
        "Zazu",
        "Kiki",
        "Bubbles",
        "Ollie",
        "Jade",
    ]
    malpi_wojownicy = [MalpiWojownik(imie) for imie in malpie_imiona]
    symulacja(rycerz, malpi_wojownicy)
