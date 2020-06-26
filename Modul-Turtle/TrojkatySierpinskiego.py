import turtle
import random

def przesuniecie(zolwik, x, y):
    zolwik.up()
    zolwik.goto(x,y)
    zolwik.down()

def rysuj_trojkat(zolwik, punkty, kolor):
    przesuniecie(zolwik,punkty[0][0],punkty[0][1])
    zolwik.fillcolor(kolor)
    zolwik.begin_fill()
    zolwik.goto(punkty[1][0],punkty[1][1])
    zolwik.goto(punkty[2][0],punkty[2][1])
    zolwik.goto(punkty[0][0],punkty[0][1])
    zolwik.end_fill()

def wyznacz_srodek(p1,p2):
    return ((p1[0]+p2[0])/2,(p1[1]+p2[1])/2)

def sierpinski(zolwik, punkty, stopnie):
    lista_kolorow = ['red', 'violet', 'green', 'blue', 'grey', 'orange', 'yellow']
    rysuj_trojkat(zolwik, punkty, lista_kolorow[random.randint(0,len(lista_kolorow)-1)])
    if stopnie > 0:
        sierpinski(zolwik, (punkty[0],wyznacz_srodek(punkty[0],punkty[1]),wyznacz_srodek(punkty[0],punkty[2])),stopnie-1)
        sierpinski(zolwik, (punkty[1],wyznacz_srodek(punkty[0],punkty[1]),wyznacz_srodek(punkty[1],punkty[2])),stopnie-1)
        sierpinski(zolwik, (punkty[2],wyznacz_srodek(punkty[2],punkty[1]),wyznacz_srodek(punkty[0],punkty[2])),stopnie-1)

zolwik = turtle.Turtle()
zolwik.speed(0)

lista_punktow = [[-200,-100],[0,200],[200,-100]]

sierpinski(zolwik,lista_punktow,3)

turtle.exitonclick()
