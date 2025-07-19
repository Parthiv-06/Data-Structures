def inverted_triangle(n):
    for i in range(n-1,-1,-1):
        for j in range(i,n):
            print(" ",end="")
        for j in range((2*i)+1):
            print("*",end="")
        print()
inverted_triangle(10)