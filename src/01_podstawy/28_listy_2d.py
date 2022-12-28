macierz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(macierz)

print(macierz[0][0])
print(macierz[0][1])

# modyfikacja elementu
macierz[0][0] = 10
print(macierz)

# dodanie rzedu
macierz.append([10, 11, 12])
print(macierz)

# dodanie kolumny
kolumna = [13, 14, 15, 16]
for i in range(len(macierz)):
    macierz[i].append(kolumna[i])

print(macierz)

# usuwanie kolumny
indeks = 1
for i in range(len(macierz)):
    macierz[i].pop(indeks)

print(macierz)

# dodawanie macierzy
macierz_a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
macierz_b = [[10, 11, 12], [13, 14, 15], [16, 17, 18]]
macierz_c = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for i in range(len(macierz_a)):
    for j in range(len(macierz_a[i])):
        macierz_c[i][j] = macierz_a[i][j] + macierz_b[i][j]

print(macierz_c)

# tabliczka mnozenia
tabliczka = [[0 for i in range(10)] for j in range(10)]

for i in range(1, 10):
    for j in range(1, 10):
        tabliczka[i][j] = i * j

for i in range(1, 10):
    for j in range(1, 10):
        print(tabliczka[i][j], end="\t")
    print()
