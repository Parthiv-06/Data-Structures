def triangle_2(n):
    for i in range(n):
        for j in range(i,n):
            print("*",end="")
        print()
triangle_2(10)