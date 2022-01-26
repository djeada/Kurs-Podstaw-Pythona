# Szyfr Cezara

# funkcja realizujaca algorytm szyfru Cezara
def szyfr_cezara(wiadomosc, klucz):
    # zmienna przechowujaca zaszyfrowana wiadomosc
    zaszyfrowana_wiadomosc = ""

    # przechodzimy przez wszystkie znaki napisu wiadomosc
    for x in wiadomosc:
        # sprawdzamy czy x jest litera
        if x.isalpha():
            # zamieniamy znak na reprezentacje liczbowa
            liczba = ord(x)
            # przesuwamy reprezentacje liczbowa znaku o klucz pozycji
            liczba += klucz

            if x.isupper():
                if liczba > 90:
                    liczba -= 26
                elif liczba < 65:
                    liczba += 26
            else:
                if liczba > 122:
                    liczba -= 26
                elif liczba < 97:
                    liczba += 26

            # wracamy do reprezentacji znakowej i budujemy zaszyfrowana wiadomosc
            zaszyfrowana_wiadomosc += chr(liczba)
        else:
            zaszyfrowana_wiadomosc += x
    return zaszyfrowana_wiadomosc


# wiadomosc do zaszyfrowania
print("Podaj swoja wiadomosc")
wiadomosc = input()

# klucz
print("Podaj swoj klucz")
klucz = int(input())

print("Twoja zaszyfrowana wiadomosc to ")
print(szyfr_cezara(wiadomosc, klucz))
