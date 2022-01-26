"""\
*
**
***
"""
for i in range(0, 3):
    for j in range(2 - i, 3):
        print("*", end="")
    print("\r")

print("")
print("")

"""\
1
11
111
"""
for i in range(0, 3):
    for j in range(2 - i, 3):
        print("1", end="")
    print("\r")

print("")
print("")

"""\
1
12
123
"""
for i in range(0, 3):
    for j in range(0, i + 1):
        print(j + 1, end="")
    print("\r")

print("")
print("")
