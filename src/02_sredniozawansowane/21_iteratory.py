class IteratorOdwracajacy:
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]


class IteratorZdania:
    def __init__(self, zdanie):
        self.zdanie = zdanie
        self.index = 0
        self.slowa = zdanie.split()

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.slowa):
            raise StopIteration
        self.index += 1
        return self.slowa[self.index - 1]


if __name__ == "__main__":
    lista = [1, -5, 9]

    iterator_listy = iter(lista)
    print("Iterator listy:")
    print(iterator_listy)
    print(next(iterator_listy))
    print(next(iterator_listy))
    print(next(iterator_listy))
    # print(next(iterator_listy)) # StopIteration

    print("\nIterator odwracajacy liste:")
    iterator_odwracajacy = IteratorOdwracajacy(lista)
    for element in iterator_odwracajacy:
        print(element)

    print("\nIterator odwracajacy napis:")
    iterator_odwracajacy_napis = IteratorOdwracajacy("Ala")
    for element in iterator_odwracajacy_napis:
        print(element)

    print("\nIterator zdania:")
    iterator_zdania = IteratorZdania("Ala ma kota")
    for element in iterator_zdania:
        print(element)
