def zbadajParzystosc(liczba):
    if liczba & 1 == 1:
        return "Liczba {} jest nieparzysta ".format(liczba)
    return "Liczba {} jest parzysta ".format(liczba)


for x in range(1, 11):
    print(zbadajParzystosc(x))
