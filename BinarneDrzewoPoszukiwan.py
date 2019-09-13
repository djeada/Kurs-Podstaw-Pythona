import random

class Wezel():
    def __init__(self,dane=None):
        self.dane = dane
        self.lewe_dziecko = None
        self.prawe_dziecko = None

class Binarne_Drzewo_Poszukiwan():
    def __init__(self):
        self.korzen = Wezel()

    def dodaj(self,dane):
        if self.korzen.dane == None:
            self.korzen.dane = dane
        else:
            def dodaj_do_korzenia(dane, korzen):
                if  dane < korzen.dane:
                    if korzen.lewe_dziecko == None:
                        korzen.lewe_dziecko = Wezel(dane)
                    else:
                        dodaj_do_korzenia(dane, korzen.lewe_dziecko)
                elif dane > korzen.dane:
                    if korzen.prawe_dziecko == None:
                        korzen.prawe_dziecko = Wezel(dane)
                    else:
                        dodaj_do_korzenia(dane, korzen.prawe_dziecko)
            dodaj_do_korzenia(dane, self.korzen)

    def wyswietl(self):
        wynik = ''
        def przechodzenie_wzdluzne(wezel, wynik):
        #Korzeń -> Lewy -> Prawy
            if wezel:
                if wezel.dane:
                    wynik += (str(wezel.dane) + '-')
                    wynik = przechodzenie_wzdluzne(wezel.lewe_dziecko, wynik)
                    wynik = przechodzenie_wzdluzne(wezel.prawe_dziecko, wynik)
            return wynik
        def przechodzenie_poprzeczne(wezel, wynik):
        #Lewy -> Korzeń -> Prawy
            if wezel:
                if wezel.dane:
                    wynik = przechodzenie_wzdluzne(wezel.lewe_dziecko, wynik)
                    wynik += (str(wezel.dane) + '-')
                    wynik = przechodzenie_wzdluzne(wezel.prawe_dziecko, wynik)
            return wynik
        def przechodzenie_wsteczne(wezel, wynik):
        #Lewy -> Prawy -> Korzeń
            if wezel:
                if wezel.dane:
                    wynik = przechodzenie_wzdluzne(wezel.lewe_dziecko, wynik)
                    wynik = przechodzenie_wzdluzne(wezel.prawe_dziecko, wynik)
                    wynik += (str(wezel.dane) + '-')
            return wynik
        print(przechodzenie_wzdluzne(self.korzen, wynik))
        print(przechodzenie_poprzeczne(self.korzen, wynik))
        print(przechodzenie_wsteczne(self.korzen, wynik))

drzewo = Binarne_Drzewo_Poszukiwan()
for i in range(30):
    drzewo.dodaj(random.randint(0,50))

drzewo.wyswietl()

