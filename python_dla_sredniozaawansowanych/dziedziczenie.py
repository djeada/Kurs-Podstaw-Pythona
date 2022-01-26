# dziedziczenie polega na dzieleniu sie cechami miedzy klasami
# dziedziczymy z nad-klasy do pod-klasy


class Ryba:
    def __init__(self, imie="Nemo", wiek=0):
        self.imie = imie
        self.wiek = wiek

    def wyswietl(self):
        print("Jestem ", self.imie, " i mam ", self.wiek, " lat.")


class Tunczyk(Ryba):
    def __init__(self, imie, wiek):
        super().__init__(imie, wiek)

    def wyswietl(self):
        super().wyswietl()
        print("A w dodatku jestem fajnym tunczykiem.")

    def pozegnanie(self):
        print(self.imie, " was zegna")


james = Ryba("James", 100)
george = Tunczyk("George", 34)

james.wyswietl()
george.wyswietl()
# james.pozegnanie()
george.pozegnanie()

print(type(james))
print(type(george))

print("czy james jest ryba? ", str(isinstance(james, Ryba)))
print("czy james jest tunczykiem? ", str(isinstance(james, Tunczyk)))
print("czy george jest ryba? ", str(isinstance(george, Ryba)))
print("czy george jest tunczykiem? ", str(isinstance(george, Tunczyk)))
