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


def czy_palindrom(lista: ListaPolaczona) -> bool:
    if lista.dlugosc() <= 1:
        return True
    lewy = lista.korzen
    prawy = lista.korzen
    while prawy.nastepny is not None:
        prawy = prawy.nastepny
    while lewy is not prawy and lewy.nastepny is not prawy:
        if lewy.wartosc != prawy.wartosc:
            return False
        lewy = lewy.nastepny
        aktualny = lista.korzen
        while aktualny.nastepny is not prawy:
            aktualny = aktualny.nastepny
        prawy = aktualny
    return True


if __name__ == "__main__":
    # test 1: 1, 2, 3
    lista = ListaPolaczona()
    lista.dodaj(1)
    lista.dodaj(2)
    lista.dodaj(3)
    print(f"Lista: {lista} jest palindromem: {czy_palindrom(lista)}")

    # test 2: 1, 2, 2, 1
    lista = ListaPolaczona()
    lista.dodaj(1)
    lista.dodaj(2)
    lista.dodaj(2)
    lista.dodaj(1)
    print(f"Lista: {lista} jest palindromem: {czy_palindrom(lista)}")

    # test 3: 1, 2, 3, 2, 1
    lista = ListaPolaczona()
    lista.dodaj(1)
    lista.dodaj(2)
    lista.dodaj(3)
    lista.dodaj(2)
    lista.dodaj(1)
    print(f"Lista: {lista} jest palindromem: {czy_palindrom(lista)}")
