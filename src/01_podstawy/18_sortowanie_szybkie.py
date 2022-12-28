"""
Sortowanie szybkie (ang. quicksort).

1. Wybieramy element z listy, nazywamy go pivotem.
2. Przechodzimy po wszystkich elementach listy i porownujemy je z pivotem.
3. Elementy mniejsze od pivota przenosimy do lewej czesci listy, a wieksze do prawej.
4. Powtarzamy kroki 1-3 dla lewej i prawej czesci listy, az lista bedzie posortowana.
"""


def sortowanie_szybkie(lista):
    if len(lista) <= 1:
        return lista

    pivot = lista[0]
    mniejsze = [element for element in lista[1:] if element <= pivot]
    wieksze = [element for element in lista[1:] if element > pivot]

    return sortowanie_szybkie(mniejsze) + [pivot] + sortowanie_szybkie(wieksze)


if __name__ == "__main__":
    print(sortowanie_szybkie([1, 2, 3, 4, 5]))
    print(sortowanie_szybkie([5, 4, 3, 2, 1]))
    print(sortowanie_szybkie([1, 5, 2, 4, 3]))
    print(sortowanie_szybkie([1, 1, 1, 1, 1]))
