from math import sqrt, floor

def primes(n: int) -> list[int]:
    """
    Find all prime numbers up to n, exclusive

    Runtime: O(n log log n)

    Memory: O(n)

    Args:
    - n: upper bound

    Returns:
    - list of prime numbers up to n

    This implementation uses the Sieve of Eratosthenes algorithm. We iterate through all numbers from 2 to n,
    marking all multiples of each number as non-prime. We then return all numbers that are still marked as prime.

    Note that the next number we might need to mark as non-prime is the square of the current number, since all
    smaller multiples would have already been marked by previous numbers. So, we iterate up to sqrt(n).
    """
    count = 0
    prime = [True] * n
    prime[0] = False
    prime[1] = False

    for i in range(2, floor(sqrt(n))):
        if prime[i]:
            count += 1
            for j in range(i*i, n, i):
                prime[j] = False
        
    return [i for i in range(n) if prime[i]]
