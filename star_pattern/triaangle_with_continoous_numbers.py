def continous_numbers_triangle(n):
    s=1
    for i in range(n):
        for j in range(i):
            print(s,end=" ")
            s+=1
        print()
continous_numbers_triangle(5)
