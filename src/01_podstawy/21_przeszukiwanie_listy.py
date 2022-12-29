"""
Wyszukiwanie liniowe

1. Przechodzimy po wszystkich elementach listy
2. Porownujemy element z szukanym elementem
3. Jesli elementy sa takie same, to zwracamy indeks elementu
4. Jesli nie znalezlismy elementu, to zwracamy -1

Wyszukiwanie binarne

1. Wybieramy element z srodka listy
2. Porownujemy element z szukanym elementem
3. Jesli elementy sa takie same, to zwracamy indeks elementu
4. Jesli element jest wiekszy, to szukamy w lewej czesci listy
5. Jesli element jest mniejszy, to szukamy w prawej czesci listy
"""


def wyszukiwanie_liniowe(lista, element):
    for i in range(len(lista)):
        if lista[i] == element:
            return i
    return -1


def wyszukiwanie_binarne(lista, element):
    lewy = 0
    prawy = len(lista) - 1

    while lewy <= prawy:
        srodek = (lewy + prawy) // 2

        if lista[srodek] == element:
            return srodek
        elif lista[srodek] < element:
            lewy = srodek + 1
        else:
            prawy = srodek - 1

    return -1


if __name__ == "__main__":
    lista = [1, 2, 3, 4, 5]
    klucz = 3
    print(wyszukiwanie_liniowe(lista, klucz))
    print(wyszukiwanie_binarne(lista, klucz))

    klucz = 6
    print(wyszukiwanie_liniowe(lista, klucz))
    print(wyszukiwanie_binarne(lista, klucz))
