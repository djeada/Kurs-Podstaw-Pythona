#watki to czesci programu ktore dzialaja jednoczesnie
#istnieje w obrebie jednego procesu
#wspodziela zasoby danego procesu

from threading import Thread
import time

#wyswietlamy czas
def licznik(nazwa, opoznienie, powtorzenia):
    print(nazwa, ' zostal uruchomiony')
    for i in range(powtorzenia):
        time.sleep(opoznienie)
        print(nazwa, ' ', str(time.ctime(time.time())))
    print(nazwa, ' zakonczyl dzialanie')

lista = []
for i in range(3):
    lista.append(Thread(target=licznik, args=('Licznik '+str(i+1),i+1,(i+i)**2)))

for x in lista:
    x.start()
    
