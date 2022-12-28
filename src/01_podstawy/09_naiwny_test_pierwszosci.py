# liczby pierwsze: 2, 3, 5, 7
# liczby złożone: 4, 6, 8, 9, 10
# test pierwszosci:
# 1. sprawdzamy czy liczba jest podzielna przez liczby od 2 do liczba-1
# 2. jesli tak, to liczba jest zlozona
# 3. jesli nie, to liczba jest pierwsza


def czy_pierwsza(liczba):

    if liczba < 2:
        return False

    for i in range(2, liczba):
        if liczba % i == 0:
            return False
    return True


for i in range(10):
    if czy_pierwsza(i):
        print(i, "jest pierwsza")
    else:
        print(i, "jest zlozona")
