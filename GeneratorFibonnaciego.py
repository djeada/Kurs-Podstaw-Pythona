
def genFib(n):
    a, b = 0, 1
    for i in range(n+1):
        yield a
        a, b = b, a + b
   
print(list(genFib(5)))
