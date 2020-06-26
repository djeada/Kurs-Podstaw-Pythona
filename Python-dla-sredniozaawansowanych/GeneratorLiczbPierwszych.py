import math

#naiwny test pierwszosci
def czyPierwsza(x):
    for i in range(2,int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True

#znajdujemy wszystkie liczby pierwsze do n
def genPierwszych(n):
    for i in range(2,n+1):
        if czyPierwsza(i):
            yield i

print(list(genPierwszych(100)))

#rozwiazanie za pomoca iteratora
class itPierwszych:
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
            if czyPierwsza(self.i):
                return self.i

print(list(itPierwszych(100)))

        
    
