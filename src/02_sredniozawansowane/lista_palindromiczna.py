# kajak
# 19,9,8,9,91


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

    def czyPalindrom1(self):
        napis = ""
        licznik = self.head
        while licznik:
            napis += str(licznik.dane)
            licznik = licznik.nastepny
        return napis == napis[::-1]

    def czyPalindrom2(self):
        stos = []
        licznik = self.head
        while licznik:
            stos.append(licznik.dane)
            licznik = licznik.nastepny
        licznik = self.head
        while licznik:
            if licznik.dane != stos.pop():
                return False
            licznik = licznik.nastepny
        return True


lista1 = Lista()
lista2 = Lista()
lista3 = Lista()
lista1.append("a")
lista1.append("b")
lista1.append("d")
lista1.append("b")
lista1.append("a")

lista2.append(1)
lista2.append(3)
lista2.append(8)
lista2.append(3)
lista2.append(1)

lista3.append(1)
lista3.append(5)
lista3.append(8)
lista3.append(3)
lista3.append(1)


print(lista1.czyPalindrom2())
print(lista2.czyPalindrom2())
print(lista3.czyPalindrom2())
