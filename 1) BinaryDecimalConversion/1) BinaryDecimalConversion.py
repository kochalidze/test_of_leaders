# 1)
# Create a program which receives a binary number and converts it to decimal.

# Examples:
# 10001 --> 17
# 1111 --> 15

def binary_to_decimal():
    binary =  int(input("Enter a binary number: "))
    decimal =  0
    power = 0
    for i in range(len(binary)-1, -1, -1):
        if binary[i] == '1':
            decimal += 2 ** power
            power += 1 
    
        return decimal

binary_to_decimal()