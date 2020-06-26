#generator to funkcja to tworzenia iteratora

def generator():
    yield 1
    yield 2
    yield 8
    
print('Generator1: ')

for i in generator():
    print(i)

x = generator()
print(next(x))
print(next(x))
print(next(x))

def generator2(a,b):
    while a <= b:
        yield a
        a +=3

print('')
print('Generator2: ')

for i in generator2(2,20):
    print(i)

print('')
print('Odwroc: ')

def odwroc(dane):
    for i in range(len(dane)-1,-1,-1):
        yield dane[i]

for i in odwroc('kukulka'):
    print(i,end='')

for i in odwroc((4,3,9,'k',False)):
    print(i,end='')
        
    
