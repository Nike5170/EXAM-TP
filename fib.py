def fibon(n):
    
    fib1 = fib2 = 1

    while n > 0:
        fib1, fib2 = fib2, fib1 + fib2
        n -= 1
    return fib2
