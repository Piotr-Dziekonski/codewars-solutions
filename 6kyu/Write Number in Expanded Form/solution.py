def expanded_form(num):
    arr = []
    s = str(num)
    flag = 1
    for x in range(len(s)-1,-1,-1):        
        if s[x] != '0':
            arr.insert(0,int(s[x]) * flag)
            print(s[x])
        flag *= 10
    return ' + '.join(str(x) for x in arr)