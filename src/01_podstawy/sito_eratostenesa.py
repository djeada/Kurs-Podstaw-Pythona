# znajdujemy liczby pierwsze z przedzialu [2,n]
def sito(n):
    temp = [1 for x in range(n + 1)]
    for i in range(2, n + 1):
        for j in range(i + 1, n + 1):
            if j % i == 0:
                temp[j] = 0

    primes = []
    for i in range(2, len(temp)):
        if temp[i] == 1:
            primes.append(i)

    return primes


def sito2(n):
    primes = []
    temp = [True] * (n + 1)
    for i in range(2, n):
        if temp[i]:
            primes.append(i)
            for j in range(i * i, n + 1, i):
                temp[j] = False
    return primes


print(sito(100))
print(sito2(100))
