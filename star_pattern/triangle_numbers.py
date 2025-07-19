def triangle_numbers(n):
    for i in range(n):
        for j in range(1,i):
            print(j,end="")
        print()
triangle_numbers(10)