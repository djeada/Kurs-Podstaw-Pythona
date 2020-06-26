#iterator to obiekt ktory przegladania elementow kolekcji
#listy, zbiory, slowniki, krotki sa iterowalne

lista = [1, 3, 4]

iterator_listowy = iter(lista)
print(iterator_listowy)
print(next(iterator_listowy))
print(next(iterator_listowy))
print(next(iterator_listowy))
#print(next(iterator_listowy))

#iter inicjuje iteracje
#next zwraca wartosc danego elementu i przechodzi do nastepnego
#zwraca wyjatek gdy dojdzie do konca

class MojIterator():
    def __init__(self, maks=10):
        self.x = 1
        self.max = maks

    def __iter__(self):
        return self

    def __next__(self):
        x = self.x

        if x > self.max:
            raise StopIteration

        self.x +=5
        return x


for i in MojIterator(40):
    print(i)


class Odwroc():
    def __init__(self, dane='Napis'):
        self.dane = dane
        self.indeks = len(dane)

    def __iter__(self):
        return self

    def __next__(self):
        if self.indeks == 0:
            raise StopIteration
        
        self.indeks -= 1
        return self.dane[self.indeks]

for i in Odwroc():
    print(i, end='')

print('')

for i in Odwroc('tunczyk'):
    print(i, end='')
   
print('')

for i in Odwroc((3,2,'e',10)):
    print(i, end='')


    
        
