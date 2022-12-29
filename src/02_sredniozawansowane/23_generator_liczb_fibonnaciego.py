# rozwiazanie z uzyciem generatora
def generator_liczb_fibonnaciego(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


# rozwiazanie z uzyciem iteratora
class IteratorLiczbFibonnaciego:
    def __init__(self, n):
        self.a, self.b = 0, 1
        self.i = 0
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.i >= self.n:
            raise StopIteration
        self.i += 1
        a = self.a
        self.a, self.b = self.b, self.a + self.b
        return a


if __name__ == "__main__":
    n = 10
    print(f"Pierwsze {n} liczb Fibonnaciego:")

    print("\nRozwiazanie z uzyciem generatora:")
    print(list(generator_liczb_fibonnaciego(n)))

    print("\nRozwiazanie z uzyciem iteratora:")
    print(list(IteratorLiczbFibonnaciego(n)))
