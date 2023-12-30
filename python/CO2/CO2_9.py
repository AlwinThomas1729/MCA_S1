def patt(n):
    for i in range(n):
        for j in range(i + 1):
            print("*", end=" ")
        print()

    # Lower part of the pattern
    for i in range(n - 1, 0, -1):
        for j in range(i):
            print("*", end=" ")
        print()

n=int(input("Enter max line number"))
patt(n)