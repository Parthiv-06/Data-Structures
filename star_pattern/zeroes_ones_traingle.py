def zeroes_ones_triangle(n):
    key=0
    for i in range(n):
        for j in range(i):
            if j%2!=0:
                key=1
            else:
                key=0
            print(key,end="")
        print()
zeroes_ones_triangle(5)