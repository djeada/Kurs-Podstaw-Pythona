# Pong przy uzyciu grafiki zolwia
# Autor: Adam Djellouli

import turtle
import winsound
import time
import random
import os

def random_color():
    rgbl=[random.randint(0,255),random.randint(0,255),random.randint(0,255)]
    return tuple(rgbl)

def setup(okno):
    okno.title("Pong")
    okno.setup(width=1000, height=800)
    okno.tracer(0)
    okno.colormode(255)
    okno.bgcolor(random_color())

class Paletka():
    def __init__(self, pozycja):
        self.p = turtle.Turtle()
        self.p.speed(1)
        self.p.shape("square")
        self.p.color("white")
        self.p.shapesize(stretch_wid=10,stretch_len=1)
        self.p.penup()
        self.p.goto(pozycja, 0)

    def gora(self):
        y = self.p.ycor()
        y += 30
        if y < 330:
            self.p.sety(y)

    def dol(self):
        y = self.p.ycor()
        y -= 30
        if y > -330:
            self.p.sety(y)

class Dlugopis():
    def __init__(self):
        self.p = turtle.Turtle()
        self.p.speed(3)
        self.p.shape("square")
        self.p.color("white")
        self.p.penup()
        self.p.hideturtle()
        self.p.goto(0, 350)
        self.p.write("Gracz A: 0  Gracz B: 0", align="center", font=("Arial", 30))

    def wypisz(self, punkty_a, punkty_b):
        self.p.clear()
        self.p.write("Gracz A: {}  Gracz B: {}".format(punkty_a, punkty_b), align="center", font=("Arial", 30))

class Pilka():
    def __init__(self, dlugopis, a, b):
        self.p = turtle.Turtle()
        self.p.shape("circle")
        self.p.color("white")
        self.p.penup()
        self.p.goto(0, 0)
        self.p.dx = 1
        self.p.dy = 1
        self.dlugopis = dlugopis
        self.punkty_a = 0
        self.punkty_b = 0
        self.a = a
        self.b = b

    def ruch(self):
        self.p.setx(self.p.xcor() + self.p.dx)
        self.p.sety(self.p.ycor() + self.p.dy)

    def zderzenia(self):
        #gora i dol
        if self.p.ycor() > 390:
            self.p.sety(390)
            self.p.dy *= -1
    
        elif self.p.ycor() < -390:
            self.p.sety(-390)
            self.p.dy *= -1

        #prawo i lewo
        if self.p.xcor() > 480:
            self.punkty_a += 1
            self.dlugopis.wypisz(self.punkty_a, self.punkty_b)   
            self.p.dx *= -1

        elif self.p.xcor() < -490:
            self.punkty_b += 1
            self.dlugopis.wypisz(self.punkty_a, self.punkty_b)   
            self.p.dx *= -1

        #paletki
        if self.p.xcor() < -430 and self.p.ycor() < self.a.p.ycor() + 50 and self.p.ycor() > self.a.p.ycor() - 50:
            self.p.goto(-425, self.p.ycor())
            self.p.dx *= -1
            self.p.color(random_color())
            self.p.dx += 1
            self.p.dy += 1
            winsound.PlaySound('dzwiek.wav', winsound.SND_ASYNC)


    
        elif self.p.xcor() > 420 and self.p.ycor() < self.b.p.ycor() + 50 and self.p.ycor() > self.b.p.ycor() - 50:
            self.p.goto(420, self.p.ycor())
            self.p.dx *= -1
            self.p.color(random_color())
            self.p.dx += 1
            self.p.dy += 1
            winsound.PlaySound('dzwiek.wav', winsound.SND_ASYNC)

def bind(okno, a, b):
    okno.listen()
    okno.onkeypress(a.gora, 'w')
    okno.onkeypress(a.dol, 's')
    okno.onkeypress(b.gora, 'Up')
    okno.onkeypress(b.dol, 'Down')

def gra(okno):
    a = Paletka(-450)
    b = Paletka(450)
    dlugopis = Dlugopis()
    pilka = Pilka(dlugopis,a,b)
    bind(okno,a,b)
    while True:
        time.sleep(0.002)
        okno.update()
        pilka.ruch()
        pilka.zderzenia()

def main():
    okno = turtle.Screen()
    setup(okno)
    gra(okno)

main()
