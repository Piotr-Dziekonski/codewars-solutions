def sum_two_smallest_numbers(numbers):
    lowest = min(numbers)
    del numbers[numbers.index(lowest)]
    secondLowest = min(numbers)
    return lowest + secondLowest