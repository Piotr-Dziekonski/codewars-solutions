def find(n):
    sum = 0
    for i in range(3, n+1):
        sum += i if i % 3 == 0 or i % 5 == 0 else False  
    return sum