import random
from time import sleep

class Wojownik():
    def __init__(self,imie='anonim',zycie=0,pAtaku=0,pObrony=0):
        self.imie = imie
        self.zycie = zycie
        self.pAtaku = pAtaku
        self.pObrony = pObrony

    def atak(self):
        return random.randint(0,self.pAtaku)*random.randint(2,5)

    def obrona(self):
        return random.randint(0,self.pObrony)

    def straconeZycie(self,ilosc):
        self.zycie -= ilosc
        if self.zycie <= 0:
            print(self.imie, ' polegl w walce')

    def czyZywy(self):
        if self.zycie <= 0:
            return False
        else:
            return True

    def __str__(self):
        return self.imie

def walka(malpa,rycerz):

    i = 1
    while(malpa.czyZywy() and rycerz.czyZywy()):
        print('Runda nr: ', i)
        wyswietlStaty(malpa,rycerz)

        if random.randint(0,1) == 0:
            pojedynek(malpa,rycerz)
        else:
            pojedynek(rycerz,malpa)

        print('')
        sleep(5)
        i+=1

    if rycerz.czyZywy():
        print('Rycerz zwyciezyl walke')
    else:
        print('Malpi wojwnik zwyciezyl walke')

def pojedynek(x,y):
    print(x, ' zostal zaatakowany prze ', y)
    obrazenia = y.atak() - x.obrona()
    print(x, ' stracil ', obrazenia, ' punktow zycia.')
    x.straconeZycie(obrazenia)


def wyswietlStaty(x,y):
    for i in (x,y):
        print(i, ' ma ', i.zycie, ' punktow zycia.')

rycerz = Wojownik('Rycerz',random.randint(100,1000), random.randint(10,50),random.randint(5,30))
malpa = Wojownik('Malpi Wojownik',random.randint(100,1000), random.randint(10,50),random.randint(5,30))

walka(malpa,rycerz)
            



          
