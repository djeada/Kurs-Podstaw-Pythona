import random
import math
import csv

czas = []
dane = []

for i in range(100):
    czas.append(i)
    dane.append((math.sin(i)+random.uniform(-0.5,0.5),i+random.random()*math.sqrt(i)))

with open('generowane.csv', 'w') as zapiszPlik:
    zapis = csv.writer(zapiszPlik)
    zapis.writerows([(czas[i],dane[i]) for i in range(100)])
                
