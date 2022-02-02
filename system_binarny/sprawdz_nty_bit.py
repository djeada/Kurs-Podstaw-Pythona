def sprawdzNtyBit(liczba, n):
    if liczba & (1 << (n - 1)):
        return 1
    return 0


print(sprawdzNtyBit(17, 1))
print(sprawdzNtyBit(28, 3))
print(sprawdzNtyBit(9, 2))
