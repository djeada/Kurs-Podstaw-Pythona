from dataclasses import dataclass


def funkcja_mat(a, b):
    return a * b - b + 5


@dataclass
class Miasto:
    nazwa: str
    liczba_mieszkancow: int


if __name__ == "__main__":
    mat_lambda = lambda a, b: a * b - b + 5

    print("Wynik funkcji matematycznej: a * b - b + 5")
    print(funkcja_mat(4, 6))
    print(mat_lambda(4, 6))

    # transformacja listy
    lista = [-1, 2, -3, 4]
    wynik = list(map(lambda x: x ** 2, lista))
    print("\nWynik transformacji listy: x**2")
    print(wynik)

    # wlasne sortowanie
    miasto_a = Miasto("Inowroclaw", 70_000)
    miasto_b = Miasto("Warszawa", 2_000_000)
    miasto_c = Miasto("Wroclaw", 1_000_000)

    miasta = (miasto_a, miasto_b, miasto_c)

    # posortowane po liczbie mieszkancow
    print("\nSortowanie po liczbie mieszkancow:")
    print(
        sorted(miasta, key=lambda m: m.liczba_mieszkancow)
    )  # Inwroclaw, Wroclaw, Warszawa

    # posortowane po dlugosci nazwy
    print("\nSortowanie po dlugosci nazwy:")
    print(sorted(miasta, key=lambda m: len(m.nazwa)))  # Wroclaw, Warszawa, Inwroclaw

    # lambda z warunkiem
    wielka_litera = lambda x: x.capitalize() if isinstance(x, str) else x
    print("\nWielka litera:")
    print(wielka_litera("ala ma kota"))  # Ala ma kota
    print(wielka_litera(123))  # 123

    # filtrowanie listy
    print("\nFiltrowanie listy:")
    print(list(filter(lambda x: x > 0, lista)))  # [2, 4]

    # zmiana wartosci pola w obiekcie
    print("\nZmiana wartosci pola w obiekcie:")
    print(miasto_a)  # Miasto(nazwa='Inowroclaw', liczba_mieszkancow=70000)
    resetuj_nazwe = lambda m: setattr(m, "nazwa", "brak nazwy")
    resetuj_nazwe(miasto_a)
    print(miasto_a)  # Miasto(nazwa='brak nazwy', liczba_mieszkancow=70000)
    print()
