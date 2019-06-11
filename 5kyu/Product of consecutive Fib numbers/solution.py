def productFib(prod):
    fib = [0,1]
    x = 2
    while True:
        a = fib[x-1]
        b = fib[x-2]
        fib.append(a + b)
        if a * b == prod:
            return [b,a, True]
        elif a * b > prod:
            return [b,a, False]
        x+=1