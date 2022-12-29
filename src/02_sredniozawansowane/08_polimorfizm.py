from abc import ABC, abstractmethod


class Ksztalt(ABC):
    @abstractmethod
    def pole(self):
        pass

    @abstractmethod
    def obwod(self):
        pass


class Kolo(Ksztalt):
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


class Kwadrat(Ksztalt):
    def __init__(self, bok):
        self.bok = bok

    def obwod(self):
        return 4 * self.bok

    def pole(self):
        return self.bok ** 2

    def __str__(self):
        return f"Kwadrat o boku {self.bok}"

    def __repr__(self):
        return self.__str__()


if __name__ == "__main__":
    # ksztalt = Ksztalt() # TypeError: Can't instantiate abstract class Ksztalt with abstract methods obwod, pole
    kolo = Kolo(5)
    kwadrat = Kwadrat(5)

    ksztalty = [kolo, kwadrat]

    for ksztalt in ksztalty:
        print(ksztalt)
        print(f"Pole: {ksztalt.pole()}")
        print(f"Obwod: {ksztalt.obwod()}")
        print()
