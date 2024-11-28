# Write a Python function that returns a list of prime numbers found in the input list.
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primes(lst):
    return [num for num in lst if is_prime(num)]
