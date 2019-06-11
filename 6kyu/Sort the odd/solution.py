def sort_array(source_array):
    arr = []
    flag = 0
    for x in source_array:        
        if (x % 2 == 0) | (x == 0):
            arr.append([source_array.index(x), x])
    for x in arr:  
        del source_array[x[0] - flag]
        flag += 1
    source_array.sort()
    flag = 0
    for x in arr:
        source_array.insert(x[0] + flag, x[1])
    return source_array