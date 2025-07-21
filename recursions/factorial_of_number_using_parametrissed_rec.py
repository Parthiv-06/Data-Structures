def factorial(n,fact):
    if n==1:
        print(fact)
        return 
    return factorial(n-1,fact*n)
factorial(5,1)
