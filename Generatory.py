def generator():
    yield 1
    yield 2
    yield 3


for i in generator():
    print(i)


def generator2(a,b):
    while a < b:
        yield a
        a+=1

for i in generator2(4,10):
    print(i)
