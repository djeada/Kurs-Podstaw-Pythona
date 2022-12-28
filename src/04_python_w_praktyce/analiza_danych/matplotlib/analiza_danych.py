import csv
import numpy
from matplotlib import pyplot

with open("generowane.csv") as otworzPlik:
    dane = list(csv.reader(otworzPlik, delimiter=","))

dane = list(filter(None, dane))

czas = [x[0] for x in dane]
wartosci = [float(y.strip(")(")) for x in dane for y in x[1].split(",")]

sinus = [wartosci[i] for i in range(len(wartosci)) if i % 2 == 0]
funkcja = [wartosci[i] for i in range(len(wartosci)) if i % 2 == 1]

pyplot.plot(czas, sinus, marker="o", linestyle="None")
pyplot.plot(czas, funkcja, marker="+", linestyle="None")
pyplot.show()

print("Dla funkcji rosnącej: ")
print("Wartość maksymalna: ", max(funkcja))
print("Wartość minimalna: ", min(funkcja))
print("Średnia: ", numpy.mean(funkcja))
print("Mediana: ", numpy.mean(funkcja))
print("Odchylenie standardowe: ", numpy.std(funkcja))

print("Dla funkcji sinus: ")
print("Wartość maksymalna: ", max(sinus))
print("Wartość minimalna: ", min(sinus))
print("Średnia: ", numpy.mean(sinus))
print("Mediana: ", numpy.mean(sinus))
print("Odchylenie standardowe: ", numpy.std(sinus))
