import math
import turtle

def draw_arc(b,circumfrence):
    n=int(circumfrence/2) 
    l=circumfrence/n
    for i in range(n):
        b.fd(l)
        b.lt(60/n)

def draw_petal(b,r):
    draw_arc(b,r)
    b.lt(120)
    draw_arc(b,r)

def narysuj_kwiatek(t, dlugosc, ilosc):
    for i in range(ilosc):
        draw_petal(t,dlugosc)
        t.left(int(180/ilosc))

bob=turtle.Turtle()
bob.speed(0)

narysuj_kwiatek(bob,radius,8)

turtle.exitonclick()
