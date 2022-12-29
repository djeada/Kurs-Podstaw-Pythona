class Kaczka:
    def kwacz(self):
        print("Kwa kwa")


class Ornitolog:
    def kwacz(self):
        print("Dziwne dzwieki")


if __name__ == "__main__":
    kaczka = Kaczka()
    ornitolog = Ornitolog()

    niepowiazane_obiekty = [kaczka, ornitolog]

    for obiekt in niepowiazane_obiekty:
        obiekt.kwacz()
