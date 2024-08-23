def gcd(a: int, b: int) -> int:
    """
    Euclidean algorithm for GCD (greatest common divisor)

    Runtime: O(log(min(a, b)))
    """
    if b == 0:
        return a
    return gcd(b, a % b)
