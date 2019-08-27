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
        
lista = Lista()
lista.append(4)
lista.append(11)
lista.wyswietl()

lista2 = Lista()
lista3 = Lista()
for i in range(10):
    lista3.append(i)
    
print(lista.dlugosc())
print(lista2.dlugosc())
print(lista3.dlugosc())

print('Lista 3 przed usunieciem: ')
lista3.wyswietl()
lista3.usun(0)
lista3.usun(4)
lista3.usun(lista3.dlugosc()-1)
print('Lista 3 po usunieciu: ')
lista3.wyswietl()

lista2.usun(0)

