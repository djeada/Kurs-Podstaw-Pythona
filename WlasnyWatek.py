import threading
import time

class mojWatek(threading.Thread):
 
    def __init__(self, nazwa = 'Watek', opoznienie = 1, powtorzenia = 3):
        threading.Thread .__init__(self)
 
        self.nazwa = nazwa
        self.powtorzenia = powtorzenia
        self.opoznienie = opoznienie
 
    def run(self):
        print(self.nazwa, ' rozpoczyna dzialanie')
        for i in range(self.powtorzenia):
            print(self.nazwa, ' idzie spac na ', self.opoznienie, ' sekund')
            time.sleep(self.opoznienie)
        print(self.nazwa, ' konczy dzialanie')

print('Tworze dwa watki')
watek1 = mojWatek('Watek 1', 1, 8)
watek2 = mojWatek('Watek 2', 2, 3)
watek1.start()
watek2.start()

print('Na razie')
