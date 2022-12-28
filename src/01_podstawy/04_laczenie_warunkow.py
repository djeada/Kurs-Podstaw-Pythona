# dla and - wszystkie warunki musza byc spelnione
# dla or - wystarczy ze jeden warunek jest spelniony

if True and False:
    print("1")
elif True and True:
    print("2")
elif False and False:
    print("3")

if True or True:
    print("a")
elif True or False:
    print("b")
elif False or False:
    print("c")

# warunek trojkata

a = int(input("Podaj dlugosc boku a: "))
b = int(input("Podaj dlugosc boku b: "))
c = int(input("Podaj dlugosc boku c: "))

if a + b > c and a + c > b and b + c > a:
    print("Mozna zbudowac trojkat")
else:
    print("Nie mozna zbudowac trojkata")


# znajdz maksimum z 3 liczb

a = int(input("Podaj liczbe a: "))
b = int(input("Podaj liczbe b: "))
c = int(input("Podaj liczbe c: "))

if a > b and a > c:
    print("a jest najwieksza")
elif b > a and b > c:
    print("b jest najwieksza")
else:
    print("c jest najwieksza")
