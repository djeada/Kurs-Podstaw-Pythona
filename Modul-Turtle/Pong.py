import turtle

def ustawieniaOkna(okno):
    okno.title('Gra Pong')
    okno.setup(width=1000,height=800)
    okno.tracer(0)
    okno.colormode(255)
    okno.bgcolor('green')

class Dlugopis():
    def __init__(self):
        self.zolwik = turtle.Turtle()
        self.zolwik.hideturtle()
        self.zolwik.color('white')
        self.zolwik.shapesize(stretch_wid=10,stretch_len=1)
        self.zolwik.penup()
        self.zolwik.goto(0,350)
        self.zolwik.write('Gracz A: 0 Gracz B: 0', align='Center',font=('Arial',30))

    def wypisz(self, punkty_A, punkty_B):
        self.zolwik.clear()
        self.zolwik.write('Gracz A: {} Gracz B: {}'.format(punkty_A,punkty_B), align='Center',font=('Arial',30))

class Paletka():
    def __init__(self,pozycja):
        self.zolwik = turtle.Turtle()
        self.zolwik.shape('square')
        self.zolwik.color('white')
        self.zolwik.shapesize(stretch_wid=10,stretch_len=1)
        self.zolwik.penup()
        self.zolwik.goto(pozycja,0)

    def gora(self):
        y = self.zolwik.ycor()
        y += 30
        if y < 330:
            self.zolwik.sety(y)

    def dol(self):
        y = self.zolwik.ycor()
        y -= 30
        if y > -330:
            self.zolwik.sety(y)

class Pilka():
    def __init__(self,a,b,dlugopis):
        self.zolwik = turtle.Turtle()
        self.zolwik.shape('circle')
        self.zolwik.color('white')
        self.zolwik.penup()
        self.zolwik.goto(0,0)
        self.dx = 1
        self.dy = 1
        self.a = a
        self.b = b
        self.dlugopis = dlugopis
        self.punkty_A = 0
        self.punkty_B = 0

    def ruch(self):
        self.zolwik.setx(self.zolwik.xcor()+self.dx)
        self.zolwik.sety(self.zolwik.ycor()+self.dy)

    def zderzenia(self):
        #gora i dol
        if self.zolwik.ycor() > 390:
            self.zolwik.sety(390)
            self.dy *= -1

        if self.zolwik.ycor() < -390:
            self.zolwik.sety(-390)
            self.dy *= -1
        
        #lewo i prawo
        if self.zolwik.xcor() > 490:
            self.zolwik.setx(490)
            self.dx *= -1
            self.punkty_A += 1
            self.dlugopis.wypisz(self.punkty_A,self.punkty_B)

        if self.zolwik.xcor() < -490:
            self.zolwik.setx(-490)
            self.dx *= -1
            self.punkty_B += 1
            self.dlugopis.wypisz(self.punkty_A,self.punkty_B)

        #paletki
        if self.zolwik.xcor() < -430 and abs(self.zolwik.ycor() - self.a.zolwik.ycor()) < 50:
            self.zolwik.goto(-420,self.zolwik.ycor())
            self.dx *= -1
            
        if self.zolwik.xcor() > 430 and abs(self.zolwik.ycor() - self.b.zolwik.ycor()) < 50:
            self.zolwik.goto(420,self.zolwik.ycor())
            self.dx *= -1
                                                        
def bind(okno, a, b):
    okno.listen()
    okno.onkeypress(a.gora, 'w')
    okno.onkeypress(a.dol, 's')
    okno.onkeypress(b.gora, 'Up')
    okno.onkeypress(b.dol, 'Down')

def gra(okno):
    a = Paletka(-450)
    b = Paletka(450)
    d = Dlugopis()
    pilka = Pilka(a,b,d)
    bind(okno,a,b)
    while True:
        okno.update()
        pilka.ruch()
        pilka.zderzenia()

def main():
    okno = turtle.Screen()
    ustawieniaOkna(okno)
    gra(okno)
  
main()
