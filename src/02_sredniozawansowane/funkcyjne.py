def celsisus_na_fahrenheit(temp):
    return (temp * 9/5) + 32


def fahrenheit_na_celsisus(temp):
    return (temp-32) * 5/9


def ograniczony_float(wartosc, precyzja=2):
    return f'{wartosc:.{precyzja}f}'

def main():
    liczby = (3, 2,4,5,8,23,42,34,81,7,4)
    napis = "jakisNaPIS"

    nieparzyste = list(filter(lambda x: x % 2 == 1, liczby))
    print(nieparzyste)

    male_litery = list(filter(lambda x: x.islower(), napis))
    print(''.join(male_litery))

    celsius = list(map(fahrenheit_na_celsisus, nieparzyste))
    celsius_z_formatowaniem = list(map(ograniczony_float, celsius))
    print(celsius_z_formatowaniem)

if __name__ == "__main__":
    main()