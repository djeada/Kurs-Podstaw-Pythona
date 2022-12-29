class Pensja:
    def __init__(self, pensja: int, stopa_podwyzki: float):
        self.pensja = pensja
        self.stopa_podwyzki = stopa_podwyzki

    def awansuj(self):
        self.pensja += int(self.pensja * self.stopa_podwyzki)

    def roczna_pensja(self):
        return self.pensja * 12

    def __str__(self):
        return f"Pensja: {self.pensja}, stopa podwyzki: {self.stopa_podwyzki}"


class Pracownik:
    def __init__(self, imie: str, nazwisko: str, pensja: Pensja):
        self.imie = imie
        self.nazwisko = nazwisko
        self.pensja = pensja  # kompozycja, pensja jest czescia pracownika

    def awansuj(self):
        self.pensja.awansuj()

    def __str__(self):
        return f"Pracownik: {self.imie} {self.nazwisko}, zarabia rocznie: {self.pensja.roczna_pensja()}"


class Szef(Pracownik):
    def __init__(self, imie: str, nazwisko: str, pensja: Pensja):
        super().__init__(imie, nazwisko, pensja)

    def awansuj(self):
        self.pensja.stopa_podwyzki *= 2
        self.pensja.awansuj()

    def __str__(self):
        return f"Szef: {self.imie} {self.nazwisko}, zarabia rocznie: {self.pensja.roczna_pensja()}"


if __name__ == "__main__":
    informatyk_a = Pracownik("Jan", "Kowalski", Pensja(1000, 0.1))
    informatyk_b = Pracownik("Anna", "Nowak", Pensja(2000, 0.1))
    szef = Szef("Adam", "Nowak", Pensja(3000, 0.1))

    pracownicy_firmy = (informatyk_a, informatyk_b, szef)

    print("Rok 2022:")
    for pracownik in pracownicy_firmy:
        print(pracownik)
        pracownik.awansuj()

    print("\nRok 2023:")
    for pracownik in pracownicy_firmy:
        print(pracownik)
