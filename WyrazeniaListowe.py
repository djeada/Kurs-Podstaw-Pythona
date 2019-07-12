#ogolny wzor
#lista = [wyrazenie for element in zbior if warunek]

#tworzymy liste za pomoca petli
lista = []
for x in range(10):
    lista.append(x+1)

print(lista)

#tworzymy identyczna liste za pomoca wyrazenia listowego
lista = [x+1 for x in range(10)]
print(lista)

#lista skladajaca sie z szescianow liczb naturalnych 1-10
lista = [(x+1)*(x+1)*(x+1) for x in range(10)]
print(lista)

#lista skladajaca sie z szescianow liczb parzystych nalezacych 1-10
lista = [(x+1)*(x+1)*(x+1) for x in range(10) if (x+1) % 2 == 0]
print(lista)

#lista skladajaca sie z liczb parzystych podzielnych przez 3 i 5 nalezacych do przedzialu 1-100
lista = [x for x in range(1,100) if x % 2 == 0 and x % 3 == 0 and x % 5 == 0]
print(lista)

#lista napisow
zakupy = ['tunczyk', 'brokul', 'groszek', 'fasolka', 'kukurydza', 'grahamki']
print(zakupy)

#uzyskujemy wszystkie napisy zaczynajace sie na litere b z listy napisow
for zakup in zakupy:
    if zakup.startswith('b'):
        print(zakup)

#to samo poprzez wyrazenie listowe
bZakupy = [zakup for zakup in zakupy if zakup.startswith('b')]
print(bZakupy)

#lista 10x10 zainicjalizowana 0
lista2D = [[0]*10 for i in range(10)]
print(lista2D)

#lista 10x10 zainicjalizowana przez numer pozycji listy w liscie
lista2D = [[i]*10 for i in range(10)]
print(lista2D)


