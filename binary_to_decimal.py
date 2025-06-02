##using list method

def binary_to_decimal(arr):
    decimal=0
    n=len(arr)
    for i in range(n):
        decimal+=arr[n-1-i]*(2**i)
        # print(decimal)
    return decimal
arr=[1,1,0,1]
print(binary_to_decimal(arr))

# using string method

def binary_to_decimal1(bin):
    n=len(bin)
    decimal=0
    for i in range(n):
        decimal+=int(bin[n-1-i])*(2**i)
    return decimal
bin='1101'
print(binary_to_decimal1(bin))