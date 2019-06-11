def digital_root(n):
    sum = 0
    for x in str(n):
        sum += int(x)
    if n < 10 :
        return sum
    return digital_root(sum)