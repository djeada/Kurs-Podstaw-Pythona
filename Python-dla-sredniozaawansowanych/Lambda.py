def funkcja(a, b):
    return a * b - b + 5


# nie ma def ani return
# lambda arguemnty : wyrazenie
funLambda = lambda a, b: a * b - b + 5

print(funkcja(4, 6))
print(funLambda(4, 6))

# przyklad funkcji lambda bez argumentow
funLambda2 = lambda: "Nie ma argumentow"
print(funLambda2())

# przyklad funkcji zwracajacej funkcje lambda
def funkcja2(a):
    return lambda x: x * x + a


print(funkcja2(3)(2))

# przyklad uzycia funkcji lambda jako argumentu funkcji map()
print(list(map(lambda x: x * 3, [3, 2, 5, 8, 2])))

# przyklad funkcji lambda polaczonej z instrukcja warunkowa
funLambda3 = lambda x: "Tak" if x % 2 == 0 else "Nie"
print(funLambda3(5))

print(list(map(lambda x: "Tak" if x % 2 == 0 else "Nie", [3, 2, 5, 8, 2])))

# przyklad uzycia funkcji lambda jako argumentu funkcji filter()
print(list(filter(lambda x: x % 2 == 0, [3, 2, 5, 8, 2])))
