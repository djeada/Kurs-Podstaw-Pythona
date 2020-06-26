#klasa to nasz typ danych
#atrybuty to sa konkretne dane
#metody to sa funkcje zdefiniowane w obrebie klasy
#za pomoca self metoda wchodzi w interakcje z aktualna instacja klasy

class osoba:
    def __init__(self, imie='Adam', wiek=0, zarobki=100.50):
        self.imie = imie
        self.wiek = wiek
        self.zarobki = zarobki

    def przywitanie(self):
        print('Jestem ', self.imie, ' i mam ', self.wiek, ' lat.')

ja = osoba('Adam',33, 41.5)
James = osoba('James',23,4000.89)
Tunczyk = osoba()

Tunczyk.przywitanie()
ja.przywitanie()
James.przywitanie()

print(ja.imie)
print(ja.wiek)
print(ja.zarobki)

print(James.imie)
print(James.wiek)
print(James.zarobki)
