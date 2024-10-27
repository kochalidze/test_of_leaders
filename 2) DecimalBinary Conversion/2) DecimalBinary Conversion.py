# 2)
# Create a program which receives a decimal number and converts it to binary.

# Examples:
# 17 --> 10001
# 15 --> 1111

def decimal_to_binary(decimal_number):
    if decimal_number < 0:
        return "Error: Please enter a non-negative integer."
    binary_number = bin(decimal_number)[2:]
    return binary_number


try:
    user_input = int(input("Enter a decimal number: "))
    binary_output = decimal_to_binary(user_input)
    print(f"{user_input} --> {binary_output}")
except ValueError:
    print("Error: Please enter a valid integer.")
