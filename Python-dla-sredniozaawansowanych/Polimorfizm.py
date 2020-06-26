#polimorfizm umozliwia uzycie metod tej samej nazwy w roznych klasach

class Ksztalt:
    def __init__(self, nazwa='Ksztalt'):
        self.nazwa = nazwa

    def pole(self):
        print('Brak danych na temat ', self.nazwa)

class Trojkat(Ksztalt):
    def __init__(self, nazwa='Trojkat', a=2, h=2):
        super().__init__(nazwa)
        self.a = a
        self.h = h

    def pole(self):
        print('Pole figury ', self.nazwa)
        print(self.a*self.h/2)

class Prostokat(Ksztalt):
    def __init__(self, nazwa='Prostokat', a=2, b=2):
        super().__init__(nazwa)
        self.a = a
        self.b = b

    def pole(self):
        print('Pole figury ', self.nazwa)
        print(self.a*self.b)

class Kwadrat():
    def __init__(self, nazwa='Kwadrat', a=3):
        self.nazwa = nazwa
        self.a = a

    def pole(self):
        print('Pole figury ', self.nazwa)
        print(self.a**2)

def wyswietl_pole(lista):
    for x in lista:
        x.pole()

ksztalt = Ksztalt()
trojkat = Trojkat()
prostokat = Prostokat()
kwadrat = Kwadrat()
'''
for x in (ksztalt, trojkat, prostokat, kwadrat):
    print(type(x))
    x.pole()
'''
lista = [ksztalt, trojkat, prostokat, kwadrat]
wyswietl_pole(lista)

    


    
