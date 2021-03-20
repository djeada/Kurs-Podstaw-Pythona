# uzyskujemy n pierwszych wyrazow ciagu Fibonacciego za pomoca generatora
def genFib(n):
    a, b = 0, 1
    for i in range(n + 1):
        yield a
        a, b = b, a + b


print(list(genFib(5)))

# uzyskujemy n pierwszych wyrazow ciagu Fibonacciego za pomoca iteratora


class itFib:
    def __init__(self, n):
        self.a = 0
        self.b = 1
        self.i = 0
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.i > self.n:
            raise StopIteration
        self.i += 1
        x = self.a
        self.a, self.b = self.b, self.a + self.b
        return x


lista = []

for x in itFib(5):
    lista.append(x)

print(lista)
