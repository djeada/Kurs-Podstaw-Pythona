from dataclasses import dataclass
from typing import Optional
from collections import deque


@dataclass
class Wezel:
    wartosc: int
    lewy: Optional["Wezel"] = None
    prawy: Optional["Wezel"] = None


class BinarneDrzewoPoszukiwan:
    def __init__(self):
        self.korzen = None

    def dodaj(self, wartosc: int):
        nowy_wezel = Wezel(wartosc)
        if self.korzen is None:
            self.korzen = nowy_wezel
        else:
            aktualny_wezel = self.korzen
            while True:
                if wartosc < aktualny_wezel.wartosc:
                    if aktualny_wezel.lewy is None:
                        aktualny_wezel.lewy = nowy_wezel
                        return
                    aktualny_wezel = aktualny_wezel.lewy
                else:
                    if aktualny_wezel.prawy is None:
                        aktualny_wezel.prawy = nowy_wezel
                        return
                    aktualny_wezel = aktualny_wezel.prawy

    def usun(self, wartosc: int):
        if self.korzen is None:
            return
        if self.korzen.wartosc == wartosc:
            self.korzen = self.korzen.prawy
            return
        aktualny_wezel = self.korzen
        while aktualny_wezel is not None:
            if (
                aktualny_wezel.lewy is not None
                and aktualny_wezel.lewy.wartosc == wartosc
            ):
                aktualny_wezel.lewy = aktualny_wezel.lewy.prawy
                return
            if (
                aktualny_wezel.prawy is not None
                and aktualny_wezel.prawy.wartosc == wartosc
            ):
                aktualny_wezel.prawy = aktualny_wezel.prawy.prawy
                return
            if wartosc < aktualny_wezel.wartosc:
                aktualny_wezel = aktualny_wezel.lewy
            else:
                aktualny_wezel = aktualny_wezel.prawy

    def dlugosc(self) -> int:
        dlugosc = 0
        aktualny_wezel = self.korzen
        while aktualny_wezel is not None:
            dlugosc += 1
            aktualny_wezel = aktualny_wezel.prawy
        return dlugosc

    def wypisz_poziomami(self) -> None:
        def _wypisz_poziomami(wezel: Wezel, poziom: int) -> None:
            if wezel is not None:
                _wypisz_poziomami(wezel.lewy, poziom + 1)
                print(" " * 4 * poziom + "-> " + str(wezel.wartosc))
                _wypisz_poziomami(wezel.prawy, poziom + 1)

        _wypisz_poziomami(self.korzen, 0)

    def __contains__(self, wartosc: int) -> bool:
        aktualny_wezel = self.korzen
        while aktualny_wezel is not None:
            if aktualny_wezel.wartosc == wartosc:
                return True
            if wartosc < aktualny_wezel.wartosc:
                aktualny_wezel = aktualny_wezel.lewy
            else:
                aktualny_wezel = aktualny_wezel.prawy
        return False

    def __iter__(self):
        aktualny_wezel = self.korzen
        while aktualny_wezel is not None:
            yield aktualny_wezel.wartosc
            aktualny_wezel = aktualny_wezel.prawy

    def __str__(self):
        return str(list(self))

    def __repr__(self):
        return str(self)


if __name__ == "__main__":
    drzewo = BinarneDrzewoPoszukiwan()
    drzewo.dodaj(5)
    drzewo.dodaj(3)
    drzewo.dodaj(7)
    drzewo.dodaj(1)
    drzewo.dodaj(4)
    drzewo.dodaj(6)
    drzewo.dodaj(8)
    drzewo.dodaj(2)
    drzewo.dodaj(9)
    drzewo.dodaj(0)
    drzewo.wypisz_poziomami()
    print(drzewo)
    print(drzewo.dlugosc())
    print(5 in drzewo)
    print(10 in drzewo)
    drzewo.usun(5)
    print(drzewo)
    drzewo.usun(0)
    print(drzewo)
    drzewo.usun(9)
    print(drzewo)
