import random
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

    def odworc_iter(self):
        poprzednik = None
        licznik = self.head
        while licznik:
            nastepnik = licznik.nastepny
            licznik.nastepny = poprzednik
            poprzednik = licznik
            licznik = nastepnik
        self.head = poprzednik

    def odworc_rek(self):
        
        def odwroc_rek_wew(licznik, poprzednik):
            if not licznik:
                self.head = poprzednik
                return

            nastepnik = licznik.nastepny
            licznik.nastepny = poprzednik
            
            odwroc_rek_wew(nastepnik, licznik)
            
        odwroc_rek_wew(licznik=self.head, poprzednik=None)
       
lista = Lista()
for i in range(5):
    lista.append(random.randint(0,30))

print('Przed: ')
lista.wyswietl()
lista.odworc_iter()
print('Po: ')
lista.wyswietl()
lista.odworc_iter()
print('Po: ')
lista.wyswietl()
lista.odworc_rek()
print('Po: ')
lista.wyswietl()


