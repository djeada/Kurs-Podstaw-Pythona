"""
Szyfr Cezara

1. Pobierz napis i przesuniecie.
2. Przejdz przez wszystkie znaki napisu.
3. Sprawdz czy znak jest litera.
4. Jesli tak, to przesun go zgodnie z przesunieciem.
5. Wypisz zaszyfrowany napis.
"""


def szyfruj(napis, przesuniecie):
    szyfrogram = ""
    for znak in napis:
        if znak.isalpha():
            num = ord(znak)
            num += przesuniecie

            if znak.isupper():
                if num > ord("Z"):
                    num -= 26
                elif num < ord("A"):
                    num += 26
            elif znak.islower():
                if num > ord("z"):
                    num -= 26
                elif num < ord("a"):
                    num += 26

            szyfrogram += chr(num)
        else:
            szyfrogram += znak

    return szyfrogram


def odzyfruj(napis, przesuniecie):
    return szyfruj(napis, -przesuniecie)


def main():
    napis = input("Podaj napis: ")
    przesuniecie = int(input("Podaj przesuniecie: "))
    szyfrogram = szyfruj(napis, przesuniecie)
    print("Zaszyfrowany napis:", szyfrogram)
    print("Odszyfrowany napis:", odzyfruj(szyfrogram, przesuniecie))


if __name__ == "__main__":
    main()
