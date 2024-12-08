# N9

#  Create a function that accepts two integers, start and end, and returns a list of all non-prime numbers 
#    within the range [start, end] (inclusive). 

def non_primes(start, end):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
            return True
        
    numbers = []

    for i in range(start, end + 1):
        if not is_prime(i):
            numbers.append(i)

    return numbers
    

print(non_primes(1, 10))

