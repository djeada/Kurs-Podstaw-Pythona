import random
from time import sleep

class Wojownik():
    def __init__(self, imie="anonim", zycie=0, pAtaku=0,pObrony=0):
        self.imie = imie
        self.zycie = zycie
        self.pAtaku = pAtaku
        self.pObrony = pObrony

    def atak(self):
        return random.randint(0, self.pAtaku) 
 
    def obrona(self):
        return random.randint(0, self.pObrony)

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

def walka(rycerz, malpa):

    i = 1
    
    while(rycerz.czyZywy() and malpa.czyZywy()):

        print('Runda nr: ', i)
        wyswietlStaty(rycerz,malpa)
        
        if random.randint(0,1) == 0:
            pojedynek(malpa,rycerz)
        else:
            pojedynek(rycerz,malpa)

        print('')
        sleep(3)
        i+=1

    if rycerz.czyZywy():
        print('Rycerz zwyciezyl walke')
    else:
        print('Malpa zwyciezyl walke')
        
def pojedynek(x,y):
    print(x, ' zostal zaatakowany  przez ', y)
    ilosc = y.atak() - x.obrona()
    print(x, ' stracil ', ilosc, ' punktow zycia. ')
    x.straconeZycie(ilosc)

def wyswietlStaty(x,y):
    for i in (x,y):
        print(i, 'ma ', i.zycie, 'punktow zycia.')

rycerz = Wojownik('Rycerz',random.randint(30,100),random.randint(5,30),random.randint(5,15))
malpa = Wojownik('Malpi Wojownik',random.randint(30,100),random.randint(5,30),random.randint(5,15))

walka(rycerz,malpa)


