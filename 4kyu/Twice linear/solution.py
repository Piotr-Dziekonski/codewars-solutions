def dbl_linear(n):
    u = [1]
    a = 0
    b = 0
    for i in range(0,n):
        y = 2*u[a] +1
        z = 3*u[b] +1
        if y<z:
            u.append(y)
            a+=1
        elif y>z:
            u.append(z) 
            b+=1
        else:
            u.append(z)
            a+=1
            b+=1
    return u[n]