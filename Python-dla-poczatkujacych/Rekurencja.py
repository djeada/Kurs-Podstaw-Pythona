def suma_Petla(lista):
    suma = 0
    for x in lista:
        suma += x
    return suma

#kazda funkcja rekurencyjna ma dwa przypadki: podstawowy i rekurencyjny

def suma_Rekurencyjna(lista):
    #przypadek podstawowy
    if lista == []:
        return 0
    #przypadek rekurencyjny
    else:
        return lista[0] + suma_Rekurencyjna(lista[1:])

lista = [3, 2, 4, 9]
print('Suma poprzez petle: ')
print(suma_Petla(lista))
print('')
print('Suma poprzez rekurencje: ')
print(suma_Rekurencyjna(lista))

#silnia n = n*(n-1)*(n-2)...
#silnia 3 = 3*2*1 = 6

def silnia_Petla(x):
    silnia = 1
    for i in range(1,x+1):
        silnia *= i
    return silnia

def silnia_Rekurencyjna(x):
    #przypadek podstawowy
    if x <= 1:
        return 1
    #przypadek rekurencyjny
    else:
        return x*silnia_Rekurencyjna(x-1)

print('')
print('Silnia poprzez petle: ')
print(silnia_Petla(3))
print('')
print('Silnia poprzez rekurencje: ')
print(silnia_Rekurencyjna(3))

#pierwszy rowny 0 drugi rowny 1 kazdy nastepny suma dwoch poprzednich

def fibonacci_Petla(x):
    poprzedniapoprzednia_liczba = 0
    poprzednia_liczba = 0
    szukana_liczba = 1
    for i in range(1,x):
        poprzedniapoprzednia_liczba = poprzednia_liczba
        poprzednia_liczba = szukana_liczba
        szukana_liczba = poprzedniapoprzednia_liczba + poprzednia_liczba

    return szukana_liczba
    
def fibonacci_Rekurencyjnie(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return fibonacci_Rekurencyjnie(x-1) + fibonacci_Rekurencyjnie(x-2)
    
print('')
print('Fibonacci poprzez petle: ')
print(fibonacci_Petla(10))
print('')
print('Fibonacci poprzez rekurencje: ')
print(fibonacci_Rekurencyjnie(10))




