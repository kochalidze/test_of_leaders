# N3


#  Create a function to find the missing number in a list of integers from 1 to n.

def numbers(numbers1):

    n = len(numbers1) + 1
    sum_n = n * (n + 1) // 2
    num = sum(numbers1)

    return sum_n - num

print(numbers([3, 5, 6, 1, 2]))