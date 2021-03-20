import argparse


def suma(a, b):
    return a + b


p = argparse.ArgumentParser()
p.add_argument("x", help="pierwsza liczba", type=int)
p.add_argument("y", help="druga liczba", type=int)
p.add_argument("-zapis", help="czy zapisujemy do pliku", action="store_true")
argumenty = p.parse_args()

print(suma(argumenty.x, argumenty.y))

if argumenty.zapis:
    with open("plik.txt", "w") as plik:
        plik.write(str(suma(argumenty.x, argumenty.y)))
