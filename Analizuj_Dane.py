import csv
import numpy
from matplotlib import pyplot

with open('generowane.csv', 'r') as otworzPlik:
    dane = list(csv.reader(otworzPlik, delimiter=','))

dane = list(filter(None, dane))

print('Dane: ')
print(dane[:10])

czas = [x[0] for x in dane]
dane = [float(y.strip('()')) for x in dane for y in x[1].split(',')]

sinus = [dane[i] for i in range(len(dane)) if i%2 == 0]
funkcja = [dane[i] for i in range(len(dane)) if i%2 == 1]

print('Czas: ')
print(czas[:10])
print('Dane2: ')
print(sinus[:10])

print('Największa wartość: ', max(funkcja))
print('Najmniejsza wartość: ', min(funkcja))

print('Wartość średnia: ', numpy.mean(sinus))
print('Odchylenie standardowe: ', numpy.std(sinus))
print('Mediana: ', numpy.median(sinus))


      
pyplot.plot(czas,sinus)
pyplot.plot(czas,funkcja, marker='+', linestyle='None')
pyplot.ylim([-2,2])
pyplot.show()

