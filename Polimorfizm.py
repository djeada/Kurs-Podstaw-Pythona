#polimorifzm pozwala w różnych klasach implementować metody
#o tej samej nazwie

class Ksztalt:
    def __init__(self, nazwa='Ksztalt'):
        self.nazwa = nazwa

    def pole(self):
        print('Brak danych')

class Trojkat(Ksztalt):
    def __init__(self, nazwa='Trojkat', wysokosc=2, podstawa=2):
        super().__init__(nazwa)
        self.wysokosc = wysokosc
        self.podstawa = podstawa

    def pole(self):
        print(int(self.wysokosc*self.podstawa/2))

class Prostokat(Ksztalt):
    def __init__(self, nazwa='Prostokat', a=2, b=2):
        super().__init__(nazwa)
        self.a = a
        self.b = b

    def pole(self):
        print(int(self.a*self.b))

class Kwadrat():
    def __init__(self, nazwa='Kwadarat', a=5):
        self.nazwa = nazwa
        self.a = a

    def pole(self):
        print(int(self.a**2))

ksztalt = Ksztalt()
trojkat = Trojkat(3,4)
prostokat = Prostokat(2,5)
kwadrat = Kwadrat(8)

for x in (ksztalt, trojkat, prostokat, kwadrat):
    x.pole()



        

    
    
