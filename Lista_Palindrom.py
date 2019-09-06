class Wezel():
    def __init__(self,dane=None):
        self.dane = dane
        self.nastepny = None

class Lista():
    def __init__(self):
        self.head = Wezel()

    def append(self,dane):
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
            wynik +=1
        return wynik

    def usun(self, i):
        if self.head.dane == None:
            print('lista jest pusta!')
            return
        if i >= self.dlugosc() or i < 0:
            print('zly indeks')
            return
        if i == 0:
            self.head = self.head.nastepny
            return
        licznik = self.head
        pozycja = 0
        while licznik.nastepny != None:
            poprzednik = licznik
            licznik = licznik.nastepny
            if pozycja+1 == i:
                poprzednik.nastepny = licznik.nastepny
                return
            pozycja += 1

    def czy_palindrom1(self):
        s = ''
        p = self.head
        while p:
            s += str(p.dane)
            p = p.nastepny
        return s == s[::-1]

    def czy_palindrom2(self):
        s = []
        p = self.head
        while p:
            s.append(p.dane)
            p = p.nastepny
        while p:
            dane = s.pop()
            if p.dane != dane:
                return False
            p = p.nastepny
        return True

lista = Lista()
lista.append(2)
lista.append(3)
lista.append(2)

print(lista.czy_palindrom2())

lista2 = Lista()
lista2.append('a')
lista2.append('c')
lista2.append('a')

print(lista2.czy_palindrom2())

