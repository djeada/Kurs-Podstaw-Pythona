# while powtarza blok kodu dopoki warunek jest prawdziwy

while False:  # dla True mamy petle nieskonczona
    print("Ten kod sie nie wykona")

# wypisywanie liczb z przedzialu 0-9
i = 0
while i < 10:
    print(i)
    i += 1

# sprawdzanie danych od uzytkownika
dane = "xxx"
while dane != "koniec":
    dane = input("Wpisz 'koniec' zeby zakonczyc: ")

# wypisywanie cyfr liczby
liczba = 123456789
while liczba > 0:
    cyfra = liczba % 10
    print(cyfra)
    liczba = liczba // 10
