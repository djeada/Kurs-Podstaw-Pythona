"""\
***
***
***
"""
for i in range(0, 3):
    for j in range(0, 3):
        print("*", end="")
    print("\r")

print("")
print("")

"""\
1111
1111
1111
"""
for i in range(0, 3):
    for j in range(0, 4):
        print("1", end="")
    print("\r")

print("")
print("")

"""\
1234
1234
1234
"""
for i in range(0, 3):
    for j in range(0, 4):
        print(j + 1, end="")
    print("\r")

print("")
print("")

"""\
123
456
789
"""
for i in range(0, 3):
    for j in range(0, 3):
        print(j + 1 + 3 * i, end="")
    print("\r")
