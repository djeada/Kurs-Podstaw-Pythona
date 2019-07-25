#iterator to obiekt ktory sluzy do przegladania elementow struktury
#listy, zbiory, slowniki, krotki sa iterowalne

lista = [2, 9, 3]

moj_iterator = iter(lista)
print(moj_iterator)
print(next(moj_iterator))
print(next(moj_iterator))
print(next(moj_iterator))

#iter inicjuje iteracje
#next zwraca wartosc danego elementu, przechodzi do nastepnego
#i zwraca blad gdy doszlismy do konca


class MojIterator():
    def __init__(self):
        self.x = 1
        self.max = 10

    def __iter__(self):
        return self


    def __next__(self):
        x = self.x

        if x > self.max:
            raise StopIteration

        self.x += 1
        return x

for i in MojIterator():
    print(i)







