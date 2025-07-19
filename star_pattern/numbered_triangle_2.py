def numbered_triangle_3(n):
    for i in range(n):
        for j in range(1,n-i):
            print(j,end="")
        print()
numbered_triangle_3(10)