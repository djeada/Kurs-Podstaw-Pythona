# kilka przykladow z petla for
# petla for - iteruje po sekwencji

# iteracja po liczbach naturalnych
for i in range(10):
    print(i)

# krok rowny 3
for i in range(3, 30, 3):
    print(i)

# iteracja od konca
for i in range(10, 0, -1):
    print(i)


# iteracja po elementach listy
lista = [-2, 3, 0, 9, 1]
for element in lista:
    print(element)

# iteracja po elementach listy i indeksach
for i, element in enumerate(lista):
    print(i, element)

# iteracja po znakach napisu
napis = "Ala ma kota"
for znak in napis:
    print(znak)
