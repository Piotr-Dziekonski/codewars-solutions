def maxSequence(arr):
    maxSum = 0
    sum = 0
    flag = 0
    for x in arr:
        for y in range(flag, len(arr)):
            sum = sum + arr[y]
            if sum > maxSum:
                maxSum = sum
        sum = 0
        flag = flag + 1
    return maxSum