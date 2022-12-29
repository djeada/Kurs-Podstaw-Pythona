class Kolo:
    def __init__(self, promien):
        self.promien = promien

    def obwod(self):
        return 2 * 3.14 * self.promien

    def pole(self):
        return 3.14 * self.promien ** 2

    def __str__(self):
        return f"Kolo o promieniu {self.promien}"

    def __repr__(self):
        return self.__str__()


def znajdz_najwieksze_kolo(kola):
    najwieksze_kolo = kola[0]
    for kolo in kola:
        if kolo.promien > najwieksze_kolo.promien:
            najwieksze_kolo = kolo
    return najwieksze_kolo


if __name__ == "__main__":
    kolo1 = Kolo(5)
    kolo2 = Kolo(10)
    kolo3 = Kolo(15)
    kola = [kolo1, kolo2, kolo3]
    print(znajdz_najwieksze_kolo(kola))
