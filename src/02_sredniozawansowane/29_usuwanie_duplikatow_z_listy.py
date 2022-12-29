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


def usun_duplikaty(lista: ListaPolaczona) -> ListaPolaczona:
    unikalne = ListaPolaczona()
    for wezel in lista:
        if wezel not in unikalne:
            unikalne.dodaj(wezel)
    return unikalne


if __name__ == "__main__":
    lista = ListaPolaczona()
    lista.dodaj(1)
    lista.dodaj(2)
    lista.dodaj(2)
    lista.dodaj(3)
    lista.dodaj(3)
    lista.dodaj(3)
    lista.dodaj(4)
    lista.dodaj(4)
    lista.dodaj(4)
    lista.dodaj(4)
    print(lista)
    print(usun_duplikaty(lista))
