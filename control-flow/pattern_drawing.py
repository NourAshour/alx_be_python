size = int(input("Enter the size of the pattern: "))
i = 0
while i <= size:
    for i in range(size):
        print("*", end="")
    print("\n")
    i = i + 1