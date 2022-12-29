class Tunczyk:

    ilosc_tunczykow = 0

    def __init__(self, imie):
        self.imie = imie
        Tunczyk.ilosc_tunczykow += 1

    @classmethod
    def alternatywny_konstruktor(cls):
        return cls(f"Tunczyk_{cls.ilosc_tunczykow + 1}")

    def __del__(self):
        Tunczyk.ilosc_tunczykow -= 1

    def __str__(self):
        return f"Tunczyk o imieniu {self.imie}"

    def __repr__(self):
        return self.__str__()


if __name__ == "__main__":
    tunczyk_a = Tunczyk("Nemo")
    tunczyk_b = Tunczyk("Fin")
    tunczyk_c = Tunczyk("Gilly")
    print(tunczyk_a)
    print(tunczyk_b)
    print(tunczyk_c)
    print(f"Ilosc tunczykow: {Tunczyk.ilosc_tunczykow}")
    del tunczyk_a
    print(f"Ilosc tunczykow: {Tunczyk.ilosc_tunczykow}")

    Tunczyk.ilosc_tunczykow = 0
    print(f"Ilosc tunczykow: {Tunczyk.ilosc_tunczykow}")

    tunczyk_d = Tunczyk.alternatywny_konstruktor()
    print(tunczyk_d)
