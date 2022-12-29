def silnia_czysta(n, wynik=1):
    for i in range(1, n + 1):
        wynik *= i
    return wynik


def silnia_nieczysta(n, wynik=1):
    for i in range(1, n + 1):
        wynik *= i
    with open("wynik.txt", "w") as f:
        f.write(str(wynik))
    return wynik


class Czlowiek:
    def __init__(self, imie, wiek):
        self.imie = imie
        self.wiek = wiek

    def __str__(self):
        return f"{self.imie} ma {self.wiek} lat"

    def __repr__(self):
        return self.__str__()


def reset_czysta(czlowiek):
    return Czlowiek(czlowiek.imie, 0)


def reset_nieczysta(czlowiek):
    czlowiek.wiek = 0
    return czlowiek


if __name__ == "__main__":
    print(silnia_czysta(5))
    print(silnia_nieczysta(5))

    czlowiek = Czlowiek("Jan", 20)
    print(f'Id czlowieka "{czlowiek}" to {id(czlowiek)}')

    nowy_a = reset_czysta(czlowiek)
    print(f'Id czlowieka "{nowy_a}" to {id(nowy_a)}')

    nowy_b = reset_nieczysta(czlowiek)
    print(f'Id czlowieka "{nowy_b}" to {id(nowy_b)}')
