import turtle


def kwadrat(nazwa, dlugosc):
    for i in range(4):
        nazwa.pensize(i * 5)
        nazwa.forward(dlugosc)
        nazwa.left(90)


def skomplikowany(nazwa):
    for i in range(300):
        nazwa.forward(i)
        nazwa.right(88)


zolwik = turtle.Turtle()
zolwik.speed(1)
zolwik.pencolor("blue")
# rysujemy kwadrat
kwadrat(zolwik, 100)
kwadrat(zolwik, 200)

# rysujemy inny ksztalt
skomplikowany(zolwik)

turtle.exitonclick()
