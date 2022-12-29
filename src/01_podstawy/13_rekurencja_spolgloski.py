"""
Policz spolgloski w napisie.

Adam -> wynik: 2 (wyjasnienie: d i m)
Robert -> wynik: 4 (wyjasnienie: r b r t)
"""


def policz_spolgloski_petla(napis):
    spolgloski = 0
    for znak in napis:
        znak = znak.lower()
        if znak.isalpha() and znak not in "aeiouy":
            spolgloski += 1
    return spolgloski


def policz_spolgloski_rekurencja(napis):
    if len(napis) == 0:
        return 0
    znak = napis[0].lower()
    if znak.isalpha() and znak not in "aeiouy":
        return policz_spolgloski_rekurencja(napis[1:])
    return 1 + policz_spolgloski_rekurencja(napis[1:])


if __name__ == "__main__":
    print("Liczymy spolgloski w napisie Adam")
    print(policz_spolgloski_petla("Adam"))
    print(policz_spolgloski_rekurencja("Adam"))
    print()

    print("Liczymy spolgloski w napisie Robert")
    print(policz_spolgloski_petla("Robert"))
    print(policz_spolgloski_rekurencja("Robert"))
    print()

    print("Liczymy spolgloski w napisie abc123")
    print(policz_spolgloski_petla("abc123"))
    print(policz_spolgloski_rekurencja("abc123"))
