import os
import datetime

#nazwa systemu
print(os.name)

#folder w ktorym aktualnie jestesmy
print(os.getcwd())

#sciezka absolutna
print(os.path.abspath('.'))

#wyswietlenie zawartosci folderu w ktorym jestesmy
print(os.listdir('.'))

#przechodzenie miedzy folderami
#os.chdir(sciezka)

#tworzenie nowego folderu
os.mkdir('folder')

#usuwanie folderu
#os.rmdir('folder')

#tworzymy plik
with open('plik.txt', mode='w') as plik:
    print('test')

#zmiana nazwy
os.rename('plik.txt','folder/plik2.txt')

#info o pliku
print(os.stat('folder/plik2.txt'))

#czas ostatniej modyfikacji
print(datetime.datetime.fromtimestamp(os.stat('folder/plik2.txt').st_mtime))

#usuwamy plik
#os.remove('plik2.txt')

#walk przechodzi przez wszystkie foldery znajdujace sie w obecnym folderze
#zwraca informacje o sciezce, o folderach i plikach

folder = os.getcwd()

for sciezka, foldery, pliki in os.walk(folder):
    print('Sciezka: ', sciezka)
    print('Foldery: ', foldery)
    print('Pliki: ', pliki)
    print()




