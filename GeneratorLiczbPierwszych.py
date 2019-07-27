import math

def isprime(num):
    for i in range(2, int(math.sqrt(num))):
        if (num % i) == 0:
            return False
    return True

def gen_primes(max_number):
    for num1 in range(2, max_number):
        if isprime(num1):
            yield num1

print(list(gen_primes(333)))


class itPierwszych():
    def __init__(self, n):
        self.i = 0
        self.n = n
        
    def __iter__(self):
        return self

    def __next__(self):
        while True:
            self.i+=1
            if self.i > self.n:
                raise StopIteration
            if isprime(self.i):
                return self.i

print(list(itPierwszych(333)))



