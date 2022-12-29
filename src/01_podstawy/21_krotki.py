# Krotki sa podobne do list, ale nie mozna ich modyfikowac

krotka = (1, 2, 3, 4, 5)
print(krotka)

# krotka[0] = 10 # TypeError: 'tuple' object does not support item assignment

# Krotki sa szybsze od list
from timeit import timeit

print(
    timeit("krotka = (1, 2, 3, 4, 5)", number=1000000)
)  # timeit zwraca czas w sekundach
print(timeit("lista = [1, 2, 3, 4, 5]", number=1000000))

# Krotki sa uzyteczne do zwracania wielu wartosci z funkcji
def funkcja():
    return 1, 2, 3


print(funkcja())
print(type(funkcja()))

# Krotki mozna rozpakowywac
a, b, c = funkcja()

print(a)
print(b)
print(c)

# Krotki mozna laczyc
krotka1 = (1, 2, 3)
krotka2 = (4, 5, 6)

print(krotka1 + krotka2)

# Krotki mozna mnozyc
print(krotka1 * 3)

# Krotki mozna indeksowac
print(krotka1[0])
print(krotka1[-1])
print(krotka1[1:3])
print(krotka1[1:])

# sprawdzanie czy element jest w krotce
print(1 in krotka1)

# dlugosc krotki
print(len(krotka1))

# zliczanie wystapien elementu w krotce
print((1, 1, 2, 1).count(1))
