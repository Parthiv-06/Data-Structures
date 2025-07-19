def rhombus(n):
    for i in range(n):
        for j in range(i,n):
            print(" ",end="")
        for k in range((2*i)+1):
            print("*",end="")
        print()
    for i in range(n-1,-1,-1):
        for j in range(i,n):
            print(" ",end="")
        for k in range((2*i)+1):
            print("*",end="")
        print()
rhombus(5)