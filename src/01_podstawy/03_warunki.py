# typ logiczny - bool - jedynie dwie wartosci: True, False

zmienna = True
print(zmienna)

# przydatne przy budowaniu warunkow

a = 5
b = 10

a_mniejsze_od_b = a < b
a_rowne_b = a == b

print(a_mniejsze_od_b)
print(a_rowne_b)

if a_mniejsze_od_b:
    print("a jest mniejsze od b")

zapisane_haslo = "haslo"
otrzymane_haslo = input("Podaj haslo: ")

if otrzymane_haslo == zapisane_haslo:
    print("Haslo poprawne")
else:
    print("Haslo niepoprawne")

# if - else - elif

liczba = int(input("Podaj liczbe: "))

if liczba < 0:
    print("Liczba ujemna")
elif liczba == 0:
    print("Liczba jest rowna 0")
else:
    print("Liczba dodatnia")


# znajdowanie wiekszej liczby

liczba_a, liczba_b = input("Podaj dwie liczby: ").split()

liczba_a = int(liczba_a)
liczba_b = int(liczba_b)

# if liczba_a > liczba_b:
#    print(liczba_a)
# else:
#    print(liczba_b)

# zagniezdzanie warunkow

if liczba_a > liczba_b:
    print("Liczba a jest wieksza od liczby b")
    if liczba_a > 0:
        print("Liczba a jest dodatnia")
    else:
        print("Liczba a jest ujemna")
else:
    print("Liczba b jest wieksza od liczby a")
    if liczba_b > 0:
        print("Liczba b jest dodatnia")
    else:
        print("Liczba b jest ujemna")
