import math


class Wektor2D:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def modul(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __add__(self, other):
        return Wektor2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Wektor2D(self.x - other.x, self.y - other.y)

    def __str__(self):
        return f"Wektor2D({self.x}, {self.y})"

    def __repr__(self):
        return self.__str__()


def iloczyn_skalarny(wektor1, wektor2):
    return wektor1.x * wektor2.x + wektor1.y * wektor2.y


def kat(wektor1, wektor2):
    return math.acos(
        iloczyn_skalarny(wektor1, wektor2) / (wektor1.modul() * wektor2.modul())
    )


if __name__ == "__main__":
    w1 = Wektor2D(1, 2)
    w2 = Wektor2D(3, 4)

    print(w1)
    print(w2)

    print(f"Modul wektora1: {w1.modul()}")
    print(f"Modul wektora2: {w2.modul()}")

    print(f"Wektor1 + Wektor2: {w1 + w2}")
    print(f"Wektor1 - Wektor2: {w1 - w2}")

    print(f"Iloczyn skalarny wektor1 i wektor2: {iloczyn_skalarny(w1, w2)}")
    print(f"Kat pomiedzy wektor1 i wektor2: {kat(w1, w2)}")
