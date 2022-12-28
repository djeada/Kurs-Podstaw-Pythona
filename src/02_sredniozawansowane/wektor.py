# klasa reprezentujaca wektor 2D (x,y)
import math


class Wektor:
    # inicjalizacja metoda ktora wywolywana jest gdy tworzymy nowy obiekt
    def __init__(tunczyk, x=0.0, y=0.0):
        tunczyk.x = x
        tunczyk.y = y

    # chcemy zeby dla naszych obiektow dzialal +
    def __add__(self, other):
        return Wektor(self.x + other.x, self.y + other.y)

    # chcemy zeby dla naszych obiektow dzialal +=
    def __isadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

    # chcemy zeby dla naszych obiektow dzialal -
    def __sub__(self, other):
        return Wektor(self.x - other.x, self.y - other.y)

    # chcemy zeby dla naszych obiektow dzialal *
    def __mul__(self, other):
        return Wektor(self.x * other.x, self.y * other.y)

    # chcemy zeby dla naszych obiektow dzialal /
    def __div__(self, other):
        return Wektor(self.x / other.x, self.y / other.y)

    # liczymy dlugosc
    def dlugosc(self):
        return int(math.sqrt(self.x ** 2 + self.y ** 2))

    # liczymy kat
    def kat(self):
        return int(math.degrees(math.atan2(self.y, self.x)))

    # wyswietlamy info
    def wyswietl(self):
        return (
            "Wspolrzedna x to "
            + str(self.x)
            + " Wspolrzedna y to "
            + str(self.y)
            + " Dlugosc wektora to "
            + str(self.dlugosc())
            + " Kat wektora to "
            + str(self.kat())
        )


wektor1 = Wektor(6, 2)
wektor2 = Wektor(4, 8)
wektor3 = wektor1 + wektor2
wektor3 += wektor2
wektor4 = wektor1 * wektor2

print("Wektor1: ", wektor1.wyswietl())
print("Wektor2: ", wektor2.wyswietl())
print("Wektor3: ", wektor3.wyswietl())
print("Wektor4: ", wektor4.wyswietl())
