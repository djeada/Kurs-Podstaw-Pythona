"""
Pierwsze wystapienie wielkiej litery w napisie.

Adam -> wynik: 0 (wyjasnienie: A)
w miescie Warszawa -> wynik: 10 (wyjasnienie: W)
"""


def pierwsza_wielka_petla(napis):
    for i, znak in enumerate(napis):
        if znak.isupper():
            return i
    return -1


def pierwsza_wielka_rekurencja(napis):
    if len(napis) == 0:
        return -1
    if napis[0].isupper():
        return 0
    wynik = pierwsza_wielka_rekurencja(napis[1:])
    if wynik == -1:
        return -1
    return 1 + wynik


if __name__ == "__main__":
    print("Pierwsza wielka litera w napisie w miescie Warszawa")
    print(pierwsza_wielka_petla("w miescie Warszawa"))
    print(pierwsza_wielka_rekurencja("w miescie Warszawa"))
    print()

    print("Pierwsza wielka litera w napisie 123ABC")
    print(pierwsza_wielka_petla("123ABC"))
    print(pierwsza_wielka_rekurencja("123ABC"))
    print()

    print("Pierwsza wielka litera w napisie abc")
    print(pierwsza_wielka_petla("abc"))
    print(pierwsza_wielka_rekurencja("abc"))
