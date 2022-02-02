import random
import matplotlib.pyplot as plt

# czy lubisz warzywa
liczba_miast = 1000

# wszystkie odpowiedzi wszystkich ankietowanych ze wszystkich miast
lista_pelna = []

for miast in range(liczba_miast):
    # odpowiedzi ankietowanych w danym miescie
    lista_miasta = []
    odp = random.randint(0, 1)
    for czlowiek in range(random.randint(100, 3000)):
        lista_miasta.append(odp)
    lista_pelna.append(lista_miasta)

# print(lista_pelna[0][-20:])

# ile procentowo osob powiedzialo tak dla danego miasta
lista_procent = []

for miasto in range(liczba_miast):
    lista_procent.append(100 * lista_pelna[miasto].count(1) / len(lista_pelna[miasto]))

plt.hist(lista_procent, bins=10)
plt.xlim(0, 100)
plt.show()
