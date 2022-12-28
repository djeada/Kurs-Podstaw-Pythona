"""
Sortowanie przez wybieranie

1. Przechodzimy po wszystkich elementach listy.
2. Szukamy najmniejszego elementu.
3. Zamieniamy go z pierwszym elementem.
4. Powtarzamy kroki 1-3, n razy, gdzie n to liczba elementow w liscie.
"""


def znajdz_najmniejszy(lista):
    najmniejszy = lista[0]
    najmniejszy_index = 0
    for i in range(1, len(lista)):
        if lista[i] < najmniejszy:
            najmniejszy = lista[i]
            najmniejszy_index = i

    return najmniejszy_index


def sortowanie_przez_wybieranie(lista):
    nowa_lista = []
    for _ in range(len(lista)):
        najmniejszy = znajdz_najmniejszy(lista)
        nowa_lista.append(lista.pop(najmniejszy))

    return nowa_lista


if __name__ == "__main__":
    print(sortowanie_przez_wybieranie([1, 2, 3, 4, 5]))
    print(sortowanie_przez_wybieranie([5, 4, 3, 2, 1]))
    print(sortowanie_przez_wybieranie([1, 5, 2, 4, 3]))
    print(sortowanie_przez_wybieranie([1, 1, 1, 1, 1]))
