import string

def is_pangram(s):
    arr=[]
    for c in s:
        arr.append(ord(c.lower()))
    arr = list(set(arr))
    arr.sort()
    ascii = 97
    for e in arr:
        if e < 97:
            continue
        if e == 122:
            return True
        elif e == ascii:
            ascii+=1
            continue
        else:
            return False