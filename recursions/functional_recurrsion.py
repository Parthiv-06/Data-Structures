def sum_of_n(i):
    if i==0:
        return 0
    return i+sum_of_n(i-1)
print(sum_of_n(5))
