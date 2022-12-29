from dataclasses import dataclass


@dataclass
class Punkt:
    x: float
    y: float


def slownik_na_klase_danych(**kwargs):
    return Punkt(**kwargs)


def klasa_danych_na_slownik(klasa_danych):
    return klasa_danych.__dict__


if __name__ == "__main__":
    p1 = Punkt(1, 2)
    p2 = Punkt(3, 4)

    print(p1)
    print(p2)

    print(f"Punkt {p1} jako slownik: {klasa_danych_na_slownik(p1)}")

    slownik = {"x": -5, "y": -5}
    p3 = slownik_na_klase_danych(**slownik)
    print(f"Slownik {slownik} jako klasa danych: {p3}")
