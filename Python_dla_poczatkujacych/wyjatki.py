# blad skladni
# wyjatki
# wyjatek = obiekt Pythna, reprezentujacy blad(jaki blad, gdzie wystapil)
# try-except

lista = []

for i in range(5):
    try:
        x = int(input())
        # x = a
    except ValueError as e:
        x = 0
        print(e)
    except Exception as e:
        print(e)
    else:
        print("Poprawnie dodano liczbe")
    finally:
        lista.append(x)

for i in range(5):
    print(lista[i])
