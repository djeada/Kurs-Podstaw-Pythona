def zmienNtyBit(liczba, n, bit):
    if bit == 1:
        return liczba | (1 << (n - 1))
    elif bit == 0:
        return liczba & ~(1 << (n - 1))


print(zmienNtyBit(5, 2, 1))
print(zmienNtyBit(5, 1, 0))
