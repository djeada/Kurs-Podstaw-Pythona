class Tunczyk:
    #tworzymy zmienna statyczna
    ilosc_tunczykow = 0

    def __init__(self, imie):
        self.imie = imie
        Tunczyk.ilosc_tunczykow += 1

    #twirzymy metode statyczna
    @staticmethod
    def getIloscTunczykow():
        print('Aktualna liczba tunczykow to ', Tunczyk.ilosc_tunczykow)

    #nadpisujemy destruktor
    def __del__(self):
        print('Tunczyk ', self.imie, ' zostal usuniety.')
        Tunczyk.ilosc_tunczykow -= 1

Tunczyk.getIloscTunczykow()

tunczyk1 = Tunczyk('James')

Tunczyk.getIloscTunczykow()

tunczyk2 = Tunczyk('Greg')

Tunczyk.getIloscTunczykow()

del tunczyk2

#print(tunczyk2.name)

Tunczyk.getIloscTunczykow()


