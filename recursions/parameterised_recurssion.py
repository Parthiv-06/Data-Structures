def sum_of_n(i,sum):
    if i <=0:
        return sum
    return sum_of_n(i-1,sum+i)
print(sum_of_n(5,0))
