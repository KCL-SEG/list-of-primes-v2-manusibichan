"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def primes(number_of_primes):
    if number_of_primes <= 0:
        raise ValueError("Input must be a positive integer.")

    prime_list = []
    i = 2
    while len(prime_list) < number_of_primes:
        if is_prime(i):
            prime_list.append(i)
        i += 1
    return prime_list
