import math

# naiwny test pierwszosci
def czy_pierwsza(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


# rozwiazanie z uzyciem generatora
def generator_liczb_pierwszych(n):
    for i in range(2, n + 1):
        if czy_pierwsza(i):
            yield i


# rozwiazanie z uzyciem iteratora
class IteratorLiczbPierwszych:
    def __init__(self, n):
        self.i = 1
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        while 1:
            self.i += 1
            if self.i > self.n:
                raise StopIteration
            if czy_pierwsza(self.i):
                return self.i


if __name__ == "__main__":
    n = 30
    print(f"Liczby pierwsze mniejsze od {n}:")

    print("\nRozwiazanie z uzyciem generatora:")
    print(list(generator_liczb_pierwszych(n)))

    print("\nRozwiazanie z uzyciem iteratora:")
    print(list(IteratorLiczbPierwszych(n)))
