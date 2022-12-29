from dataclasses import dataclass
from typing import Optional


@dataclass
class Wezel:
    wartosc: int
    nastepny: Optional["Wezel"] = None


class ListaPolaczona:
    def __init__(self):
        self.korzen = None

    def dodaj(self, wartosc: int):
        nowy_wezel = Wezel(wartosc)
        if self.korzen is None:
            self.korzen = nowy_wezel
        else:
            aktualny_wezel = self.korzen
            while aktualny_wezel.nastepny is not None:
                aktualny_wezel = aktualny_wezel.nastepny
            aktualny_wezel.nastepny = nowy_wezel

    def usun(self, wartosc: int):
        if self.korzen is None:
            return
        if self.korzen.wartosc == wartosc:
            self.korzen = self.korzen.nastepny
            return
        aktualny_wezel = self.korzen
        while aktualny_wezel.nastepny is not None:
            if aktualny_wezel.nastepny.wartosc == wartosc:
                aktualny_wezel.nastepny = aktualny_wezel.nastepny.nastepny
                return
            aktualny_wezel = aktualny_wezel.nastepny

    def dlugosc(self) -> int:
        dlugosc = 0
        aktualny_wezel = self.korzen
        while aktualny_wezel is not None:
            dlugosc += 1
            aktualny_wezel = aktualny_wezel.nastepny
        return dlugosc

    def __iter__(self):
        aktualny_wezel = self.korzen
        while aktualny_wezel is not None:
            yield aktualny_wezel.wartosc
            aktualny_wezel = aktualny_wezel.nastepny

    def __str__(self):
        return str(list(self))


if __name__ == "__main__":
    # lista 3, 7, 2, -3, 9

    lista = ListaPolaczona()
    lista.dodaj(3)
    lista.dodaj(7)
    lista.dodaj(2)
    lista.dodaj(-3)
    lista.dodaj(9)

    print(lista)

    # usuniecie 7
    lista.usun(7)
    print(lista)

    # dlugosc listy
    print(lista.dlugosc())

    # usun wszystkie elementy
    lista.usun(3)
    lista.usun(2)
    lista.usun(-3)
    lista.usun(9)

    print(lista)
    print(lista.dlugosc())
