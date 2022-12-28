liczba = 10
print(liczba)

liczba = 20  # przypisanie nowej wartosci do zmiennej
print(liczba)

wynik = liczba + 10  # operacja na zmiennych
print(wynik)

zmiennoprzecinkowa = 10.5
napis = "Ala ma kota"

# typy danych
print(type(liczba))
print(type(zmiennoprzecinkowa))
print(type(napis))

# nie wszystkie operacje sa mozliwe na wszystkich typach danych
wynik = liczba + zmiennoprzecinkowa
print(wynik)
print(type(wynik))
# wynik = liczba + napis # blad


# operacje na napisach
print(napis + " i psa")
print(napis * 3)
# print(napis / 2) # blad

# nadpisanie zmiennej
a = 5
b = a
b = 10

print(a)
print(b)

print(id(a))
print(id(b))

# podmien wartosci zmiennych
a = 3
b = 9

print(a, b)
print(id(a))
print(id(b))

a, b = b, a

print(a, b)
print(id(a))
print(id(b))
