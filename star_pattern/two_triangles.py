def two_triangles(n):
    for i in range(n):
        for j in range(i):
            print(j,end="")
        for k in range(i,n):
            print("  ",end="")
        for l in range(i-1,-1,-1):
            print(l,end="")
        print()
two_triangles(5)