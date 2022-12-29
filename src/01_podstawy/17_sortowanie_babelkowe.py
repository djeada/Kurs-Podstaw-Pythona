"""
Sortowanie babelkowe:

1. Przechodzimy po wszystkich elementach listy.
2. Porownujemy dwa sasiednie elementy.
3. Jesli elementy nie sa posortowane, to zamieniamy je miejscami.
4. Powtarzamy kroki 1-3, n x n razy, gdzie n to liczba elementow w liscie.
"""


def sortowanie_babelkowe(lista):
    for _ in range(len(lista)):
        for j in range(len(lista) - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

    return lista


if __name__ == "__main__":
    print(sortowanie_babelkowe([1, 2, 3, 4, 5]))
    print(sortowanie_babelkowe([5, 4, 3, 2, 1]))
    print(sortowanie_babelkowe([1, 5, 2, 4, 3]))
    print(sortowanie_babelkowe([1, 1, 1, 1, 1]))
