def suma(a,b):
    return a + b

def roznica(a,b):
    return a - b

def iloczyn(a,b):
    return a*b

def iloraz(a,b):
    return a/b

def kalkulator(wybor,a,b):
    if wybor == 1:
        print('suma liczb', a, ' i ', b, ' to ', suma(a,b))
    if wybor == 2:
        print('roznica liczb', a, ' i ', b, ' to ',roznica(a,b))
    if wybor == 3:
        print('iloczyn liczb', a, ' i ', b, ' to ',iloczyn(a,b))
    if wybor == 4:
        print('iloraz liczb', a, ' i ', b, ' to ',iloraz(a,b))

for i in range(1,5):
    kalkulator(i,10,5)
