def right_triangle_4(n):
    for i in range(n):
        for j in range(i,n):
            print(" ",end="")
        for k in range(i):
            print("*",end="")
        print()
right_triangle_4(10)