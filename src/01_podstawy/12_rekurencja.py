def suma_petla(lista):
    suma = 0
    for element in lista:
        suma += element
    return suma


def suma_rekurencja(lista):
    if len(lista) == 0:
        return 0
    return lista[0] + suma_rekurencja(lista[1:])


def silnia_petla(n):
    silnia = 1
    for i in range(1, n + 1):
        silnia *= i
    return silnia


def silnia_rekurencja(n):
    if n == 0:
        return 1
    return n * silnia_rekurencja(n - 1)


def fibonacci_petla(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a


def fibonacci_rekurencja(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_rekurencja(n - 1) + fibonacci_rekurencja(n - 2)


if __name__ == "__main__":
    lista = [1, 2, 3, 4, 5]
    print("Suma elementow listy: ", lista)
    print(suma_petla(lista))
    print(suma_rekurencja(lista))
    print()

    print("Silnia z 5")
    print(silnia_petla(5))
    print(silnia_rekurencja(5))
    print()

    print("10 element ciagu Fibonacciego")
    print(fibonacci_petla(10))
    print(fibonacci_rekurencja(10))
    print()
