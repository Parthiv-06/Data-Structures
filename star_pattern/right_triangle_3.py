def right_triangle_2(n):
    for i in range(n):
        for j in range(i):
            print(" ",end="")
        for k in range(i,n):
            print("*",end="")
        print()
right_triangle_2(10)