def staircase(n):
    # Write your code here
    for i in range (n):
        for j in range(0, n - 1- i):
            print(" ", end="")
        for j in range(0, i + 1):
            print("#",end="")
        print()

staircase(6)