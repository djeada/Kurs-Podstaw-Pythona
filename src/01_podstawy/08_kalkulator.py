# kalkulator z menu


def suma(a, b):
    return a + b


def roznica(a, b):
    return a - b


def iloczyn(a, b):
    return a * b


def iloraz(a, b):
    return a / b


def potega(a, b):
    return a ** b


def menu():
    print("1. Dodawanie")
    print("2. Odejmowanie")
    print("3. Mnozenie")
    print("4. Dzielenie")
    print("5. Potegowanie")
    print("6. Wyjscie")


def main():

    while True:
        menu()
        wybor = input("Wybierz opcje: ")

        if wybor == "6":
            break

        a = int(input("Podaj liczbe a: "))
        b = int(input("Podaj liczbe b: "))

        if wybor == "1":
            print(suma(a, b))
        elif wybor == "2":
            print(roznica(a, b))
        elif wybor == "3":
            print(iloczyn(a, b))
        elif wybor == "4":
            print(iloraz(a, b))
        elif wybor == "5":
            print(potega(a, b))
        else:
            print("Niepoprawny wybor")


if __name__ == "__main__":
    main()
