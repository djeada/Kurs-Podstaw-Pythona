import math


class A:
    def __init__(self):
        self.a = None
        self.b = None


class Punkt:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def przesun(self, dx, dy):
        self.x += dx
        self.y += dy


def odleglosc(punkt1, punkt2):
    return math.sqrt((punkt1.x - punkt2.x) ** 2 + (punkt1.y - punkt2.y) ** 2)


if __name__ == "__main__":
    a = A()
    print(a)
    print(a.a, a.b)
    print(id(a), id(a.a), id(a.b))

    a.a = 1
    a.b = 2

    print(a)
    print(a.a, a.b)
    print(id(a), id(a.a), id(a.b))

    p1 = Punkt(1, 2)
    p2 = Punkt(3, 4)

    print(p1.x, p1.y)
    print(p2.x, p2.y)

    print(f"Odleglosc miedzy punktami: {odleglosc(p1, p2)}")

    p1.przesun(1, 1)

    print(p1.x, p1.y)
    print(p2.x, p2.y)

    print(f"Odleglosc miedzy punktami: {odleglosc(p1, p2)}")
