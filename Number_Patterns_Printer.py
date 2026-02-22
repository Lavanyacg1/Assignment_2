pattern = int(input("Enter pattern number (1 to 6): "))
h = int(input("Enter height: "))

if pattern == 1:
    for i in range(1, h + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

elif pattern == 2:
    for i in range(1, h + 1):
        for j in range(i):
            print(i, end=" ")
        print()

elif pattern == 3:
    for i in range(h, 0, -1):
        for j in range(i, 0, -1):
            print(j, end=" ")
        print()

elif pattern == 4:
    for i in range(1, h + 1):
        for j in range(1, i + 1):
            print(j, end="")
        for j in range(i - 1, 0, -1):
            print(j, end="")
        print()

elif pattern == 5:
    num = 1
    for i in range(1, h + 1):
        for j in range(i):
            print(num, end=" ")
            num += 1
        print()

elif pattern == 6:
    for i in range(1, h + 1):
        for j in range(1, i + 1):
            print((i + j) % 2, end=" ")
        print()

else:
    print("Invalid pattern number!")