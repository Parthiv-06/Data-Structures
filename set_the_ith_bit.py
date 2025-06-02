def set_the_ith_bit(val,i):
    x=val|(1<<i)
    return x
val=9
i=2
print(set_the_ith_bit(val,i))