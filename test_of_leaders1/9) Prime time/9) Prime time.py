# Write a function that takes a maximum bound and returns all primes up to and including the maximum bound.

# For example:
# 11 => [2, 3, 5, 7, 11]

def get_primes(max_bound):
    if max_bound < 2:
        return []
    
    is_prime = [True] *  (max_bound + 1)
    is_prime[0], is_prime[1] = False, False

    for i in range(2, int(max_bound**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, max_bound + 1, i):
                is_prime[j] = False
    
    primes = [num for num, prime in enumerate(is_prime) if prime]

    return primes

result = get_primes(11)
print(result)