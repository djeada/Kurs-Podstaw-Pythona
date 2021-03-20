import random


class Wezel:
    def __init__(self, dane=None):
        self.dane = dane
        self.nastepny = None


class Lista:
    def __init__(self):
        self.head = Wezel()

    def append(self, dane):
        dostawiany_wezel = Wezel(dane)
        if self.head.dane == None:
            self.head = dostawiany_wezel
        else:
            licznik = self.head
            while licznik.nastepny != None:
                licznik = licznik.nastepny
            licznik.nastepny = dostawiany_wezel

    def wyswietl(self):
        licznik = self.head
        print(licznik.dane)
        while licznik.nastepny != None:
            print(licznik.nastepny.dane)
            licznik = licznik.nastepny

    def dlugosc(self):
        licznik = self.head
        if self.head.dane == None:
            return 0
        wynik = 1
        while licznik.nastepny != None:
            licznik = licznik.nastepny
            wynik += 1
        return wynik

    def usun(self, i):
        if self.head.dane == None:
            print("lista jest pusta!")
            return
        if i >= self.dlugosc() or i < 0:
            print("zly indeks")
            return
        if i == 0:
            self.head = self.head.nastepny
            return
        licznik = self.head
        pozycja = 0
        while licznik.nastepny != None:
            poprzednik = licznik
            licznik = licznik.nastepny
            if pozycja + 1 == i:
                poprzednik.nastepny = licznik.nastepny
                return
            pozycja += 1

    def pobierz(self, i):
        if self.head.dane == None:
            print("lista jest pusta!")
            return
        if i >= self.dlugosc() or i < 0:
            print("zly indeks")
            return
        licznik = self.head
        pozycja = 0
        while licznik:
            if pozycja == i:
                return licznik.dane
            pozycja += 1
            licznik = licznik.nastepny

    def podziel(self):
        dlugosc = self.dlugosc()
        if dlugosc == 0:
            return None
        if dlugosc == 1:
            return self.head

        a = Lista()
        b = Lista()

        srodek = int(dlugosc / 2)
        licznik = self.head
        pozycja = 0

        while pozycja < srodek:
            a.append(licznik.dane)
            licznik = licznik.nastepny
            pozycja += 1

        while licznik:
            b.append(licznik.dane)
            licznik = licznik.nastepny

        return a, b

    def sortuj(self):
        if self.dlugosc() <= 1:
            return self
        else:
            a, b = self.podziel()
            return scal(a.sortuj(), b.sortuj())


def scal(a, b):
    pozycja_a = pozycja_b = 0

    polaczone_listy = Lista()
    dlugosc_poloczonych_list = a.dlugosc() + b.dlugosc()

    while polaczone_listy.dlugosc() < dlugosc_poloczonych_list:
        if a.pobierz(pozycja_a) <= b.pobierz(pozycja_b):
            polaczone_listy.append(a.pobierz(pozycja_a))
            pozycja_a += 1
        else:
            polaczone_listy.append(b.pobierz(pozycja_b))
            pozycja_b += 1

        if pozycja_a == a.dlugosc():
            while pozycja_b < b.dlugosc():
                polaczone_listy.append(b.pobierz(pozycja_b))
                pozycja_b += 1

        elif pozycja_b == b.dlugosc():
            while pozycja_a < a.dlugosc():
                polaczone_listy.append(a.pobierz(pozycja_a))
                pozycja_a += 1

    return polaczone_listy


lista = Lista()

for i in range(30):
    lista.append(random.randint(0, 50))

print("Przed sortowaniem: ")
lista.wyswietl()

print("Posortowaniu: ")
lista.sortuj().wyswietl()
