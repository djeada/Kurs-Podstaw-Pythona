import random

# liczba losowa zmiennoprzecinkowa z przedzialu [0, 1)
print("Liczba losowa z przedzialu [0, 1)")
print(random.random())
print()

# liczba losowa zmiennoprzecinkowa z przedzialu [0, 10)
print("Liczba losowa z przedzialu [0, 10)")
print(random.random() * 10)
print()

# liczba losowa zmiennoprzecinkowa z przedzialu [5, 25)
print("Liczba losowa z przedzialu [5, 25)")
print(random.random() * 20 + 5)
print()

# liczba calkowita z przedzialu [0, 10)
print("Liczba calkowita z przedzialu [0, 10)")
print(random.randint(0, 10))
print()

# liczba calkowita z przedzialu [5, 25)
print("Liczba calkowita z przedzialu [5, 25)")
print(random.randint(5, 25))
print()

# losowanie elementu z listy
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Losowanie elementu z listy", lista)
print(random.choice(lista))
print()

# losowanie elementu z napisu
napis = "Ala ma kota"
print("Losowanie elementu z napisu", napis)
print(random.choice(napis))
print()

# losowanie z rozkladu normalnego miedzy -5 a 5
def rozklad_normalny_z_przedzialu(minimum, maksimum):
    mediana = (minimum + maksimum) / 2
    odchylenie = (maksimum - minimum) / 6
    return random.gauss(mediana, odchylenie)


print("Losowanie z rozkladu normalnego miedzy -5 a 5")
for i in range(10):
    print(rozklad_normalny_z_przedzialu(-5, 5))
print()
