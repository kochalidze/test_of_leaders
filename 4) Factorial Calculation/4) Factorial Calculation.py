# 4)
# Create a program that receives a non-negative integer and returns its factorial. The factorial of a number n is the product of all positive integers from 1 to n. By definition, the factorial of 0 is 1.
# Examples:
# 5 --> 120
# 0 --> 1


def factorial():
    n = int(input('Enter  a non-negative integer: '))
    if n < 0:
        print('Error: Factorial is not defined for nagetive numbers')
    else:
        result = 1
    
    for i in range(1, n + 1):
        result *= i
    return result

factorial()
