def set_the_ith_bit(val,i):
    x=val|(1<<i)
    return x
val=9
i=2
print(set_the_ith_bit(val,i))

# clear the ith set_the_ith_bit
 
def clear_ith_bit(val,i):
    x=val&(~(1<<i))
    return x
val=13
i=2
print(clear_ith_bit(val,i))

#toggle the bit

def toggele_ith_bit(val,i):
    x=val^(1<<i)
    return x
val=13
i=2
print(toggele_ith_bit(val,i))