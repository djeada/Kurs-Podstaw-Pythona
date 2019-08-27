import numpy
import matplotlib.pyplot as plt
import scipy.interpolate as inter
import random

liczba_miast = 1000

lista_pelna = []

for miasto in range(liczba_miast):
    lista_miasta = []
    for czlowiek in range(random.randint(100,3000)):
        if random.random() < 0.1:
            lista_miasta.append(1)
        else:
            lista_miasta.append(0)
    lista_pelna.append(lista_miasta)

for miasto in range(liczba_miast):
    lista_pelna[miasto] = 100*lista_pelna[miasto].count(1)/len(lista_pelna[miasto])

print(lista_pelna)

plt.hist(lista_pelna, bins=30)
plt.xlim(0,100)
plt.show()


