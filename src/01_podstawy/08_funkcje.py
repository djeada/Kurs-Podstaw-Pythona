def powitanie():
    print("Powitanie")


def powitanie_z_imieniem(imie):
    print("Witaj " + imie)


def powitanie_dla_krola(imie):
    if imie == "Jan":
        print("Witaj Królu")
    else:
        print("Witaj " + imie)


def suma(a, b):
    return a + b


def maks_dwoch(a, b):
    if a > b:
        return a
    else:
        return b


def maks_trzech(a, b, c):
    return maks_dwoch(a, maks_dwoch(b, c))


def sortuj_trzy(a, b, c):
    if a > b:
        a, b = b, a
    if b > c:
        b, c = c, b
    if a > b:
        a, b = b, a
    return a, b, c


if __name__ == "__main__":
    powitanie()
    powitanie_z_imieniem("Jan")
    powitanie_dla_krola("Jan")
    powitanie_dla_krola("Adam")

    print(suma(1, 2))
    print(suma(3, 4))

    print(maks_dwoch(1, 2))
    print(maks_dwoch(3, 4))

    print(maks_trzech(1, 2, 3))
    print(maks_trzech(3, 4, 5))

    print(sortuj_trzy(1, 2, 3))
    print(sortuj_trzy(1, 3, 2))
    print(sortuj_trzy(2, 1, 3))
    print(sortuj_trzy(2, 3, 1))
    print(sortuj_trzy(3, 1, 2))
    print(sortuj_trzy(3, 2, 1))
