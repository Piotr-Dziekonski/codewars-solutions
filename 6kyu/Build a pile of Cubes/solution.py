def find_nb(m):
    n = 1
    sum = 0
    while 1:
        sum += n**3
        if m == sum:
            return n
        elif sum > m:
            return -1
        else:
            n += 1