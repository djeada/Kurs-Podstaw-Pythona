"""
Sito Eratostenesa

1. Przygotuj liste zapelniona zerami o dlugosci n+1.
2. Przechodzimy po wszystkich elementach listy.
3. Wykresl wszystkie wielokrotnosci aktualnie sprawdzanego elementu.
4. Powtarzamy kroki 2-3, az dojdziemy do pierwiastka z n.
5. Liczby, ktore pozostaly nie wykreslone sa liczbami pierwszymi.
"""


def sito_eratostenesa(n):
    lista = [0] * (n + 1)
    for i in range(2, int(n ** 0.5) + 1):
        if lista[i] == 0:
            for j in range(i * i, n + 1, i):
                lista[j] = 1

    return [i for i in range(2, n + 1) if lista[i] == 0]


if __name__ == "__main__":
    print(sito_eratostenesa(10))
    print(sito_eratostenesa(20))
    print(sito_eratostenesa(30))
    print(sito_eratostenesa(40))
    print(sito_eratostenesa(50))
