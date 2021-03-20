def potega(a):
    return a ** 2


# przypisanie funkcji do nazwy
g = potega

print(g(2))
print(potega(2))

# mozemy przekazac funkcje jako parametr do innej funkcji
def wyswietlObliczenia(funkcja, lista):
    for x in lista:
        print(funkcja(x))


def zwieksz2(a):
    return a + 2


lista = [1, 3, 5]

wyswietlObliczenia(g, lista)
wyswietlObliczenia(zwieksz2, lista)

# mozemy zwracac funkcje
def zwiekszLiczba(a):
    def zwieksz(liczba):
        print("a to: ", a)
        print("liczba to: ", liczba)
        return a + liczba

    return zwieksz


g = zwiekszLiczba(8)
print(g(4))
print(zwiekszLiczba(9)(7))

# mozemy umieszczac funkcje w strukturach danych
listaFunkcji = [potega, zwieksz2]

for funkcja in listaFunkcji:
    for x in lista:
        print(funkcja(x))
