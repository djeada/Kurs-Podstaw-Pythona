#lista slownikow
#mini baza ksiazek w ksiegarni
#lista slownikow reprezentujaca ksiazki w ksiegarni
#dodawnie ksiazki
#usuwac
#wyswietlanie ksiazek wedlug kryterium
#znajdowanie najtanszej oraz najdrozszej ksiazki

from operator import itemgetter

def dodaj_ksiazke(lista_ksiazek, klucze):
    #lista przechowujaca wartosci dla pojedynczego slownika
    lista = []
    while 1:
        print('Podaj tytul ksiazki')
        tytul = input()
        if czy_ksiazka(lista_ksiazek, tytul):
            print('Ksiazka o tytule ', tytul, ' jest juz w naszym zbiorze!')
        else:
            lista.append(tytul)
            break

    print('Podaj autora ksiazki')
    autor = input()
    lista.append(autor)
    print('Podaj rok wydania ksiazki')
    rok = int(input())
    lista.append(rok)
    print('Podaj cene ksiazki')
    cena = input()
    lista.append(cena)
    print('Podaj liczbe stron ksiazki')
    liczba_stron = input()
    lista.append(liczba_stron)

    #dodajemy ksiazke do listy ksiazek
    lista_ksiazek.append(dict(zip(klucze, lista)))
    

#funkcja sprawdza czy ksiazka znajduje sie w liscie ksiazek
def czy_ksiazka(lista_ksiazek, tytul):
    for ksiazka in lista_ksiazek:
        if tytul == ksiazka['Tytul']:
            return True
    return False

#funkcja realizujaca usuwanie ksiazek
def usun_ksiazke(lista_ksiazek, tytul):
    for ksiazka in lista_ksiazek:
        if tytul == ksiazka['Tytul']:
            del ksiazka
            break

#funkcja znajdujaca najtansza ksiazke
def najtansza(lista_ksiazek):
    indeks = 0
    najtansza = lista_ksiazek[0]['Cena']
    for i in range(1, len(lista_ksiazek)):
        if lista_ksiazek[i]['Cena'] < najtansza:
            najtansza = lista_ksiazek[i]['Cena']
            indeks = i
    return indeks

def wyswietl(lista_ksiazek, klucze):
    i = 0
    for ksiazka in lista_ksiazek:
        print('Ksiazka numer ', i)
        print(' '.join(str(ksiazka[klucz]) for klucz in klucze))
        print(' ')
        i += 1

#lista slownikow, reprezentuje ksiazki w ksiegarni
lista_ksiazek = []
klucze = ['Tytul', 'Autor', 'Rok Wydania', 'Cena', 'Liczba Stron']

for i in range(3):
    dodaj_ksiazke(lista_ksiazek, klucze)

wyswietl(lista_ksiazek, klucze)

print('lista posortowana wedlug ceny: ')
print(sorted(lista_ksiazek, key=itemgetter('Cena')))
#print(sorted(lista_ksiazek, key=itemgetter('Cena'), reverse=True))

print('najtansza ksiazka: ')
print(lista_ksiazek[najtansza(lista_ksiazek)])

while 1:
    print('Podaj nazwe ksiazki ktora chcesz usunac')
    tytul = input()
    if not czy_ksiazka(lista_ksiazek, tytul):
        print('Ksiazka o tytule ', tytul, ' nie znajduje sie w zbiorze!')
    else:
        usun_ksiazke(lista_ksiazek, tytul)
        print('Poprawnie usunieto')
        break




    

