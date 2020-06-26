#liczby pierwsze 2,3,5,7,11
#liczby zlozone 4,6,8,9,10

#naiwny test pierwszosci
#sprawdzamy czy x jest pierwsza
#czy przy dzieleniu x przez 2,3,4...x**0.5 otrzymujemy 0
#jesli tak liczba zlozna
#jesli nie liczba pierwsza
import random

def test_pierwszosci(x):
    if x <= 1:
        return False
    for i in range(2,int(x**0.5)):
        if x % i == 0:
            return False
    return True

liczba1 = random.randint(2,1000000)
liczba2 = random.randint(2,1000000)
liczba3 = random.randint(2,1000000)

print('czy liczba ', liczba1, 'jest pierwsza?')
print(test_pierwszosci(liczba1))
print('czy liczba ', liczba2, 'jest pierwsza?')
print(test_pierwszosci(liczba2))
print('czy liczba ', liczba3, 'jest pierwsza?')
print(test_pierwszosci(liczba3))

i=0
while not test_pierwszosci(liczba1):
    liczba1 = random.randint(2,1000000)
    i += 1

print(liczba1, ' jest liczba pierwsza')
print(i)



