def zeroes_ones_triangle_2(n):
    for i in range(n):
        if i%2==0:
            start=1
        else:
            start=0
        for j in range(i):
            print(start,end="")
            start=1-start
        print()
zeroes_ones_triangle_2(5)