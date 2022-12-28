import turtle


def rysuj_luk(zolwik, dlugosc):
    n = int(dlugosc / 2)
    for i in range(n):
        zolwik.forward(dlugosc / n)
        zolwik.left(60 / n)


def rysuj_platek(zolwik, dlugosc):
    rysuj_luk(zolwik, dlugosc)
    zolwik.left(120)
    rysuj_luk(zolwik, dlugosc)


def rysuj_kwiat(zolwik, dlugosc, ilosc):
    for i in range(ilosc):
        rysuj_platek(zolwik, dlugosc)
        zolwik.left(360 / ilosc)


zolwik = turtle.Turtle()
zolwik.speed(0)

rysuj_kwiat(zolwik, 100, 16)

turtle.exitonclick()
