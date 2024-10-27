import numpy as np

def gcd(a: int, b: int) -> int:
    """
    Euclidean algorithm for GCD (greatest common divisor)

    Runtime: O(log(min(a, b)))
    """
    if b == 0:
        return a
    return gcd(b, a % b)

def stirling_number(n: int, k: int) -> int:
    """
    Stirling number of the second kind

    The number of ways to partition a set of n elements into k non-empty subsets.

    Runtime: O(n*k)

    S(n, k) = k * S(n-1, k) + S(n-1, k-1)
    Thought process:
    - If we have one fewer element but still k groups, we can add it to an existing group. There are k groups to choose from.
    - If we have one fewer element and k-1 groups, we can create a new group with it.

    Base cases:
    - S(0, 0) = 1
    - S(n, 0) = 0, n >= 1
        - We can't have 0 groups if we have elements
    """
    # bottom up
    dp = [[0] * (k + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = 0
        for j in range(1, k + 1):
            if i < j:
                dp[i][j] = 0
            elif i == j:
                dp[i][j] = 1
            else:
                dp[i][j] = j * dp[i - 1][j] + dp[i - 1][j - 1]

    return dp[n][k]

    # recursive implementation
    if n == 0 and k == 0:
        return 1
    if n == 0 or k == 0:
        return 0
    return k * stirling_number(n - 1, k) + stirling_number(n - 1, k - 1)

def fast_exp(base: int, exp: int, mod: int|None = None) -> int:
    """
    Fast exponentiation

    Runtime: O(log(exp))

    This function calculates (base^exp) % mod using the fast exponentiation algorithm.
    """
    ans = 1
    if mod is not None:
        base %= mod

    while exp:
        if exp & 1:
            ans *= base
            if mod is not None:
                ans %= mod
        base *= base
        if mod is not None:
            base %= mod
        exp >>= 1

    return ans

def matrix_exp(matrix: np.ndarray, exp: int, mod: int|None = None) -> np.ndarray:
    """
    Matrix exponentiation

    Runtime: O(log(exp) * n^3)

    This function calculates (matrix^exp) % mod using the fast exponentiation algorithm.

    Assumes that the matrix is square.
    """
    n = matrix.shape[0]
    ans = np.eye(n, dtype=int)
    if mod is not None:
        matrix %= mod

    while exp:
        if exp & 1:
            ans = ans @ matrix
            if mod is not None:
                ans %= mod
        matrix = matrix @ matrix
        if mod is not None:
            matrix %= mod
        exp >>= 1

    return ans
