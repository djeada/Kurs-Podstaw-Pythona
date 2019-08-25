def znajdz_duza_litere_iter(napis):
    for x in napis:
        if x.isupper():
            return x
    return -1

def znajdz_duza_litere_rek(napis):
    if len(napis) == 0:
        return -1
    if napis[0].isupper():
        return napis[0]
    else:
        return znajdz_duza_litere_rek(napis[1:])

lista = ['marcepAn', 'tuNczyk', 'rower']

for x in lista:
    print(znajdz_duza_litere_iter(x))
    print(znajdz_duza_litere_rek(x))

