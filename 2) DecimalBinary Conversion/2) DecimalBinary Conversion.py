# 2)
# Create a program which receives a decimal number and converts it to binary.

# Examples:
# 17 --> 10001
# 15 --> 1111
def decimal_to_binary():
    
    decimal  = int(input("Enter a decimal number: "))
    binary = ''
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal = decimal // 2
        return binary

decimal_to_binary()