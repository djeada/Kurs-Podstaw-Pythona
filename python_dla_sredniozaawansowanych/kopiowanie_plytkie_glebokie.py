import copy


def przypisanie_refrencja(lista):
    nowa_lista = lista

    # porownanie id
    print(id(nowa_lista) == id(lista))
    print(id(nowa_lista[0]) == id(lista[0]))

    # modyfikujemy oryginalna liste
    lista.append([-1, -2, -3])
    lista[0].insert(1, 1)

    print(nowa_lista)


def przypisanie_wartosci(lista):
    nowa_lista = lista[:]

    # porownanie id
    print(id(nowa_lista) == id(lista))
    print(id(nowa_lista[0]) == id(lista[0]))

    # modyfikujemy oryginalna liste
    lista.append([-1, -2, -3])
    lista[0].insert(1, 1)

    print(nowa_lista)


def kopiowanie_plytkie(lista):
    nowa_lista = copy.copy(lista)

    # porownanie id
    print(id(nowa_lista) == id(lista))
    print(id(nowa_lista[0]) == id(lista[0]))

    # modyfikujemy oryginalna liste
    lista.append([-1, -2, -3])
    lista[0].insert(1, 1)

    print(nowa_lista)


def kopiowanie_glebokie(lista):
    nowa_lista = copy.deepcopy(lista)

    # porownanie id
    print(id(nowa_lista) == id(lista))
    print(id(nowa_lista[0]) == id(lista[0]))

    # modyfikujemy oryginalna liste
    lista.append([-1, -2, -3])
    lista[0].insert(1, 1)

    print(nowa_lista)


print("\nPrzypisanie refrencja")
lista = [[1, 2, 3], [4, 5, 6]]
przypisanie_refrencja(lista)

print("\nPrzypisanie wartosci")
lista = [[1, 2, 3], [4, 5, 6]]
przypisanie_wartosci(lista)

print("\nKopiowanie plytkie")
lista = [[1, 2, 3], [4, 5, 6]]
kopiowanie_plytkie(lista)

print("\nKopiowanie glebokie")
lista = [[1, 2, 3], [4, 5, 6]]
kopiowanie_glebokie(lista)
