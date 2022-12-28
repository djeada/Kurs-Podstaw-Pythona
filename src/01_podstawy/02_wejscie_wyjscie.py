# wejscie i wyjscie

napis = input("Podaj napis: ")
print(napis)

liczba = input("Podaj liczbe: ")
print(liczba)

# liczba = liczba + 10 # blad

liczba = int(liczba)
liczba = liczba + 10
print(liczba)

# pobierz dwie liczby i wyswietl ich sume
liczba_a, liczba_b = input("Podaj dwie liczby: ").split()

liczba_a = int(liczba_a)
liczba_b = int(liczba_b)

print(liczba_a + liczba_b)

# pobierz trzy liczby i wyswietl je w odwrotnej kolejnosci
liczba_a, liczba_b, liczba_c = input("Podaj trzy liczby: ").split()

liczba_a = int(liczba_a)
liczba_b = int(liczba_b)
liczba_c = int(liczba_c)

print(liczba_c, liczba_b, liczba_a)
