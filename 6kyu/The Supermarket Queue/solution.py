""" 
def queue_time(customers, n):
    tills = []
    for till in range(0, n): #creating needed amount of tills
        tills.append(0);
    sum = 0
    for customer in customers:
        foundFreeTill = 0
        for i in range(0,len(tills)):
            if tills[i] == 0:
                tills[i] = customer
                foundFreeTill = 1
                break
        if foundFreeTill == 1:
            continue
        else:
            minim = min(tills)
            if minim > customer:
                sum+=minim
                indexOfNextTill = tills.index(minim)
                for i in range(0,len(tills)):
                    tills[i] -= minim
                tills[indexOfNextTill] = customer
            elif minim <= customer:
                sum+=minim
                for i in range(0,len(tills)):
                    tills[i] -= minim
                tills[tills.index(0)] = customer
    sum+=max(tills)
    return sum
"""

def queue_time(customers, n):
    tills = [0]*n
    for customer in customers:
        tills[tills.index(min(tills))] += customer
    return max(tills)