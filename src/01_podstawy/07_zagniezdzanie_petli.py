# kwadrat
for i in range(4):
    for j in range(4):
        print("*", end="")
    print()

# prostokat
for i in range(4):
    for j in range(6):
        print("*", end="")
    print()

# trojkat
for i in range(4):
    for j in range(i + 1):
        print("*", end="")
    print()

# trojkat odwrocony
for i in range(4):
    for j in range(4 - i):
        print("*", end="")
    print()

# trojkat rownoramienny
for i in range(4):
    for j in range(4 - i):
        print(" ", end="")
    for j in range(i + 1):
        print("*", end="")
    print()
