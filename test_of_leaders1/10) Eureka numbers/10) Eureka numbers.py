# 10)
# The Eureka numbers are numbers like this: 135 = 1^1 + 3^2 + 5^3. Which means that we have to take a number and sum its digits raised to the consecutive powers.
# First digit to power 1, second to power 2 and so on... If the result of that sum is the same as the number itself that means that number is Eureka.

# Create a function which receives a range like (a, b) and outputs every Eureka number in it.

# NOTE: Every number which has one digit is Eureka, because for example 5 = 5^1...

# Examples:
# 1, 10  --> [1, 2, 3, 4, 5, 6, 7, 8, 9]
# 1, 100 --> [1, 2, 3, 4, 5, 6, 7, 8, 9, 89]

def  eureka_numbers(a, b):
    eureka = []

    for i in range(a, b + 1):
        digits = str(i)
        sum_of_powers = sum(int(digits[i]) ** (i + 1) for i in range(len(digits)))

        if sum_of_powers == i:
            eureka.append(i)
    return eureka

print(eureka_numbers(1, 10))
print(eureka_numbers(1, 100))