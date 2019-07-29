#watki to czesci programu ktore moga dzialac jednoczesnie
#watki istnieja w obrebie danego procesu
#wspoldziela zasoby

from threading import Thread
import time

#wyswietla czas
def licznik(nazwa, opoznienie, powtorzenia):
    print(nazwa, ' zostal uruchomiony')
    for i in range(powtorzenia):
        time.sleep(opoznienie)
        print(nazwa, ' ', str(time.ctime(time.time())))
    print(nazwa, ' zakonczyl dzialanie')

lista = []
for i in range(3):
    lista.append(Thread(target=licznik, args=('Licznik ' + str(i+1), i+1, (i+1)**2)))

for x in lista:
    x.start()
