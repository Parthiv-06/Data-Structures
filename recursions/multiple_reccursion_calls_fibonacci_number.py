def fibonacci_of_n(n):
    if n<=1:
        return n
    return fibonacci_of_n(n-1)+fibonacci_of_n(n-2)
print(fibonacci_of_n(6))