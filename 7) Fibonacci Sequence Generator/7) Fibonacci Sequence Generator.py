# 7)
# Create a program that receives an integer n and returns the first n numbers in the Fibonacci sequence. The sequence starts with 0 and 1, and each subsequent number is the sum of the previous two.
# Examples:
# 5 --> [0, 1, 1, 2, 3]
# 7 --> [0, 1, 1, 2, 3, 5, 8]

def Generator(n):

    if n <= 0:
        return []
    list = [0, 1]
    for i in range(2, n):
        next_number = list[i - 1] + list[i - 2]
        list.append(next_number)
    return list[:n]

Generator()