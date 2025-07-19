def half_rhombus(n):
    for i in range(n):
        for j in range(i):
            print("*",end="")
        print()
    for i in range(n):
        for j in range(i,n):
            print("*",end="")
        print()
half_rhombus(5)
    