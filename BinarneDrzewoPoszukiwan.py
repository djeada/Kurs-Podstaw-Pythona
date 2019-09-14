class Wezel():
    def __init__(self, dane=None):
        self.dane = dane
        self.lewe_dziecko = None
        self.prawe_dziecko = None
        
class BST():
    def __init__(self):
        self.korzen = Wezel()

    def dodaj(self, dane):
        if self.korzen.dane == None:
            self.korzen.dane = dane
        else:
            def dodaj_do_wierzcholka(dane, wierzcholek):
                if dane < wierzcholek.dane:
                    if wierzcholek.lewe_dziecko == None:
                        wierzcholek.lewe_dziecko = Wezel(dane)
                    else:
                        dodaj_do_wierzcholka(dane, wierzcholek.lewe_dziecko)
                if dane > wierzcholek.dane:
                    if wierzcholek.prawe_dziecko == None:
                        wierzcholek.prawe_dziecko = Wezel(dane)
                    else:
                        dodaj_do_wierzcholka(dane, wierzcholek.prawe_dziecko)
            dodaj_do_wierzcholka(dane, self.korzen)

    def wyswietl(self):
        wynik = ''
        def przechodzenie_wzdluzne(wynik, wierzcholek):
            #Korzen -> Lewy -> Prawy
            if wierzcholek:
                if wierzcholek.dane:
                    wynik += (str(wierzcholek.dane) + '-')
                    wynik = przechodzenie_wzdluzne(wynik, wierzcholek.lewe_dziecko)
                    wynik = przechodzenie_wzdluzne(wynik, wierzcholek.prawe_dziecko)
            return wynik
        def przechodzenie_poprzeczne(wynik, wierzcholek):
            # Lewy -> Korzen -> Prawy
            if wierzcholek:
                if wierzcholek.dane:
                    wynik = przechodzenie_poprzeczne(wynik, wierzcholek.lewe_dziecko)
                    wynik += (str(wierzcholek.dane) + '-')
                    wynik = przechodzenie_poprzeczne(wynik, wierzcholek.prawe_dziecko)
            return wynik
        def przechodzenie_wsteczne(wynik, wierzcholek):
            # Lewy -> Prawy -> Korzen
            if wierzcholek:
                if wierzcholek.dane:
                    wynik = przechodzenie_wsteczne(wynik, wierzcholek.lewe_dziecko)
                    wynik = przechodzenie_wsteczne(wynik, wierzcholek.prawe_dziecko)
                    wynik += (str(wierzcholek.dane) + '-')
            return wynik
        print(przechodzenie_wzdluzne(wynik, self.korzen))
        print(przechodzenie_poprzeczne(wynik, self.korzen))
        print(przechodzenie_wsteczne(wynik, self.korzen))


drzewo = BST()
drzewo.dodaj(3)
drzewo.dodaj(2)
drzewo.dodaj(1)
drzewo.dodaj(7)
drzewo.dodaj(8)
drzewo.dodaj(99)
drzewo.wyswietl()
