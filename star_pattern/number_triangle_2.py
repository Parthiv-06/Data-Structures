def numbered_triangle_2(n):
    for i in range(1,n):
        for j in range(i):
            print(i,end="")
        print()
numbered_triangle_2(10)