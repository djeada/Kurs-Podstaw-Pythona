#lista z imionami
#ile razy kazde z imion pojawia sie w liscie
#slowniki maja klucze oraz odpowiadajace wartosci
import random

def dodaj_imie(slownik, lista_imion):
    for imie in lista_imion:
        if imie not in slownik:
            slownik[imie] = 1
        else:
            slownik[imie] = slownik[imie] + 1

def ile_razy(slownik, imie):
    if imie in slownik:
        x = slownik[imie]
    else:
        x = 0
    return x

def wyswietl_slownik(slownik):
    for klucz in slownik:
        print('Imie ', klucz, ' wystapilo ', slownik[klucz], ' razy.')

slownik = dict()
lista_imion = ['Tunczyk', 'James', 'Adam', 'brokul', 'Jerzy', 'wiezy', 'lol']
nowa_lista = []

for x in range(30):
    for i in range(20):
        nowa_lista.append(lista_imion[random.randint(0,len(lista_imion)-1)])
    dodaj_imie(slownik,nowa_lista)
    nowa_lista = []

wyswietl_slownik(slownik)
print(ile_razy(slownik, 'Adam'))
