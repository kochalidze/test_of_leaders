# 1)
# Create a program which receives a binary number and converts it to decimal.

# Examples:
# 10001 --> 17
# 1111 --> 15

def binary_to_decimal(binary_str):

    decimal_value = int(binary_str, 2)
    return decimal_value

binary_input = input("Enter a binary number: ")
decimal_output = binary_to_decimal(binary_input)

print(f"The decimal value of binary {binary_input} is: {decimal_output}")
