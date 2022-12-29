def celsjusz_na_fahrenheit(temp):
    return (temp * 9 / 5) + 32


def fahrenheit_na_celsjusz(temp):
    return (temp - 32) * 5 / 9


def float_z_precyzja(wartosc, precyzja=2, jednostka="C"):
    return f"{wartosc:.{precyzja}f} {jednostka}"


if __name__ == "__main__":
    liczby = (3, 2, 4, 5, 8, 23, 42, 34, 81, 7, 4)
    napis = "jakisNaPIS"

    nieparzyste = list(filter(lambda x: x % 2 == 1, liczby))
    print(nieparzyste)

    male_litery = list(filter(lambda x: x.islower(), napis))
    print("".join(male_litery))

    stopnie = list(map(fahrenheit_na_celsjusz, nieparzyste))
    stopnie = list(map(float_z_precyzja, stopnie))
    print(stopnie)
