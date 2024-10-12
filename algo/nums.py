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
