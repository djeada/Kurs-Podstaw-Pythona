"""
Bogo sort

1. Losujemy permutacje elementow listy.
2. Sprawdzamy, czy lista jest posortowana.
3. Jesli nie, to wracamy do kroku 1.
"""

import random


def czy_posortowana(lista):
    for i in range(len(lista) - 1):
        if lista[i] > lista[i + 1]:
            return False
    return True


def bogo_sort(lista):
    while not czy_posortowana(lista):
        random.shuffle(lista)
    return lista


if __name__ == "__main__":
    print(bogo_sort([1, 2, 3, 4, 5]))
    print(bogo_sort([5, 4, 3, 2, 1]))
    print(bogo_sort([1, 5, 2, 4, 3]))
    print(bogo_sort([1, 1, 1, 1, 1]))
