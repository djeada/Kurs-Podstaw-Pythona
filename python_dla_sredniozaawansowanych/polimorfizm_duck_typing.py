'''
Rozpoznawanie typu obiektu nie na podstawie deklaracji, ale przez badanie metod udostępnionych przez obiekt.
'''

class Kaczka:
  def kwacz(self):
    print("Kuaaaaaak!")

class Czlowiek:
  def kwacz(self):
    print("Czlowiek ktory kwacze")

def foo(obiekt):
  obiekt.kwacz()

ornitolog = Czlowiek()
daisy = Kaczka()

for obiekt in (ornitolog, daisy):
  foo(obiekt)
