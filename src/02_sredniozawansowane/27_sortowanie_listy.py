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


def sorotowanie_przez_scalanie(lista: ListaPolaczona) -> ListaPolaczona:
    if lista.dlugosc() <= 1:
        return lista
    lista1 = ListaPolaczona()
    lista2 = ListaPolaczona()
    for i, wezel in enumerate(lista):
        if i < lista.dlugosc() // 2:
            lista1.dodaj(wezel)
        else:
            lista2.dodaj(wezel)
    lista1 = sorotowanie_przez_scalanie(lista1)
    lista2 = sorotowanie_przez_scalanie(lista2)
    return scalanie_list(lista1, lista2)


def scalanie_list(lista1: ListaPolaczona, lista2: ListaPolaczona) -> ListaPolaczona:
    lista = ListaPolaczona()
    while lista1.dlugosc() > 0 and lista2.dlugosc() > 0:
        if lista1.korzen.wartosc < lista2.korzen.wartosc:
            lista.dodaj(lista1.korzen.wartosc)
            lista1.usun(lista1.korzen.wartosc)
        else:
            lista.dodaj(lista2.korzen.wartosc)
            lista2.usun(lista2.korzen.wartosc)
    while lista1.dlugosc() > 0:
        lista.dodaj(lista1.korzen.wartosc)
        lista1.usun(lista1.korzen.wartosc)
    while lista2.dlugosc() > 0:
        lista.dodaj(lista2.korzen.wartosc)
        lista2.usun(lista2.korzen.wartosc)
    return lista


if __name__ == "__main__":
    lista = ListaPolaczona()
    lista.dodaj(5)
    lista.dodaj(2)
    lista.dodaj(1)
    lista.dodaj(3)
    lista.dodaj(4)
    print(lista)
    print(sorotowanie_przez_scalanie(lista))
