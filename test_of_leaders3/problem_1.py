# N1



# Create a function that takes a list of numbers and returns the sum of all positive numbers.

def numbers(numbers_list):

    num = 0 
    for i in numbers_list:
        if i > 0:
            num += i
        
    return num

print(numbers([1, -4, 7, 12]))

